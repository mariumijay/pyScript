import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Split Data into Test & Train
from sklearn.model_selection import train_test_split
# for algorithm 01
from sklearn.ensemble import RandomForestClassifier
#  for algorithm 02
from sklearn.linear_model import LogisticRegression
#  for algorithm 03
from sklearn.tree import DecisionTreeClassifier
#for evluting the model
from sklearn.metrics import classification_report, roc_auc_score ,confusion_matrix,log_loss
#convert string val into numeric val
from sklearn.preprocessing import LabelEncoder 

df = pd.read_csv("bank.csv")
print(df.head())

print("print colums : \n",df.columns)
print("print heads : \n",df.head())

# ______Preproseeing on the data
# Check missing values
print("\n______PREPROCESSING ON THE DATASET______ \n")
print("Null values in each column:\n", df.isnull().sum()) #check only missing data

# Preview clean version without missing values
print("Shape without missing data:", df.dropna().shape) #remove missing data

# Remove rows with missing data (permanently)
df.dropna(inplace=True)
print("Shape after removing missing data:", df.shape)

# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)
print("Final shape after cleaning:", df.shape)

# ______Splitting targes & features 
print("\n______SPLITTING TARGETS & FEATURES______ \n")
X = df.drop("y",axis=1) #This stores all columns except y in X as your features
print("Features: \n",X)
y = df["y"] # takes just the y column from the DataFrame and stores it in the variable y (your target/label).
print("Targets: \n",y)
#_______Convert string columns into numeric values
#import tool(label encoder for it) in libraries

le = LabelEncoder()
      
for col in X.columns:
    if X[col].dtype =="object":
     X[col] = le.fit_transform(X[col])

    if y.dtype =="object":
        y = le.fit_transform(y)  

#______Spliting the data in 80% Training & 20% Testing
print("\n ______SPLITING INTO TRAIN & TEST______ \n")
#use lib func trian_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("Shape of X_train:",X_train.shape)
print("Shape of X_test:",X_test.shape)
print("Shape of y_train:",y_train.shape)
print("Shape of y_test:",y_test.shape,"\n")

# ______Applying the models
print("\n ______CHOOSE MODEL FOR THE TRAINING______\n")

models = {
    "1": ("Random Forest Classifier", RandomForestClassifier(random_state=50)),
    "2": ("Logistic Regression", LogisticRegression(max_iter=1000, random_state=50)),
    "3": ("Decision Tree Classifier", DecisionTreeClassifier(random_state=50))
}
model_name = input("Enter the model name you want to  use : ")
if model_name in models:
   name,model = models[model_name] # unpack the tuple cuz there is no fit( ) in tuples
   print(f"YOU SELECTED : {model_name} '->' {models[model_name][0]}")
   
   print("\n______TRAIN THE MODEL______\n")
   model.fit(X_train,y_train)
   print("Model Trainings : \n ",X_train.head())
   #_______Testing the model by predictions
   print("\n______TEST THE MODEL______\n")
   y_pred =model.predict(X_test)
   print("Predictions: \n",y_pred)
   y_prob = model.predict_proba(X_test)[:,1]
   print("Probability: \n",y_prob)
   #for actual, predicted in zip(y_test, y_pred):
    #print(f"Actual: {actual} -> Predicted: {predicted}")
    #_______Evaluting the model
   print("\n______EVALUATION ON THE MODEL______\n")
   print(le.classes_)  # To confirm what 0 and 1 represent
   print("Classification report : \n ",classification_report(y_test,y_pred))
   print("ROC AUC Score : ", roc_auc_score(y_test,y_prob))
   print("Confusion Matrix :  ",confusion_matrix(y_test,y_pred))
   print("log loss :  ",log_loss(y_test,y_pred))
else:
   print("Input is Invalid.Try Again!!!")

choice = input("Do you want to print CreditWorthy & Non CreditWorthy (y/n) :")
if choice == "y":
    print("\n______CREDITWORTHY ON THE MODEL______\n")
    for i in range(900):
     status = "Creditworthy" if y_pred[i] == 1 else "Not Creditworthy"
     print(f"Sample {i+1}: {status} (Probability: {y_prob[i]:.2f})")
elif choice == "n":
     print("End Of the Excusion!!")
elif choice != "y" or choice !="n" :
   print("Invalid Input.Try Again.")     
else:
   print("Exit.")





















