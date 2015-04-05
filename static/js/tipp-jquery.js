$(function() {
  var hoverEnabled;
  jQuery(document).ready(function($) {
  $( "#sortable" ).sortable({
    placeholder: "ui-state-highlight"
  });
  $( "#sortable" ).disableSelection();
  });

  jQuery(document).ready(function($) {
  $("#blimed").click( function(event) {
    var ordning = $("#sortable").sortable("toArray").join('_');
    var ligaid 
    var url 
    ligaid= $(this).attr("data-ligaid");
    url= $(this).attr("data-redirecturl");
    $.get('/blimediligaform/', {ligaid:ligaid, ordning:ordning});
      alert("Takk!");
    $(location).attr('href', url);
  });
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
        $.get('/regnpoeng/', {lagid:lagid, tabelltippid: tabelltippid}, function(data) {
            var svar = jQuery.parseJSON( data );
            var message = svar.lag + " er på " + svar.plass + ". plass og har " + svar.poeng + " poeng. Dette gir " + svar.minuspoeng + " minuspoeng.";
            $("#freeow").freeow("Poengberegning",message, { classes: ["smokey", "notice"]});
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

