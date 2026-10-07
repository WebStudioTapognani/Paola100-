# L'IA in Comune

Manuale normativo e operativo per scrivere gli atti con l'intelligenza artificiale: AI Act, GDPR, metodo e prompt.
Autore: Riccardo Tapognani. Scritto con l'intelligenza artificiale, con il metodo che insegna.

## Cosa c'è qui

| Cartella | Contenuto |
|---|---|
| `libro/capitoli/` | il testo del libro, un file Markdown per capitolo |
| `libro/metadata.yaml` | titolo, sottotitolo, autore, pagina del copyright |
| `autore/` | questionario, note di stile e diario di bordo della scrittura |
| `docs/piano-pubblicazione.md` | checklist dalla scrittura alla pubblicazione |
| `docs/proposta-editoriale.md` | lettera e scheda da mandare all'editore |
| `template/` | impaginazione del PDF di stampa e dell'ebook |
| `build.py` | genera il libro |

Il manoscritto è completo: 22 capitoli in quattro parti, premessa e nove allegati. I punti da ricontrollare sui testi ufficiali prima della stampa sono in `autore/verifiche-libro.md`.

## Scaricare il libro impaginato

A ogni modifica GitHub rigenera il libro da solo:
1. apri la scheda **Actions** del repository;
2. clicca sull'ultima esecuzione di **Libro**;
3. in fondo, sotto **Artifacts**, scarica `libro`: contiene il PDF di stampa (17x24 cm), l'EPUB e il DOCX da mandare all'editore.

Nella stessa pagina trovi la tabella con parole scritte e segnaposto ancora aperti per capitolo.

## Generarlo sul proprio PC

Servono Python 3 e pandoc 3.1.

```
pip install -r requirements.txt
python build.py          # PDF, EPUB e DOCX in dist/
python build.py pdf      # solo il PDF
python build.py stato    # quanto manca
```
