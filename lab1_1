import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_COLOR_INDEX

doc = docx.Document('modified_doc.docx')


def run_get_spacing(run):
    rPr = run._r.get_or_add_rPr()
    spacings = rPr.xpath("./w:spacing")
    return spacings


def run_get_scale(run):
    rPr = run._r.get_or_add_rPr()
    scale = rPr.xpath("./w:w")
    return scale


def main():
    kod = ''
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            font_color = run.font.color.rgb
            font_size = run.font.size
            font_highlight_color = run.font.highlight_color
            font_scale = run_get_scale(run)
            font_spacing = run_get_spacing(run)

            if (font_size.pt != 11.0):
                for i in range(len(run.text)):
                    kod += '1'
            else:
                for i in range(len(run.text)):
                    kod += '0'

    
    print(kod)
    #print(len(kod))



if __name__ == '__main__':
    main()

