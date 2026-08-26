const kindle = 'https://kdp.amazon.com/amazon-dp-action/us/dualbookshelf.marketplacelink/B0HDKQTKZ9';
const paperback = 'https://kdp.amazon.com/amazon-dp-action/us/dualbookshelf.marketplacelink/B0HFHC2QL7';

export function Header() {
  return <nav className="nav wrap"><a className="brand" href="/"><span>YL</span> Yeney López-Pérez</a><div className="navlinks"><a href="/el-metodo">El método</a><a href="/el-libro">El libro</a><a href="/la-autora">La autora</a><a href="/preguntas">Preguntas</a><a className="navcta" href={paperback} target="_blank" rel="noreferrer">Comprar</a></div></nav>;
}

export function PurchaseButtons() {
  return <div className="actions"><a className="button primary" href={paperback} target="_blank" rel="noreferrer">Comprar tapa blanda <span>↗</span></a><a className="button ghost" href={kindle} target="_blank" rel="noreferrer">Leer en Kindle <span>↗</span></a></div>;
}

export function Footer() {
  return <footer className="wrap"><a className="brand" href="/"><span>YL</span> Yeney López-Pérez</a><div className="footerLinks"><a href="/el-metodo">El método</a><a href="/el-libro">El libro</a><a href="/la-autora">La autora</a><a href="/preguntas">Preguntas</a></div><p>© 2026 Yeney López-Pérez</p></footer>;
}
