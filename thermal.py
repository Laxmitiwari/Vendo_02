import cups
conn = cups.Connection()
printers = conn.getPrinters ()
for printer in printers:
	print printer, printers[printer]["device-uri"]

file="print.txt"
printer_name=printers.keys()[0]
print(printer_name)
conn.printFile (printer_name, file, "Text Print", {})