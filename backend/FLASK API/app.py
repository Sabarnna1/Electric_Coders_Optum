from flask import Flask
from app_function import *

app = Flask(__name__)

# Types of allergies
@app.route('/allergies',methods = ['GET'])
def allergies():
    return(count_allergies())

# Types of health conditions
@app.route('/conditions',methods = ['GET'])
def conditions():
    return(count_conditions())

# Types of Immunizers
@app.route('/immunizer',methods = ['GET'])
def immunizer():
    return(count_immunizer())

# Types of procedures
@app.route('/procedures',methods = ['GET'])
def procedures():
    return(count_procedures())

# Sale of medicine
@app.route('/medicine',methods = ['GET'])
def medicine():
    return(count_medicine())

# Percentage of prefered insurances
@app.route('/most_prefered_insurance',methods = ['GET'])
def most_prefered_insurance():
    return(prefered_insurance())

# Payment Percentage via Insurance
@app.route('/insurance_transactions',methods = ['GET'])
def insurance_transactions():
    return(used_insurance())

@app.route('/patient_issue_count',methods = ['GET'])
def patient_issue_count():
    return(patient_health_issue_count())

# Population
@app.route('/population_info',methods = ['GET'])
def population_info():
    return(population())

if __name__=='__main__':
    app.run()