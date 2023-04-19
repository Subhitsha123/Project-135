import matplotlib.pyplot as plt
import csv

df = []
with open('output_stars.csv','r') as f:
  csvreader = csv.reader(f)
  for row in csvreader:
    if row != []:
      df.append(row)

headers = df[0] 
data = df[1:]
star_name = []
star_mass = []
star_radius = []
star_distance = []
star_gravity = []

for i in data:
  star_name.append(i[1])
  star_distance.append(float(i[2]))
  star_mass.append(float(i[3]))
  star_radius.append(float(i[4]))
  star_gravity.append(float(i[5].split(' ')[0]))

plt.bar(star_name,star_mass)
plt.title('Name VS Mass')
plt.xlabel('Name')
plt.ylabel('Mass')
plt.show()

plt.bar(star_name,star_radius)
plt.title('Name VS Radius')
plt.xlabel('Name of Stars')
plt.ylabel('Radius')
plt.show()

plt.bar(star_name,star_distance)
plt.title('Name VS Distance')
plt.xlabel('Name')
plt.ylabel('Distance')
plt.show()

plt.bar(star_name,star_gravity)
plt.title('Name VS Gravity')
plt.xlabel("Name")
plt.ylabel('Gravity')
plt.show()