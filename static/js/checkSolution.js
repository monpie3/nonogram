function checkSolution(solution) {
    const mainGridTable = document.querySelector('#mainGrid');
    const gridRows = mainGridTable.querySelectorAll('#mainGrid tbody tr');

    if (solution.length !== gridRows.length) {
        console.error("Solution and grid row counts do not match.");
        return;
    }

    let isCorrect = true;

    for (let i = 0; i < gridRows.length; i++) {
        const cells = gridRows[i].querySelectorAll('td');

        if (solution[i].length !== cells.length) {
            console.error(`Solution and grid column counts do not match for row ${i}.`);
            return;
        }

        for (let j = 0; j < cells.length; j++) {
            const cell = cells[j];
            const cellValue = cell.classList.contains('bg-black') ? 0 : 1;

            if (cellValue !== solution[i][j]) {
                isCorrect = false;
            }
        }
    }

    if (isCorrect) {
        alert('Congratulations! You solved the Nonogram!');
    } else {
        alert('Some cells are incorrect. Please try again.');
    }
}
