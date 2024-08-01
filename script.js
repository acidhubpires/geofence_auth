var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

var marker;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    map.setView([lat, lon], 15);
    if (marker) {
        marker.setLatLng([lat, lon]);
    } else {
        marker = L.marker([lat, lon]).addTo(map).bindPopup("Você está aqui!").openPopup();
    }
    var username = document.getElementById('username').value;
    if (username) {
        var data = { latitude: lat, longitude: lon, username: username };
        var hash = CryptoJS.SHA256(username + lat + lon).toString();
        saveDataAsJSON(data, hash);
    } else {
        alert("Por favor, insira seu nome.");
    }
}

function saveDataAsJSON(data, hash) {
    var jsonData = JSON.stringify(data);
    var blob = new Blob([jsonData], { type: "application/json" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = hash + ".json";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

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
