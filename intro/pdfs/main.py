from pypdf import PdfReader, PdfWriter

with open('./pdfs/dummy-1.pdf', 'rb') as file:
    reader = PdfReader(file)
    page = reader.pages[0]
    page.rotate(90)
    writer = PdfWriter()
    writer.insert_page(page)

    with open('./pdfs/dummy-1.1.pdf', mode='wb') as new_file:
        writer.write(new_file)
