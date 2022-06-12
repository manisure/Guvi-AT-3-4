// CREATE HTML ELEMENTS USING DOM

const suman = document.createElement("div");
suman.id = "suman";
suman.innerHTML = "this is a suman div created dynamically by Javascript";
document.body.appendChild(suman);

const ganguly = document.createElement("p");
ganguly.id = "ganguly";
ganguly.innerHTML = "this is the 2nd tag";
document.body.appendChild(ganguly);

// DELETE HTML ELEMENTS DYNAMICALLY USING JAVASCRIPT

document.getElementById("btn1").addEventListener("click", function () {
  document.getElementById("suman").remove();
});
