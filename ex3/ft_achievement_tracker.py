"""
Achievement Tracker System - Game Achievement Manager.

Demonstrates:
- Using sets to track unique achievements
- Set operations (union, intersection, difference)
- Finding common and rare achievements
- Comparing player achievement collections
"""


def format_set(achievements_set):
    """Format a set of achievements for display."""
    sorted_items = sorted(achievements_set)
    formatted_items = [f"'{item}'" for item in sorted_items]
    return "{" + ", ".join(formatted_items) + "}"


def get_all_achievements(players_dict):
    """Get a set of all unique achievements from all players."""
    all_achievements = set()
    for achievements in players_dict.values():
        all_achievements = all_achievements.union(achievements)
    return all_achievements


def get_common_achievements(players_dict):
    """Get a set of achievements common to all players."""
    achievement_sets = list(players_dict.values())
    if not achievement_sets:
        return set()

    common_achievements = achievement_sets[0]
    for achievements in achievement_sets[1:]:
        common_achievements = common_achievements.intersection(achievements)
        return common_achievements


def get_rare_achievements(players_dict):
    """Get a set of achievements that are unique to each player."""
    ach_counts = {}
    for achievements in players_dict.values():
        for achievement in achievements:
            ach_counts[achievement] = ach_counts.get(achievement, 0) + 1
    rare_achievements = {
        achievement for achievement, count in ach_counts.items() if count == 1
    }
    return rare_achievements


def main():
    """Run the Achievement Tracker System."""
    print("=== Achievement Tracker System - Game Achievement Manager ===\n")

    # Create player achievement sets
    players = {
        "Alice": {"first kill", "level_10", "treasure_hunter", "speed_demon"},
        "Bob": {"first kill", "level_10", "boss_slayer", "collector"},
        "Charlie": {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        },
    }
    # Display player achievements
    print(f"Player Alice achievements: {format_set(players['Alice'])}")
    print(f"Player Bob achievements: {format_set(players['Bob'])}")
    print(f"Player Charlie achievements: {format_set(players['Charlie'])}")
    print("\n=== Achievement Analytics ===")
    # All unique achievements
    all_achievements = get_all_achievements(players)
    print(f"All unique achievements: {format_set(all_achievements)}")
    print(f"Total unique achievements: {len(all_achievements)}")

    # Common achievements
    common_achievements = get_common_achievements(players)
    print(f"Common achievements: {format_set(common_achievements)}")
    print(f"Total common achievements: {len(common_achievements)}")

    # Rare achievements owned by only one player
    rare_achievements = get_rare_achievements(players)
    print(f"Rare achievements: {format_set(rare_achievements)}")
    print(f"Total rare achievements: {len(rare_achievements)}")

    # Alice vs Bob comparison
    alice_bob_common = players["Alice"].intersection(players["Bob"])
    print(f"Alice and Bob common achievements: {format_set(alice_bob_common)}")

    # Alice unique achievements
    alice_unique = players["Alice"].difference(players["Bob"])
    print(f"Alice unique achievements: {format_set(alice_unique)}")

    # Bob unique achievements
    bob_unique = players["Bob"].difference(players["Alice"])
    print(f"Bob unique achievements: {format_set(bob_unique)}")

    print("\n✅ Achievement tracking completed.")


main()
