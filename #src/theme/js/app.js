import * as functions from "./modules/functions.js";

functions.isWebp();

import '../js/modules/menu/stickyMenu.js';
import '../js/modules/map.js';
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
  spaceBetween: 30,
  effect: "fade",
  loop: true,

  pagination: {
    el: '.slider-full__pagination',
  },

  autoplay: {
    delay: 5000,
  },
});

const swiper_work = new Swiper('.index-work__slider', {
  modules: [Navigation, Pagination],
  slidesPerView: 3,
  spaceBetween: 30,
});