import csv
import json
import os
import sys
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib import styles
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from PIL import Image
from sys import exit
import subprocess
import platform


from tkinter import Tk
from tkinter.filedialog import askopenfilename

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

base_dir = os.path.abspath(os.path.dirname(__file__))

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux and macOS

def preprocess_image(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
    except FileNotFoundError:
        exit("\nXXX Immagine logo.png non presente nella cartella Resources XXX\n")

    print("Immagine logo caricata correttamente")

    new_img = Image.new("RGBA", img.size, (255, 255, 255, 255)) 

    new_img.paste(img, (0, 0), img)

    new_img.save(output_path, "PNG")
    print("Immagine logo.png con sfondo trasparente correttamente creata nella cartella results")


def read_columns_from_txt(txt_file_path):
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            columns = [line.strip() for line in txt_file.readlines() if line.strip()]
        print("File columns.txt letto correttamente")
    except FileNotFoundError:
        exit("\nXXX File columns.txt non trovato XXX\n")
    return columns


def read_collapse_column(txt_file_path):
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            collapse_column = txt_file.readline().strip()  # Prende solo la prima riga
        print("File collapse.txt letto correttamente")
    except FileNotFoundError:
        exit("\nXXX File collapse.txt non trovato XXX\n")
    return collapse_column


def json_to_pdf(json_file_path, pdf_file_path, logo_path):
    base_dir = os.path.dirname(__file__)
    
    poppins_regular_path = os.path.join(base_dir, 'utilities','Poppins', 'Poppins-Regular.ttf')
    poppins_bold_path = os.path.join(base_dir, 'utilities','Poppins', 'Poppins-Bold.ttf')

    pdfmetrics.registerFont(TTFont('Poppins', poppins_regular_path))
    pdfmetrics.registerFont(TTFont('Poppins-Bold', poppins_bold_path))

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    c = canvas.Canvas(pdf_file_path, pagesize=A4)
    width, height = A4
    pageNumber = 1
    rowSpace = 20

    primary_color = HexColor("#fdbf00")
    secondary_color = HexColor("#F5F5F5")
    header_text_color = HexColor("#7800a0")
    content_text_color = HexColor("#333333")
    column_text_color = HexColor("#7800a0")

    c.setFont("Poppins-Bold", 16)

    # --- Header Logo ---
    logo_image = ImageReader(logo_path)
    original_width, original_height = logo_image.getSize()
    logo_max_width = 100
    logo_max_height = 50
    logo_scale = min(logo_max_width / original_width, logo_max_height / original_height)
    scaled_logo_width = original_width * logo_scale
    scaled_logo_height = original_height * logo_scale

    logo_x = 50 
    logo_y = height - scaled_logo_height - 40

    c.drawImage(logo_path, logo_x, logo_y, width=scaled_logo_width, height=scaled_logo_height)

    # --- Header ---
    c.setFillColor(primary_color)
    c.roundRect(50, logo_y - 100, width - 100, 50, 10, stroke=0, fill=1)

    c.setFillColor(header_text_color)
    c.drawString(60, logo_y - 80, "Documento Ufficiale")
    c.setFont("Poppins", 12)

    # --- Visual separators ---
    c.setLineWidth(1)
    c.line(70, logo_y - 120, width - 70, logo_y - 120)
    c.setStrokeColor(primary_color)

    # --- Document body ---
    y_position = logo_y - 120

    for key, items in data.items():
        max_columns = len(items[0].keys())
        column_width = (width - 150) / max_columns 

        bubble_height = 50 + (len(items) * rowSpace)

        if y_position - bubble_height < 150:
            c.showPage()
            y_position = height - 40 

            # --- Piedipagina ---
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(colors.grey)
            c.drawString(50, 30, "Documento generato automaticamente. Pettez © 2024")
            c.setFillColor(header_text_color)
            c.drawRightString(width - 50, 30, f"Pagina {pageNumber}")
            pageNumber += 1

        y_position -= bubble_height + rowSpace
        
        c.setStrokeColor(primary_color)

        # Informations Section
        c.setFillColor(secondary_color)
        c.roundRect(50, y_position, width - 100, bubble_height, 10, stroke=1, fill=1)

        # key for the collapsed column
        c.setFillColor(primary_color)
        c.setFont("Poppins-Bold", 10)
        c.drawString(60, y_position + bubble_height - 20, f"{key}:")

        # Write data inside the Informations Section
        c.setFont("Poppins", 8)
        c.setFillColor(content_text_color)
        y_text_position = y_position + bubble_height - 40 

        header_keys = list(items[0].keys())
        x_base_position = 60

        c.setFillColor(column_text_color)
        c.setFont("Poppins-Bold", 8)
        for idx, header in enumerate(header_keys):
            x_position = x_base_position + idx * column_width
            c.drawString(x_position, y_text_position, header)
        y_text_position -= 20

        c.setFillColor(content_text_color)

        c.setFont("Poppins", 8)
        for idx, item in enumerate(items):
            x_position = x_base_position
            for key in header_keys:
                c.drawString(x_position, y_text_position, str(item[key]))
                x_position += column_width 
            y_text_position -= rowSpace
    print("File pdf correttamente creato nella cartella results")
    c.save()


def csv_to_json(csv_file_path, json_file_path, columns_to_keep, collapse_column, delimiter=','):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
            
            collapsed_data = {}
            single_data = {}
            collapse_counts = {}

            for row in csv_reader:
                try:
                    collapse_key = row[collapse_column]
                except KeyError:
                    exit("\nXXX Formato del file collapse.txt non consono XXX\n")

                if collapse_key not in collapse_counts:
                    collapse_counts[collapse_key] = 0
                collapse_counts[collapse_key] += 1

            csv_file.seek(0)
            next(csv_reader) 

            for row in csv_reader:
                collapse_key = row[collapse_column]

                filtered_row = {key: row[key] for key in columns_to_keep if key in row and key != collapse_column}

                if collapse_counts[collapse_key] > 1:
                    if collapse_key not in collapsed_data:
                        collapsed_data[collapse_key] = []
                    collapsed_data[collapse_key].append(filtered_row)
                else:
                    single_data[collapse_key] = [filtered_row]
    except FileNotFoundError:
        exit("\nXXX File document.csv non trovato XXX\n")
    
    print("File document.csv letto correttamente")

    collapsed_data.update(single_data)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(collapsed_data, json_file, indent=4)

    print("File json correttamente creato nella cartella results")


def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    import pyfiglet
except ImportError:
    print("pyfiglet non è installato. Installazione in corso...")
    install('pyfiglet')
    import pyfiglet 
try:
    import reportlab
except ImportError:
    print("reportlab non è installato. Installazione in corso...")
    install("reportlab")
    import reportlab
try:
    from PIL import Image
except ImportError:
    print("Pillow non è installato. Installazione in corso...")
    install("Pillow")
    from PIL import Image


clear_console()

text = "---CsvToPdf---"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)

csv_file = os.path.join(base_dir, 'resources', 'document.csv')
input_logo_path = os.path.join(base_dir, 'resources', 'logo.png')
columns_file = os.path.join(base_dir, 'resources', 'columns.txt')
collapse_file = os.path.join(base_dir, 'resources', 'collapse.txt')

output_logo_path = os.path.join(base_dir,'results', 'processed_logo.png')
json_file = os.path.join(base_dir, 'results','output.json')
pdf_file = os.path.join(base_dir,'results', 'document.pdf')
delimiter = ';'

# Preprocess the image
preprocess_image(input_logo_path, output_logo_path)

# Read the columns to keep from the .txt file
columns_to_keep = read_columns_from_txt(columns_file)

# Read the column to collapse from the .txt file
collapse_column = read_collapse_column(collapse_file)

# Perform the conversion
csv_to_json(csv_file, json_file, columns_to_keep, collapse_column, delimiter)
json_to_pdf(json_file, pdf_file, output_logo_path)


text = "-------------"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
