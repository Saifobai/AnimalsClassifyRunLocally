function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = document.getElementById("preview");
            img.src = e.target.result;
            img.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
}

function sendImage(modelType) {
    const fileInput = document.getElementById("imageInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image!");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    fetch(`/predict/${modelType}`, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            const resultDiv = document.getElementById(
                modelType === "vgg" ? "result-vgg" : "result-team"
            );

            if (data.error) {
                resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p><strong>Prediction:</strong> <span style="color:#00FFFF">${data.prediction}</span></p>
                    <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(2)}%</p>
                    <details><summary>All Probabilities</summary><pre>${JSON.stringify(data.all_probs, null, 2)}</pre></details>
                `;
            }
        })
        .catch((err) => {
            const resultDiv = document.getElementById(
                modelType === "vgg" ? "result-vgg" : "result-team"
            );
            resultDiv.innerHTML = `<p style="color:red;">${err}</p>`;
        });
}

function clearAll() {
    document.getElementById("imageInput").value = "";
    document.getElementById("preview").src = "#";
    document.getElementById("preview").style.display = "none";

    document.getElementById("result-vgg").innerHTML =
        '<p>Click "Classify VGG16" to see result</p>';
    document.getElementById("result-team").innerHTML =
        '<p>Click "Classify Team" to see result</p>';
}
