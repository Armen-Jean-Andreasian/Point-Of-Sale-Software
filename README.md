# Point of Sale (POS) Software

## Description

This Point of Sale (POS) software project streamlines the sales process for businesses. It allows users to input product information via barcode scanning, accesses a MySQL database to retrieve item details, and generates receipts in both text and PDF formats. The software calculates the total amount to be paid and provides a printable receipt in PDF format that can be adapted to different receipt printing machines.

## Features

- Manual input for quick product identification. (Which should be substituted with Barcode input, depending on the software the store uses)
- Accesses a MySQL database to fetch item information (id, name, price).
- Generates itemized receipts with product name, quantity, and price per item.
- Calculates and displays the total amount to be paid.
- Automatically generates PDF receipts for easy printing.

## Technologies Used

- **Programming Language:** Python
- **Database:** MySQL
- **PDF Generation:** [FPDF Library](https://pyfpdf.readthedocs.io/en/latest/)
- **Barcode Scanning:** (manual input for now)
