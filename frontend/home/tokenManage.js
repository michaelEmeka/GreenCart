// Store tokens
function storeTokens(accessToken, refreshToken) {
    localStorage.setItem('accessToken', accessToken);
    localStorage.setItem('refreshToken', refreshToken);
    scheduleTokenRefresh(accessToken); // Schedule refresh for new token
}

// Function to parse token expiration
function getTokenExpiry(token) {
    const payload = JSON.parse(atob(token.split('.')[1]));
    return payload.exp * 1000; // Convert to milliseconds
}

// Function to refresh access token using refresh token
function refreshAccessToken(refreshToken) {
    fetch('your-api-endpoint-to-refresh-token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: refreshToken }),
    })
    .then(response => response.json())
    .then(data => {
        storeTokens(data.accessToken, data.refreshToken);
    })
    .catch(err => console.error('Error refreshing token', err));
}

// Schedule token refresh before it expires
function scheduleTokenRefresh(accessToken) {
    const expiry = getTokenExpiry(accessToken);
    console.log(expiry)
    const timeToRefresh = expiry - Date.now() - 60000; // Refresh 1 minute before expiry

    if (timeToRefresh > 0) {
        setTimeout(() => {
            const refreshToken = localStorage.getItem('refreshToken');
            refreshAccessToken(refreshToken);
        }, timeToRefresh);
    }
}

// Run token refresh check on page load
(function() {
    const accessToken = localStorage.getItem('accessToken');
    if (accessToken) {
        scheduleTokenRefresh(accessToken); // Schedule refresh if token exists
    }
})();
