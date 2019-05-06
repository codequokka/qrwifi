from setuptools import setup, find_packages

setup(
    name="qrwifi",
    version="0.1",
    author_email="codequokka@gmail.com",
    packages=['qrwifi'],
    package_data={},
    install_requires=[
        'pyqrcode',
        'pypng',
        'SolidPython',
        'numpy',
        'Flask',
        'click'
    ],
    entry_points={
        'console_scripts': ['qrwifi = qrwifi.cli:start']
    }
)
