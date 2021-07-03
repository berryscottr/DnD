import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roll-dnd-berryscottr",
    version="0.0.1",
    author="Scott Berry",
    author_email="berryscottr@gmail.com",
    description="Roll for DnD as Artificer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/berryscottr/DnD",
    project_urls={
        "Bug Tracker": "https://github.com/berryscottr/DnD/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
