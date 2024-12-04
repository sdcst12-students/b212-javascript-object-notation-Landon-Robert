#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
data = req.text
importedData = json.loads(data)
print(type(importedData))
print("Menu:")
for i in importedData['menu']:
    for j in importedData['menu'][importedData['menu'].index(i)]:
        print(importedData['menu'][importedData['menu'].index(i)][j])
    print('='*20)
# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains
