import sys
import urllib3
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("""\u001b[32m
 /$$$$$$$  /$$      /$$  /$$$$$$ 
| $$__  $$| $$$    /$$$ /$$__  $$
| $$  \ $$| $$$$  /$$$$| $$  \__/
| $$  | $$| $$ $$/$$ $$| $$      
| $$  | $$| $$  $$$| $$| $$      
| $$  | $$| $$\  $ | $$| $$    $$
| $$$$$$$/| $$ \/  | $$|  $$$$$$/
|_______/ |__/     |__/ \______/\u001b[0m
	
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

def getDMARC(site):
	r = requests.get(f'https://dmarcly.com/server/dmarc_check.php?domain={site}')
	rjson = r.json()
	if rjson["code"] == 'success':
		print(f"\u001b[34mThe domain :\'{site}\' contains a valid DMARC record\u001b[0m")
		print(f'Host: \'{rjson["dmarcRecords"][0]["host"]}\'')
		print(f'Record: {rjson["dmarcRecords"][0]["txt"]}')
		print("\u001b[33m="*50+"\u001b[0m")
	else:
		print(f"\u001b[31mDMARC record not found for \u001b[0m\'{site}\'")
		print("\u001b[33m="*50+"\u001b[0m")

if __name__ == '__main__':
	if args.wordlist:
		f = open(WORDLIST, "r").read()
		l = f.splitlines()
		with ThreadPoolExecutor() as executor:
			executor.map(getDMARC, l, timeout=3)
	else:
		getDMARC(URL)
