# Iris Flower Dataset Classification Using Random Forest Classifier: 
 @Author: Priyal Nile  

## 1. Project Description/Highlights: 
- Uses Iris Dataset from Scikit Learn to Classify/Predict the flowers into 'setosa' 'versicolor' 'virginica' based on selected inputs.
- Allows Selecting the Inputs i.e. Sepal Length, Sepal Width, Petal Length & Petal Width by a Slider through User Interface
- Show Prediction Immediately on the UI

~[StreamlitScreenshot](Iris_classification_streamlit.png)

## 2. Project Structure: 
- .gitignore: When integrated in the VSCode, .gitignore ensures that, the python env configuration files, where we install all Python Libraries is not pushed into Github (As it's not needed and users can download while an installation). Note: No, you do not add the virtual environment folder (like venv1) to GitHub or any version control system (VCS) like Git. This is because virtual environments are specific to your local machine and should not be shared or committed to version control. The virtual environment can be easily recreated by others using the requirements.txt file, which lists all the dependencies your project needs. 
- classification.py: This has all the project code to implement this classifier. 
- requirements.txt: Contains a list of required Python packages for the project.

## 3. Learnings: 
- Git & GitHub Setup & Commands,
- VSCode Setup and Python ENV Configuration,
- Streamlit: User Interface for Quick Proof Of Concepts
- Scikit Learn Package Usage
- Model Tuning/Optimization/Validation (will be added as part of Future Implementation)

## 4. Installation: 

1. Clone this repository to your local machine using following OR:

```bash
git clone https://github.com/priyalanile/iris_dataset_classification_streamlit.git
```
OR Run following commands in VSCODE -> Project folder (that you created in your system) -> Terminal (Powershell) after you've Logged in to Github & created a Public/Private repository (without README.md file). 
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
Setting up Python Virtual Environment in VSCODE -> Project folder -> Terminal (DO preferably using CMD i.e. Command Prompt)

- To create a new environment using Conda (Anaconda installation should be in place) from Command prompt in VSCode inside your project directory.

```bash
conda create -p venv python==3.9 -y 
```
- To activate this newly created environment: (Note: Generally you get this command ready as a part of venv creation log in above step)

```bash
conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv 
```

- Output will be something like: (C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv) C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode>

- Incase, you want to deactivate the environment: 

```bash
conda deactivate 
```

- Now when within the env environment, if need to install all python libraries present in requirements.txt: 

```bash
pip install -r requirements.txt 
```

- To check which libraries are installed: 
```bash
pip list 
```

## 5. Usage: 
1. Make sure the Python Environment we created is activated. 
```bash
conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv
```

2. Run the Streamlit App within directory where classification.py file is present (having streamlit code within it) by executing:

```bash
streamlit run classification.py
```

## 6. Possible Future Improvements In this Project: 
- To complete all Exploratory Data Analysis,
- To compare performance with Other Classifier Models,
- To implement evaluation
- To Show Image of the Flower based on prediction

----------------------------------------------------------------
----------------------------------------------------------------

### Additional Notes on Git/VSCode/Bugs Issues:

1. To Add any .py or other files that are present in your project folder into GitHub Repo:
For staging multiple files:
```bash
git add . 
```
For commiting the files to make them ready to push into GitHub repo:
```bash
git commit -m "<comments>"
```
To finally push the changes onto GitHub Repo: 
```bash
git push 
```

2. When after closing streamlit app in browser, the VSCode command (CMD) session doesn't close (Bug): 
i) Kill the cmd/powershell terminal sessions manually.
ii) create a new terminal CMD session again 
iii) Again Activate the Python Env.
```bash
conda activate C:\Users\priya\VS_Code_Projects\4_IRIS_Dataset_Classification_VSCode\venv
```
iv) cd /<folder where streamlit's main code is written, if no other directory, remain there!> 
```bash 
streamlit run classification.py
```

