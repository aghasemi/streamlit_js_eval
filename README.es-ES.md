

# Streamlit-JS-Eval

[![PyPI version](https://badge.fury.io/py/streamlit_js_eval.svg?service=github)](https://badge.fury.io/py/streamlit_js_eval) [![Downloads](https://static.pepy.tech/badge/streamlit-js-eval?service=github)](https://static.pepy.tech/badge/streamlit-js-eval)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://share.streamlit.io/streamlit/corp/main](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/))


SJE es un componente personalizado de Streamlit, diseñado para evaluar expresiones arbitrarias de JavaScript y devolver el resultado. Puede resultar útil para realizar ciertas funcionalidades que son _simples_ en JavaScript, pero que no están disponibles o son difíciles de implementar en Streamlit. Los ejemplos incluyen la gestión de cookies, escritura en el portapapeles, obtención del ancho del dispositivo (por ejemplo, para verificar si estamos en un dispositivo móvil), obtención del idioma del navegador, compartir algo a través de la función de compartir de Android, conocer el agente de usuario, etc. Consulta la [documentación de MDN](https://developer.mozilla.org/en-US/docs/Web/API) para obtener más información sobre las API web. 

- _Versión 0.1.7 - Marzo de 2024_: Se propuso una solución alternativa para el problema #2.


## Instalación

```python
pip3 install streamlit_js_eval
```

## Ejemplo

```python
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")
```
`key` es una cadena arbitraria pero única, requerida por la API de componentes de Streamlit para cada llamada a `streamlit_js_eval`.

### Funcionalidades comunes de JavaScript

Algunas funcionalidades más comunes ya están implementadas como funciones de Python. Los ejemplos incluyen:

```python
# Returns user's location after asking for permission
location = get_geolocation()

# Check if location permission was denied
if location and 'error' in location:
    if location['error']['code'] == 1:
        st.error("Location permission denied")
    else:
        st.warning(f"Geolocation error: {location['error']['message']}")
elif location:
    st.write(f"Latitude: {location['coords']['latitude']}")
    st.write(f"Longitude: {location['coords']['longitude']}")

# The URL parts of the page
location_json = get_page_location()
```

Consulta `streamlit_js_eval/__init__.py` para ver más funciones. Revisa una demostración en `example.py` o [mírala en vivo](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/).

### Manejo de errores de geolocalización

La función `get_geolocation()` ahora devuelve información de error cuando el usuario niega el permiso o cuando falla la geolocalización. El objeto devuelto tendrá una clave `error` con los campos `code` y `message`:

```python
location = get_geolocation()

if location and 'error' in location:
    error_code = location['error']['code']
    error_msg = location['error']['message']
    
    # Error codes:
    # 0: Browser doesn't support geolocation
    # 1: Permission denied by user
    # 2: Position unavailable
    # 3: Timeout
    
    if error_code == 1:
        st.error("User denied location permission")
        # Disable location-related buttons, etc.
    else:
        st.warning(f"Geolocation error: {error_msg}")
elif location:
    # Success - location contains coords and timestamp
    st.write(f"Lat: {location['coords']['latitude']}, Lon: {location['coords']['longitude']}")
```

## Limitaciones conocidas

- Parece que SJE tiene problemas con `st.button` cuando se llama desde dentro de una rama en Streamlit (por ejemplo, en un bucle, un bloque `if-else`, ...). Desde la versión 0.1.7, puedes usar el `bootstrapButton` personalizado como solución alternativa en tales situaciones.
