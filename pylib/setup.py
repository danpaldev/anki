#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import setuptools

#install_requires” should be used to specify what dependencies a project minimally needs to run. 
#When the project is installed by pip, this is the specification that is used to install its dependencies.
install_requires = [
    "beautifulsoup4",
    "requests[socks]",
    "decorator",
    "protobuf",
    'orjson; platform_machine == "x86_64"',
    'psutil; sys_platform == "win32"',
    'distro; sys_platform != "darwin" and sys_platform != "win32"',
]

#This is not my comment ---> # maturin develop hides the package from pip - https://github.com/ankitects/anki/pull/600
if not os.environ.get("SKIP_ANKI_RSPY", False):
    install_requires.append("ankirspy==2.1.31")  # automatically updated 1

    
#As mentioned above, the primary feature of setup.py is that it contains a global setup() function.
#The keyword arguments to this function are how specific details of your project are defined.
setuptools.setup(
    name="anki",
    version="2.1.31",  # automatically updated 2
    author="Ankitects Pty Ltd",
    description="Anki's library code",
    long_description="Anki's library code",
    long_description_content_type="text/markdown",
    url="https://apps.ankiweb.net",
    packages=setuptools.find_packages(".", exclude=["tests"]),
    license="License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    package_data={"anki": ["py.typed"]},
    classifiers=[],
    python_requires=">=3.7",
    install_requires=install_requires,
)
