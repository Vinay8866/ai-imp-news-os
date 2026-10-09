"""
AI IMP NEWS OS
Configuration Settings
Version: v3.4 (Final - All Aliases + FreeLLMAPI)
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ============================================
# PATHS
# ============================================
ROOT_DIR = Path(__file__).resolve().parents[3]
BASE_DIR = Path(__file__).resolve().parents[2]

# Database Path
DATABASE_PATH = ROOT_DIR / "database" / "news.db"
DB_PATH = DATABASE_PATH

# Media Paths
MEDIA_DIR = ROOT_DIR / "media"
IMAGES_DIR = MEDIA_DIR / "images"
THUMBNAILS_DIR = MEDIA_DIR / "thumbnails"

# Docs & Content Paths
DOCS_DIR = ROOT_DIR / "docs"
EVIDENCE_DIR = DOCS_DIR / "evidence"
CONTENT_DIR = DOCS_DIR / "content"
PUBLISHED_DIR = DOCS_DIR / "published"

# Logs Path
LOGS_DIR = ROOT_DIR / "logs"

# Ensure all directories exist automatically
for directory in [MEDIA_DIR, IMAGES_DIR, THUMBNAILS_DIR, DOCS_DIR, EVIDENCE_DIR, CONTENT_DIR, PUBLISHED_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ============================================
# GEMINI API & ALIASES
# ============================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
GEMINI_MODEL_TEXT = GEMINI_MODEL
GEMINI_MODEL_VISION = "gemini-1.5-flash"

# ============================================
# FREELLMAPI (Primary AI Engine)
# ============================================
FREELLMAPI_BASE_URL = os.getenv("FREELLMAPI_BASE_URL", "http://localhost:3001/v1")
FREELLMAPI_API_KEY = os.getenv("FREELLMAPI_API_KEY", "")
FREELLMAPI_MODEL = os.getenv("FREELLMAPI_MODEL", "auto")

# ============================================
# IMAGE GENERATION
# ============================================
POLLINATIONS_URL = os.getenv("POLLINATIONS_URL", "https://image.pollinations.ai/prompt")

# ============================================
# PIPELINE SETTINGS & QUALITY THRESHOLDS (All Aliases)
# ============================================
TOP_NEWS_COUNT = 6
MAX_RAW_NEWS = 50
MAX_RSS_ARTICLES = 50
APP_PORT = 8000
HOST = "127.0.0.1"

# Quality Thresholds (multiple names for compatibility)
QUALITY_PUBLISH_THRESHOLD = 85
QUALITY_REWRITE_THRESHOLD = 70
PUBLISH_QUALITY_THRESHOLD = 85
REWRITE_QUALITY_THRESHOLD = 70
QUALITY_THRESHOLD = 85

# ============================================
# HELPER FUNCTIONS
# ============================================
def is_freellmapi_available() -> bool:
    """Check if FreeLLMAPI key is configured."""
    if not FREELLMAPI_API_KEY:
        return False
    if "your-unified-key" in FREELLMAPI_API_KEY.lower():
        return False
    return True

def is_gemini_available() -> bool:
    """Check if Gemini key is configured."""
    if not GEMINI_API_KEY:
        return False
    if "your_existing" in GEMINI_API_KEY.lower():
        return False
    return True

def get_ai_status() -> str:
    """Return current AI engine status."""
    if is_freellmapi_available():
        return "FreeLLMAPI (Primary) + Gemini (Backup)"
    elif is_gemini_available():
        return "Gemini Only (FreeLLMAPI not configured)"
    else:
        return "Template Only (No AI keys configured)"

if __name__ == "__main__":
    print("=" * 60)
    print("AI IMP NEWS OS - Settings Loaded Successfully")
    print("=" * 60)
    print(f"ROOT_DIR         : {ROOT_DIR}")
    print(f"DB_PATH          : {DB_PATH}")
    print(f"FreeLLMAPI URL   : {FREELLMAPI_BASE_URL}")
    print(f"FreeLLMAPI Key   : {'SET' if is_freellmapi_available() else 'NOT SET'}")
    print(f"Gemini Key       : {'SET' if is_gemini_available() else 'NOT SET'}")
    print(f"AI Status        : {get_ai_status()}")
    print("=" * 60)