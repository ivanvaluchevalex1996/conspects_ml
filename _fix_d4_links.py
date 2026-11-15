# -*- coding: utf-8 -*-
import re
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(r"c:\Users\HUAWEI\Desktop\все мои конспекты в ynote")
DL = ROOT / "d.Машинное обучение" / "d.4 Deep Learning"
D33_DIR = "d.4.33 Нейрон и полносвязная сеть"
D33_FILE = "d.4.33 Нейрон и полносвязная сеть.md"
CANON = quote(f"{D33_DIR}/{D33_FILE}", safe="/")
ENC_FILE = quote(D33_FILE, safe="")
D34_DIR = "d.4.34 Функции активации"
D34_11 = "d.4.1.1 Затухающий градиент — почему ReLU в скрытых, а не sigmoid.md"
ENC_D34_11 = quote(D34_11, safe="")
REL_D34_11_FROM_D33 = f"../{quote(D34_DIR, safe='')}/{ENC_D34_11}"
REL_D33_FROM_D34 = f"../{CANON}"
OLD_D41_MD = "../d.4.1%20%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B5%D1%82%D0%B8.md"

OLD_PATHS = [
    f"../{D33_DIR}/{ENC_FILE}",
    f"../../{D33_DIR}/{ENC_FILE}",
    f"../../../{D33_DIR}/{ENC_FILE}",
    f"../{D33_DIR}/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../../{D33_DIR}/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../../../{D33_DIR}/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../{D33_DIR}/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../../{D33_DIR}/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    "d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../../d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
    f"../../d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/{ENC_FILE}",
    f"d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C/d.4.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
]

REL_PREFIX = {2: "../", 3: "../../", 4: "../../../"}


def rel_canon(prefix: str) -> str:
    return prefix + CANON


def fix_text(s: str) -> str:
    # сломанный markdown после массовой замены: ](url)(url2)
    s = re.sub(r"(\]\([^)]+\.md)\)\([^)]+\)", r"\1)", s)

    for old in OLD_PATHS:
        if old.startswith("../"):
            depth = old.count("../")
            s = s.replace(old, rel_canon(REL_PREFIX.get(depth, "../")))
        else:
            s = s.replace(old, CANON)

    s = s.replace("[`d.4.1` §", "[`d.4.33` §")
    s = s.replace("[`d.4.1 … .md`]", f"[`d.4.33 … .md`]({rel_canon('../../')})")
    s = s.replace("Конспект: [`d.4.1`](../../", "Конспект: [`d.4.33`](../../")
    s = s.replace("Теория: [`d.4.1 … .md`]", "Теория: [`d.4.33 … .md`]")
    s = s.replace("# Практика d.4.1 ·", "# Практика d.4.33 ·")
    s = s.replace("§11 в `d.4.1 …`", f"§11 в [`d.4.33`](../{CANON})")
    s = s.replace(
        "[`../d.4.33/…/d.4.1 … .md`]",
        f"[`d.4.33 …`](../{CANON})",
    )
    s = s.replace(
        "Дальше: [d.4.35](./d.4.35%20Backpropagation.md).",
        "Дальше: [d.4.35](../d.4.35%20Backpropagation/d.4.35%20Backpropagation.md).",
    )
    s = s.replace(
        "(d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md)",
        f"(../{CANON})",
    )
    s = s.replace("**handbook_gl34/**", "**practice/**")
    s = s.replace(OLD_D41_MD, f"../{CANON}")
    # из practice/d.4.34: короче, чем ../../d.4.34.../file
    s = re.sub(
        rf"\]\(\.\./\.\./{re.escape(quote(D34_DIR, safe=''))}/{re.escape(ENC_D34_11)}\)",
        f"](../{ENC_D34_11})",
        s,
    )
    # ipynb в d.4.33/practice: неверное имя файла (без префикса d.4.33)
    s = s.replace(
        "../../d.4.33%20Нейрон%20%D0%B8%20%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D1%81%D0%B2%D1%8F%D0%B7%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B5%D1%82%D1%8C.md",
        f"../../{ENC_FILE}",
    )
    d36 = quote("d.4.36 Оптимизация и обучение в DL", safe="")
    s = s.replace("../../d.4.37%20", "../d.4.37%20")
    enc_d36_main = quote("d.4.36 Оптимизация и обучение в DL.md", safe="")
    s = s.replace(
        "Дальше: [d.4.36](./d.4.36%20%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20DL.md).",
        f"Дальше: [d.4.36](../{d36}/{enc_d36_main}).",
    )
    return s


def fix_text_d433(s: str) -> str:
    s = fix_text(s)
    s = re.sub(
        r"\]\(d\.4\.1\.1%20[^)]+\)",
        lambda m: f"]({REL_D34_11_FROM_D33})",
        s,
    )
    s = re.sub(
        r"\(d\.4\.1\.1%20[^)]+\)",
        lambda m: f"({REL_D34_11_FROM_D33})",
        s,
    )
    return s


def fix_text_d437(s: str) -> str:
    s = fix_text(s)
    d37 = quote("d.4.37 Регуляризация в DL", safe="")
    s = s.replace(f"](../{d37}/d.4.3", "](./d.4.3")
    s = s.replace(f"](../{d37}/practice/", "](./practice/")
    return s


def fix_text_d436(s: str) -> str:
    s = fix_text(s)
    d36 = quote("d.4.36 Оптимизация и обучение в DL", safe="")
    s = s.replace(f"](../{d36}/practice/", "](./practice/")
    return s


def fix_text_d434_child(s: str) -> str:
    s = fix_text(s)
    s = re.sub(
        r"\]\(d\.4\.33%20[^)]+\)",
        lambda m: f"]({REL_D33_FROM_D34})",
        s,
    )
    s = re.sub(
        r"\(d\.4\.33%20%D0%9D%D0%B5%D0%B9%D1%80%D0%BE%D0%BD[^)]+\)",
        lambda m: f"({REL_D33_FROM_D34})",
        s,
    )
    return s


n = 0
for base in (DL, ROOT):
    if not base.exists():
        continue
    for p in base.rglob("*"):
        if p.suffix.lower() not in {".md", ".ipynb"}:
            continue
        if "_fix_" in p.name:
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except Exception:
            continue
        rel = p.relative_to(ROOT)
        if D33_DIR in str(rel) and p.name == D33_FILE:
            u = fix_text_d433(t)
        elif D33_DIR in str(rel):
            u = fix_text_d433(t)
        elif D34_DIR in str(rel):
            u = fix_text_d434_child(t)
        elif "d.4.37 Регуляризация в DL" in str(rel):
            u = fix_text_d437(t)
        elif "d.4.36 Оптимизация и обучение в DL" in str(rel):
            u = fix_text_d436(t)
        else:
            u = fix_text(t)
        if u != t:
            p.write_text(u, encoding="utf-8")
            n += 1

broken = []
link_re = re.compile(r"\]\(([^)#]+)(#[^)]*)?\)")


def check_links(p: Path, text: str) -> None:
    for m in link_re.finditer(text):
        href = m.group(1)
        if href.startswith(("http:", "https:", "mailto:")):
            continue
        if href.startswith("#"):
            continue
        target = (p.parent / unquote(href.split("#")[0])).resolve()
        if not target.exists():
            broken.append((str(p.relative_to(ROOT)), href))


for base in (DL,):
    for p in base.rglob("*"):
        if p.suffix.lower() not in {".md", ".ipynb"}:
            continue
        if "_fix_" in p.name:
            continue
        try:
            check_links(p, p.read_text(encoding="utf-8"))
        except Exception:
            pass

print("CANON:", CANON)
print("updated", n)
if broken:
    print("BROKEN", len(broken))
    for row in broken[:40]:
        print(" ", row[0], "->", row[1][:120])
else:
    print("BROKEN 0")