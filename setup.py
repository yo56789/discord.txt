import setuptools

with open("README.md", "r") as readme:
    long_desc = readme.read()

setuptools.setup(
    name="discord.txt",
    version="1.0.0",
    author="yo56789",
    license="MIT",
    description="Create a discord bot using a .txt file",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/yo56789/discord.txt",
    packages=["discordtxt"],
    install_requires=["discord.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.8"
)