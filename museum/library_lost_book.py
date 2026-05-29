from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="1234",database="museum")
@app.route("/")
def index():

    cursor = db.cursor()
    cursor.execute("SELECT b_id FROM library_lost_book")  # assuming 'id' is your PK
    ids = cursor.fetchall()
    cursor.close()

    # Build dropdown HTML in Python
    dropdown_html = '<select name="b_id">'
    for row in ids:
        dropdown_html += f'<option value="{row[0]}">{row[0]}</option>'
    dropdown_html += '</select>'

    return render_template("library_lost_book.html", dropdown=dropdown_html)

@app.route("/save",methods=["POST"])
def save():
    t1=request.form["t1"]
    t2=request.form["t2"]
    t3=request.form["t3"]
    t4=request.form["t4"]
    t5=request.form["t5"]
    t6=request.form["t6"]
    cursor=db.cursor()
    cursor.execute ("INSERT INTO library_lost_book VALUES ("+t1+","+t2+",'"+t3+"','"+t4+"','"+t5+"',"+t6+")")
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
    
    cursor=db.cursor()
    cursor.execute("UPDATE library_lost_book SET b_id="+t2+",book_name='"+t3+"',author='"+t4+"',publication='"+t5+"',price="+t6+" WHERE s_no="+t1+"")
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
    cursor.execute("DELETE FROM library_lost_book WHERE s_no="+t1+"")
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
    cursor.execute("SELECT * from library_lost_book")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_book_search.html',data=data)
@app.route("/psearch",methods=["POST"])
def psearch():
    t1=request.form["t1"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_lost_book where s_no="+t1+"")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_book_search.html',data=data)

@app.route("/spsearchformopen",methods=["POST"])
def spsearchformopen():
    return render_template('spsearch.html')
@app.route("/spsearch",methods=["POST"])
def spsearch():
    t1=request.form["t1"]
    col=request.form["col"]
    cursor=db.cursor()
    cursor.execute("SELECT * from library_lost_book WHERE "+col+"='"+t1+"'")
    data=cursor.fetchall()
    cursor.close()
    return render_template('library_lost_book_search.html',data=data)

if __name__=="__main__":
    app.run(debug=True,port=5003)