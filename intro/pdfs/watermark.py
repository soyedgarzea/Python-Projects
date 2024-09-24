from sys import path
from pypdf import PdfReader, PdfWriter

root = path[0]
stamp = PdfReader(f'{root}/stamp.pdf').pages[0]
writer = PdfWriter(f'{root}/merged.pdf')

for page in writer.pages:
    page.merge_page(stamp, over=False)

writer.write(f'{root}/merged.pdf')
