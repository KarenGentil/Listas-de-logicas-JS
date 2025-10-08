var salarioMinimo = parseFloat(prompt("Digite o valor do salário mínimo:"));
var salarioFuncionario = parseFloat(prompt("Digite o salário do funcionário:"));

var quantidade = salarioFuncionario / salarioMinimo;

alert("O funcionário recebe " + quantidade.toFixed(2) + " salários mínimos.");
