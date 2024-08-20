import sys
from pypdf import PdfMerger

inputs = sys.argv[1:]


def pdf_combiner(pdf_list: list[str]):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(f'{sys.path[0]}/{pdf}')

    merger.write(f'{sys.path[0]}/merged.pdf')

pdf_combiner(inputs)
