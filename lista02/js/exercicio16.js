var quantidade = parseInt(prompt("Digite o número de maçãs compradas:"));
var preco;

if (quantidade >= 12) {
    preco = 0.40;
} else {
    preco = 0.50;
}

var total = quantidade * preco;
alert("O valor total da compra é: R$ " + total.toFixed(2));
