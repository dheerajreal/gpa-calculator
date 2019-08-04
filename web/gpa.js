var name=alert("Welcome to GPA calculator");
document.write("<h1>GPA calculator<br /></h1>");
var subs=prompt("Number of subjects?");
//checking for valid values
subs=parseInt(subs);
if (!(Number.isInteger(subs)) || subs<0) {
    document.write("<h2 class=error> Enter positive  numeric value for subject!</h2>");
    errorMessage();
}
//bunch of variables
var marksList=[];
var sum=0;
var gpaList=[];
var gpa=0;
//prompt for values
for (i=0;i<subs;i++){
    var marks=prompt("Enter marks in paper "+(i+1));
    //checking for valid values
    marks=parseInt(marks);
    if ( !(Number.isInteger(marks)) || marks>100 || marks<0){
        document.write("<h2 class=error> Only numeric values between 0 and 100 are allowed!</h2>");
        errorMessage();
    }
    //add values to markList
    marksList.push(marks)
    document.write("<h3>Marks in paper "+(i+1)+" :"+marks+ "</h3>");
    //add values to gpaList
    {   if (marks<40){
            gpaList.push(0);
        }
        else if  (marks>=40 && marks<45){
            gpaList.push(4);
        }
        else if (marks>=45 && marks<50){
            gpaList.push(5);
        }
        else if (marks>=50 && marks<60){
            gpaList.push(6);
        }
        else if (marks>=60 && marks<70){
            gpaList.push(7);
        }
        else if (marks>=70 && marks<75){
            gpaList.push(8);
        }
        else if (marks>=75 && marks<80){
            gpaList.push(9);
        }
        else if (marks>=80) {
            gpaList.push(10);
        }
    }
}
//add all values in marksList
for (i=0;i<marksList.length;i++){
    sum+=marksList[i];

}

//add all values in gpaList
for (i=0;i<gpaList.length;i++){
    gpa+=gpaList[i];

}
//display sum and average
document.writeln("<h2>The total marks are :"+sum+ "</h2>");
document.writeln("<h2>The average marks are :"+(sum/subs).toFixed(2) + "</h2>");
document.writeln("<h2>The GPA is:"+(gpa/subs).toFixed(2) + "</h2>");
//error message
function errorMessage(){
    throw new Error("Something went badly wrong!");
}





