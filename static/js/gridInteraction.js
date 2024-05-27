container.addEventListener('mousedown', function (event) {
    const cell = event.target;
    const classes = Array.from(cell.classList);

    if (event.target.tagName === 'TD' && classes.some(c => c.startsWith('main_'))) {
        if (event.button === 0) { // left click
            // if there is already X then just reset the cell
            if (cell.textContent === 'X') {
                cell.textContent = '';
            }
            // fill the cell with black color if it is empty
            if (cell.style.backgroundColor === 'black') {
                cell.style.backgroundColor = '';
            } else {
                cell.style.backgroundColor = 'black';
            }
        } else if (event.button === 2) { // right click
            // if the cell is already black then just reset the cell
            if (cell.style.backgroundColor === 'black') {
                cell.style.backgroundColor = '';
            }
            // enter X if the cell is empty
            if (cell.textContent === 'X') {
                cell.textContent = '';
            } else {
                cell.textContent = 'X';
            }
        }
        event.preventDefault();
    }
});

// prevent context menu from showing on right click
container.addEventListener('contextmenu', function (event) {
    event.preventDefault();
});
