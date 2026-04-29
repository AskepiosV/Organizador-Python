
# 🗂️ File Organizer (Python)

Script en Python para organizar automáticamente archivos en una carpeta según su tipo.

---

## 🚀 Descripción

Este proyecto permite clasificar archivos dentro de una carpeta (por defecto `Descargas`) en subcarpetas como:

* 📷 Imagenes
* 📄 Documentos
* 📦 Comprimidos
* 🧲 Torrents
* 📁 Sin Categoria

Evita sobrescribir archivos existentes generando nombres únicos automáticamente.

---

## ⚙️ Características

* Detecta tipo de archivo por extensión
* Crea carpetas automáticamente
* Evita sobrescribir archivos (`archivo_1.pdf`, `archivo_2.pdf`, etc.)
* Ignora carpetas (solo procesa archivos)
* Funciona en Linux (probado en Arch Linux)

---

## 📦 Estructura de ejemplo

Antes:

```
Descargas/
├── foto.jpg
├── documento.pdf
├── archivo.zip
```

Después:

```
Descargas/
├── Imagenes/
│   └── foto.jpg
├── Documentos/
│   └── documento.pdf
├── Comprimidos/
│   └── archivo.zip
```

---

## ▶️ Uso

```bash
python organizador.py
```

---

## 🛠 Tecnologías usadas

* Python 3
* pathlib

---

## 📌 Mejoras futuras

* [ ] Modo simulación (`--dry-run`)
* [ ] Configuración con JSON
* [ ] CLI con argumentos (`argparse`)
* [ ] Logs de actividad
* [ ] Ignorar carpetas específicas

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica para aprender Python, automatización y manejo de archivos en Linux.

---

## 💡 Notas

Este proyecto forma parte de mi aprendizaje como desarrollador y está en constante mejora.
