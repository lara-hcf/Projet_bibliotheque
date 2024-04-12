function deleteRow(rowId) {
    /*var rowElement = document.getElementById(rowId);
    var id = rowElement.cells[0].textContent; // Récupère l'ID à partir de la première colonne
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
    });*/
    document.getElementById(rowId).remove();
    console.log("Suppression livre ID="+rowId);
    window.location.href= "/delete/"+rowId;
}