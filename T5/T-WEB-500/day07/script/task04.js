const increaseButton = document.querySelector('footer').getElementsByTagName('button')[0];
const decreaseButton = document.querySelector('footer').getElementsByTagName('button')[1];
const backgroundColor = document.querySelector('footer').getElementsByTagName('select')[0];

increaseButton.addEventListener('click', () => {
  const currentFontSize = parseFloat(getComputedStyle(document.body).fontSize);
  var newfontSize = currentFontSize + 2;
  document.body.style.fontSize = `${newfontSize}px`;
});

decreaseButton.addEventListener('click', () => {
  const currentFontSize = parseFloat(getComputedStyle(document.body).fontSize);
  var newfontSize = currentFontSize - 2;
  document.body.style.fontSize = `${newfontSize}px`;
});

backgroundColor.addEventListener('change', () => {
  const hexColor = backgroundColor.value;
  document.body.style.backgroundColor = hexColor;
});
