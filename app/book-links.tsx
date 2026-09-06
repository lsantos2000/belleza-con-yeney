import type { SiteLanguage } from './language-switcher';

const paperback = 'https://www.amazon.com/dp/B0HFHC2QL7';
const googlePlay = 'https://play.google.com/store/books/details?id=8VgDEgAAQBAJ';
const youTube = 'https://www.youtube.com/watch?v=xUI1K6fISGw';

const copy = {
  es: {
    tagline: 'Aprende a conocer tu cabello y crea una rutina consciente, práctica y personalizada.',
    links: [
      { icon: '📕', label: 'Consigue el libro impreso o digital en Amazon', href: paperback },
      { icon: '📱', label: 'Disfruta la edición digital en Google Play Books', href: googlePlay },
      { icon: '📖', label: 'Descarga una muestra gratuita del libro', href: '/demo-libro' },
      { icon: '▶️', label: 'Mira la demostración en YouTube', href: youTube },
    ],
  },
  en: {
    tagline: 'Learn to understand your hair and build a conscious, practical, and personalized routine.',
    links: [
      { icon: '📕', label: 'Get the printed or digital book on Amazon', href: paperback },
      { icon: '📱', label: 'Enjoy the digital edition on Google Play Books', href: googlePlay },
      { icon: '📖', label: 'Download a free sample of the book', href: '/en/demo-libro' },
      { icon: '▶️', label: 'Watch the demo on YouTube', href: youTube },
    ],
  },
} as const;

export default function BookLinks({ lang = 'es' }: { lang?: SiteLanguage }) {
  const t = copy[lang];
  return <div className="bookLinks">
    <p className="bookLinksLead">{t.tagline}</p>
    <ul>{t.links.map(link => <li key={link.href}><span aria-hidden="true">{link.icon}</span><a href={link.href} target="_blank" rel="noopener noreferrer">{link.label} <span aria-hidden="true">↗</span></a></li>)}</ul>
  </div>;
}
