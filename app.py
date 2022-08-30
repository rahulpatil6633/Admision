from flask import Flask,request,jsonify
import config
import numpy as np
from project_app.utils import Admission 

app=Flask(__name__)
@app.route('/')

def hello_flask():
    return 'welcome'

@app.route('/admission')

def get_adm():
    data=request.form
    GRE_Score=eval(data['GRE_Score'])
    TOEFL_Score=eval(data['TOEFL_Score'])
    University_Rating=eval(data['University_Rating'])
    SOP=eval(data['SOP'])
    LOR=eval(data['LOR'])
    CGPA=eval(data['CGPA'])
    Research=eval(data['Research'])
    
    adm=Admission(GRE_Score,TOEFL_Score,University_Rating,SOP,LOR,CGPA,Research)
    result=adm.get_admission()
    return jsonify({'result':f" {result}"})


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)