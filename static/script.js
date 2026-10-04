
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("wineForm");

    const resetButton =
        document.getElementById("resetButton");

    const analyzeButton =
        document.getElementById("analyzeButton");


    // ========================================================
    // DEFAULT VALUES
    // ========================================================

    const defaults = {

        fixed_acidity: "7.4",

        volatile_acidity: "0.70",

        citric_acid: "0.00",

        residual_sugar: "1.9",

        chlorides: "0.076",

        free_sulfur_dioxide: "11",

        total_sulfur_dioxide: "34",

        density: "0.9978",

        pH: "3.51",

        sulphates: "0.56",

        alcohol: "9.4"

    };


    // ========================================================
    // RESET FORM
    // ========================================================

    resetButton.addEventListener("click", function () {

        Object.keys(defaults).forEach(function (name) {

            const field =
                document.querySelector(
                    `[name="${name}"]`
                );

            if (field) {

                field.value = defaults[name];

            }

        });


        analyzeButton.innerHTML = `
            <span>◈</span>
            ANALYZE WINE SAMPLE
            <b>→</b>
        `;

        analyzeButton.disabled = false;

        analyzeButton.style.opacity = "1";

    });


    // ========================================================
    // ANALYSIS LOADING
    // ========================================================

    form.addEventListener("submit", function () {

        analyzeButton.innerHTML = `
            <span>◌</span>
            ANALYZING WINE SAMPLE...
            <b>...</b>
        `;

        analyzeButton.disabled = true;

        analyzeButton.style.opacity = "0.75";

    });

});