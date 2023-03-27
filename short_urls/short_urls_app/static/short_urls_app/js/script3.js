window.onload = function() {
  var dropdown = document.getElementById("template_list").onchange();
};

function populateDropdowns() {
  var dropdown = document.getElementById('template_list');
  if (dropdown.value === 'Site') {
    Site_fillTemplate_TargetURL();
  }
}

function Site_fillTemplate_TargetURL() {
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