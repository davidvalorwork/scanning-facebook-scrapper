import csv

def write_csv(dicts, name):
  with open('responses/'+name + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dicts[0].keys())
    writer.writeheader()  # Writes the header row
    writer.writerows(dicts)  # Writes all the rows