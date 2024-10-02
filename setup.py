from setuptools import setup
from setuptools_scm import ScmVersion
import setuptools_scm
def version_for_project(version: ScmVersion) -> str:
   print(f"setup.py:version: {version.tag}")
   return str(version.tag)
   
print(setuptools_scm.__version__)


print("setup.py: Starting setup")
setup(use_scm_version={'version_scheme':version_for_project})