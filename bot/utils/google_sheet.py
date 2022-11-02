from typing import Optional

import pygsheets
from datetime import datetime

sheet_auth = pygsheets.authorize(service_file='../../pysheets-demo-362905-50f5575b16f9.json')
# SAB degan sheetni och
sheet = sheet_auth.open('example_dev')
alphabets = ["A{}", "B{}", "C{}", "D{}", "E{}", "F{}",
             "G{}", "H{}", "I{}", "J{}", "K{}", "L{}",
             "M{}", "N{}", "O{}", "P{}", "Q{}", "R{}",
             "S{}", "T{}", "U{}", "V{}", "W{}", "X{}",
             "Y{}", "Z{}"]
# Shu SAB Sheetdagi student degan listni och
worksheet = sheet.worksheet('title', 'Python_G1')


def update_cell(pk: int, date: Optional[datetime] = None) -> Optional[None]:
    cell_coord = worksheet

update_cell(123456)

