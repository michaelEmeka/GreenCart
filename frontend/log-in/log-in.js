//IMPORTs
import { API_URL, WEB_URL } from "../base.js";

//Variables Initialization(DOM)
const loginForm = document.getElementById("log-inForm");

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const endpoint = `${API_URL}/api/v1/auth/login/`;
    const redirect = `${WEB_URL}/frontend/home/index.html`;

    const formData = new FormData(loginForm);
    const data = Object.fromEntries(formData.entries());
    //console.log(data); //API POST REQUEST
    await axios
        .post(endpoint, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {
            if (response.status != 200) {
                console.log(`Error: ${response.status}`);
                throw new Error("Request failed");
            }
            return response.data;
        })
        .then((data) => {
            console.log("Success:", data);
            localStorage.setItem("greencart", JSON.stringify(data));
            window.location.replace(redirect);
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
});