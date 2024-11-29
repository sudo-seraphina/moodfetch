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
                 disk_threshold_high: float = 80.0):
        """
        Initialize system mood analyzer with configurable thresholds.

        Args:
            cpu_threshold_high (float): Threshold for high CPU usage (%).
            memory_threshold_high (float): Threshold for high memory usage (%).
            disk_threshold_high (float): Threshold for high disk usage (%).
        """
        self.logger = logging.getLogger(__name__)

        # Configurable performance thresholds
        self.thresholds = {
            'cpu': {
                'high': cpu_threshold_high,
                'moderate': 50.0
            },
            'memory': {
                'high': memory_threshold_high,
                'moderate': 50.0
            },
            'disk': {
                'high': disk_threshold_high,
                'moderate': 50.0
            }
        }

    def get_system_metrics(self) -> Dict[str, Any]:
        """
        Collect and return comprehensive system metrics.

        Returns:
            Dict containing system performance metrics.

        Raises:
            SystemPerformanceException: If unable to retrieve system metrics.
        """
        try:
            # CPU Usage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Memory Usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            memory_total = memory.total / (1024 ** 3)  # Convert to GB
            memory_available = memory.available / (1024 ** 3)  # Convert to GB

            # Disk Usage
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent
            disk_total = disk.total / (1024 ** 3)  # Convert to GB
            disk_free = disk.free / (1024 ** 3)  # Convert to GB

            # System Uptime
            uptime = time.time() - psutil.boot_time()
            uptime_hours = uptime / 3600  # Convert to hours

            return {
                'cpu_usage': cpu_usage,
                'memory_usage': memory_usage,
                'memory_total_gb': round(memory_total, 2),
                'memory_available_gb': round(memory_available, 2),
                'disk_usage': disk_usage,
                'disk_total_gb': round(disk_total, 2),
                'disk_free_gb': round(disk_free, 2),
                'uptime_hours': round(uptime_hours, 2)
            }
        except Exception as e:
            self.logger.error(f"Failed to retrieve system metrics: {e}")
            raise SystemPerformanceException("Unable to collect system metrics") from e

    def determine_mood(self) -> SystemMood:
        """
        Determine the system's current mood based on performance metrics.

        Evaluates multiple system parameters to categorize
        the overall system performance state.

        Returns:
            SystemMood: Categorized system mood state.
        """
        try:
            metrics = self.get_system_metrics()

            # Stressed condition (high resource utilization)
            if (metrics['cpu_usage'] > self.thresholds['cpu']['high'] or
                metrics['memory_usage'] > self.thresholds['memory']['high'] or
                metrics['disk_usage'] > self.thresholds['disk']['high']):
                return SystemMood.STRESSED

            # Tired condition (prolonged uptime)
            if metrics['uptime_hours'] > 24:  # Over a day uptime
                return SystemMood.TIRED

            # Happy condition (low resource utilization)
            if (metrics['cpu_usage'] < self.thresholds['cpu']['moderate'] and
                metrics['memory_usage'] < self.thresholds['memory']['moderate'] and
                metrics['disk_usage'] < self.thresholds['disk']['moderate']):
                return SystemMood.HAPPY

            # Default to calm if no other conditions are met
            return SystemMood.CALM

        except SystemPerformanceException:
            # Fallback mood if metrics collection fails
            self.logger.warning("Defaulting to CALM mood due to metrics collection failure")
            return SystemMood.CALM

    def get_mood_details(self) -> Dict[str, Any]:
        """
        Generate a comprehensive mood report.

        Provides detailed insights into system performance
        and current mood state.

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
                'metrics': metrics
            }
        except SystemPerformanceException as e:
            self.logger.error(f"Mood details generation failed: {e}")
            return {
                'mood': 'unknown',
                'emoji': '❓',
                'ascii_art': 'System metrics unavailable',
                'metrics': {}
            }

def main():
    """
    Demonstration of SystemMoodAnalyzer functionality.
    """
    logging.basicConfig(level=logging.INFO)

    try:
        analyzer = SystemMoodAnalyzer()
        mood_report = analyzer.get_mood_details()

        print("System Mood Analysis Report:")
        print(f"Mood: {mood_report['mood'].capitalize()}")
        print(f"Emoji: {mood_report['emoji']}")
        print("\nASCII Art:")
        print(mood_report['ascii_art'])

        print("\nSystem Metrics:")
        for metric, value in mood_report['metrics'].items():
            print(f"{metric.replace('_', ' ').title()}: {value}")

    except Exception as e:
        logging.error(f"Mood analysis failed: {e}")

if __name__ == "__main__":
    main()
