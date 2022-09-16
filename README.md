# Streamlit-JS-Eval

[![PyPI version](https://badge.fury.io/py/streamlit_js_eval.svg?service=github)](https://badge.fury.io/py/streamlit_js_eval) [![Downloads](https://static.pepy.tech/badge/streamlit-js-eval?service=github)](https://static.pepy.tech/badge/streamlit-js-eval)


SJE is a custom Streamlit component, built to evaluate arbitrary Javascript expressions and return the result. It can become useful in doing certain functionalities which are _simple_ things in JavaScript, but unavailable or difficult to do in Streamlit. Examples include cookie management, writing to clipboard, getting device width (e.g. to check if we are on a mobile device), getting browser language, sharing something through Android's share feature, knowing user agent, etc. See [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API) for more information about Web APIs. 

## Install

```python
pip3 install streamlit_js_eval==0.1.0
```

## Example

```python
st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}")
```
`key` is an arbitrary but unique string, required by Streamlit components API for each call to `streamlit_js_eval`.

### Common JavaScript functionalities

Some more common functionalities are already implemented as Python functions. Examples include:

```python
# Returns user's location after asking for permission when the user clicks the generated link with the given text
location = get_geolocation('Get my location')
# The URL parts of the page
location_json = get_page_location()
```

See `streamlit_js_eval/__init__.py` for more functions. Check a demo in `example.py` or [see it live](https://aghasemi-streamlit-js-eval-example-yleu91.streamlitapp.com/).
