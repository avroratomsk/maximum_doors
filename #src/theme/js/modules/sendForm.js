import "./functions.js"

// Функция для поиска английских букв в поле ввода
function containsEnglishLetters(str) {
  const regex = /[a-zA-Z]/;
  return regex.test(str);
}


// Функция для нахождения ссылки в поле ввода
function containsLink(input) {
  const regex = /(https?:\/\/[^\s]+)/g;
  return regex.test(input);
}

function validateForm(fieldsArray) {
  if (containsEnglishLetters(fieldsArray.name)) {
    return false;
  }

  if (containsLink(fieldsArray.message)) {
    return false;
  }

  return true;
}

function sendForm(form, popupName = "default") {
  form.addEventListener("submit", function (event) {

    event.preventDefault();

    const eventForm = event.target;
    const formData = new FormData(eventForm);
    const csrfToken = eventForm.querySelector("[name=csrfmiddlewaretoken]").value;

    let dataObj = {};
    for (let [key, value] of formData.entries()) {
      dataObj[key] = value;
    }

    if (validateForm(dataObj)) {
      fetch(form.action, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken
        },
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          form.reset();
          if (popupName !== "default") {
            document.documentElement.classList.remove("popup-show");
            // bodyUnLock();
            document.getElementById(popupName).classList.remove("popup_show");
          }
          // document.getElementById("success").classList.add("notification_show");
        })
        .catch(error => {
          console.log(error);
        });
    }
  });
}

const callBackForm = document.getElementById("callback-form");
console.log(callBackForm)
if (callBackForm) {
  sendForm(callBackForm, "leave-request");
}

const contactForm = document.getElementById("contact-form");
if (contactForm) {
  sendForm(contactForm);
}
