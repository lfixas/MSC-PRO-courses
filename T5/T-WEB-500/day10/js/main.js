document.addEventListener("DOMContentLoaded", function () {
    const nameForm = document.getElementById("nameForm");
    const nameInput = document.getElementById("nameInput");
    const submitBtn = document.getElementById("submitBtn");

    submitBtn.addEventListener("click", function () {
        const name = nameInput.value;

        // Make an AJAX GET request to task01.php
        fetch(`task01.php?name=${name}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then((data) => {
                // Display a success notification
                alert(`Received name from server: ${data.name}`);
            })
            .catch((error) => {
                // Display an error notification
                alert("An error occurred: " + error.message);
            });
    });
});
