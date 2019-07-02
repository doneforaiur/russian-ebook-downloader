import requests
import time
from bs4 import BeautifulSoup
import zipfile
import os
import argparse

parser = argparse.ArgumentParser(description='Download russian ebooks in bulk.')
parser.add_argument('-g','--genre',default='detective',choices=['detective', 'det_action', 'thriller'],
                    help='avaliable genres; "detective", "det_action","thriller"')
parser.add_argument('-s', '--start_number', type=int,default=0,
                    help='from which position to download')
parser.add_argument('-e', '--end_number', type=int,default=10,
                    help='to which position to download')
args = parser.parse_args()
print(args)

def main(args):
	download(args.genre,args.start_number,args.end_number)
			
def download(genre, startNum, endNum):
	url = "http://flibusta.is/g/" + genre;
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	soup = soup.select('a[href^="/b/"]')
	if(len(soup) < endNum):
		print('Ending number is higher than the current number of avaliable ebooks in this genre. Avaliable;',len(soup))
		return;
	for x in range(startNum,endNum):
		link = soup[x]['href']
		download_url = 'http://flibusta.is'+ link + "/fb2"

		print(download_url)
		r = requests.get(download_url, allow_redirects=True)
		if(r.headers['Content-Disposition'].find('fb2')==-1):
			print("Skipped due to file not being .FB2")
			continue;
		open('temp.zip', 'wb').write(r.content)
		zip_ref = zipfile.ZipFile("temp.zip", 'r')
		zip_ref.extractall("./dl")
		zip_ref.close()
		os.remove("temp.zip")


if __name__ == "__main__":
	print(args)
	main(args)