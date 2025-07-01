Technical Thesis: Student Performance Analyzer
A Machine Learning  and EDA Approach to Predicting Academic Success  (⁠ʘ⁠ᴗ⁠ʘ⁠⁠)

---------------------------------------------------------------------------------------------

CORE OF MY PROJECT  (⁠◠⁠‿⁠・⁠)⁠—⁠☆   :

I developed Student Performance Analyzer that predicts academic outcomes (pass/fail or final grades) based on student-related features such as attendance, study hours, and previous grades. The system uses Python, Pandas, Scikit-learn, and Matplotlib to preprocess data, perform exploratory analysis, and train machine learning models. The goal is to provide educators with actionable insights to improve student success rates.

Here the version of pandas, numpy, scikitlrn and matplot lib used are :
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
numpy==1.25.2


---------------------------------------------------------------------------------------------


Problem Statement   🤔  :
Institutions struggle to identify at-risk students early. Traditional methods rely on manual analysis, which is lenghty and subjective. This project automates performance prediction using a very simple machine learning model, enabling data-driven outcomes .

1.2 Objectives 
Analyze student data (grades, attendance, study habits).

Predict pass/fail outcomes using classification already provided .csv data sheet from excel.

Generate visual insights for educators in a form of .png for grade distribution and also grade vs study graph too 📈📉📊

Deploy a model for academic institutions.

---------------------------------------------------------------------------------------------

Data Collection & Preprocessing :
Dataset: (student_data.csv) containing:
student_id, attendance, study_hours, previous_grade, final_grade

---------------------------------------------------------------------------------------------

Graphs and Plots 📉📈:

Exploratory Data Analysis (EDA)
Visualizations generated:

Grade Distribution Histogram

Shows frequency of grades to identify trends (e.g., grade clustering).

Study Hours vs. Final Grade Scatter Plot

Correlates study with performance.


----------------------------------------------------------------------------------


Machine Learning Model
Algorithm: Logistic Regression (binary classification)

Features: attendance, study_hours, previous_grade.

Target: pass_fail (1/0).

here if marks>=50 then 1 ie;pass/else 0(fail) (●'◡'●)

Train-Test Split: 80-20 ratio.

Evaluation Metrics:
1)Accuracy
2)Confusion Matrix


-------------------------------------------------------------------------


Tools & Libraries  🔨
Tool/Library	  |       Purpose
================================================
Python 3.8+       |  	Core programming language
Pandas	          |      Data manipulation
Scikit-learn	  |     Model training & evaluation
Matplotlib	      |      Data visualization
NumPy	          |     Numerical operations








--------------------------------------------------------------------



Process from scratch⛏️  :

1) Here i used visual studio 2022, with python 3.11.9 version.
2) a folder is created naming it as student acedamic predictions.
3) 1 more folder is created naming it as data, while inside this folder there  is .csv file created using excel, in this excel csv file we have data as :  student_id,attendance,study_hours,previous_grade,final_grade
1,90,5,72,75
2,65,2,48,45
3,80,4,68,70
4,40,1,30,28
5,95,7,85,88
6,75,3,60,62
7,50,1,55,50
8,85,6,78,80
9,30,0,35,30
10,100,8,90,92

4) A text file is created naming it as requirements.txt, where these versions of toolkits are placed with pip install function :  pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.2
numpy==1.24.3

5) Opening folder wrt visual studio code, and also opening terminal, inside terminal i have directly pulled thenrequirements.txt content for quick initialization of toolkits, by using     (pip install -r requirements.txt)
[SOME MATPLOTLIB VERSIONS ARE NOT COMPATIBLE WITH NUMPYS AND OTHER TOOLKITS]
also Set-ExecutionPolicy RemoteSigned -Scope CurrentUser command is used in admins powershell to let scripts run smoothly.

7) Making of environment is done by using Windows (CMD/PowerShell)
.\student-env\Scripts\activate COMMAND USED FIRST TO MAKE THE ENVIRONTMENT and then to activate it student-env\Scripts\activate command in PS or CP or even in terminal is used.
[HERE, MAKING OF ENVIRONMENT IS DONE BEFORE INSTALLING THE TOOLKITS]
Extra files will be created into the main folder named as SCRIPTS due to usage of above student-env commands


9) create .py:
   create a file named, python main.py into the maing folder




----TILL HERE WE HAVE CREATED ALL THE REQUIRED SETUPS TO RUN THIS PROJECT⚙️🛠️, SO NOW WE ARE READY TO CODE IN main.py that we previously created.---




HOW YOUR MAIN FOLDER MUST LOOK LIKE AFTER DOING ALL THE ABOVE STEPS CORRECTLY :



student_performance_analyzer/
├── data/
│   └── student_data.csv   # Sample dataset
├── main.py                # Main application
└── requirements.txt










































































Go to main.py
