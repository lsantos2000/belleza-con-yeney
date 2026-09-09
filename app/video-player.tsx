import type { SiteLanguage } from './language-switcher';

// Promotional video for El Método Cabello Saludable, hosted on YouTube.
const videoId = 'xUI1K6fISGw';
const watchUrl = `https://www.youtube.com/watch?v=${videoId}`;
const embedUrl = `https://www.youtube-nocookie.com/embed/${videoId}?rel=0`;

const copy = {
  es: {
    eyebrow: 'Video de presentación',
    heading: 'Conoce el método en tres minutos.',
    lead: 'Un recorrido breve por El Método Cabello Saludable: qué encontrarás dentro del libro y cómo puede acompañarte en tu rutina diaria.',
    title: 'Video de presentación de El Método Cabello Saludable',
    note: '¿Prefieres verlo en YouTube?',
    link: 'Abrir el video',
  },
  en: {
    eyebrow: 'Introduction video',
    heading: 'Meet the method in three minutes.',
    lead: 'A short walkthrough of The Healthy Hair Method: what you will find inside the book and how it can support your daily routine.',
    title: 'Introduction video for The Healthy Hair Method',
    note: 'Prefer to watch it on YouTube?',
    link: 'Open the video',
  },
} as const;

export default function VideoPlayer({ lang = 'es' }: { lang?: SiteLanguage }) {
  const t = copy[lang];
  return <section className="videoBand" id="video" aria-labelledby="videoHeading"><div className="wrap">
    <div className="videoIntro"><p className="eyebrow">{t.eyebrow}</p><h2 id="videoHeading">{t.heading}</h2><p className="lead">{t.lead}</p></div>
    <div className="videoFrame"><iframe src={embedUrl} title={t.title} loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen/></div>
    <p className="videoNote">{t.note} <a href={watchUrl} target="_blank" rel="noopener noreferrer">{t.link} <span aria-hidden="true">↗</span></a></p>
  </div></section>;
}
