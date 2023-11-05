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

function ActivateScript() {
    fetch('/trigger_script', {
        method: 'POST',
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            if (data.success) {
                // Task was triggered successfully, you can handle the response as needed
                window.location.reload();
            } else {
                // Handle errors if needed
                console.error('Error:', data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}