# Anotações 27/08

- Cardinalidade
  - Dentro de um domínio pode existir um atributo obrigatório ou opcional, que pode ser mono ou multi valorado

  - Os relacionamentos tem uma cardinalidade que indica quantas instâncias de uma entidade podem se relacionar com instâncias de outra entidade
    - um pra um
    - um pra muitos
    - muitos pra muitos

  - A cardinalidade é representada pela tupla (min, max)

  - Atributos
    - (0,1) mono e opcional
    - (0,N) multi e opcional
    - (1,1) mono e obrigatório
    - (1,N) multi e obrigatório
    - quando não está escrito, vai ser (1,1)
  
- Generalização
  - abstrair características de duas ou mais entidades para criar uma entidade pai
  - ex: criar a entidade "cadastro" de "aluno" e "professor"

- Especialização
  - criar entidades mais específicas a partir de uma entidade geral
  - ex: criar entidades "pessoa física" e "empresa" de uma entidade "cliente"

- Tanto generalização quanto especialização são representados da mesma forma, com um triângulo

- Tipos de relacionamento
  - Total
    - obrigatoriamente a entidade pai será uma entidade filha
  - Parcial
    - nem sempre a entidade pai será uma entidade filha
  