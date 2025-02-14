const whiteBox1 = document.querySelector('footer').getElementsByTagName('div')[0];
const whiteBox2 = document.querySelector('footer').getElementsByTagName('div')[1];
const canvas = document.querySelector('canvas');

whiteBox1.style.position = "relative";
canvas.style.position = "absolute";
canvas.style.userSelect = "none";

function move(xpos, ypos) {
  canvas.style.left = xpos + 'px';
  canvas.style.top = ypos + 'px';
  whiteBox2.textContent = `New coordinates => {x:${xpos}, y:${ypos}}`;
}

let isDragging = false;
let initialX = 0;
let initialY = 0;

canvas.addEventListener("mousedown", (e) => {
  isDragging = true;
  initialX = e.clientX + window.scrollX - canvas.getBoundingClientRect().left;
  initialY = e.clientY + window.scrollY - canvas.getBoundingClientRect().top;
});

document.addEventListener("mousemove", (e) => {
  if (!isDragging) return;
  let posX = e.clientX + window.scrollX - initialX - whiteBox1.getBoundingClientRect().left;
  let posY = e.clientY + window.scrollY - initialY - whiteBox1.getBoundingClientRect().top;

  let boundaryX = whiteBox1.offsetWidth - canvas.offsetWidth - 5;
  let boundaryY = whiteBox1.offsetHeight - canvas.offsetHeight;

  posX = Math.min(Math.max(posX, 0), boundaryX);
  posY = Math.min(Math.max(posY, 0), boundaryY);

  move(posX, posY);
});

document.addEventListener("mouseup", () => {
  isDragging = false;
});
