const menuIcon = document.querySelector('.menu-icon');
const hiddenMenu = document.querySelector('.hidden-menu');
const newImage = new Image();
newImage.src = 'images/menu_icon_2.svg';

menuIcon.addEventListener('click', () => {
  hiddenMenu.classList.toggle('active');

  const menuIconImage = menuIcon.querySelector('img');
  if (menuIconImage.getAttribute('src') === 'images/menu_icon.svg') {
    menuIconImage.setAttribute('src', newImage.src);
  } else {
    menuIconImage.setAttribute('src', 'images/menu_icon.svg');
  }
});
