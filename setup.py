from setuptools import setup

setup(
    name='vault',
    version='0.1.0',
    description='Secret management System over vault',
    author='Admin',
    packages=['vault'],
    install_requires=[
        'pika>=1.2.0',
        'PyJWT>=2.3.0',
        # Note: 'logging', 'json', 'os', and 'http.server' are part of the Python standard library and do not need to be listed as dependencies.
    ],
)
