import csv
your_list = []
string = ""

with open('sample_data.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

#print your_list

for l in your_list:
    if l[1] != 'created_at':
        if 1403395200 < int(l[1]) < 1405987200:
            string += l[8] + " "
print string