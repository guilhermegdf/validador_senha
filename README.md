### Validação de senha
***
O código desenvolvido é uma API Restful na qual consiste em verificar certos critérios de uma senha recebida e informar
 se ela é válida ou não.
>
Os critérios são:
>
>* Nove ou mais caracteres
>* Ao menos 1 dígito
>* Ao menos 1 letra minúscula
>* Ao menos 1 letra maiúscula
>* Ao menos 1 dos seguintes caracteres especiais: !@#$%^&*()-+
>* Não possuir caracteres repetidos dentro do conjunto

### Requisitos
***
* [Python](https://www.python.org/downloads/): Versão 3.X
* [pip](https://pip.pypa.io/en/stable/cli/pip/): Versão 21.X

### Configuração
***
Caso esteja utilizando o editor de código *Pycharm*, ao criar um novo projeto o ambiente de desenvolvimento é criado 
e ativado automaticamente. Nesse caso só é necessario instalar as dependencias com o comando abaixo:

`pip install -r requirements.txt`

Caso esteja utilizando qualquer outro editor de código como Visual Studo Code e Atom, é preciso criar manualmente o 
ambiente. Para isso, consulte o link.
[Virtualenv](https://docs.python.org/3/tutorial/venv.html)

Para executar a aplicação execute o arquivo `app.py`.

### Utilização
***
Para realizar a validação da "senha", é preciso realizar uma requisição no localhost:5050, usando o metódo POST e 
enviar um JSON com a chave "senha".

Exemplo de Body:
>{"senha":'aBc123$'}

### Testes
***
Os testes são utilizados para testar o metódo desenvolvido sem precisar subir a API e realizar requisição. para executar
 basta acesse o diretório `test` e execute o `validador.py`.

Caso queira alterar ou adicionar mais testes, é só seguir os modelos já criados.
>self.assertEqual(validacao([senha]), [resultado esperado])

