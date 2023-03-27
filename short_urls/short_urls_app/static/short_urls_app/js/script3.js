function populateDropdowns() {
  var dropdown = document.getElementById('template_list');
  if (dropdown.value === 'Site') {
    Site_fillTemplateURL2();
  }
}

function Site_fillTemplateURL() {
  var data = [
    {
      "id": "https://givinschool.org/pto",
      "name": "https://givinschool.org/pto"
    }
  ];
    $.each(data, function(i, option) {
      $('#template_target_url').append($('<option/>').attr("value", option.id).text(option.name));
    });
}

function Site_fillTemplateURL2() {
  var data = [
    {
      "value": "https://givinschool.org/pto",
      "text": "https://givinschool.org/pto"
    }
  ];
  // Clear the dropdown list
  var dropdown = document.getElementById('template_target_url');
  dropdown.innerHTML = "";
  // Add options to the dropdown list
  for (var i = 0; i < data.length; i++) {
    var option = document.createElement("option");
    option.value = data[i].value;
    option.text = data[i].text;
    dropdown.add(option);
  }
}