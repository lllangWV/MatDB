from setuptools import setup
from setuptools_scm import ScmVersion
import setuptools_scm
def version_for_project(version: ScmVersion) -> str:
   print(f"setup.py:version: {version.tag}")
   return str(version.tag)
   
import pkg_resources
print(pkg_resources.get_distribution('setuptools_scm').version)
print(pkg_resources.get_distribution('setuptools').version)


print("setup.py: Starting setup")
setup(use_scm_version={'version_scheme':version_for_project})