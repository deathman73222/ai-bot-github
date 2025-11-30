"""
Setup script for AI Bot
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-bot",
    version="1.0.0",
    author="Your Name",
    description="A hybrid AI bot with online and offline search capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "PyQt5>=5.15.0",
        "wikipedia-api>=0.5.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-bot=ai_bot.gui.main_window:main",
        ],
    },
)
