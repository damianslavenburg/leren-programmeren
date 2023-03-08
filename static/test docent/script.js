var button1 =document.getElementById("button1");
var button2 =document.getElementById("button2");

var count1 = 1;	
var count2 = 100;

button1.innerHTML = count1;
button2.innerHTML = count2;

button1.onclick = button1Clicked;
button2.onclick = button2Clicked;

function button1Clicked(){
    count1++;
    button1.innerHTML = count1;
}

function button2Clicked(){
    count2--;
    button2.innerHTML =count2;
}