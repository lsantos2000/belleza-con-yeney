'use client';
import { useRef } from 'react';

const photos=Array.from({length:51},(_,i)=>`/yeney-gallery/yeney-${String(i+1).padStart(2,'0')}.jpg`);

export default function AuthorCarousel(){
  const track=useRef<HTMLDivElement>(null);
  const move=(direction:number)=>track.current?.scrollBy({left:direction*Math.min(window.innerWidth*.78,720),behavior:'smooth'});
  return <div className="carouselShell"><div className="carouselTop"><p>51 fotografías · imágenes completas, sin recortes</p><div><button onClick={()=>move(-1)} aria-label="Fotografía anterior">←</button><button onClick={()=>move(1)} aria-label="Fotografía siguiente">→</button></div></div><div className="authorCarousel" ref={track}>{photos.map((src,i)=><figure key={src}><img src={src} alt={`Yeney López-Pérez, fotografía ${i+1}`} loading={i<3?'eager':'lazy'}/><figcaption>{String(i+1).padStart(2,'0')} / {photos.length}</figcaption></figure>)}</div></div>
}
