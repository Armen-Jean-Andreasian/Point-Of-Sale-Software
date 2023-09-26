import os


class SupermarketDetails:
    supermarket_logo: str = 'files/logo.png'
    supermarket_name: str = '7 Eleven'
    supermarket_address: str = 'Shau Kei Wan, Hong Kong'
    supermarket_operates: str = 'Mon-Sat 6AM-12AM'
    destination_folder: str = 'reports/receipts'

    @classmethod
    def get_supermarket_details(cls) -> tuple:
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

        Hint: logo is being kept at 'files/logo.png'.

        :param logo_path: path to the new logo file
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
        Example usage:

        SupermarketDetails.set_supermarket_name('New Name')
        """
        cls.supermarket_name = name

    @classmethod
    def set_supermarket_address(cls, address: str):
        """
        Example usage:

        SupermarketDetails.set_supermarket_address('New Address')
        """
        cls.supermarket_address = address

    @classmethod
    def set_supermarket_operates(cls, operates: str):
        """
        Example usage:

        SupermarketDetails.set_supermarket_operates('Mon-Fri 1AM-8AM')
        """
        cls.supermarket_operates = operates


if __name__ == '__main__':
    print(SupermarketDetails.get_supermarket_details())
