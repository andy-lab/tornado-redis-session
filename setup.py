from setuptools import setup


setup(
    name='tornado-redis-session',
    packages=['tornado_redis_session'],
    version='0.1.4',
    description='Server side session middleware based on redis or rediscluster',
    author='David Wong & Andy Wong',
    author_email='stef-hw@163.com & dooostyle@gmail.com',
    url='https://github.com/andy-lab/tornado-redis-session',
    #download_url='https://github.com/hw20686832/tornado-redis-session/archive/0.1.3.tar.gz',
    keywords=['tornado', 'session', 'redis', 'rediscluster'],
    install_requires=['redis', 'rediscluster', 'tornado'],
    classifiers=[],
)
