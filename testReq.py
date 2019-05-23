import requests
import random as R

#page = requests.get('https://google.com')
#print(page)
base_url = 'https://google.com'
links = ['About','Contact','Home','Map','Samples','Testimonials']
print(links)
links_length = len(links)
for l in range(0, links_length):
    randomNum = R.randint(0,len(links) - 1)
    print('link working with: ' + links[randomNum])
    if links[randomNum] == 'Home':
        requests.get(base_url)
    else:
        requests.get(base_url + '/' + links[randomNum])
    print(links)
    del links[randomNum]
    print(links)
    print(randomNum)