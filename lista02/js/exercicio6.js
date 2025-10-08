var nota1 = parseInt(prompt("Digite a primeira nota: "))
var nota2 = parseInt(prompt("Digite a Segunda nota: "))
var nota3 = parseInt(prompt("Digite a Terceira nota: "))

var resultado = (nota1 + nota2 + nota3) /  3

if(resultado >= 7){
    alert("Você foi aprovado, sua nota foi " +resultado)
}else{
    alert("Reprovado, sua nota foi " +resultado)
}