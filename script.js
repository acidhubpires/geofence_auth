// Initialize the map
var map = L.map('map').setView([0, 0], 2); // Center at lat: 0, lon: 0 with zoom 2

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var marker;

// Function to get the user's location
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocalização não é suportada por este navegador.");
    }
}

// Show the position on the map
function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    // Update map view and marker
    map.setView([lat, lon], 15); // Zoom level 15 for a closer view

    if (marker) {
        marker.setLatLng([lat, lon]);
    } else {
        marker = L.marker([lat, lon]).addTo(map)
            .bindPopup("Você está aqui!").openPopup();
    }

    // Capture username and coordinates for hashing
    var username = document.getElementById('username').value;
    if (username) {
        var data = {
            latitude: lat,
            longitude: lon,
            username: username
        };
        
        // Generate SHA256 hash
        var hash = CryptoJS.SHA256(username + lat + lon).toString();

        // Save coordinates to a JSON file
        saveDataAsJSON(data, hash);
    } else {
        alert("Por favor, insira seu nome.");
    }
}

// Save data to JSON file
function saveDataAsJSON(data, hash) {
    // Convert data to JSON
    var jsonData = JSON.stringify(data);

    // Create a Blob object from the JSON data
    var blob = new Blob([jsonData], { type: "application/json" });

    // Create a URL for the Blob
    var url = URL.createObjectURL(blob);

    // Create a temporary link element
    var a = document.createElement("a");
    a.href = url;
    a.download = hash + ".json"; // Use the hash as the filename
    document.body.appendChild(a);

    // Programmatically click the link to trigger the download
    a.click();

    // Clean up
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Handle errors
function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("Usuário negou o pedido de Geolocalização.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Informação de localização está indisponível.");
            break;
        case error.TIMEOUT:
            alert("A solicitação para obter localização do usuário expirou.");
            break;
        case error.UNKNOWN_ERROR:
            alert("Ocorreu um erro desconhecido.");
            break;
    }
}
