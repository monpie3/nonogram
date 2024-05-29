let isMouseDown = false;
let isFilled;
let currentButton;

container.addEventListener('mousedown', function (event) {
    const cell = event.target;
    const classes = Array.from(cell.classList);

    if (event.target.tagName === 'TD' && classes.some(c => c.startsWith('main_'))) {
        isMouseDown = true;
        currentButton = event.button;
        toggleCell(cell, event.button);
        isFilled = (cell.style.backgroundColor === 'black' || cell.textContent === 'X');
        event.preventDefault(); // prevent text selection
    }
});

container.addEventListener('mouseover', function (event) {
    if (isMouseDown) {
        const cell = event.target;
        const classes = Array.from(cell.classList);
        if (event.target.tagName === 'TD' && classes.some(c => c.startsWith('main_'))) {
            toggleCell(cell, currentButton, isFilled);
        }
    }
});

document.addEventListener('mouseup', function () {
    isMouseDown = false;
    currentButton = null;
});


function toggleCell(cell, button, isFilled = null) {
    if (button === 0) { // left click
        if (isFilled === null) {
            if (cell.textContent === 'X') {
                cell.textContent = '';
            }
            // fill the cell with black color if it is empty
            if (cell.style.backgroundColor === 'black') {
                cell.style.backgroundColor = '';
            } else {
                cell.style.backgroundColor = 'black';
            }
        } else {
            if (isFilled) {
                cell.style.backgroundColor = 'black';
                cell.textContent = '';
            } else {
                cell.style.backgroundColor = '';
            }
        }
    } else if (button === 2) { // right click
        if (isFilled === null) {
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
        } else {
            if (isFilled) {
                cell.textContent = 'X';
                cell.style.backgroundColor = '';
            } else {
                cell.textContent = '';
            }
        }
    }
}

// prevent context menu from showing on right click
container.addEventListener('contextmenu', function (event) {
    event.preventDefault();
});
