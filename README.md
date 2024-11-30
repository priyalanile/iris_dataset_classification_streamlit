# Iris Flower Dataset Classification Using Random Forest Classifier:

## 1. Project Description/Highlights: 
- Uses Iris Dataset from Scikit Learn to Classify/Predict the flowers into 'setosa' 'versicolor' 'virginica' based on selected inputs.
- Allows Selecting the Inputs i.e. Sepal Length, Sepal Width, Petal Length & Petal Width by a Slider through User Interface
- Show Prediction Immediately on the UI

## 2. Project Structure: 
- .gitignore: When integrated in the VSCode, .gitignore ensures that, the python env configuration files, where we install all Python Libraries is not pushed into Github (As it's not needed and users can download while an installation).
- classification.py: This has all the project code to implement this classifier.
- requirements.txt: Contains a list of required Python packages for the project.

## 3. Learnings: 
- Git & GitHub Setup & Commands,
- VSCode Setup and Python ENV Configuration,
- Streamlit: User Interface for Quick Proof Of Concepts
- Scikit Learn Package Usage
- Model Tuning/Optimization/Validation (will be added as part of Future Implementation)

## 4. Installation: 

- 1. Clone this repository to your local machine using following OR:

```bash
git clone https://github.com/priyalanile/iris_dataset_classification_streamlit.git
```
OR: Run following commands in VSCODE -> Project folder (that you created in your system) -> Terminal (Powershell) after you've Logged in to Github & created a Public/Private repository (without README.md file). 
Later, Check by refreshing browser that Github Repository is updated now.

```bash
echo "# iris_dataset_classification_streamlit" >> README.md 
git init 
git add README.md 
git commit -m "first commit" 
git branch -M main 
git remote add origin https://github.com/priyalanile/iris_dataset_classification_streamlit.git 
git push -u origin main 
```
2. Setup the Python Environment (env) using the following commands: 



## 5. Usage: 
1. Run the Streamlit App by executing:
```bash
streamlit run classification.py
```

## 6. Possible Future Improvements: 
- To complete all Exploratory Data Analysis,
- To compare performance with Other Classifier Models,
- To implement evaluation
- To Show Image of the Flower based on prediction

----------------------------------------------------------------------------------------------

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
