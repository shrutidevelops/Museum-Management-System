from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    return render_template("library_cds_entry.html")
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
   

    cursor=db.cursor()
    cursor.execute("INSERT INTO library_cds_entry VALUES ("+t1+","+t2+",'"+t3+"','"+t4+"','"+t5+"','"+t6+"',"+t7+",'"+t8+"','"+t9+"')")
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
    
    cursor=db.cursor()
    cursor.execute("UPDATE library_cds_entry SET cd_id="+t2+",cd_name='"+t3+"',type='"+t4+"',date_of_purchase='"+t5+"',date_of_entry='"+t6+"',amt="+t7+",purchased_from='"+t8+"',con_dept='"+t9+"' WHERE s_no="+t1+"")
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
    cursor.execute("DELETE FROM library_cds_entry WHERE s_no="+t1+"")
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
    cursor.execute("SELECT * from library_cds_entry")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cds_entry_search.html',data=data)

@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_cds_entry where s_no="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cds_entry_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_cds_entry WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cds_entry_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5011)