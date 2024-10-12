require("dotenv").config();

const BASE_URL = process.env.BASE_URL
var form = document.getElementById("sign-upForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("https://example.com/api/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data), // Send data as JSON
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const responseData = await response.json();
        console.log("Success:", responseData);
    } catch (error) {
        console.error("Error:", error);
    }
    console.log(data);
});
