from datetime import datetime
from typing import Optional
import logging

import pygsheets

logger = logging.getLogger(__name__)


class WorkSheet:
    def __init__(self, service_file: str, sheet_name: str, spread_sheet: str):
        sheet_auth = pygsheets.authorize(service_file=service_file)
        self.sheet = sheet_auth.open(sheet_name)
        self.worksheet = self.sheet.worksheet('title', spread_sheet)

    def mark_student(self,
                     student_id: Optional[str],
                     date: str = datetime.strftime(datetime.today(), '%d.%m.%Y')) -> Optional[None]:
        row = self.worksheet.find(student_id)[0].row
        col = self.worksheet.find(date)[0].col
        # if len(row) > 1 or len(col) > 1:
        #     raise Exception("There are so many elements in the list, so elements must be unique!!!")
        coord = (row, col)
        self.worksheet.update_value(coord, ' +')

    def create_spread_sheet(self, title: str) -> Optional[None]:
        """
        TODO: later
        :param title:
        :return:
        """
        self.sheet.add_worksheet(title=title)
        logger.info('Created!!!')