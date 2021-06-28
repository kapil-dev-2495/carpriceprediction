from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas


app=Flask(__name__)
loadedModel=pickle.load(open('car_price.pkl','rb'))

@app.route("/" ,methods=['GET'])
def Home():
    return  render_template('car_price.html')
    
    
@app.route("/predict" ,methods=['POST'])
def predict():
    year=int(request.form['Year'])
    present_price=float(request.form['Present_Price'])
    Kms_driven=int(request.form['Kms_driven'])
    Transmission=(request.form['Transmission'])
    Fuel_Type=(request.form['Fuel_Type'])

    if Transmission=="Manual":
        Transmission=1
    else:
        Transmission=0


    if Fuel_Type=="CNG":
        Petrol=0
        Diesel=0
    elif Fuel_Type=="Petrol":
        Petrol=1
        Diesel=0
    elif Fuel_Type=="Diesel":
        Petrol=0
        Diesel=1


    print("Year:",year)
    print("Present_price:",present_price)
    print("Kms_driven:",Kms_driven)
    print("Transmission:",Transmission)
    print("Fuel_Type:",Fuel_Type)

    
    prediction=loadedModel.predict([[ year,  present_price, Kms_driven,Transmission,Diesel,Petrol]])[0]

    print(prediction)
    if prediction <0:
        prediction="less than  1 "
    else:
        prediction=round(prediction,2)
    
    return render_template('car_price.html',selling_price=str(prediction)+"lakhs")
if __name__=='__main__' :
    app.run(debug=True)
    
