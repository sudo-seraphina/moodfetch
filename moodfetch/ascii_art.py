"""
ASCII art and emoji mappings for system moods in moodfetch utility.

This module provides visual representations of system moods through
ASCII art and emojis, enhancing the user experience of the moodfetch tool.
"""

from enum import Enum, auto
from typing import Dict, Optional

class SystemMood(Enum):
    """
    Enumeration of possible system mood states.
    Provides a more type-safe and extensible way to define system moods.
    """
    HAPPY = auto()
    TIRED = auto()
    STRESSED = auto()
    CALM = auto()

class MoodVisuals:
    """
    A class to manage ASCII art and emoji representations for system moods.
    Provides centralized and easily extendable mood visualization.
    """
   
    MOOD_ASCII_ART: Dict[SystemMood, str] = {
        SystemMood.HAPPY: r'''
    \(^_^)/
    Systems go! Feeling awesome!
         ''',
        SystemMood.TIRED: r'''
    (- _ -)  Zzz
    Need a system recharge...
         ''',
        SystemMood.STRESSED: r'''
    (╬ಠ益ಠ)
    Overloaded! Cooling required!
         ''',
        SystemMood.CALM: r'''
    (づ￣ ³￣)づ
    Steady and stable operations
         ''',
    }

   
    MOOD_EMOJIS: Dict[SystemMood, str] = {
        SystemMood.HAPPY: '😄',     # Low load, plenty of resources
        SystemMood.TIRED: '😴',     # Moderate load
        SystemMood.STRESSED: '😰',  # High load, low resources
        SystemMood.CALM: '😌',      # Optimal system state
    }

    @classmethod
    def get_ascii_art(cls, mood: SystemMood) -> str:
        """
        Retrieve ASCII art for a given system mood.

        Args:
            mood (SystemMood): The system mood to retrieve ASCII art for.

        Returns:
            str: ASCII art representation of the mood.
            Defaults to a neutral face if mood not found.
        """
        return cls.MOOD_ASCII_ART.get(mood, r'''
    (°_°)
    Unknown mood
        ''')

    @classmethod
    def get_emoji(cls, mood: SystemMood) -> str:
        """
        Retrieve emoji for a given system mood.

        Args:
            mood (SystemMood): The system mood to retrieve emoji for.

        Returns:
            str: Emoji representation of the mood.
            Defaults to a neutral face if mood not found.
        """
        return cls.MOOD_EMOJIS.get(mood, '😐')

    @classmethod
    def display_mood(cls, mood: SystemMood) -> None:
        """
        Display both ASCII art and emoji for a given system mood.

        Args:
            mood (SystemMood): The system mood to display.
        """
        print(f"Mood: {cls.get_emoji(mood)}")
        print(cls.get_ascii_art(mood))

def main():
    """
    Demonstration of mood visualization capabilities.
    """
  
    print("Moodfetch Mood Visualization Demo:")
    for mood in SystemMood:
        print(f"\n--- {mood.name} Mood ---")
        MoodVisuals.display_mood(mood)

if __name__ == "__main__":
    main()
