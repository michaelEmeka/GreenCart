document.getElementById("sign-upForm").addEventListener('input', function () {
    validateForm()
});

function validateForm() {
    const firstName = document.getElementById('firstname').value;

    const lastName = document.getElementById("lastname").value;

    const email = document.getElementById("emailAddress").value;

    const password = document.getElementById("password").value;

    const confirmPassword = document.getElementById("confrimPassword").value;

    const errorElement = document.getElementById("errorMessage")

    const submitBtn = document.getElementById("submitBtn")

    let isValid = true;
    
    if (!firstName || !lastName || !password || !confirmPassword) {
        isValid = false;
    }

    if (password !== confirmPassword) {
        errorElement.textContent = 'Password does not match';

        errorElement.classList.remove('success');
        errorElement.classList.add("error");
        isValid = false;
    } else {
        errorElement.textContent = 'Password match'
        errorElement.classList.remove("error");
        errorElement.classList.add("success");
    }

    if (isValid) {
        submitBtn.classList.add('enabled');
        submitBtn.disabled = false;
    } else {
        submitBtn.classList.remove("enabled");
        submitBtn.disabled = true;
    }
}
