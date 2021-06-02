from flask import Flask, redirect, render_template, url_for, request, flash, session, jsonify
import requests
import pymysql
import sys
from DB_handler import DBModule
import os
from flask import request
from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

#from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
import pymysql

# import database
app = Flask(__name__)


# @app.route("/")
# def login():
#     return render_template("login.html")

# # @app.route("/login_done", methods=["get"])
# # def login_done():
# #     uid = request.args.get("id")
# #     pwd = request.args.get("pwd")
# #     if DB.login(uid, pwd):
# #         session["uid"] = uid
# #         return redirect(url_for("home"))
# #     else:
# #         return redirect(url_for("login"))

# @app.route("/logout")
# def logout():
#     pass

# @app.route("/signin")
# def signin():
#     return render_template("signin.html")

# @app.route("/signin_done")
# def signin_done():
#     uid = request.args.get("id")
#     pwd = request.args.get("pwd")
#     if DB.signin(_id_=uid, pwd=pwd):
#         return redirect(url_for("home"))
#     else:
#         return redirect(url_for("signin"))

@app.route("/home")
def home():
    #graph = f"/graph_img.jpg"
    #return render_template("Home.html", graph=graph)
    return render_template("Home.html")

@app.route("/home/graph")
def graph():
    user_id ="oauth2|kakao|1750600619"
    test_db = pymysql.connect(user='root', passwd='team09', host='35.180.122.212', db='mydb', charset='utf8')
    cursor = test_db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT distinct user_face.date, prescription_data.sym_id, prescription_data.sym_name,prescription_data.symptom, prescription_data.cause, prescription_data.caution, prescription_data.solution FROM prescription_data JOIN user_face WHERE user_face.date = (select MAX(date) from user_face) and user_face.sym_id = prescription_data.sym_id  limit 3" 
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result[0]["symptom"])
    
    # sym_name =result[0]["sym_name"]
    symptoms = []
    causes = []
    cautions = []
    solutions = []
    
    # for d in result:
    #     #date = d["date"]
    #     symptom.append(d["symptom"])
    #     cause.append(d["cause"])
    #     caution.append(d['caution'])
    #     solution.append(d['solution'])
        #date = date.split()
        
        
        
    # symptom = [''.join([sol for sol in symptom if not sol.isdigit()])  ]
    # symptoms.append(symptom)
    # cause = ''.join([sol for sol in cause if not sol.isdigit()])  
    # causes.append(cause)
    # caution = ''.join([sol for sol in caution if not sol.isdigit()])
    # cautions.append(caution)
    # solution = ''.join([sol for sol in solution if not sol.isdigit()]) 
    # solutions.append(solution)               

    

    sqls = "SELECT distinct  face_detail.forehead, face_detail.cheek_R, face_detail.nose, face_detail.philtrum, face_detail.chin, face_detail.cheek_L, user_face.sym_id FROM face_detail JOIN user_face WHERE user_face.date = (select MAX(date) from user_face) and user_face.user_face_id = face_detail.user_face_id  limit 1" 
    cursor.execute(sqls)
    results = cursor.fetchall()



    return render_template("grapy.html", result=result, symptoms=symptoms, causes=causes, cautions=cautions, solutiosn=solutions, results=results) 

    
# @app.route("/home/photo")
# def photo():
#     return render_template("Photo.html")
    
@app.route("/home/product")
def product():
    return render_template("Product.html")



# app.config['IMG_FOLDER'] = os.path.join('static','images')
@app.route("/home/album")
def album():
    db = pymysql.connect(user='root', passwd='team09', host='35.180.122.212', port=3306, db='mydb', charset='UTF8')
    cursor = test_db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("set names utf8")
    cursor.execute("SELECT date, img_url1 FROM user_face")
    rows = cursor.fetchall()
    test_db.close()
    

    print(rows)
    return render_template("album.html", rows=rows)

app.config['IMG_FOLDER'] = os.path.join('static','images')
@app.route("/home/photo")
def photo():
    # import os
    # file_path = os.path.join('static','images')
    im = "im"
    
    files = os.listdir(os.path.join(app.config['IMG_FOLDER'], im))
    #files = os.path.join(file_path, files)
    #files.sort()
    # file_list = []
    # for file in files:
    #     file = os.path.join(file_path, file)
    #     file_list.append(file)

    return render_template("Photo.html", pics=files, im=im)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

    
    