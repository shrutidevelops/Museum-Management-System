from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("menu.html")

@app.route("/basic_tkt",methods=["POST"])
def basic_tkt():
    return render_template("basic_tkt.html")

@app.route("/combo_tkt",methods=["POST"])
def combo_tkt():
    return render_template("combo_tkt.html")

@app.route("/drama_tkt",methods=["POST"])
def drama_tkt():
    return render_template("drama_tkt.html")

@app.route("/jewellery",methods=["POST"])
def jewellery():
    return render_template("jewellery.html")

@app.route("/library_book_entry",methods=["POST"])
def library_book_entry():
    return render_template("library_book_entry.html")

@app.route("/library_book_issue",methods=["POST"])
def library_book_issue():
    return render_template("library_book_issue.html")

@app.route("/library_cd_issue",methods=["POST"])
def library_cd_issue():
    return render_template("library_cd_issue.html")

@app.route("/library_cds_entry",methods=["POST"])
def library_cds_entry():
    return render_template("library_cds_entry.html")

@app.route("/library_lost_book",methods=["POST"])
def library_lost_book():
    return render_template("library_lost_book.html")

@app.route("/library_lost_cd",methods=["POST"])
def library_lost_cd():
    return render_template("library_lost_cd.html")

@app.route("/library_membership",methods=["POST"])
def library_membership():
    return render_template("library_membership.html")

@app.route("/museum_exhibition",methods=["POST"])
def museum_exhibition():
    return render_template("museum_exhibition.html")

@app.route("/museum_master",methods=["POST"])
def museum_master():
    return render_template("museum_master.html")

@app.route("/museum_membership",methods=["POST"])
def museum_membership():
    return render_template("museum_membership.html")

@app.route("/pottery",methods=["POST"])
def pottery():
    return render_template("pottery.html")

@app.route("/sculpture",methods=["POST"])
def sculpture():
    return render_template("sculpture.html")

@app.route("/stone",methods=["POST"])
def stone():
    return render_template("stone.html")

@app.route("/textiles",methods=["POST"])
def textiles():
    return render_template("textiles.html")

@app.route("/menu",methods=["POST"])
def menu():
    return render_template("menu.html")
if __name__=="__main__":
    app.run(debug=True,port=5020)