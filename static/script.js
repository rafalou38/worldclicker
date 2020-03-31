/*effet=document.getElementsByClassName("bulle");
document.getElementById("butotonShoot").addEventListener(bule)

alert("b")
function bule(){
    for (let i = 0; i < 20; i++) {

    }
}
*/
var pluses = []
function getRandomInt(max) {
	return Math.floor(Math.random() * Math.floor(max));
  }






var pluszone = document.querySelector(".pluszone")

$("#butotonShoot").click(function (e) {
	e.preventDefault();
	pluszone = document.querySelector(".pluszone")
	
	$.ajax({
		url: 'ajax/update/',
		data: {
		'username': "rafalou38"
		},
		dataType: 'json',
		success: function (data) {
			$("#bulle").text(data.clicks).append(setplus);
			animateplus()
			
		}
	})
	
})

function setplus(){

	var plus = document.createElement("p");
	plus.innerText = "+1";

	pluszone.appendChild(plus);
	plus.style.position = "absolute";
	var a = getRandomInt(50)+1;
	console.log(a+20);
	plus.style.right = 20 + a + "%";
	plus.setAttribute("class", "plus");
	pluses.push(plus)
	return( pluszone);
}
b=""
function animateplus(){
	// var Timeline = anime.timeline(parameters);
	// Timeline.add(parameters, offset);

	anime({

		targets: '.plus',
		opacity: 0,
		translateY: -180,
		easing: 'linear'
	});
	for (let i = 0; i < pluses.length; i++){
		plu = pluses[i];
		if (plu.style.opacity == 0) {
			plu.parentNode.removeChild(plu);
			pluses.splice(pluses.indexOf(plu),1)
		}else{
		 	break
		}
	}
}