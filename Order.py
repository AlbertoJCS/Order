import os
import shutil

#obtener ruta actual
ruta_actual = os.path.dirname(__file__)

# Obtener la lista de archivos en el directorio de origen
archivos = os.listdir(ruta_actual)

# Mapeo de extensiones a carpetas de destino
extension_carpetas = {
    #extensiones documentos de texto
    '.txt': 'archivos_Word_txt',
    '.docx': 'archivos_Word_txt',
    '.doc': 'archivos_Word_txt',
    '.docm': 'archivos_Word_txt',
    '.odt': 'archivos_Word_txt',
    #extensiones de excel
    '.xlsx': 'archivos_Excel',
    '.csv': 'archivos_Excel',
    '.xlsm': 'archivos_Excel',
    '.xlsb': 'archivos_Excel',
    '.xls': 'archivos_Excel',
    #extensiones de imagenes
    '.jpg': 'archivos_Img',
    '.png': 'archivos_Img',
    '.jpeg': 'archivos_Img',
    '.gif': 'archivos_Img',
    '.svg': 'archivos_Img',
    '.bmp': 'archivos_Img',
    '.ico': 'archivos_Img',
    #extensiones Pdf
    '.pdf': 'archivos_Pdf',
    #extensiones iso
    '.iso': 'archivos_ISO',
    #extensiones archivos comprimidos
    '.zip': 'archivos_Comprimidos',
    '.rar': 'archivos_Comprimidos',
    '.7z': 'archivos_Comprimidos',
    '.rar5': 'archivos_Comprimidos',
    '.gz': 'archivos_Comprimidos',
    '.tar.bz2': 'archivos_Comprimidos',
    #extensiones archivos multimedia
    '.mp4': 'archivos_Video_Audio',
    '.mp3': 'archivos_Video_Audio',
    '.wmv': 'archivos_Video_Audio',
    '.avi': 'archivos_Video_Audio',
    '.mpg': 'archivos_Video_Audio',
    '.mkv': 'archivos_Video_Audio',
    #extensiones de presentaciones
    '.pptx': 'archivos_Presentaciones',
    '.pptm': 'archivos_Presentaciones',
    '.ppt': 'archivos_Presentaciones',
    #extensiones de ejecutables
    '.exe': 'archivos_Ejecutables',
    '.msi': 'archivos_Ejecutables',
    '.vsix': 'archivos_Ejecutables',
    #extensiones de progra
    '.bat': 'archivos_Progra',
    '.java': 'archivos_Progra',
    '.js': 'archivos_Progra',
    '.c': 'archivos_Progra',
    '.html': 'archivos_Progra',
    '.url': 'archivos_Progra',
    '.css': 'archivos_Progra',
    '.php': 'archivos_Progra',
}

def mover_archivos():
    for archivo in archivos:
        if os.path.isfile(os.path.join(ruta_actual, archivo)):
            nombre, extension = os.path.splitext(archivo)
            if extension.lower() in extension_carpetas:
                carpeta_destino = os.path.join(ruta_actual, extension_carpetas[extension])
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                shutil.move(os.path.join(ruta_actual, archivo), os.path.join(carpeta_destino, archivo))
                print(f"Archivo {archivo} movido a {carpeta_destino}\n")
            else:
                print(f"No se encontró una carpeta destino para la extensión de archivo {archivo}\n")

# Llamar a la función para mover los archivos
mover_archivos()