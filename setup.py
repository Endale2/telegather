import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegather",
    version="0.1.4",
    author="Endale Shimelis",
    author_email="endale406@gmail.com",
    description="CLI tool to scrape messages from a Telegram channel into CSV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Endale2/telegather",

    # SPDX license expression (PyPI understands “MIT”)
    license="MIT",

    # <— This tells setuptools “please include exactly this LICENSE file in dist-info”
    #     and not to auto-generate a separate License-File metadata field.
    license_files=("LICENSE",),

    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "telethon>=1.28.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "telegather=telegather.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
