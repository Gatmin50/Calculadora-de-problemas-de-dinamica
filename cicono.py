from PIL import Image
import os

def png_to_ico(png_path, ico_path, ico_folder):
    # Crea la carpeta si no existe
    if not os.path.exists(ico_folder):
        os.makedirs(ico_folder)

    # Abre la imagen PNG
    img = Image.open(png_path)

    # Convierte la imagen PNG en ICO
    img = img.resize((32, 32), Image.ANTIALIAS)
    img.save(os.path.join(ico_folder, ico_path), format='ICO', sizes=[(32,32)])

# Ruta de la imagen PNG
png_path = 'ruta/a/tu/imagen.png'

# Nombre del archivo ICO
ico_path = 'nombre_del_archivo.ico'

# Carpeta donde se guardará el archivo ICO
ico_folder = 'ruta/a/la/carpeta'

# Llama a la función
png_to_ico(png_path, ico_path, ico_folder)