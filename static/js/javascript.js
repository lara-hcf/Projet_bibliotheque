function deleteRow(rowId) {
    document.getElementById(rowId).remove();
    console.log("Suppression livre ID="+rowId);
    window.location.href= "/delete/"+rowId;
}