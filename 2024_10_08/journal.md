# Anotações 08/10

- Tratamento de Exceções

  - exceptions são acontecimentos que interrompem o fluxo normal da execução do código
  - as exceptions servem para que a aplicação não quebre quando ocorrer um erro inesperado
  - situações inesperadas podem ser falha de conexão com o banco, API externa fora do ar, etc.
  - as exceptions derivam da classe imbutida no python: BaseException
  - exemplos: FileNotFoundError, TypeError, ZeroDivisionError, etc.
  - try, except, else, finally
  - raise
  - é possível criar classes personalizadas derivando de Exception
  - ex: class CpfInvalidoError(Exception):