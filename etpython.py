#Numpy
#import numpy as np
#Matplotlib
#pyplot
'''
import csv
product_names=[]
rating=[]
for d in csv.DictReader(open('C:\\Users\\navneeth\\Desktop\\DSCE\\New folder\\10-11-2019.csv'), delimiter='\t'):
    rating.append(int(d['Rating']))
    product_names.append(int(d['Product name']))
    #rating.append(int(d['Rating']))
print('Product Names =', product_names)
print('Rating =', rating)

import csv
filename="C:\\Users\\navneeth\\Desktop\\DSCE\\New folder\\10-11-2019.csv"
fields=[]
rows=[]

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for rows in csvreader:
        rows.append(row)
    print("Total number of rows: %d"%(csvreader.line_num))
    print("Field names are:" + ", ".join(field for field in fields))
    print('\nFirst Five Rows are:\n')
    for row in rows[:5]:
        for col in row:
            print("%10s"%col),
        print('\n')      
'''
import csv
import time
from collections import defaultdict
columns = defaultdict(list)

with open('C:\\Users\\navneeth\\Desktop\\DSCE\\New folder\\10-11-2019.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)
#print(columns['Product'])
#print(columns['Rating'])
product_names=[]
rating=[]
#product_names=columns['Product']
#rating=columns['Rating']
product_names=columns['Product'][:10]
rating=columns['Rating'][:10]
x=1
z=0
for i in product_names:
    h=product_names[z].split()
    product_names[z]=h[0]+" "+h[1]+" "+h[2]
    z=z+1
print(rating)
z=0
import matplotlib.pyplot as plt
for i, j in zip(product_names, rating):
    y=float(rating[z])
    plt.bar([product_names[z]], [y], label=product_names[z])
    x=x+1
    z=z+1
'''
plt.bar([1],[5], label = "Acer", color='black')
plt.bar([2],[7], label="Lenovo", color='green')
plt.bar([3],[9], label="HP", color='red')
plt.bar([4],[8], label="Apple", color='cyan')
plt.bar([5], [8], label="MSI", color='grey')
plt.bar([6], [3], label="ASUS", color='yellow')
plt.bar([7], [5], label="Dell", color='pink')
plt.bar([8], [7], label="Razer", color='orange')
plt.bar([9], [7], label="Alienware", color='brown')
plt.bar([10], [6], label="Gigabyte", color='purple')
'''

plt.legend()
plt.xlabel('Laptops Brands')
plt.ylabel('Laptops Rating')
plt.title('Laptops by rating on Flipkart')
plt.show()
