"""
AI_BABA Verification Engine Core

Enterprise verification controller.

Responsibilities:
    - Project structure validation
    - Required file validation
    - Dependency verification
    - Advanced analyzer execution
    - AI recommendation generation
    - Verification report generation

Designed as the central verification engine
for the complete AI_BABA platform.
"""

from pathlib import Path
from dataclasses import dataclass, field
import importlib.util


from .config import VerifierConfig
from .analyzers import (
    ProjectAnalyzer,
    DependencyAnalyzer,
    ArchitectureAnalyzer,
)

from .ai_advisor import AIAdvisor
from .reporter import VerificationReporter



@dataclass
class VerificationResult:

    success: bool = True

    total_checks: int = 0

    passed: int = 0

    failed: int = 0

    errors: list[str] = field(
        default_factory=list
    )



class VerificationEngine:


    REQUIRED_DIRECTORIES = [

        "app",

        "tests",

        "docs",

    ]


    REQUIRED_FILES = [
     "requirements.txt",
    ]


    REQUIRED_PACKAGES = [

        "fastapi",

        "sqlalchemy",

        "pydantic",

    ]



    def __init__(
        self,
        project_root: Path
    ):

        self.project_root = Path(
            project_root
        )

        self.result = VerificationResult()



    def run(self):

        self.check_directories()

        self.check_files()

        self.check_dependencies()


        analyzer_reports = []


        project_analyzer = ProjectAnalyzer(
            self.project_root
        )


        analyzer_reports.extend(

            project_analyzer.run_all()

        )


        dependency_report = (
            DependencyAnalyzer(
                self.project_root
            )
            .check_requirements()
        )


        analyzer_reports.append(
            dependency_report
        )


        architecture_report = (
            ArchitectureAnalyzer(
                self.project_root
            )
            .report()
        )


        analyzer_reports.append(
            architecture_report
        )


        advisor = AIAdvisor()


        recommendations = (
            advisor.generate_advice(
                analyzer_reports
            )
        )


        report_file = (
            VerifierConfig(
                self.project_root
            )
            .get_report_path()
        )


        VerificationReporter().create_report(

            self.result,

            analyzer_reports,

            report_file

        )


        return self.result



    def check_directories(self):

        for directory in self.REQUIRED_DIRECTORIES:


            path = (
                self.project_root
                /
                directory
            )


            if path.exists():


                self.success()


            else:


                self.failure(

                    f"Missing directory: {directory}"

                )



    def check_files(self):

        for file_name in self.REQUIRED_FILES:


            path = (

                self.project_root
                /
                file_name

            )


            if path.exists():


                self.success()


            else:


                self.failure(

                    f"Missing file: {file_name}"

                )



    def check_dependencies(self):

        for package in self.REQUIRED_PACKAGES:


            if importlib.util.find_spec(
                package
            ):


                self.success()


            else:


                self.failure(

                    f"Missing package: {package}"

                )



    def success(self):

        self.result.total_checks += 1

        self.result.passed += 1



    def failure(
        self,
        message: str
    ):

        self.result.total_checks += 1

        self.result.failed += 1

        self.result.success = False

        self.result.errors.append(
            message
        )