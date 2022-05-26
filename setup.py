from setuptools import setup, find_packages

setup(
    name='gpx_tools',
    version='0.0.0.1',
    author='UCSD Engineers for Exploration',
    author_email='e4e@eng.ucsd.edu',
    entry_points={
        'console_scripts': [
            # 'ExamplePythonConsoleScript = examplePackage.exampleModule:exampleEntryPoint'
            "gpxcut = gpx_tools.gpxcut:main"
        ]
    },
    packages=find_packages(),
    install_requires=[
        "gpxpy",
    ]
)