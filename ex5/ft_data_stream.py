"""
Stream Wizard - Generator-based Event Processing System.

Demonstrates:
- Creating generators with yield
- Processing data streams efficiently
- Filtering events with generator expressions
- Memory-efficient statistics tracking
- Comparison between list storage vs streaming
"""


def event_stream(events):
    """Generator that yields events one by one."""
    for event in events:
        yield event
