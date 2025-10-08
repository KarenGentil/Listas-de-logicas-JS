var base = parseFloat(prompt("Digite o valor da base do triângulo (cateto adjacente): "))
var altura = parseFloat(prompt("Digite o valor da altura do triângulo (cateto oposto): "))

var hipotenusa = Math.sqrt((base ** 2) + (altura ** 2))

alert("A hipotenusa do triângulo é: " + hipotenusa.toFixed(2))