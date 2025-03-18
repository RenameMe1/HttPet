from __future__ import annotations

from pandas import DataFrame

from typing import Protocol, TYPE_CHECKING, final

if TYPE_CHECKING:
    from typing import Any, Sequence, Hashable
    from pandas._typing import FilePath, WriteExcelBuffer, ExcelWriter

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
    ): ...


@final
class ExcelController:
    slots = [
        "excel_writer",
    ]

    def __init__(
        self,
        excel_writer: FilePath | WriteExcelBuffer | ExcelWriter,
    ) -> None:
        self.excel_writer = excel_writer

    def write(
        self,
        output_data: Any,
        *,
        page: str = "Sheet1",
        columns: Sequence[Hashable] | None = None,
    ) -> None:
        df = DataFrame(output_data, columns=columns)

        df.to_excel(
            excel_writer=self.excel_writer,
            sheet_name=page,
        )
