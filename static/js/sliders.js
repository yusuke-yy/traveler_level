var mySwiper = new Swiper ('.swiper-container', {
    
    loop: true,
    speed: 600,
    slidesPerView: 4,
    spaceBetween: 10,
    setWrapperSize: true,
    direction: 'horizontal',
    effect: 'slide',
 
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
