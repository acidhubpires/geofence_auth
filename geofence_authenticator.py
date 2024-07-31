import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário
get_location_script = """
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    console.log("showPosition called");
    console.log("Latitude: " + position.coords.latitude);
    console.log("Longitude: " + position.coords.longitude);
    const coords = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
    };
    return coords;
}

function showError(error) {
    console.log("showError called");
    switch(error.code) {
        case error.PERMISSION_DENIED:
            console.log("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            console.log("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            console.log("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            console.log("An unknown error occurred.");
            break;
    }
    return null;
}

getLocation();
"""

# Executa o script e obtém as coordenadas
coords = streamlit_js_eval(get_location_script, "Obtendo coordenadas")

# Verificar se as coordenadas foram capturadas
if coords:
    st.write(f"Coordenadas capturadas:")
    st.write(f"Latitude: {coords['latitude']}")
    st.write(f"Longitude: {coords['longitude']}")
else:
    st.warning("Coordenadas não capturadas. Clique no botão 'Obter Coordenadas' para tentar novamente.")

# Informação adicional para os usuários de desktop
st.info("Se você estiver no desktop, habilite a identificação de coordenadas no seu navegador.")
