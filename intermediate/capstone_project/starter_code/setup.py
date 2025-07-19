from setuptools import setup, find_packages

setup(
    name="weather-analyzer",
    version="1.0.0",
    description="A comprehensive weather data analysis application",
    author="Python Learning Path Student",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "flake8>=4.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "weather-analyzer=weather_analyzer.main:main",
        ],
    },
    python_requires=">=3.8",
)