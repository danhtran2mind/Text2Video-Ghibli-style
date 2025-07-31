document.addEventListener('DOMContentLoaded', () => {
    // Add loading animation to generate button
    const generateBtn = document.querySelector('.generate-btn');
    if (generateBtn) {
        generateBtn.addEventListener('click', () => {
            generateBtn.textContent = 'Generating...';
            generateBtn.disabled = true;
            generateBtn.style.opacity = '0.7';
            
            // Reset button after 2 seconds (simulating async operation)
            setTimeout(() => {
                generateBtn.textContent = 'Generate Video';
                generateBtn.disabled = false;
                generateBtn.style.opacity = '1';
            }, 2000);
        });
    }

    // Add input validation feedback
    const inputs = document.querySelectorAll('input[type="text"]');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            if (input.value.trim() === '') {
                input.style.borderColor = '#e53e3e';
            } else {
                input.style.borderColor = '#4c51bf';
            }
        });
    });

    // Add subtle animation to sliders
    const sliders = document.querySelectorAll('input[type="range"]');
    sliders.forEach(slider => {
        slider.addEventListener('input', () => {
            slider.style.transform = 'scale(1.02)';
            setTimeout(() => {
                slider.style.transform = 'scale(1)';
            }, 200);
        });
    });

    // Auto-resize textarea
    const textarea = document.querySelector('textarea');
    if (textarea) {
        textarea.addEventListener('input', () => {
            textarea.style.height = 'auto';
            textarea.style.height = `${textarea.scrollHeight}px`;
        });
    }
});