"""
MoodFetch Utility: System Performance Mood Tracker

This utility provides a quick and intuitive way to assess
system performance and current operational state.
"""

import sys
import argparse
import logging
from typing import Dict, Any

from .mood_analyzer import SystemMoodAnalyzer, SystemPerformanceException
from .ascii_art import MoodVisuals, SystemMood

def configure_logging() -> logging.Logger:
    """
    Configure logging for the moodfetch utility.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger('moodfetch')
    logger.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - moodfetch - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    return logger

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the moodfetch utility.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='MoodFetch: System Performance Mood Tracker',
        epilog='Track your system\'s operational state with ease.'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Display detailed system metrics'
    )

    parser.add_argument(
        '-m', '--minimal',
        action='store_true',
        help='Show only mood and emoji'
    )

    return parser.parse_args()

def display_mood_details(
    mood_details: Dict[str, Any],
    logger: logging.Logger,
    args: argparse.Namespace
) -> None:
    """
    Display system mood and associated details.

    Args:
        mood_details (Dict[str, Any]): Comprehensive mood analysis details.
        logger (logging.Logger): Logger instance for potential error reporting.
        args (argparse.Namespace): Parsed command-line arguments.
    """
    mood = mood_details['mood'].upper()
    emoji = mood_details['emoji']

    # Primary mood display
    print(f"System Mood: {mood} {emoji}")

    # ASCII Art Display (unless in minimal mode)
    if not args.minimal:
        print("\n" + mood_details['ascii_art'])

    # Verbose metrics display
    if args.verbose:
        print("\nDetailed System Metrics:")
        metrics = mood_details['metrics']
        for key, value in metrics.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"{formatted_key}: {value}")

def main() -> None:
    """
    Primary entry point for the moodfetch utility.
    Orchestrates system mood analysis and result presentation.
    """
    # Configure logging
    logger = configure_logging()

    try:
        # Parse command-line arguments
        args = parse_arguments()

        # Create system mood analyzer
        analyzer = SystemMoodAnalyzer()

        # Retrieve mood details
        mood_details = analyzer.get_mood_details()

        # Display mood and metrics
        display_mood_details(mood_details, logger, args)

    except SystemPerformanceException as spe:
        # Handle specific system performance collection errors
        logger.error(f"System performance analysis failed: {spe}")
        sys.exit(1)

    except Exception as e:
        # Catch-all for unexpected errors
        logger.error(f"Unexpected error in moodfetch: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
