from distutils.core import setup, Extension
import numpy.distutils.misc_util

# Adding OpenCV to project
# ************************



# Adding sources of the project
# *****************************

SOURCES = ["../src/cloud/cloud.cpp",
           "../src/npm_ply/ply_file_in.cc",
           "../src/npm_ply/ply_file_out.cc",
           "../src/grid_subsampling/grid_subsampling.cpp",
           "wrap_subs.cpp"]

module = Extension(name="grid_subsampling",
                    sources=SOURCES,
                    extra_compile_args=['-std=c++11',
                                        '-D_GLIBCXX_USE_CXX11_ABI=0'])


setup(ext_modules=[module], include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs())








