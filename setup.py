from setuptools import setup, find_packages

install_requires = [
    'Django>=4.1',
]

setup(
    name='django-trix-editor',
    version='0.3',
    packages=find_packages(),
    url='https://github.com/adilkhash/django-trix-editor',
    license='MIT',
    author='Adylzhan Khashtamov',
    author_email='adil.khashtamov@gmail.com',
    description='Django App To Integrate Trix Editor',
    install_requires=install_requires,
)
