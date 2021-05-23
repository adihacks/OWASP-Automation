import requests
import re
from bs4 import BeautifulSoup
import sys
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('jQUery version'))

scripts = []
#val = input("Enter your value: ")

filename = sys.argv[1]
url = requests.get(filename)
soup = BeautifulSoup(url.text, 'html.parser')

for link in soup.find_all('script'):
 newline = link.get('src')
 scripts.append(newline)
 
for script in scripts:
 if "jquery" in str(script).lower():
     #hel = re.findall(r'\d+', str(script))
     print(script)



