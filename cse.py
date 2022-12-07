from db import db


from flask import Flask,render_template,jsonify,request,flash,redirect,url_for

cur =db.cursor()
def in_CSE(ph=None,
        Name=None ,
        ETC=None,
        ESC=None,
        course=None,pg=None):

        cur =db.cursor()
                       
        cur.execute("INSERT INTO  detail (phone,name,Dept,subject1,subject2,subject3,subject4,subject5,subject6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,course,"Mathematics for CSE","Physics for CSE Stream",
                        "Principles of Programming Using C",
                        "Communicative English",
                        "Samskrutika Kannada/Balake Kannada",
                        "Engineering Exploration",ESC,ETC,pg))
        db.commit()
        return "True"


man_cse=[{"name":"22MATS11 - Mathematics for CSE" },
{"name":"22PHYS12 - Physics for CSE Stream"},
{"name":"22POPC13 - Principles of Programming Using C"},
{"name":"22CENG16 - Communicative English - I "},
{"name":"22SKAN17 - Samskrutika Kannada/22BKAN17 Balake Kannada"},
{"name":"22EEXP18 - Engineering Exploration "}]

