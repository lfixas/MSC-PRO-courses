document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('button');
  
    button.addEventListener('click', function () {
      const paragraphs = document.querySelectorAll('p');
  
      paragraphs.forEach((paragraph) => {
        paragraph.style.display = 'none';
      });
    });
  });
  