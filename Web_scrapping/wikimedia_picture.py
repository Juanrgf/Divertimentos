import requests
from bs4 import BeautifulSoup
import shutil

import re
import datetime
import os

import cv2
import matplotlib.pyplot as plt

def pictureofday_wikimedia():
    regex = r'\..{3,4}$'
    human_date = datetime.date.today().strftime('%d/%m/%Y')
    
    url = 'https://commons.m.wikimedia.org/wiki/Main_Page'
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        url_img = soup.find('a', class_='image').find('img')['src']
        response_img = requests.get(url_img, stream=True)
        
        if response_img.ok:
            extension = re.search(regex, url_img).group()
            title = soup.find('div', class_='description').text.strip().strip('.')
            name = f'{title}{extension}'
            
            if not os.path.exists(name):
                with open(name, 'wb') as f_img:
                    response_img.raw.decode_content = True
                    shutil.copyfileobj(response_img.raw, f_img)
            else:
                print(f'Ya existe {name}')
                
            img = img = cv2.imread(name)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            plt.imshow(rgb, cmap='gray')
            plt.title(f'{title}\n{human_date}')
            plt.axis('off')
            plt.show()
        
if __name__ == '__main__':
    pictureofday_wikimedia()
            