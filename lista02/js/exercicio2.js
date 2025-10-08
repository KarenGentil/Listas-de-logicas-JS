var nome1 = prompt("Digite seu nome: ");
var idade1 = parseInt(prompt("Digite a idade de " +nome1));

var nome2 = prompt("Digite seu nome : ");
var idade2 = parseInt(prompt("Digite a idade de "+nome2));

if (idade1 > idade2){
    alert(nome1+ " é mais velho(a) que " + nome2)
} else if (idade2 > idade1){
    alert(nome2+ " é mais velho(a) que " + nome1)
} else{
    alert(nome1 + " e " + nome2 + " têm a mesma idade.")
}