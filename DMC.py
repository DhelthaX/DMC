import sys
import urllib3
import requests
import argparse
#from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("""
 /$$$$$$$  /$$      /$$  /$$$$$$ 
| $$__  $$| $$$    /$$$ /$$__  $$
| $$  \ $$| $$$$  /$$$$| $$  \__/
| $$  | $$| $$ $$/$$ $$| $$      
| $$  | $$| $$  $$$| $$| $$      
| $$  | $$| $$\  $ | $$| $$    $$
| $$$$$$$/| $$ \/  | $$|  $$$$$$/
|_______/ |__/     |__/ \______/
	
		     by: dhelthaX
	""")


parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-d", "--domain", help="For a Single Domain")
parser.add_argument("-w", "--wordlist", help="For a List of Domains")
args = parser.parse_args()

if args.domain == None and args.wordlist == None:
    print("Usage: python3 DMC.py -h")
    sys.exit()

WORDLIST = args.wordlist
URL = args.domain
HEADERS = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0", "Referer": "https://dmarcian.com/", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}

def getDMARC(site, dom):
	r = requests.post('https://dmarcian.com/wp-admin/admin-ajax.php', data=site, headers=HEADERS)
	rjson = r.json()
	if rjson["payload"]["valid"] == False:
		print(f'{rjson["payload"]["messages"][1]["text"]} for {dom}')
		print("="*40)
	else:
		print(f"Valid DMARC found for {dom}")
		print(str(rjson["payload"]["records"][0]["txt"]))
		print("="*40)

if __name__ == '__main__':
	if args.wordlist:
		f = open(WORDLIST, "r")
		for x in f:
			DATA = f'action=dm_integration_inspect_dmarc&domain={x}&security=69879e3ab6'
			getDMARC(str(DATA), str(x))
	else:
		DATA = f'action=dm_integration_inspect_dmarc&domain={URL}&security=69879e3ab6'
		getDMARC(DATA, URL)
