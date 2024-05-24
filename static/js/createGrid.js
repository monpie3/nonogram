/*
Creates 4 tables:
one for the column clues, one for the row clues, and one for the main grid
and the last one which combines everything
*/
function createGrid(rowClues, columnClues) {
    const table = document.createElement('nonogramTable');
    table.className = 'shrink-0';
    const tbody = document.createElement('tbody');

    // Create table with column clues
    const topRow = document.createElement('tr');

    const emptyCorner = document.createElement('td');
    emptyCorner.style.background = 'rgb(240, 240, 240)';

    topRow.appendChild(emptyCorner); // Empty top-left cell

    const topRowCell = document.createElement('td');
    const topRowTable = document.createElement('table');
    const topRowTbody = document.createElement('tbody');

    const maxColumnHeight = Math.max(...columnClues.map(col => col.length));

    for (let i = 0; i < maxColumnHeight; i++) {
        const tr = document.createElement('tr');
        for (let j = 0; j < columnClues.length; j++) {
            const td = document.createElement('td');
            if (i < maxColumnHeight - columnClues[j].length) {
                // fill with empty cells if there is space before the clues
                td.className = 'col_header_empty ';
                td.innerHTML = '<div>&nbsp;</div>';
            } else {
                // fill with column clues
                td.className = `col_header_${j}_${i} `;
                td.innerHTML = `<div>${columnClues[j][i - (maxColumnHeight - columnClues[j].length)]}</div>`;
            }
            td.className += 'border border-gray-400 text-center';
            tr.appendChild(td);
        }
        topRowTbody.appendChild(tr);
    }

    topRowTable.appendChild(topRowTbody);
    topRowCell.appendChild(topRowTable);
    topRow.appendChild(topRowCell);
    tbody.appendChild(topRow);

    // Create table with row clues and table with the main grid
    const sideTableCell = document.createElement('td');
    const sideTable = document.createElement('table');
    const sideTbody = document.createElement('tbody');

    const mainGridCell = document.createElement('td');
    const mainGridTable = document.createElement('table');
    const mainGridTbody = document.createElement('tbody');

    rowClues.forEach((row, rowIndex) => {
        const sideRow = document.createElement('tr');
        const mainRow = document.createElement('tr');

        const maxRowWidth = Math.max(...rowClues.map(row => row.length));
        // header rows
        for (let i = 0; i < maxRowWidth; i++) {
            const td = document.createElement('td');
            if (i < maxRowWidth - row.length) {
                // fill with empty cells if there is space before the clues
                td.className = 'row_header_empty ';
                td.innerHTML = '<div>&nbsp;</div>';
            } else {
                // fill with row clues
                td.className = `row_header_${i}_${rowIndex} `;
                td.innerHTML = `<div>${row[i - (maxRowWidth - row.length)]}</div>`;
            }
            td.className += 'border border-gray-400 text-center';
            sideRow.appendChild(td);
        }
        sideTbody.appendChild(sideRow);

        // main grid
        for (let colIndex = 0; colIndex < columnClues.length; colIndex++) {
            const td = document.createElement('td');
            td.className = `main_${colIndex}_${rowIndex} `;
            td.innerHTML = '<div></div>';
            td.className += 'border border-gray-400 text-center';
            mainRow.appendChild(td);
        }
        mainGridTbody.appendChild(mainRow);
    });

    sideTable.appendChild(sideTbody);
    sideTableCell.appendChild(sideTable);

    mainGridTable.appendChild(mainGridTbody);
    mainGridCell.appendChild(mainGridTable);

    const combinedRow = document.createElement('tr');
    combinedRow.appendChild(sideTableCell);
    combinedRow.appendChild(mainGridCell);
    tbody.appendChild(combinedRow);

    table.appendChild(tbody);
    document.body.appendChild(table);
    return table;
}
