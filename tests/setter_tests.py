import webbrowser

from src.supermarket_information.supermarket_customization import SupermarketDetails

filepath = r'C:\Users\Hardy\Desktop\logo.png'
SupermarketDetails.set_supermarket_logo(filepath)

webbrowser.open(filepath)