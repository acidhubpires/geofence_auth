import streamlit as st

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário
st.markdown(
    """
    <script>
    function getLocation() {
        console.log("getLocation called");
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
            console.log("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        console.log("showPosition called");
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        console.log("Latitude: " + lat);
        console.log("Longitude: " + lon);
        document.getElementById("latitude").innerHTML = lat;
        document.getElementById("longitude").innerHTML = lon;
    }

    function showError(error) {
        console.log("showError called");
        switch(error.code) {
            case error.PERMISSION_DENIED:
                document.getElementById("demo").innerHTML = "User denied the request for Geolocation.";
                console.log("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                document.getElementById("demo").innerHTML = "Location information is unavailable.";
                console.log("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                document.getElementById("demo").innerHTML = "The request to get user location timed out.";
                console.log("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                document.getElementById("demo").innerHTML = "An unknown error occurred.";
                console.log("An unknown error occurred.");
                break;
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        getLocation();
    });
    </script>

    <button onclick="getLocation()">Obter Coordenadas</button>
    <p>Latitude: <span id="latitude"></span></p>
    <p>Longitude: <span id="longitude"></span></p>
    <p id="demo"></p>
    """,
    unsafe_allow_html=True,
)

# Informação adicional para os usuários de desktop
st.info("Se você estiver no desktop, habilite a identificação de coordenadas no seu navegador.")
