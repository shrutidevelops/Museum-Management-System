from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():

    cursor = db.cursor()
    cursor.execute("SELECT mu_mem_id FROM museum_master")  # assuming 'id' is your PK
    ids = cursor.fetchall()

    cursor.execute("SELECT mu_libmem_id FROM museum_master")
    cds = cursor.fetchall()

    cursor.close()

    # Build dropdown HTML in Python
    dropdown_html = '<select name="mu_mem_id">'
    for row in ids:
        dropdown_html += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown_html += '</select>'

    dropdown2 = '<select name="mu_libmem_id">'
    for row in cds:
        dropdown2 += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown2 += '</select>'

    return render_template("museum_master.html",dropdown=dropdown_html,dropdown2=dropdown_html)

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
    cursor.execute("INSERT INTO museum_master VALUES ("+t1+",'"+t2+"','"+t3+"','"+t4+"','"+t5+"',"+t6+",'"+t7+"','"+t8+"',"+t9+","+t10+","+t11+",'"+t12+"')")
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
    cursor.execute("UPDATE museum_master SET antiq_name='"+t2+"',doreg='"+t3+"',museum_condition='"+t4+"',source='"+t5+"',estimated_cost="+t6+",con_dept='"+t7+"',con_person='"+t8+"',mu_mem_id="+t9+",mu_libmem_id="+t10+",tkt_no="+t11+",tkt_type='"+t12+"' WHERE an_id="+t1+"")
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
    cursor.execute("DELETE FROM museum_master WHERE an_id="+t1+"")
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
    cursor.execute("SELECT * from museum_master")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_master_search.html',data=data)
@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from museum_master where an_id="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_master_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from museum_master WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('museum_master_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5004)