import java.util.ArrayList;
import java.util.Scanner;

class Product {
    String name;
    int quantity;
    double price;

    Product(String name, int quantity, double price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    double getTotal() {
        return quantity * price;
    }
}

public class ShoppingBill {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Product> productList = new ArrayList<>();

        System.out.println("===== Welcome to Shopping Bill System =====");

        while (true) {
            System.out.print("\nEnter Product Name: ");
            String name = scanner.nextLine();

            System.out.print("Enter Quantity: ");
            int quantity = Integer.parseInt(scanner.nextLine());

            System.out.print("Enter Price per unit: ");
            double price = Double.parseDouble(scanner.nextLine());

            productList.add(new Product(name, quantity, price));

            System.out.print("Add another product? (yes/no): ");
            String choice = scanner.nextLine();
            if (!choice.equalsIgnoreCase("yes")) {
                break;
            }
        }

        // Generate the Bill
        System.out.println("\n\n========== Final Bill ==========");
        System.out.printf("%-20s %-10s %-10s %-10s\n", "Product", "Quantity", "Price", "Total");

        double grandTotal = 0;
        for (Product p : productList) {
            double total = p.getTotal();
            grandTotal += total;
            System.out.printf("%-20s %-10d %-10.2f %-10.2f\n", p.name, p.quantity, p.price, total);
        }

        System.out.println("-------------------------------------------");
        System.out.printf("%-42s %.2f\n", "Grand Total:", grandTotal);
        System.out.println("===========================================");

        scanner.close();
    }
}
