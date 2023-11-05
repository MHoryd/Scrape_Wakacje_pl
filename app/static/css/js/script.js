function ActivateScript() {
    fetch('/trigget_script',{
        method: 'POST',
    })
    .then(response => {
        if (response.ok){
            window.location.reload();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

}