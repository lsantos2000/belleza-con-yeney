# Generador del video promocional vigente

Todo lo necesario vive en este repositorio; no utiliza Downloads ni otras carpetas externas.

Desde la raíz del repositorio, con Python 3.12:

```powershell
python -m venv tools/video-promo/.venv
tools/video-promo/.venv/Scripts/python -m pip install -r tools/video-promo/requirements.txt
tools/video-promo/.venv/Scripts/python tools/video-promo/generate.py
```

Añadir `--preview` para comprobar duplicados y generar la vista general sin renderizar. En Linux/macOS usar `.venv/bin/python`. FFmpeg viene incluido en imageio-ffmpeg. Windows usa Arial; Linux usa DejaVu Sans. Se pueden definir PROMO_FONT y PROMO_FONT_BOLD con rutas a fuentes TTF.

## Edición y recursos

- `storyboard.json`: títulos, guion de referencia, orden de fotos y páginas.
- `public/media/video-promocional/fotos-unicas/`: selección fuente; el storyboard utiliza 27 fotografías individuales sin repetir y excluye el selfie del espejo.
- `public/media/video-promocional/paginas-libro/`: 41 páginas españolas en orden, incluidas las páginas de collage 17, 19 y 21.
- `public/media/video-promocional/audio/narracion.m4a`: narración aprobada con Yeney. Se reutiliza sin llamar a servicios externos. Si cambia el texto hablado, reemplazar también este audio: cambiar el JSON no cambia la voz.

El validador comprueba rutas, SHA-256, similitud visual dHash, alternancia izquierda/derecha y presencia del libro. Las fotos individuales que aparecen en los tres collages nuevos se retiran del montaje individual. Las ilustraciones y retratos impresos dentro de otras páginas forman parte del libro original. No se duplica el retrato como fondo desenfocado. Todas las escenas incluyen una página, salvo el cierre aprobado donde Yeney sostiene el libro físico. Los fundidos de medio segundo se aplican entre escenas y bloques, sin pantallas negras.

## Salidas

El video dura 180 segundos, con seis bloques de 30 segundos. Se escriben únicamente los artefactos vigentes: `public/media/video-promocional/video/el-metodo-cabello-saludable-promo-3-minutos.mp4`, `storyboard.jpg` y `verification.json`. Se verifica la decodificación completa tras cada render. Los temporales de `tools/video-promo/build/` están excluidos de Git.
