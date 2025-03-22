class Professor {
    private String nome;
    private int matricula;
    private int cargaHoraria;

    public Professor() {

    }

    public Professor(String n) {
        this.nome = n;
    }

    public Professor(String n, int c) {
        this.nome = n;
        this.cargaHoraria = c;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getMatricula() {
        return matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public int getCargaHoraria() {
        return cargaHoraria;
    }
    public void setCargaHoraria(int cargaHoraria) {
        this.cargaHoraria = cargaHoraria;
    }

    public String mostraProfessor() {
        String dados = "";
        dados += "Nome: " + this.nome;
        dados += "\nMatrícula: " + this.matricula;
        dados += "\nCarga Horária: " + this.cargaHoraria;
        dados += "\nCarga Horária Mensal: " + this.cargaHorariaMensal();
        return dados;
    }

    public Float cargaHorariaMensal(){
        return this.cargaHoraria * 4.5f;
    }

    @Override
    public String toString() {
        String r = "";
        r += this.nome;
        r += this.matricula;
        r += this.cargaHoraria;
        return r;
    }
}

