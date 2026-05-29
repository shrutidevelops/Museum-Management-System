from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    return render_template("sculpture.html")
@app.route("/save",methods=["POST"])
def save():
    t1=request.form["t1"]
    t2=request.form["t2"]
    t3=request.form["t3"]
    t4=request.form["t4"]
    t5=request.form["t5"]
    t6=request.form["t6"]
    t7=request.form["t7"]
    t8=request.form["t8"]
    t9=request.form["t9"]
    t10=request.form["t10"]
    t11=request.form["t11"]
    t12=request.form["t12"]

    cursor=db.cursor()
    cursor.execute("INSERT INTO sculpture VALUES ("+t1+",'"+t2+"','"+t3+"','"+t4+"',"+t5+","+t6+","+t7+",'"+t8+"','"+t9+"','"+t10+"','"+t11+"','"+t12+"')")
    db.commit()
    cursor.close()
    return """
    <script>
        alert("Record saved successfully!");
        window.location.href = "/";
    </script>
    """

@app.route("/update",methods=["POST"])
def update():
    t1=request.form["t1"]
    t2=request.form["t2"]
    t3=request.form["t3"]
    t4=request.form["t4"]
    t5=request.form["t5"]
    t6=request.form["t6"]
    t7=request.form["t7"]
    t8=request.form["t8"]
    t9=request.form["t9"]
    t10=request.form["t10"]
    t11=request.form["t11"]
    t12=request.form["t12"]

    
    cursor=db.cursor()
    cursor.execute("UPDATE sculpture SET name='"+t2+"',topic='"+t3+"',color='"+t4+"',weight="+t5+",height="+t6+",width="+t7+",artist_name='"+t8+"',sculpture_condition='"+t9+"',rel_period='"+t10+"',con_dept="+t11+",con_person='"+t12+"' WHERE an_id="+t1+"")
    db.commit()
    cursor.close()
    return """
    <script>
        alert("Record updated successfully!");
        window.location.href = "/";
    </script>
    """

@app.route("/delete",methods=["POST"])
def delete():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("DELETE FROM sculpture WHERE an_id="+t1+"")
    db.commit()
    cursor.close()
    return """
    <script>
        alert("Record deleted successfully!");
        window.location.href = "/";
    </script>
    """
@app.route("/allsearch",methods=["POST"])
def allsearch():
    cursor=db.cursor()
    cursor.execute("SELECT * from sculpture")
    data=cursor.fetchall()
    cursor.close()
    return render_template('sculpture_search.html',data=data)
@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from sculpture where an_id="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('sculpture_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from sculpture WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('sculpture_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5018)