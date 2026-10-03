"""
Task Manager FastAPI Application

A Python FastAPI app that integrates with both Foundry Agent Service and LangGraph agents.
"""

from .models import *
from .services import *
from .agents import *
from .routes import *

__version__ = "1.0.0"
