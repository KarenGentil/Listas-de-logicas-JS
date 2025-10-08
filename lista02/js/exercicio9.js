var mes = prompt("Digite o nome de um mês: ")

if (mes === "janeiro" || mes === "Março" || mes === "Abriu" || mes === "Maio" || mes === "Junho" || mes === "Julho" || mes === "Agosto" || mes === "Setembro" || mes === "Outubro" || mes === "Novembro" || mes === "Dezembro"){
    alert("O mês de " + mes + " tem 31 dias.")
} else if (mes === "abril" || mes === "junho" || mes === "setembro" || mes === "novembro") {
    alert("O mês de " + mes + " tem 30 dias.");
} else if (mes === "fevereiro") {
    alert("O mês de fevereiro tem 28 dias (29 em ano bissexto).");
} else {
    alert("Mês inválido!");
}
