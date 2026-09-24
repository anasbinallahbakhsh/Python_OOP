import re

with open('index.html', 'r') as f:
    content = f.read()

links = re.findall(r'href="(.*?)"', content)

with open('links.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')

print ( links)