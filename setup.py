from setuptools import setup, find_packages

setup(
    name="myai",
    version="0.1",
    packages=find_packages(),
    author="Your Name",
    author_email="you@example.com",
    description="A tiny AI answering 'What is AI?'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://your-cloud-host-link.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
