import setuptools

setuptools.setup(
    name='shell-cache',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/shell-cache']
)
