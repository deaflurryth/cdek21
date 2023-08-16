const sliderContent = document.querySelector('.slider-content');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');
const images = document.querySelectorAll('.slider-content img');

const imageWidth = 200; // Замените это на фактическую ширину изображения
let currentIndex = 0;

function updateSlider() {
  const sliderOffset = -((currentIndex - 1) * imageWidth);
  sliderContent.style.transform = `translateX(${sliderOffset}px)`;

  images.forEach((image, index) => {
    const offset = Math.abs(currentIndex - index);
    const scaleFactor = Math.pow(0.8, offset);

    image.style.transform = `scale(${scaleFactor})`;

    if (offset === 0) {
      image.style.opacity = 1;
      image.classList.add('middle');
    } else {
      image.style.opacity = 0.6;
      image.classList.remove('middle');
    }
  });
}

prevButton.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  updateSlider();
});

nextButton.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % images.length;
  updateSlider();
});

updateSlider();
