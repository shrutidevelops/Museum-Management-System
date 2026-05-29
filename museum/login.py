from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    return render_template("login.html")
@app.route("/login",methods=["POST"])
def login():
    t1=request.form["t1"]
    t2=request.form["t2"]
    cursor=db.cursor()
    cursor.execute("SELECT * from login")
    data=cursor.fetchall()
    f=0
    for col in data:
        if(col[0]==t1 and col[1]==t2):
            f=1
    cursor.close()
    if(f==1):
        return """<script>window.open("http://127.0.0.1:5020")</script>"""
    else:
        return """<script>alert("Invalid ID or Password")</script>"""
    return ""
   
if __name__=="__main__":
    app.run(debug=True,port=5019)
