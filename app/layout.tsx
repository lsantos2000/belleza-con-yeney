import type { Metadata } from 'next';
import './globals.css';
import './purchase-menu.css';

export const metadata: Metadata = {
  title: 'El Método Cabello Saludable | Yeney López-Pérez',
  description: 'Una guía cálida y práctica para comprender, nutrir y transformar la relación con tu cabello.',
  openGraph: { title: 'El Método Cabello Saludable', description: 'Cuida tu cabello desde el conocimiento y el amor.', images: ['/og.png'] },
  twitter: { card: 'summary_large_image', title: 'El Método Cabello Saludable', description: 'Cuida tu cabello desde el conocimiento y el amor.', images: ['/og.png'] },
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="es"><body>{children}</body></html>;
}

