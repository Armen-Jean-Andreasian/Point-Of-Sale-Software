class SupermarketDetails:
    supermarket_logo: str = 'files/7_eleven_logo.png'
    supermarket_name: str = '7 Eleven'
    supermarket_address: str = 'Shau Kei Wan, Hong Kong'
    supermarket_operates: str = 'Mon-Sat 6AM-12AM'
    destination_folder: str = 'reports'

    @classmethod
    def get_supermarket_details(cls) -> tuple:
        return (
            cls.supermarket_logo,
            cls.supermarket_name,
            cls.supermarket_address,
            cls.supermarket_operates,
            cls.destination_folder
        )
