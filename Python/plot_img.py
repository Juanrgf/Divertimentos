import matplotlib.pyplot as plt

def plot_img(img, title=None):
    """Graficador de imágenes

    Args:
        img (np.array): Imagen a graficar
        title (str, optional): Titulo de la imagen

    Returns:
        None
    """

    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title(title)
    plt.show()

    return None

if __name__ == '__main__':
    from url2img import url2img
    import cv2
    
    url = 'https://upload.wikimedia.org/wikipedia/commons/2/24/Northeastward_view_from_Train_leaving_Brighton_Station_%28Platform_8%29_%28March_2011%29.JPG'
    img = url2img(url, use=True)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plot_img(rgb, 'Imagen')
