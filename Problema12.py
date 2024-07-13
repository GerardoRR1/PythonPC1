#Problema 12

nombre_archivo = input("Ingrese el nombre del archivo: ").lower()

print(nombre_archivo)
tipos_MIME = {
        '.gif': 'image/gif', 
        '.jpg': 'image/jpeg', 
        '.jpeg': 'image/jpeg', 
        '.png': 'image/png', 
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'}

for nombre_archivo in tipos_MIME:
    print()
salida = tipos_MIME.values()
print(salida)