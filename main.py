import pandas as pd        #weconsidered pandas as pd
import matplotlib.pyplot as plt    #considered matplots as plot
from sklearn.model_selection import train_test_split  #imported traintest from scikit's learn model
from sklearn.linear_model import LogisticRegression  #linear regressing
from sklearn.metrics import accuracy_score, confusion_matrix   #using matrix for pass fail prediction
import numpy as np  #consider numpy as np

# --- take the data from .csv that we have created using excel, i have aready mentioned the data i have used in README.md file ---
def load_data():
    df = pd.read_csv('data/student_data.csv')    #pull and load data from .csv
    
    # Create pass/fail column (1 = Pass, 0 = Fail)
    df['pass_fail'] = df['final_grade'].apply(lambda x: 1 if x >= 50 else 0)
    
    return df

# --- EDA Visualizations ---
def show_visualizations(df):  #visualization of the code is done here, matplotlib toolkit is used to plot and display a graph
    # Histogram of Grades
    plt.figure(figsize=(10, 6))
    plt.hist(df['final_grade'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Final Grade Distribution')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.savefig('grade_distribution.png')
    plt.close()
    
    # Scatter Plot: Study Hours vs Grades
    plt.figure(figsize=(10, 6))
    plt.scatter(df['study_hours'], df['final_grade'], c=df['pass_fail'], cmap='coolwarm')
    plt.title('Study Hours vs Final Grade')
    plt.xlabel('Study Hours')
    plt.ylabel('Final Grade')
    plt.colorbar(label='Pass(1)/Fail(0)')
    plt.savefig('study_vs_grade.png')
    plt.close()
    
    print("Visualizations saved as PNG files!")   #also a .png is created too to get a idea of the situation, this visualization will change as we continue to change the .csv file using excel

# --- Prediction Model ---
def train_model(df):
    # Features and Target
    X = df[['attendance', 'study_hours', 'previous_grade']]
    y = df['pass_fail']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.2f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    return model

# --- Main Function ---
def main():
    # Load data
    df = load_data()
    print("Dataset Preview:")
    print(df.head())
    
    # Show visualizations
    show_visualizations(df)
    
    # Train model
    model = train_model(df)
    
    # Interactive prediction
    print("\nPredict Pass/Fail for New Student:")
    attendance = float(input("Attendance (%): "))
    study_hours = float(input("Study Hours: "))
    prev_grade = float(input("Previous Grade: "))
    
    prediction = model.predict([[attendance, study_hours, prev_grade]])
    print("\nPrediction:", "PASS" if prediction[0] == 1 else "FAIL")

if __name__ == "__main__":
    main()
