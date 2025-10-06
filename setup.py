from setuptools import setup, find_packages

setup(
    name="carabas2tools",
    version="1.0.0",
    author="Gabriel Luiz Espindola Pedro",
    author_email="gabrielluizep.glep@gmail.com",
    description="Tools to work with CARABAS-II dataset (requires local data)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielluizep/carabas2tools",
    license="MIT",
    packages=find_packages(),
    install_requires=["numpy", "scipy", "pandas"],
    python_requires=">=3.8",
)
