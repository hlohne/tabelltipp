$(function() {
  var hoverEnabled;
  $( "#sortable" ).sortable({
    placeholder: "ui-state-highlight"
  });
  $( "#sortable" ).disableSelection();

  $("#knapp").click( function(event) {
    var lagid
    lagid = $(this).attr("data-lagid");
    var ordning = $("#sortable").sortable("toArray").join('_');
    $.get('/tipp/tipp/', {ord_id:ordning});
    $(location).attr('href', "/tipp/");
  });

  $("#blimed").click( function(event) {
    var ordning = $("#sortable").sortable("toArray").join('_');
    var ligaid 
    var url 
    ligaid= $(this).attr("data-ligaid");
    url= $(this).attr("data-redirecturl");
    $.get('/tipp/blimediligaform/', {ligaid:ligaid, ordning:ordning});
    $(location).attr('href', url);
  });



  jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
      window.document.location = $(this).data("href");
  });
});
  jQuery(document).ready(function($) {
    $(".clickable-row").hover(function() {
        $(this).addClass('info');
      },
      function() {
        $(this).removeClass('info');
      });
  });
  jQuery(document).ready(function($) {
    $(".table-row").hover(function() {
        $(this).addClass('info');
      },
      function() {
        $(this).removeClass('info');
      });
  });
  jQuery(document).ready(function($) {
    $(".tabell").hover(function() {
        $(this).addClass('info');
      },
      function() {
        $(this).removeClass('info');
      });
  });
  
});

