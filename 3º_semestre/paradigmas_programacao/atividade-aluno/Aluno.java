public class Aluno implements Comparable<Aluno>{
    private String nome;
    private Integer idade;
    private Double notaFinal;

    public String getNome() {
        return nome;
    }
    public Integer getIdade() {
        return idade;
    }
    public Double getNotaFinal() {
        return notaFinal;
    }

    public Aluno(){
        
    }

    public Aluno(String nome, Integer idade, Double notaFinal){
        this.nome = nome;
        this.idade = idade;
        this.notaFinal = notaFinal;
    }

    @Override
    public int compareTo(Aluno a1){
        int r;
        r = Double.compare(this.notaFinal, a1.notaFinal);
        return r;
    }

    @Override
    public String toString(){
        String r = "";
        r += this.nome + " " + this.idade + " " + this.notaFinal;
        return r;
    }
}

