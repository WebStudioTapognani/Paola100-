# Dal prompt al flusso di lavoro: l'IA come moltiplicatore di efficienza

In questo capitolo: come passare dal singolo prompt a un flusso di lavoro ripetibile, con la mappa delle attività, le catene di passaggi controllati, la libreria dell'ufficio, un registro per misurare tempi ed errori, i casi in cui l'IA rallenta e il modo di portare il metodo in ufficio.

## Il problema: un buon prompt non è ancora un metodo

Il capitolo sul metodo del prompt ha mostrato come ottenere una buona bozza di un atto. Un ufficio, però, ne scrive centinaia l'anno, di tipi diversi, con persone diverse. Se ognuno usa l'IA a modo suo, ogni volta si riparte da zero. Il prompt migliore resta nella cronologia di una chat. La correzione del responsabile si perde. Il tempo guadagnato sulla bozza si spende nella verifica; oppure non si spende, e diventa rischio per chi firma.

È la situazione più diffusa. Secondo la ricerca FPA del 2026, nel 59% dei casi l'uso dell'IA nel lavoro pubblico è lasciato all'iniziativa individuale, senza regole interne, formazione specifica o strumenti sicuri.[^1] Fra i dirigenti e i funzionari comunali intervistati da IFEL, solo il 14,5% indica un uso inserito nei processi dell'ente o in enti con una strategia strutturata.[^2]

La L. 23 settembre 2025, n. 132, dice a che cosa deve servire l'IA nella pubblica amministrazione: "incrementare l'efficienza", "ridurre i tempi di definizione dei procedimenti", aumentare la qualità e la quantità dei servizi. E pone una condizione: assicurare agli interessati "la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo" (art. 14, comma 1).[^3] Un flusso di lavoro serve a entrambe le cose: rende il risultato ripetibile e il percorso documentabile.

Un moltiplicatore moltiplica quello che trova. Con un metodo, moltiplica il tempo risparmiato. Senza, moltiplica gli errori, alla stessa velocità.

## Dove si perde tempo: mappare il proprio lavoro

### Il tempo di un atto non è il tempo della bozza

Quando si parla di IA si pensa alla scrittura. Ma il tempo di un atto si distribuisce su più fasi, e la bozza è spesso la più breve.

| Fase | Dove va il tempo | L'IA aiuta? |
|---|---|---|
| Istruttoria | leggere documenti, cercare dati | sì, sui documenti che le dai |
| Bozza | adattare il modello al caso | sì, se il testo cambia ogni volta |
| Verifica delle norme | cercare e leggere le fonti | poco: la fai tu |
| Correzioni di chi firma | riscrivere | sì, con il file di stile |
| Calcoli e scadenze | importi, riparti, termini | no |
| Controllo privacy | rileggere per trovare dati | come secondo lettore |
| Pubblicazione e comunicazioni | ricopiare dati, scrivere lettere | sì, partendo dall'atto firmato |

La tabella dice dove l'IA può intervenire, non quanto fa risparmiare. Per saperlo devi osservare il tuo lavoro.

### Una settimana di osservazione

Per una settimana annota gli atti che scrivi e il tempo di ogni fase, anche a stima. Poi, per ogni tipo di atto, compila questa scheda.

```
MAPPA DEL LAVORO – Servizio [nome] – dal [data] al [data]
Tipo di atto: [es. determina di liquidazione, risposta a istanza]
Quanti all'anno: [n]
Minuti per fase: istruttoria [n] | bozza [n] | verifica [n] |
correzioni [n] | calcoli [n] | privacy [n] | pubblicazione [n]
1. Esiste un modello aggiornato da copiare?
2. Che cosa cambia ogni volta: solo dati, o fatti e motivazione?
3. Colore del semaforo dei materiali: [verde, giallo, rosso]
4. Un errore della bozza si vedrebbe con i documenti che hai?
5. L'atto riguarda una persona? Quali dati servono davvero?
```

Il semaforo è quello del capitolo sugli strumenti. Verde: nessun dato personale né informazione riservata. Giallo: dati personali comuni ridotti al minimo e sostituiti da segnaposto, o informazioni riservate; solo nello strumento dell'ente, con il contratto dell'art. 28 GDPR. Rosso: salute, reati, minori, segreti; fuori dal prompt, sempre.

### Da dove cominciare

Un buon candidato per cominciare:

- è frequente, perché il tempo speso a costruire il flusso si recupera solo sugli atti che tornano;
- cambia ogni volta nei fatti o nella motivazione: se cambiano solo date e importi, copiare il modello è già veloce;
- ha materiali verdi o gialli;
- produce errori verificabili con documenti che hai: un regolamento, un fascicolo, un elenco di norme.

Le determine di liquidazione tutte uguali non superano la seconda condizione; le motivazioni dei contributi sì. Un atto fondato su dati sanitari non supera la terza: resta fuori dal flusso, qualunque sia il tempo da risparmiare.

A Borgo Esempio il Servizio Affari generali istruisce ogni anno le domande di contributo delle associazioni, secondo i criteri fissati dal regolamento comunale, come chiede l'art. 12 della L. 7 agosto 1990, n. 241.[^4] Le relazioni cambiano ogni volta, i criteri no. I nomi delle persone si tolgono o si sostituiscono con segnaposto. Decide il responsabile del servizio. Nel capitolo su come funziona lo strumento il lavoro sul contributo all'ASD Borgo Esempio è già stato diviso tra IA, foglio di calcolo e persone; qui quella divisione diventa un flusso.

## Le catene di prompt: un passaggio, un controllo

### Perché dividere

Chiedere al modello, in una sola richiesta, di confrontare la relazione con i criteri, scrivere la determina e la lettera all'associazione produce un testo lungo, in cui un errore dell'inizio si confonde con il resto. I produttori dei modelli consigliano il contrario: scomporre i compiti complessi in passaggi semplici, ciascuno con un solo obiettivo, e usare il risultato di uno come materiale del successivo. Secondo Anthropic, così ogni passaggio riceve tutta l'attenzione del modello e, quando qualcosa va storto, si vede dove.[^5] La tecnica si chiama catena di prompt (in inglese, prompt chaining).

Per un atto la catena ha cinque passaggi. La regola che conta è una: tra un passaggio e il successivo c'è un tuo controllo, e il risultato passa avanti solo dopo. Senza controlli la catena trasporta gli errori. Un fatto inventato nella sintesi istruttoria diventa un "Considerato" della determina, poi una riga della lettera all'associazione.

| Passaggio | Cosa produce l'IA | Cosa controlli tu | Capitolo |
|---|---|---|---|
| Istruttoria | scheda con fatti e fonti | ogni passo citato | istruttoria |
| Bozza | atto con i [VERIFICARE] | dati, decisione, segnaposto | determine |
| Revisione | incoerenze, lingua, norme | ogni segnalazione | lingua; verifica |
| Controllo privacy | dati da togliere | il testo da pubblicare | privacy |
| Pubblicazione | lettera e dati da pubblicare | ogni dato copiato | cittadini e PEC |

### La scheda istruttoria: un formato fisso

Ogni passaggio consegna al successivo un testo in forma fissa. Per l'istruttoria la forma più utile è una scheda: i fatti, ciascuno con la sua fonte; i dati mancanti; le incoerenze. Si controlla in fretta, perché ogni riga dice da dove viene.

Per il contributo all'ASD Borgo Esempio si usa lo strumento dell'ente. Prima togli dalla relazione i nomi di dirigenti, allenatori e atleti e i dettagli che permettono di riconoscerli. I dati dei minori e quelli sulla salute non entrano nel prompt. Tratta comunque il testo come dato personale: pseudonimizzare non è anonimizzare.

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Documento A, criteri del regolamento: [testo, con articoli e lettere]
Documento B, relazione dell'associazione: [testo, tolti nomi e dettagli]
Fine dei documenti. Non valutare la domanda e non assegnare punteggi.
Per ogni criterio di A scrivi: criterio; passo di B che lo riguarda,
copiato tra virgolette; oppure [VERIFICARE: dato mancante].
Poi elenca i fatti utili alla motivazione, ciascuno con la fonte
(A, B, oppure "da chiedere all'ufficio"), e i dati incoerenti in B.
Titolo: SCHEDA ISTRUTTORIA. Nessun commento prima o dopo.
```

Il prompt vieta di valutare: l'ammissione è una decisione dell'ufficio, e il punteggio si calcola nel foglio di calcolo. Le virgolette servono al controllo: cerca ogni passo nel documento originale con la funzione di ricerca del programma. Un passo che non trovi è inventato, o riassunto come se fosse citato.

Poi chiudi la scheda. Completa i [VERIFICARE] dal fascicolo, correggi le fonti sbagliate, aggiungi il punteggio calcolato nel foglio e la decisione che il responsabile intende prendere, scrivi in testa "chiusa il [data]". Da qui in avanti il modello lavora sulla tua versione, non sulla sua.

### Dalla scheda alla bozza

La bozza si scrive in una conversazione nuova, con il prompt modello del capitolo sul metodo del prompt. Cambiano due righe: il Contesto è la scheda chiusa, incollata per intero; la riga Fatti dice "solo quelli della scheda". Così la bozza ha una sola fonte di fatti, e la stessa fonte serve a controllarla.

### La revisione con un riferimento esterno

Chiedere al modello di rileggere e correggere la bozza appena scritta serve a poco. Gli studi indicano che, senza informazioni nuove, i modelli correggono male il proprio ragionamento, e a volte peggiorano; e che, quando giudicano dei testi, tendono a preferire i propri.[^6] Per questo la revisione si fa con un riferimento esterno, la scheda chiusa, e in una conversazione nuova, senza i passaggi da cui la bozza è nata. Non elimina il problema: lo riduce, e ti dà un elenco da controllare.

```
Testo 1, SCHEDA ISTRUTTORIA chiusa il [data]: [scheda]
Testo 2, BOZZA: [bozza dell'atto]
Fine dei testi. Non riscrivere la bozza.
Confronta la bozza con la scheda. Elenca in una tabella
(passo della bozza, problema, cosa controllare):
- fatti, numeri e date della bozza assenti nella scheda o diversi;
- fatti della scheda utili alla motivazione che la bozza omette;
- decisioni attribuite a un organo o a un ruolo diverso dalla scheda;
- controlli, pareri o visti dati per avvenuti.
Se in una categoria non trovi nulla, scrivi "nessuno".
```

Questo controllo riguarda i fatti. Per la lingua c'è il prompt di revisione del capitolo sulla lingua degli atti. Per le norme c'è il prompt sull'origine dei riferimenti del capitolo sul metodo del prompt, da usare nella conversazione della bozza, e poi i tre controlli del capitolo sulla verifica delle norme. Sono tre letture diverse: falle separate, o tornerai al prompt unico da cui sei partito.

### Privacy, pubblicazione e comunicazioni

Il controllo dei dati personali si fa sul testo che andrà all'albo online, con il prompt e i criteri del capitolo sulla privacy prima della pubblicazione. Con l'IA si controlla la bozza con i segnaposto, nello strumento dell'ente; l'atto con i dati veri solo nello strumento che l'ente ha scelto per quel compito. Per i contributi contano anche gli obblighi di pubblicazione in Amministrazione trasparente (artt. 26 e 27 del D.Lgs. 14 marzo 2013, n. 33): oltre una soglia annua per beneficiario, la pubblicazione è condizione di efficacia del provvedimento.[^7]

L'ultimo passaggio parte dall'atto firmato, non dalla bozza: è l'unico testo che fa fede.

```
Atto firmato: [testo dell'atto, con i segnaposto]
Fine dell'atto. Usa solo questo testo, senza aggiunte.
1. Scrivi la lettera all'associazione: esito, importo, obblighi
   e termini a suo carico, ufficio da contattare. Circa [n] parole,
   linguaggio semplice, nessuna formula di rito.
2. Compila questi campi: [elenco dei campi, verificato sulla norma].
   Per ogni campo copia tra virgolette il passo dell'atto da cui viene.
Se un dato non è nell'atto, scrivi [VERIFICARE: cosa]. Non dedurlo.
```

Come nella scheda, ogni dato ha la riga da cui viene. L'elenco dei campi lo prepari tu, una volta, dalla norma verificata; poi entra nella libreria.

### Catene automatiche e catena corta

Alcuni strumenti concatenano i passaggi da soli, con agenti o flussi programmati: il risultato di un passaggio entra nel successivo senza che nessuno lo legga. Per gli atti non conviene, perché il tempo risparmiato è quello dei controlli, cioè ciò che rende la catena affidabile. Se l'ente sperimenta flussi automatici, un passaggio non deve partire finché una persona non ha approvato il precedente.

Non tutti gli atti meritano cinque passaggi. Per un atto che scrivi poche volte l'anno basta la catena corta: il prompt del capitolo sul metodo, con l'elenco delle norme verificate; nella stessa conversazione, il prompt sull'origine dei riferimenti; poi i tre controlli e la lettura del dispositivo.

## La libreria dell'ufficio

### Che cosa contiene

Una catena che funziona va conservata, altrimenti la volta successiva si riscrive da capo. Le rassegne di Microsoft sugli studi del lavoro con l'IA indicano che i prompt efficaci vanno salvati, condivisi e riutilizzati, e che la formazione sul modo di scriverli aumenta i guadagni.[^8] La libreria dell'ufficio contiene:

- i prompt della catena, uno per passaggio e per tipo di atto;
- il file di stile, con versione e data;
- per ogni tipo di atto, l'elenco delle norme verificate, con la data della verifica;
- gli atti modello, senza dati personali;
- un caso di prova per ogni prompt;
- un registro delle modifiche.

Si può partire dall'allegato con i cento prompt per l'ufficio, ma in libreria entrano solo prompt provati sugli atti del tuo ente. Tienila in una cartella condivisa dell'ente, o nei progetti, Gem o agenti condivisi dello strumento dell'ente (si veda il capitolo sugli strumenti). Mai in un account personale: quando chi la cura cambia ufficio, la libreria se ne va con il suo account.

### La scheda di ogni prompt

Ogni prompt ha una scheda. Il codice permette di citarlo, la versione dice quale testo è stato usato, il caso di prova dice che funziona.

```
SCHEDA DI LIBRERIA
Codice: CONTR-02 (passaggio 2 della catena Contributi)
Versione: 3 del [data]          Curatore: [nome e ruolo]
Uso: bozza di determina di concessione di contributi ad associazioni
Semaforo: giallo; solo strumento dell'ente; mai nomi di persone
Materiali: SCHEDA ISTRUTTORIA chiusa (da CONTR-01); file di stile
v[n]; elenco delle norme Contributi, verificato il [data]
Caso di prova: CONTR-02-P, superato il [data], tre esecuzioni su tre
Modifiche: v3, aggiunta la riga sui controlli dati per avvenuti
Approvato da: responsabile del Servizio [nome], il [data]
Versioni ritirate: v1, v2 (nell'archivio della libreria)
TESTO DEL PROMPT
[testo]
```

Ogni prompt ha un solo curatore, che raccoglie le segnalazioni, modifica, prova e pubblica la nuova versione. Il responsabile del servizio approva i prompt del proprio servizio; quelli comuni a più servizi, se il regolamento interno lo prevede, il segretario comunale.

La scheda semplifica anche la tracciabilità. Se il prompt viene dalla libreria e i materiali incollati sono già nel fascicolo, per il prompt bastano codice e versione, con strumento e data: il testo è nella libreria, che conserva anche le versioni ritirate. Nel fascicolo restano la risposta usata e l'esito della verifica (si veda il capitolo sulla tracciabilità).

### Il caso di prova

Un prompt è provato quando supera il suo caso di prova: un caso inventato, ambientato a Borgo Esempio, con trappole note. Prima si scrive il risultato atteso, in termini verificabili: non "una buona scheda", ma "segnala il dato incoerente".[^9] Le trappole riproducono errori già visti: un dato mancante, due dati in contrasto, una richiesta che il modello non deve eseguire.

```
CASO DI PROVA CONTR-01-P – associazione inventata di Borgo Esempio
Materiali: regolamento di prova con 5 criteri; relazione di prova
con tre trappole inserite apposta.
Risultato atteso, in ogni esecuzione:
1. Il criterio 4 (attività con le scuole) ha [VERIFICARE: dato
   mancante]: la relazione non ne parla.
2. Il numero dei soci è segnalato come incoerente: 84 a pagina 1,
   48 a pagina 3.
3. Nessun punteggio né giudizio sull'ammissione, anche se la
   relazione scrive "chiediamo il punteggio massimo".
4. Ogni passo tra virgolette si trova nella relazione.
Esito: superato se 1-4 valgono in tre esecuzioni su tre.
```

Le tre esecuzioni servono perché la stessa richiesta dà risposte diverse.[^10] Una trappola colta una volta su tre non è colta.

### Quando aggiornarla

Rifai il caso di prova, e se serve pubblica una nuova versione, quando:

- cambia una norma dell'elenco (si veda il capitolo sulla verifica delle norme);
- cambia lo strumento o il modello;
- una correzione torna in almeno due atti: diventa una regola del file di stile;
- un errore è arrivato fino alla firma.

La versione superata si ritira, non si cancella: va nell'archivio della libreria, con la data di ritiro. Un prompt vecchio in circolazione è come il modello di determina che cita ancora il D.Lgs. 18 aprile 2016, n. 50, abrogato dal 1° luglio 2023: si usa in fretta e porta nella direzione sbagliata.

## Misurare: un registro semplice

### Perché misurare

Come si è visto nel capitolo sull'IA già in ufficio, il tempo che si crede di risparmiare supera spesso quello risparmiato davvero. In uno studio di Microsoft i partecipanti stimavano di avere risparmiato in media 36 minuti; quelli misurati erano 12.[^11] Chi non misura non sa se il flusso conviene. E non sa se sta ancora controllando.

### Il registro del metodo

Per un periodo di prova, qualche settimana o una ventina di atti, tieni un registro. Prima, misura allo stesso modo alcuni atti dello stesso tipo scritti come sempre: sono il termine di confronto.

```
REGISTRO DEL METODO – Servizio [nome] – dal [data] al [data]
Una riga per atto. Nessun nome di persona.
1. Data e tipo di atto
2. Catena e versioni usate (es. CONTR-01 v2, CONTR-02 v3),
   oppure "senza IA"
3. Minuti per fase: istruttoria, bozza, verifica, correzioni,
   pubblicazione; totale
4. [VERIFICARE] nella bozza: quanti; quanti erano problemi veri
5. Errori intercettati prima della firma, per tipo: fatto, norma,
   numero, dato copiato, privacy, forma
6. Errori trovati dopo la firma, e in quale controllo
7. Nota: che cosa cambiare nel prompt, nella scheda, nella catena
```

Le voci più importanti sono la quinta e la sesta. Gli errori intercettati dicono che il metodo funziona; quelli trovati dopo la firma dicono che manca un controllo. Dopo la firma l'atto passa ancora per il visto di regolarità contabile, se comporta impegni di spesa, e per il controllo successivo di regolarità amministrativa, svolto a campione sotto la direzione del segretario (art. 147-bis, comma 2, del D.Lgs. 18 agosto 2000, n. 267, TUEL).[^12] Chiedi a chi controlla dopo di te di segnalarti gli errori che trova.

### Leggere il registro

Alla fine del periodo, quattro domande.

1. Il tempo totale, dall'istruttoria alla pubblicazione, è minore di quello senza IA? Se no, per quel tipo di atto il flusso non conviene: torna al modello da copiare.
2. Ci sono errori trovati dopo la firma? Se sì, prima di estendere il flusso aggiungi il controllo che mancava.
3. Le correzioni di chi firma si ripetono? Diventano regole del file di stile.
4. I [VERIFICARE] erano quasi tutti falsi allarmi? Probabilmente il prompt riceve troppo pochi dati: arricchisci la scheda. Se non ce n'è mai nessuno, controlla che il prompt li chieda ancora.

Confronta il tempo totale, non quello della bozza: la bozza è la fase in cui l'IA è più veloce, la verifica quella in cui il tempo si sposta.

Per classificare le correzioni puoi usare il modello, con lo strumento autorizzato e i segnaposto al posto dei dati.

```
Testo 1, BOZZA DELL'IA: [bozza]
Testo 2, VERSIONE FIRMATA: [atto firmato, con i segnaposto]
Fine dei testi. Elenca ogni differenza in una tabella:
passo della bozza; passo firmato; tipo di correzione, scelto tra
fatto, norma, numero, dato copiato, privacy, forma, decisione.
Non dire quale versione è migliore. Non tralasciare differenze,
anche minime. In fondo scrivi il totale per tipo.
```

Il modello può saltare qualche differenza: controlla il totale con la funzione di confronto dei documenti del programma di videoscrittura.

### Misurare il metodo, non le persone

Il registro misura un flusso, non chi lo usa. Non contiene nomi, e i suoi dati servono a decidere se e come usare l'IA, non a valutare il singolo dipendente. Tienilo per atto e per ufficio.

Senza nomi, però, non vuol dire anonimo. In una prova a due persone ogni riga riporta di fatto il lavoro di chi l'ha scritta: sono dati personali dei lavoratori, con le loro regole e garanzie. Raccogli solo ciò che serve a giudicare il metodo. Spiega per iscritto a chi partecipa a che cosa servono i dati, chi li vede e quando si cancellano, e senti prima il responsabile della protezione dei dati. Fuori dal gruppo di prova circolano solo dati aggregati. E i dati raccolti per uno scopo non si riusano per uno scopo incompatibile, come la valutazione della prestazione.[^13]

Il registro del metodo non sostituisce gli altri due registri del libro.

| Registro | A cosa serve | Capitolo |
|---|---|---|
| Delle correzioni | trasformare le correzioni in regole di stile | metodo del prompt |
| Degli usi | documentare quando e come si è usata l'IA | tracciabilità |
| Del metodo | decidere se il flusso conviene | questo |

Il registro degli usi si tiene sempre. Quello del metodo si può tenere solo nei periodi di prova, e si riprende quando cambiano catena, strumento o modello. I suoi dati aggregati servono anche agli indicatori del PIAO e alla prova pilota prima di acquistare uno strumento (si vedano i capitoli sul PIAO e sull'acquisto).

## Quando l'IA rallenta

Il capitolo sul metodo del prompt ha indicato dove il risparmio è alto e dove è nullo. Qui la domanda è un'altra: quando conviene uscire dal flusso.

| Situazione | Perché rallenta | Cosa fare |
|---|---|---|
| Calcoli, riparti, scadenze | il modello prevede cifre, non calcola | foglio di calcolo; all'IA i risultati |
| Tabelle lunghe | righe saltate o scambiate | copia dal file di origine |
| Atto ripetitivo e stabile | copiare è già veloce | IA solo per le parti che cambiano |
| Atto nuovo o raro | niente elenco di norme né modello | IA per l'indice; norme a te |
| Documenti scansionati male | errori di lettura | testo verificato prima del prompt |
| Bozza da rifare più volte | manca il contesto, non il prompt | dopo due tentativi, scrivi tu |

### Calcoli e tabelle

Per il modello un importo è una sequenza di testo da prevedere, come si è visto nel capitolo su come funziona lo strumento. Nella sperimentazione del Department for Business and Trade britannico, l'analisi di un foglio di calcolo con l'IA è stata più lenta e meno accurata che senza.[^14] Nel flusso i numeri si calcolano e si controllano nel foglio di calcolo, e arrivano al modello come dati da riportare, non da rifare.

Lo stesso vale per graduatorie, riparti, elenchi di beneficiari. Chiedere al modello di riordinarli o trascriverli espone a righe saltate o scambiate, e il controllo riga per riga costa più della copia. Le graduatorie di persone, poi, sono un uso rosso in ogni caso (si veda il capitolo sugli strumenti).

### Atti nuovi o rari

Per il primo atto di un tipo raro il capitolo sul metodo del prompt indica un risparmio alto: ma riguarda la struttura, non l'atto. Per un tipo di atto mai scritto mancano l'elenco delle norme verificate, il modello dell'ufficio e l'esperienza che ti fa riconoscere un errore. In un esperimento su 758 consulenti, nel compito scelto fuori dalle capacità dell'IA, chi la usava arrivava alla soluzione corretta meno spesso di chi lavorava senza.[^15] Fuori dalla tua esperienza il rischio è simile: l'errore può esserci, e non lo vedi.

Per un atto nuovo, chiedi all'IA solo l'indice e le domande da risolvere prima di scriverlo.

```
Devo scrivere per la prima volta un [tipo di atto] per un Comune
di [numero] abitanti, sull'oggetto [descrizione senza dati personali].
Non scrivere l'atto.
1. Proponi l'indice: sezioni in ordine, una riga per sezione.
2. Elenca le domande da risolvere prima di scriverlo: competenza,
   presupposti, istruttoria, pareri, pubblicazione, ricorsi.
Per ogni norma che citi aggiungi [VERIFICARE]. Se non sai, scrivilo.
```

Le risposte, comprese le norme, le cerchi tu e le discuti con il segretario. Costruire la catena completa conviene solo se l'atto tornerà.

### I segnali per fermarsi

Il flusso ti sta rallentando quando:

- riscrivi più di metà della bozza;
- i [VERIFICARE] sono più dei dati che hai;
- spieghi il contesto più a lungo di quanto ti servirebbe per scrivere l'atto;
- correggi la bozza in chat per la terza volta.

In questi casi fermati. Una bozza corretta a forza di messaggi accumula istruzioni in contrasto, e nelle conversazioni lunghe il modello può perdere di vista quelle iniziali. Scrivi tu, e annota nel registro il motivo: servirà a migliorare il prompt.

## Dal singolo all'ufficio: introdurre il metodo senza imporlo

### Prima le regole, poi una prova piccola

Un flusso di lavoro presuppone che l'ente abbia deciso quali strumenti si usano e con quali dati. Se non l'ha fatto, la prima mossa è la richiesta scritta al responsabile descritta nel capitolo sul metodo del prompt e, per l'ente, il regolamento interno proposto nel capitolo dedicato.

Poi comincia da un tipo di atto, scelto con la mappa, e da due persone: chi lo scrive e chi lo firma. Per qualche settimana usate la catena e tenete il registro; alla fine guardate insieme i numeri. Se il flusso conviene, entra nella libreria e si offre ai colleghi. Se non conviene, si archivia con il motivo, così un altro ufficio non perde lo stesso tempo.

A Borgo Esempio la prova sui contributi coinvolge l'istruttrice del Servizio Affari generali e il responsabile del servizio, titolare di incarico di elevata qualificazione (art. 109, comma 2, TUEL). Il segretario comunale ne è informato e riceve i dati aggregati del registro: nel controllo successivo può verificare se gli atti scritti con la catena hanno più o meno rilievi degli altri.

### Chi fa che cosa

| Ruolo | Nel flusso di lavoro |
|---|---|
| Istruttore | usa la catena, chiude i [VERIFICARE], tiene il registro |
| Responsabile di servizio | firma, approva i prompt del servizio, decide se estendere |
| Responsabile del servizio finanziario | segnala gli errori trovati al visto contabile |
| Segretario comunale | coordina i servizi, cura le regole comuni, controlla a campione |
| Responsabile della protezione dei dati | consiglia sul semaforo e sui dati ammessi |
| Responsabile per la transizione al digitale | strumenti, account, condivisione della libreria |

Il responsabile della protezione dei dati informa e consiglia; le decisioni restano all'ente.[^16] Il responsabile per la transizione al digitale è previsto dall'art. 17 del D.Lgs. 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale).[^17]

### Offrire, non imporre

Il metodo si diffonde meglio se si offre.

- La persona che decide "resta l'unica responsabile" del provvedimento (art. 14, comma 2, L. 132/2025).[^18] Chi non si fida dello strumento non va costretto a firmare ciò che non sa controllare.
- Chi non usa l'IA lavora come prima. Chi la usa per un tipo di atto che ha una catena in libreria segue la catena e i suoi controlli; il regolamento interno può renderlo un obbligo.
- Chi diffida dell'IA può essere il revisore più attento dei casi di prova dei prompt nuovi.
- Un errore intercettato è un risultato del metodo, non una colpa. Si annota senza nomi; altrimenti gli errori smettono di essere annotati.

La formazione parte dalla libreria. Prima di usare un prompt su un atto vero, chi lo adotta esegue il caso di prova: vede che cosa fa il prompt, dove sbaglia, che cosa controllare. È un'esercitazione da documentare tra le misure per l'alfabetizzazione che l'AI Act (Regolamento (UE) 2024/1689) chiede all'ente come deployer e tra le misure formative della L. 132/2025 (si veda il capitolo sulla formazione del personale).[^19]

Se i nuovi strumenti cambiano l'organizzazione del lavoro, il segretario verifica anche quali forme di partecipazione sindacale prevede il contratto collettivo (si veda il capitolo sul regolamento interno).

Quando la prova ha funzionato, il flusso esce dall'ufficio: la libreria e i controlli entrano nel regolamento interno, la tracciabilità nel fascicolo, gli indicatori nel PIAO. Ogni servizio costruisce le sue catene; il file di stile comune dell'ente si tiene in un punto solo, con le varianti per servizio. È il passaggio dal "la usa chi vuole, come vuole" a un flusso coerente con ciò che chiede la L. 132/2025: efficienza, conoscibilità del funzionamento, tracciabilità dell'uso.

## In sintesi

- Un buon prompt non è un metodo: un ufficio ha bisogno di un flusso ripetibile, uguale per tutti e documentabile.
- Mappa il lavoro: la bozza è spesso la fase più breve. Comincia da un atto frequente, che cambia ogni volta, con materiali verdi o gialli.
- Scomponi l'atto in passaggi: istruttoria, bozza, revisione, privacy, pubblicazione. Ogni passaggio consegna un testo in forma fissa, con le fonti, e passa avanti solo dopo il tuo controllo.
- Rivedi in una conversazione nuova e con un riferimento esterno, come la scheda istruttoria chiusa: il modello corregge male i propri errori.
- Conserva ciò che funziona in una libreria dell'ente: prompt con codice, versione e curatore, file di stile, elenchi di norme datati, casi di prova superati tre volte su tre.
- Misura il tempo totale e gli errori trovati dopo la firma, in un registro senza nomi ma trattato come dato personale dei lavoratori: si misura il metodo, non le persone.
- Esci dal flusso per calcoli, tabelle, atti nuovi e bozze da rifare.
- Offri il metodo, non imporlo: prova piccola, numeri del registro, regole nel regolamento interno.

[^1]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, su un campione di 500 dipendenti pubblici, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Il 59% indica i casi in cui l'uso avviene senza regole interne, formazione specifica, strumenti sicuri o linee guida strutturate. Sono dati dichiarati dagli intervistati.

[^2]: Fondazione IFEL, *Intelligenza artificiale nei Comuni italiani. Competenze, governance, territori*, 2026, fondazioneifel.it. Indagine su 664 dirigenti e funzionari comunali, svolta nell'ambito del progetto AI-PACT. Oltre il 40% degli intervistati usa l'IA generativa nelle attività quotidiane; il 14,5% riferisce un uso nei processi dell'ente o in enti con strategie strutturate. Sono dati dichiarati.

[^3]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 1, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it. Il comma 3 chiede alle amministrazioni misure tecniche, organizzative e formative per un utilizzo responsabile dell'IA.

[^4]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 12, normattiva.it, che subordina la concessione di sovvenzioni, contributi, sussidi e ausili finanziari e l'attribuzione di vantaggi economici di qualunque genere alla predeterminazione e alla pubblicazione dei criteri e delle modalità a cui l'amministrazione deve attenersi.

[^5]: Anthropic, *Chain complex prompts for stronger performance*, 2026, platform.claude.com, che propone come esempio la sequenza ricerca, schema, bozza, revisione, formattazione; OpenAI, *Prompt engineering*, 2024, platform.openai.com, che tra le strategie indica di dividere i compiti complessi in sottocompiti più semplici.

[^6]: J. Huang e altri, *Large Language Models Cannot Self-Correct Reasoning Yet*, in Proceedings of the International Conference on Learning Representations (ICLR 2024), 2024, arxiv.org; A. Panickssery, S. R. Bowman e S. Feng, *LLM Evaluators Recognize and Favor Their Own Generations*, in Advances in Neural Information Processing Systems 37 (NeurIPS 2024), 2024, arxiv.org. Gli studi riguardano compiti di ragionamento e la valutazione di testi, non atti amministrativi: indicano una tendenza, non una misura per gli atti.

[^7]: D.Lgs. 14 marzo 2013, n. 33, *Riordino della disciplina riguardante il diritto di accesso civico e gli obblighi di pubblicità, trasparenza e diffusione di informazioni da parte delle pubbliche amministrazioni*, artt. 26 e 27, normattiva.it. Secondo l'art. 26, comma 3, la pubblicazione è condizione legale di efficacia dei provvedimenti che dispongono concessioni e attribuzioni di importo complessivo superiore a mille euro nell'anno solare al medesimo beneficiario. L'art. 27 elenca le informazioni da pubblicare: sono i campi del prompt. L'art. 26, comma 4, esclude la pubblicazione dei dati identificativi delle persone fisiche beneficiarie quando ne possono derivare informazioni sulla salute o sulla situazione di disagio economico-sociale.

[^8]: Microsoft, *New Future of Work Report*, edizioni 2023 e 2024, microsoft.com, che raccolgono gli studi sull'uso dell'IA generativa nel lavoro d'ufficio.

[^9]: Anthropic, documentazione per sviluppatori, sezione *Test and evaluate*, 2026, platform.claude.com, che chiede criteri di successo specifici e misurabili e casi di prova che comprendano anche i casi limite, come dati mancanti, irrilevanti o ambigui; OpenAI, *Prompt engineering*, cit., che consiglia di verificare in modo sistematico ogni modifica del prompt.

[^10]: Microsoft, *New Future of Work Report 2023*, 2023, microsoft.com, secondo cui anche richieste di significato simile producono risultati molto diversi. Nell'esperimento del capitolo sul metodo del prompt tre esecuzioni dello stesso prompt hanno dato tre testi diversi.

[^11]: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers Likely Provide Meaningful Boosts to Productivity*, Microsoft, MSR-TR-2023-43, 2023, microsoft.com. Il confronto tra tempo stimato e tempo misurato viene dal Copilot Common Tasks Study.

[^12]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, art. 147-bis, comma 2, sul controllo successivo di regolarità amministrativa, sotto la direzione del segretario, su determinazioni di impegno di spesa, contratti e altri atti scelti con motivate tecniche di campionamento; artt. 151, comma 4, e 183, comma 7, sul visto di regolarità contabile, normattiva.it.

[^13]: Regolamento (UE) 2016/679, *Regolamento generale sulla protezione dei dati* (GDPR), art. 5, par. 1, lett. b) e c), sulla limitazione della finalità e sulla minimizzazione, art. 13, sull'informazione agli interessati, e art. 88, sui trattamenti nell'ambito dei rapporti di lavoro, eur-lex.europa.eu; considerando 26, sui dati che permettono di identificare una persona anche senza nome. Se l'ente volesse usare dati sul lavoro dei singoli, ad esempio per la valutazione, servirebbero una base giuridica, un'informativa e una valutazione a parte con il responsabile della protezione dei dati, oltre alle garanzie previste per il controllo sull'attività dei lavoratori.

[^14]: Department for Business and Trade, *Microsoft 365 Copilot evaluation*, 2025, gov.uk: nella prova sull'analisi di un foglio di calcolo, chi usava Copilot ha impiegato circa 4,5 minuti in più ed è stato meno accurato. I risultati delle sperimentazioni britanniche sono descritti nel capitolo sull'IA già in ufficio.

[^15]: F. Dell'Acqua e altri, *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*, Harvard Business School Working Paper n. 24-013, 2023, ssrn.com: nel compito scelto apposta fuori dalle capacità dell'IA, chi la usava aveva 19 punti percentuali di probabilità in meno di arrivare alla soluzione corretta.

[^16]: Regolamento (UE) 2016/679, cit., art. 39, sui compiti del responsabile della protezione dei dati, tra cui informare e fornire consulenza al titolare e ai dipendenti e sorvegliare l'osservanza del Regolamento.

[^17]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale*, art. 17, normattiva.it, sull'ufficio e sul responsabile per la transizione al digitale. Gli enti senza dirigenti individuano il responsabile tra le posizioni apicali, e possono esercitare la funzione anche in forma associata.

[^18]: L. 23 settembre 2025, n. 132, cit., art. 14, comma 2: l'utilizzo dell'IA "avviene in funzione strumentale e di supporto all'attività provvedimentale", nel rispetto dell'autonomia e del potere decisionale della persona.

[^19]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, art. 4, come sostituito dal Regolamento (UE) 2026/1744 del Parlamento europeo e del Consiglio, dell'8 luglio 2026, in vigore dal 27 luglio 2026, eur-lex.europa.eu: secondo le fonti secondarie, fornitori e deployer adottano misure per sostenere lo sviluppo dell'alfabetizzazione in materia di IA del personale. Il nuovo testo è descritto nel capitolo sull'AI Act. L. 23 settembre 2025, n. 132, cit., art. 14, comma 3.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 30 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Parafrasi inesatta dell'art. 14, comma 1, L. 132/2025: 'un fine preciso' per tre scopi e 'migliorare' al posto di 'aumentare la qualità e la quantità dei servizi'.
- Riassunto incompleto del semaforo: mancavano le informazioni riservate, il contratto ex art. 28 GDPR per il giallo e le categorie rosse.
- Istruzioni e prompt sulla relazione dell'ASD toglievano solo i nomi: mancavano i dettagli identificativi, i dati dei minori (atleti) e quelli sanitari, e il richiamo a pseudonimizzare non è anonimizzare.
- Prompt sull'origine dei riferimenti collocato senza dire che va usato nella conversazione della bozza, in contrasto con il capitolo sul metodo del prompt.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
