// Get the modal
const modal1 = document.getElementById("myModal1");
const modal2 = document.getElementById("myModal2");

const btn1 = document.getElementById("myBtn1");
const btn2 = document.getElementById("myBtn2");
/*const btn2 = document.getElementById("myBtn2");
const btn3 = document.getElementById("myBtn3");
const btn4 = document.getElementById("myBtn4");
const btn5 = document.getElementById("myBtn5");
const btn6 = document.getElementById("myBtn6");
const btn7 = document.getElementById("myBtn7");
const btn8 = document.getElementById("myBtn8");
const btn9 = document.getElementById("myBtn9");
const btn10 = document.getElementById("myBtn10");
const btn11 = document.getElementById("myBtn11");
const btn12 = document.getElementById("myBtn12");
const btn13 = document.getElementById("myBtn13");
const btn14 = document.getElementById("myBtn14");
const btn15 = document.getElementById("myBtn15");
const btn16 = document.getElementById("myBtn16");
const btn17 = document.getElementById("myBtn17");
const btn18 = document.getElementById("myBtn18");
const btn19 = document.getElementById("myBtn19");
const btn20 = document.getElementById("myBtn20"); */


const span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn1.onclick = function() {
  modal1.style.display = "block";
}

 btn2.onclick = function() {
  modal2.style.display = "block";
}
/*
btn2.onclick = function() {
  modal.style.display = "block";
}
btn3.onclick = function() {
  modal.style.display = "block";
}
btn4.onclick = function() {
  modal.style.display = "block";
}
btn5.onclick = function() {
  modal.style.display = "block";
}
btn6.onclick = function() {
  modal.style.display = "block";
}
btn7.onclick = function() {
  modal.style.display = "block";
}
btn8.onclick = function() {
  modal.style.display = "block";
}
btn9.onclick = function() {
  modal.style.display = "block";
}
btn10.onclick = function() {
  modal.style.display = "block";
}
btn11.onclick = function() {
  modal.style.display = "block";
}
btn12.onclick = function() {
  modal.style.display = "block";
}
btn13.onclick = function() {
  modal.style.display = "block";
}
btn14.onclick = function() {
  modal.style.display = "block";
}
btn15.onclick = function() {
  modal.style.display = "block";
}
btn16.onclick = function() {
  modal.style.display = "block";
}
btn17.onclick = function() {
  modal.style.display = "block";
}
btn18.onclick = function() {
  modal.style.display = "block";
}
btn19.onclick = function() {
  modal.style.display = "block";
}
btn20.onclick = function() {
  modal.style.display = "block";
} */  

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal1.style.display = "none";
}

/*span.onclick = function() {
  modal2.style.display = "none";
}  */ 
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}

/*window.onclick = function(event) {
  if (event.target == modal2) {
    modal2.style.display = "none";
  }
} */