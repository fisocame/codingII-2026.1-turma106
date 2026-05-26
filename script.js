let projetos = [];

function mostrarMensagem(){
    let nome = document.getElementById("nome").value;
    let status = document.getElementById("statusProjeto").value;
    let curso = document.getElementById("cursoProjeto").value;

    if (nome === "" || status === "") {
        document.getElementById("resultado").innerText =
        "Digite um projeto e o seu status!";

        document.getElementById("resultado").className =
        "mensagem-erro";

        return;
    }

    let projeto = {
        nome: nome,
        status: status,
        curso: curso
    }

    projetos.push(projeto);

    atualizarLista();

    document.getElementById("resultado").innerText =
    "Projeto encontrado com sucesso.";

    document.getElementById("resultado").className =
    "mensagem-sucesso";

    limparMensagem();
}

function atualizarLista() {

    let lista = document.getElementById("listaProjetos");

    lista.innerHTML = "";

    for (let i = 0; i < projetos.length; i++) {

        let projeto = projetos[i];

        let card = document.createElement("div");

        card.className = "card-projeto";

        let classeStatus = "status-andamento";

        if (projeto.status.toLowerCase() === "finalizado") {

            classeStatus = "status-finalizado";
        }

        card.innerHTML =`
            <h3>${projeto.nome}</h3>

            <p>
                Curso: ${projeto.curso}
            </p>

            <p class="$classeStatus">
                Status: ${projeto.status}
            </p>

            <button class="btn-remover" onclick="removerProjeto(${i})">
                Remover
            </button>
        `;

        lista.appendChild(card);

    }

    atualizarContador();

}

function removerProjeto(indice) {

    projetos.splice(indice, 1)

    atualizarLista();
}

function atualizarContador() {

    document.getElementById("contadorProjetos").innerText =
    "Total de Projetos: " + projetos.length;
}

function limparMensagem(){

    document.getElementById("nome").value = "";

    document.getElementById("statusProjeto").value = "";

    document.getElementById("resultado").innerText = "";

}