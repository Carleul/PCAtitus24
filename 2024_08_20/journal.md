# Anotações 20/08

- ACID
  - Atomicidade
    - uma transação é tudo ou nada, se uma transação não for inteiramente completa, por alguma falha do sistema, o banco de dados permanece inalterado
  - Consistência
    - uma transação leva o banco de dados de um estado válido para outro
  - Isolamento
    - transações permanecem invisíveis para outras pessoas até que quem esteja alterando conclua a operação
  - Durabilidade
    - uma vez que a transação for concluída, ela permanecerá assim mesmo que dê alguma falha no sistema

- Arquitetura de SGBDs
  - Autonomia Distribuição Heterogeneidade (ADH)
    - o serverless é brabo, tem o melhor de todas as 3 características

  - n-Camadas (3 ou mais camadas)
    - bom para aplicações
  - cliente/servidor
    - bom para jogos
  - serverless
    - bom na maioria das situações

- Criação de Banco de Dados
  - Definição de Negócio
    - modelagem conceitual

  - Definição de estrutura
    - modelagem lógica e física

  - Inserção e Busca de Dados
    - SQL

- MER
  - Entidades
    - objetos ou conceitos do mundo real com relevância para o sistema
    - coisa ou pessoa que pode ser individualmente identificada
    - ex: cliente, produto, loja...
  - Atributos
    - propriedades que descrevem uma entidade
    - podem ser simples ou compostos
    - cada atributo tem um domínio
    - ex: entidade: pessoa; atributos: nome, idade...