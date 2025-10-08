var peso = parseFloat(prompt("Digite o seu peso em kg: "))
var altura = parseFloat(prompt("Digite a sua altura em metros: "))

var imc = peso / (altura ** 2);

alert("O seu IMC é: " + imc.toFixed(2));