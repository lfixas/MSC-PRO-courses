const whiteBox = document.querySelector('footer').getElementsByTagName('div')[0];
var countClick = 0;
function checkClickCounter() {
  countClick++;
  whiteBox.textContent = `${countClick}`;
}

whiteBox.addEventListener("click", checkClickCounter);
