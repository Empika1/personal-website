const r = document.querySelector(':root');
const b = document.body;

addEventListener("load", setHeight);
addEventListener("resize", setHeight);
function setHeight(_) {
  const height = b.scrollHeight;
  console.log({height});
  r.style.setProperty('--page-height', `${height}px`);
}

b.addEventListener("scroll", setScroll);
function setScroll(_) {
  const scroll = b.scrollTop;
  console.log({scroll});
  r.style.setProperty('--page-scroll', `-${scroll}px`);
}
setScroll();