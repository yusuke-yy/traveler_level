var mySwiper = new Swiper ('.swiper-container', {
    init: false,

    loop: true,
    speed: 600,
    slidesPerView: 1,
    spaceBetween: 10,
    setWrapperSize: false,
    direction: 'horizontal',
    effect: 'fade',

    autoplay: {
      delay: 3000,
      stopOnLast: false,
      disableOnInteraction: true
    },

    breakpoints: {
        980: {
          slidesPerView: 3,
          spaceBetween: 30
        },
        640: {
          slidesPerView: 2,
          spaceBetween: 20
        }
    },

    pagination: {
      el: '.swiper-pagination',
    },
 
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    scrollbar: {
      el: '.swiper-scrollbar',
    }
});

mySwiper.init();

mySwiper.on('init', function () {
    console.log('initialized');
  });
