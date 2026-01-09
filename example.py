import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation, get_page_href, redirect_to
import json

st.write(f"User agent is _{streamlit_js_eval(js_expressions='window.navigator.userAgent', want_output = True, key = 'UA')}_")

st.write(f"Screen width is _{streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}_")

st.write(f"Browser language is _{streamlit_js_eval(js_expressions='window.navigator.language', want_output = True, key = 'LANG')}_")

st.write(f"Page location is _{ streamlit_js_eval(js_expressions='window.location.origin', want_output = True, key = 'LOC')}_")

# Copying to clipboard only works with a HTTP connection

copy_to_clipboard("Text to be copied!", "Copy something to clipboard (only on HTTPS)", "Successfully copied" , component_key = "CLPBRD")

# Share something using the sharing API
create_share_link(dict({'title': 'streamlit-js-eval', 'url': 'https://github.com/aghasemi/streamlit_js_eval', 'text': "A description"}), "Share a URL (only on mobile devices)", 'Successfully shared', component_key = 'shdemo')

if st.checkbox("Check my location"):
    loc = get_geolocation()
    if loc:
        if 'error' in loc:
            # Handle geolocation errors
            error_code = loc['error']['code']
            error_msg = loc['error']['message']
            if error_code == 1:
                st.error(f"❌ Location permission denied: {error_msg}")
            else:
                st.warning(f"⚠️ Geolocation error (code {error_code}): {error_msg}")
        else:
            # Success - show coordinates
            st.success("✅ Location retrieved successfully!")
            st.write(f"Your coordinates are {loc}")
    else:
        st.info("Waiting for location data...")
    
if True:
    x = streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH',  want_output = True,)                
    st.write(f"Width is {x}")
    
st.write(f"Full page location is _{get_page_href()}_")

if st.button("Add get parameter streamlitUrl=test"):
    st.query_params['streamlitUrl'] = 'test'
    st.rerun()

if st.button("Try redirect to example.com"):
    redirect_to("https://example.com")