from dagster import load_assets_from_package_module, repository

from datalized import assets


@repository
def datalized():
    return [load_assets_from_package_module(assets)]
