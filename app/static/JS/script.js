(function () {

    const form = document.querySelector('form');
    const msgSuccess = document.querySelector('#success');
    const msgError = document.querySelector('#error');


    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const valorCpf = document.querySelector('#cpf_digitado');
        const cpf = { cpf: valorCpf.value };

        fetch(`${window.origin}/validarCPF`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(cpf),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            }),
        }).then((response) => {
            if (response.status !== 200) {
                console.log(`Parece que houve um problema. Código de status: ${response.status}`);
                return;
            }
            response.json().then((data) => {
                if (data['mensagem'] === "False") {
                    msgSuccess.style.display = 'none';
                    msgError.style.display = 'block';
                } else {
                    msgSuccess.style.display = 'block';
                    msgError.style.display = 'none';
                    console.log(msgSuccess.style.display);
                }
            });
        })
    });

}());
