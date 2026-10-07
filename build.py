#!/usr/bin/env python3
"""Genera il libro in dist/: PDF di stampa, EPUB e DOCX (il formato di stampa è in libro/metadata.yaml).

Uso:
    python build.py            # tutti i formati
    python build.py pdf epub   # solo i formati indicati
    python build.py stato      # parole e segnaposto [DA SCRIVERE] per capitolo
"""
import re
import subprocess
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent
CAPITOLI = sorted((RADICE / "libro" / "capitoli").glob("*.md"))
METADATI = RADICE / "libro" / "metadata.yaml"
COPERTINA = RADICE / "libro" / "copertina.jpg"
TEMPLATE = RADICE / "template"
DIST = RADICE / "dist"
NOME = "ia-in-comune"

SEGNAPOSTO = re.compile(r"\[DA SCRIVERE\]")


def pandoc(*argomenti):
    # --file-scope: ogni capitolo ha la sua numerazione delle note ([^1], [^2]...)
    # e pandoc la tiene separata invece di confonderla tra un file e l'altro.
    comando = ["pandoc", "--file-scope", "--metadata-file", METADATI, *CAPITOLI, *argomenti]
    subprocess.run([str(a) for a in comando], check=True)


def pdf():
    import typst
    from pypdf import PdfReader

    sorgente = DIST / f"{NOME}.typ"
    uscita = DIST / f"{NOME}-stampa.pdf"
    pandoc(
        "-t", "typst",
        "--template", TEMPLATE / "libro.typst",
        "--lua-filter", TEMPLATE / "senza-numero.lua",
        "-o", sorgente,
    )
    typst.compile(str(sorgente), output=str(uscita))
    pagine = len(PdfReader(uscita).pages)
    print(f"PDF di stampa: {uscita.relative_to(RADICE)} ({pagine} pagine)")


def epub():
    uscita = DIST / f"{NOME}.epub"
    extra = ["--epub-cover-image", COPERTINA] if COPERTINA.exists() else []
    pandoc(
        "-t", "epub3",
        "--toc", "--toc-depth=2",
        "--number-sections",
        "--split-level=1",
        "--css", TEMPLATE / "epub.css",
        *extra,
        "-o", uscita,
    )
    print(f"EPUB: {uscita.relative_to(RADICE)}")


def docx():
    uscita = DIST / f"{NOME}.docx"
    pandoc("-t", "docx", "--toc", "-o", uscita)
    print(f"DOCX: {uscita.relative_to(RADICE)}")


def stato():
    totale_parole = totale_segnaposto = 0
    print(f"{'Capitolo':<42} {'Parole':>7} {'Da scrivere':>12}")
    for capitolo in CAPITOLI:
        testo = capitolo.read_text(encoding="utf-8")
        parole = len(re.findall(r"\w+", SEGNAPOSTO.sub("", testo)))
        aperti = len(SEGNAPOSTO.findall(testo))
        totale_parole += parole
        totale_segnaposto += aperti
        print(f"{capitolo.stem:<42} {parole:>7} {aperti:>12}")
    print(f"{'TOTALE':<42} {totale_parole:>7} {totale_segnaposto:>12}")
    # Circa 340 parole per pagina nel formato 17x24 con questo corpo del testo.
    print(f"Stima: circa {totale_parole // 340} pagine di testo")


FORMATI = {"pdf": pdf, "epub": epub, "docx": docx}


def main(argomenti):
    if argomenti == ["stato"]:
        stato()
        return
    scelti = argomenti or list(FORMATI)
    sconosciuti = [a for a in scelti if a not in FORMATI]
    if sconosciuti:
        sys.exit(f"Formato sconosciuto: {', '.join(sconosciuti)}. Usa: {', '.join(FORMATI)} o stato")
    DIST.mkdir(exist_ok=True)
    for formato in scelti:
        FORMATI[formato]()


if __name__ == "__main__":
    main(sys.argv[1:])
