# from distutils.core import setup
from setuptools import setup, find_packages

setup(
        name='iostatToCharts',
        version='0.1',
        packages=find_packages(),
        url='http://github.com/jagjag/iostattocharts',
        license='GPL',
        author='JJmomark',
        author_email='kyukou@163.com',
        description='use iostat data to draw charts'
)
