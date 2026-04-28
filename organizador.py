from pathlib import Path

extenciones = {
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
    categoria = extenciones.get(i.suffix, "Sin Categoria")
    destino = ruta / categoria 
    destino.mkdir(exist_ok =True)
    i.rename (destino / i.name)

print ("Todo ordenado... Askepios")







