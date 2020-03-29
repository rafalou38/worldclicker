// effet=document.getElementsByClassName("bulle");
// document.getElementById("butotonShoot").addEventListener(bule)

// alert("b")
// function bule(){
//     for (let i = 0; i < 20; i++) {
        
//     }
// }

// $(document).ready(function(){
// 	$('#butotonShoot').click(function (e) { 
// 		// e.preventDefault();
// 		var clicks = $(this).attr('clicks')
// 		console.log(clicks)
// 		req = $.ajax({
// 			type: "POST",
// 			url: "/update",
// 			data: {clicks : clicks},
// 		});
// 	});

	
// })
// $(document).ready(function(e){
// 	$('#butotonShoot').click(function (e) { 
// 		e.preventDefault();
// 		var pk = $(this).attr('clicks')
// 		$.ajax({
// 			type: 'POST',
// 			url: '{% url "test" %}',
// 			data : {'clicks' : pk, 'csrfmidelwaretoken': '{{ csrf_token}}'},
// 			dataType : 'json',
// 			success: function(resonse){
// 				$('.bulle').html(resonse['form'])
// 				console.log($('.bulle').html(resonse['form']));
				
// 			},
// 			error: function(rs, e){
// 				console.log(rs.responseText);
				
// 			}
			
// 		})
// 	});
// });


// $("#button").click(funct
	// var username = $(this).val();

	// $.ajax({
	//   url: '/ajax/validate_username/',
	//   data: {
	// 	'username': username
	//   },
	//   dataType: 'json',
	//   success: function (data) {
	// 	if (data.is_taken) {
	// 	  alert("A user with this username already exists.");
	// 	}
	//   }
	// });

//   });

	
$("#butotonShoot").click(function (e) { 
	e.preventDefault();
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
