from __future__ import annotations

from pandas import DataFrame, ExcelWriter

from typing import Protocol, TYPE_CHECKING, final

if TYPE_CHECKING:
    from typing import Any, Sequence, Hashable
    from pathlib import Path

__all__ = [
    "IOutputController",
    "ExcelController",
]


class IOutputController(Protocol):
    def __init__(self): ...

    def write(
        self,
        output_data: Any,
        *,
        page: str = "Sheet1",
        columns: Sequence[Hashable] | None = None,
    ) -> None: ...


@final
class ExcelController:
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
        df = DataFrame(output_data, columns=columns)

        with ExcelWriter(
            self.excel_file,
            engine="openpyxl",
            mode="a",
            if_sheet_exists="replace",
        ) as writer:
            df.to_excel(
                writer,
                sheet_name=page,
                index=False,
            )
