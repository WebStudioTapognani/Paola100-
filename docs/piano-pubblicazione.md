# Piano di pubblicazione

L'obiettivo è essere **solo autore**: un editore pubblica e vende, tu incassi royalty da diritto d'autore. Niente Amazon KDP, dove l'editore del libro saresti tu.

## 0. Prima di scrivere
- [ ] Rendi privato il repository: Settings → Danger Zone → Change visibility → Private.
- [ ] Leggi il regolamento sugli incarichi extra-istituzionali dell'Unione. I proventi da diritto d'autore rientrano tra le attività escluse dall'autorizzazione (art. 53, comma 6, lett. b, D.Lgs. 165/2001), ma molti regolamenti chiedono comunque una comunicazione.
- [ ] Manda la comunicazione all'ufficio personale (modello sotto).
- [ ] Scrivi fuori dall'orario di lavoro, sul tuo PC, senza usare atti o dati dell'ente.

Modello di comunicazione:

```
Oggetto: Comunicazione attività di autore (art. 53, comma 6, lett. b, D.Lgs. 165/2001)

Il sottoscritto Riccardo Tapognani comunica che sta scrivendo un manuale
sull'uso dell'intelligenza artificiale negli uffici comunali, che sarà
pubblicato a proprio nome da un editore. L'attività è svolta fuori
dall'orario di servizio, con mezzi propri e senza utilizzare documenti o
dati dell'ente. I proventi derivano esclusivamente dall'utilizzazione
economica dell'opera da parte dell'autore. Resta a disposizione per
eventuali chiarimenti.
```

## 1. Primo traguardo: la proposta all'editore
1. Rispondi al questionario per il capitolo 3 (il tuo metodo) → Claude scrive la bozza → tu correggi.
2. Capitolo campione finito e impaginato.
3. Manda la proposta a Edizioni Simone con `docs/proposta-editoriale.md`, l'indice e il capitolo campione in PDF.
4. Se entro 4-6 settimane non rispondono, manda la stessa proposta a Maggioli e Publika.

## 2. Scrittura (mentre aspetti la risposta)
1. Capitoli 4, 5 e 7: quelli che il lettore cerca di più.
2. Capitoli 6, 8, 9, 10, 11.
3. Capitoli 1 e 2 per ultimi, così le norme sono aggiornate.
4. Premessa e Allegati alla fine.

Dopo ogni sessione, una riga in `autore/diario-di-bordo.md`: servirà per "Dietro le quinte" e per l'Allegato B.

## 3. Revisione
- [ ] Ogni norma verificata su Normattiva, con la data di aggiornamento nel colophon.
- [ ] Un lettore esterno (un collega o un segretario comunale) legge almeno i capitoli 3 e 4.
- [ ] Nessun dato reale, nessun nome, nessun atto copiato.

## 4. Il contratto con l'editore: cosa controllare
- [ ] Percentuale di royalty sul prezzo di copertina e su ebook, e ogni quanto viene pagata.
- [ ] Eventuale anticipo.
- [ ] Durata della cessione dei diritti e cosa succede se il libro va fuori catalogo.
- [ ] Possibilità di riusare i contenuti per articoli e per i volumi successivi.
- [ ] Nessun contributo economico richiesto all'autore: se ti chiedono soldi per pubblicare è editoria a pagamento, da evitare.

## 5. Piano B: Youcanprint
Se gli editori dicono no, Youcanprint resta coerente con l'obiettivo:
- l'editore è Youcanprint, con il suo ISBN gratuito; tu concedi solo una licenza non esclusiva e resti titolare dei diritti;
- royalty: 20% del prezzo di copertina sul cartaceo venduto nei negozi (30% sul loro store), 50% sull'ebook negli store (70% sul loro);
- distribuzione in libreria e negli store online (Amazon, Feltrinelli, Mondadori, Hoepli…), ma il venditore è Youcanprint, non tu;
- prima di caricare il PDF controlla che il formato 15x21 sia tra quelli disponibili. Se non c'è, si cambia in `libro/metadata.yaml` e il libro si reimpagina da solo.

## 6. Tasse
Le royalty pagate da un editore sono diritti d'autore: di norma niente partita IVA né contributi INPS. L'editore applica di solito la ritenuta d'acconto, e il reddito si dichiara nel 730 con una deduzione forfettaria del 25%, che sale al 40% sotto i 35 anni. Conferma con il CAF prima della dichiarazione.

## 7. Autorevolezza (il vero obiettivo)
- Articoli su riviste per la PA (lentepubblica.it, Diritto.it, Agenda Digitale): anche la collaborazione a giornali e riviste è esclusa dall'autorizzazione (art. 53, comma 6, lett. a). Un articolo per capitolo porta lettori e costruisce il nome.
- Profilo LinkedIn con il libro in evidenza e i "Dietro le quinte" come post.
- Curriculum: le pubblicazioni attinenti spesso sono titoli valutabili nelle progressioni tra aree e nei concorsi. Controlla bando e regolamento.

## 8. La serie
Stesso schema, volumi brevi per settore: IA per l'anagrafe, IA per i tributi, IA per i servizi sociali, IA per l'ufficio tecnico. Ogni volume riusa il template e la struttura di questo repository.
