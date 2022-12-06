from db import db
from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_ECE(ph=None ,Name=None ,ETC=None,ESC=None,pg=None):
   

    cur.execute("INSERT INTO  detail (phone,name,Dept,subject1,subject2,subject3,subject4,subject5,subject6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",( ph,Name,"ECE","Mathematics for ECE","Chemistry for ECE","Computer-Aided Engineering Drawing","Communicative English-I","Indian Constitution","Social Innovation",ESC,ETC,pg))

    db.commit()
    
    return "True"


man_ece=[{"name":"22MATE11 - Mathematics for EEE Stream-I"},
{"name":"22CHEE12 - Chemistry for EES"},
{"name":"22CED13 - Computer-Aided Engineering Drawing"},
{"name":"22CE16 - Communicative English-I "},
{"name":"22IC17 - Indian Constitution"},
{"name":"22SI18 - Social Innovation"}]

