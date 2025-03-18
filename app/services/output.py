from __future__ import annotations

from pathlib import Path
from typing import Protocol, TYPE_CHECKING, final

from pandas import DataFrame, ExcelWriter

if TYPE_CHECKING:
    from typing import Any, Sequence, Hashable

__all__ = [
    "IOutputService",
    "ExcelOutputService",
]


class IOutputService(Protocol):
    def write(
        self,
        output_data: Any,
        *,
        page: str = "Sheet1",
        columns: Sequence[Hashable] | None = None,
    ) -> None: ...


@final
class ExcelOutputService:
    slots = [
        "excel_writer",
    ]

    def __init__(
        self,
        excel_file: Path,
    ) -> None:
        self.excel_file = excel_file

    def write(
        self,
        output_data: Any,
        *,
        page: str = "Sheet1",
        columns: Sequence[Hashable] | None = None,
    ) -> None:
        mode = "w"
        if_sheet_exists = None

        if Path(self.excel_file).is_file():
            mode = "a"
            if_sheet_exists = "replace"

        df = DataFrame(output_data, columns=columns)

        with ExcelWriter(
            self.excel_file,
            engine="openpyxl",
            mode=mode,
            if_sheet_exists=if_sheet_exists,
        ) as writer:
            df.to_excel(
                writer,
                sheet_name=page,
                index=False,
            )
