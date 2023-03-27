window.onload = function () {
    var dropdown = document.getElementById("template_list").onchange();
};

function populateDropdowns() {
    var dropdown = document.getElementById('template_list');
    if (dropdown.value === 'Site') {
        Site_template_target_url();
        Site_template_utm_source();
    }
}

function fillSelect(dropdown, data) {
    // Clear the dropdown list
    dropdown.innerHTML = "";
    // Add options to the dropdown list
    for (var i = 0; i < data.length; i++) {
        var option = document.createElement("option");
        option.value = data[i].value;
        option.text = data[i].text;
        dropdown.add(option);
    }
}

var mainTargetURL = [{
        "value": "https://givinschool.org/pto",
        "text": "https://givinschool.org/pto"
    }
];

function Site_template_target_url() {
    var dropdown = document.getElementById('template_target_url');
    fillSelect(dropdown, mainTargetURL)
}

function Site_template_utm_source() {
    var data = [{
            "value": "givinschool_org",
            "text": "givinschool_org"
        }
    ];
    var dropdown = document.getElementById('template_utm_source');
    fillSelect(dropdown, data)
}
