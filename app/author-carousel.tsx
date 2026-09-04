'use client';
import { useRef } from 'react';

// Existing unique portraits; kitchen/corset photos remain excluded.
const order=[22,19,17,39,23,20,16,40,25,21,36,41,29,15,28,44,30,31,12,38,32,13,10,3,33,11,50,34,14,2,51,6,5,7,26];
// Reuse the new originals already stored in the repo, without duplicate copies.
const newOrder=[13,1,6,10,4,17,19,42];
const photos=[
  ...newOrder.map(i=>`/media/video-promocional/fotos-unicas/yeney-${String(i).padStart(2,'0')}.jpeg`),
  ...order.map(i=>`/yeney-gallery/yeney-${String(i).padStart(2,'0')}.jpg`),
  ...[18,48].map(i=>`/yeney-gallery/yeney-${i}.jpg`),
];

export default function AuthorCarousel({lang='es'}:{lang?:'es'|'en'}){
  const track=useRef<HTMLDivElement>(null);
  const move=(direction:number)=>track.current?.scrollBy({left:direction*Math.min(window.innerWidth*.78,720),behavior:'smooth'});
  return <div className="carouselShell"><div className="carouselTop"><div><button onClick={()=>move(-1)} aria-label={lang==='es'?'Fotografía anterior':'Previous photograph'}>←</button><button onClick={()=>move(1)} aria-label={lang==='es'?'Fotografía siguiente':'Next photograph'}>→</button></div></div><div className="authorCarousel" ref={track}>{photos.map((src,i)=><figure key={src}><img src={src} alt={lang==='es'?`Yeney López-Pérez, fotografía ${i+1}`:`Yeney López-Pérez, photograph ${i+1}`} loading={i<3?'eager':'lazy'}/><figcaption>{String(i+1).padStart(2,'0')} / {photos.length}</figcaption></figure>)}</div></div>
}
