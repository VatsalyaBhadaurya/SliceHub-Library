from fastapi import APIRouter
from typing import List

class RideSlice:
    def __init__(self):
        self.router = APIRouter(prefix="/ride")
        self._setup_routes()

    def _setup_routes(self):
        @self.router.get("/status")
        async def status():
            return {"status": "ride slice working"}

    def register(self, app):
        app.include_router(self.router)
