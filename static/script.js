let slider=document.getElementById("n");

slider.oninput=function(){

let n=this.value;

document.getElementById("value").innerHTML=n;

document.getElementById("o1").innerHTML=1;

document.getElementById("olog").innerHTML=
Math.log2(n).toFixed(2);

document.getElementById("on").innerHTML=n;

document.getElementById("onlog").innerHTML=
(n*Math.log2(n)).toFixed(2);

document.getElementById("on2").innerHTML=
n*n;

}

slider.oninput();