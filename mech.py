from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_mech(ph=None,
       
        Name=None ,
        ETC=None,
        ESC=None,
        pg=None):
   cur.execute("INSERT INTO  detail (phone,name,Dept,subject1,subject2,subject3,subject4,subject5,subject6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"MECH","Mathematics for Mechanical Engg","Chemistry for Mechanical Engg Stream",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ESC,ETC,pg))

   db.commit()
    
   return "True"

man_mech=[{"name":"22MATM11 - Mathematics for MES-I"},{"name":"22CHEM12 - Chemistry for MES"},{"name":"22CED13 - Computer-Aided Engineering Drawing"},{"name":"22CE16 - Communicative English-I "},{"name":"22IC17 - Indian Constitution"},{"name":"22SI18 - Social Innovation"}]
