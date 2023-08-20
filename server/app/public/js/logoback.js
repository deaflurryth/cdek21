document.addEventListener('DOMContentLoaded', function () {
    var logo = document.getElementById('logo');

    logo.addEventListener('click', function () {
        window.location.href = 'index.html';
        window.scrollTo(0, 0);
    });
});