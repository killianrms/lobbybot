import setuptools

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="oimbot",
    version="10.5.3",
    author="Aeroz",
    long_description="A Fortnite LobbyBot creation tool",
    description="Lobby_Bot_Ftn",
    url="https://bot.aerozoff.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    include_package_data=True,
)
