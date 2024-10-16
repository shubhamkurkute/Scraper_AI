from pydantic import BaseModel
from typing import Optional, List


class TableAttributes(BaseModel):
    class_: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None


class TableData(BaseModel):
    table_no: int
    row_index: int
    css_selector: str
    attrs: TableAttributes
    head_row_names: List[str]
