# NoShowAppointments
Project Used for Capstone

# Pre-requisites

WSL (Windows Sub-Linux)

1. Enable [WSL](https://winaero.com/blog/enable-wsl-windows-10-fall-creators-update/) in windows 
2. Install Ubuntu App from Windows Store
3. Create Login and sudo password for Linux

# Getting Started 

1. Fork Github Repository
2. Copy Files to a Local Directory
3. Make a directory in WSL

```sh
mkdir AppointmentNoShow
```

4. Copy Files to new directory

/mnt/c is the same as your C: drive on windows

```sh
cp -r /mnt/c/users/narquette/Dropbox/Personal/School/DataScience_Capstone/NoShowAppointments/ .
```

***You won't be able to copy and paste a directory from Windows to you Linux virtual machine

5. Create Environment for Running Code use environment file

```sh
cd NoShowAppointments #go to directory from step 4
conda env create -f capstone_environment.yml
```
6. Open Jupyter Notebook

```sh
conda activate noshowappts
jupyter notebook
```
7. Copy URL from command line

8. Run Data_Prep.ipynb


# Release History

