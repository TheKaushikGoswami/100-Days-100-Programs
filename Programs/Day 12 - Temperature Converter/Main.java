import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            double temperature;
            int choice;
            while (true) {
                System.out.println("\nChoose conversion type: ");
                System.out.println("1. Celsius to Fahrenheit");
                System.out.println("2. Fahrenheit to Celsius");
                System.out.println("3. Celsius to Kelvin");
                System.out.println("4. kelvin to Celsius");
                System.out.println("5. Kelvin to Fahrenheit");
                System.out.println("6. Fahrenheit to Kelvin");
                System.out.println("7. Exit");
                choice = sc.nextInt();
                switch (choice) {
                    case 1:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double CF = (temperature * 9 / 5) + 32;
                        System.out.println(temperature + " Celsius is equal to " + CF + " Fahrenheit.");
                        break;
                    case 2:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double FC = (temperature - 32) * 5 / 9;
                        System.out.println(temperature + " Fahrenheit is equal to " + FC + " Celsius.");
                        break;
                    case 3:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double CK = temperature + 273.15;
                        System.out.println(temperature + " Celsius is equal to " + CK + " Kelvin.");
                        break;
                    case 4:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double KC = temperature - 273.15;
                        System.out.println(temperature + " Kelvin is equal to " + KC + " Celsius.");
                        break;
                    case 5:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double KF = (temperature - 273.15) * 9 / 5 + 32;
                        System.out.println(temperature + "Kelvin  is equal to " + KF + " Fahrenheit.");
                        break;
                    case 6:
                        System.out.println("Enter the temperature: ");
                        temperature = sc.nextDouble();
                        double FK = (temperature - 32) * 5 / 9 + 273.15;
                        System.out.println(temperature + " Fahrenheit is equal to " + FK + " Kelvin.");
                        break;
                    case 7:
                        System.out.println("Thank you for visiting");
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice.");
                        break;
                }
            }
        }
    }
}