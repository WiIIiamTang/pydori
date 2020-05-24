from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()
  
setup(
  name = 'pydori',         
  packages = find_packages(),   
  version = '0.1.1.7',      
  license='MIT',        
  description = 'A python package to interact with the bandori.party and bandori.ga public APIs',
  long_description=long_description,
  long_description_content_type='text/markdown',  
  author = 'William Tang',                   
  author_email = 'williaamt0@gmail.com',      
  #url = 'https://github.com/WiIIiamTang/pydori',    
  keywords = ['API', 'Bandori', 'Bang Dream'],   
  install_requires=['requests'],
  classifiers=[
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
    "Operating System :: OS Independent"
  ],
)