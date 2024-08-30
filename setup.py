from setuptools import setup, find_packages

setup(
    name="mapIt",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mapit=package.mapit:main',  # Hiermee kun je het script aanroepen met 'mijn_script' in de terminal
        ],
    },
    author="Frits Schapendonk",
    author_email="info@fritsschapendonk.nl",
    description="Met deze package kun je een locatie plotten op google maps door deze als argument mee te geven",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/fschapendonk/mapit",  # Optioneel, de URL naar je project
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',  # Geef hier de minimale Python versie op
    install_requires=[
        "pyperclip",
    ],
)
