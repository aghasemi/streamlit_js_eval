# Streamlit-JS-Eval

[![PyPI version](https://badge.fury.io/py/streamlit_js_eval.svg?service=github)](https://badge.fury.io/py/streamlit_js_eval) [![Downloads](https://static.pepy.tech/badge/streamlit-js-eval?service=github)](https://static.pepy.tech/badge/streamlit-js-eval)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://share.streamlit.io/streamlit/corp/main](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/))


SJE is a custom Streamlit component, built to evaluate arbitrary Javascript expressions and return the result. It can become useful in doing certain functionalities which are _simple_ things in JavaScript, but unavailable or difficult to do in Streamlit. Examples include cookie management, writing to clipboard, getting device width (e.g. to check if we are on a mobile device), getting browser language, sharing something through Android's share feature, knowing user agent, etc. See [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API) for more information about Web APIs. 

- _Version 0.1.7 - March 2024_: Proposed a workaround for issue #2.


## Install

```python
pip3 install streamlit_js_eval
```

## Example

```python
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', key = 'SCR')}")
```
`key` is an arbitrary but unique string, required by Streamlit components API for each call to `streamlit_js_eval`.

### Common JavaScript functionalities

Some more common functionalities are already implemented as Python functions. Examples include:

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

See `streamlit_js_eval/__init__.py` for more functions. Check a demo in `example.py` or [see it live](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/).

### Handling Geolocation Errors

The `get_geolocation()` function now returns error information when the user denies permission or when geolocation fails. The returned object will have an `error` key with `code` and `message` fields:

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

## Known Limitations

- It seems SJE has issues with `st.button` when getting called from inside a branch in Streamlit (e.g. in a loop, `if-else` block, ...). In version 0.1.7, you may use the custom `bootstrapButton` as a workaround in such situations.
