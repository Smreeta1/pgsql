from setuptools import setup, find_packages

setup(
    name='pgsql_project', 
    version='1.0',
    description='A simple database using PostgreSQL',
    author='Smreeta', 
    packages=find_packages(), 
    install_requires=[
        'psycopg2-binary', 
        'python-dotenv'  
    ],
   
)