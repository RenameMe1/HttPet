import asyncio

from app.controllers.output import ExcelOutput
from app.service.general_report import GeneralReportService


async def main():
    excel = ExcelOutput("output.xlsx")
    report = GeneralReportService(output=excel)

    await report.generate()


if __name__ == "__main__":
    asyncio.run(main())
