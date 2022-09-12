import setuptools
import pathlib

setuptools.setup(
    name="streamlit_js_eval",
    version="0.0.3",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["streamlit==1.12.0"],
    keywords=['Python', 'Streamlit', 'JavaScript'],
    python_requires=">=3.6",
)