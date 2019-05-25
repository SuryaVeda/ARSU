$(document).ready(function(){
  $(".sche").slice(2).hide();
  $(".resu").slice(2).hide();
  $(".atte").slice(2).hide();
  $(".naca").slice(2).hide();
  $(".camp").slice(2).hide();
  $(".ebook").slice(2).hide();
  $(".lecture").slice(2).hide();
  $(".paper").slice(2).hide();

  $("#loadMore1").click(function (e) {
    $(".sche").slice(2).show();
    e.preventDefault();
    $("#loadMore1").hide();
  });
  $("#loadMore2").click(function (e) {
    $(".resu").slice(2).show();
    e.preventDefault();
    $("#loadMore2").hide();
  });
  $("#loadMore3").click(function (e) {
    $(".atte").slice(2).show();
    e.preventDefault();
    $("#loadMore3").hide();
  });
  $("#loadMore4").click(function (e) {
    $(".naca").slice(2).show();
    e.preventDefault();
    $("#loadMore4").hide();
  });
  $("#loadMore5").click(function (e) {
    $(".camp").slice(2).show();
    e.preventDefault();
    $("#loadMore5").hide();
  });
  $("#loadMore6").click(function (e) {
    $(".ebook").slice(1).show();
    e.preventDefault();
    $("#loadMore6").hide();
  });
  $("#loadMore7").click(function (e) {
    $(".paper").slice(2).show();
    e.preventDefault();
    $("#loadMore7").hide();
  });
  $("#loadMore8").click(function (e) {
    $(".lecture").slice(2).show();
    e.preventDefault();
    $("#loadMore8").hide();
  });

});
