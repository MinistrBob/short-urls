$(function() {
    var data = [
        {
        "id": "1",
        "name": "test1"},
    {
        "id": "2",
        "name": "test2"}
    ];
    $.each(data, function(i, option) {
        $('#sel').append($('<option/>').attr("value", option.id).text(option.name));
    });
})
