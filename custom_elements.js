class DiamondDiv extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML =
      `<link rel="stylesheet" href="content.css">
      <div class="box">
        <div class="diamond-decal-tl"></div>
        <div class="diamond-decal-tr"></div>
        <div class="diamond-decal-bl"></div>
        <div class="diamond-decal-br"></div>
        <slot></slot>
      </div>`;
  }
}

class ProjectIcon extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const iconTypes = this.getAttribute("types").split(" ");
    this.innerHTML = iconTypes.map(type =>
      `<span class="project-icon ${type}-project">
        <svg>
          <use href="#icon-${type}"></use>
        </svg>
      </span>`).join(" ");
  }
}

customElements.define("diamond-div", DiamondDiv);
customElements.define("project-icon", ProjectIcon);