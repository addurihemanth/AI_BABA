"""
AI_BABA Verification Engine

Single command launcher for project health verification.

Usage:
    python -m tools.verifier.main

Responsibilities:
    - Load configuration
    - Execute verification engine
    - Display final result
"""

from pathlib import Path
import sys

from .engine import VerificationEngine

PROJECT_ROOT = Path(__file__).resolve().parents[2]




def print_banner() -> None:
    print("=" * 70)
    print(" AI_BABA ENTERPRISE VERIFICATION ENGINE")
    print("=" * 70)
    print(f" Project Root: {PROJECT_ROOT}")
    print()


def main() -> int:
    print_banner()

    engine = VerificationEngine(
        project_root=PROJECT_ROOT
    )

    result = engine.run()

    print()
    print("=" * 70)

    if result.success:
        print("✅ VERIFICATION PASSED")
    else:
        print("❌ VERIFICATION FAILED")

    print("=" * 70)

    print()
    print("Summary:")
    print(f" Checks Executed : {result.total_checks}")
    print(f" Passed          : {result.passed}")
    print(f" Failed          : {result.failed}")

    if result.errors:
        print()
        print("Errors:")
        for error in result.errors:
            print(f" - {error}")

    return 0 if result.success else 1


if __name__ == "__main__":
    sys.exit(main())