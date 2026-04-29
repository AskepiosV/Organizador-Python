from pathlib import Path

extenciones = {
    ".png": "Imagenes",
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".docx": "Documentos",
    ".pdf": "Documentos",
    ".rar": "Comprimidos",
    ".zip": "Comprimidos",
    ".torrent": "Torrents"
}

ruta = Path.home() / "Descargas"

for i in ruta.iterdir():
    if i.is_dir():
        continue
    categoria = extenciones.get(i.suffix.lower(), "Sin Categoria")
    destino = ruta / categoria 
    destino.mkdir(exist_ok =True)
    rutaFinal = destino / i.name
    count = 1 
    while rutaFinal.exists():
        nuevoNombre = (i.stem + str(count) + i.suffix ) 
        rutaFinal = destino / nuevoNombre
        count += 1 
        
    i.rename (rutaFinal)

print ("Todo ordenado... Askepios")

