from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Environment :: Console",
    "Programming Language :: Python",
]

setup(name='pycapse',
      version='0.1.0',
      description='PyCapse emulates the CMB angular power spectrum, as provided by CLASS',
      url='https://github.com/CosmologicalEmulators/PyCapse',
      author="Marco Bonici",
      license='MIT',
      packages=['pycapse'],
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
      install_requires=[
        'juliacall'
      ],
      zip_safe=False)
