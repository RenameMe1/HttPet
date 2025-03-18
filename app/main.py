import asyncio

from pathlib import Path

from app.services import ExcelOutputService
from app.controllers import GeneralReportController

__all__ = ("main",)


async def main():
    excel = ExcelOutputService(Path("output.xlsx"))
    report = GeneralReportController(output=excel)

    await report.generate()


if __name__ == "__main__":
    asyncio.run(main())
