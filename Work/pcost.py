# pcost.py
#
# Exercise 1.27


f = open('Data/portfolio.csv', 'rt')

headers = next(f);

sum = 0;

for line in f:
    row = line.split(',')
    print(row)
    sum += float(row[2].strip())

print(f'Total cost is {sum:0.2f}')

f.close()