"""
Supermarket Customization Script

This script allows users to view and customize supermarket information using the SupermarketDetails class.

Menu Options:
- Users can choose to view or edit supermarket details.
- Viewing supermarket details displays the current details.
- Editing options allow users to change the logo, name, address, or operating hours.

Usage:
1. Run the script and follow the menu prompts.
2. Provide input as instructed to make changes.

"""

from src.supermarket_information.supermarket_customization import SupermarketDetails


def customize():
    while True:
        user_input = input('1 - View supermarket details \n'
                           '2 - Edit supermarket details\n'
                           '3 - Exit the program\n'
                           'Your Choice: ')
        match user_input:
            case '1':
                print('')
                print(SupermarketDetails.get_supermarket_details())
            case '3':
                break
            case '2':
                choice = input('1 - Change the logo  \n'
                               '2 - Edit supermarket name\n'
                               '3 - Edit supermarket address\n'
                               '4 - Edit operating hours\n'
                               '5 - Exit this menu'
                               'Your Choice: ')
                match choice:
                    case '1':
                        logo_path = input('Enter the logo location.\n'
                                          'Example: C://Users/Desktop/logo.png\n')
                        SupermarketDetails.set_supermarket_logo(logo_path)
                        print('Done')
                        print('')

                    case '2':
                        new_name = input('Enter the new name: ')
                        SupermarketDetails.set_supermarket_name(new_name)
                        print('Done')
                        print('')

                    case '3':
                        new_address = input('Enter the new address: ')
                        SupermarketDetails.set_supermarket_address(new_address)
                        print('Done')
                        print('')

                    case '4':
                        new_hours = input('Enter the new hours: ')
                        SupermarketDetails.set_supermarket_operates(new_hours)
                        print('Done')
                        print('')

                    case '5':
                        break



