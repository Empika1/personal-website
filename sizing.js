var root = document.querySelector(':root');
var body = document.body;
var bottom = document.getElementById("bottom");

function getPageOffset(el) {
    let top = 0;
    while (el) {
        top += el.offsetTop;
        el = el.offsetParent;
    }
    return top;
}

function getContentHeight() {
    return getPageOffset(bottom);
}

function updateHeightAndScroll() {
    const ch = getContentHeight()
    root.style.setProperty("--content-height", `${ch}px`);
}

window.onresize = updateHeightAndScroll;
updateHeightAndScroll();