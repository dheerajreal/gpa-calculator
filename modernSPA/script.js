$(document).ready(function() {
    $("#myform").submit(function() {
        calculate();
    });
});

function calculate() {
    var one = $("#1").val();
    var two = $("#2").val();
    var three = $("#3").val();
    var four = $("#4").val();
    var five = $("#5").val();
    var six = $("#6").val();
    var seven = $("#7").val();
    var eight = $("#8").val();
    var nine = $("#9").val();
    var ten = $("#10").val();

    //bunch of variables
    var marksList = [];
    var sum = 0;
    var gpaList = [];
    var gpa = 0;
    //add values to markList
    var marksList = [one, two, three, four, five, six, seven, eight, nine, ten];
    for (let index = 0; index < marksList.length; index++) {
        let marks = marksList[index];
        marks = parseInt(marks);
        marksList[index] = marks;
    }
    //add values to gpaList
    marksList.forEach(marks => {
        if (marks < 40) {
            gpaList.push(0);
        } else if (marks >= 40 && marks < 45) {
            gpaList.push(4);
        } else if (marks >= 45 && marks < 50) {
            gpaList.push(5);
        } else if (marks >= 50 && marks < 55) {
            gpaList.push(6);
        } else if (marks >= 55 && marks < 60) {
            gpaList.push(7);
        } else if (marks >= 60 && marks < 70) {
            gpaList.push(8);
        } else if (marks >= 70 && marks < 80) {
            gpaList.push(9);
        } else if (marks >= 80) {
            gpaList.push(10);
        }
    });

    //add all values in marksList
    for (i = 0; i < marksList.length; i++) {
        sum += marksList[i];
    }

    //add all values in gpaList
    for (i = 0; i < gpaList.length; i++) {
        gpa += gpaList[i];
    }
    if (Number.isInteger(sum) && Number.isInteger(gpa)) {
        $(".invisible").removeClass("invisible");
        $("#sum").text(sum);
        $("#percent").text((sum / 10).toFixed(2));
        $("#gpa").text((gpa / 10).toFixed(2));
        document.querySelector("form").remove();
    }
}