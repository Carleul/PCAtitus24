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