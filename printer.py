from fpdf import FPDF
import os
import time


class Time:
    @staticmethod
    def current_time():
        ct_object = time.localtime(time.time())
        current_hour, current_minute, current_second = ct_object.tm_hour, ct_object.tm_min, ct_object.tm_sec
        formatted_time = f"{current_hour:02}:{current_minute:02}:{current_second:02}"
        return formatted_time


class PdfReport:
    supermarket_logo: str = 'files/7_eleven_logo.png'

    supermarket_name: str = '7 Eleven'
    supermarket_address: str = 'Shau Kei Wan, Hong Kong'
    supermarket_operates: str = 'Mon-Sat 6AM-12AM'

    destination_folder: str = 'reports'

    def __init__(self, receipt: dict, total: float):
        self.total = total
        self.receipt = receipt
        self.filename = f'{self.supermarket_name}_{Time.current_time().replace(":", "-")}'

    def generate_pdf(self):
        PdfGenerator.generate_pdf(self)


class PdfGenerator(PdfReport):
    def generate_pdf(self):
        pdf = FPDF(orientation='P', unit='pt', format='A5')
        pdf.add_page()

        def add_logo():
            """ Logo """
            # Add logo on the left
            pdf.image(name=self.supermarket_logo, x=10, y=10, w=50, h=50)

        add_logo()

        def add_name():
            """ Supermarket name """
            # Set font for Supermarket name (in the middle)
            pdf.set_font(family='Times', size=24, style='B')

            # Calculate the width of the supermarket name text
            name_width = pdf.get_string_width(self.supermarket_name)
            # Calculate the x-position for the name to be centered
            name_x = (pdf.w - name_width) / 2

            # Insert supermarket name in the middle
            pdf.text(x=name_x, y=35, txt=self.supermarket_name)

        add_name()

        def add_address():
            """ Supermarket address  and operating hours """
            # Set font for supermarket address and operates (below the name)
            pdf.set_font(family='Times', size=10)

            # Insert supermarket address and operates below the name
            pdf.ln(20)  # Move down to create space
            pdf.multi_cell(0, 10, self.supermarket_address + '\n' + self.supermarket_operates, align='C')

        add_address()

        def add_time():
            """ Current Time """
            # Set font for current TIME (on the right)
            pdf.set_font(family='Times', size=15, style='B')

            # Calculate the width of the current time text
            time_width = pdf.get_string_width(Time.current_time())

            # Calculate the x-position for the time to be on the right
            time_x = pdf.w - 20 - time_width  # 60 is the space from the right edge

            # Insert current time on the right
            pdf.text(x=time_x, y=35, txt=Time.current_time())

        add_time()

        # Add two breaklines
        pdf.ln(20)

        def add_products():
            """ Products """
            # Set font for Product label, Amount, and Price (in the middle, centered)
            pdf.set_font(family='Times', size=14, style='B')
            pdf.cell(w=100, h=40, txt='Product', border=0, align='C')
            pdf.cell(w=70, h=40, txt='Amount', border=0, align='C')
            pdf.cell(w=80, h=40, txt='Price', border=0, align='C', ln=1)

            # Insert receipt items
            pdf.set_font(family='Times', size=12)
            for product, details in self.receipt.items():
                pdf.cell(w=100, h=30, txt=product, border=0, align='C')
                pdf.cell(w=70, h=30, txt=str(details[0]), border=0, align='C')  # Display the item amount
                pdf.cell(w=80, h=30, txt=f"${details[1]:.2f}", border=0, align='C', ln=1)  # Display the item price

        add_products()

        # Add a breakline
        pdf.ln(10)

        def add_total():
            """ Total """
            # Set font for Total (in the middle)
            pdf.set_font(family='Times', size=14, style='B')

            # Calculate the width of the total text
            total_width = pdf.get_string_width(f"Total: ${self.total:.2f}")

            # Calculate the x-position for the total to be centered
            total_x = (pdf.w - total_width) / 2

            # Insert Total in the middle
            pdf.cell(w=total_x, h=30, txt='', border=0)  # Empty space before the total
            pdf.cell(w=total_width, h=30, txt=f"Total: ${self.total:.2f}", border=0, ln=1, align='C')  # Centered Total

        add_total()

        def save_file():
            # Save the PDF to the reports folder
            pdf.output(os.path.join(self.destination_folder, f'{self.filename}.pdf'))

        save_file()


if __name__ == '__main__':
    report = PdfReport(receipt={'Milky Way': [1, 9.2], 'Backpack (Nike)': [2, 801.0]}, total=810.2)
    report.generate_pdf()
