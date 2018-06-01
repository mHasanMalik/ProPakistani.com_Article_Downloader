import requests
from bs4 import BeautifulSoup


def find_words(word_list, all_links):
	a = set()
	for url in all_links:
		
		req = requests.get(url)
		
		if req.status_code == 200:
			#print "Link is working fine" 
			parser_obj = BeautifulSoup(req.content, "html.parser")
			a_tag_list = parser_obj.find_all("a")
			
			div_tag_list=parser_obj.find_all('div', {'class': 'single-story'})
			
			for div_tag in div_tag_list:
				div_child = div_tag.findChildren()
				for child in div_child:
					a_tag_list = child.find_all("a")
					for a_tag in a_tag_list:
						for word in word_list:
							if word in a_tag.get_text():
								a.add(a_tag["href"])	


		else:
			print "Bad Network error, Check Internet Connections"	

	for n in list(a):
			print n


def read_from_file():
	mylist= []
	filename="input"
	file=open(filename,"r")
	mystr=file.read()

	for word in mystr.split(','):
		mylist.append(word)
		
	mylist.append("abc")
	return mylist


def make_links(URL):
	mylinks= []
	
	counter = 2
	
	while(counter !=6):
		newlink = "%spage/%d" % (URL,counter)
		mylinks.append(newlink)
		counter = counter + 1
	
	return mylinks

def main():

	word_list = read_from_file()
	URL ="https://propakistani.pk/"
	all_links= make_links(URL)
	find_words(word_list,all_links)


if __name__ == "__main__":
	main()
