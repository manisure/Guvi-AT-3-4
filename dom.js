"use strict";

// create HTML elements using Javascript

const suman = document.createElement("p");
suman.id = "first";
suman.innerHTML = "suman loves pizza and he is an excellent cook !";
document.body.appendChild(suman);

const guvi = document.createElement("div");
guvi.id = "guvi";
guvi.innerHTML = "this is a GUVI class on Python automation";
document.body.appendChild(guvi);

// DELETE THE DYNAMIC ELEMENTS

document.getElementById("btn1").addEventListener("click", function () {
  document.getElementById("first").remove();
});
