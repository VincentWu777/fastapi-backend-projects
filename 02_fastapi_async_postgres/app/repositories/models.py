from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class UserRecord:
    """
    Repository-level user representation.

    This model represents persisted user data,
    independent of HTTP or validation concerns.
    """
    id: int
    email: str
    age: Optional[int]
