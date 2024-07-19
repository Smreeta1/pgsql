from setuptools import setup, find_packages

setup(
    name='pgsql_project', 
    version='0.1.0',
    description='A simple library management system using PostgreSQL',
    author='Your Name', 
    packages=find_packages(), 
    install_requires=[
        'psycopg2-binary', 
        'python-dotenv'  
    ],
   
)
