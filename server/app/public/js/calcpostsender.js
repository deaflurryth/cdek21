document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form_calc');
    const calcButton = document.getElementById('calc_button');

    calcButton.addEventListener('click', function () {
        const cityFrom = document.getElementById('calc_input1').value;
        const cityTo = document.getElementById('calc_input2').value;
        const weight = document.getElementById('calc_input3').value;
        const length = document.getElementById('calc_input4').value;
        const width = document.getElementById('calc_input5').value;
        const height = document.getElementById('calc_input6').value;

        const data = {
            cityFrom: cityFrom,
            cityTo: cityTo,
            weight: weight,
            length: length,
            width: width,
            height: height
        };
        fetch('http://127.0.0.1:8000/cdek_calc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            })
            .catch(error => {
                console.error('Ошибка при отправке запроса:', error);
            });
    });
});
