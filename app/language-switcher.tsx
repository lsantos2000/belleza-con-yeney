'use client';

import { useEffect } from 'react';

export type SiteLanguage = 'es' | 'en';

export function LanguageSwitcher({ lang, path }: { lang: SiteLanguage; path: string }) {
  const spanishHref = path;
  const englishHref = path === '/' ? '/en' : `/en${path}`;

  useEffect(() => {
    document.documentElement.lang = lang;
    const saved = document.cookie
      .split('; ')
      .find((entry) => entry.startsWith('yeney_language='))
      ?.split('=')[1];
    if (saved === 'en' && lang !== 'en') window.location.replace(englishHref);
    if (saved === 'es' && lang !== 'es') window.location.replace(spanishHref);
  }, [englishHref, lang, spanishHref]);

  const remember = (value: SiteLanguage) => {
    document.cookie = `yeney_language=${value}; Max-Age=31536000; Path=/; SameSite=Lax`;
  };

  return <div className="languageSwitcher" role="group" aria-label="Idioma / Language">
    <a href={spanishHref} lang="es" aria-current={lang === 'es' ? 'page' : undefined} onClick={() => remember('es')}>Español</a>
    <span aria-hidden="true">/</span>
    <a href={englishHref} lang="en" aria-current={lang === 'en' ? 'page' : undefined} onClick={() => remember('en')}>English</a>
  </div>;
}
