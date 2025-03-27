from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]  # Moves up two levels from `constant/`

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"

# Debugging: Print the resolved paths
print(f"🔍 CONFIG_FILE_PATH from constant: {CONFIG_FILE_PATH}")
print(f"🔍 PARAMS_FILE_PATH from constant: {PARAMS_FILE_PATH}")

# CONFIG_FILE_PATH = Path(__file__).parent.parent / "config" / "config.yaml"
# PARAMS_FILE_PATH=Path(__file__).parent.parent / "config" / "params.yaml"


