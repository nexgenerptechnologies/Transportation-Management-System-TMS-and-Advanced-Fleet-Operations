from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = [line.strip() for line in f.read().splitlines() if line.strip()]

# get version from __version__ variable in tms/__init__.py
from tms import __version__ as version

setup(
	name="tms",
	version=version,
	description="Transportation Management System",
	author="NexGen ERP Technologies",
	author_email="admin@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
