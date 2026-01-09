"""
Test script to demonstrate geolocation permission detection.
This script shows how to detect when a user denies location permissions.
"""
import streamlit as st
from streamlit_js_eval import get_geolocation

st.title("Geolocation Permission Detection Test")

st.write("""
This demo shows how to detect when a user denies location permissions.

When you click the button:
- If you **allow** location access, you'll see your coordinates
- If you **deny** location access, you'll see an error message
- The button will be disabled after denial
""")

# Initialize session state for tracking permission denial
if 'location_denied' not in st.session_state:
    st.session_state.location_denied = False

# Create button (disabled if location was denied)
button_disabled = st.session_state.location_denied
if st.button("Get My Location", disabled=button_disabled):
    st.session_state.location_requested = True

# Show status message if button is disabled
if st.session_state.location_denied:
    st.error("Location access was denied. Please refresh the page to try again.")

# Get location if button was clicked
if st.session_state.get('location_requested', False):
    loc = get_geolocation()
    
    if loc is not None:
        # Check if there's an error in the response
        if 'error' in loc:
            error_code = loc['error']['code']
            error_message = loc['error']['message']
            
            # Error code 1 is PERMISSION_DENIED
            if error_code == 1:
                st.session_state.location_denied = True
                st.error(f"❌ Location permission denied: {error_message}")
                st.info("The button has been disabled. Refresh the page to try again.")
            else:
                st.warning(f"⚠️ Geolocation error (code {error_code}): {error_message}")
        else:
            # Success - we have coordinates
            st.success("✅ Location access granted!")
            st.write(f"**Latitude:** {loc['coords']['latitude']}")
            st.write(f"**Longitude:** {loc['coords']['longitude']}")
            st.write(f"**Accuracy:** {loc['coords']['accuracy']} meters")
    else:
        st.warning("Waiting for location data...")
    
    # Clear the request flag
    st.session_state.location_requested = False

st.markdown("---")
st.markdown("""
### Error Codes Reference:
- **Code 0**: Browser doesn't support geolocation
- **Code 1**: Permission denied by user
- **Code 2**: Position unavailable
- **Code 3**: Timeout
""")
