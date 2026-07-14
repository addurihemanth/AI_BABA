"""
AI_BABA Verification Engine Configuration
"""

from pathlib import Path


class VerifierConfig:

    PROJECT_NAME = "AI_BABA"

    VERSION = "1.0.0"

    ROOT_FILES = [
        "README.md",
        "pyproject.toml",
        ".gitignore",
    ]

    CORE_DIRECTORIES = [
        "app",
        "tests",
        "docs",
    ]

    PYTHON_EXTENSIONS = [
        ".py"
    ]


    def __init__(
        self,
        project_root: Path
    ):

        self.project_root = Path(project_root)


    def get_report_path(self):

       return (
         self.project_root
        /
        "verification_report.json"
    )