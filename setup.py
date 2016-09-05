from setuptools import setup
from cjkwrap import __version__ as version

setup(name='CJKwrap',
      version=version,
      description='CJKwrap is a library for wrapping and filling CJK text. Fix Python issue24665',
      author='Florent Gallaire',
      author_email='fgallaire@gmail.com',
      url='https://fgallaire.github.io/cjkwrap',
      license='GNU LGPLv3+',
      keywords='cjk wrap',
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
          "Topic :: Software Development :: Internationalization",
          "Topic :: Software Development :: Localization",
          "Topic :: Text Processing",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
      ],
      py_modules=['cjkwrap'],
      )