public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        Professor professor;
        professor = new Professor();
        professor.setNome("Franz");
        professor.setMatricula(1);
        professor.setCargaHoraria(8);

        Professor p2;
        p2 = new Professor("Marcelo");

        Professor p3;
        p3 = new Professor("Matheus", 12);

        System.out.println(professor.mostraProfessor());
        System.out.println(p2.mostraProfessor());
        System.out.println(p3.mostraProfessor());
    }
}
