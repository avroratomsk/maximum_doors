import("./modules/dorpdownMenu.js");
import("./modules/generateSlug.js");

/**
 * Переключение вкладок на страницах продуктов, категорий
 */
const tabButton = document.querySelectorAll('[data-name]');
const pageEditButton = document.querySelectorAll('.page-content');

tabButton?.forEach(btn => {
  btn.addEventListener('click', function (e) {
    tabButton.forEach(item => item.classList.remove('_active'));
    pageEditButton.forEach(item => item.classList.remove('_show'));


    let bodyTabBody = document.getElementById(this.dataset.name);

    btn.classList.add('_active');
    bodyTabBody.classList.add('_show');
  })
})


// const ctx = document.getElementById('myChart');

// const no_register = document.getElementById('no_register');
// if(no_register){

// }

var ctx = document.getElementById('myChart');
if (ctx) {
  ctx.getContext('2d');
  var salesChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
      datasets: [
        {
          label: 'Зарегистрировались и купили',
          data: [12, 19, 3, 5, 2, 3, 8, 12, 13, 14, 5, 9, 11, 6, 8, 10, 15, 18, 16, 10, 12, 17, 19, 21, 20, 18, 16, 14, 12, 10],
          borderColor: 'rgba(75, 192, 192, 1)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderWidth: 1
        },
        {
          label: 'Не зарегистрировались',
          data: [10, 15, 6, 8, 5, 4, 7, 9, 11, 12, 6, 8, 10, 9, 7, 5, 12, 14, 13, 9, 10, 13, 15, 16, 14, 13, 11, 9, 8, 7],
          borderColor: 'rgba(153, 102, 255, 1)',
          backgroundColor: 'rgba(153, 102, 255, 0.2)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        x: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Дни месяца'
          }
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Количество продаж'
          }
        }
      }
    }
  });
}


/**
 * Подсчет и отображение количества символов в meta-полях
 */

const numberSymbols = {
  'title': 50,
  'description': 140
}

const metaFields = document.querySelectorAll('.meta_field');

metaFields?.forEach(item => {
  let parentItem = item.closest('.form__group').querySelector('.meta-lenght');
  if (item.value <= 0) {
    parentItem.innerText = 0;
  } else {
    parentItem.innerText = item.value.length;
  }

  item.addEventListener('input', (e) => {
    checkLengthSymbol(numberSymbols, e.currentTarget);
  })
})


function checkLengthSymbol(lengthSymbol, item) {
  item.previousElementSibling.innerText = item.value.length;
  if (item.value.length > numberSymbols.title) {
    item.previousElementSibling.classList.add("_red");
  }

  if (item.value.length > numberSymbols.description) {
    item.previousElementSibling.classList.add("_red");
  }
};


document.addEventListener('click', function (event) {
  if (event.target.classList.contains('form__plus')) {
    const blockPasteChar = document.getElementById('paste-char');
    let char_name_id = document.getElementById('id_char_name').innerHTML;
    console.log(char_name_id);
    blockPasteChar.innerHTML += `
    <div class="form__group-char">
      <label for="{{ product_char_form.char_name.id_for_label }}" class="form__controls-label">
        Название характеристики <span>:</span>
      </label>
      <select name="text_name" class="form__controls" placeholder="Название характеристики" id="id_name">${char_name_id}</select>
    
    <label for="id_char_value">Значение:</label>
    <input type="text" name="char_value" class="form__controls" placeholder="Значение" required="" id="id_char_value">
    <div class="form__remove">
      Удалить
    </div>
    </div>`
  }
});


