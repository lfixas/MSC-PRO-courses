const whiteBox = document.querySelector('footer').getElementsByTagName('div')[0];

function checkClickDialogBox() {
  const name = prompt("What's your name?");
  if (name === null || name.trim() === "") { //No null or spaces
    checkClickDialogBox();
  } else {
    const confirmed = confirm(`Are you sure that ${name} is your name?`);
  if (confirmed) {
    alert(`Hello ${name}!`);
    whiteBox.textContent = `Hello ${name}!`;
  } else {
    checkClickDialogBox();
  }
  }
}

whiteBox.addEventListener("click", checkClickDialogBox);