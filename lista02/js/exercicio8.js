var salario = parseFloat(prompt("Digite o salário do funcionário: "));

var bonus;

if (salario > 2000) {
    bonus = salario * 0.10;
} else {
    bonus = salario * 0.05;
}

alert("O bônus do funcionário é de R$ " + bonus.toFixed(2));
