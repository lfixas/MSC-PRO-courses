document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const textInput = document.querySelector('#text-input');
  const dropdown = document.querySelector('#dropdown');
  const list = document.querySelector('#bullet-list');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const text = textInput.value.trim();
    const option = dropdown.value;
    if (text && option) {
      const listItem = document.createElement('li');
      listItem.textContent = text;
      listItem.classList.add(option);
      list.appendChild(listItem);
      textInput.value = '';
    }
  });
});
