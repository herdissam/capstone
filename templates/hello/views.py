from templates import app
from flask import render_template, Blueprint, request, jsonify, Flask, redirect
from flask_sqlalchemy import SQLAlchemy

hello_blueprint = Blueprint('hello',__name__)

treshold_score = 500

@hello_blueprint.route('/')
@hello_blueprint.route('/hello')
def index():
    return render_template("index.html")

@hello_blueprint.route("/scoring", methods=["GET","POST"])
def scoring():
    if request.form:
        import pandas as pd 
        import os

        project_dir = os.path.dirname(os.path.abspath(__file__))
        data = pd.read_csv(project_dir + "/sc_cc_data.csv")

        random = data.groupby('variable').apply(pd.DataFrame.sample, n=1).reset_index(drop=True)
        score = random['points'].sum()

        print(request.form)
        print(request.form.get("income"))
        # print(scorecard.data.head())

        if score > treshold_score:
            accepted = True
            print('Selamat Pengajuan Anda Diterima')
        else:
            rejected = True
            print('Maaf Pengajuan Anda Ditolak')

    print(score)

    x = True if request.form.get("income") and request.form.get("phone") else False
    print(x)
    if x == True:
        if score > treshold_score:
            return render_template("/result.html")
        else:
            return render_template("/result.html")
    else:
        return render_template("/index.html")

    