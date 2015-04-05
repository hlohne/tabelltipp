$(function() {
  var hoverEnabled;
  $( "#sortable" ).sortable({
    placeholder: "ui-state-highlight"
  });
  $( "#sortable" ).disableSelection();

  $("#blimed").click( function(event) {
    var ordning = $("#sortable").sortable("toArray").join('_');
    var ligaid 
    var url 
    ligaid= $(this).attr("data-ligaid");
    url= $(this).attr("data-redirecturl");
    $.get('/blimediligaform/', {ligaid:ligaid, ordning:ordning});
      alert("Du er nå blitt medlem!");
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
    $(".table-row").click(function() {
        var lagid = $(this).attr("data-lagid");
        var tabelltippid = $(this).attr("data-tabelltippid");
        $.get('/testmetode/', {lagid:lagid, tabelltippid: tabelltippid}, function(data) {
            var svar = jQuery.parseJSON( data );
            alert("Laget er på " + svar.plass + t" plass og har " + svar.poeng + " poeng. Dette gir " + svar.minuspoeng + " minuspoeng ");
            });
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

