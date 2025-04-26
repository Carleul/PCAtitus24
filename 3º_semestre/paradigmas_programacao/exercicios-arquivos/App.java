import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class App {
    static App app = new App();
    public static void main(String[] args) {
        escreve3(false, "Paradigmas de Linguagens de Programação");
        escreve3(true, "Desafio da Comunicação");
        escreve3(true, "Otimização de Banco de Dados");
        escreve3(true, "Engenharia de Software");

        escreve1(false, "Pensamento Computacional");
        escreve1(true, "Inteligência Artificial");
        escreve1(true, "Desafio da Profissão");
        for (int i = 5; i <= 20; i++) {
            escreve1(true, i + ",");
        }
        escreve1(true, "Números pares até 50:");
        for (int i = 2; i <= 50; i += 2) {
            escreve1(true, i + ",");
        }

        app.lePrimeiraLinha();
        app.leSegundaLinha();
        System.out.println("------------------------------------");
        System.out.println("Disciplinas do 3 semestre:");
        app.leTudo();
        System.out.println("------------------------------------");
        System.out.println("linhas impares:");
        leImpares();
        System.out.println("------------------------------------");
        System.out.println("penultima linha:");
        lePenultima();

    }

    public static void escreve3(Boolean tipo, String conteudo) {
        try {
            FileWriter filew = new FileWriter("disciplinas3.txt", tipo);
            filew.write(conteudo + "\n");
            filew.close();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public static void escreve1(Boolean tipo, String conteudo) {
        try {
            FileWriter filew = new FileWriter("disciplinas1.txt", tipo);
            filew.write(conteudo + "\n");
            filew.close();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public void lePrimeiraLinha(){
        try {
            FileReader filer = new FileReader("disciplinas3.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            System.out.println("Primeira Linha -> " + line);
            buffer.close();
            filer.close();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public void leSegundaLinha(){
        try {
            FileReader filer = new FileReader("disciplinas3.txt");
            BufferedReader buffer = new BufferedReader(filer);
            buffer.readLine(); // <- ignorando a pimeira linha
            String line = buffer.readLine();
            buffer.close();
            filer.close();
            System.out.println("Segunda Linha -> " + line);
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public void leTudo(){
        try {
            FileReader filer = new FileReader("disciplinas3.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            while (line!= null) {
                System.out.println(line);
                line = buffer.readLine();
            }
            buffer.close();
            filer.close();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public static void leImpares() {
        try (BufferedReader br = new BufferedReader(new FileReader("disciplinas3.txt"))) {
            String line;
            int numberLine = 1;
            while ((line = br.readLine()) != null) {
                if (numberLine % 2 != 0) {
                    System.out.println(numberLine + "- " + line);
                }
                numberLine++;
            }
        } catch (IOException e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }

    public static void lePenultima() {
        try (BufferedReader br = new BufferedReader(new FileReader("disciplinas3.txt"))) {
            String line;
            String penultima = null;
            while ((line = br.readLine()) != null) {
                if (br.ready()) {
                    penultima = line;
                }
            }
            System.out.println(penultima);
        } catch (IOException e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }
}
