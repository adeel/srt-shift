from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

setup(
  name='srt-shift',
  version='0.1',
  description="For fixing out-of-sync .srt subtitle files.",
  long_description=open('README').read(),
  author='Adeel Ahmad Khan',
  author_email='adeel@soundofemptiness.com',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: Utilities',
  ],
  py_modules=['srt_shift'],
  entry_points={'console_scripts': ['srt-shift = srt_shift:main']},
  zip_safe=False,
)