#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

extras_require = {
    "test": [  # `test` GitHub Action jobs uses this
        "ape-arbitrum",  # Needed for Arbitrum integration
        "ape-base",  # Needed for Base networks integration
        "ape-bsc",  # For testing BSC integration
        "ape-fantom",  # For testing Fantom integration
        "ape-optimism",  # Needed for Optimism integration
        "ape-polygon",  # Needed for Polygon integration
        "ape-polygon-zkevm",  # Needed for Polygon ZkEVM integration
        "ape-infura",  # Needed for live network tests
        "ape-solidity",  # Needed for contract verification tests
        "pytest>=6.0",  # Core testing package
        "pytest-xdist",  # multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "hypothesis>=6.2.0,<7",  # Strategy-based fuzzer
        "pytest-mock",  # Test mocker
    ],
    "lint": [
        "black>=23.3.0,<24",  # auto-formatter and linter
        "mypy>=0.991,<1",  # Static type analyzer
        "types-requests>=2.28.7",  # Needed due to mypy typeshed
        "types-setuptools",  # Needed due to mypy typeshed
        "flake8>=6.0.0,<7",  # Style linter
        "isort>=5.10.1,<6",  # Import sorting linter
        "mdformat>=0.7.16",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
    ],
    "doc": [
        "Sphinx>=3.4.3,<4",  # Documentation generator
        "sphinx_rtd_theme>=0.1.9,<1",  # Readthedocs.org theme
        "towncrier>=19.2.0,<20",  # Generate release notes
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "setuptools-scm",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .'[dev]'` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="ape-etherscan",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""ape-etherscan: Etherscan Explorer Plugin for Ethereum-based networks""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ApeWorX Ltd.",
    author_email="admin@apeworx.io",
    url="https://github.com/ApeWorX/ape-etherscan",
    include_package_data=True,
    install_requires=[
        "eth-ape>=0.6.16,<0.7",
        "requests",  # Use same version as eth-ape
    ],
    python_requires=">=3.8,<4",
    extras_require=extras_require,
    py_modules=["ape_etherscan"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_etherscan": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
