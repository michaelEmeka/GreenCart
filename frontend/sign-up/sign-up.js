//IMPORTs
import { API_URL, WEB_URL } from "../base.js";

//Variables Initialization(DOM)
const signupForm = document.getElementById("sign-upForm");
const otpForm = document.getElementById("otp-Form");
const navButton = document.getElementsByClassName("form-nav");

//Variables Initialization(Local)
var email = "";

//Signup-Form handler
signupForm.addEventListener("submit", async (event) => {
    const endpoint = `${API_URL}api/v1/auth/signup/`;
    event.preventDefault();
    const formData = new FormData(signupForm);
    const data = Object.fromEntries(formData.entries());
    email = data.email;
    console.log(data);
    //API POST REQUEST
    await axios
        .post(endpoint, JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => {
            if (response.status != 201) {
                console.log(`Error: ${response.status}`);
                throw new Error("Request failed");
            }
            navButton[1].click();
            return response.data;
        })
        .then((data) => {
            console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
});

otpForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const endpoint = `${API_URL}api/v1/auth/verify-user/`;
    const redirect = WEB_URL;
    
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
            //redirect to home window.href.location = redirect
        })
        .catch((error) => {
            console.error("Fetch error:", error);
        });
});
