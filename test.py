from db import db
courssssse="ECE"
ph="9606343588"
c=db.cursor()
c.execute("Select * from {value} where MOBILE = {number} ".format(value=courssssse,number="9538025014"))
d=c.fetchall()

print(d[0][6])