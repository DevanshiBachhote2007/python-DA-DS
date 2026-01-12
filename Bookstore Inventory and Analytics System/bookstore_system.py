# Bookstore Inventory and Analytics System

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Bookstore:
    def __init__(self, inventory_file='inventory.csv', sales_file='sales.csv'):
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.inventory = self.load_inventory()
        self.sales = self.load_sales()

    def load_inventory(self):
        try:
            return pd.read_csv(self.inventory_file)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Title', 'Author', 'Genre', 'Price', 'Quantity'])

    def load_sales(self):
        try:
            return pd.read_csv(self.sales_file)
        except FileNotFoundError:
            return pd.DataFrame(columns=['Date', 'Title', 'Quantity Sold', 'Total Revenue'])

    def save_inventory(self):
        self.inventory.to_csv(self.inventory_file, index=False)

    def save_sales(self):
        self.sales.to_csv(self.sales_file, index=False)

    def add_book(self, title, author, genre, price, quantity):
        if price <= 0 or quantity < 0:
            print("Error: Price must be positive and quantity non-negative.")
            return
        if title in self.inventory['Title'].values:
            print(f"Book '{title}' already exists. Use update_inventory to change quantity.")
            return
        new_book = pd.DataFrame({'Title': [title], 'Author': [author], 'Genre': [genre], 'Price': [price], 'Quantity': [quantity]})
        self.inventory = pd.concat([self.inventory, new_book], ignore_index=True)
        self.save_inventory()
        print(f"Book '{title}' added successfully.")

    def update_inventory(self, title, quantity):
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
        if title not in self.inventory['Title'].values:
            print(f"Book '{title}' not found in inventory.")
            return
        self.inventory.loc[self.inventory['Title'] == title, 'Quantity'] = quantity
        self.save_inventory()
        print(f"Inventory for '{title}' updated to {quantity}.")

    def record_sale(self, title, quantity):
        if title not in self.inventory['Title'].values:
            print(f"Book '{title}' not found in inventory.")
            return
        current_stock = self.inventory.loc[self.inventory['Title'] == title, 'Quantity'].values[0]
        if quantity > current_stock:
            print(f"Error: Not enough stock. Available: {current_stock}")
            return
        price = self.inventory.loc[self.inventory['Title'] == title, 'Price'].values[0]
        revenue = price * quantity
        date = input("Enter sale date (YYYY-MM-DD, e.g., 2026-01-12): ")
        new_sale = pd.DataFrame({'Date': [date], 'Title': [title], 'Quantity Sold': [quantity], 'Total Revenue': [revenue]})
        self.sales = pd.concat([self.sales, new_sale], ignore_index=True)
        self.inventory.loc[self.inventory['Title'] == title, 'Quantity'] -= quantity
        self.save_inventory()
        self.save_sales()
        print(f"Sale recorded: {quantity} of '{title}' for ${revenue:.2f}")

    def generate_report(self):
        print("\n--- Inventory Report ---")
        print(f"Total books: {len(self.inventory)}")
        print(f"Total stock: {self.inventory['Quantity'].sum()}")
        print(f"Total value: ${self.inventory['Price'].sum() * self.inventory['Quantity'].sum():.2f}")

        print("\n--- Sales Report ---")
        if not self.sales.empty:
            total_revenue = self.sales['Total Revenue'].sum()
            total_sold = self.sales['Quantity Sold'].sum()
            print(f"Total revenue: ${total_revenue:.2f}")
            print(f"Total books sold: {total_sold}")
            best_seller = self.sales.groupby('Title')['Quantity Sold'].sum().idxmax()
            print(f"Best-selling book: {best_seller}")
        else:
            print("No sales data available.")

# Additional functions for analysis and visualization

def analyze_total_revenue(bookstore):
    sales = bookstore.sales
    if sales.empty:
        print("No sales data to analyze.")
        return

    # Using NumPy for computations
    revenues = np.array(sales['Total Revenue'])
    total_revenue = np.sum(revenues)
    avg_revenue = np.mean(revenues)
    print(f"\nTotal Revenue: ${total_revenue:.2f}")
    print(f"Average Revenue per Sale: ${avg_revenue:.2f}")

def analyze_revenue_by_genre(bookstore):
    sales = bookstore.sales
    if sales.empty:
        print("No sales data to analyze.")
        return

    # Pandas analysis
    sales_by_genre = sales.merge(bookstore.inventory[['Title', 'Genre']], on='Title').groupby('Genre')['Total Revenue'].sum()
    print("\nRevenue by Genre:")
    print(sales_by_genre)

def analyze_monthly_sales(bookstore):
    sales = bookstore.sales.copy()
    if sales.empty:
        print("No sales data to analyze.")
        return

    try:
        sales['Date'] = pd.to_datetime(sales['Date'])
        monthly_sales = sales.groupby(sales['Date'].dt.to_period('M'))['Total Revenue'].sum()
        print("\nMonthly Sales:")
        print(monthly_sales)
    except Exception as e:
        print(f"Error analyzing monthly sales: {e}")

def visualize_bar_chart(bookstore):
    sales = bookstore.sales
    inventory = bookstore.inventory
    if sales.empty or inventory.empty:
        print("Insufficient data for visualization.")
        return

    sales = sales.merge(inventory[['Title', 'Genre', 'Author']], on='Title')

    # Bar Chart: Total sales by genre
    plt.figure(figsize=(10, 6))
    sales_by_genre = sales.groupby('Genre')['Total Revenue'].sum()
    sales_by_genre.plot(kind='bar', color='skyblue')
    plt.title('Total Sales by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Total Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_line_graph(bookstore):
    sales = bookstore.sales
    inventory = bookstore.inventory
    if sales.empty or inventory.empty:
        print("Insufficient data for visualization.")
        return

    sales = sales.merge(inventory[['Title', 'Genre', 'Author']], on='Title')

    # Line Graph: Monthly sales trends
    try:
        sales['Date'] = pd.to_datetime(sales['Date'])
        monthly_sales = sales.groupby(sales['Date'].dt.to_period('M'))['Total Revenue'].sum()
        plt.figure(figsize=(10, 6))
        monthly_sales.plot(kind='line', marker='o')
        plt.title('Monthly Sales Trends')
        plt.xlabel('Month')
        plt.ylabel('Total Revenue ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating line graph: {e}")

def visualize_pie_chart(bookstore):
    sales = bookstore.sales
    inventory = bookstore.inventory
    if sales.empty or inventory.empty:
        print("Insufficient data for visualization.")
        return

    sales = sales.merge(inventory[['Title', 'Genre', 'Author']], on='Title')

    # Pie Chart: Revenue share by genre
    plt.figure(figsize=(8, 8))
    sales_by_genre = sales.groupby('Genre')['Total Revenue'].sum()
    sales_by_genre.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Revenue Share by Genre')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

def visualize_heatmap(bookstore):
    sales = bookstore.sales
    inventory = bookstore.inventory
    if sales.empty or inventory.empty:
        print("Insufficient data for visualization.")
        return

    sales = sales.merge(inventory[['Title', 'Genre', 'Author']], on='Title')

    # Heatmap: Correlation between book prices and sales volumes
    # Need to aggregate sales per book
    book_sales = sales.groupby('Title').agg({'Quantity Sold': 'sum', 'Total Revenue': 'sum'})
    book_sales = book_sales.merge(inventory[['Title', 'Price']], on='Title')
    corr_data = book_sales[['Price', 'Quantity Sold']]
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation between Price and Quantity Sold')
    plt.tight_layout()
    plt.show()

# Main menu for user interaction
def main():
    bookstore = Bookstore()
    print("=====Welcome to the Bookstore Inventory and Analytics System!=====")

    while True:
        print("\n--- Bookstore Inventory and Analytics System ---")
        print("1. Add Book")
        print("2. Update Inventory")
        print("3. Record Sale")
        print("4. Generate Report")
        print("5. Analyze Sales")
        print("6. Visualize Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title (e.g., 'The Great Gatsby'): ")
            author = input("Author (e.g., 'F. Scott Fitzgerald'): ")
            genre = input("Genre (e.g., 'Fiction'): ")
            price = float(input("Price (e.g., 12.99): "))
            quantity = int(input("Quantity (e.g., 50): "))
            bookstore.add_book(title, author, genre, price, quantity)
        elif choice == '2':
            title = input("Title (e.g., 'The Great Gatsby'): ")
            quantity = int(input("New Quantity (e.g., 45): "))
            bookstore.update_inventory(title, quantity)
        elif choice == '3':
            title = input("Title (e.g., 'The Great Gatsby'): ")
            quantity = int(input("Quantity Sold (e.g., 5): "))
            bookstore.record_sale(title, quantity)
        elif choice == '4':
            bookstore.generate_report()
        elif choice == '5':
            while True:
                print("\n--- Analyze Sales ---")
                print("1. Total Revenue")
                print("2. Revenue by Genre")
                print("3. Monthly Sales")
                print("4. Back to Main Menu")

                sub_choice = input("Enter sub-choice: ")
                if sub_choice == '1':
                    analyze_total_revenue(bookstore)
                elif sub_choice == '2':
                    analyze_revenue_by_genre(bookstore)
                elif sub_choice == '3':
                    analyze_monthly_sales(bookstore)
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid sub-choice. Try again.")
        elif choice == '6':
            while True:
                print("\n--- Visualize Data ---")
                print("1. Bar Chart: Total Sales by Genre")
                print("2. Line Graph: Monthly Sales Trends")
                print("3. Pie Chart: Revenue Share by Genre")
                print("4. Heatmap: Correlation between Price and Quantity Sold")
                print("5. Back to Main Menu")

                sub_choice = input("Enter sub-choice: ")
                if sub_choice == '1':
                    visualize_bar_chart(bookstore)
                elif sub_choice == '2':
                    visualize_line_graph(bookstore)
                elif sub_choice == '3':
                    visualize_pie_chart(bookstore)
                elif sub_choice == '4':
                    visualize_heatmap(bookstore)
                elif sub_choice == '5':
                    break
                else:
                    print("Invalid sub-choice. Try again.")
        elif choice == '7':
            print("==========Exiting the system. Goodbye!==========")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()