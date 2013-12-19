import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'src'), np.get_include()]

# Define extensions
# Form is: Extension(end_module_name, [sources], include_dirs, language)
primes = Extension("tools.primes",
                   ["tools/primes.pyx"],
                   include_dirs=incdirs)

# List modules we want to build
ext_modules = [primes]

setup(name='tools',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules,
      packages=['hbspy']
      )
