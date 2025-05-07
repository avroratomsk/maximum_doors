import * as functions from "./modules/functions.js";

functions.isWebp();

import '../js/modules/menu/stickyMenu.js';
import '../js/modules/map.js';
import '../js/modules/switchImage.js';
import '../js/modules/popup/popup.js';
import '../js/modules/searchCatalog.js';
import '../js/modules/menu/mobileMenu.js';

import Swiper from 'swiper';
import {Navigation, Pagination, FreeMode, EffectFade, Autoplay} from 'swiper/modules';


const swiper_reviews = new Swiper('.index-reviews__slider', {
  modules: [Navigation, Pagination, FreeMode],
  freeMode: true,

  breakpoints: {
    320: {
      slidesPerView: 1.1,
      spaceBetween: 20,

    },
    536: {
      slidesPerView: 2,
      spaceBetween: 20
    },
    1200: {
      slidesPerView: 3,
      spaceBetween: 30
    },
    1500: {
      slidesPerView: 4.5,
      spaceBetween: 30
    }
  }
});

const swiper_news = new Swiper('.index-news__slider', {
  modules: [Navigation, Pagination],
  slidesPerView: 3,
  spaceBetween: 30,

  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 20
    },
    536: {
      slidesPerView: 2,
      spaceBetween: 20
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 30
    },
    1200: {
      slidesPerView: 3,
      spaceBetween: 30
    }
  }
});

const slider_full = new Swiper('.slider-full', {
  modules: [Navigation, Pagination, EffectFade, Autoplay],
  slidesPerView: 1,
  spaceBetween: 0,
  effect: "slide",
  loop: true,

  pagination: {
    el: '.slider-full__pagination',
  },

  autoplay: {
    delay: 10000,
  },
});

const swiper_work = new Swiper('.index-work__slider', {
  modules: [Navigation, Pagination],
  slidesPerView: 3,
  spaceBetween: 30,
});


// Создание правильной ссылка номера телефона
const regNum = document.querySelectorAll("a[href^=\"tel:\"]");

if (regNum) {
  regNum.forEach(num => {
    let number = formatPhoneNumber(num.href);
    num.href = `tel:${number}`;
  });
}

function formatPhoneNumber(phoneNumber) {

  // Убираем все лишние символы (скобки, пробелы, тире)
  let cleanedNumber = phoneNumber.replace("tel:", "").replace(/[\s\-\(\)]/g, "");

  // Если номер уже начинается на +7, ничего не делаем
  if (cleanedNumber.startsWith("+7")) {
    return cleanedNumber;
  }

  // Если номер начинается на 8, заменяем на +7
  if (cleanedNumber.startsWith("8")) {
    return "+7" + cleanedNumber.slice(1);
  }

  // В остальных случаях добавляем +7 к началу
  return "+7" + cleanedNumber;
}