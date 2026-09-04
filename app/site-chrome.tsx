import { LanguageSwitcher, type SiteLanguage } from './language-switcher';

const paperback = 'https://www.amazon.com/dp/B0HFHC2QL7';
const googlePlay = 'https://play.google.com/store/books/details?id=8VgDEgAAQBAJ';
const prefix = (lang: SiteLanguage) => lang === 'en' ? '/en' : '';

export function MobileMenu({ lang = 'es' }: { lang?: SiteLanguage }) {
  const p = prefix(lang);
  return <details className="mobileMenu"><summary aria-label={lang === 'es' ? 'Abrir menú' : 'Open menu'}><span></span><span></span><span></span></summary><div><a href={`${p}/`}>{lang === 'es' ? 'Inicio' : 'Home'}</a><a href={`${p}/el-metodo`}>{lang === 'es' ? 'El método' : 'The method'}</a><a href={`${p}/el-libro`}>{lang === 'es' ? 'El libro' : 'The book'}</a><a href={`${p}/demo-libro`}>PDF demo</a><a href={`${p}/la-autora`}>{lang === 'es' ? 'La autora' : 'The author'}</a><a href={`${p}/preguntas`}>{lang === 'es' ? 'Preguntas' : 'Questions'}</a><strong className="mobileBuyLabel">{lang === 'es' ? 'Comprar' : 'Buy'}</strong><a href={paperback} target="_blank" rel="noreferrer">{lang === 'es' ? 'Amazon Kindle/Libro Impreso' : 'Amazon Kindle/Printed Book'}</a><a href={googlePlay} target="_blank" rel="noreferrer">{lang === 'es' ? 'Google Play Libros PDF/ePub' : 'Google Play Books PDF/ePub'}</a></div></details>;
}

function PurchaseMenu({ lang = 'es' }: { lang?: SiteLanguage }) {
  return <details className="purchaseMenu"><summary>{lang === 'es' ? 'Comprar' : 'Buy'} <span aria-hidden="true">⌄</span></summary><div><a href={paperback} target="_blank" rel="noreferrer"><strong>Amazon</strong><small>{lang === 'es' ? 'Kindle/Libro Impreso' : 'Kindle/Printed Book'}</small></a><a href={googlePlay} target="_blank" rel="noreferrer"><strong>{lang === 'es' ? 'Google Play Libros' : 'Google Play Books'}</strong><small>PDF/ePub</small></a></div></details>;
}

export function Header({ lang = 'es', path = '/' }: { lang?: SiteLanguage; path?: string }) {
  const p = prefix(lang);
  return <nav className="nav wrap" aria-label={lang === 'es' ? 'Navegación principal' : 'Main navigation'}><MobileMenu lang={lang}/><a className="brand" href={`${p}/`}><span>YL</span> Yeney López-Pérez</a><div className="navlinks"><a href={`${p}/el-metodo`}>{lang === 'es' ? 'El método' : 'The method'}</a><a href={`${p}/el-libro`}>{lang === 'es' ? 'El libro' : 'The book'}</a><a href={`${p}/demo-libro`}>Demo</a><a href={`${p}/la-autora`}>{lang === 'es' ? 'La autora' : 'The author'}</a><a href={`${p}/preguntas`}>{lang === 'es' ? 'Preguntas' : 'Questions'}</a><PurchaseMenu lang={lang}/><LanguageSwitcher lang={lang} path={path}/></div></nav>;
}

export function PurchaseButtons({ lang = 'es' }: { lang?: SiteLanguage }) {
  return <div className="purchaseInfo"><h3>{lang === 'es' ? 'Información de compra' : 'Purchase info'}</h3><p>{lang === 'es' ? 'Libro impreso y digital en Amazon Books. Edición digital en Google Play Books.' : 'Printed and digital book on Amazon Books. Digital edition on Google Play Books.'}</p><div className="actions purchaseActions"><a className="button amazonButton" href={paperback} target="_blank" rel="noreferrer">{lang === 'es' ? 'Amazon Books · Libro impreso y digital' : 'Amazon Books · Printed and digital book'} <span>↗</span></a><a className="button googlePlay" href={googlePlay} target="_blank" rel="noreferrer">{lang === 'es' ? 'Google Play Books · Edición digital' : 'Google Play Books · Digital edition'} <span>↗</span></a></div><p><a href="https://www.youtube.com/watch?v=xUI1K6fISGw" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'underline', textUnderlineOffset: '0.2em' }}>{lang === 'es' ? 'YouTube Demo' : 'YouTube Demo'} <span aria-hidden="true">↗</span></a></p><p><strong>{lang === 'es' ? 'Reserva tu copia HOY MISMO.' : 'Reserve your copy TODAY.'}</strong></p></div>;
}

export function Footer({ lang = 'es' }: { lang?: SiteLanguage }) {
  const p = prefix(lang);
  return <footer className="wrap"><a className="brand" href={`${p}/`}><span>YL</span> Yeney López-Pérez</a><div className="footerLinks"><a href={`${p}/el-metodo`}>{lang === 'es' ? 'El método' : 'The method'}</a><a href={`${p}/el-libro`}>{lang === 'es' ? 'El libro' : 'The book'}</a><a href={`${p}/demo-libro`}>PDF demo</a><a href={`${p}/la-autora`}>{lang === 'es' ? 'La autora' : 'The author'}</a><a href={`${p}/preguntas`}>{lang === 'es' ? 'Preguntas' : 'Questions'}</a></div><p>© 2026 Yeney López-Pérez</p></footer>;
}
