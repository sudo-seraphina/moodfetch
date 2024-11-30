import sys
import argparse
import logging
from typing import Dict, Any, List
from .mood_analyzer import SystemMoodAnalyzer, SystemPerformanceException
from .ascii_art import MoodVisuals, SystemMood

def configure_logging() -> logging.Logger:
    logger = logging.getLogger('moodfetch')
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - moodfetch - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='MoodFetch: System Performance Mood Tracker',
        epilog='Track your system\'s operational state with ease.'
    )
    parser.add_argument('-v', '--verbose', action='store_true', help='Display detailed system metrics')
    parser.add_argument('-m', '--minimal', action='store_true', help='Show only mood and emoji')
    return parser.parse_args()

def format_output(mood_details: Dict[str, Any], args: argparse.Namespace) -> str:
    color_codes = {
        'EXCELLENT': '\033[92m',    # Bright Green
        'GOOD': '\033[96m',         # Cyan
        'AVERAGE': '\033[93m',      # Yellow
        'POOR': '\033[91m',         # Bright Red
        'CRITICAL': '\033[41;1;37m' # Red Background with White Text
    }
    reset = '\033[0m'
    bold_white = '\033[1;37m'

    mood = mood_details['mood'].upper()
    mood_color = color_codes.get(mood, '\033[97m')
    emoji = mood_details.get('emoji', '🤔')

    # Format ASCII art
    ascii_art = mood_details.get('ascii_art', 'No ASCII art available').split('\n')
    ascii_art = [line[:40].ljust(40) for line in ascii_art]  # Wrap and pad for consistent width

    # Prepare system info
    info_lines = [
        f"{bold_white}Mood      {reset}: {mood_color}{mood} {emoji}{reset}",
    ]

    if args.verbose and 'metrics' in mood_details:
        metrics = mood_details['metrics']
        for key, value in metrics.items():
            formatted_key = key.replace('_', ' ').title()
            info_lines.append(f"{bold_white}{formatted_key:<10}{reset}: {value:>5}%")

    # Combine ASCII art and info lines
    max_lines = max(len(ascii_art), len(info_lines))
    output = f"\n{mood_color}MoodFetch - System Performance Mood Tracker{reset}\n"
    output += f"{mood_color}─────────────────────────────────────────{reset}\n"

    for i in range(max_lines):
        art = ascii_art[i] if i < len(ascii_art) else ' ' * 40
        info = info_lines[i] if i < len(info_lines) else ''
        output += f"{mood_color}{art}{reset} {info}\n"

    return output

def display_mood(mood_details: Dict[str, Any], args: argparse.Namespace) -> None:
    output = format_output(mood_details, args)
    print(output)

def main() -> None:
    logger = configure_logging()
    args = parse_arguments()

    try:
        analyzer = SystemMoodAnalyzer()
        mood_details = analyzer.get_mood_details()
        display_mood(mood_details, args)
    except SystemPerformanceException as spe:
        logger.error(f"System performance analysis failed: {spe}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error in moodfetch: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
