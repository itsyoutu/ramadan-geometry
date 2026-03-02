from pptx import Presentation
import os

def get_slide_count(pptx_path):
    prs = Presentation(pptx_path)
    return len(prs.slides)

if __name__ == "__main__":
    pptx_path = "/home/ubuntu/ramadan-geometry/Engineering_Ramadan.pptx"
    count = get_slide_count(pptx_path)
    print(f"SLIDE_COUNT:{count}")
