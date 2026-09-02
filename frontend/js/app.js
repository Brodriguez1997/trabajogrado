javascript
const fileInput = document.getElementById("fileInput");
const analyzeButton = document.getElementById("analyzeButton");

const status = document.getElementById("status");

const resultContainer = document.getElementById("resultContainer");

const result = document.getElementById("result");
const score = document.getElementById("score");
const observations = document.getElementById("observations");

analyzeButton.addEventListener("click", async () => {

    const file = fileInput.files[0];

    if (!file) {
        status.textContent = "Por favor selecciona un archivo.";
        return;
    }

    status.textContent = "Analizando documento...";

    const formData = new FormData();

    formData.append("file", file);

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Error en el servidor");
        }

        const data = await response.json();

        result.textContent = data.result;
        score.textContent = data.score;
        observations.textContent = data.observations;

        resultContainer.classList.remove("hidden");

        status.textContent = "Análisis completado.";

    } catch (error) {

        console.error(error);

        status.textContent =
            "No fue posible realizar el análisis.";

    }

});

