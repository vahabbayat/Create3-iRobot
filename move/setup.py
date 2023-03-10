from setuptools import setup

package_name = 'move'

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
    maintainer='vahabbayat',
    maintainer_email='baya0029@algonquinlive.com',
    description='moving along the edge',
    license='No License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move = move.move:main',
        ],
    },
)
