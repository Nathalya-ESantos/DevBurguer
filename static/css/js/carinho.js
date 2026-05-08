function mostrar_carrinho()
{
    const resposta = await fetch("hhtp://10.110.134.2:8080/api/get/carrinho")

    if (!resposta.ok){
        alert("ERRO AO CARREGAR O CARRINHO!")
    }

    else{
        const dados = await resposta.json()

        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        for(let dado of dados){
            let linha =
        }
    }
} 