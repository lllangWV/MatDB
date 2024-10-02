from setuptools import setup
from setuptools_scm import ScmVersion

def version_for_project(version: ScmVersion) -> str:
   print(f"setup.py:version: {version.tag}")
   return str(version.tag)
   


print("setup.py: Starting setup")
setup(use_scm_version={'version_scheme':version_for_project})