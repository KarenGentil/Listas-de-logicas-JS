var nome = prompt("Digite o nome do aluno:");
var nota = parseFloat(prompt("Digite a nota de " + nome + ":"));

if (nota >= 7) {
    alert(nome + " está Aprovado(a).");
} else {
    alert(nome + " está em Recuperação.");
}
