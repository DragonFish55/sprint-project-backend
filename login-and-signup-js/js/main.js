function switchSignup() {
  var left_cover = document.getElementById('left-cover');
  var left_form = document.getElementById('left-form');

  var right_cover = document.getElementById('right-cover');
  var right_form = document.getElementById('right-form');
  right_form.classList.add('fade-in-element');
  left_cover.classList.add('fade-in-element');

  left_form.classList.add('form-hide');
  left_cover.classList.remove('cover-hide');
  right_form.classList.remove('form-hide');
  right_cover.classList.add('cover-hide');
}
async function callSignup() {
  let url = baseUrl + '/api/signup';
  let username = document.getElementById('signup-username').value;
  let password = document.getElementById('signup-password').value;
  let confirmpass = document.getElementById('signup-cpassword').value;
  let myBody = {
    username,
    password,
    confirmpass,
  };
  const response = await fetch(url, {
    method: 'POST',
    body: myBody,
    headers: {
      'Content-Type': 'application/json',
    },
  });
  const myJson = await response.json();
}

async function callLogin() {
  let url = baseUrl + '/api/login';
  let username = document.getElementById('login-username').value;
  let password = document.getElementById('login-password').value;
  let myBody = {
    username,
    password,
  };
  const response = await fetch(url, {
    method: 'POST',
    body: myBody,
    headers: {
      'Content-Type': 'application/json',
    },
  });
  const myJson = await response.json();
}
