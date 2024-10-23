
//URLS
const API_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://greencart-api.onrender.com"
const WEB_URL = window.location.hostname === "localhost" ? "http://127.0.0.1:5500" : "https://greencart-bsrg.onrender.com"
//console.log(API_URL)

//Variables Initialization(DOM)
const loader = document.getElementById("loader");
const signupForm = document.getElementById("sign-upForm");
const otpForm = document.getElementById("otp-Form");
const navButton = document.getElementsByClassName("form-nav");

//Variables Initialization(Local)
var userEmail = "";

//SIGNUP-Form handler
signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const endpoint = `${API_URL}/api/v1/auth/signup/`;
    const formData = new FormData(signupForm);
    const data = Object.fromEntries(formData.entries());
    userEmail = data.email;

    //Display Loader
    loader.classList.toggle("active");

    //API POST REQUEST
    try {
        const response = await axios.post(endpoint, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
        });

        console.log(response.status);

        if (response.status === 201) {
            //Hide Loader
            loader.classList.toggle("active");
            navButton[1].click();
            console.log("Success:", response.data);
        }
    } catch (error) {
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            if (error.response.status === 409) {
                //Hide Loader
                loader.classList.toggle("active");
                console.log("Error: User already exists.");
                navButton[1].click();
            } else {
                //Hide Loader
                loader.classList.toggle("active");
                console.error(
                    `Error: ${error.response.status}: ${error.response.data}`
                );
            }
        } else if (error.request) {
            // The request was made but no response was received
            //Hide Loader
            loader.classList.toggle("active");
            console.error("No response received:", error.request);
        } else {
            // Something happened in setting up the request that triggered an Error
            //Hide Loader
            loader.classList.toggle("active");
            console.error("Error setting up request:", error.message);
        }
    }
});

//OTP-Form handler
otpForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const endpoint = `${API_URL}/api/v1/auth/verify-user/`;
    const redirect = `${WEB_URL}/log-in/log-in.html`;

    const formData = new FormData(otpForm);
    const data = Object.fromEntries(formData.entries());
    console.log(data); //API POST REQUEST

    //Display Loader
    loader.classList.toggle("active");

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
            window.location.replace(redirect);
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
});

//Resend-OTP handler
document
    .getElementById("ResendOTP")
    .addEventListener("click", async function ResendOTP() {
        const endpoint = `${API_URL}/api/v1/auth/resend-otp/`;
        console.log(endpoint);
        console.log(userEmail);
        if (!userEmail) {
            console.log(userEmail);
            console.error("No email in memory");
            return;
        }

        //Display Loader
        loader.classList.toggle("active");

        await axios
            .post(endpoint, JSON.stringify({ email: userEmail }), {
                headers: {
                    "Content-Type": "application/json",
                },
                timeout: 300000
            })
            .then((response) => {
                //Hide Loader
                loader.classList.toggle("active");
                if (response.status != 200) {
                    throw new Error("Request Failed");
                }
                return response.data;
            })
            .then((data) => {
                console.log("Success: ", data);
            })
            .catch((e) => {
                console.error("Error: ", e);
            });
    });
