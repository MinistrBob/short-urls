window.onload = function () {
    var dropdown = document.getElementById("template_list").onchange();
};

function populateDropdowns() {
    var dropdown = document.getElementById('template_list');
    if (dropdown.value === 'Site') {
        Site_template_target_url();
        Site_template_utm_source();
        Site_template_utm_medium();
        Site_template_utm_content();
        Site_template_utm_campaign();
        Site_template_utm_term();
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
//        dropdown.add(option);
        dropdown.appendChild(option);
        console.log("Added option %o for dropdown %o", option, dropdown);
    }
    console.log("option[0]=%o", dropdown.options[0]);
    dropdown.options[0].defaultSelected = true;
}

var mainTargetURL = [{
        "value": "https://givinschool.org/pto",
        "text": "https://givinschool.org/pto"
    },
    {
        "value": "https://givinschool3.org/pto",
        "text": "https://givinschool3.org/pto"
    }
];

function Site_template_target_url() {
    var dropdown = document.getElementById('template_target_url');
    console.log("dropdown=%o", dropdown);
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

function Site_template_utm_medium() {
    var data = [{
            "value": "event_page_GS",
            "text": "event_page_GS"
        }
    ];
    var dropdown = document.getElementById('template_utm_medium');
    fillSelect(dropdown, data)
}

function Site_template_utm_content() {
    var data = [{
            "value": "post_anons",
            "text": "post_anons"
        }
    ];
    var dropdown = document.getElementById('template_utm_content');
    fillSelect(dropdown, data)
}

function Site_template_utm_campaign() {
    var data = [{
            "value": "",
            "text": ""
        }
    ];
    var dropdown = document.getElementById('template_utm_campaign');
    fillSelect(dropdown, data)
}

function Site_template_utm_term() {
    var data = [{
            "value": "",
            "text": ""
        }
    ];
    var dropdown = document.getElementById('template_utm_term');
    fillSelect(dropdown, data)
}
