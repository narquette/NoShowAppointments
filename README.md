# NoShowAppointments
Project code used for Master of Data Science Capstone Project.  

# Data Used for Analysis
1. [Healthcare](https://www.kaggle.com/joniarroba/noshowappointments/) 
2. [Weather] (https://developer.accuweather.com/user/login)
  a. The weather data was gathered using the accuweather API.
  b. The final output was merged together with the healthcare data.

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

3. Install Anaconda in Windows Sub Linux

```sh
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```

4. Change script to executable and run install file

```sh
chmod +x Anaconda3-2020.02-Linux-x86_64.sh
./Anaconda3-2020.02-Linux-x86_64.sh
```

5. Remove install file

```sh
rm Anaconda3-2020.02-Linux-x86_64.sh
```

6. Activate anaconda

```sh
source ~anaconda3/bin/activate
```

7. Update conda

```sh
conda update --all
```

8. Create Environment for Running Code use environment file

```sh
cd NoShowAppointments #go to directory from step 4
conda env create -f capstone_environment.yml
```
9. Add new environment to Jupyter Kernel

```sh
conda activate noshowappointments
python -m ipykernel install --user --name noshowappts --display-name "Python (noshowappts)"
```
10. Open Jupyter Notebook

```sh
jupyter notebook
```
11. [Copy URL from command line](https://www.screencast.com/t/JgVmAL6wC)

12. Run Data_Prep.ipynb

# Risk Appointment App Testing

No Show Prediction

1) Go to [Heroku App](https://apptnoshow.herokuapp.com/)
2) Enter in the [following values:](https://www.screencast.com/t/WopLcsUI95m)
3) Press Analyze
4) View [results](https://www.screencast.com/t/h1EpH8Pr) 




# Release History

