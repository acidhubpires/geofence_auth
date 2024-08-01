// Inicialize o mapa com Leaflet
var map = L.map('map').setView([0, 0], 2); // Centro no lat: 0, lon: 0 com zoom 2

// Adicione os tiles do OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var marker;

// Função para obter a localização do usuário
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocalização não é suportada por este navegador.");
    }
}

// Mostrar a posição no mapa
function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    // Atualizar vista do mapa e marcador
    map.setView([lat, lon], 15); // Nível de zoom 15 para uma visão mais próxima

    if (marker) {
        marker.setLatLng([lat, lon]);
    } else {
        marker = L.marker([lat, lon]).addTo(map)
            .bindPopup("Você está aqui!").openPopup();
    }

    // Capturar nome de usuário e coordenadas para hashing
    var username = document.getElementById('username').value;
    if (username) {
        var data = {
            latitude: lat,
            longitude: lon,
            username: username
        };
        
        // Gerar hash SHA256
        var hash = CryptoJS.SHA256(username + lat + lon).toString();

        // Salvar coordenadas em um arquivo JSON
        saveDataAsJSON(data, hash);
    } else {
        alert("Por favor, insira seu nome.");
    }
}

// Salvar dados em arquivo JSON
function saveDataAsJSON(data, hash) {
    // Converter dados para JSON
    var jsonData = JSON.stringify(data);

    // Criar um objeto Blob a partir dos dados JSON
    var blob = new Blob([jsonData], { type: "application/json" });

    // Criar uma URL para o Blob
    var url = URL.createObjectURL(blob);

    // Criar um elemento de link temporário
    var a = document.createElement("a");
    a.href = url;
    a.download = hash + ".json"; // Use o hash como nome do arquivo
    document.body.appendChild(a);

    // Clique programaticamente no link para acionar o download
    a.click();

    // Limpar
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Tratar erros
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
