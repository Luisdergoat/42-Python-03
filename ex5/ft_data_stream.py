"""
Game Data Stream Processor - Generator-based Event System.

Demonstrates:
- Creating generators with yield
- Processing large data streams efficiently
- Filtering events without storing all data
- Memory-efficient statistics tracking
- Mathematical sequence generators
"""

import random
import time


def game_event_generator(count):
    """
    Generate game events on-demand using a generator.

    Args:
        count:  Number of events to generate

    Yields:
        dict: Event with player, level, and action
    """
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(count):
        event = {
            "id": i + 1,
            "player": random.choice(players),
            "level": random.randint(1, 15),
            "action": random.choice(actions),
        }
        yield event


def count_high_level_players(event_stream):
    """
    Count events from high-level players (level 10+).

    Args:
        event_stream: Generator of game events

    Returns:
        int: Count of high-level player events
    """
    count = 0
    for event in event_stream:
        if event["level"] >= 10:
            count += 1
    return count


def count_action_events(event_stream, action):
    """
    Count events of a specific action type.

    Args:
        event_stream: Generator of game events
        action: Action string to count

    Returns:
        int:  Count of matching events
    """
    count = 0
    for event in event_stream:
        if event["action"] == action:
            count += 1
    return count


def fibonacci_generator(n):
    """
    Generate Fibonacci sequence.

    Args:
        n:  Number of Fibonacci numbers to generate

    Yields:
        int:  Next Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num: Number to check

    Returns:
        bool:  True if prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    """
    Generate prime numbers.

    Args:
        n: Number of primes to generate

    Yields:
        int: Next prime number
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main():
    """Run the game data stream processor."""
    # Set random seed for reproducibility
    random.seed(42)

    print("=== Game Data Stream Processor ===")

    # Configuration
    event_count = 1000

    # Display first few events
    print(f"Processing {event_count} game events...")
    event_gen = game_event_generator(event_count)

    # Show first 3 events
    for i, event in enumerate(event_gen):
        if i < 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
            )
        else:
            break

    print("...")

    # Stream Analytics
    print()
    print("=== Stream Analytics ===")

    # Start timing
    start_time = time.time()

    # Reset seed for consistent statistics
    random.seed(42)

    # Total events (we know it's 1000, but could count)
    print(f"Total events processed: {event_count}")

    # Count high-level players
    random.seed(42)
    high_level_gen = game_event_generator(event_count)
    high_level_count = count_high_level_players(high_level_gen)
    print(f"High-level players (10+): {high_level_count}")

    # Count treasure events
    random.seed(42)
    treasure_gen = game_event_generator(event_count)
    treasure_count = count_action_events(treasure_gen, "found treasure")
    print(f"Treasure events:  {treasure_count}")

    # Count level-up events
    random.seed(42)
    levelup_gen = game_event_generator(event_count)
    levelup_count = count_action_events(levelup_gen, "leveled up")
    print(f"Level-up events: {levelup_count}")

    # Memory usage
    print("Memory usage: Constant (streaming)")

    # Processing time
    end_time = time.time()
    processing_time = end_time - start_time
    print(f"Processing time: {processing_time:.3f} seconds")

    # Generator Demonstration
    print()
    print("=== Generator Demonstration ===")

    # Fibonacci sequence
    fib_gen = fibonacci_generator(10)
    fib_numbers = list(fib_gen)
    fib_str = ", ".join(map(str, fib_numbers))
    print(f"Fibonacci sequence (first 10): {fib_str}")

    # Prime numbers
    prime_gen = prime_generator(5)
    prime_numbers = list(prime_gen)
    prime_str = ", ".join(map(str, prime_numbers))
    print(f"Prime numbers (first 5): {prime_str}")


main()
