from fastapi import FastAPI
from typing import List, Type


class SliceHub:
    def __init__(self, title: str = "SliceHub App"):
        self._app = FastAPI(title=title)
        self._slices: List = []
        self._auth_enabled = False
        self._db_enabled = False

    def register_slice(self, slice_obj: object):
        """Register a slice which provides routes and models."""
        if hasattr(slice_obj, "register"):
            slice_obj.register(self._app)
            self._slices.append(slice_obj)
        else:
            raise ValueError("Slice must implement register(app: FastAPI)")

    def enable_auth(self, **kwargs):
        """Enable authentication (JWT) placeholder."""
        self._auth_enabled = True
        # future: configure JWT here

    def enable_database(self, url: str):
        """Enable database layer (SQLAlchemy)"""
        self._db_enabled = True
        # placeholder: create engine, session etc.

    def get_app(self) -> FastAPI:
        return self._app
