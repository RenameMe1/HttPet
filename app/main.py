import asyncio

from app.controllers import ExcelController
from app.service.general_report import GeneralReportService

__all__ = ("main",)


async def main():
    excel = ExcelController("output.xlsx")
    report = GeneralReportService(output=excel)

    await report.generate()


if __name__ == "__main__":
    asyncio.run(main())
