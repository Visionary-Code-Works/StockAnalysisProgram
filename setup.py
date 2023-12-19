from setuptools import setup, find_packages

setup(
    name='stock-analysis-program',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    description='A Python-based toolkit for fetching and visualizing financial data and metrics for stocks.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/visionarycodeworks/stock-analysis-program',
    author='Thaddeus Thomas',
    author_email='thaddeus.r.thomas@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "Development Status :: 4 - Beta"
    ],
    install_requires=[
        yfinance = "^0.1.63",
        matplotlib = "^3.3.4",
        pandas = "^1.2.4",
    ],
    python_requires='>=3.8',
)
