from setuptools import setup, find_packages

setup(
    name="Ytt_dlp",
    version="1.2.0",  # Versi diperbarui sesuai dengan perubahan yang dilakukan
    description="GUI untuk yt-dlp dengan fitur manajemen unduhan",
    author="Myunikon",
    author_email="myunikon@example.com",
    packages=find_packages(),
    install_requires=[
        "kivy>=2.0.0",
        "yt-dlp>=2023.3.4",
        "requests>=2.25.1",
        "pillow>=8.0.0",
        "appdirs>=1.4.4",  # Untuk lokasi file konfigurasi standar
        "aiohttp>=3.8.1",   # Untuk operasi jaringan asinkron
    ],
    entry_points={
        "console_scripts": [
            "ytt-dlp=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)