from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/likes', methods=['POST','GET'])


def index():

    {
    'error' : error,
    'data': names,
    'error_mesagge': error_mesage,


    return render_template("index.html", data=data, ganre= ganre, naz1=naz1, naz3=naz3, year= year, naz=naz, naz2=naz2)






if __name__ == "__main__":
    app.run(debug=False)