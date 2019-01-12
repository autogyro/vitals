#!/usr/bin/python3

from distutils.core import setup

setup(
    name='Vitals',
    version='1.0',
    author='Kyle Corry',
    description='Log your vitals',
    url='https://github.com/kylecorry31/vitals',
    license='MIT',
    scripts=['vitals_gui/vitals_gui'],
    packages=['vitals_gui'],
    data_files=[
        ('share/metainfo', ['data/screen_time.appdata.xml']),
    ],
)
