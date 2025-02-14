document.addEventListener('DOMContentLoaded', function () {
  const hyperlinks = document.querySelectorAll('a:not([target="_blank"])');

  hyperlinks.forEach((element) => {
    element.style.opacity = '0.5';
    // element.style.color = "#ff0000";
  });
});
