"""
AI_BABA RBAC Module

Enterprise Role-Based Access Control (RBAC) package.

This package provides:s
- Role management
- Permission management
- Authorization services
- RBAC API endpoints
- Repository layer
- Business services
- Dependency registration

The implementation is designed to integrate with the
existing AI_BABA IAM and Authentication modules.
"""

from app.modules.rbac.api import router

__all__ = [
    "router",
]