//URLs
const API_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://greencart-api.onrender.com"
const WEB_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:5500/frontend" : "https://greencart-bsrg.onrender.com"

const loader = document.getElementById("loader");

const userName = document.getElementById("user-name");//Main name
const userDp = document.getElementById("user-dp");//Main profile pic
const footerName = document.getElementById("footer-name");//footer name
const footerEmail = document.getElementById("footer-email");//footer email
const mainTextName = document.getElementById("main-text").getElementsByTagName("h2")[0];//Welcome back {{name}}
const totaleExchange = document.getElementById("total-exchange");
const totalRecycle = document.getElementById("total-recycle");
const totalEarnings = document.getElementById("total-earnings");

const logoutButton = document.getElementById("logout");

//const cta = document.getElementsByClassName("cta");
//const ref = document.getElementById("ref");
//console.log(cta);

//USER CREDENTIALS
const user = JSON.parse(localStorage.getItem("greencart"));

//Init Page
document.addEventListener("DOMContentLoaded", async () => {
    const user = JSON.parse(localStorage.getItem("greencart"));
    if (user) {
        let data = await UserDetail(user);
        console.log(data)
        if (data["first_name"]) {
            //cta[0].style.display = "None";
            setupPage(data);

        }
    }
});

function setupPage(data) {
    userName.innerHTML = `${data["first_name"]} ${data["last_name"]}`;
    userDp.innerHTML = "";
    footerName.innerHTML = `${data["first_name"]} ${data["last_name"]}`;
    footerEmail.innerHTML = data["email"];
    mainTextName.innerHTML = `Welcome Back, ${data["first_name"]}`;
    totaleExchange.innerHTML = "0";
    totalRecycle.innerHTML = "0";
    totalEarnings.innerHTML = "$0";
    //ref.innerText = `Welcome, ${data["first_name"]}`;
}

async function UserDetail(user) {
    const endpoint = `${API_URL}/api/v1/auth/user-detail/`;

    //Display Loader
    loader.classList.toggle("active");
    //console.log(user["access_token"]);
    var jsonData = {}
    await axios
        .get(endpoint, {
            headers: {
                Authorization: `Bearer ${user["access_token"]}`,
            },
        })
        .then((response) => {
            //Hide Loader
            loader.classList.toggle("active");
            if (response.status == 200)
                return response.data;
        })
        .then((data) => {
            console.log(data);
            jsonData = data;
        })
        .catch((error) => {
            //Hide Loader
            loader.classList.toggle("active");
            //cta[0].style.display = "block";
            console.error("Fetch error: ", error);
        });
    return jsonData;
}

logoutButton.addEventListener("click",
    async function () {
        const endpoint = `${API_URL}/api/v1/auth/logout/`;
        const redirect = `${WEB_URL}/home/index.html`;

        //console.log(user["refresh_token"]);
        var jsonData = { "refresh_token": user["refresh_token"] };
        //console.log(jsonData)
        //Display Loader
        loader.classList.toggle("active");
        await axios
            .post(endpoint, JSON.stringify(jsonData), {
                headers: {
                    Authorization: `Bearer ${user["access_token"]}`,
                    "Content-Type": "application/json",
                },
            })
            .then((response) => {
                //Hide Loader
                loader.classList.toggle("active");
                if (response.status == 200) return response.data;
            })
            .then((data) => {
                localStorage.removeItem("greencart");
                window.location.replace(redirect);
                console.log(data);
            })
            .catch((error) => {
                //Hide Loader
                loader.classList.toggle("active");
                //cta[0].style.display = "block";
                console.error("Fetch error: ", error);
            });
        return jsonData;
    }
)