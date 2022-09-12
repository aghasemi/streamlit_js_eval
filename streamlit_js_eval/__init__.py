import streamlit.components.v1 as components
import json, os

absolute_path = os.path.dirname(os.path.abspath(__file__))
frontend_path = os.path.join(absolute_path, "streamlit_js_eval")

streamlit_js_eval = components.declare_component(
    "streamlit_js_eval",
    path=frontend_path
)

def set_cookie(name, value, duration_days, component_key):
    js_ex = f'setCookie(\'{name}\', \'{value}\', {duration_days})'
    return streamlit_js_eval(js_expressions=js_ex, key = component_key )

def get_cookie(name, component_key):
    return streamlit_js_eval(js_expressions=f'getCookie(\'{name}\')', key = component_key)

def copy_to_clipboard(copiedText, linkText, successText, component_key):
    js_text = ''' 
    setFrameHeight(100);
    document.getElementsByTagName("body")[0].innerHTML += `<a href="#%s" id="cbc">%s</a>`;
    
    document.getElementById("cbc").addEventListener("click", function() {
        console.log('Copying')
        const copiedText = `%s`
        copyToClipboard(copiedText, () => document.getElementById("cbc").innerHTML = '%s' );
        
      })
    '''%(str(87264), linkText, copiedText, successText)
    return streamlit_js_eval(js_expressions=js_text, want_output = True, key = component_key)


def get_geolocation(linkText, component_key):
    js_text = 'getLocation()' 
    return streamlit_js_eval(js_expressions=js_text, want_output = True, key = component_key)
