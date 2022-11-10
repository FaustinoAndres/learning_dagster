from setuptools import find_packages, setup

setup(
    name="datalized",
    packages=find_packages(exclude=["datalized_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
