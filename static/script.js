/*effet=document.getElementsByClassName("bulle");
document.getElementById("butotonShoot").addEventListener(bule)

alert("b")
function bule(){
    for (let i = 0; i < 20; i++) {

    }
}
*/
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
