from fpdf import FPDF
import os


class PdfGenerator:
    pdf = FPDF(orientation='P', unit='pt', format='A5')

    def __init__(self, receipt: dict, total: float, supermarket: tuple, current_day: str, current_time: str) -> object:

        self.receipt = receipt
        self.total = total
        self.supermarket_logo = supermarket[0]
        self.supermarket_name = supermarket[1]
        self.supermarket_address = supermarket[2]
        self.supermarket_operates = supermarket[3]
        self.destination_folder = supermarket[4]
        self.current_day = current_day
        self.current_time = current_time

        self.filename = f'{self.supermarket_name}_{current_time.replace(":", "-")}'

    def start(self):
        self.pdf.add_page()
        self.add_logo()
        self.add_name()
        self.add_address()
        self.add_time()
        self.pdf.ln(20)  # Add two breaklines
        self.add_products()
        self.pdf.ln(10)  # Add a breakline
        self.add_total()
        self.save_file()
        print('\nThe receipt was generated! \n'
              f'Check {self.destination_folder}/{self.current_day}-{self.filename}.pdf\n')

    def add_logo(self):
        """ Adds logo on the top left """
        self.pdf.image(name=self.supermarket_logo, x=10, y=10, w=50, h=50)

    def add_name(self):
        """ Set font for Supermarket name (in the middle) """
        self.pdf.set_font(family='Times', size=24, style='B')

        # Calculate the width of the supermarket name text
        name_width = self.pdf.get_string_width(self.supermarket_name)
        # Calculate the x-position for the name to be centered
        name_x = (self.pdf.w - name_width) / 2

        # Insert supermarket name in the middle
        self.pdf.text(x=name_x, y=35, txt=self.supermarket_name)

    def add_address(self):
        """ Supermarket address  and operating hours """
        # Set font for supermarket address and operates (below the name)
        self.pdf.set_font(family='Times', size=10)

        # Insert supermarket address and operates below the name
        self.pdf.ln(20)  # Move down to create space
        self.pdf.multi_cell(0, 10, self.supermarket_address + '\n' + self.supermarket_operates, align='C')

    def add_time(self):
        """ Current Time """
        # Set font for current TIME (on the right)
        self.pdf.set_font(family='Times', size=15, style='B')

        # Calculate the width of the current time text
        time_width = self.pdf.get_string_width(self.current_time)

        # Calculate the x-position for the time to be on the right
        time_x = self.pdf.w - 20 - time_width  # 60 is the space from the right edge

        # Insert current time on the right
        self.pdf.text(x=time_x, y=35, txt=self.current_time)

    def add_products(self):
        """ Products """
        # Set font for Product label, Amount, and Price (in the middle)
        self.pdf.set_font(family='Times', size=14, style='B')
        self.pdf.cell(w=100, h=40, txt='Product', border=0, align='C')
        self.pdf.cell(w=70, h=40, txt='Amount', border=0, align='C')
        self.pdf.cell(w=80, h=40, txt='Price', border=0, align='C', ln=1)

        # Insert receipt items
        self.pdf.set_font(family='Times', size=12)
        for product, details in self.receipt.items():
            self.pdf.cell(w=100, h=30, txt=product, border=0, align='C')
            self.pdf.cell(w=70, h=30, txt=str(details[0]), border=0, align='C')  # Display the item amount
            self.pdf.cell(w=80, h=30, txt=f"${details[1]:.2f}", border=0, align='C', ln=1)  # Display the item price

    def add_total(self):
        """ Total """
        # Set font for Total (in the middle)
        self.pdf.set_font(family='Times', size=14, style='B')

        # Calculate the width of the total text
        total_width = self.pdf.get_string_width(f"Total: ${self.total:.2f}")

        # Calculate the x-position for the total to be centered
        total_x = (self.pdf.w - total_width) / 2

        # Insert Total in the middle
        self.pdf.cell(w=total_x, h=30, txt='', border=0)  # Empty space before the total
        self.pdf.cell(w=total_width, h=30, txt=f"Total: ${self.total:.2f}", border=0, ln=1, align='C')  # Centered Total

    # def save_file(self):
    #     # Save the PDF to the reports folder
    #     self.pdf.output(os.path.join(self.destination_folder, f'{self.current_day}-{self.filename}.pdf'))

    def save_file(self) -> None:
        """
        Saves the PDF file within a folder named after the current day in the specified destination folder.

        This method creates a folder with the current day's name within the destination folder if it doesn't exist
        and saves the PDF file in that folder.

        """
        # Create the folder for the current day if it doesn't exist
        day_folder = os.path.join(self.destination_folder, self.current_day)
        if not os.path.exists(day_folder):
            os.makedirs(day_folder)

        # Save the PDF within the day's folder
        pdf_path = os.path.join(day_folder, f'{self.current_day}-{self.filename}.pdf')
        self.pdf.output(pdf_path)

