import pymysql
from thread import NewThreadedTask
from flask import Flask,render_template,jsonify,request,flash,redirect,url_for
from Data import *
from civil import in_civil,man_civil
from db import db
from time import sleep
from mech import in_mech,man_mech
from eee import in_EEE,man_eee
from ece import in_ECE,man_ece
from cse import in_CSE,man_cse
from get_count import count
from database import CSEAIML,Mech,civil,ECE,EEE


course_info=""

emtc=["Green Buildings",
"Introduction to Nano Technology",
"Renewable Energy Sources",
"Introduction to Internet of Things (IOT)",
"Introduction to Cyber Security"]

engscour=["Introduction to Civil Engineering" ,
 "Introduction to Electrical Engineering",
  "Introduction to Electronics Engineering",
  "Introduction to Mechanical Engineering",
  "Introduction to C Programming"
]
progcour=["Introduction to Web Programming",
 "Introduction to Python Programming ",
 "Basics of JAVA Programming",
 "Introduction to C++ Programming"
]

save={};

course_data=[{"name":"CSE"},{"name":"AIML"},{"name":"ISE"} ]#, {"name":"MECH"},{"name":"EEE"},{"name":"ECE"},{"name":"CIVIL"}]

app=Flask(__name__)
app.secret_key = "super secret key"

#set up Cursor

cursor = db.cursor()

db.autocommit( 1 )
cursor = db.cursor( pymysql.cursors.DictCursor )

cur=db.cursor()

@app.route('/')
@app.route('/index')
def home():
 
    
    for data in progcour:
        cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(data)) )
        c=cur.fetchall()
    
        save[data]=[c[0][0],120-c[0][0]]     

    for data in emtc:
        cur.execute(("select  count(EmgergingTechnologyCourse) from detail where EmgergingTechnologyCourse=%s"),(str(data)) )
        c=cur.fetchall()
        if data=="Introduction to Nano Technology":
            save[data]=[c[0][0],180-c[0][0]]
            
        elif data=="Renewable Energy Sources":
            save[data]=[c[0][0],120-c[0][0]]
           
        else:
            save[data]=[c[0][0],60-c[0][0]]         

    for data in engscour:
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(data)) )
        c=cur.fetchall()
    
        save[data]=[c[0][0],"No limit"]
        
    # print(save)

    return render_template("index.html",data=course_data,result=save)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route('/insert', methods = ['GET','POST'])
def insert():
    
   
    if request.method == "POST":
           
        
            ph=request.form['Phone']
          
            Name = request.form['Name']
            ETC= request.form.get('Emerging Technology Courses')
            ESC=request.form.get('Emerging Science Courses')
          
            cur =db.cursor()
            cur.execute("Select * from {value} where MOBILE = {number} ".format(value=course_info,number=ph))
            stud_data=cur.fetchall()
          
            if stud_data: 

            
                        
                if course_info=="CSE" or course_info=="AIML" or course_info=="ISE":
                                a,b=CSEAIML.count(etc=ETC,esc=ESC)
                                if ETC=="Renewable Energy Sources":
                                    if a>=120 :
                                        flash("Seats are full for "+(ETC)+". Choose another subject from the seats available list")
                                        return redirect(url_for("home"))
                                if ETC=="Introduction to Nano Technology":
                                    if a>=180 :
                                        flash("Seats are full for "+str(ETC)+".Choose another subject from the seats available list")
                                        return redirect(url_for("home"))
                                elif a>=1:
                                        flash("Seats are full for "+str(ETC)+". Choose another subject from the seats available list")
                                        return redirect(url_for("home"))

                else:
                                a,b=civil.count_civil(esc=ETC,pgc=ESC)
                                if a>=120:
                                    flash("Seats are full for "+str(ESC)+". Choose another subject from the seats available list")
                                    return redirect(url_for("home"))                  
                            

                            
                                    
                if course_info=="CSE":
                                            try:
                                                cur.execute("INSERT INTO detail(Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ph,Name,course_info,"Mathematics for CSE","Physics for CSE Stream","Principles of Programming Using C","Communicative English","Samskrutika Kannada/Balake Kannada","Engineering Exploration",ESC,ETC,None))
                                                db.commit()
                                                flash("Data Submited Successfully")
                                                return redirect(url_for('home'))
                                            except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                                    
                                            
                                        
                if course_info=="AIML":
                                        try: 
                                            cur.execute("INSERT INTO detail(Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse)VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ph,Name,course_info,"Mathematics for CSE","Physics for CSE Stream","Principles of Programming Using C","Communicative English","Samskrutika Kannada/Balake Kannada","Engineering Exploration",ESC,ETC,None))
                                            db.commit()
                                            flash("Data Submited Successfully")
                                                    
                                            return redirect(url_for('home'))
                                        except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                    
                                        
                if course_info=="ISE":
                                        
                                            try: 
                                                    cur.execute("INSERT INTO detail(Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse)VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ph,Name,course_info,"Mathematics for CSE","Physics for CSE Stream","Principles of Programming Using C","Communicative English","Samskrutika Kannada/Balake Kannada","Engineering Exploration",ESC,ETC,None))
                                                    db.commit()
                                                    flash("Data Submited Successfully")
                                                    
                                                    return redirect(url_for('home'))
                                            except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                    
                if course_info=="CIVIL":
                                        
                                            try:
                                                cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"CIVIL","Mathematics for Civil Engg",
                                                                "Chemistry for Civil Engg Stream",
                                                                "Computer-Aided Engineering Drawing",
                                                                "Communicative English-I",
                                                                "Indian Constitution",
                                                                "Social Innovation",ETC,None,ESC))
                                                db.commit()
                                                flash("Data Submited Successfully")
                                                        
                                                return redirect(url_for('home'))
                                            except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                            

                if course_info=="MECH":
                                            try:


                                        

                                                cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"MECH","Mathematics for MES-I","Chemistry for MES",
                                                                "Computer-Aided Engineering Drawing",
                                                                "Communicative English-I",
                                                                "Indian Constitution",
                                                                "Social Innovation",ETC,None,ESC))

                                                db.commit()
                                                flash("Data Submited Successfully")
                                                        
                                                return redirect(url_for('home'))
                                            except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                                    




                elif str(course_info)=="EEE":
                                            try:
                                                cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",( ph,Name,"EEE","Mathematics for EES-I","Chemistry for EES","Computer-Aided Engineering Drawing","Communicative English-I","Indian Constitution","Social Innovationc",ETC,None,ESC))
                                                db.commit()
                                                flash("Data Submited Successfully")
                                                return redirect(url_for('home'))  
                                            except Exception as e:
                                                flash(str(e))
                                                return redirect(url_for('home'))
                                            
                if course_info=="ECE":
                                        
                                                    
                                                try:
                                                    cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"ECE","Mathematics for ECE Stream-I","Physics for ECE Stream",
                                                    "Basic Electronics",
                                                    "Communicative English-I",
                                                    "Samskrutika Kannada/ Balake Kannada",
                                                    "Engineering Exploration",ETC,None,ESC))
            
                                                    db.commit()
                                                    flash("Data Submited Successfully")
                                    
                                    
                                    
                                    
                                                    return redirect(url_for('home'))   

                                                except Exception as e:
                                                    flash(str(e))
                                                    return redirect(url_for('home')) 
            else:
                    flash("Invalid number/Try again !")
                    return redirect(url_for('home'))                 
                
                    
            
                                        
                            



                                            
            



        
@app.route('/course', methods = ['POST'])
def course():
    if request.method=='POST':
        global course_info
        course_info= request.form.get('comp_select')
       
        if course_info=="CSE":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        
        if course_info=="AIML":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        
        if course_info=="ISE":
            return render_template("index.html",man=man_cse,head="Engineering Science Courses",main="Emerging Technology Courses",data=cs_open,EmergingTechnologyCourses=cs_pro,course=course,data_course=cs_pro,data_course_science=cs_open,c_image=True)
        if course_info=='CIVIL':
            return render_template("index.html",man=man_civil,head="Programming Language Courses-I",main="Engineering Science Courses",data=civil_open,EmergingTechnologyCourses=civil_pro,course=course,data_course=civil_pro,data_course_science=civil_open,civil_image=True)
    
        if course_info=='EEE':
            return render_template("index.html",data=eee_open,man=man_eee,head="Programming Language Courses-I",main="Engineering Science Courses",EmergingTechnologyCourses=eee_pro,course=course,data_course=eee_pro,data_course_science=eee_open,eee_img=True)

    
        if course_info=='MECH':
            return render_template("index.html",man=man_mech,data=mech_open,head="Programming Language Courses-I",main="Engineering Science Courses",EmergingTechnologyCourses=mech_pro,course=course,data_course=mech_pro,data_course_science=mech_open,mec_img=True)

        if course_info=='ECE':
            return render_template("index.html",man=man_ece,head="Engineering Science Courses",data=ece_open,main="Engineering Science Courses",EmergingTechnologyCourses=ece_pro,course=course,data_course=ece_pro,data_course_science=ece_open,ece_img=True)
        else:
            flash("Kindly select your department")
            return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True,threaded=True)
