from bs4 import BeautifulSoup
import requests


url = 'https://www.indeed.com/q-software-engineer-l-USA-jobs.html'

#r = requests.get(url)

#soup = BeautifulSoup(r.text, 'lxml')

#print(soup.find_all(attrs={'id':'sja0'}))

#a = soup.find_all(attrs={'id':'sja0'})

#print(a[0]['href'])

r1 = requests.get('https://www.indeed.com'+'/pagead/clk?mo=r&ad=-6NYlbfkN0ABpo_ZgZOIhs9tMr8Gpr-iBBVTsm4adlixB0fYJReMSldynnTLIcW4QRCDvf4TVHhpMVMAM8TIK3eMyINnd7eMKoEbrt3sO3-wiw01JaiWpQ_pkz2stSdMK_T4A58AudOtaqNAjDqJ2gl5oi8SP7Uc6WTJCCGtcVCxMMytKvTWopUdRJ_UyTa7JmrVVkeFGBwZj1d7q2JExRUWRuacRYmYD8b7mGMgfo9eB36uOL2bRurh88zOGOzMJJrqtYX0OAQYR-wy4VQ5M3oDgemrs56oTxYL6Y1d3JC6o--m2zzBeMTVv1Y12fiIZ3Wx5MwsVnhxfEBW7_2wuI12Xn6tMzD0k3z1EcdofjINtWHaAFD8ONXoTuQt7EE-wmT-PRICFz2cEtJ9C2JbgDsVDtKcs6-5dLE6aYc_NfRBJbB2zXH622oewr5LxEhcu4cerohqK5jTpZTfNuso_w==&p=0&fvj=1&vjs=3')

soup1 = BeautifulSoup(r1.text, 'lxml')

description=''

for c in soup1.find_all(attrs={'id':'jobDescriptionText'})[0].contents:
    if c.name=='p':
        description+=(c.text+'\n')
    if c.name=='ul':
        for li in c.contents:
            description+=('   '+li.text+'\n')

print(description)


