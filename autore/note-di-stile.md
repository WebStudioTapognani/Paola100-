# Note di stile del libro

## Lettore
Dipendente comunale con poco tempo: istruttore o funzionario che scrive atti. Conosce il lavoro, non necessariamente l'IA.

## Tono
- Diretto e concreto. Niente enfasi, niente "rivoluzione", niente marketing.
- Istruzioni operative in seconda persona singolare ("copia il prompt", "verifica la norma").
- Parti normative in forma impersonale.
- Frasi brevi, un'idea per frase.

## Struttura dei capitoli operativi (Parte III)
1. Il problema
2. Il prompt
3. Esempio: prima e dopo
4. Errori tipici
5. Checklist prima della firma
6. Dietro le quinte

## L'IA come firma del libro
- Il libro dichiara apertamente di essere scritto con l'IA: è la prova che il metodo funziona.
- La formula è sempre "scritto **con** l'IA", mai "scritto **da** un'IA". Il diritto d'autore tutela solo le opere frutto del lavoro intellettuale umano (L. 132/2025): l'autore decide struttura e contenuti, mette esperienza ed esempi, corregge e verifica.
- "Dietro le quinte" chiude ogni capitolo: prompt usato, errori dell'IA, correzioni dell'autore. Dati presi da `autore/diario-di-bordo.md`.

## Esempi
- Sempre inventati o anonimizzati, ambientati nel "Comune di Borgo Esempio" (non "Valverde": esiste davvero, in provincia di Catania).
- Mai nomi di persone reali, mai dati dell'ente, mai atti veri copiati.

## Rimandi interni
- Per nome del capitolo, non per numero: "nel capitolo sull'AI Act".

## Norme
- Prima citazione completa (D.Lgs. 18 agosto 2000, n. 267), poi abbreviata (TUEL).
- Ogni riferimento va verificato su Normattiva prima della pubblicazione.

## Prompt
- In blocchi di codice, così nel libro escono nel riquadro grigio.
- Parti da sostituire tra parentesi quadre: [oggetto], [importo].
- [VERIFICARE: cosa] è il segnale che il modello lascia al lettore: non si sostituisce.
- Segnaposto dei dati personali in maiuscolo, senza parentesi: RICHIEDENTE_1, ATTO_1, RUP_1.
- Al massimo 12 righe per prompt.
- Ogni prompt compare anche nell'Allegato A.

## Lunghezza
- Capitolo: 3.000-6.000 parole, note escluse.
- Libro: circa 450 pagine nel formato 15x21 (stima del direttore editoriale per l'indice in quattro parti).
- Controllo con `python build.py stato`.
