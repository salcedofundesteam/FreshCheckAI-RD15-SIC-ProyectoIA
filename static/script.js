const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewImage = document.getElementById('previewImage');
const removeBtn = document.getElementById('removeBtn');
const uploadContent = document.querySelector('.upload-content');
const analyzeBtn = document.getElementById('analyzeBtn');
const resultCard = document.getElementById('resultCard');
const resultContent = document.getElementById('resultContent');
const loader = document.getElementById('loader');
const predictionText = document.getElementById('predictionText');

let currentFile = null;

// Drag & Drop
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    handleFile(file);
});

uploadArea.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFile(file);
});

function handleFile(file) {
    if (file && file.type.startsWith('image/')) {
        currentFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
            previewImage.hidden = false;
            removeBtn.hidden = false;
            uploadContent.classList.add('hidden');
            analyzeBtn.disabled = false;

            // Generate a fake prediction for immediate feedback if needed, 
            // but we'll wait for the button click
            resultCard.classList.add('hidden');
        };
        reader.readAsDataURL(file);
    }
}

removeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    currentFile = null;
    fileInput.value = '';
    previewImage.hidden = true;
    removeBtn.hidden = true;
    uploadContent.classList.remove('hidden');
    analyzeBtn.disabled = true;
    resultCard.classList.add('hidden');
});

analyzeBtn.addEventListener('click', async () => {
    if (!currentFile) return;

    // UI Updates
    resultCard.classList.remove('hidden');
    resultContent.classList.add('hidden');
    loader.classList.remove('hidden');
    analyzeBtn.disabled = true;

    const formData = new FormData();
    formData.append('file', currentFile);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            showResult(data);
        } else {
            alert('Error: ' + data.error);
            loader.classList.add('hidden');
            analyzeBtn.disabled = false;
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Ocurrió un error al analizar la imagen.');
        loader.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
});

function showResult(data) {
    loader.classList.add('hidden');
    resultContent.classList.remove('hidden');
    analyzeBtn.disabled = false;

    // Update text
    predictionText.textContent = data.class;

    // Dynamic color based on result
    if (data.class.toLowerCase().includes('podrida') || data.class.toLowerCase().includes('rotten')) {
        predictionText.style.color = '#f44336';
    } else if (data.class.toLowerCase().includes('verde') || data.class.toLowerCase().includes('unripe')) {
        predictionText.style.color = '#FF9800';
    } else {
        predictionText.style.color = '#4CAF50';
    }
}
