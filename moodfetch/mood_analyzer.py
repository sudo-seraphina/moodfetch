"""
System Mood Analyzer for moodfetch utility.

This module provides comprehensive system performance analysis
and mood determination based on system metrics.
"""

import psutil
import time
import logging
from typing import Dict, Any, Optional
from enum import Enum, auto

from .ascii_art import MoodVisuals, SystemMood

class SystemPerformanceException(Exception):
    """Custom exception for system performance-related errors."""
    pass

class SystemMoodAnalyzer:
    """
    Comprehensive analyzer for determining system performance 'mood'.

    Analyzes key system metrics to provide insights into
    system health and performance state.
    """
    def __init__(self,
                 cpu_threshold_high: float = 80.0,
                 memory_threshold_high: float = 80.0,
                 disk_threshold_high: float = 80.0,
                 uptime_threshold_hours: int = 24):
        """
        Initialize system mood analyzer with configurable thresholds.

        Args:
            cpu_threshold_high (float): Threshold for high CPU usage (%).
            memory_threshold_high (float): Threshold for high memory usage (%).
            disk_threshold_high (float): Threshold for high disk usage (%).
            uptime_threshold_hours (int): Threshold for prolonged uptime (hours).
        """
        self.logger = logging.getLogger(__name__)

        self.thresholds = {
            'cpu': {'high': cpu_threshold_high, 'moderate': 50.0},
            'memory': {'high': memory_threshold_high, 'moderate': 50.0},
            'disk': {'high': disk_threshold_high, 'moderate': 50.0},
        }
        self.uptime_threshold_hours = uptime_threshold_hours

    def get_system_metrics(self) -> Dict[str, Any]:
        """
        Collect and return comprehensive system metrics.

        Returns:
            Dict containing system performance metrics.

        Raises:
            SystemPerformanceException: If unable to retrieve system metrics.
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            uptime_seconds = time.time() - psutil.boot_time()

            return {
                'cpu_usage': cpu_usage,
                'memory_usage': memory.percent,
                'memory_total_gb': round(memory.total / (1024**3), 2),
                'memory_available_gb': round(memory.available / (1024**3), 2),
                'disk_usage': disk.percent,
                'disk_total_gb': round(disk.total / (1024**3), 2),
                'disk_free_gb': round(disk.free / (1024**3), 2),
                'uptime_hours': round(uptime_seconds / 3600, 2),
            }
        except Exception as e:
            self.logger.error(f"Error retrieving system metrics: {e}")
            raise SystemPerformanceException("Failed to collect system metrics") from e

    def calculate_health_score(self, metrics: Dict[str, Any]) -> float:
        """
        Calculate a weighted health score for the system.

        Args:
            metrics (Dict[str, Any]): System performance metrics.

        Returns:
            float: Health score (0-100), where higher is better.
        """
        cpu_score = max(0, 100 - metrics['cpu_usage'])
        memory_score = max(0, 100 - metrics['memory_usage'])
        disk_score = max(0, 100 - metrics['disk_usage'])
        uptime_penalty = min(20, metrics['uptime_hours'] / self.uptime_threshold_hours * 20)

        # Aggregate health score
        return max(0, (cpu_score + memory_score + disk_score) / 3 - uptime_penalty)

    def determine_mood(self) -> SystemMood:
        """
        Determine the system's current mood based on performance metrics.

        Returns:
            SystemMood: Categorized system mood state.
        """
        metrics = self.get_system_metrics()
        health_score = self.calculate_health_score(metrics)

        if health_score < 40 or metrics['cpu_usage'] > self.thresholds['cpu']['high']:
            return SystemMood.STRESSED
        elif metrics['uptime_hours'] > self.uptime_threshold_hours:
            return SystemMood.TIRED
        elif health_score > 80:
            return SystemMood.HAPPY
        else:
            return SystemMood.CALM

    def get_mood_details(self) -> Dict[str, Any]:
        """
        Generate a comprehensive mood report.

        Returns:
            Dict containing mood information and system metrics.
        """
        try:
            metrics = self.get_system_metrics()
            mood = self.determine_mood()

            return {
                'mood': mood.name.lower(),
                'emoji': MoodVisuals.get_emoji(mood),
                'ascii_art': MoodVisuals.get_ascii_art(mood),
                'metrics': metrics,
                'health_score': self.calculate_health_score(metrics),
            }
        except SystemPerformanceException as e:
            self.logger.error(f"Failed to generate mood details: {e}")
            return {
                'mood': 'unknown',
                'emoji': '❓',
                'ascii_art': 'Metrics unavailable',
                'metrics': {},
                'health_score': 0,
            }

def main():
    """
    Run a demonstration of the SystemMoodAnalyzer.
    """
    logging.basicConfig(level=logging.INFO)
    analyzer = SystemMoodAnalyzer()

    try:
        report = analyzer.get_mood_details()
        print("System Mood Report:")
        print(f"Mood: {report['mood'].capitalize()} {report['emoji']}")
        print("\nASCII Art:")
        print(report['ascii_art'])
        print("\nSystem Metrics:")
        for key, value in report['metrics'].items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        print(f"\nHealth Score: {report['health_score']:.2f}")
    except Exception as e:
        logging.error(f"Error during mood analysis: {e}")

if __name__ == "__main__":
    main()
