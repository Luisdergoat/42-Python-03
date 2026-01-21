"""
3D Coordinate System - Game Position Manager.

Demonstrates:
- 3D position creation with immutable tuples
- Euclidean distance calculation in 3D space
- String parsing for coordinate input
- Tuple unpacking
- Error handling for invalid inputs
"""

import math


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(coord_str):
    """Parse a string of the form 'x,y,z' into a tuple of floats."""
    parts = coord_str.split(",")
    x = int(parts[0].strip())
    y = int(parts[1].strip())
    z = int(parts[2].strip())
    return (x, y, z)


def main():
    print("=== 3D Coordinate System - Position Manager ===\n")

    # Create some 3D points
    coord1 = (10, 20, 5)
    print(f"position Created: '{coord1}'")

    original_point = (0, 0, 0)
    dist1 = calculate_distance(original_point, coord1)
    print(f"Distance from {original_point} to {coord1}: {dist1:.2f}")

    coord2_str = "3, 4, 0"
    print(f"\nParsing coordinates: '{coord2_str}'")
    coord2_str = parse_coordinates(coord2_str)
    print(f"Parsed coordinates: {coord2_str}")
    dist2 = calculate_distance(original_point, coord2_str)
    print(f"Distance from {original_point} to {coord2_str}: {dist2:.2f}")

    # demonstrate error handling
    invalid_coord_str = "1, two, 3"
    print(f"\nParsing coordinates: '{invalid_coord_str}'")
    try:
        invalid_coord = parse_coordinates(invalid_coord_str)
        print(f"Parsed coordinates: {invalid_coord}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
    print("\n✅ Position management completed.")
    x, y, z = coord2_str
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates; x={x}, y={y}, z={z}")


main()
