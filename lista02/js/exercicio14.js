var peso = parseFloat(prompt("Digite seu peso (kg):"));
var altura = parseFloat(prompt("Digite sua altura (m):"));

var imc = peso / (altura ** 2);
var classificacao = "";

if (imc < 18.5) classificacao = "Abaixo do peso";
else if (imc < 25) classificacao = "Peso normal";
else if (imc < 30) classificacao = "Sobrepeso";
else classificacao = "Obesidade";

alert("Seu IMC é " + imc.toFixed(2) + " - " + classificacao);
