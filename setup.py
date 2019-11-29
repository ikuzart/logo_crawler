from setuptools import setup, find_packages

setup(name="logo_finder",
      version="0.0.1",
      description="Logo images crawler",
      url="https://github.com/ikuzart/logo_finder",
      packages=find_packages(),
      install_requires=["requests","beautifulsoup4"],
      python_requires='>=3.6'
      )
