import xlrd
from . import video_down
from . import split


def start_training():
    file_loc = "sv.xlsx"
    workbook = xlrd.open_workbook(file_loc)
    sh = workbook.sheet_by_index(0)
    no_ro = sh.nrows

    for rol in range(1, no_ro):
        a = str(sh.cell_value(rol, 0)) + ' ' + str(sh.cell_value(rol, 1))
        b = str(sh.cell_value(rol, 2))
        video_down.dwn_video(b, a)
        split.split(a, 'videos/' + a + '.mp4')
