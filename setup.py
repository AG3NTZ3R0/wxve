import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wxve",
    version="0.0.1",
    author="Brandon Lacy",
    author_email="Z3R0@duck.com",
    description="A set of modules to assist in the analysis of stock market equities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AG3NTZ3R0/wxve",
    keywords="glaciology photogrammetry time-lapse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    install_requires=['glob2', 'matplotlib', 'numpy', 'opencv-python>=3', 'pillow', 'scipy'],
    python_requires='>=3',
)