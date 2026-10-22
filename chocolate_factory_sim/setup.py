from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'chocolate_factory_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        *[
            (os.path.join('share', package_name, os.path.dirname(f)),
             [f])
            for folder in ['launch', 'config', 'meshes',
                           'models', 'urdf', 'worlds']
            for f in glob(folder + '/**/*', recursive=True)
            if os.path.isfile(f)
        ],
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Custom Gazebo simulation world',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['spawn_chocolate = chocolate_factory_sim.spawn_chocolate:main', 'chocolate_subscriber = chocolate_factory_sim.chocolate_subscriber:main'],
    },
)
