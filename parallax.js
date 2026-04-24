const r = document.querySelector(':root');
const b = document.body;

addEventListener("load", setHeight);
addEventListener("resize", setHeight);
function setHeight(_) {
  const height = b.scrollHeight;
  r.style.setProperty('--page-height', `${height}px`);
  setScroll();
}

let ticking = false;
b.addEventListener("scroll", onScroll);
function onScroll() {
  if (!ticking) {
    requestAnimationFrame(setScroll);
    ticking = true;
  }
}
function setScroll() {
  const scroll = b.scrollTop;
  r.style.setProperty('--page-scroll', `-${scroll}px`);
  ticking = false;
}
setHeight();