import importlib, sys
print("Python", sys.version)
for pkg in ["numpy","pandas","scipy","sklearn","matplotlib","xarray","netCDF4","yaml"]:
    try:
        importlib.import_module(pkg); print("OK", pkg)
    except Exception as e:
        print("MISSING", pkg, e)
for pkg in ["tensorflow","geopandas","rasterio","rioxarray"]:
    try:
        importlib.import_module(pkg); print("OK optional", pkg)
    except Exception as e:
        print("Missing optional", pkg, e)
