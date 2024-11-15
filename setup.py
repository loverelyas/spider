from setuptools import setup, find_packages

setup(
    name="spider_XR",
    version="1.5", 
    description="my lib is power",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/loverelyas/spider",
    author="spiderXR7",
    author_email="spiderxr7@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
