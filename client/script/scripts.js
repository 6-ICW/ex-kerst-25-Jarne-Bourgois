// vraag 1

// een textbox met id text?? 
const text = document.querySelector("#text");
const password = document.querySelector("#password");
const btnlogin = document.querySelector("#btnlogin");
// vraag 2
currentPSW = document.querySelector("#currentPSW");
newPSW = document.querySelector("#newPSW");
ConfirmNewPSW = document.querySelector("#ConfirmNewPSW");
btnUpdate = document.querySelector("#btnUpdate");

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
      // Je krijgt een resultaat terug maar print het enkel uit. 
      // wellicht door het refreshen van je pagina
      console.log(data);
    });
});

btnUpdate.addEventListener("click", (e) => {
  options = {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id: 1,
      password: newPSW.value,
    }),
  };
  fetch("https://ex-kerst-2025.onrender.com/user/", options)
    .then((result) => result.json())
    .then((data) => {
      console.log(data);
    });
});
