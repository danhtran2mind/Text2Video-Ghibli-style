document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector(".generate-btn");
    button.addEventListener("click", function() {
        button.textContent = "Generating...";
        button.disabled = true;
        setTimeout(() => {
            button.textContent = "Generate Video";
            button.disabled = false;
        }, 5000); // Simulates generation time; adjust based on actual inference
    });
});