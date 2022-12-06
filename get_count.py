from db import db


cur=db.cursor()
def count(et,esc,pg):
    
    cur.execute(("select  count(EngineeringScienceCource) from detail where EngineeringScienceCource=%s"),(str(esc)) )
    engs=cur.fetchall()
    cur.execute(("select  count(EmgergingTechnologyCourse) from detail where EmgergingTechnologyCourse=%s"),(str(et)) )
    etcs=cur.fetchall()
    cur.execute(("select  count(ProgramingCourse) from detail where ProgramingCourse=%s"),(str(pg)) )
    pgs=cur.fetchall()



    return etcs[0][0],engs[0][0],pgs

