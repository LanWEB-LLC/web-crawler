from bs4 import BeautifulSoup, NavigableString
import requests

count=0

def save_to_file(file_name, contents):
    fh = open(file_name, 'w', encoding = 'utf-8')
    fh.write(contents)
    fh.close()

def getdetail(href):
    url_detail = 'https://www.indeed.com' + href

    print('url_detail')
    print(url_detail)

    r1 = requests.get(url_detail)

    soup1 = BeautifulSoup(r1.text, 'lxml')

    description=''

    for divroot in soup1.find_all(attrs={'id':'jobDescriptionText'}):
        for tag in divroot.descendants:
            if isinstance(tag, NavigableString):
                continue
            else:
                if len(tag.contents)==1 and isinstance(tag.contents[0], str):
                    if len(tag.text)==0:
                        continue
                    description+=(tag.text+'\n')

    #print(description)

    description = url_detail+'\n'+description
    save_to_file('E://log'+str(count)+'.txt', description)

url = 'https://www.indeed.com/q-software-engineer-l-USA-jobs.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

titles = soup.find_all('h2', attrs={'class':'title'})

for link in titles:
    if 'href' in link.a.attrs:
        getdetail(link.a['href'])
        count+=1



