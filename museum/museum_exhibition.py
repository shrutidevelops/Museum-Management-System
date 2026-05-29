from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    return render_template("museum_exhibition.html")
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
   

    cursor=db.cursor()
    cursor.execute("INSERT INTO museum_exhibition VALUES ("+t1+",'"+t2+"','"+t3+"',"+t4+",'"+t5+"',"+t6+",'"+t7+"','"+t8+"')")
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
    
    cursor=db.cursor()
    cursor.execute("UPDATE museum_exhibition SET exhi_name='"+t2+"',sub='"+t3+"',hall_no="+t4+",exhi_incharge='"+t5+"',no_of_days="+t6+",date_from='"+t7+"',date_to='"+t8+"' WHERE s_no="+t1+"")
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
    cursor.execute("DELETE FROM museum_exhibition WHERE s_no="+t1+"")
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
    cursor.execute("SELECT * from museum_exhibition")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_exhibition_search.html',data=data)
@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from museum_exhibition where s_no="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_exhibition_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from museum_exhibition WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_exhibition_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5010)