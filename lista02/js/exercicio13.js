var idade = parseInt(prompt("Digite a sua idade:"));
var sexo = prompt("Digite seu sexo (M ou F):").toUpperCase();

if ((sexo === "M" && idade >= 65) || (sexo === "F" && idade >= 60)) {
    alert("Você pode se aposentar.");
} else {
    alert("Você ainda não pode se aposentar.");
}
