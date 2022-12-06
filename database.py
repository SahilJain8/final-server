import pymysql

db=pymysql.connect(host='college.c32dgo5rl1oj.us-east-1.rds.amazonaws.com',user='admin',password='root1234',port=3306,database='college')

class CSEAIML:
    def insert_cse(ph,Name,ETC=None,course=None,ESC=None,pg=None):
        cur=db.cursor()

        cur.execute("INSERT INTO detail(Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse)VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ph,Name,"Mathematics for CSE","Physics for CSE Stream","Principles of Programming Using C","Communicative English","Samskrutika Kannada/Balake Kannada","Engineering Exploration",ETC,ESC,course))
        db.commit()
    def count(etc,esc):
        cur=db.cursor()
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
        engs=cur.fetchall()
        cur.execute(("select  count(EmgergingTechnologyCourse) from detail where EmgergingTechnologyCourse=%s"),(str(etc)) )
        etcs=cur.fetchall()
        return etcs[0][0],engs[0][0]


class civil:
    def insert_civil(ph,Name,ETC=None,course=None,ESC=None,pg=None):
        cur=db.cursor()

        cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"CIVIL","Mathematics for Civil Engg",
                        "Chemistry for Civil Engg Stream",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ESC,ETC,pg))


    def count_civil(esc,pgc):
        cur=db.cursor()
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
        engs=cur.fetchall()
        cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(pgc)) )
        pg=cur.fetchall()
        return pg[0][0],engs[0][0]

class Mech:
    def insert_mech(ph,Name,ETC=None,course=None,ESC=None,pg=None):
        cur=db.cursor()

        cur.execute("INSERT INTO  detail (INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s,%s,%s %s, %s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"MECH","Mathematics for MES-I","Chemistry for MES",
                        "Computer-Aided Engineering Drawing",
                        "Communicative English-I",
                        "Indian Constitution",
                        "Social Innovation",ESC,ETC,pg))

    def count_mech(esc,pgc):
        cur=db.cursor()
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
        engs=cur.fetchall()
        cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(pgc)) )
        pg=cur.fetchall()
        return pg[0][0],engs[0][0]

class EEE:
    def insert_cse(ph,Name,ETC=None,course=None,ESC=None,pg=None):
        cur=db.cursor()
        cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",( ph,Name,"EEE","Mathematics for EES-I","Chemistry for EES","Computer-Aided Engineering Drawing","Communicative English-I","Indian Constitution","Social Innovationc",ETC,ESC,pg))
        db.commit()

    def count_eee(esc,pgc):
        cur=db.cursor()
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
        engs=cur.fetchall()
        cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(pgc)) )
        pg=cur.fetchall()
        return pg[0][0],engs[0][0]

class ECE:
    def insert_cse(ph,Name,ETC=None,course=None,ESC=None,pg=None):
        cur=db.cursor()

        cur.execute("INSERT INTO  detail (Phone,name,dept,subj1,subj2,subj3,subj4,subj5,subj6,EngineeringScienceCource,EmgergingTechnologyCourse,ProgramingCourse) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (ph,Name,"ECE","Mathematics for EEE Stream-I","Physics for EEE Stream",
                                "Basic Electronics",
                                "Communicative English-I",
                                "Samskrutika Kannada/ Balake Kannada",
                                "Engineering Exploration",ESC,ETC,pg))
        db.commit()

    def count_ece(esc,pgc):
        cur=db.cursor()
        cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
        engs=cur.fetchall()
        cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(pgc)) )
        pg=cur.fetchall()
        return pg[0][0],engs[0][0]