import * as functions from "./modules/functions.js";

functions.isWebp();

import '../js/modules/menu/stickyMenu.js'

import Swiper from 'swiper';
import { Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.index-reviews__slider', {
  modules: [Navigation, Pagination],
  slidesPerView: 4.5,
  spaceBetween: 30,
});
const swiper_news = new Swiper('.index-news__slider', {
  modules: [Navigation, Pagination],
  slidesPerView: 3,
  spaceBetween: 30,
});