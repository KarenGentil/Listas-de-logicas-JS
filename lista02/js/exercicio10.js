var numero1 = parseInt(prompt("Digite o primeiro numero: "))
var numero2 = parseInt(prompt("Digite o Segundo numero: "))
var numero3 = parseInt(prompt("Digite o Terceiro numero: "))


var numeros = [numero1, numero2, numero3];
numeros.sort(function(a, b){ return a - b; });

alert("Os números em ordem crescente são: " + numeros.join(", "));
