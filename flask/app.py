from flask import Flask, render_template, request, flash
from gpa import db_work_extra, gpa_calculate, result_calculate

# defining app
app = Flask(__name__)
app.secret_key = "some_secret_key"

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
            passing = all(gpa_list)
            # uncomment for database
            # db_work_extra(marks_list, result)
            return render_template(
                "result.html",
                result=result,
                passing=passing
            )
        except Exception as e:
            print(e)
            return render_template("gpa.html")

    else:
        return render_template("gpa.html")


@app.route('/eight', methods=["GET", "POST"])
def eight():
    template_name = "eight.html"
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

            marks_list = [
                one, two, three, four, five, six, seven, eight
            ]
            gpa_list = [gpa_calculate(marks) for marks in marks_list]
            result = result_calculate(marks_list, gpa_list)
            passing = all(gpa_list)

            return render_template(
                "result.html",
                result=result,
                passing=passing
            )
        except Exception as e:
            flash("Invalid data received", category="danger")
            print(e)
            return render_template(template_name)

    else:
        return render_template(template_name)


# remove favicon.ico 404
@app.route('/favicon.ico')
def favicon():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
