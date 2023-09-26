"""
SupermarketDetails: Utility class for managing supermarket details.

This module defines the SupermarketDetails class, which provides methods for managing details of a supermarket,
including its logo, name, address, and operating hours.

Classes:
    SupermarketDetails: Utility class for managing supermarket details.

Methods:
    get_supermarket_details: Get the current supermarket details.
    set_supermarket_logo: Replace the supermarket logo with a new image.
    set_supermarket_name: Set the name of the supermarket.
    set_supermarket_address: Set the address of the supermarket.
    set_supermarket_operates: Set the operating hours of the supermarket.

Usage:
    The SupermarketDetails class allows you to manage details of a supermarket.

Examples:
    To get the current supermarket details:
    details = SupermarketDetails.get_supermarket_details()
    print("Supermarket Details:", details)

    To set a new logo for the supermarket:
    SupermarketDetails.set_supermarket_logo('new_logo.png')

    To set the name of the supermarket:
    SupermarketDetails.set_supermarket_name('New Name')

    To set the address of the supermarket:
    SupermarketDetails.set_supermarket_address('New Address')

    To set the operating hours of the supermarket:
    SupermarketDetails.set_supermarket_operates('Mon-Fri 1AM-8AM')

"""


import os


class SupermarketDetails:
    supermarket_logo: str = 'files/logo.png'
    supermarket_name: str = '7 Eleven'
    supermarket_address: str = 'Shau Kei Wan, Hong Kong'
    supermarket_operates: str = 'Mon-Sat 6AM-12AM'
    destination_folder: str = 'reports/receipts'

    @classmethod
    def get_supermarket_details(cls) -> tuple:
        """
        Get the current supermarket details.

        Returns:
            tuple: A tuple containing supermarket logo path, name, address, operating hours, and destination folder.
        """
        return (
            cls.supermarket_logo,
            cls.supermarket_name,
            cls.supermarket_address,
            cls.supermarket_operates,
            cls.destination_folder
        )

    @classmethod
    def set_supermarket_logo(cls, logo_path: str):
        """
        Replaces the logo file.

        Args:
            logo_path (str): Path to the new logo file.

        Hint: The logo will be saved at 'files/logo.png'.
        """
        #
        current_directory = os.getcwd()
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

        project_logo_path = parent_directory + '/files/logo.png'

        with open(logo_path, 'rb') as new_logo_file:
            with open(project_logo_path, 'wb') as existing_logo_file:
                existing_logo_file.write(new_logo_file.read())
            print('Done')

    @classmethod
    def set_supermarket_name(cls, name: str):
        """
        Set the name of the supermarket.

        Usage example:
                SupermarketDetails.set_supermarket_name('New Name')
        """
        cls.supermarket_name = name

    @classmethod
    def set_supermarket_address(cls, address: str):
        """
        Set the address of the supermarket.

        Usage example:
                SupermarketDetails.set_supermarket_address('New Address')
        """
        cls.supermarket_address = address

    @classmethod
    def set_supermarket_operates(cls, operates: str):
        """
        Set the operating hours of the supermarket.

        Usage example:
                SupermarketDetails.set_supermarket_operates('Mon-Fri 1AM-8AM')
        """
        cls.supermarket_operates = operates


if __name__ == '__main__':
    print(SupermarketDetails.get_supermarket_details())
