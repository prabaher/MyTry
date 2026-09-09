from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql*121#",
    database="sample2"
)

cursor = db.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    reg_no = request.form["reg_no"]
    rating = request.form["rating"]
    feedback = request.form["feedback"]

    sql = """
        INSERT INTO feedback
        (name, reg_no, rating, feedback)
        VALUES (%s, %s, %s, %s)
    """

    values = (name, reg_no, rating, feedback)

    cursor.execute(sql, values)

    db.commit()


    print("Feedback saved!")
    print(name, reg_no, rating, feedback)

    print("Name:", name)
    print("Reg No:", reg_no)
    print("Rating:", rating)
    print("Feedback:", feedback)

    return render_template("done.html")

if __name__ == "__main__":
    app.run(debug=True)