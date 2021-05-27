from flask import Flask, redirect, render_template, url_for, request, flash, session, jsonify
import requests
import pymysql
import sys
from DB_handler import DBModule
import os

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
    return render_template("Graph.html")

# @app.route("/home/photo")
# def photo():
#     return render_template("Photo.html")
    
@app.route("/home/product")
def product():
    return render_template("Product.html")



# app.config['IMG_FOLDER'] = os.path.join('static','images')
@app.route("/home/album")
def album():
    test_db = pymysql.connect(user='root', passwd='team09', host='35.180.122.212', port=3306, db='mydb', charset='UTF8')
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

    
    