from flask import Flask , request
import pickle
import sklearn
import os

app = Flask(__name__)
#model_pickle = open(r"C:\Users\satheeskumar\Documents\MLOPS\Flask\artefacts\classifier.pkl", "rb")
#model_pickle = os.path.join(os.path.dirname(__file__), "artefacts", "classifier.pkl")
#model_pickle = os.path.join(os.getcwd(), "artefacts", "classifier.pkl")

with open("artefacts/classifier.pkl", "rb") as model_file:
    clf = pickle.load(model_file) 

#clf = pickle.load(model_pickle)

@app.route("/hello", methods = ["GET"])
def welcome_page():
    return "<h1> welcome to LOAN TAP!!</h2>"

@app.route("/fill", methods = ["GET"])
def first_page():
    return "<h1> fill your details</h2>"

@app.route("/predict", methods = ["POST"])
def prediction():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
            Gender = 0
    else:
            Gender = 1

    if loan_req['Married'] == "No":
            Married = 0
    else:
            Married = 1
        
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    if loan_req["Credit_History"] == "Unclear Debts":
           Credit_History = 0
    else:
           Credit_History = 1   

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]
    result = clf.predict([input_data])
        
    if result == 0:
            pred = "Rejected"
    else:
            pred = "Approved"


    return {"loan_approval_status":pred}

