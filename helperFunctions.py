# import modules
import unicodedata

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

def remove_neighborhood_accent(text):
    text_info = text
    text_info_byte = unicodedata.normalize('NFD', text_info).encode('ascii', 'ignore')
    return text_info_byte.decode('utf-8','ignore')