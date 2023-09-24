import os
import time
from fpdf import FPDF


class Time:
    @staticmethod
    def current_time():
        # Convert the seconds to object
        ct_object = time.localtime(time.time())

        # Invoking values
        current_hour, current_minute, current_second = ct_object.tm_hour, ct_object.tm_min, ct_object.tm_sec

        formatted_time = f"{current_hour:02}:{current_minute:02}:{current_second:02}"

        return formatted_time


class PdfReport:
    supermarket_name: str = '7 Eleven'
    supermarket_logo: str = 'files/7_eleven_logo.png'
    destination_folder: str = 'reports'

    def __init__(self, receipt: dict, total: float):
        self.total = total
        self.receipt = receipt
        self.filename = f'{self.supermarket_name}_{Time.current_time().replace(":", "-")}'

    def generate_pdf(self):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name=self.supermarket_logo, x=10, y=10, w=50, h=50)

        # Insert supermarket name
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt=self.supermarket_name, border=0, align='C', ln=1)

        # Insert current time
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt=Time.current_time(), border=0, align='C', ln=1)

        # Insert Product label and Price
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Product', border=0)
        pdf.cell(w=150, h=40, txt='Price', border=0, ln=1)

        # Insert receipt items
        pdf.set_font(family='Times', size=12)
        for product, details in self.receipt.items():
            pdf.cell(w=100, h=30, txt=product, border=0)
            pdf.cell(w=150, h=30, txt=f"${details[1]:.2f}", border=0, ln=1)

        # Insert Total
        pdf.cell(w=100, h=30, txt='Total', border=0)
        pdf.cell(w=150, h=30, txt=f"${self.total:.2f}", border=0, ln=1)

        # Save the PDF to the reports folder
        pdf.output(os.path.join(self.destination_folder, f'{self.filename}.pdf'))


if __name__ == '__main__':
    report = PdfReport(receipt={'Milky Way': [1, 9.2], 'Backpack (Nike)': [2, 801.0]}, total=810.2)
    report.generate_pdf()
