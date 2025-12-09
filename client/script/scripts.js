const text = document.querySelector("#text");
const password = document.querySelector("#password");
const btnlogin = document.querySelector("#btnlogin");

btnlogin.addEventListener("click", (e) => {
  console.log(text);
  console.log(text.value);
  console.log(password);
  console.log(password.value);
  options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      login: text.value,
      password: password.value,
    }),
  };
  fetch("https://ex-kerst-2025.onrender.com/user/", options)
    .then((result) => result.json())
    .then((data) => {
      console.log(data);
    });
});
