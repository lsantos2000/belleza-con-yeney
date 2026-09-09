import { cp, mkdir, rm } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const copies = [
  ['resources/images/author/gallery', 'public/yeney-gallery'],
  ['resources/images/author/video-source', 'public/media/video-promocional/fotos-unicas'],
  ['resources/images/books/ElMetodoCabelloSaludable/es/web-pages', 'public/book-pages'],
  ['resources/images/books/ElMetodoCabelloSaludable/es/video-pages', 'public/media/video-promocional/paginas-libro'],
  ['resources/audio/ElMetodoCabelloSaludable/narracion.m4a', 'public/media/video-promocional/audio/narracion.m4a'],
  ['resources/videos/ElMetodoCabelloSaludable/el-metodo-cabello-saludable-promo-3-minutos.mp4', 'public/media/video-promocional/video/el-metodo-cabello-saludable-promo-3-minutos.mp4'],
  ['resources/demo/El_Metodo_Cabello_Saludable-demo.pdf', 'public/El-metodo-cabello-saludable-de-yeny-demo.pdf'],
  ['resources/demo/The_Healthy_Hair_Method_v48_demo_en_20260909.pdf', 'public/The-Healthy-Hair-Method-demo-en.pdf'],
  ['resources/images/books/ElMetodoCabelloSaludable/en/libro-portada-en.png', 'public/libro-portada-en.png'],
];

for (const [source, destination] of copies) {
  const to = join(root, destination);
  await rm(to, { recursive: true, force: true });
  await mkdir(dirname(to), { recursive: true });
  await cp(join(root, source), to, { recursive: true });
}
console.log('Shared resources synchronized to public web paths.');
