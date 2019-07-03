import requests
import time
from bs4 import BeautifulSoup
import zipfile
import os
import argparse
from math import inf

def check_positive(value):
	value = int(value)
	if value < 0:
		raise argparse.ArgumentTypeError('Start number can\'t be negative.')
	return value


parser = argparse.ArgumentParser(description='Download russian ebooks in bulk.')
parser.add_argument('-g','--genre',default='detective',
					choices=['detective', 'det_action', 'thriller','dramaturgy','computers','love_history','sci_popular','network_literature'],
                    help='genres to download from')
parser.add_argument('-s', '--start_number', type=check_positive,default=0,
                    help='from which position to download')
parser.add_argument('-e', '--end_number', type=int,default=10,
                    help='to which position to download')
parser.add_argument('-dir',default='./ebooks',
                    help='which directory to download')
parser.add_argument('-file_type',default='fb2',choices=['fb2','epub', 'mobi','pdf'],
                    help='which file type to be downloaded')
args = parser.parse_args()



def main(args):
	download(args.genre,args.start_number,args.end_number,args.dir,args.file_type)
	
	
			
def download(genre, startNum, endNum, dir, fileType):
	url = "http://flibusta.is/g/" + genre;
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	soup = soup.select('a[href^="/b/"]')
	if(len(soup) < endNum):
		print('Ending number is higher than the current number of avaliable ebooks in this genre. Avaliable;',len(soup))
		return;
	for x in range(startNum,endNum):
		link = soup[x]['href']
		download_url = 'http://flibusta.is'+ link + "/" + fileType

		print(download_url)
		r = requests.get(download_url, allow_redirects=True)
		if(r.headers['Content-Disposition'].find(fileType)==-1):
			print("Skipped due to file not being",fileType )
			continue;
		open('temp.zip', 'wb').write(r.content)
		zip_ref = zipfile.ZipFile("temp.zip", 'r')
		zip_ref.extractall(dir)
		zip_ref.close()
		os.remove("temp.zip")


if __name__ == "__main__":
	main(args)
	