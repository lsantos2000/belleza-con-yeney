'use client';
import { useRef } from 'react';

const order=[38,39,40,41,44,22,23,25,19,20,21,11,12,13,14,15,16,17,31,32,33,26,27,28,29,30,1,2,3,4,5,6,7,9,10,18,34,36,47,48,49,50,51];
const photos=order.map(i=>`/yeney-gallery/yeney-${String(i).padStart(2,'0')}.jpg`);

export default function AuthorCarousel(){
  const track=useRef<HTMLDivElement>(null);
  const move=(direction:number)=>track.current?.scrollBy({left:direction*Math.min(window.innerWidth*.78,720),behavior:'smooth'});
  return <div className="carouselShell"><div className="carouselTop"><p>{photos.length} fotografías únicas · primero, las que mejor muestran el cabello</p><div><button onClick={()=>move(-1)} aria-label="Fotografía anterior">←</button><button onClick={()=>move(1)} aria-label="Fotografía siguiente">→</button></div></div><div className="authorCarousel" ref={track}>{photos.map((src,i)=><figure key={src}><img src={src} alt={`Yeney López-Pérez, fotografía ${i+1}`} loading={i<3?'eager':'lazy'}/><figcaption>{String(i+1).padStart(2,'0')} / {photos.length}</figcaption></figure>)}</div></div>
}
