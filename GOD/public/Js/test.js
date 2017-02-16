function checkUser(){
    var elMsg = document.getElementById('feedback');
    var user = document.getElementById('usuario');
    var pass =  document.getElementById('empresa')
    if (user.value!="gabsmoreira" || pass.value!="mengo1998_" ){
           alert("Wrong password!")

        }
    else{
        window.open("inicial.html");
    }
}


function store(){
     var inputUsuario= document.getElementById("usuario");
     localStorage.setItem("usuario", inputUsuario.value);

     var inputEstabelecimento= document.getElementById("estabelecimento");
     localStorage.setItem("estabelecimento", inputEstabelecimento.value);

     var inputEmpresa= document.getElementById("empresa");
     localStorage.setItem("empresa", inputEmpresa.value);


    }
