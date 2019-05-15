from setuptools import setup


setup(
    name='tornado-rediscluster-session',
    packages=['tornado_rediscluster_session'],
    version='0.1.4',
    description='Server side session middleware based on redis or rediscluster',
    author='David Wong & Andy Wong',
    author_email='stef-hw@163.com & dooostyle@gmail.com',
    url='https://github.com/andy-lab/tornado-rediscluster-session',
    #download_url='https://github.com/andy-lab/tornado-rediscluster-session/archive/0.1.4.tar.gz',
    keywords=['tornado', 'session', 'redis', 'rediscluster'],
    install_requires=['redis', 'rediscluster', 'tornado'],
    classifiers=[],
)
