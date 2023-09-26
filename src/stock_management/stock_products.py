"""
Stock Products: Utility module for generating stock reports in PDF format.

This module provides functionality for generating PDF reports of available products in the stock.

Functions:
    generate_pdf: Generates a PDF report of available products in the stock.
    available_products: Function to generate the PDF report of available products.

Usage:
    The 'available_products' function generates a PDF report of available products in the stock.
    You can specify the destination folder for the report. If no folder is provided, it will use the default folder.

Examples:
    To generate a PDF report of available products directly:
    available_products(destination_folder='../../reports/stock_reports')

    To generate a PDF report of available products in the default folder:
    available_products()

"""


from database.database import get_all_items
from fpdf import FPDF
from datetime import date


def generate_pdf(products, destination_folder, pdf=FPDF()):
    """
        Generates a PDF report of available products in the stock.

        Args:
            products (list): A list of product information as tuples (id, name, price).
            destination_folder (str): The destination folder for saving the PDF report.
            pdf (FPDF, optional): An FPDF instance for creating the PDF report. Defaults to FPDF().

        Returns:
            None
        """

    # Get today's date in the 'YYYY-MM-DD' format
    todays_date = date.today().strftime('%Y-%m-%d')

    # Define the destination PDF file path including today's date
    filename = f'{destination_folder}/stock_{todays_date}.pdf'

    # Create a PDF instance
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Define column widths
    col_widths = [20, 80, 30]  # Adjust these widths as needed

    # Add a header row
    pdf.cell(col_widths[0], 10, "ID", border=1)
    pdf.cell(col_widths[1], 10, "Name", border=1)
    pdf.cell(col_widths[2], 10, "Price", border=1)
    pdf.ln()

    # Add product data
    for product in products:
        for i in range(3):
            pdf.cell(col_widths[i], 10, str(product[i]), border=1)
        pdf.ln()

    # Output the PDF to the specified destination
    pdf.output(filename)
    print('PDF report generated successfully.')


def available_products(destination_folder=None):
    """
    Function to generate the PDF report of available products.

    Args:
        destination_folder (str, optional): The destination folder for saving the PDF report.
            If not provided, it will use the default folder.

    Returns:
        None
    """

    if not destination_folder:
        destination_folder = 'reports/stock_reports'
    products = get_all_items()
    # [(1, 'Coca-Cola', 125), (2, 'Snickers', 250), (66, 'Twix', 9), (13, 'Fanta', 4.5), (12, 'Backpack (Nike)', 400.5)]
    generate_pdf(products, destination_folder=destination_folder)


if __name__ == '__main__':
    available_products(destination_folder='../../reports/stock_reports')
