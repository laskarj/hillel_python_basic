import csv
#'cash_file.csv'

data = {'UA': 27.3, 'AVAILABLE_UA': 30000.0, 'USD': 27.5, 'AVAILABLE_USD': 10000.0}

x = data.keys()
print(x)
"""
data = {'UA': 27.3, 'AVAILABLE_UA': 30000.0, 'USD': 27.5, 'AVAILABLE_USD': 10000.0}

def unpacking_data(namefile: str):
    with open(namefile) as f:
        read = DictReader(f)
        for items in read:
            data_money: dict = items
            for k, v in data_money.items():
                if v != float:
                    data_money[k] = float(v)
            return data_money


x = unpacking_data('cash_file.csv')

print(x)

with open('cash_file.csv', 'w') as csvfile:
    fieldnames = ['UA', 'AVAILABLE_UA', 'USD', 'AVAILABLE_USD']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)
"""