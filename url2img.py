import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import cv2
import urllib.request

def url2img(url, use=False, save=False):
    """Función que recibe una url y retorna una imagen. Por defecto la imagen
    solo se muestra, pero adicionalmente se puede guardar para ser usada en el
    programa o para guardarla en carpeta.

    Args:
        url (str): Cadena de la url de la imagen.
        use (bool, optional): ¿Se usará posteriormente la imagen en el código?.
        Defaults to False.
        save (bool, optional): ¿Se desea guardar la imagen en el sistema?.
        Defaults to False.

    Returns:
        np.array: Arreglo que contiene a la imagen (BGR) en caso de que
        save=True. None en otro caso
    """

    url_response = urllib.request.urlopen(url)
    img = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), 
    cv2.IMREAD_COLOR)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if save:
        folder_name = 'Images_url'
        now = datetime.datetime.now()
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        full_path = os.path.join(folder_name, f'Imagen_{str(now)}.png')
        cv2.imwrite(full_path, img)
    
    if use:
        return img

    plt.imshow(rgb, cmap='gray')
    plt.axis('off')
    plt.show()
    
    return None

if __name__ == '__main__':
    url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Scarlet_darter_%28Crocothemis_erythraea%29_female_Bulgaria.jpg/1200px-Scarlet_darter_%28Crocothemis_erythraea%29_female_Bulgaria.jpg'
    url2img(url)