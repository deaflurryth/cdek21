document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".left-content-banner").classList.add("appear");
    document.querySelector(".right-content-banner").classList.add("appear");
});

document.addEventListener("DOMContentLoaded", function () {
  const steps = document.querySelectorAll(".step");
  const line = document.querySelector(".line");
  const container = document.querySelector(".stages_wrapper");
  const stepHeight = steps[0].offsetHeight + 130; // Учтем расстояние между кружками

  const totalHeight = container.scrollHeight - window.innerHeight;
  const maxScrollPosition = totalHeight - stepHeight;

  let scrollTimeout; // Для управления задержкой

  document.addEventListener("scroll", function () {
    let scrollPosition = window.scrollY - container.offsetTop;
    scrollPosition = Math.min(Math.max(scrollPosition, 0), maxScrollPosition);

    const scrollPercentage = (scrollPosition / maxScrollPosition) * 100;
    line.style.height = scrollPercentage + "%";

    const activeStepIndex = Math.floor(scrollPosition / stepHeight);

    steps.forEach((step, index) => {
      const passed = index <= activeStepIndex;
      step.classList.toggle("active_step", passed);
      step.dataset.passed = passed; // Записываем состояние в data-атрибут
    });

    // Сбрасываем задержку, чтобы избежать мерцания
    clearTimeout(scrollTimeout);

    // Устанавливаем задержку перед снятием состояния
    scrollTimeout = setTimeout(() => {
      steps.forEach((step, index) => {
        if (step.dataset.passed === "true" && !step.classList.contains("active_step")) {
          step.dataset.passed = "false";
        }
      });
    }, 100); // Можно регулировать эту задержку
  });
});



























