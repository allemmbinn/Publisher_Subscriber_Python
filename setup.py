from setuptools import setup
w
package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='allemmbinn',
    maintainer_email='allemmbinn@gmail.com',
    description='Package with Publishers and Subscribers',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher:main',
            'listener = py_pubsub.subscriber:main',
        ],
    },
)
