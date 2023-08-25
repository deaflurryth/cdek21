document.addEventListener("DOMContentLoaded", function () {
  const popup = document.getElementById("popup1");
  const sendButton = popup.querySelector(".action-button");
  const nameInput = popup.querySelector(".what_is_ur_name");
  const phoneNumberInput = popup.querySelector(".phone_number_1");
  sendButton.addEventListener("click", function (event) {
    event.preventDefault();
    const name = nameInput.value;
    const phoneNumber = phoneNumberInput.value;

    const url = "https://test-cdek-danyanara.amvera.io/report/dashboard";
    const data = {
      name: name,
      phone: phoneNumber
    };

    console.log("Отправка данных на сервер:", data);

    fetch(url, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(data),
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            }
    })
        .then(response => response.json())
        .catch(error => {
          console.error('Ошибка при отправке запроса:', error);
        });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const popup = document.getElementById("popup2");
  const sendButton = popup.querySelector(".action-button2");
  const nameInput = popup.querySelector(".what_is_ur_name2");
  const phoneNumberInput = popup.querySelector(".phone_number_2");
  const infoInput = popup.querySelector(".short_info_inp");
  sendButton.addEventListener("click", function (event) {
    event.preventDefault();
    const name = nameInput.value;
    const phoneNumber = phoneNumberInput.value;
    const shorterInfo = infoInput.value;
    const url = "https://test-cdek-danyanara.amvera.io/report/dashboard";
    const data = {
      name: name,
      phone: phoneNumber,
      info: shorterInfo
    };

    console.log("Отправка данных на сервер:", data);

    fetch(url, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(data),
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            }
    })
        .then(response => response.json())
        .catch(error => {
          console.error('Ошибка при отправке запроса:', error);
        });
  });
});

