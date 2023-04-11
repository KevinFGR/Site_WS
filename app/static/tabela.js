function sub() {
    return document.forms[0].submit();
}
function habilita(x) {
    x = x.substr(0, x.length - 12);
    x = x.split('pontevirgula');
    let inputs = document.forms[0].elements;
    let tam = inputs.length-1;
    for (i = 0; i < tam; i++) {
        inputs[i].disabled = false;
        if (i < tam - 5) {
            inputs[i].value = x[i];
        }
    }
    let chave = document.getElementById('chave');
    chave.value = x[0];
}
function limpa() {
    let inputs = document.forms[0].elements;
    let tam = inputs.length-1;
    for (i = 0; i < tam; i++) {
        if (i < tam - 5) {
            inputs[i].value = "";
        }
        if (i < tam - 1) {
            inputs[i].disabled = true;
        }
    }
    inputs[tam - 3].disabled = false;

}
function adiciona() {
    let inputs = document.forms[0].elements;
    let tam = inputs.length-1;
    inputs[tam - 1].hidden = true;
    for (i = 0; i < tam; i++) {
        inputs[i].disabled = false;
        if (i < tam - 5) {
            inputs[i].value = "";
        }
    }
    inputs[tam - 3].disabled = true;
    inputs[tam - 2].disabled = true;
    let chave = document.getElementById('chave');
    chave.value = "adicionar";
    return sub();
}
function exclui() {
    let chave = document.getElementById('chave');
    chave.value = "excluir";
    return sub();
}
