# Copyright (c) Capital Fund Management
# Distributed under the terms of the MIT License.

import os.path

from setuptools import setup, find_packages

README = """

NoteTab allows you to **explore in [Tableau](https://www.tableau.com/) data which is generated
dynamically by a Jupyter Notebook**. You can thus create Tableau data sources in a very flexible way
using all the power of Python. This is achieved by having Tableau access data through a
**web server created by NoteTab**.

NoteTab is built on **solid foundations**: Tableau's
[Web Data Connector](https://tableau.github.io/webdataconnector/) and the
[Jupyter Kernel Gateway](https://github.com/jupyter/kernel_gateway).


Features:

* **Expose multiple pandas dataframes** to Tableau from a Jupyter notebook
* Access **several notebooks** from Tableau through a **single entry point** (web server)
* Manage your notebooks using a **web interface**
* **Secure access** to your data

The full documentation is available on the
[project's home page](https://github.com/CFMTech/notetab).
"""

# This call to setup() does all the work
setup(
    name="notetab",
    version="0.9.2",
    description="Connect Tableau to your Jupyter Notebook",
    # long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/CFMTech/NoteTab",
    author="Brian Tribondeau",
    author_email="brian.tribondeau@cfm.fr",
    license="MIT",
    keywords="notetab jupyter notebook wdc tableau",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    install_requires=["jupyter_kernel_gateway"],
    project_urls={
        "Bug Tracker": "https://github.com/btribonde/notetab/issues",
        "Documentation": "https://github.com/btribonde/notetab",
        "Source Code": "https://github.com/btribonde/notetab"
    },
    entry_points={
        "console_scripts": [
            "notetab=notetab.__main__:main",
        ]
    },
)
