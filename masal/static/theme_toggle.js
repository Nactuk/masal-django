document.addEventListener('DOMContentLoaded', function () {
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    let darkMode = false;

    themeToggleBtn.addEventListener('click', function () {
        const body = document.querySelector('body');
        darkMode = !darkMode;
        body.classList.toggle('dark-theme', darkMode);
        themeToggleBtn.classList.toggle('btn-dark', darkMode); // Butonun rengini deðiþtir
        themeToggleBtn.classList.toggle('btn-light', !darkMode); // Butonun rengini deðiþtir
    });
});

