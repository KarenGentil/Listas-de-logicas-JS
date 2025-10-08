var nome1 = prompt("Digite o nome da primeira pessoa:")
var idade1 = parseInt(prompt("Digite a idade de " + nome1 + ":"))

var nome2 = prompt("Digite o nome da primeira pessoa:")
var idade2 = parseInt(prompt("Digite a idade de " + nome2 + ":"))

var nome3 = prompt("Digite o nome da primeira pessoa:")
var idade3 = parseInt(prompt("Digite a idade de " + nome3 + ":"))

var media = (idade1 + idade2 + idade3) / 3;

alert("A média das idades de " + nome1 + ", " + nome2 + " e " + nome3 + " é: " + media.toFixed(1));
