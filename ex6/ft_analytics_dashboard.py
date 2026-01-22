"""
Game Analytics Dashboard - Comprehension Mastery.

Demonstrates:
- List comprehensions for filtering and transforming
- Dict comprehensions for mapping and grouping
- Set comprehensions for finding unique values
- Combined analysis using all comprehension types
"""


def create_sample_data():
    """
    Create sample gaming data for analysis.

    Returns:
        dict: Dictionary containing players, sessions, and achievements
    """
    data = {
        "players": [
            {
                "name": "alice",
                "score": 2300,
                "level": 15,
                "active": True,
                "region": "north",
            },
            {
                "name": "bob",
                "score": 1800,
                "level": 12,
                "active": True,
                "region": "east",
            },
            {
                "name": "charlie",
                "score": 2150,
                "level": 18,
                "active": True,
                "region": "central",
            },
            {
                "name": "diana",
                "score": 2050,
                "level": 14,
                "active": False,
                "region": "north",
            },
        ],
        "achievements": {
            "alice": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "speed_demon",
            ],
            "bob": ["first_kill", "level_10", "collector"],
            "charlie": [
                "first_kill",
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "speed_demon",
                "perfectionist",
                "master",
            ],
            "diana": ["first_kill", "level_10", "boss_slayer"],
        },
    }
    return data


def list_comprehension_examples(players):
    """
    Demonstrate list comprehensions.

    Args:
        players:  List of player dictionaries

    Returns:
        dict: Results of various list comprehensions
    """
    # Filter high scorers (>2000)
    high_scorers = [p["name"] for p in players if p["score"] > 2000]

    # Transform:  double all scores
    scores_doubled = [p["score"] * 2 for p in players]

    # Filter active players
    active_players = [p["name"] for p in players if p["active"]]

    return {
        "high_scorers": high_scorers,
        "scores_doubled": scores_doubled,
        "active_players": active_players,
    }


def dict_comprehension_examples(players, achievements):
    """
    Demonstrate dict comprehensions.
    Args:
        players: List of player dictionaries
        achievements: Dict of player achievements

    Returns:
        dict:  Results of various dict comprehensions
    """
    # Create name -> score mapping
    player_scores = {p["name"]: p["score"] for p in players}

    # Categorize scores
    score_categories = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] < 1500]),
    }

    # Count achievements per player
    achie_counts = {name: len(achs) for name, achs in achievements.items()}

    return {
        "player_scores": player_scores,
        "score_categories": score_categories,
        "achievement_counts": achie_counts,
    }


def set_comprehension_examples(players, achievements):
    """
    Demonstrate set comprehensions.

    Args:
        players: List of player dictionaries
        achievements: Dict of player achievements

    Returns:
        dict: Results of various set comprehensions
    """
    # Get unique player names
    unique_players = {p["name"] for p in players}

    # Get all unique achievements
    unique_achie = {ach for achs in achievements.values() for ach in achs}

    # Get unique regions (only active players)
    active_regions = {p["region"] for p in players if p["active"]}

    return {
        "unique_players": unique_players,
        "unique_achievements": unique_achie,
        "active_regions": active_regions,
    }


def combined_analysis(players, achie):
    """
    Perform combined analysis using multiple comprehensions.

    Args:
        players: List of player dictionaries
        achievements: Dict of player achievements

    Returns:
        dict:  Combined analysis results
    """
    # Total players
    total_players = len(players)

    # Total unique achievements across all players
    all_achievements = {ach for achs in achie.values() for ach in achs}
    total_unique_achievements = len(all_achievements)

    # Average score
    total_score = sum(p["score"] for p in players)
    average_score = total_score / total_players if total_players > 0 else 0

    # Find top performer (highest score + achievement count)
    top_player = max(
        players, key=lambda p: (p["score"], len(achie.get(p["name"], [])))
        )
    top_name = top_player["name"]
    top_score = top_player["score"]
    top_achievements = len(achie.get(top_name, []))

    return {
        "total_players": total_players,
        "total_unique_achievements": total_unique_achievements,
        "average_score": average_score,
        "top_performer": {
            "name": top_name,
            "score": top_score,
            "achievements": top_achievements,
        },
    }


def main():
    """Run the analytics dashboard."""
    print("=== Game Analytics Dashboard ===")

    # Create sample data
    data = create_sample_data()
    players = data["players"]
    achievements = data["achievements"]

    # List Comprehension Examples
    print()
    print("=== List Comprehension Examples ===")
    list_results = list_comprehension_examples(players)
    print(f"High scorers (>2000): {list_results['high_scorers']}")
    print(f"Scores doubled: {list_results['scores_doubled']}")
    print(f"Active players:  {list_results['active_players']}")

    # Dict Comprehension Examples
    print()
    print("=== Dict Comprehension Examples ===")
    dict_results = dict_comprehension_examples(players, achievements)
    print(f"Player scores: {dict_results['player_scores']}")
    print(f"Score categories: {dict_results['score_categories']}")
    print(f"Achievement counts: {dict_results['achievement_counts']}")

    # Set Comprehension Examples
    print()
    print("=== Set Comprehension Examples ===")
    set_results = set_comprehension_examples(players, achievements)
    print(f"Unique players:  {set_results['unique_players']}")
    print(f"Unique achievements: {set_results['unique_achievements']}")
    print(f"Active regions: {set_results['active_regions']}")

    # Combined Analysis
    print()
    print("=== Combined Analysis ===")
    analysis = combined_analysis(players, achievements)
    print(f"Total players: {analysis['total_players']}")
    print(f"Total unique achievements: "
          f"{analysis['total_unique_achievements']}")
    print(f"Average score: {analysis['average_score']}")
    top = analysis["top_performer"]
    print(
        f"Top performer: {top['name']} ({top['score']} points, "
        f"{top['achievements']} achievements)"
    )


main()
