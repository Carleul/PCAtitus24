import java.util.ArrayList;
import java.util.Collections;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        ArrayList<Aluno> alunos;
        Aluno a1 = new Aluno("Alberto", 17, 8.0);
        Aluno a2 = new Aluno("Bruno", 18, 9.0);
        Aluno a3 = new Aluno("Camila", 17, 7.0);
        Aluno a4 = new Aluno("Daniel", 16, 10.0);

        alunos = new ArrayList<>();
        alunos.add(a1);
        alunos.add(a2); 
        alunos.add(a3);
        alunos.add(a4);

        System.out.println(alunos);
        Collections.sort(alunos);
        System.out.println(alunos);
        ComparadorPorIdade cpi = new ComparadorPorIdade();
        alunos.sort(cpi);
        System.out.println(alunos);
        ComparadorPorNome cpn = new ComparadorPorNome();
        alunos.sort(cpn);
        System.out.println(alunos);
    }
}
