import setuptools
import pathlib

setuptools.setup(
    name="streamlit_js_eval",
    version="0.0.2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["streamlit==1.12.0"],
)