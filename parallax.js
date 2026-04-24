const r = document.querySelector(':root');
const b = document.body;

addEventListener("load", setHeight, { passive: true });
addEventListener("resize", setHeight, { passive: true });
function setHeight(_) {
  const height = b.scrollHeight;
  r.style.setProperty('--page-height', `${height}px`);
  setScroll();
}

let latestScroll = 0;
let prevScroll = -1;

b.addEventListener("scroll", () => {
  setScroll();
}, { passive: true });

function setScroll() {
  latestScroll = b.scrollTop
}

function loop() {
  if (latestScroll !== prevScroll) {
    r.style.setProperty('--page-scroll', `-${latestScroll}px`);
    prevScroll = latestScroll;
  }
  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);