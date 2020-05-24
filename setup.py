from distutils.core import setup
setup(
  name = 'pydori',         
  packages = ['pydori'],   
  version = '0.1',      
  license='MIT',        
  description = 'A python package to interact with the bandori.party and bandori.ga public APIs',   
  author = 'William Tang',                   
  author_email = 'williaamt0@gmail.com',      
  url = 'https://github.com/WiIIiamTang/pydori',  
  download_url = 'https://github.com/WiIIiamTang/pydori/archive/v0.1.tar.gz',  
  keywords = ['API', 'Bandori', 'Bang Dream'],   
  install_requires=['requests'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)