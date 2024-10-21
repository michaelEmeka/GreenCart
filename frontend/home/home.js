import { API_URL, WEB_URL } from "../home/base.js";

const cta = document.getElementsByClassName("cta");
const ref = document.getElementById("ref");
//console.log(cta);
document.addEventListener("DOMContentLoaded", async () => {
    const user = JSON.parse(localStorage.getItem("greencart"));
    if (user) {
        let data = await UserDetail(user);
        console.log(data)
        cta[0].style.display = "None";
        ref.innerText = `Welcome, ${data["first_name"]}`;
    }
});

async function UserDetail(user) {
    const endpoint = `${API_URL}/api/v1/auth/user-detail/`;
    console.log(user["access_token"]);
    var jsonData = {}
    await axios
        .get(endpoint, {
            headers: {
                Authorization: `Bearer ${user["access_token"]}`,
            },
        })
        .then((response) => {
            if (response.status == 200)
                return response.data;
        })
        .then((data) => {
            console.log(data);
            jsonData = data;
        })
        .catch((error) => {
            cta[0].style.display = "block";
            console.error("Fetch error: ", error);
        });
    return jsonData;
}

async function logout() {
    const endpoint = `${API_URL}/api/v1/auth/logout/`;
    console.log(user["access_token"]);
    var jsonData = {};
    await axios
        .get(endpoint, {
            headers: {
                Authorization: `Bearer ${user["access_token"]}`,
            },
        })
        .then((response) => {
            if (response.status == 200) return response.data;
        })
        .then((data) => {
            console.log(data);
            jsonData = data;
        })
        .catch((error) => {
            cta[0].style.display = "block";
            console.error("Fetch error: ", error);
        });
    return jsonData;
}