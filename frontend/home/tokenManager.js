//URLs
const API_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:8000" : "https://greencart-api.onrender.com"
const WEB_URL = window.location.hostname === "127.0.0.1" ? "http://127.0.0.1:5500/frontend" : "https://greencart-q85r.onrender.com"


window.addEventListener("load", () => {
    const accessToken = JSON.parse(localStorage.getItem('greencart'))["access_token"];
    console.log(accessToken);
    if (accessToken) {
        scheduleTokenRefresh(accessToken); // Schedule refresh if token exists
    }
})

// Store tokens
function storeTokens(accessToken) {
    var tokens = JSON.parse(localStorage.getItem("greencart"))
    tokens["access_token"] = accessToken
    localStorage.setItem("greencart", JSON.stringify(tokens));
    scheduleTokenRefresh(accessToken); // Schedule refresh for new token
}

// Function to parse token expiration
function getTokenExpiry(token) {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.exp * 1000; // Convert to milliseconds
}

// Function to refresh access token using refresh token
function refreshAccessToken(refreshToken) {
    axios.post(`${API_URL}/api/v1/auth/token/refresh/`, JSON.stringify({ "refresh": refreshToken }),
        {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            storeTokens(data.access);
        })
        .catch(err => console.error('Error refreshing token', err));
}

// Schedule token refresh before it expires
function scheduleTokenRefresh(accessToken) {
    const expiry = getTokenExpiry(accessToken);
    console.log(expiry)
    const timeToRefresh = expiry - Date.now() - 60000; // Refresh 1 minute before expiry
    console.log(timeToRefresh)

    if (timeToRefresh > 0) {
        setTimeout(() => {
            const refreshToken = JSON.parse(localStorage.getItem('greencart'))["refresh_token"];
            refreshAccessToken(refreshToken);
        }, timeToRefresh);
    }
}

// Run token refresh check on page load
(function () {

})();

console.log("token manager loaded")