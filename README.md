# NoShowAppointments
This is the project code used for a [Master of Data Science Capstone Project](https://www.linkedin.com/in/nicholasarquette/).  I used healthcare data from kaggle.com (see link below) joined with weather data (see link below) to predict whether or not a patient will not show up (NoShow) for an medical appointment.  The capstone project documented on my linkedin profile will include steps I think are necessary for anyone data science to successfully implement Data Science in healthcare or other industries.

# Data Used for Analysis
1. [Healthcare](https://www.kaggle.com/joniarroba/noshowappointments/) 
2. [Weather](https://developer.accuweather.com/user/login)

The weather data was gathered using the accuweather API and merged together with the healthcare data.

# Pre-requisites

Option 1: WSL (Windows Sub-Linux)

1. Enable [WSL](https://winaero.com/blog/enable-wsl-windows-10-fall-creators-update/) in windows 
2. Install Ubuntu App from Windows Store
3. Create Login and sudo password for Linux

Option 2: Google-colab

1. Login to [google colab](https://colab.research.google.com/notebooks/welcome.ipynb)
2. Copy forked GitHub files to google colab
3. Run code 

# Getting Started 

1. Open Windows Sub Linux (Ubuntu App)

2. Run the following command

```sh
git clone https://github.com/narquette/NoShowAppointments CapstoneProject
```

3. Change install script to executable and run install file

```sh
chmod +x prereq_install.sh
./prereq_install.sh
```

4. Open Jupyter Notebook

```sh
jupyter notebook --no-browser
```
5. [Copy URL from command line](https://www.screencast.com/t/JgVmAL6wC)

6. Run Data_Prep.ipynb in Code / Python / Data Processing

# Risk Appointment App Testing

No Show Prediction

1) Go to [Heroku App](https://apptnoshow.herokuapp.com/)
2) Enter in the [following values:](https://www.screencast.com/t/xFwlA991PF)
3) Press Analyze
4) View [results](https://www.screencast.com/t/h1EpH8Pr) 


# Folder Overview

Code 
- Python
  - APITesting (local api testing)
  - Data Processing (exploratory data analysis, data cleaning, feature engineering, adding weather data)
  - Deployment (basic flask app development)
  - Final Model (run final model, save model, predict a single patient)
  - Model API (files needed to deploy application to heroku)
  - Model Evaluation (model evaluation information)

Data
- Preprocessing (original data from kaggle)
- Stage (cleaned data, test and train data)

Visualizaitons (list of exploratory reports, pandas profile report for completed dataset)

 

