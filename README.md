# web_scraping_proxy

## Descrição
O código é um exemplo de como usar a biblioteca requests e BeautifulSoup para fazer o scraping de uma página web e extrair informações específicas dela. O objetivo desse código é obter uma lista de proxies gratuitos e salvar os proxies válidos em um arquivo JSON.

## Como o codigo funciona?
1. O código importa as bibliotecas necessárias: requests, BeautifulSoup e json.
2. Em seguida, é criada uma lista vazia chamada proxyList para armazenar os proxies válidos.
3. A variável page é inicializada com o valor 1. Essa variável será usada para percorrer as diferentes páginas da lista de proxies.
4. O código entra em um loop while True, que será executado até que não haja mais botões "próxima página" na página.
5. Dentro do loop, é feita uma requisição HTTP para obter o conteúdo HTML da página atual da lista de proxies usando a função requests.get(). A URL é construída dinamicamente com base no número da página.
6. O código cria um objeto BeautifulSoup a partir do conteúdo HTML da página usando o parser 'lxml'.
7. O código encontra a tabela que contém os proxies na página usando o método find() do objeto BeautifulSoup. Em seguida, encontra todas as linhas da tabela usando o método find_all().
8. Um loop for é usado para percorrer todas as linhas da tabela, começando a partir do índice 1. Isso é feito para ignorar o cabeçalho da tabela.
9. Dentro do loop, as colunas de cada linha são encontradas usando o método find_all() novamente. As informações relevantes, como IP, porta, protocolo e país, são extraídas das colunas usando a propriedade text.
10. Verifica-se se o protocolo é "yes" e se o país é "elite proxy" ou "anonymous". Se essas condições forem atendidas, um dicionário contendo as informações do proxy é criado e adicionado à lista proxyList.
11. O código verifica se há um botão "próxima página" na página atual usando o método find() do objeto BeautifulSoup. Se não houver, o loop é interrompido com a instrução break.
12. Caso haja um botão "próxima página", o valor da variável page é incrementado em 1 e o loop continua para a próxima iteração.
13. Depois de sair do loop, a lista proxyList é convertida em uma string JSON usando a função json.dumps().
14. Em seguida, o código abre um arquivo chamado "proxies.json" no modo de escrita e escreve a string JSON no arquivo usando o método write() do objeto de arquivo.
15. Por fim, o código exibe o número total de proxies salvos usando a função len() para contar o número de elementos na lista proxyList.

## Requisitos
Para executar este código, você precisa ter as seguintes bibliotecas instaladas:
- requests
- BeautifulSoup
- json

## Como funciona essas bibliotecas?
- requests:
  - A biblioteca "requests" é amplamente utilizada para fazer requisições HTTP em Python.
  - Ela permite enviar solicitações a servidores e obter respostas.
  - Com o "requests", você pode enviar solicitações GET, POST, PUT, DELETE, etc., e também enviar parâmetros e cabeçalhos personalizados.
  - A biblioteca facilita o trabalho com APIs web, a coleta de dados de páginas da web e muito mais.
  - Documentação da biblioteca: https://requests.readthedocs.io/en/latest/
    
- BeatifulSoup:
  - O "BeautifulSoup" é uma biblioteca de análise HTML e XML em Python.
  - Ele ajuda a extrair dados de documentos HTML/XML de forma fácil e eficiente.
  - Com o "BeautifulSoup", você pode percorrer a estrutura de um documento HTML/XML e extrair informações específicas.
  - Ele fornece métodos para buscar, filtrar e manipular elementos HTML/XML com base em tags, classes, IDs, atributos, etc.
  - É amplamente utilizado em projetos de web scraping, onde você precisa extrair dados de sites.
  - Documentação da biblioteca: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

- json:
  - JSON (JavaScript Object Notation) é um formato de dados muito comum e fácil de ler e escrever.
  - A biblioteca "json" em Python fornece métodos para trabalhar com JSON.
  - Você pode usar essa biblioteca para serializar (converter) objetos Python em JSON e vice-versa.
  - Com o "json", você pode carregar dados JSON de um arquivo ou uma string, bem como salvar dados Python em um formato JSON.
  - Documentação da biblioteca: https://www.json.org/json-pt.html

## Executando o código:
Para executar o código, basta executar o arquivo Python. O arquivo "proxies.json" será gerado no diretório onde o código está sendo executado. Certifique-se de ter permissão de escrita no diretório.
