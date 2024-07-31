import streamlit as st
import folium
from geopy.distance import geodesic

st.title("Autenticação Baseada em Geolocalização")

# Função JavaScript para obter coordenadas do usuário
st.markdown(
    """
    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        document.getElementById("latitude").value = position.coords.latitude;
        document.getElementById("longitude").value = position.coords.longitude;
        document.getElementById("geoForm").submit();
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

latitude = st.query_params.get("latitude", [None])[0]
longitude = st.query_params.get("longitude", [None])[0]

if latitude and longitude:
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")

    # Definir o centro da geofence e o raio em metros
    geofence_center = (40.748817, -73.985428)  # Exemplo: Coordenadas da Times Square, NYC
    geofence_radius = 500  # 500 metros

    user_location = (float(latitude), float(longitude))

    # Função para verificar se o usuário está dentro da geofence
    def is_within_geofence(user_location, geofence_center, geofence_radius):
        distance = geodesic(user_location, geofence_center).meters
        return distance <= geofence_radius

    if is_within_geofence(user_location, geofence_center, geofence_radius):
        st.success("Você está dentro da geofence.")
    else:
        st.error("Você está fora da geofence.")

    # Criar o mapa centrado na geofence
    m = folium.Map(location=geofence_center, zoom_start=15)

    # Adicionar a geofence (círculo)
