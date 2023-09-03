document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form_calc');
    const calcButton = document.getElementById('calc_button');
    const tariffDescriptions = {
        'column_price.posilka_dver_dver': 'Посылка дверь-дверь',
        'column_price.posilka_sklad_dver': 'Посылка склад-дверь',
        'column_price.posilka_sklad_sklad': 'Посылка склад-склад',
        'column_price.eco_posilka_skald_dver': 'Экономичная посылка склад-дверь',
        'column_price.eco_posilka_skald_sklad': 'Экономичная посылка склад-склад',
        'column_price.express_dver_dver': 'Экспресс дверь-дверь',
        'column_price.express_sklad_dver': 'Экспресс склад-дверь',
        'column_price.express_sklad_sklad': 'Экспресс склад-склад',
        'column_price.mag_express_skald_dver': 'Магистральный экспресс склад-дверь',
        'column_price.medj_doc_dver_dver': 'Международный экспресс документы дверь-дверь',
        'column_price.medj_gruz_dver_dver': 'Международный экспресс грузы дверь-дверь'
    };
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
        const successIcon = document.createElement('span');
        successIcon.textContent = 'ПОСЧИТАНО ✓';
        calcButton.textContent = '';
        calcButton.appendChild(successIcon);
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
        fetch('https://cdek21vek.ru/cdek_calc', {
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

                for (const elementClass in tariffDescriptions) {
                    const spanElement = document.querySelector('.' + elementClass);

                    if (spanElement) {
                        const tariff = result.tariff_codes.find(tariff => tariff.tariff_name === tariffDescriptions[elementClass]);

                        if (tariff) {
                            const deliverySum = tariff.delivery_sum;
                            spanElement.style.color = '#222222';
                            spanElement.textContent = `${deliverySum}₽`;
                        } else {
                            spanElement.textContent = '✖';
                            spanElement.style.color = 'red';
                        }
                    }
                }
            })
            .catch(error => {
                console.error('Ошибка при отправке запроса:', error);
            });
    });
});
