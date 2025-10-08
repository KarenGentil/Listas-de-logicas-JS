var nome = prompt("Digite o nome do aluno:");
var turno = prompt("Digite o turno (M para Matutino, V para Vespertino):").toUpperCase();

if (turno === "M") {
    alert("Bom dia, " + nome + "!");
} else if (turno === "V") {
    alert("Boa tarde, " + nome + "!");
} else {
    alert("Turno inválido!");
}
