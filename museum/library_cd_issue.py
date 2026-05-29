from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT mu_libmem_id FROM library_cd_issue")  # assuming 'id' is your PK
    ids = cursor.fetchall()

    cursor.execute("SELECT cd_id FROM library_cd_issue")
    cds = cursor.fetchall()

    cursor.close()

    # Build dropdown HTML in Python
    dropdown_html = '<select name="ticket_id">'
    for row in ids:
        dropdown_html += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown_html += '</select>'

    dropdown2 = '<select name="cd_id">'
    for row in cds:
        dropdown2 += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown2 += '</select>'

    return render_template("library_cd_issue.html",dropdown=dropdown_html,dropdown2=dropdown_html)

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
    

    cursor=db.cursor()
    cursor.execute("INSERT INTO library_cd_issue VALUES ("+t1+","+t2+",'"+t3+"','"+t4+"','"+t5+"',"+t6+",'"+t7+"','"+t8+"','"+t9+"',"+t10+",'"+t11+"')")
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
    
    cursor=db.cursor()
    cursor.execute("UPDATE library_cd_issue SET cd_id="+t2+",cd_name='"+t3+"',type='"+t4+"',issued_to='"+t5+"',mu_libmem_id="+t6+",date_of_issue='"+t7+"',rec_back_date='"+t8+"',revd_back='"+t9+"',penalty="+t10+",cd_condition='"+t11+"' WHERE s_no="+t1+"")
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
    cursor.execute("DELETE FROM library_cd_issue WHERE s_no="+t1+"")
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
    cursor.execute("SELECT * from library_cd_issue")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cd_issue_search.html',data=data)

@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_cd_issue where s_no="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cd_issue_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_cd_issue WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_cd_issue_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5012)