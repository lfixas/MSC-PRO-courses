const canvas = document.querySelector('canvas');
const canv = canvas.getContext('2d');

// canv.fillStyle = 'white';
canv.strokeStyle = 'white';
canv.moveTo(6, 6);
canv.lineTo(14, 10);
canv.lineTo(6, 14);
canv.lineTo(6, 6);
// canv.fill();
canv.stroke();

const pauseButton = document.querySelector('footer').getElementsByTagName('button')[0];
const stopButton = document.querySelector('footer').getElementsByTagName('button')[1];
const muteButton = document.querySelector('footer').getElementsByTagName('button')[2];

const content = document.querySelector('pre').textContent.trim();

const audio = new Audio();
audio.src = content;

canvas.addEventListener('click', () => {
  audio.play();
});

pauseButton.addEventListener('click', () => {
  audio.pause();
});

stopButton.addEventListener('click', () => {
  audio.pause();
  audio.currentTime = 0;
});

muteButton.addEventListener('click', () => {
  audio.muted = !audio.muted;
});