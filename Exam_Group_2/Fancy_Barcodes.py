import re

count_of_barcodes = int(input())
barcode_pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(count_of_barcodes):
    new_barcode = input()
    match = re.match(barcode_pattern, new_barcode)

    if match:
        core = match.group(1)
        product_group = ''.join(filter(str.isdigit, core)) or '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
