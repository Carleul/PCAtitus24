# Anotações 26/09

- Atributos de Classe ou de Instância
  - classe: atributo comum a todos os objetos da classe
    - é vantajoso pois só armazena o valor uma vez na memória
    - são definidos antes do construtor
  - instância: valor exclusivo à instância
    - definidos dentro do construtor
  - método de instancia
    - metodos comuns de uma classe, recebem self como primeiro parametro
  - métodos de classe
    - metodos marcados com o decorator @classmethod
    - recebem a própria classe como primeiro argumento, nomeado de cls(convenção)
  - métodos estáticos
    - não recebe nem self e nem a própria classe como primeiro parametro
    - usam o decorator com @staticmethod
    - métodos estáticos não podem acessar ou alterar o estado da instância de uma classe