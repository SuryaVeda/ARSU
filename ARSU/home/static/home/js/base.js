$(document).ready(function(){
  $('.next').click(function () {
      let CurrentSlide = $('.active');
      let NextSlide = CurrentSlide.next();
      CurrentSlide.fadeOut(300).removeClass('active');
      NextSlide.fadeIn(300).addClass('active');
      if (NextSlide.length == 0) {
        $('.slide').first().fadeIn(300).addClass('active');
      }
    });
    $('.prev').click(function () {
      let CurrentSlide = $('.active');
      let PrevSlide = CurrentSlide.prev();
      CurrentSlide.fadeOut(300).removeClass('active');
      PrevSlide.fadeIn(300).addClass('active');
      if (PrevSlide.length == 0) {
        $('.slide').last().fadeIn(300).addClass('active');
      }
    });
});
