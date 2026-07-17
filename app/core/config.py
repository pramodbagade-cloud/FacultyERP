"""
FacultyERP
Configuration
-------------

Central application configuration.
"""

from pathlib import Path


class AppConfig:
    """Application configuration."""

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    APP_NAME = "FacultyERP"
    VERSION = "1.0.0"

    # ------------------------------------------------------------------
    # Window
    # ------------------------------------------------------------------
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    MIN_WIDTH = 1100
    MIN_HEIGHT = 650

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------
    ROOT_DIR = Path.cwd()

    DATABASE_DIR = ROOT_DIR / "database"
    DATABASE_FILE = DATABASE_DIR / "facultyerp.db"

    LOG_DIR = ROOT_DIR / "logs"

    ASSET_DIR = ROOT_DIR / "app" / "assets"

    ICON_DIR = ASSET_DIR / "icons"

    IMAGE_DIR = ASSET_DIR / "images"

    THEME_DIR = ASSET_DIR / "themes"