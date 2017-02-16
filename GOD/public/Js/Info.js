function checkNome(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<4){
        elMsg.textContent = 'O nome deve ser maior!';
        }
    else{
        elMsg.textContent ='';
    }
}

function checkHora(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<4){
        elMsg.textContent = 'Horário não aceito!';
        }
    else{
        elMsg.textContent ='';
    }
}

function checkPlaca(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<4){
        elMsg.textContent = 'Placa não aceita!';
        }
    else{
        elMsg.textContent ='';
    }
}

function checkModelo(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<4){
        elMsg.textContent = 'Modelo não aceito!';
        }
    else{
        elMsg.textContent ='';
    }
}

function checkCor(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<3){
        elMsg.textContent = 'Cor não aceita!';
        }
    else{
        elMsg.textContent ='';
    }
}

function checkLocal(){
    var elMsg = document.getElementById('feedback');
    var elUsername = document.getElementById('nome');
    if (elUsername.value.length<4){
        elMsg.textContent = 'Local não aceito!';
        }
    else{
        elMsg.textContent ='';
    }
}


function store(){
     var inputDono= document.getElementById("dono");
     localStorage.setItem("dono", inputDono.value);

     var inputHorario= document.getElementById("horario");
     localStorage.setItem("horario", inputHorario.value);

     var inputPlaca= document.getElementById("placa");
     localStorage.setItem("placa", inputPlaca.value);

     var inputModelo= document.getElementById("modelo");
     localStorage.setItem("modelo", inputModelo.value);

     var inputCor= document.getElementById("cor");
     localStorage.setItem("cor", inputCor.value);

     var inputVaga= document.getElementById("vaga");
     localStorage.setItem("vaga", inputVaga.value);

    }

function myFunction(x) {
    x.classList.toggle("change");
}