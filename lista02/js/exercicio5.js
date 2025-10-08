var numero1 = parseInt(prompt("Digite um numero: "))
var numero2 = parseInt(prompt("Digite o segundo  numero: "))

if(numero1 > numero2){
    alert("o " +numero1+ " é maior que o "+ numero2)
}else if(numero2 > numero1){
    alert("o " +numero2+ " é maior que o "+ numero1)
}else{
    alert("os numeros são iguais!")
}