# Anotações 05/09

- Normalização
  - é uma regra dos bancos de dados utilizada para evitar a **redundância** de dados
  - forma normal: regra que deve ser obedecida
  - um projeto de banco de dados está na *n*FN se as tabelas respeitam a forma normal do determinado nível
  - 1FN: não pode ter atributos dívisiveis
  - 2FN: os dados dependem da chave primária, só é necessário verificar se houver chave composta 
  - 3FN: não pode ter um atributo dependendo de outro atributo que não a chave
  - BCNF: é uma generalização da 3FN, todos os atributos da tabela precisam depender da chave
  - 4FN: não há dependências multivaloradas
  - 5FN: está na 4FN e pode ser decomposta sem grandes perdas