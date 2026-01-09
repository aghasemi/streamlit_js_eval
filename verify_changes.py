"""
Simple verification script to check that get_geolocation can be imported
and that the JavaScript code structure is correct.
"""
import sys
import os
from pathlib import Path

# Get the repository root directory
repo_root = Path(__file__).parent.absolute()

# Add the package to the path
sys.path.insert(0, str(repo_root))

# Test import
try:
    from streamlit_js_eval import get_geolocation
    print("✅ Successfully imported get_geolocation")
except Exception as e:
    print(f"❌ Failed to import get_geolocation: {e}")
    sys.exit(1)

# Check that the JavaScript file has been updated
index_html_path = repo_root / 'streamlit_js_eval' / 'index.html'
with open(index_html_path, 'r') as f:
    content = f.read()
    
# Verify the error handling code is present
checks = [
    ('error callback parameter', '(error) =>'),
    ('error object in response', "error: {"),
    ('error code', "code: error.code"),
    ('error message', "message: error.message"),
]

all_passed = True
for check_name, check_str in checks:
    if check_str in content:
        print(f"✅ Found {check_name}")
    else:
        print(f"❌ Missing {check_name}")
        all_passed = False

if all_passed:
    print("\n✅ All verification checks passed!")
    print("\nThe getLocation() function now:")
    print("  - Handles permission denial errors")
    print("  - Returns an error object with code and message")
    print("  - Error code 1 = PERMISSION_DENIED")
    print("  - Error code 2 = POSITION_UNAVAILABLE")
    print("  - Error code 3 = TIMEOUT")
    print("  - Error code 0 = Browser doesn't support geolocation")
else:
    print("\n❌ Some verification checks failed")
    sys.exit(1)
