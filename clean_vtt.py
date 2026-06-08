import re, sys, pathlib

def clean(vtt_text):
    lines = vtt_text.splitlines()
    out = []
    last = None
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s == "WEBVTT" or s.startswith("Kind:") or s.startswith("Language:"):
            continue
        if "-->" in s:           # cue timing line
            continue
        if s == " " or s == "&nbsp;":
            continue
        # strip inline timestamp tags <00:00:02.320> and <c>...</c> tags
        s = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", "", s)
        s = re.sub(r"</?c[^>]*>", "", s)
        s = s.replace(" ", " ")
        s = re.sub(r"\s+", " ", s).strip()
        if not s:
            continue
        if s == last:            # drop rolling-caption duplicate
            continue
        out.append(s)
        last = s
    text = " ".join(out)
    text = re.sub(r"\s+", " ", text).strip()
    return text

src = pathlib.Path("transcripts")
dst = pathlib.Path("transcripts/clean")
dst.mkdir(exist_ok=True)
for f in sorted(src.glob("*.en-orig.vtt")):
    txt = clean(f.read_text(encoding="utf-8"))
    name = f.name.replace(".en-orig.vtt", ".txt")
    (dst / name).write_text(txt, encoding="utf-8")
    print(f"{name}: {len(txt.split())} words")
