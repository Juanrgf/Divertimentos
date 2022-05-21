import requests
from bs4 import BeautifulSoup
import cv2
import matplotlib.pyplot as plt

import os, re, shutil, datetime

def pictureofday_wikimedia(view=True):
    """ Descarga la imagen del día del sitio de wikimedia

    Args:
        view (bool, optional): ¿Quieres visualizar la imagen? Por defecto se
        muestra la imagen 
    """

    # Creamos una regex para atrapar el formato de la imagen
    regex = r'\..{3,4}$'
    # Fecha de hoy
    human_date = datetime.date.today().strftime('%d/%m/%Y')
    
    # Página de wikimedia
    url = 'https://commons.m.wikimedia.org/wiki/Main_Page'
    # Configuramos el user-agent
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    # Hacemos la petición
    response = requests.get(url, headers=headers)

    # Si la petición tuvo exito
    if response.ok:
        # Creamos el obejto soup con la página
        soup = BeautifulSoup(response.text, 'html.parser')
        # Capturamos el url de la imagen del día
        url_img = soup.find('a', class_='image').find('img')['src']
        # Hacemos otra petición para obtener la imagen
        response_img = requests.get(url_img, stream=True)
        
        # Si la petición tuvo exito
        if response_img.ok:
            # Buscamos la extensión del archivo
            extension = re.search(regex, url_img).group()
            # Nombramos a la imagen
            title = soup.find('div', class_='description').text.strip().strip('.')
            name = f'{title}{extension}'
            
            # Si la imagen aún no ha sido guardada
            if not os.path.exists(f'Images/{name}'):
                # Creamos el archivo
                with open(f'Images/{name}', 'wb') as f_img:
                    # Deodificamos los datos de la petición
                    response_img.raw.decode_content = True
                    # Guardamos en la ruta 
                    shutil.copyfileobj(response_img.raw, f_img)
                    f_img.close()
                print('La imagen ha sido descargada')

            # En caso de que la imagen ya haya sido guardada
            else:
                print(f'Ya existe\t{name}\nen el directorio Images')
        
        # Para visualizar la imagen
        if view:
            img = img = cv2.imread(f'Images/{name}')
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            plt.imshow(rgb, cmap='gray')
            plt.title(f'{title}\n{human_date}')
            plt.axis('off')
            plt.show()
        
if __name__ == '__main__':
    pictureofday_wikimedia()
            