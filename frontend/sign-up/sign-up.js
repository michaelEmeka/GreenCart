import { BASE_URL } from "../base.js";

var form = document.getElementById("sign-upForm");
//const axios = require("axios/dist/browser/axios.cjs");

axios.get("https://jsonplaceholder.typicode.com/posts/1")
    .then((response) => {
        console.log(response.data);
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
        document.getElementById(
            "response"
        ).textContent = `Error: ${error.message}`;
    });


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
            console.log("response.ok")
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
