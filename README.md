# iris_dataset_classification_streamlit 
 To run it into your system! 
 
####################################################################################################
### Step 1: Login to Github & create a Public/Private repository (without README.md file)

### Step 2: Setting up Github & Git in VSCode: 
Run following commands in VSCODE -> Project folder (that you created in your system) -> Terminal (Powershell) 
>echo "# iris_dataset_classification_streamlit" >> README.md 
>git init 
>git add README.md 
>git commit -m "first commit" 
>git branch -M main 
>git remote add origin https://github.com/priyalanile/iris_dataset_classification_streamlit.git 
>git push -u origin main 

Check by refreshing browser that Github Repository is updated now.

### Step 3: Add any .py or other files that are present in your project folder into Github: 
#'git add .' for staging the files, 
#'git commit -m "<comments>"' for any comments while committing. 
#'git push' to finally push the changes onto Github Repo 

>git add . 
>git commit -m "added classification.py and requirements.txt files" 
>git push 

### Step 4: Setting up Python Virtual Environment in VSCODE -> Project folder -> Terminal (DO preferably using CMD i.e. Command Prompt)

#To create a new environment using Conda (Anaconda installation should be in place) from Command prompt in VSCode inside your project directory. 
>conda create -p venv python==3.9 -y 

#To activate this newly created environment: (Note: Generally you get this command ready as a part of venv creation log in above step) 
>conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv 

#Output will be like: 
(C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv) C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode> 

#To deactivate this environment: 
>conda deactivate 

#Now when within the env environment, if need to install all python libraries present in requirements.txt: 
>pip install -r requirements.txt 

#To check which libraries are installed: 
>pip list 
<br></br>
### Step 5: Running Streamlit app first time: 
in VSCODE -> Project folder -> Terminal (CMD) (NOte: Don't use powershell here, else it won't work!) 
#If conda activate didn't give the directory as shown in above step, try to activate it again! 
>conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv 
>streamlit run classification.py 
#By this, the streamlit app will start running in the background and on the chrome browser.

## Step 6: When after closing streamlit app, the session doesn't close its running in VSCode: 
i) Kill the cmd/powershell terminal sessions. 
ii) create new terminal CMD session again 
iii) conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv 
iv) #cd /<folder where streamlit's main code is written, if no other directory, remain there!> 
>cd Sreamlit_Classification_Folder 
>streamlit run classification.py 
#################################################################################################### 
><br></br>
## Note: 
#No, you do not add the virtual environment folder (like venv1) to GitHub or any version control system (VCS) like Git. 
#This is because virtual environments are specific to your local machine and should not be shared or committed to version control. 
#The virtual environment can be easily recreated by others using the requirements.txt file, which lists all the dependencies your project needs. 
<br></br>
##THE END##
