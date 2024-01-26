"""Common views attribution. Custom mixins."""
from typing import Any


class TitleMixin:
    """Common attribute title that all views with template have."""
    title = None

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
