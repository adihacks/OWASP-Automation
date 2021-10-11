import requests
import re
from bs4 import BeautifulSoup
import sys
from pyfiglet import Figlet

f = Figlet(font='slant')
print (f.renderText('jQUery version'))

scripts = []



filename = sys.argv[1]
url = requests.get(filename)
soup = BeautifulSoup(url.text, 'html.parser')

for link in soup.find_all('script'):
 newline = link.get('src')
 scripts.append(newline)
 
# for script in scripts:
#  if "jquery" in str(script).lower():
#      ans = script
#      print(ans)

for script in scripts:
 if "1.9.1" in str(script).lower():
     
     print(" Jquery = 1.9.1	  \n Medium	2432 3rd party CORS request may execute CVE-2015-9251 \n Medium	CVE-2015-9251 11974 parseHTML() executes scripts in event handlers \n Medium	CVE-2019-11358 jQuery before 3.4.0, as used in Drupal, Backdrop CMS, and other products, mishandles jQuery.extend(true, {}, ...) because of Object.prototype pollution	\n Medium	CVE-2020-11022 Regex in its jQuery.htmlPrefilter sometimes may introduce XSS	 \n Medium	CVE-2020-11023 Regex in its jQuery.htmlPrefilter sometimes may introduce XSS")

 if "1.11.3" in str(script).lower():
    
     print("Jquery Version = 1.11.3 \n Medium CVE-2015-9251 3rd party CORS request may execute \n Medium CVE-2015-9251 11974 parseHTML() executes scripts in event handlers \n Medium CVE-2019-11358 jQuery before 3.4.0, as used in Drupal, Backdrop CMS, and other products, mishandles jQuery.extend(true, {}, ...) because of Object.prototype pollution   \n Medium CVE-2020-11022 Regex in its jQuery.htmlPrefilter sometimes may introduce XSS	\n Medium CVE-2020-11023 Regex in its jQuery.htmlPrefilter sometimes may introduce XSS")


 if "3.6.0" in str(script).lower():
     
     print("Updated no cves")

 if "3.5.0" in str(script).lower():
     
     print("Jquery Version = 3.5.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.5.1" in str(script).lower():
     
     print("Jquery Version = 3.5.1 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")



 if "3.0.0" in str(script).lower():
     
     print("Jquery Version = 3.0.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.1.1" in str(script).lower():
     
     print("Jquery Version = 3.1.1 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.1.0" in str(script).lower():
    
     print("Jquery Version = 3.1.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.2.0" in str(script).lower():
    
     print("Jquery Version = 3.2.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.2.1" in str(script).lower():
    
     print("Jquery Version = 3.2.1 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.3.0" in str(script).lower():
     
     print("Jquery Version = 3.3.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.3.1" in str(script).lower():
     
     print("Jquery Version = 3.3.1 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")


 if "3.4.1" in str(script).lower():
     
     print("Jquery Version = 3.4.1 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")

 if "3.4.0" in str(script).lower():
    
     print("Jquery Version = 3.4.0 \n Medium CVE-2019-11358 https://nvd.nist.gov/vuln/detail/CVE-2019-11358")
