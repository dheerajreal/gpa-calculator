from flask import Flask, render_template, request
import sqlite3
from gpa import gpa_calculate, result_calculate, db_work_extra, db_work
# defining app
app = Flask(__name__)

# defining routes
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            one = int(request.form.get("one"))
            two = int(request.form.get("two"))
            three = int(request.form.get("three"))
            four = int(request.form.get("four"))
            five = int(request.form.get("five"))
            six = int(request.form.get("six"))
            seven = int(request.form.get("seven"))
            eight = int(request.form.get("eight"))
            nine = int(request.form.get("nine"))
            ten = int(request.form.get("ten"))

            marks_list = [one, two, three, four,
                          five, six, seven, eight, nine, ten]
            gpa_list = [gpa_calculate(marks) for marks in marks_list]
            result = result_calculate(marks_list, gpa_list)
            # db_work(result)
            db_work_extra(marks_list, result)
            return render_template("result.html", result=result)
        except Exception as e:
            print(e)
            return render_template("gpa.html")

    else:
        return render_template("gpa.html")


if __name__ == "__main__":
    app.run(debug=True)
