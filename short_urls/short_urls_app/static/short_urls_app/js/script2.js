$(function() {
  $.getJSON('http://127.0.0.1:8000/static/short_urls_app/data/data.json', function(data) {
    $.each(data, function(i, option) {
      $('#sel').append($('<option/>').attr("value", option.id).text(option.name));
    });
  });
});