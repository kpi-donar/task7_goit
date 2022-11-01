from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    description='To order your Forder',
    url='https://github.com/kpi-donar/task7_goit.git',
    author='DAM',
    author_email='dam@example.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)