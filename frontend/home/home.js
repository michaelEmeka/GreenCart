//URLs
const API_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://greencart-api.onrender.com"
const WEB_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:5500/frontend" : "https://greencart-q85r.onrender.com"

const cta = document.getElementsByClassName("cta");
const ref = document.getElementById("ref");
//console.log(cta);

//Init Page
document.addEventListener("DOMContentLoaded", async () => {
    const user = JSON.parse(localStorage.getItem("greencart"));
    if (user) {
        let data = await UserDetail(user);
        console.log(data)
        if (data["first_name"]) {
            cta[0].style.display = "None";
            ref.innerText = `Welcome, ${data["first_name"]}`;
        }
    }
});

async function UserDetail(user) {
    const endpoint = `${API_URL}/api/v1/auth/user-detail/`;
    //console.log(user["access_token"]);
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