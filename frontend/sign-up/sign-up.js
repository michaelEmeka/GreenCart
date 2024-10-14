import { BASE_URL } from "../base.js";

const form = document.getElementById("sign-upForm");
const navButton = document.getElementsByClassName("form-nav");
//const axios = require("axios/dist/browser/axios.cjs");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    await axios.post(`${BASE_URL}api/v1/auth/signup/`, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            }
            // Send data as JSON
        })
        .then((response) => {
            if (response.status != 201) {
                console.log(`Error: ${response.status}`);
                throw new Error("Request failed");
            }
            navButton[1].click();
            return response.data; // Parse JSON response
        })
        .then((data) => {
            console.log("Success:", data); // Handle the response data here
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
        console.log(data); // This logs the data immediately after form submission
});
