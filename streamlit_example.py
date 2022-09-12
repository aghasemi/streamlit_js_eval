import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.write(f"User agent is {streamlit_js_eval(js_expressions='window.navigator.userAgent', want_output = True, key = 'UA')}")

st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}")

st.write(f"Browser language is {streamlit_js_eval(js_expressions=' window.navigator.language', want_output = True, key = 'LANG')}")

