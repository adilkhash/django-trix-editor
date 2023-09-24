from setuptools import setup, find_packages

install_requires = [
    'Django>=4.1',
]

setup(
    name='django-trix2',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/adilkhash/django-trix2',
    license='MIT',
    author='Adylzhan Khashtamov',
    author_email='adil.khashtamov@gmail.com',
    description='Django App To Integrate Trix Editor',
    install_requires=install_requires,
)