#Problema 12

def obtener_tipo_mime(nombre_archivo):
    # Convertir el nombre del archivo a minúsculas para evitar problemas con la comparación
    nombre_archivo = nombre_archivo.lower()
    
    # Diccionario de sufijos y sus tipos MIME correspondientes
    tipos_MIME = {
        '.gif': 'image/gif', 
        '.jpg': 'image/jpeg', 
        '.jpeg': 'image/jpeg', 
        '.png': 'image/png', 
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    
    # Buscar el tipo MIME basado en el sufijo del archivo
    for sufijo, mime in tipos_MIME.items():
        if nombre_archivo.endswith(sufijo):
            return mime
    
    # Si el sufijo no está en la lista, devolver 'application/octet-stream'
    return 'application/octet-stream'

# Solicitar el nombre del archivo al usuario
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener y mostrar el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)
print(tipo_mime)