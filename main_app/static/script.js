
console.log("coucou")
$("#butotonShoot").click(function (e) {
	e.preventDefault();
	alert("ddd")
	makeBubble()
	$.ajax({
		
		url: 'ajax/update/',
		// data: {
		// 	'username': "rafalou38"
		// },
		// dataType: 'json',
		success: function (data) {
			$("#bulle").text(data.clicks);
		}
	})
})



// function makeBubble(){
	
// }
        




