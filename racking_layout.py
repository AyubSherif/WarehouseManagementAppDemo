import pandas as pd

def generate_single_rack(aisle, bay_range, level_order, level_dimensions):
    locations = []
    level_bottoms = {}
    cumulative_height = 0
    for lvl in level_order:
        level_bottoms[lvl] = cumulative_height
        cumulative_height += level_dimensions[lvl][0]

    for bay in bay_range:
        for level in level_order:
            height, width = level_dimensions[level]
            num_positions = 12 if width == 1 else 3
            for pos in range(1, num_positions + 1):
                z_offset = level_bottoms[level] + height / 2
                y_pos = (bay - 1) * 12 + (pos - 1) * width + width / 2
                x_pos = 15 - z_offset if aisle == "A" else 25 + z_offset
                location_id = f"{aisle}-{bay:02}-{level}-{pos:02}"
                locations.append((location_id, x_pos, y_pos, width, height, aisle, level))
    return locations

def generate_rack_locations():
    rack_A = generate_single_rack('A', range(1, 5), ['A', 'B', 'C', 'D', 'E'],
                                  {'A': (1, 1), 'B': (1, 1), 'C': (1, 1), 'D': (4, 4), 'E': (4, 4)})
    rack_B = generate_single_rack('B', range(1, 4), ['A', 'B', 'C', 'D', 'E'],
                                  {'A': (2, 1), 'B': (2, 1), 'C': (2, 1), 'D': (3, 3), 'E': (3, 3)})
    df = pd.DataFrame(rack_A + rack_B, columns=["location_id", "x", "y", "width", "height", "aisle", "level"])
    return df
