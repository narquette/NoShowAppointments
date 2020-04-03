# NoShowAppointments
Project Used for Capstone

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
2. Run the folling command

```sh
git clone https://github.com/narquette/NoShowAppointments CapstoneProject
```

3. Create Environment for Running Code use environment file

```sh
cd NoShowAppointments #go to directory from step 4
conda env create -f capstone_environment.yml
```
4. Add new environment to Jupyter Kernel

```sh
conda activate noshowappointments
python -m ipykernel install --user --name noshowappts --display-name "Python (noshowappts)"
```
5. Open Jupyter Notebook

```sh
jupyter notebook
```
6. [Copy URL from command line](https://www.screencast.com/t/JgVmAL6wC)

7. Run Data_Prep.ipynb

# Risk Appt Testing

No Show Prediction

1) Go to https://apptnoshow.herokuapp.com/
2) Enter in the [following values:](https://www.screencast.com/t/yXCUFfM02ZyB)
3) Press Analyze
4) View [results](https://www.screencast.com/t/MWXPI1pj83p) 




# Release History

