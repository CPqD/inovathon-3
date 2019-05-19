
function sayHello(id_produ) {

    let peso = document.getElementById('peso').value
    let produ = document.getElementById('produtor').value
    console.log(id_produ)  
    console.log(peso) 
    var ajax = new XMLHttpRequest();

// Seta tipo de requisição: Post e a URL da API
    ajax.open("POST", "/produtor/"+produ+"/cattle/transfer2producer/"+id_produ, true);
    ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

// Seta paramêtros da requisição e envia a requisição
    ajax.send("peso="+peso);

// Cria um evento para receber o r  etorno.
    ajax.onreadystatechange = function() {
  
  // Caso o state seja 4 e o http.status for 200, é porque a requisiçõe deu certo.
	if (ajax.readyState == 4 && ajax.status == 200) {
    
		var data = ajax.responseText;
		
    // Retorno do Ajax
        // console.log(1111);
        
        window.location.href = "/produtor/"+produ;
	}
}


    
  }