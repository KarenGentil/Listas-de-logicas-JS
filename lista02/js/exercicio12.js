var codigo = parseInt(prompt("Digite o código do produto (1 a 3):"));
var quantidade = parseInt(prompt("Digite a quantidade comprada:"));
var preco;

if (codigo === 1) {
    preco = 5.00;
} else if (codigo === 2) {
    preco = 10.00;
} else if (codigo === 3) {
    preco = 20.00;
} else {
    alert("Código inválido!");
}

if (preco) {
    var total = preco * quantidade;
    alert("O valor total a ser pago é: R$ " + total.toFixed(2));
}
