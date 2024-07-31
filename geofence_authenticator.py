import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário
get_location_script = """
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    var coords = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
    };
    document.dispatchEvent(new CustomEvent("returnCoords", {detail: coords}));
}

function showError(error) {
    var message;
    switch(error.code) {
        case error.PERMISSION_DENIED:
            message = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            message = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            message = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            message = "An unknown error occurred.";
            break;
    }
    document.getElementById("demo").innerHTML = message;
    document.dispatchEvent(new CustomEvent("returnCoords", {detail: null}));
}

getLocation();
"""

# Executa o script e obtém as coordenadas
coords = streamlit_js_eval(get_location_script, "Obtendo coordenadas", event_name="returnCoords")

# Verificar se as coordenadas foram capturadas
if coords:
    st.write(f"Coordenadas capturadas:")
    st.write(f"Latitude: {coords['latitude']}")
    st.write(f"Longitude: {coords['longitude']}")
else:
    st.warning("Coordenadas não capturadas. Clique no botão 'Obter Coordenadas' para tentar novamente.")

# Informação adicional para os usuários de desktop
st.info("Se você estiver no desktop, habilite a identificação de coordenadas no seu navegador.")
