document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('.call-form');
  const nameInput = form.querySelector('.input-field:nth-of-type(1)');
  const phoneInput = form.querySelector('.input-field:nth-of-type(2)');
  const submitButton = form.querySelector('.action-button');

  submitButton.addEventListener('click', function (event) {
    event.preventDefault();

    const name = nameInput.value;
    const phone = phoneInput.value;

    const data = {
      name: name,
      phone: phone
    };
    console.log(data)
    fetch('https://test-cdek-danyanara.amvera.io/dashboard', {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(data),
    mode: "cors",
    headers: {
        "Content-Type": "application/json"
    }
    })
      .then(response => response.json())
      .then(result => {
        console.log(result);
      })
      .catch(error => {
        console.error('Ошибка при отправке запроса:', error);
      });

    return false;
  });
});


document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('.call-form2');
  const nameInput = form.querySelector('.input-field2:nth-of-type(1)');
  const phoneInput = form.querySelector('.input-field2:nth-of-type(2)');
  const commitInput = form.querySelector('.input-field2:nth-of-type(3)');
  const submitButton = form.querySelector('.action-button2');

  submitButton.addEventListener('click', function (event) {
    event.preventDefault();

    const name = nameInput.value;
    const phone = phoneInput.value;
    const commit = commitInput.value;
    const data = {
      name: name,
      phone: phone,
      commit: commit
    };
    console.log(data)
    fetch('http://127.0.0.1:8000/', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(result => {
        console.log(result);
      })
      .catch(error => {
        console.error('Ошибка при отправке запроса:', error);
      });

    return false;
  });
});