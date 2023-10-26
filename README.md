# Análise de Consultas Web - README

## Descrição

O projeto `Análise de Consultas Web` é um aplicativo web desenvolvido com Streamlit que permite aos usuários executar consultas sobre tópicos diversos através da API de Pesquisa Personalizada do Google. As consultas retornam informações relevantes, como título, link e snippet. Além disso, o aplicativo identifica o país de origem do domínio do resultado através da API IP Stack. As informações coletadas são apresentadas de forma estruturada na interface do usuário, incluindo uma análise da frequência de países de origem nos resultados das consultas.

## Como Usar

1. **Instalação**:
    - Certifique-se de ter o Python 3.6 ou versões superiores instalado em sua máquina.
    - Instale as bibliotecas necessárias usando o comando: `pip install streamlit requests`.

2. **Configuração**:
    - Obtenha uma chave de API do [Google Cloud Platform](https://cloud.google.com/) para a Pesquisa Personalizada do Google.
    - Para obter a chave de API acesse [Identify your application to Google with API key](https://developers.google.com/custom-search/v1/introduction) e siga os passos.
    - E para obter o ID do mecanismo, acesso o endereço [mecanismos de pesquisa](https://cse.google.com/all) e siga os passos.
    - Obtenha uma chave de API do [IP Stack](https://ipstack.com/) e substitua o valor de `IPSTACK_API_KEY` na função `inferir_pais`.
    - Configure as variáveis de ambiente `GOOGLE_API_KEY`, `CX` e `IPSTACK_API_KEY` com as chaves de API e o ID do mecanismo de pesquisa obtidos.

3. **Execução**:
    - Execute o comando: `streamlit run nome_do_arquivo.py` no terminal.
    - Abra o navegador e acesse o URL fornecido no terminal.
    - Digite os campos de busca (um por linha) na área de texto e clique no botão "Buscar" para obter os resultados.

4. **Uso**:
    - O aplicativo mostrará os resultados obtidos para cada campo de busca, junto com o país de origem do domínio.
    - Além disso, apresentará uma lista dos países mais frequentes entre os resultados.

## Como Contribuir

1. **Fork e Clone**:
    - Faça um fork deste repositório.
    - Clone o repositório forkado para a sua máquina local.

2. **Crie uma Branch**:
    - Crie uma nova branch para trabalhar na funcionalidade ou correção que deseja implementar: `git checkout -b nome-da-nova-branch`.

3. **Faça suas Modificações**:
    - Faça as modificações necessárias no código.
    - Teste suas mudanças garantindo que elas funcionem como esperado.

4. **Commit e Push**:
    - Faça commit de suas alterações com uma mensagem descritiva: `git commit -m "Descrição das alterações"`.
    - Envie suas alterações para o GitHub: `git push origin nome-da-nova-branch`.

5. **Crie um Pull Request**:
    - Vá para a página do repositório no GitHub e clique no botão "New Pull Request".
    - Selecione a branch que você criou e preencha as informações necessárias, descrevendo as alterações que você fez.
    - Submeta o Pull Request para revisão e merge.

## Deploy na AWS EC2

1. **Configuração da EC2**:
    - Acesse o [Console da AWS](https://aws.amazon.com/console/) e crie uma nova instância EC2.
    - Selecione uma AMI (Amazon Machine Image) com Ubuntu Server.
    - Configure as regras de entrada no grupo de segurança da EC2 para permitir o tráfego HTTP e HTTPS.
    - Acesse sua instância EC2 via SSH.

2. **Preparação do Ambiente**:
    - Atualize o sistema operacional com o comando: `sudo apt-get update && sudo apt-get upgrade`.
    - Instale o Python 3.6 ou superior: `sudo apt-get install python3`.
    - Instale o pip: `sudo apt-get install python3-pip`.
    - Instale o Streamlit e o Requests com o comando: `pip install streamlit requests`.

3. **Transferência do Código**:
    - Transfira o seu código e quaisquer outros arquivos necessários para a instância EC2 usando SCP ou outro método de sua escolha.

4. **Configuração de Variáveis de Ambiente**:
    - Configure as variáveis de ambiente para suas chaves de API usando o comando: `export NOME_VARIAVEL=valor_variavel`. 

5. **Execução**:
    - Execute o Streamlit com o comando: `streamlit run nome_do_arquivo.py --server.port 80`.

6. **Acesso**:
    - Acesse o aplicativo no navegador usando o endereço IP público da sua instância EC2.

7. **(Opcional) Configuração de Domínio**:
    - Configure um nome de domínio para apontar para o endereço IP da sua instância EC2 para um acesso mais fácil.

Este projeto é aberto para contribuições. Seja corrigindo bugs, melhorando a documentação, adicionando novas funcionalidades ou contribuindo de qualquer outra forma que achar relevante, sua ajuda é bem-vinda!
