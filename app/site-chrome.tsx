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
  return <div className="actions purchaseActions"><a className="button amazonButton" href={paperback} target="_blank" rel="noreferrer">{lang === 'es' ? 'Amazon (Kindle/Libro impreso)' : 'Amazon (Kindle/Printed book)'} <span>↗</span></a><a className="button googlePlay" href={googlePlay} target="_blank" rel="noreferrer">Google Play Books (Ebook) <span>↗</span></a></div>;
}

export function Footer({ lang = 'es' }: { lang?: SiteLanguage }) {
  const p = prefix(lang);
  return <footer className="wrap"><a className="brand" href={`${p}/`}><span>YL</span> Yeney López-Pérez</a><div className="footerLinks"><a href={`${p}/el-metodo`}>{lang === 'es' ? 'El método' : 'The method'}</a><a href={`${p}/el-libro`}>{lang === 'es' ? 'El libro' : 'The book'}</a><a href={`${p}/demo-libro`}>PDF demo</a><a href={`${p}/la-autora`}>{lang === 'es' ? 'La autora' : 'The author'}</a><a href={`${p}/preguntas`}>{lang === 'es' ? 'Preguntas' : 'Questions'}</a></div><p>© 2026 Yeney López-Pérez</p></footer>;
}
