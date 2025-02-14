const OK = document.querySelector('footer div:nth-child(1) a');
const whiteBox1 = document.querySelector('footer').getElementsByTagName('div')[0];
const footer = document.querySelector('footer');
const whiteBox2 = document.createElement('div');
const acceptsCookies = getCookie('acceptsCookies');

OK.addEventListener('click', () => {
  if (acceptsCookies !== 'true') {
    const expires = new Date();
    expires.setDate(expires.getDate() + 1);
    document.cookie = "acceptsCookies=true; expires=" + expires.toUTCString() + "; SameSite=None; Secure";
    secondWhiteBox();
  } else {
    checkCookie();
  }
});

whiteBox2.addEventListener('click', () => {
  deleteCookie();
  firstWhiteBox();
});

function checkCookie() {
  if (acceptsCookies === 'true') {
    secondWhiteBox();
  } else {
    firstWhiteBox();
  }
}

function firstWhiteBox() {
  whiteBox1.innerHTML = 'This site uses cookies, click on OK if you accept their use. <a href="#">OK</a>';
  location.reload()
  if (whiteBox2 && whiteBox2.parentNode) {
    whiteBox2.parentNode.removeChild(whiteBox2);
  }
}

function secondWhiteBox() {
  whiteBox1.textContent = "ㅤ";
  const deleteCookieLink = document.createElement('a');
  deleteCookieLink.href = '#';
  deleteCookieLink.textContent = 'Delete the cookie';
  whiteBox2.textContent = "Do you want to delete your cookie? : ";
  whiteBox2.appendChild(deleteCookieLink);

  footer.appendChild(whiteBox2);
}

function deleteCookie() {
  document.cookie = "acceptsCookies=true; expires=Thu, 01 Jan 1970 00:00:00 UTC; SameSite=None; Secure";
}

function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
    const [cookieName, cookieValue] = cookie.trim().split('=');
    if (cookieName === name) {
      return cookieValue;
    }
  }
  return null;
}