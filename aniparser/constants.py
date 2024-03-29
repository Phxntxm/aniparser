import re

video_file_extensions = [
    "webm",
    "mkv",
    "flv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "drc",
    "gif",
    "gifv",
    "mng",
    "avi",
    "mts",
    "m2ts",
    "ts",
    "mov",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "rmvb",
    "viv",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "mpg",
    "mpeg",
    "m2v",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
]
subtitle_file_extensions = ["ass", "cmml", "lrc", "sami", "ttml", "srt", "ssa", "usf"]
audio_terms = [
    r"[25](\.[01])?(CH)",
    r"DTS(5\.1|-ES)*?",
    r"TRUEHD5\.1",
    r"AAC(X[234])*?",
    r"(E|E-)?AC-?3",
    r"FLAC(X[234])*?",
    "LOSSLESS",
    "MP3",
    "OGG",
    "VORBIS",
    r"DUAL[\- ]?AUDIO",
]
video_terms = [
    r"\d+(\.\d+)?FPS",
    r"(8|10)[\- ]?BITS*?",
    r"HI(10|444)P?P*?",
    r"[HX]\.?26[45]",
    r"HEVC2*?",
    r"DIVX[56]",
    r"AV[CI]",
    r"WMV[39]",
    "XVID",
    "RMVB",
    r"[HL]Q",
    r"[HS]D",
    r"multi-?subs",
]
source_terms = [
    r"BD(RIP)*?",
    r"BLU[\- ]?RAY",
    r"DVD-?([59]|R2J|RIP)*?",
    r"R2J?(DVD)*?(RIP)*?",
    r"HDTV(RIP)*?",
    r"HDTV",
    r"TV-?RIP",
    r"WEB-?(CAST|RIP)",
]
drop_terms = ["", "ONA", "OVA", "END", "FINAL", "SPECIAL"]
