import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailsender",
    version="0.1.0",
    author="Matheus Almeida",
    author_email="mat.almeida@live.com",
    description="Send mails using SMTP and a HTML template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matAlmeida/mailsender",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Topic :: Communications :: Email",
    ),
)
