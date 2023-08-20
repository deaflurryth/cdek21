document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form_calc');
    const calcButton = document.getElementById('calc_button');

    calcButton.addEventListener('click', function () {
        const cityFrom = document.getElementById('calc_input1').value;
        const cityTo = document.getElementById('calc_input2').value;
        const weight = parseFloat(document.getElementById('calc_input3').value);
        const length = parseFloat(document.getElementById('calc_input4').value);
        const width = parseFloat(document.getElementById('calc_input5').value);
        const height = parseFloat(document.getElementById('calc_input6').value);
        console.log("отправитьель ", cityFrom)
        console.log("получатель ", cityTo)
        console.log("вес ", weight)
        console.log("длина ", length)
        console.log("ширина ", width)
        console.log("высота ", height)
        const data = {
            sender_city_code: cityFrom,
            receiver_city_code: cityTo,
            weight: weight,
            length: length,
            width: width,
            height: height
        };
        const formData = {
            sender_city_code: cityFrom,
            receiver_city_code: cityTo,
        };

        const goodsData = {
            weight: weight,
            length: length,
            width: width,
            height: height,
        };

        formData.goods = goodsData;
        console.log(data)
        fetch('http://127.0.0.1:8000/cdek_calc', {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(formData),
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
    });
});
