from setuptools import setup

setup(
    # mandatory
    name="continuous-pull",
    # mandatory
    version="0.1",
    # mandatory
    author="Eric J. Ma",
    description=("A lightweight CLI tool to continuously pull a Git repository."),
    license="MIT",
    keywords="git, utilities, command line tools, git pull, continuous pull",
    url="https://github.com/ericmjl/continuous-pull",
    packages=["cp"],
    install_requires=["click==7.0"],
    entry_points={"console_scripts": ["cpull = cp.__init__:main"]},
)
