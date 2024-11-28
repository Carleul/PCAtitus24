# Anotações 29/08

- chaves estrangeiras
  - quando (1,1), botar a chave na entidade contrária
  - quando as duas cardinalidades terminam em N, as chaves ficam no relacionamento
    - essas chaves vão representar uma outra tabela

- Integridade de Relacionamento: Generalização
  - total (t)
    - precisa da ocorrencia de ao menos uma das especializadas
  - parcial (p)
    - não precisa da ocorrência de nenhuma das especializadas
  - +
  - exclusivo (d)
    - toda ocorrência da generalizada pode ser ocorrência de no máximo uma especializada
  - interseção (c)
    - uma ocorrência da generalizada pode ser ocorrência de várias especializadas

- Verificando as Restrições
  - elas vão ocorrer quando houver modificação ou alteração do banco de dados
    - Inserção de dados
    - Remoção de dados
    - Alteração de dados

- Modelo Lógico
  - o ato de transformar a modelagem conceitual em tabelas
  - entidades viram tabelas, e seus atributos vão compor as colunas
  - quando há atributos compostos, há a possibilidade de aplainar ou combinar
    - aplainar: transforma cada subatributo em uma coluna diferente
    - combinar: fazer somente uma coluna com o atributo pai