from setuptools import setup

setup(
      name='pp-tracker',
      version='0.2',
      description='Program do pobrania informacji na temat przesyłki z serwerów poczty polskiej',
      url='https://github.com/mateuszpiela/tracker/pp-tracker',
      author='Mateusz Pieła',
      author_email='mpielagit@gitter.hub.pl',
      license='GPLv3',
      scripts = ['pp-tracker.py'],
      py_modules = ['pp-tracker'],
      install_requires=['zeep'],
      zip_safe=False,
      classifiers=[
		'Programming Language :: Python :: 3.0',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Environment :: Console',
		'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
		'Topic :: Internet',
		'Natural Language :: Polish',
      ],
	 keywords='zeep pp-tracker tracker',
)
