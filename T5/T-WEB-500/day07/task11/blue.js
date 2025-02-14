document.addEventListener('DOMContentLoaded', function () {
  const paragraphs = document.querySelectorAll('p');

  paragraphs.forEach((paragraph) => {
    paragraph.addEventListener('mouseover', function () {
      paragraph.classList.add('blue');
    });

    paragraph.addEventListener('click', function () {
      paragraph.classList.toggle('highlighted');
    });
  });
});
