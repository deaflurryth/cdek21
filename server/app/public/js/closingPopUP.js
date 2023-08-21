// const popup1 = document.getElementById('popup1');
// const trigger_call = document.querySelector('.recallme_button');
// const closeBtn = document.querySelector('.close');
//
// trigger_call.addEventListener('click', (e) => {
//   e.preventDefault();
//   popup1.style.display = 'flex';
// });
//
// popup1.addEventListener('click', (e) => {
//   if (e.target === popup1 || e.target === closeBtn) {
//     popup1.style.display = 'none';
//   }
// });

const popup1 = document.getElementById('popup1');
const closeBtn = popup1.querySelector('.close');
const form = popup1.querySelector('.call-form'); // Получаем форму по классу

const popup2 = document.getElementById('popup2');
const closeBtn2 = popup2.querySelector('.close2');
const form2 = popup2.querySelector('.call-form2'); // Получаем форму по классу

const recallme_button2 = document.querySelector('.callback-bt')

const trigger_call = document.querySelector('.recallme_button');

const trigger_feedback = document.querySelector('.feedback_button');

const recallme_button4 = document.querySelector('.step_recall_button')

const recallme_button3 = document.querySelector('.button_top_grid');

// Закрытие попапа при клике на него или его фон
popup1.addEventListener('click', (e) => {
  if (e.target === popup1) {
    popup1.style.display = 'none';
  }
});

// Добавьте событие для открытия попапа при клике на ссылку

trigger_call.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup1.style.display = 'flex'; // Отображаем попап
});

closeBtn.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup1.style.display = 'none'; // Закрываем попап при клике на крестик
});

form.addEventListener('submit', (e) => {
  e.preventDefault(); // Предотвращаем отправку формы
  // Здесь вы можете добавить логику для обработки отправки формы, например, отправку данных на сервер
  popup1.style.display = 'none'; // Закрываем попап после отправки формы
});



// Закрытие попапа при клике на него или его фон
popup2.addEventListener('click', (e) => {
  if (e.target === popup2) {
    popup2.style.display = 'none';
  }
});



// Добавьте событие для открытия попапа при клике на ссылку
trigger_feedback.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup2.style.display = 'flex'; // Отображаем попап
});

closeBtn2.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup2.style.display = 'none'; // Закрываем попап при клике на крестик
});

form2.addEventListener('submit', (e) => {
  e.preventDefault(); // Предотвращаем отправку формы
  // Здесь вы можете добавить логику для обработки отправки формы, например, отправку данных на сервер
  popup2.style.display = 'none'; // Закрываем попап после отправки формы
});

recallme_button2.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup1.style.display = 'flex'; // Отображаем попап
});

recallme_button3.addEventListener('click', (e) => {
  e.preventDefault(); // Предотвращаем переход по ссылке
  popup1.style.display = 'flex'; // Отображаем попап
});

recallme_button4.addEventListener('click', (e) => {  e.preventDefault(); // Предотвращаем переход по ссылке
  popup1.style.display = 'flex'; // Отображаем попап
});
