from dataclasses import dataclass
from typing import Optional, Dict, Any


class Tasks:
    def __init__(self, title: str, description: str, status: str = 'pending'):
        self.title = title
        self.description = description
        self.status = status

    @dataclass
    class TaskEntity:
        id: Optional[int] = None
        title: str = ''
        description: Optional[str] = None
        status: str = 'pending'

        def to_db_tuple(self):
            """Return tuple suitable for INSERT/UPDATE parameter order."""
            return (self.title, self.description, self.status)

        def to_dict(self) -> Dict[str, Any]:
            return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'status': self.status,
            }

        @classmethod
        def from_row(cls, row: Dict[str, Any]):
            """Create a TaskEntity from a DB row dict (keys: id, title, description, status)."""
            return cls(
                id=row.get('id'),
                title=row.get('title') or '',
                description=row.get('description'),
                status=row.get('status') or 'pending'
            )
