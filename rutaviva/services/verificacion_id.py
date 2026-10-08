import pandas as pd, geopandas as gpd

df_csv = pd.read_csv("services/seed_cli/app/data/csv/taxi_zone_lookup.csv")
gdf_shp = gpd.read_file("services/seed_cli/app/data/shapefiles/taxi_zones.shp")

ids_csv = set(df_csv["LocationID"].astype(int))
ids_shp = set(gdf_shp["LocationID"].astype(int))

print("Solo en shapefile:", ids_shp - ids_csv)
print("Solo en CSV:", ids_csv - ids_shp)