$(document).ready(function() {
$(".wrapper").click(function() {
  $(".question").css("display", "none");
  $(".images").css("display", "none");
  $(".wrapper").css("display", "none");
  $(".answer").css("display", "block");
});


$(".left").click(function() {
  $(".question").css("display", "block");
  $(".images").css("display", "block");
  $(".wrapper").css("display", "block");
  $(".answer").css("display", "none");
});

$(".right").click(function() {
  $(".question").css("display", "block");
  $(".images").css("display", "block");
  $(".wrapper").css("display", "block");
  $(".answer").css("display", "none");
});

});
