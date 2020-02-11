# change_w_pass_router
Uma gambiarra para poder mudar a senha da rede sem fio pelo terminal, para o roteador TL-WR840N &lt;W> V6.

## Warning
O código presente neste repositório é uma gambiarra, não foi adequadamente testada e não deve em nenhum caso ser implementado em um ambiente de produção. Este aviso é válido até que o matenedor do repositório teste e corrija seus bugs. 

Qualquer contribuição com melhorias no códido pode ser submetida pela comunidade através de uma pull request.

## Documetação
Inicie o servidor nodejs:
`node encrypt_server.js`

No arquivo http_router:
- Altere os parâmetros de login e senha do roteador no método `HttpRouter.change_pass('admin', 'admin')`.
- Altere também a nova senha da rede `HttpRouter.change_pass('new password')`.
- Você também pode alterar o endereço de IP do roteador momento de instanciar a classe HttpRouter.

Execute o script principal: `python3 http_router.py`
A execução deste script imprimirá o comendo correto para alterar a senha, semelhante a este:
`./change_pass.sh 740a620452ca5f77a8f6bf61b6aaad 2caac6a280ba47e41f7917ae6af8bd new-password`
Execute o comando demonstrado acima em um outro terminal e aguarde. Em cado se sucesso a seguinga linha será imprimida no output: `[error]0`
É muito importamte que você execute o passo a passo sem fuçar na interface do roteador durante o espaço de tempo entre a execução dos passos.
