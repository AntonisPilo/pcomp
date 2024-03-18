from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',

]
 
setup(
  name='pcomp',
  version='1.3.2',
  description='Possible permutations with repetition - Python Library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/AntonisPilo/pcomp',  
  author='Antonis Piloridis',
  author_email='antonispiloridis@gmail.com',
  license='MIT',
  python_requires='>=3.3',
  classifiers=classifiers,
  keywords=['permutations','permutations with repetition'], 
  packages=find_packages(),
  install_requires=[''] 
)