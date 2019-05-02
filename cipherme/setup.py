import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cipherme",
    version="0.1.4",
    author="Kelyn Paul Njeri",
    author_email="kelynpaul.devtopia@gmail.com",
    description="Cipherme is a package that enables you to have fun with the common ciphers such as the Affine Cipher and Caesar Cipher.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KelynPNjeri/Encrypto.git",
    packages=['cipherme', 'cipherme.utils'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
