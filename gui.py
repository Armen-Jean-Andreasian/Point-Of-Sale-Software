import tkinter as tk
from tkinter import messagebox
from src.point_of_sales.pdf.current_time import Time
from src.supermarket_information.supermarket_customization import SupermarketDetails
from src.point_of_sales.pdf.pdf_composer import PdfGenerator
from src.point_of_sales.counter import BarcodeScanner
from src.stock_management.product_registration import stock_registration
from src.supermarket_information.customizing import customize


class PointOfSaleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Point of Sale System")
        self.supermarket_information = SupermarketDetails.get_supermarket_details()
        self.current_time = Time.current_time()

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="1 - Add items").pack()
        tk.Label(self.root, text="2 - Check out products").pack()
        tk.Label(self.root, text="3 - Edit supermarket information").pack()
        tk.Label(self.root, text="4 - Exit the program").pack()

        tk.Button(self.root, text="Add items", command=self.add_items).pack()
        tk.Button(self.root, text="Check out products", command=self.checkout).pack()
        tk.Button(self.root, text="Edit supermarket information", command=self.edit_info).pack()
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def add_items(self):
        stock_registration()
        messagebox.showinfo("POS System", "Items added successfully.")

    def checkout(self):
        pay_for_products = BarcodeScanner()
        local_receipt, local_total = pay_for_products.point_of_sales()

        pdf_generator = PdfGenerator(
            receipt=local_receipt,
            total=local_total,
            supermarket=self.supermarket_information,
            current_time=self.current_time
        )
        pdf_generator.start()
        messagebox.showinfo("POS System", "Checkout successful. Receipt generated.")

    def edit_info(self):
        customize()
        messagebox.showinfo("POS System", "Supermarket information updated.")


if __name__ == '__main__':
    root = tk.Tk()
    app = PointOfSaleApp(root)
    root.mainloop()
