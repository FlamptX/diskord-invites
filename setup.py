import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diskord-invites",
    version="0.1.0",
    author="Flampt",
    license="MIT",
    description="Python library for simple invites tracking.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlamptX/diskord-invites",
    project_urls={
        "Source": "https://github.com/FlamptX/diskord-invites"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=['diskord', 'asyncio'],
    keywords='discord diskord discord-invites invite tracker',
    packages=setuptools.find_packages(include=['discord-invites', 'discord-invites.*']),
    python_requires=">=3.6",
)