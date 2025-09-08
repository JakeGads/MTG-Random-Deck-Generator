from setuptools import setup, find_packages

setup(
    name="mtg-random-deck",
    version="1.0.0",
    description="A tool to scrape and randomly select MTG Commander decks from Moxfield",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mtg-random-deck=main:main",
        ],
    },
)
