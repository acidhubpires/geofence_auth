import streamlit as st
import folium
from geopy.distance import geodesic

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário com logs de depuração
st.markdown(
    """
    <script>
    function getLocation() {
        console.log("getLocation called");
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        console.log("showPosition called");
        document.getElementById("latitude").value = position.coords.latitude;
        document.getElementById("longitude").value = position.coords.longitude;
        document.getElementById("geoForm").submit();
    }

    function showError(error) {
        console.log("showError called");
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
    <form id="geoForm">
        <input type="hidden" id="latitude" name="latitude">
        <input type="hidden" id="longitude" name="longitude">
    </form>
    <p id="demo"></p>
    """,
    unsafe_allow_html=True,
)

# Obter parâmetros de consulta
query_params = st.experimental_get_query_params()
latitude = query_params.get("latitude", [None])[0]
longitude = query_params.get("longitude", [None])[0]

# Verificar se as coordenadas foram capturadas
if latitude and longitude:
    st.write(f"Coordenadas capturadas:")
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")

    user_location = (float(latitude), float(longitude))

    # Criar o mapa centrado na localização do usuário
    m = folium.Map(location=user_location, zoom_start=15)

    # Adicionar um círculo com raio de 100 metros ao redor da localização do usuário
    folium.Circle(
        radius=100,
        location=user_location,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

    # Adicionar a posição do usuário ao mapa com um marcador
    folium.Marker(location=user_location, popup=f"Você está aqui: {latitude}, {longitude}").add_to(m)

    # Exibir o mapa no Streamlit
    st.markdown(m._repr_html_(), unsafe_allow_html=True)
else:
    st.warning("Coordenadas não capturadas. Clique no botão 'Obter Coordenadas' para tentar novamente.")
