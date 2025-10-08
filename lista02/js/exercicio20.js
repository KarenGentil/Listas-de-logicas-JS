var n1 = parseInt(prompt("Digite o primeiro número:"));
var n2 = parseInt(prompt("Digite o segundo número:"));
var n3 = parseInt(prompt("Digite o terceiro número:"));

var media = (n1 + n2 + n3) / 3;

if (media >= 7) {
    alert("A média é " + media.toFixed(2) + ". Aprovado!");
} else {
    alert("A média é " + media.toFixed(2) + ". Reprovado!");
}
