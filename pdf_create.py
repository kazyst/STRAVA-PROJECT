from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# Create a PDF file
pdf_file = "example_with_image.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)

# Set the title
c.setFont("Helvetica-Bold", 24)
c.drawString(100, 750, "ReportLab Example with Image")

# Add an image
image_path = r'C:\Users\kazys\OneDrive\Dokumenty\STRAVA PROJECT\testas.png'

#image_path = os.path.abspath("icon128.png")
c.drawImage(image_path, 100, 500, width=200, height=150)  # x, y, width, height

# Save the PDF
c.save()

# C:\Users\kazys\OneDrive\Dokumenty\STRAVA PROJECT\testas.png