public class Utils {

    public static boolean validaCpf(String cpf) {
        return cpf.matches("\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}");
    }
    

    public static boolean validaTelefone(String telefone) {
        return telefone.matches("\\(\\d{2}\\) 9\\d{4}-\\d{4}");
    }
    
}