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