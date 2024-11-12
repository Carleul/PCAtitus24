const pontos = document.querySelector(".pontos");
const jogador = document.querySelector(".jogador");
const obstaculo = document.querySelector(".obstaculo");
let jaPulou = false;
let count = 0;

document.addEventListener("keydown", (e) => {
  if (e.code === "Space") {
    pulo();
  }
});

function pulo() {
  if (!jogador.classList.contains("pulo")) {
    jogador.classList.add("pulo");
    jaPulou = true;

    setTimeout(() => {
      jogador.classList.remove("pulo");
      jaPulou = false;
    }, 1100);
  }
}

setInterval(() => {
  let jogadorBottom = parseInt(
    window.getComputedStyle(jogador).getPropertyValue("bottom")
  );
  let obstaculoLeft = parseInt(
    window.getComputedStyle(obstaculo).getPropertyValue("left")
  );

  if (obstaculoLeft > 40 && obstaculoLeft < 80 && jogadorBottom <= 80) {
    alert(`Você perdeu! Sua pontuação foi de: ${count}`);
    count = 0;
  }
  count++;
  pontos.innerHTML = `Pontuação: ${count}`;
}, 80);
