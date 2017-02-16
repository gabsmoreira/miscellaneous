function done (){
	var elvaga = document.getElementById('feedback_vaga');

	var eldono = document.getElementById('feedback_dono');

	var elplaca = document.getElementById('feedback_placa');

	elvaga.textContent = localStorage.getItem('vaga');
	elplaca.textContent = localStorage.getItem('placa'); 
	eldono.textContent = localStorage.getItem('dono');
}

function del (){
	eldono = ''
	elplaca = ''
	elvaga = ''
	localStorage.removeItem('vaga');
	localStorage.removeItem('placa');
	localStorage.removeItem('dono');
	localStorage.removeItem('horario');
	localStorage.removeItem('modelo');
	localStorage.removeItem('cor');
}




/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}