/*effet=document.getElementsByClassName("bulle");
document.getElementById("butotonShoot").addEventListener(bule)

alert("b")
function bule(){
    for (let i = 0; i < 20; i++) {

    }
}
*/
var hfor = true;
var pluses = [];
function getRandomInt(max) {
	return Math.floor(Math.random() * Math.floor(max));
}

// $(".wclicks")[0].innerText="c";

$(document).ready(function() {
	$(".wclicks").innerText = "vdvdvdvdvdvdfvffgffffggfdggbhgvf";
	$(".wclicks").niceScroll({
		cursorcolor: "blueviolet",
		cursorborderradius: "22px",
		cursorborder: "0px",
		cursoropacitymin: 0.3

		//cursoropacitymax:0.7,
	});
});
function setclicks(bol) {
	e = $(".wclicks")[0];
	//e.style.userSelect = "none";

	if (bol != true) {
		hfor = !hfor;
	}
	if (hfor) {
		e.innerText = mclicks;
	} else {
		e.innerText = bclicks;
	}
}

var pluszone = document.querySelector(".pluszone");
var body = document.querySelector("body");
$("#bulle").click(setclicks);

$("#butotonShoot").click(function(e) {
	e.preventDefault();
	pluszone = document.querySelector(".pluszone");

	$.ajax({
		url: "ajax/update/",
		data: {
			username: "rafalou38"
		},
		dataType: "json",
		success: function(data) {
			//$(".wclicks").text(data.clicks);
			$("#bulle").append(setplus(e));
			mclicks = data.clicks;
			bclicks = data.bcli;
			//console.log(document.getElementsByClassName("bulle"));

			setclicks(true);
			animateplus();
		}
	});
});

function setplus(e) {
	// // console.log((e.clientX-450)/1.43);
	// console.log(100 * e.clientX/$(document).width());
	// console.log(e.clientX);
	// console.log($(document).width());
	// console.log("------------------");

	// console.log((100*(e.clientX-(($(document).width()-160)/2)))/160);
	// console.log("------------------");

	var plus = document.createElement("p");
	plus.innerText = "+1";

	body.appendChild(plus);
	plus.style.position = "absolute";

	plus.style.left = e.clientX - 20 + "px";
	plus.style.top = 530 + "px";
	plus.setAttribute("class", "plus");
	pluses.push(plus);
	return pluszone;
}
b = "";
function animateplus() {
	// var Timeline = anime.timeline(parameters);
	// Timeline.add(parameters, offset);

	anime({
		targets: ".plus",
		opacity: 0,
		translateY: -180,
		easing: "linear"
	});
	for (let i = 0; i < pluses.length; i++) {
		plu = pluses[i];
		if (plu.style.opacity == 0) {
			plu.parentNode.removeChild(plu);
			pluses.splice(pluses.indexOf(plu), 1);
		} else {
			break;
		}
	}
}
