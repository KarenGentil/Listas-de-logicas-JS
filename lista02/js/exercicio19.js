var idade = parseInt(prompt("Digite sua idade:"));

if (idade >= 18 && idade <= 70) {
    alert("O voto é obrigatório.");
} else if ((idade >= 16 && idade < 18) || idade > 70) {
    alert("O voto é facultativo.");
} else {
    alert("Você ainda não pode votar.");
}
