document.addEventListener('DOMContentLoaded', () => {
  const size = 16;
  const tbody = document.getElementById('matrix-body');

  if (!tbody) {
    return;
  }

  for (let y = 0; y < size; y += 1) {
    const row = document.createElement('tr');

    for (let x = 0; x < size; x += 1) {
      const cell = document.createElement('td');
      const pixel = document.createElement('div');

      pixel.className = 'matrix-cell';
      pixel.id = `cell-${x}-${y}`;
      pixel.dataset.x = String(x);
      pixel.dataset.y = String(y);

      cell.appendChild(pixel);
      row.appendChild(cell);
    }

    tbody.appendChild(row);
  }

  const gallery = document.querySelector('.gallery-row');
  if (gallery) {
    gallery.addEventListener('click', (event) => {
      const target = event.target;
      if (!(target instanceof HTMLImageElement)) {
        return;
      }
      let imagePath = target.getAttribute('src')
      console.log(imagePath);
      renderImageToGrid(target.src);
      //send to backend
      sendImageChangeRequest(imagePath)
    });
  }


  const uploadInput = document.getElementById('upload-input');
  if (uploadInput) {
    uploadInput.addEventListener('change', (event) => {
      const file = event.target.files?.[0];
      if (!file) {
        return;
      }

      const previewUrl = URL.createObjectURL(file);
      const img = new Image();

      img.onload = () => {
        if (img.width !== img.height) {
          showNotification('Uploaded image must be square', '#ff6c5c');
          URL.revokeObjectURL(previewUrl);
          uploadInput.value = '';
          return;
        }

        showNotification('Image uploaded successfully', '#5fff65');
        renderImageToGrid(previewUrl);
      };

      img.src = previewUrl;
    });
  }

  const latestImage = document.getElementById('latest-image');
  if (latestImage?.dataset.url) {
    renderImageToGrid(latestImage.dataset.url);
  }

  const clearButton = document.getElementById('clear-button');
  if (clearButton) {
    clearButton.addEventListener('click', () => {
      clearGrid();
      clearImage()
    });
  }

  const brightnessSlider = document.getElementById('brightness-slider');
  const brightnessValue = document.getElementById('brightness-value');
  if (brightnessSlider && brightnessValue) {
    const updateBrightnessValue = () => {
      brightnessValue.textContent = brightnessSlider.value;
    };

    updateBrightnessValue();
    brightnessSlider.addEventListener('input', updateBrightnessValue);
  }
});

function clearGrid() {
  const cells = document.querySelectorAll('.matrix-cell');
  cells.forEach((cell) => {
    cell.style.backgroundColor = '';
  });
}

function sendImageChangeRequest(imgSrc){
  const payload = {image: imgSrc};

  fetch('/api/update-image', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
    })
      .then(response => {
        if (!response.ok) {
      console.error('Failed to update image on the server');
    }
  })
}

function clearImage(){
  const payload = {instruction: "clear"};

  fetch('/api/clear-image', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
    })
      .then(response => {
        if (!response.ok) {
      console.error('Failed to update image on the server');
    }
  })
}

function renderImageToGrid(imageUrl) {
  if (!imageUrl) {
    return;
  }

  const img = new Image();

  img.src = imageUrl;
  img.onload = () => {
    const width = 16;
    const height = 16;

    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;

    const ctx = canvas.getContext('2d');
    if (!ctx) {
      return;
    }

    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(img, 0, 0, width, height);
    const data = ctx.getImageData(0, 0, width, height).data;

    for (let y = 0; y < height; y += 1) {
      for (let x = 0; x < width; x += 1) {
        const i = (y * width + x) * 4;
        const r = data[i];
        const g = data[i + 1];
        const b = data[i + 2];
        const a = data[i + 3];

        const cell = document.getElementById(`cell-${x}-${y}`);
        if (cell) {
          cell.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${a / 255})`;
        }
      }
    }
  };
}

function showNotification(message, color) {
  const containerId = 'notification-container';
  let container = document.getElementById(containerId);

  if (!container) {
    container = document.createElement('div');
    container.id = containerId;
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  toast.style.background = color;

  container.appendChild(toast);

  requestAnimationFrame(() => {
    toast.classList.add('toast--visible');
  });

  setTimeout(() => {
    toast.classList.remove('toast--visible');
    setTimeout(() => {
      toast.remove();
      if (!container.hasChildNodes()) {
        container.remove();
      }
    }, 200);
  }, 2500);
}
