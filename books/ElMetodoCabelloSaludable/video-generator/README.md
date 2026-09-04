# Generador del video promocional vigente

Todo lo necesario vive en este repositorio; no utiliza Downloads ni otras carpetas externas.

Desde la raíz del repositorio, con Python 3.12:

```powershell
python -m venv books/ElMetodoCabelloSaludable/video-generator/.venv
books/ElMetodoCabelloSaludable/video-generator/.venv/Scripts/python -m pip install -r books/ElMetodoCabelloSaludable/video-generator/requirements.txt
books/ElMetodoCabelloSaludable/video-generator/.venv/Scripts/python books/ElMetodoCabelloSaludable/video-generator/generate.py
```

Añadir `--preview` para comprobar duplicados y generar la vista general sin renderizar. En Linux/macOS usar `.venv/bin/python`. FFmpeg viene incluido en imageio-ffmpeg. Windows usa Arial; Linux usa DejaVu Sans. Se pueden definir PROMO_FONT y PROMO_FONT_BOLD con rutas a fuentes TTF.

## Edición y recursos

- `storyboard.json`: títulos, guion de referencia, orden de fotos y páginas.
- `resources/images/author/video-source/`: selección fuente de fotografías.
- `resources/images/books/ElMetodoCabelloSaludable/es/video-pages/`: páginas españolas.
- `resources/audio/ElMetodoCabelloSaludable/narracion.m4a`: narración aprobada.

El validador comprueba rutas, SHA-256, similitud visual dHash, alternancia izquierda/derecha y presencia del libro. Las fotos individuales que aparecen en los tres collages nuevos se retiran del montaje individual. Las ilustraciones y retratos impresos dentro de otras páginas forman parte del libro original. No se duplica el retrato como fondo desenfocado. Todas las escenas incluyen una página, salvo el cierre aprobado donde Yeney sostiene el libro físico. Los fundidos de medio segundo se aplican entre escenas y bloques, sin pantallas negras.

## Salidas

El video dura 180 segundos, con seis bloques de 30 segundos. Los artefactos vigentes se escriben en `resources/videos/`, `resources/images/books/` y `resources/docs/`. Los temporales de este generador están excluidos de Git.
