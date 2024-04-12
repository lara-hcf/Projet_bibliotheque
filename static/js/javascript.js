function deleteRow(rowId) {
    var rowElement = document.getElementById(rowId);
    var id = rowElement.cells[0].textContent; 
    fetch('/delete/' + id, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            rowElement.remove();
        } else {
            alert('Erreur lors de la suppression');
        }
    })
    .catch(error => {
        console.error('Erreur:', error);
    });
}