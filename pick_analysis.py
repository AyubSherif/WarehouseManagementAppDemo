import numpy as np

def simulate_picking_data(locations_df):
    locations_df = locations_df.copy()
    locations_df['picks'] = np.random.randint(0, 100, size=len(locations_df))
    return locations_df
