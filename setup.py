import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="tutorial",
        description="Scrapy tutorial",
        version="0.0.1",
        author="Sujay Mansingh",
        packages=setuptools.find_packages(),
        include_package_data=True,
        url="https://github.com/sujaymansingh/scrapy-tutorial",
        install_requires=[],
        entry_points={"scrapy": ["settings = tutorial.settings"]},
    )
