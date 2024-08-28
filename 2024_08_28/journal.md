# Anotações 28/08

- Restrições de Integridade
  - validar os atributos
  - identificar unicamente os registros
  - garantir a validade dos relacionamentos
  - garantir que não haja redundância

- Restrições baseadas em esquema
  - restrições de domínio
  - restrições de entidade
  - restrições referenciais

- Integridade de Domínio
  - Domínio
    - o conjunto de valores
  - garante que somente valores recebidos por cada atributo da entidade sejam de um tipo e estejam presentes no domínio
  - o domínio pode ser finito ou infinito
  - um domínio persistido no banco de dados representa um recorte temporal do cenário abordado

- Integridade de Entidade/Identificação
  - cada entidade tem uma ***chave primária***(primary key, **PK**) não nula que identifica de forma exclusiva suas ocorrências
  - dentro de cada *tupla*, o valor de cada atributo A deve ser indivisível do domínio dom(A)
  - a identificação da tupla é feita por meio as chaves
  - uma entidade tem um ou mais atributos com valores distintos que servem para que seja identificada no conjunto de entidades
  - atributos como CPF, RG, placa de carro, são bons candidatos para chaves
  - na modelagem conceitual, a chave primária é identificada com uma bolinha preta
  - quando as entidades não possuem um candidato a chave, combina-se dois atributos para criar uma chave composta
  - também é posssível criar um atributo identificador único de chave substituta(surrogate key)

- Integridade Referencial
  - 