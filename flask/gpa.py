import sqlite3

# defining functions
# calculate gpa


def gpa_calculate(sub_marks: int) -> int:
    if sub_marks > 100 or sub_marks < 0:
        raise ValueError
    if sub_marks < 40:
        gpa = 0
    elif sub_marks >= 40 and sub_marks < 45:
        gpa = 4
    elif sub_marks >= 45 and sub_marks < 50:
        gpa = 5
    elif sub_marks >= 50 and sub_marks < 55:
        gpa = 6
    elif sub_marks >= 55 and sub_marks < 60:
        gpa = 7
    elif sub_marks >= 60 and sub_marks < 70:
        gpa = 8
    elif sub_marks >= 70 and sub_marks < 80:
        gpa = 9
    elif sub_marks >= 80:
        gpa = 10
    return gpa


def result_calculate(marks_list, gpa_list):
    total = sum(marks_list)
    avg = total/len(marks_list)
    gpa_final = sum(gpa_list)/len(marks_list)
    result = {"total": total, "average": avg, "gpa_final": gpa_final}
    return result

# database stuff


def db_work_extra(marks_list, result):
    db = sqlite3.connect("./mysite/app.db")
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO FULL VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{}) "
        .format(
            *marks_list,
            result["total"],
            result["average"],
            result["gpa_final"]
        )
    )
    db.commit()
    db.close()
