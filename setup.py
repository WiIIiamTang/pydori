from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()
  
setup(
  name = 'pydori',         
  packages = find_packages(),   
  version = '0.4.0',      
  license='MIT',        
  description = 'A python wrapper to interact with the bandori.party and bandori.ga public APIs',
  long_description=long_description,
  long_description_content_type='text/markdown',  
  author = 'William Tang',                         
  url = 'https://github.com/WiIIiamTang/pydori',    
  keywords = ['API', 'Bandori', 'Bang Dream', 'rythm game'],   
  install_requires=['requests'],
  classifiers=[
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
    "Operating System :: OS Independent"
  ],
)