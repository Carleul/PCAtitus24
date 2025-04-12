import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class App {
    static App app = new App();
    public static void main(String[] args) throws Exception {
        System.out.println("Bem-vindo ao sistema de arquivos!");
        Scanner teclado = new Scanner(System.in);
        while(true){
            System.out.println("Escolha uma opção:");
            System.out.println("1. Escrever no arquivo(apaga tudo)");
            System.out.println("2. Anexar no arquivo");
            System.out.println("3. Ler a primeira linha");
            System.out.println("4. Ler todas as linhas");
            System.out.println("9. Sair");
            System.out.print("Escolha uma opção: ");
            int op = teclado.nextInt();
            switch (op) {
                case 1:
                    app.escreve(false, "");
                    break;
                case 2:
                    app.escreve(true, "sata andagi");
                    break;
                case 3:
                    app.lePrimeiraLinha();
                    break;
                case 4:
                    app.leTudo();
                    break;
                case 9:
                    System.exit(0);
                    break;
                default:
                    break;
            }
        }

    }
    // escrevendo em arquivo;
    public void escreve(Boolean tipo, String conteudo){
        try {
            FileWriter filew;
            filew = new FileWriter("arquivo.txt",tipo);
            filew.write(conteudo + "\n");
            filew.close();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public void lePrimeiraLinha(){
        try {
            FileReader filer = new FileReader("arquivo.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            System.out.println(line);
            buffer.close();
            filer.close();
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    public void leTudo(){
        try {
            FileReader filer = new FileReader("arquivo.txt");
            BufferedReader buffer = new BufferedReader(filer);
            String line = buffer.readLine();
            while (line!= null) {
                System.out.println(line);
                line = buffer.readLine();
            }
            buffer.close();
            filer.close();
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }
}
