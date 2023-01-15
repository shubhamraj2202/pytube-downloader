"""Pydantic Model for Youtube downloader"""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ValidationError, root_validator
from pyhelper.misc import _map

from ytube.custom_exeptions import InvalidUrl


class BaseYtd(BaseModel):
    """Base Model for Youtube Downloader"""

    errors: Optional[List[Any]] = []
    raise_errors: Optional[bool] = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs, raw=kwargs)

    @root_validator()
    @classmethod
    def error_collector(cls, field_values: Dict[str, Any]):
        """Error Collector"""
        _map(
            lambda f: getattr(cls, f)(field_values)
            if f.startswith("validate_")
            else None,
            dir(cls),
        )
        if field_values["raise_errors"] and field_values["errors"]:
            raise ValidationError(field_values["errors"], cls)

        return field_values

    @classmethod
    def validate_link(cls, field_values):
        """Validate URL Link"""
        attr_name = "link"
        link: str = field_values[attr_name]
        if not link.startswith("https://"):
            err = InvalidUrl("Invalid Link"), cls
            field_values["errors"].append(err)


class Url(BaseYtd):
    """URL Pydantic Model"""

    link: str
