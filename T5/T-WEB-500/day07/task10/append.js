document.addEventListener('DOMContentLoaded', function () {
  const listItemInput = document.getElementById('listItem');
  const Button = document.getElementById('Button');
  const footerDiv = document.querySelector('footer div');

  Button.addEventListener('click', function () {
    const inputValue = listItemInput.value;
    const newDiv = document.createElement('div');
    newDiv.textContent = inputValue;
    footerDiv.appendChild(newDiv);
    listItemInput.value = ''; //To clear the listItemInputField
  });
});
