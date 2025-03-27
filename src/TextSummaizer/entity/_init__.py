from dataclasses import dataclass, field
from pathlib import Path

@dataclass(frozen=True)
class DataIngetionConfig:
    root_dir:Path
    source_URL: str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list