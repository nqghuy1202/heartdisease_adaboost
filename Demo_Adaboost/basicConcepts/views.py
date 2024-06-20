from django.shortcuts import render
from flask import render_template
from joblib import load
from basicConcepts.form import TestForm
model = load('./adaboost.joblib')
def predictor(request):
    return render(request, 'index.html')


def getFormInfo(request):
    result = None
    age = request.GET['age']
    sex = request.GET['gender']
    cp = request.GET['chestPain']
    trestbps = request.GET['bloodPressure']
    chol = request.GET['cholesterol']
    fbs = request.GET['bloodSugar']
    restecg = request.GET['Electrocardiographic']
    thalach = request.GET['heartRate']
    exang = request.GET['patient']
    oldpeak = request.GET['ST']
    slope = request.GET['slope']
    ca = request.GET['majorVessels']
    thal = request.GET['thailassemialLevel']
    y_pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if y_pred[0] == 0:
        y_pred = 'Bạn không bị mắc bệnh tim'
    else:
        y_pred = 'Bạn đã bị mắc bệnh tim'
    result = y_pred
    return render(request, 'index.html', {'result': result})