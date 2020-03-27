#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, DateField, SelectField, StringField
from wtforms.validators import NumberRange, DataRequired, InputRequired
import numpy as np  
import datetime
from tensorflow.keras.models import load_model
import joblib
import json
import os

def return_prediction(model,scaler,sample_json):
    
    # For larger data features, you should probably write a for loop
    # That builds out this array for you
    
    sample_values = list(sample_json.values())
        
    appt = [sample_values]
    
    appt = scaler.transform(appt)
    
    classes = np.array([0,1])
    
    class_dict = {0:"No",1:"Yes"}
    
    class_ind = model.predict_classes(appt)
    
    resp = int(classes[class_ind][0])
    
    return (f"{resp} which is {class_dict.get(resp)}")


app = Flask(__name__)

# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# REMEMBER TO LOAD THE MODEL AND THE SCALER!
appt_model = load_model('final_apptnoshow_model.h5')
appt_scaler = joblib.load('apptnoshow_scaler.pkl')

class ApptForm(FlaskForm):
    scholarship = SelectField("Scholarship: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    hypertension = SelectField("Hypertension: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    diabetes = SelectField("Diabetes: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    alcoholism = SelectField("Alcoholism: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    handicap = SelectField("Handicap: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    sms = SelectField("SMS: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    samedayappt = SelectField("Same Day Appointment: ", coerce=int, choices=[(0, "No"), (1, "Yes")], default=0)
    gender = SelectField("Gender: ", choices=[("F", "Female"), ("M", "Male")], default="F")
    agegroup = SelectField("Age Group: ", coerce=int, choices=[(0, "Baby/Toddler"), (1, "Child"), (2, "Adult"),(3, "Elderly")], default=2)
    neighborhood = SelectField("Neighborhood: ", coerce=int, choices=[(0, 'AEROPORTO'),
 (1, 'ANDORINHAS'),
 (2, 'ANTONIO HONORIO'),
 (3, 'ARIOVALDO FAVALESSA'),
 (4, 'BARRO VERMELHO'),
 (5, 'BELA VISTA'),
 (6, 'BENTO FERREIRA'),
 (7, 'BOA VISTA'),
 (8, 'BONFIM'),
 (9, 'CARATOIRA'),
 (10, 'CENTRO'),
 (11, 'COMDUSA'),
 (12, 'CONQUISTA'),
 (13, 'CONSOLACAO'),
 (14, 'CRUZAMENTO'),
 (15, 'DA PENHA'),
 (16, 'DE LOURDES'),
 (17, 'DO CABRAL'),
 (18, 'DO MOSCOSO'),
 (19, 'DO QUADRO'),
 (20, 'ENSEADA DO SUA'),
 (21, 'ESTRELINHA'),
 (22, 'FONTE GRANDE'),
 (23, 'FORTE SAO JOAO'),
 (24, 'FRADINHOS'),
 (25, 'GOIABEIRAS'),
 (26, 'GRANDE VITORIA'),
 (27, 'GURIGICA'),
 (28, 'HORTO'),
 (29, 'ILHA DAS CAIEIRAS'),
 (30, 'ILHA DE SANTA MARIA'),
 (31, 'ILHA DO BOI'),
 (32, 'ILHA DO FRADE'),
 (33, 'ILHA DO PRINCIPE'),
 (34, 'ILHAS OCEANICAS DE TRINDADE'),
 (35, 'INHANGUETA'),
 (36, 'ITARARE'),
 (37, 'JABOUR'),
 (38, 'JARDIM CAMBURI'),
 (39, 'JARDIM DA PENHA'),
 (40, 'JESUS DE NAZARETH'),
 (41, 'JOANA DARC'),
 (42, 'JUCUTUQUARA'),
 (43, 'MARIA ORTIZ'),
 (44, 'MARIO CYPRESTE'),
 (45, 'MARUIPE'),
 (46, 'MATA DA PRAIA'),
 (47, 'MONTE BELO'),
 (48, 'MORADA DE CAMBURI'),
 (49, 'NAZARETH'),
 (50, 'NOVA PALESTINA'),
 (51, 'PARQUE INDUSTRIAL'),
 (52, 'PARQUE MOSCOSO'),
 (53, 'PIEDADE'),
 (54, 'PONTAL DE CAMBURI'),
 (55, 'PRAIA DO CANTO'),
 (56, 'PRAIA DO SUA'),
 (57, 'REDENCAO'),
 (58, 'REPUBLICA'),
 (59, 'RESISTENCIA'),
 (60, 'ROMAO'),
 (61, 'SANTA CECILIA'),
 (62, 'SANTA CLARA'),
 (63, 'SANTA HELENA'),
 (64, 'SANTA LUCIA'),
 (65, 'SANTA LUIZA'),
 (66, 'SANTA MARTHA'),
 (67, 'SANTA TEREZA'),
 (68, 'SANTO ANDRE'),
 (69, 'SANTO ANTONIO'),
 (70, 'SANTOS DUMONT'),
 (71, 'SANTOS REIS'),
 (72, 'SAO BENEDITO'),
 (73, 'SAO CRISTOVAO'),
 (74, 'SAO JOSE'),
 (75, 'SAO PEDRO'),
 (76, 'SEGURANCA DO LAR'),
 (77, 'SOLON BORGES'),
 (78, 'TABUAZEIRO'),
 (79, 'UNIVERSITARIO'),
 (80, 'VILA RUBIM')], default=0)
    apptday = SelectField("Appointment Day of Week: ", coerce=int, choices=[(0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"), (4, "Friday"), (5, "Saturday")], default=0)
    schedTimeOfDay = SelectField("Scheduled Time of Day: ", coerce=int, choices=[(0, "Morning"), (1, "Afternoon"), (2, "Evening")], default=0)
    rainclass = SelectField("Raining: ", coerce=int, choices=[(0, "No Rain"), (1, "Light Rain"), (2, "Heavy Rain")], default=0)
    normvsact = SelectField("Normal Versus Actual Temp Average: ", choices=[("below", "Below Normal"), ("same", "Normal"), ("above", "Above Normal")], default="same")
    missedappt = StringField("Missed Appointment Amount:", [InputRequired()], default=0)    
    submit = SubmitField('Analyze')
    

@app.route('/',methods=['GET', 'POST'])
def index():
    
    # Create instance of the form.
    
    form = ApptForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['scholarship'] = form.scholarship.data
        session['hypertension'] = form.hypertension.data
        session['diabetes'] = form.diabetes.data
        session['alcoholism'] = form.alcoholism.data
        session['handicap'] = form.handicap.data   
        session['sms'] = form.sms.data
        session['samedayappt'] = form.samedayappt.data
        session['gender'] = form.gender.data
        session['agegroup'] = form.agegroup.choices[form.agegroup.data][1]
        session['neighborhood'] = form.neighborhood.choices[form.neighborhood.data][1]
        session['apptday'] = form.apptday.choices[form.apptday.data][1]
        session['schedTimeOfDay'] = form.schedTimeOfDay.choices[form.schedTimeOfDay.data][1]
        session['rainclass'] = form.rainclass.data + 1
        session['normvsact'] = form.normvsact.data
        session['missedappt'] = form.missedappt.data

        return redirect(url_for("prediction"))

    print(form.errors)
    
    return render_template('home.html', form=form)

@app.route('/prediction')
def prediction():

    
    cols = ['Scholarship',
 'Hypertension',
 'Diabetes',
 'Alcoholism',
 'Handicap',
 'SMSReceived',
 'SameDayAppointment',
 'Gender_F',
 'Gender_M',
 'Age Group_Toddler/baby',
 'Age Group_Child',
 'Age Group_Adult',
 'Age Group_Elderly',
 'Neighborhood_AEROPORTO',
 'Neighborhood_ANDORINHAS',
 'Neighborhood_ANTONIO HONORIO',
 'Neighborhood_ARIOVALDO FAVALESSA',
 'Neighborhood_BARRO VERMELHO',
 'Neighborhood_BELA VISTA',
 'Neighborhood_BENTO FERREIRA',
 'Neighborhood_BOA VISTA',
 'Neighborhood_BONFIM',
 'Neighborhood_CARATOIRA',
 'Neighborhood_CENTRO',
 'Neighborhood_COMDUSA',
 'Neighborhood_CONQUISTA',
 'Neighborhood_CONSOLACAO',
 'Neighborhood_CRUZAMENTO',
 'Neighborhood_DA PENHA',
 'Neighborhood_DE LOURDES',
 'Neighborhood_DO CABRAL',
 'Neighborhood_DO MOSCOSO',
 'Neighborhood_DO QUADRO',
 'Neighborhood_ENSEADA DO SUA',
 'Neighborhood_ESTRELINHA',
 'Neighborhood_FONTE GRANDE',
 'Neighborhood_FORTE SAO JOAO',
 'Neighborhood_FRADINHOS',
 'Neighborhood_GOIABEIRAS',
 'Neighborhood_GRANDE VITORIA',
 'Neighborhood_GURIGICA',
 'Neighborhood_HORTO',
 'Neighborhood_ILHA DAS CAIEIRAS',
 'Neighborhood_ILHA DE SANTA MARIA',
 'Neighborhood_ILHA DO BOI',
 'Neighborhood_ILHA DO FRADE',
 'Neighborhood_ILHA DO PRINCIPE',
 'Neighborhood_ILHAS OCEANICAS DE TRINDADE',
 'Neighborhood_INHANGUETA',
 'Neighborhood_ITARARE',
 'Neighborhood_JABOUR',
 'Neighborhood_JARDIM CAMBURI',
 'Neighborhood_JARDIM DA PENHA',
 'Neighborhood_JESUS DE NAZARETH',
 'Neighborhood_JOANA DARC',
 'Neighborhood_JUCUTUQUARA',
 'Neighborhood_MARIA ORTIZ',
 'Neighborhood_MARIO CYPRESTE',
 'Neighborhood_MARUIPE',
 'Neighborhood_MATA DA PRAIA',
 'Neighborhood_MONTE BELO',
 'Neighborhood_MORADA DE CAMBURI',
 'Neighborhood_NAZARETH',
 'Neighborhood_NOVA PALESTINA',
 'Neighborhood_PARQUE INDUSTRIAL',
 'Neighborhood_PARQUE MOSCOSO',
 'Neighborhood_PIEDADE',
 'Neighborhood_PONTAL DE CAMBURI',
 'Neighborhood_PRAIA DO CANTO',
 'Neighborhood_PRAIA DO SUA',
 'Neighborhood_REDENCAO',
 'Neighborhood_REPUBLICA',
 'Neighborhood_RESISTENCIA',
 'Neighborhood_ROMAO',
 'Neighborhood_SANTA CECILIA',
 'Neighborhood_SANTA CLARA',
 'Neighborhood_SANTA HELENA',
 'Neighborhood_SANTA LUCIA',
 'Neighborhood_SANTA LUIZA',
 'Neighborhood_SANTA MARTHA',
 'Neighborhood_SANTA TEREZA',
 'Neighborhood_SANTO ANDRE',
 'Neighborhood_SANTO ANTONIO',
 'Neighborhood_SANTOS DUMONT',
 'Neighborhood_SANTOS REIS',
 'Neighborhood_SAO BENEDITO',
 'Neighborhood_SAO CRISTOVAO',
 'Neighborhood_SAO JOSE',
 'Neighborhood_SAO PEDRO',
 'Neighborhood_SEGURANCA DO LAR',
 'Neighborhood_SOLON BORGES',
 'Neighborhood_TABUAZEIRO',
 'Neighborhood_UNIVERSITARIO',
 'Neighborhood_VILA RUBIM',
 'AppointmentDayOfWeek_Friday',
 'AppointmentDayOfWeek_Monday',
 'AppointmentDayOfWeek_Saturday',
 'AppointmentDayOfWeek_Thursday',
 'AppointmentDayOfWeek_Tuesday',
 'AppointmentDayOfWeek_Wednesday',
 'ScheduledTimeOfDay_Afternoon',
 'ScheduledTimeOfDay_Evening',
 'ScheduledTimeOfDay_Morning',
 'RainClassification_1',
 'RainClassification_2',
 'RainClassification_3',
 'NormalVersusActualTempAverage_above',
 'NormalVersusActualTempAverage_below',
 'NormalVersusActualTempAverage_same',
 'NoShowSum']

    zero_data = np.zeros(len(cols),dtype=int)
    zero_dict = dict(zip(cols,zero_data))  
    zero_dict['Scholarship'] = session['scholarship'] 
    zero_dict['Hypertension'] = session['hypertension']
    zero_dict['Diabetes'] = session['diabetes'] 
    zero_dict['Alcoholism'] = session['alcoholism'] 
    zero_dict['Handicap'] = session['handicap'] 
    zero_dict['SMSReceived'] = session['sms'] 
    zero_dict['SameDayAppointment'] = session['samedayappt'] 
    zero_dict[f"Gender_{session['gender']}"] = 1 
    zero_dict[f"Age Group_{session['agegroup']}"] = 1
    zero_dict[f"Neighborhood_{session['neighborhood']}"] = 1 
    zero_dict[f"AppointmentDayOfWeek_{session['apptday']}"] = 1  
    zero_dict[f"ScheduledTimeOfDay_{session['schedTimeOfDay']}"] = 1 
    zero_dict[f"RainClassification_{session['rainclass']}"] = 1 
    zero_dict[f"NormalVersusActualTempAverage_{session['normvsact']}"] = 1
    zero_dict['NoShowSum'] = session['missedappt'] 
              
    zero_dict = {k:int(v) for k,v in zero_dict.items()}

    data_dict = json.dumps(zero_dict)
    data_dict = json.loads(data_dict)
   
    results = return_prediction(model=appt_model,scaler=appt_scaler,sample_json=data_dict)
    
    return render_template('prediction.html',results=results)

if __name__ == '__main__':
    app.run(debug=True)

