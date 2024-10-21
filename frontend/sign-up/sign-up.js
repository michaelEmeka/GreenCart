
//IMPORTs
import { API_URL, WEB_URL } from "../home/base.js";

//Variables Initialization(DOM)
const signupForm = document.getElementById("sign-upForm");
const otpForm = document.getElementById("otp-Form");
const navButton = document.getElementsByClassName("form-nav");

//Variables Initialization(Local)
var userEmail = "";

//SIGNUP-Form handler
signupForm.addEventListener("submit", async (event) => {
    const endpoint = `${API_URL}/api/v1/auth/signup/`;
    event.preventDefault();
    const formData = new FormData(signupForm);
    const data = Object.fromEntries(formData.entries());
    userEmail = data.email;
    console.log(data);
    //API POST REQUEST
    try {
        const response = await axios.post(endpoint, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
        });

        console.log(response.status);

        if (response.status === 201) {
            navButton[1].click();
            console.log("Success:", response.data);
        }
    } catch (error) {
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            if (error.response.status === 409) {
                console.log("Error: User already exists.");
                navButton[1].click();
            } else {
                console.error(
                    `Error: ${error.response.status}: ${error.response.data}`
                );
            }
        } else if (error.request) {
            // The request was made but no response was received
            console.error("No response received:", error.request);
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error("Error setting up request:", error.message);
        }
    }
});

//OTP-Form handler
otpForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const endpoint = `${API_URL}/api/v1/auth/verify-user/`;
    const redirect = `${WEB_URL}/frontend/log-in/log-in.html`;

    const formData = new FormData(otpForm);
    const data = Object.fromEntries(formData.entries());
    console.log(data); //API POST REQUEST
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
        console.log(userEmail);
        if (!userEmail) {
            console.log(userEmail);
            console.error("No email in memory");
            return;
        }

        await axios
            .post(endpoint, JSON.stringify({ email: userEmail }), {
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then((response) => {
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
