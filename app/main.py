import asyncio

from pathlib import Path

from app.controllers import ExcelController
from app.service.general_report import GeneralReportService

__all__ = ("main",)


async def main():
    excel = ExcelController(Path("output.xlsx"))
    report = GeneralReportService(output=excel)

    await report.generate()


if __name__ == "__main__":
    asyncio.run(main())
