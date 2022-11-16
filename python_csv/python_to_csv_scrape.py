from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# Make HTTP get request
url = "https://en.wikipedia.org/wiki/Comma-separated_values"
page = requests.get(url)
page.status_code

# Parse content
content = BeautifulSoup(page.text, "html.parser")

# Save content in Dataframe
cars = content.find_all("pre")
df = pd.DataFrame(cars[10])

print(type(df))
df.to_csv(r'~/Desktop/Programming/ST2195/Assignment 2/python_csv/cars_python.csv', index = False, header=True)



#with open('cars_python.csv', 'wb') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerows(cars[10])
#read_file = pd.read_csv(cars[10])
#read_file
