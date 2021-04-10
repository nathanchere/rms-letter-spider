import httpx
from bs4 import BeautifulSoup

github_usernames = []
response = httpx.get('https://rms-open-letter.github.io/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.select('ol li a'):
        url = link.get('href')

        if url.find("https://github.com") != -1:
            github_usernames.append(url.strip("/").split("/")[-1])
            
    for link in soup.select('code'):        
        username = link.text
        if username[0] == '@':
            username = username[1:]
        github_usernames.append(username)

print(github_usernames)
