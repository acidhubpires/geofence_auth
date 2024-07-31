import streamlit as st

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário
st.markdown(
    """
    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        document.getElementById("latitude").innerHTML = position.coords.latitude;
        document.getElementById("longitude").innerHTML = position.coords.longitude;
    }

    function showError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                document.getElementById("demo").innerHTML = "User denied the request for Geolocation.";
                break;
            case error.POSITION_UNAVAILABLE:
                document.getElementById("demo").innerHTML = "Location information is unavailable.";
                break;
            case error.TIMEOUT:
                document.getElementById("demo").innerHTML = "The request to get user location timed out.";
                break;
            case error.UNKNOWN_ERROR:
                document.getElementById("demo").innerHTML = "An unknown error occurred.";
                break;
        }
    }
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
