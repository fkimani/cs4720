/*function myMap() {
  var mapCanvas = document.getElementById("map");
  var mapOptions = {
    //center: new google.maps.LatLng(51.5, -0.2), zoom: 10
    center: new google.maps.LatLng({{city_lat}}, {{city_lon}}), zoom: 10
  }
  var map = new google.maps.Map(mapCanvas, mapOptions);


		document.getElementById("input").onkeyup = function(){
			var input = document.getElementById("zip_input").value

			function zzvalidateInput(input){
				if ((input.value == " "))
					alert("Enter Valid Zip")
			}
		}*/


		document.getElementById('submit_btn").addEventListener("click", validateInput, false);
		
		function validateInput(){
			alert("input received")
		}
