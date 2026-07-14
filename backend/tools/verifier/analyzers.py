"""
AI_BABA Verification Engine - Optimized Analyzers

Enterprise project analysis layer.

Features:
    - Fast filesystem scanning
    - Excludes virtual environments
    - Excludes dependency folders
    - Python syntax validation
    - Configuration checks
    - Basic security checks
    - Architecture detection
"""

from dataclasses import dataclass, field
from pathlib import Path
import ast
import os



@dataclass
class AnalyzerReport:

    name: str

    success: bool

    message: str

    details: list[str] = field(
        default_factory=list
    )



class BaseAnalyzer:


    EXCLUDED_DIRECTORIES = {

        ".git",

        ".venv",

        "venv",

        "env",

        "__pycache__",

        ".pytest_cache",

        ".mypy_cache",

        "node_modules",

        "dist",

        "build",

        ".idea",

        ".vscode",

    }



    def __init__(
        self,
        project_root: Path
    ):

        self.project_root = Path(
            project_root
        )



    def iter_python_files(self):

        """
        Fast recursive Python file scanner.

        Uses directory pruning so excluded
        folders are never entered.
        """


        for root, directories, files in os.walk(
            self.project_root
        ):


            directories[:] = [

                directory

                for directory in directories

                if directory not in self.EXCLUDED_DIRECTORIES

            ]


            for file in files:


                if file.endswith(".py"):

                    yield Path(root) / file





class ProjectAnalyzer(BaseAnalyzer):


    def run_all(self):

        return [

            self.analyze_structure(),

            self.analyze_python_files(),

            self.analyze_configuration(),

            self.analyze_security(),

        ]



    def analyze_structure(self):


        required = [

            "app",

            "tests",

            "docs",

        ]


        missing = []


        for folder in required:


            if not (
                self.project_root / folder
            ).exists():

                missing.append(folder)



        if missing:


            return AnalyzerReport(

                name="Project Structure",

                success=False,

                message="Missing required directories",

                details=missing

            )


        return AnalyzerReport(

            name="Project Structure",

            success=True,

            message="Project structure validated"

        )





    def analyze_python_files(self):


        checked = 0

        errors = []


        for file in self.iter_python_files():


            checked += 1


            try:


                source = file.read_text(
                    encoding="utf-8"
                )


                ast.parse(source)



            except Exception as error:


                errors.append(

                    f"{file}: {error}"

                )



            if checked >= 5000:

                break



        if errors:


            return AnalyzerReport(

                name="Python Syntax",

                success=False,

                message="Python syntax errors detected",

                details=errors

            )



        return AnalyzerReport(

            name="Python Syntax",

            success=True,

            message=f"{checked} Python files verified"

        )





    def analyze_configuration(self):


        config_files = [

            ".env",

            "requirements.txt",

            "pyproject.toml",

        ]


        found = []


        for file in config_files:


            if (
                self.project_root / file
            ).exists():

                found.append(file)



        return AnalyzerReport(

            name="Configuration",

            success=bool(found),

            message=(

                "Configuration files found"

                if found

                else

                "Configuration files missing"

            ),

            details=found

        )





    def analyze_security(self):


        suspicious_patterns = [

            "password=",

            "secret=",

            "api_key=",

            "apikey=",

        ]


        warnings = []



        for file in self.iter_python_files():


            try:


                content = file.read_text(
                    encoding="utf-8"
                ).lower()



                for pattern in suspicious_patterns:


                    if pattern in content:


                        warnings.append(

                            f"{file}: contains {pattern}"

                        )



            except Exception:


                continue



        return AnalyzerReport(

            name="Security Scan",

            success=not warnings,

            message=(

                "No obvious secrets detected"

                if not warnings

                else

                "Potential secrets detected"

            ),

            details=warnings

        )







class DependencyAnalyzer(BaseAnalyzer):


    def check_requirements(self):


        requirements = (

            self.project_root

            /

            "requirements.txt"

        )



        if not requirements.exists():


            return AnalyzerReport(

                name="Dependencies",

                success=False,

                message="requirements.txt missing"

            )



        packages = [

            line.strip()

            for line in requirements.read_text(
                encoding="utf-8"
            ).splitlines()

            if line.strip()

            and not line.startswith("#")

        ]



        return AnalyzerReport(

            name="Dependencies",

            success=True,

            message=f"{len(packages)} dependencies registered",

            details=packages

        )







class ArchitectureAnalyzer(BaseAnalyzer):


    def detect_modules(self):


        app_folder = (

            self.project_root

            /

            "app"

        )


        if not app_folder.exists():

            return []



        return [

            item.name

            for item in app_folder.iterdir()

            if item.is_dir()

        ]





    def report(self):


        modules = self.detect_modules()



        return AnalyzerReport(

            name="Architecture",

            success=True,

            message=f"{len(modules)} modules detected",

            details=modules

        )