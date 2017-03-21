from setuptools import setup

setup(name='qcodes-device-annotator',
      version='0.1',
      use_2to3=False,

      maintainer='Jens Hedegaard Nielsen, William H.P. Nielsen',
      maintainer_email='j.h.nielsen@nbi.ku.dk',
      description='Simple Qt gui for QCoDeS to annotate device images with instrument data',
      url='https://github.com/qdev-dk/qcodes-device-annotator',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering'
      ],
      license='MIT',
      py_modules=["qcodes_device_annotator"],
      install_requires= [
          'qcodes>=0.1.3',
          'QtPy>=1.2.0',
      ],

      zip_safe=True)
