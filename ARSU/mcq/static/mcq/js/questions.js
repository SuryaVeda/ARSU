$(document).ready(function() {
$(".wrapper").click(function() {
  $(".question").css("display", "none");
  $(".images").css("display", "none");
  $(".wrapper").css("display", "none");
  $(".answer").css("display", "block");
});


$(".carousel-control-next").click(function() {
  $(".question").css("display", "block");
  $(".images").css("display", "block");
  $(".wrapper").css("display", "block");
  $(".answer").css("display", "none");
});

$(".carousel-control-prev").click(function() {
  $(".question").css("display", "block");
  $(".images").css("display", "block");
  $(".wrapper").css("display", "block");
  $(".answer").css("display", "none");
});

});
