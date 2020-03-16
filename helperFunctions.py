# import modules
import unicodedata
import os
import pandas as pd

# build function to determine if the appointment is the same day
def same_day_appt(sched_day,appt_day):
    is_same_day = 0
    if sched_day.date() == appt_day.date():
      is_same_day = 1
    return is_same_day

# return the day name for the appointment day
def appt_day_name(appt_day):
    return appt_day.day_name()

# return the time of day when the appointments was scheduled
def scheduled_time_of_day(date):
  time = ""
  if date.hour < 12:
    time = "Morning" 
  elif 12 <= date.hour <= 15 :
    time = "Afternoon"
  else:
    time = "Evening"
  return time

# remove the accent letters from neighborhood
def remove_neighborhood_accent(text):
    text_info = text
    text_info_byte = unicodedata.normalize('NFD', text_info).encode('ascii', 'ignore')
    return text_info_byte.decode('utf-8','ignore')


def add_weather_data(data):
    
    #get weather data
    weather_data = pd.read_csv(os.path.join('Data','Preprocessing','BrazilWeatherData_Vitario_2016_2019.csv'),sep='|',low_memory=False)

    #add weather date to data
    weather_data['WeatherDate'] = weather_data.apply(lambda x:'%s/%s/%s' % (int(x['WeatherYear']),int(x['WeatherMonth']), int(x['WeatherDay'])),axis=1)
    
    #convert weather date to a datetime with UTC format
    weather_data['WeatherDate'] = pd.to_datetime(weather_data['WeatherDate'],utc=True)
    
    #create a dictionary to store rain information
    weather_dict = dict(zip(weather_data['WeatherDate'],weather_data['Rain Classification']))
    
    #add it to appointment data
    data['RainClassification'] = data.apply(lambda x: weather_dict.get(x['AppointmentDay']),axis=1)
    
    #cut dataframe by buckets and labels
    #anything under -1 will be listed as below
    #anything equal to 0 will be listed as same
    #anything over 1 will be listed as a over
    buckets = [weather_data['Actual - Normal Avg Difference'].min(), -1, 1, weather_data['Actual - Normal Avg Difference'].max()]
    buckets_name = ['below', 'same', 'above']
    weather_data['ActualAvgMinusNormalAvg'] = pd.cut(weather_data['Actual - Normal Avg Difference'], buckets , labels = buckets_name)
    
    #create a dictionary to store the information actual versus normal average
    weather_avgcomparison_dict = dict(zip(weather_data['WeatherDate'],weather_data['ActualAvgMinusNormalAvg']))
    
    #add new column to appointment data
    data['NormalVersusActualTempAverage'] = data.apply(lambda x: weather_avgcomparison_dict.get(x['AppointmentDay']),axis=1)
    
    return data
    