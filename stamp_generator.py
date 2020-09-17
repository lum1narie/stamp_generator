# -*- encoding:utf-8 -*-

import sys
import os

import cairosvg
import unicodedata


def gen_stamp(str, font_family=None,
              stroke="#FF8000", fill="#8030FF",
              size=500, bg_color=None,
              weight="normal",stroke_ratio=0.05):
    SVG_START = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{size}px" height="{size}px" viewBox="0 0 {size} {size}">'
    SVG_END = '</svg>'
    BG = '<rect x="0" y="0" width="{size}" height="{size}" style="{bg_style}"/>'
    BG_STYLE = '{fill}{fill_opacity}'
    BG_FILL = 'fill:{fill}'
    BG_OPACITY = 'fill_opacity:{opacity}'
    TEXT_START = '<text y="{y}" style="{text_style}" stroke-width="{stroke_width}">'
    TEXT_STYLE = '{font_family}font-size: {font_size}px; stroke: {stroke}; fill: {fill}; font-weight: {weight};'
    FONT_FAMILY = 'font-family: {font_family}; '
    TEXT_END = '</text>'
    TSPAN_START = '<tspan x="50%" dy="2ex" text-anchor="middle" alignment-baseline="central">'
    TSPAN_END = '</tspan>'

    bg_style_dict = {
        "fill": BG_FILL.format(fill=bg_color) if bg_color is not None else "",
        "fill_opacity": "" if bg_color is not None else BG_OPACITY.format(opacity="1")
    }
    bg_style_sentence = BG_STYLE.format(**bg_style_dict)

    font_family_sentece = FONT_FAMILY.format(font_family=(
        font_family if font_family is not None else ""))

    str_list = str.split("\n")
    tspans = "\n".join([TSPAN_START + s + TSPAN_END
                        for s in str_list])
    max_unilen = max([sum([2 if unicodedata.east_asian_width(
        c) in "FWA" else 1 for c in s]) for s in str_list])
    col_num = len(str_list)

    font_size = int(size / max(max_unilen / 2, col_num) * 0.9)
    y_offset = size / 2 - font_size * (col_num + 1) / 2
    stroke_width = font_size * stroke_ratio

    svg_sentence = (
        SVG_START.format(size=size) + "\n" +
        BG.format(size=size, bg_style=bg_style_sentence) + "\n" +
        TEXT_START.format(
            y=y_offset,
            stroke_width=stroke_width,
            text_style=TEXT_STYLE.format(
                font_family=font_family_sentece, font_size=font_size, stroke=stroke, fill=fill, weight=weight)) + "\n" +
        tspans + "\n" +
        TEXT_END + "\n" +
        SVG_END
    )
    return svg_sentence


if __name__ == "__main__":
    str = ""
    read_filename = sys.argv[1]
    with open(read_filename, "r", encoding="utf-8") as f:
        str = f.read()

    out_svg_filename = os.path.splitext(read_filename)[0] + ".svg"
    with open(out_svg_filename, "w", encoding="utf-8") as f:
        f.write(gen_stamp(
            str, font_family="Mgen+ 2p Bold",
            stroke="#FF8000", fill="#8030FF",
            bg_color="#000000"))

    out_png_filename = os.path.splitext(read_filename)[0] + ".png"
    cairosvg.svg2png(url=out_svg_filename, write_to=out_png_filename)
