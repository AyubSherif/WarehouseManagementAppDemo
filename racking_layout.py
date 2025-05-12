import pandas as pd

def generate_rack_locations():
    level_dimensions = {
        'A': (1, 1),
        'B': (1, 1),
        'C': (1, 1),
        'D': (4, 4),
        'E': (4, 4),
    }

    level_order = ['A', 'B', 'C', 'D', 'E']
    level_bottoms = {}
    cumulative_height = 0
    for lvl in level_order:
        level_bottoms[lvl] = cumulative_height
        cumulative_height += level_dimensions[lvl][0]

    aisles = ['A']
    bays = range(1, 5)
    locations = []

    for aisle in aisles:
        aisle_code = ord(aisle.upper()) - 65
        for bay in bays:
            for level in level_order:
                height, width = level_dimensions[level]
                num_positions = 12 if width == 1 else 3
                for pos in range(1, num_positions + 1):
                    x_left = (bay - 1) * 12 + (pos - 1) * width
                    x_right = (bay - 1) * 12 + pos * width
                    x_center = (x_left + x_right) / 2

                    y_inside = aisle_code * 10
                    y_outside = y_inside + 4
                    y_center = (y_inside + y_outside) / 2

                    z_bottom = level_bottoms[level]
                    z_top = z_bottom + height
                    z_center = (z_bottom + z_top) / 2

                    location_id = f"{aisle}-{bay:02}-{level}-{pos:02}"

                    locations.append((location_id, aisle, bay, level, pos,
                                      x_center, y_center, z_center,
                                      x_left, x_right, y_inside, y_outside, z_bottom, z_top))

    df = pd.DataFrame(locations, columns=[
        "location_id", "aisle", "bay", "level", "position",
        "x", "y", "z", "x_left", "x_right", "y_inside", "y_outside", "z_bottom", "z_top"
    ])
    return df