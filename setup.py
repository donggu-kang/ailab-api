from setuptools import setup, find_packages

setup(
    name='ailab-api',
    version='0.7',
    description='ailab-daejin-restful-api',
    author='donggu.kang',
    author_email='kang154123@naver.com',
    url='https://github.com/GoopyAspirin/ailab-api',
    download_url='https://github.com/GoopyAspirin/ailab-api/download/ailab-api-0.4.tar.gz',
    keywords=['api'],
    python_requires='>=3',
    packages=find_packages(exclude=['test']),
    install_requires=['requests'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
