import setuptools
    
setuptools.setup(
    name="oimbot",
    version="10.5.2",
    author="Aeroz",
    description="Lobby bot.",
    url="https://www.youtube.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'crayons',
        'BenBotAsync',
        'fortnitepy==3.6.7',
        'FortniteAPIAsync',
        'sanic==21.6.2',
        'colorama',
        'aiohttp'
    ],
    dependency_links = [
        "git+git://github.com/XBXBot/fortnitepy.git"
    ],
    include_package_data=True,
)
