"""Import all routers and add them to routers_list."""
from .simple_menu import main_router

routers_list = [
    main_router,
]

__all__ = [
    "routers_list",
]
