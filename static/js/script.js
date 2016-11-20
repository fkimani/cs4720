	//this function will validate user input 
	//revisit to prevent user from being sent to results page if assertion fails. thinking about assert, look into that
	function runner()
	{
		var x = document.getElementById("zip_input").value;
		var i = 0;
		for(i in x){
			if ( isNaN(parseInt(x[i])) )
			{
				alert ("please enter correct zip code");
				break;							
			}
		}	
	}
	//event handler for runner function
	document.getElementById("submit_btn").addEventListener('click', runner, false)


