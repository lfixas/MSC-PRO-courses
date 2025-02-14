const whiteBox = document.querySelector('footer').getElementsByTagName('div')[0];
var whiteBoxText = "";
document.addEventListener('keydown', (event) => {
  whiteBoxText += event.key;
  whiteBoxText = whiteBoxText.slice(-42);
  whiteBox.textContent = whiteBoxText;
});
