import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'The Healthy Hair Method | Yeney López-Pérez',
  description: 'A warm, practical guide to understanding, nourishing, and transforming your relationship with your hair.',
  openGraph: { title: 'The Healthy Hair Method', description: 'Care for your hair with knowledge and love.', images: ['/og.png'] },
  twitter: { card: 'summary_large_image', title: 'The Healthy Hair Method', description: 'Care for your hair with knowledge and love.', images: ['/og.png'] },
};

export default function EnglishLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return children;
}
