# Belleza con Yeney

Sitio web oficial bilingüe de **Yeney López-Pérez**, autora de *El Método Cabello Saludable*. Presenta el libro, su método, una galería de la autora, preguntas frecuentes y una demostración descargable en PDF.

**Producción:** [belleza-con-yeney.pages.dev](https://belleza-con-yeney.pages.dev/)

## Características

- Español como idioma inicial y versión inglesa completa bajo `/en`.
- Selector `Español / English` que conserva la página actual y guarda la preferencia en una cookie.
- Diseño adaptable para escritorio y dispositivos móviles.
- Menú móvil accesible.
- Carrusel de fotografías que respeta el encuadre original de las imágenes.
- Demo del libro integrada en el navegador y disponible para descargar.
- Enlaces de compra oficiales para Amazon y Google Play Books.
- Sitio informativo sin autenticación ni recopilación de cuentas de usuario.

## Páginas

| Español | English | Contenido |
| --- | --- | --- |
| `/` | `/en/` | Página principal |
| `/el-metodo/` | `/en/el-metodo/` | Explicación del método |
| `/el-libro/` | `/en/el-libro/` | Interior y contenido del libro |
| `/demo-libro/` | `/en/demo-libro/` | Lector y descarga del PDF demo |
| `/la-autora/` | `/en/la-autora/` | Biografía y galería de Yeney |
| `/preguntas/` | `/en/preguntas/` | Preguntas frecuentes |

## Enlaces del libro

- [Amazon — Kindle y libro impreso](https://www.amazon.com/dp/B0HFHC2QL7)
- [Google Play Books — Ebook](https://play.google.com/store/books/details?id=8VgDEgAAQBAJ)

## Tecnología

- Next.js 16 y React 19
- Vinext y Vite
- TypeScript
- Tailwind CSS 4
- Cloudflare Pages
- pnpm

Se requiere Node.js `22.13.0` o posterior.

## Desarrollo local

```bash
pnpm install
pnpm dev
```

El servidor de desarrollo indicará la URL local disponible.

## Comandos

```bash
pnpm dev      # desarrollo local
pnpm build    # compilación de producción
pnpm start    # ejecutar la compilación localmente
pnpm lint     # revisar el código
```

## Estructura principal

```text
app/
  en/                    # rutas traducidas al inglés
  demo-libro/            # lector del PDF
  el-libro/              # muestras del interior
  el-metodo/             # explicación del método
  la-autora/             # biografía y carrusel
  preguntas/             # preguntas frecuentes
  author-carousel.tsx    # orden y comportamiento del carrusel
  language-switcher.tsx  # cookie y cambio de idioma
  site-chrome.tsx        # navegación, compras y pie de página
public/
  book-pages/            # páginas de muestra
  yeney-gallery/         # fotografías de la autora
```

El PDF público mantiene un nombre estable para permitir futuras sustituciones sin cambiar los enlaces:

```text
public/El-metodo-cabello-saludable-de-yeny-demo.pdf
```

## Publicación

La versión pública se aloja en el proyecto de Cloudflare Pages `belleza-con-yeney`. Antes de publicar, ejecuta `pnpm build` y confirma que las doce rutas en español e inglés se generen correctamente.

## Derechos

El contenido editorial, el libro y las fotografías pertenecen a sus respectivos titulares. Este repositorio no incluye una licencia de reutilización; su publicación pública no concede derechos sobre esos materiales.

