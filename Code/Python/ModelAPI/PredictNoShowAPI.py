#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
import numpy as np  
from tensorflow.keras.models import load_model
import joblib
import json
import os


#### THIS IS WHAT WE DO IN POSTMAN ###
# STEP 1: Create New Request
# STEP 2: Select POST
# STEP 3: Type correct URL (http://127.0.0.1:5000/api/flower)
# STEP 4: Select Body
# STEP 5: Select JSON
# STEP 6: Type or Paste in example json request
# STEP 7: Run 02-Basic-API.py to launch server and confirm the site is running
# Step 8: Run API request

def return_prediction(model,scaler,sample_json):
    
    # For larger data features, you should probably write a for loop
    # That builds out this array for you
    
    sample_values = list(sample_json.values())
        
    appt = [sample_values]
    
    appt = scaler.transform(appt)
    
    classes = np.array([0,1])
    
    class_ind = model.predict_classes(appt)
    
    return int(classes[class_ind][0])


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'


# REMEMBER TO LOAD THE MODEL AND THE SCALER!
appt_model = load_model(os.path.join('../','FinalModel','final_apptnoshow_model.h5'))
appt_scaler = joblib.load(os.path.join('../','FinalModel','apptnoshow_scaler.pkl'))

@app.route('/api/apptnoshow', methods=['POST'])
def predict_flower():

    content = request.json
    
    results = return_prediction(model=appt_model,scaler=appt_scaler,sample_json=content)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run()

