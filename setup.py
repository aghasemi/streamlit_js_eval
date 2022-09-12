import setuptools
import pathlib

component_name = "streamlit_js_eval"

setuptools.setup(
    name=component_name,
    version="0.0.11",
    packages=setuptools.find_packages(),
    include_package_data=True,
    url='https://github.com/aghasemi/streamlit_js_eval',
    install_requires=["streamlit==1.12.0"],
    keywords=['Python', 'Streamlit', 'JavaScript'],
    python_requires=">=3.8",
)