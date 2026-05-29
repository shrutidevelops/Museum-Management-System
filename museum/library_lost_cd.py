from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():
    
    cursor = db.cursor()
    cursor.execute("SELECT cd_id FROM library_lost_cd")  # assuming 'id' is your PK
    ids = cursor.fetchall()
    cursor.close()

    # Build dropdown HTML in Python
    dropdown_html = '<select name="cd_id">'
    for row in ids:
        dropdown_html += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown_html += '</select>'

    return render_template("library_lost_cd.html", dropdown=dropdown_html)

@app.route("/save",methods=["POST"])
def save():
    t1=request.form["t1"]
    t2=request.form["t2"]
    t3=request.form["t3"]
    t4=request.form["t4"]
    t5=request.form["t5"]
    cursor=db.cursor()
    cursor.execute("INSERT INTO library_lost_cd VALUES ("+t1+","+t2+",'"+t3+"','"+t4+"',"+t5+")")
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
    cursor=db.cursor()
    cursor.execute("UPDATE library_lost_cd SET cd_id="+t2+",cd_name='"+t3+"',type='"+t4+"',price="+t5+" WHERE s_no="+t1+"")
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
    cursor.execute("DELETE FROM library_lost_cd WHERE s_no="+t1+"")
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
    cursor.execute("SELECT * from library_lost_cd")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_cd_search.html',data=data)

@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_lost_cd where s_no="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_cd_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_lost_cd WHERE "+col+"="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_cd_search.html',data=data)


if __name__=="__main__":
    app.run(debug=True,port=5001)