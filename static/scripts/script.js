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
});

