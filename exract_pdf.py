import camelot

tables = camelot.read_pdf('CT Data Export Information.pdf', pages= '1')
print (tables)