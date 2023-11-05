function DeleteSearchParam(paramid) {

    const confirmation = confirm('Are you sure you want to delete this entry?');
    if (confirmation) {

        fetch('/delete/' + paramid, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {

                window.location.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}