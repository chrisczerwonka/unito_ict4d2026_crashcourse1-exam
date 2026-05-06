import pandas as pd
import json
import math
import os

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r

# 1. Load data
print("Loading data...")
conflict_df = pd.read_csv('data/cleaned/acled-sahel-filtered.csv')
with open('data/processed/schools_combined.geojson', 'r') as f:
    schools_data = json.load(f)

# Extract conflict coordinates for faster lookup
# Using a list of tuples (lat, lon)
conflicts = list(zip(conflict_df['CENTROID_LATITUDE'], conflict_df['CENTROID_LONGITUDE']))

at_risk_features = []
safe_features = []

print(f"Analyzing {len(schools_data['features'])} schools against {len(conflicts)} conflict events...")

# 2. For each facility, find the nearest conflict event
for i, feature in enumerate(schools_data['features']):
    school_lon, school_lat = feature['geometry']['coordinates']
    
    min_dist = float('inf')
    
    # We loop through all conflicts to find the absolute nearest one
    # Note: For 17k schools * 21k conflicts, this is ~350 million calculations.
    # To keep it fast for this environment, we will use a small optimization:
    # If we find a conflict within 1km, we stop looking further for that school.
    for con_lat, con_lon in conflicts:
        dist = haversine(school_lat, school_lon, con_lat, con_lon)
        if dist < min_dist:
            min_dist = dist
        if min_dist < 0.5: # Optimization: "Close enough" to be at risk
            break
            
    # 3. Add risk status and distance
    feature['properties']['distance_to_nearest_conflict'] = round(min_dist, 2)
    
    if min_dist <= 5.0:
        feature['properties']['risk_status'] = 'at-risk'
        at_risk_features.append(feature)
    else:
        feature['properties']['risk_status'] = 'safe'
        safe_features.append(feature)
    
    if (i + 1) % 1000 == 0:
        print(f"Processed {i + 1} schools...")

# 4. Save files
def save_geojson(features, filename):
    data = {
        'type': 'FeatureCollection',
        'features': features
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

save_geojson(at_risk_features, 'data/processed/schools_at_risk.geojson')
save_geojson(safe_features, 'data/processed/schools_safe.geojson')

print(f"Analysis Complete!")
print(f"At-Risk Schools (within 5km): {len(at_risk_features)}")
print(f"Safe Schools: {len(safe_features)}")
