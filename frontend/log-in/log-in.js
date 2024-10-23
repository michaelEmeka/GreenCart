//URLs
const API_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://greencart-api.onrender.com"
const WEB_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:5500/frontend" : "https://greencart-bsrg.onrender.com"

//Variables Initialization(DOM)
const loginForm = document.getElementById("log-inForm");
const loader = document.getElementById("loader");

console.log(WEB_URL)

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const endpoint = `${API_URL}/api/v1/auth/login/`;
    const redirect = `${WEB_URL}/home/index.html`;

    const formData = new FormData(loginForm);
    const data = Object.fromEntries(formData.entries());

    //Display Loader
    loader.classList.toggle("active");

    //console.log(data); //API POST REQUEST
    await axios
        .post(endpoint, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {
            //Hide Loader
            loader.classList.toggle("active");

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
            //Hide Loader
            loader.classList.toggle("active");
            console.error("Fetch error:", error);
        });
});