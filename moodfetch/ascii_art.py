"""
ASCII art and emoji mappings for system moods in the Moodfetch utility.
This module provides visually appealing representations of system moods,
enhancing the user experience with Linux-inspired themes using distro-specific art.
"""
from enum import Enum, auto
from typing import Dict

class SystemMood(Enum):
    """
    Enumeration of possible system mood states.
    Provides a type-safe and extensible way to define system moods.
    """
    HAPPY = auto()
    TIRED = auto()
    STRESSED = auto()
    CALM = auto()

class MoodVisuals:
    """
    A class to manage ASCII art representations for system moods.
    Provides centralized and artistically expressive mood visualization.
    """
    MOOD_ASCII_ART: Dict[SystemMood, str] = {
        SystemMood.HAPPY: r'''
       .--.
      |o_o |  HAPPY SYSTEM
      |:_/ |  Represented by Ubuntu
     //   \ \  "All Systems Go!"
    (|     | )
   /'\_   _/`\
   \___)=(___/
        ''',
        SystemMood.TIRED: r'''
      _______
    _|       |_  TIRED SYSTEM
   |   🐧    |  Represented by Debian
   |   _     |  "Low Power Mode..."
   |___|_____|
     /       \
    (_________)
        ''',
        SystemMood.STRESSED: r'''
         ____    STRESSED SYSTEM
      o8%8888,   Represented by Arch Linux
    o88%8888888.  "Resources Maxed!"
   8'-    -:8888b
  8'         8888
 d8.-=. ,==-.:888b
 >( o ) :(. o ):8888
 88~+~:'~'::~'8888
 88::.      .:88888
 888:::.  .:::88888
 88888'::'   888888
  `88       .8888888
        ''',
        SystemMood.CALM: r'''
      _______
    _|       |_  CALM SYSTEM
   |  🐧     |  Represented by Fedora
   |         |  "Smooth Operations"
   |___===___|
    (_______)
        ''',
    }

    MOOD_EMOJIS: Dict[SystemMood, str] = {
        SystemMood.HAPPY: '✨',   # Peak performance
        SystemMood.TIRED: '💤',  # Resting state
        SystemMood.STRESSED: '⚠️',  # Alert
        SystemMood.CALM: '❄️',   # Chill mode
    }

    @classmethod
    def get_ascii_art(cls, mood: SystemMood) -> str:
        """
        Retrieve ASCII art for a given system mood.
        Args:
            mood (SystemMood): The system mood to retrieve ASCII art for.
        Returns:
            str: ASCII art representation of the mood.
        """
        return cls.MOOD_ASCII_ART.get(mood, r'''
    _____________________
   /                     \
  /    UNKNOWN STATE      \
 /   System Undefined...  \
/   Diagnosis Needed! ❓  \
|  Tux is Confused! 🐧   |
 \                     /
  \___________________/
        ''')

    @classmethod
    def get_emoji(cls, mood: SystemMood) -> str:
        """
        Retrieve emoji for a given system mood.
        Args:
            mood (SystemMood): The system mood to retrieve emoji for.
        Returns:
            str: Emoji representation of the mood.
        """
        return cls.MOOD_EMOJIS.get(mood, '❓')

    @classmethod
    def display_mood(cls, mood: SystemMood) -> None:
        """
        Display both ASCII art and emoji for a given system mood.
        Args:
            mood (SystemMood): The system mood to display.
        """
        print(f"Mood Indicator: {cls.get_emoji(mood)}")
        print(cls.get_ascii_art(mood))

def main():
    """
    Demonstration of mood visualization capabilities.
    """
    print("Moodfetch Mood Visualization Demo")
    for mood in SystemMood:
        print(f"\n--- {mood.name} Mood ---")
        MoodVisuals.display_mood(mood)

if __name__ == "__main__":
    main()
