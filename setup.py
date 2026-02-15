from setuptools import setup, find_packages
from pathlib import Path

directory = Path(__file__).resolve().parent
requirements = []

with open(directory / "requirements.txt") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="kronos",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
)

