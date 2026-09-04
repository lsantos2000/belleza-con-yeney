# Video promocional de El Método Cabello Saludable

Archivos utilizados en la versión promocional final de tres minutos.

- `video/`: video final en MP4, 1280 × 720.
- `fotos-unicas/`: archivo fuente de fotografías; el montaje vigente utiliza 23 fotos individuales, auditadas por SHA-256 y similitud visual, sin repeticiones. No se utiliza la foto del vestido rojo en la cocina ni el selfie del espejo. Los paneles de frases repetidas se sustituyeron por seis composiciones de páginas. Los tres retratos de la página 15 no se usan como fotos independientes.
- `audio/narracion.m4a`: narración aprobada, reutilizable sin conexión.
- `photo-audit.json`: procedencia de cada fotografía seleccionada.
- `storyboard.jpg` y `verification.json`: vista general y comprobaciones del último render.
- `paginas-libro/`: 41 páginas distintas, utilizadas una sola vez y en orden numérico, incluidos los collages 17, 19 y 21.

La fotografía floral y el selfie del espejo con corsé blanco y jeans quedan excluidos del montaje. Los retratos individuales incluidos en los tres collages nuevos no vuelven a aparecer por separado. Los encabezados superiores usan estilo oración y la última pantalla conserva el diseño aprobado. Yeney alterna entre izquierda y derecha; todas las escenas contienen páginas o el libro físico del cierre. Hay fundidos de medio segundo entre escenas y bloques.

La lógica reproducible está en `tools/video-promo/generate.py`, con instrucciones y dependencias en ese directorio. No depende de rutas externas al repositorio. Las ilustraciones ya impresas dentro de las páginas del libro permanecen intactas; la unicidad auditada corresponde a las fotografías individuales del montaje.

Pendiente de limpieza por bloqueo del entorno: `fotos-autora/` y `fotos-autora-final/` son carpetas antiguas que no se utilizan. Pueden eliminarse; el generador solo utiliza `fotos-unicas/`.
