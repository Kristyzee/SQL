import requests
from bs4 import beautifulsoup as bs
git_user= input('Enetr the github username: ')
url='https://github.com/' + git_user
r=requests.get(url)
soup=bs(r.content, 'html.parser')
profile_image=soup.find('img',{'class': 'avatar'})['src']
print(profile_image)