# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo tabela hash (Hash Table) com tratamento de colisão por endereco aberto (Open Addressing) com sondagem quadrática (Quadratic Probing);
- Implementar e validar os conceitos relacionados ao métodos de estruturas de dados tabela hash com capacidade.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_tabela_hash.py -v
```

O pytest permite que você realize o teste sobre métodos específicos da sua estrutura de dados lista duplamente ligada. Portanto, também é válido o comando:

```console
$ pytest test/test_tabela_hash.py -k find -v --no-header
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe TabelaHashEnderecamentoAberto** no arquivo **tabela_hash.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

A prioridade com a qual os itens devem ser inseridos na fila é a seguinte:
- Os itens com maior valor de prioridade devem ocupar as primeiras posições na fila;
- Caso dois itens possuam a mesma prioridade, aquele que foi inserido primeiro deverá ter maior prioridade na fila para ser removido;

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **20pts**, o que corresponde a **20pts%** da nota da segunda etapa. Confira também a distribuição dos pontos no arquivo test_tabela_hash.py.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo tabela hash com tratamento de colisão por endereçamento aberto com sondagem quadrática;
- [ ] **(0pts)** Implementar o método **__find()**
  - [ ] Deve retornar a posição do item (Nó) no índice da tabela hash a partir da chave que foi passada como parâmetro para a busca
  - [ ] Caso o item (Nó) NÃO seja encontrado na tabela hash o método deve retornar o valor -1
  - OBS: Por se tratar de um método privado, a pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo 
- [ ] **(6pts)** Implementar o método **get()**
  - [ ] Deve retornar o valor do item (Nó) a partir da chave que foi passada como parâmetro para a busca
  - [ ] Caso o item (Nó) NÃO seja encontrado na tabela hash o método deve retornar o valor None
- [ ] **(6pts)** Implementar o método **insert()**, o qual deve receber como parâmetros de entrada uma chave e um valor
  - [ ] O método deve criar um objeto Nó a partir dos valores recebido pelo método e inserir o item (Nó) na tabela hash
  - [ ] Caso a tabela hash esteja cheia o método deverá retornar um boolean False, indicando que não foi possível inserir o item (Nó) na tabela hash
  - [ ] Caso seja possível inserir o item (Nó) na tabela hash, inserir o nó e retornar um boolean True
- [ ] **(6pts)** Implementar o método **remove()**, o qual deve remover o primeiro item da tabela hash, caso ela não esteja vazia 
  - [ ] Caso a tabela hash esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso a tabela hash esteja vazia deverá retornar o primeiro Nó da fila
- [ ] **(2pts)** Implementar o método **display()**, o qual deve retornar uma lista de todos os itens (Nós) da tabela hash
  - [ ] Caso a tabela hash esteja vazia deverá retornar uma lista vazia []
  - [ ] Caso a tabela hash NÃO esteja vazia deverá retornar uma lista com todos os itens (Nós) da tabela hash
- [ ] **(0pts)** Implementar o método **__hash()**, o qual deve retornar um int com o valor do hash da chave passada como parâmetro
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo
- [ ] **(0pts)** Implementar o método **__hash2()**, o qual deve retornar um int com o valor do hash da chave e valor k passados como parâmetro
  - [ ] A implementação desse método deve ser diferente da implementação do método hash() utilizando a mesma chave como parâmetro e sondagem quadrática
  - OBS: A pontuação da implementação desse método está implícita na pontuação do método que faz uso do mesmo