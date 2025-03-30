from setuptools import setup, find_packages

setup(
    name='production_dashboard',
    version='0.1.0',
    description='Oil and Gas Production Analysis Dashboard',
    author='Blake Woods',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'matplotlib',
        'reportlab'
    ],
    entry_points={
        'console_scripts': [
            'run-analysis = analysis:main'
        ]
    },
    include_package_data=True,
    python_requires='>=3.8',
)
