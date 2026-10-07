# Come si scrive un prompt per un atto

In questo capitolo: lo schema in cinque parti, il file di stile, un esperimento con due prompt sulla stessa determina, dati personali, responsabilità, verifica delle norme, tempi.

## Il problema: un testo che sembra finito

Chi chiede a un chatbot "scrivimi una determina" riceve spesso un testo lungo, sicuro di sé e all'apparenza pronto. A volte cita norme abrogate o articoli che dicono altro. Quasi mai segnala cosa non sa.

Secondo una ricerca FPA del giugno 2026, il 66% dei dipendenti pubblici intervistati usa l'IA nel lavoro almeno una volta a settimana; scrivere testi è, con la sintesi di documenti, l'uso più diffuso.[^1] Fra i dirigenti e i funzionari comunali intervistati da IFEL, il 41,9% usa l'IA generativa nelle attività quotidiane e, secondo le sintesi pubblicate, il 55% di chi la usa non ha ricevuto alcuna formazione.[^2] Molti la usano già per scrivere. Pochi hanno un metodo.

Un atto amministrativo ha una struttura riconosciuta: intestazione e oggetto; preambolo, motivazione e dispositivo; luogo, data e firma.[^3] La motivazione indica "i presupposti di fatto e le ragioni giuridiche" della decisione, "in relazione alle risultanze dell'istruttoria" (art. 3 della L. 7 agosto 1990, n. 241).[^4] Ogni norma citata deve esistere, dire ciò che le si attribuisce ed essere vigente. E chi firma ne risponde. Il metodo serve a ottenere una bozza che rispetti questi vincoli, e a vedere dove non li rispetta.

## Perché il prompt generico non funziona

Per questo capitolo una determina di rinnovo è stata chiesta a un modello di IA con due prompt, tre volte ciascuno. Il primo è quello che quasi tutti scrivono.

```
Scrivi una determina per rinnovare l'abbonamento a una banca dati giuridica
on line per il Comune di Borgo Esempio. Costo 1.200 euro più IVA,
fornitore Editrice Esempio S.r.l.
```

In tutte e tre le prove esce una determina completa, di 1.400-1.705 parole, aggiornata al correttivo del 2024 del Codice dei contratti pubblici e senza atti inesistenti. Ma non è priva di errori: in due prove attribuisce a un articolo ciò che non dice, in una cita un riferimento superato.

Il problema più grave, però, è un altro. Senza contesto, il modello riempie i vuoti con ciò che è probabile, e il probabile non è il vero:

- dà per fatti controlli che nessuno ha fatto: DURC regolare, nessuna convenzione Consip attiva, dichiarazione dell'operatore già resa;
- decide fatti che non conosce: l'aliquota IVA al 22%, il buon esito del contratto precedente, la congruità del prezzo;
- accumula norme: 14-15 atti normativi per 1.200 euro;
- sceglie da solo forma e registro: grassetti, titoli, tabelle.

Il testo sembra finito, ed è questo il rischio: dentro l'atto nessuna bozza segnala un dubbio, e i 53-71 campi vuoti chiedono dati, non verifiche. I modelli non sanno prevedere quando sbagliano e accettano senza critica le premesse errate dell'utente.[^5] Il prompt deve dire al modello cosa sa, cosa non sa e cosa fare quando un dato manca.

## Lo schema in cinque parti

Ruolo, contesto, compito, formato, vincoli: lo schema sintetizza le indicazioni ufficiali di Anthropic, OpenAI, Google e Microsoft, ma nessuno dei quattro lo formula esattamente così.[^6] Copia il prompt modello.

```
Sei un istruttore amministrativo del [servizio] del Comune di [nome].
Contesto: [fatti essenziali; atti precedenti con numero e data, o ATTO_1].
Dati: [importi, date, codici richiesti; persone fisiche come RICHIEDENTE_1].
Norme (solo queste) e cosa regolano: [elenco già verificato].
Esempio (solo struttura e tono, nessun dato): [atto, oppure "nessuno"].
Stile: [file di stile, oppure "applica il file di stile delle istruzioni"].
Formato: [sezioni nell'ordine dell'ufficio]; circa [n] parole; testo semplice.
Compito: scrivi la bozza di [tipo di atto] per [oggetto].
Fatti: solo i dati sopra. Non dare per avvenuti pareri, votazioni, controlli.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Norme fuori elenco: non citarle, scrivi [VERIFICARE: norma da cercare].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

Le parentesi quadre indicano ciò che sostituisci tu, tranne [VERIFICARE]: è il segnale che il modello lascia a te. I segnaposto dei dati personali sono in maiuscolo e senza parentesi, come RICHIEDENTE_1: restano così nel prompt e nella bozza.

### Riga per riga

*Ruolo.* Anche una sola frase orienta comportamento e tono.[^7] Tienilo sobrio: "istruttore amministrativo", non "il massimo esperto di diritto amministrativo". Negli atti su una persona, al posto del nome del Comune scrivi "di un Comune di [numero] abitanti".

*Contesto.* Scrivilo come per un collega bravo ma appena arrivato: se lui non capisce, non capisce nemmeno il modello.[^8] Indica solo i codici che l'atto richiede: se nel prompt c'è la voce CIG, il modello la inserirà anche in una concessione di contributo, dove non serve. I documenti lunghi vanno in alto, la richiesta in fondo.[^9]

*Norme.* È la riga più importante: norme già verificate, ciascuna con cosa regola nell'atto, e solo quelle.[^10] Se una voce è ancora da verificare, scrivilo accanto.

*Esempio.* Un atto dello stesso tipo, già firmato, è "uno dei modi più affidabili" per orientare formato e tono. I produttori consigliano fino a cinque esempi; per un atto lungo questo libro ne suggerisce uno o due, perché di più occupano spazio e il modello tende a ricalcarli.[^11] Meglio gli atti del tuo ente: in un test di Anthropic, esempi tratti dallo stesso materiale hanno ridotto gli errori, esempi generici no.[^12] Prima di incollare l'atto togli ciò che riporta a una persona: nomi, codici fiscali e partite IVA, indirizzi, protocolli, numero e data dell'atto, CIG. Con un account personale, se ammesso, usa solo atti senza persone fisiche. Dopo la bozza controlla che il modello non abbia copiato numeri, importi o norme dell'atto vecchio.

*Formato e compito.* Un compito per volta: determina e lettera al fornitore sono due richieste.[^13] Se struttura, lunghezza e formato mancano, il modello li deduce.[^14] Per gli atti notificati chiedi anche termine e autorità cui ricorrere (art. 3, comma 4, L. 241/1990).

*Vincoli.* Sono la riga Stile, le ultime quattro righe e il "solo queste" della riga Norme. I più importanti vanno alla fine: se due istruzioni si contraddicono, alcuni modelli seguono l'ultima.[^15] Il modello tende a dare per avvenuti pareri, votazioni e controlli: la riga Fatti glielo vieta. [VERIFICARE] è il permesso di non sapere, che riduce molto le informazioni false;[^16] il motivo dopo i due punti ti dice cosa controllare. "Incoerente" autorizza il modello a dubitare anche dei tuoi dati. L'elenco finale indica dove guardare per primo.[^17] Maiuscole e promesse di ricompensa non servono.[^18]

### L'elenco delle norme

La riga Norme si costruisce una volta e si riusa. Per l'esempio di questo capitolo:

```
NORME DA USARE (verificate su Normattiva il [data])
- D.Lgs. 18 agosto 2000, n. 267 (TUEL), artt. 107 e 183: competenza, impegno.
- TUEL, art. 109, comma 2: funzioni dei responsabili nei Comuni senza dirigenti.
- TUEL, art. 192: determinazione a contrattare.
- D.Lgs. 31 marzo 2023, n. 36, art. 17, commi 1 e 2: decisione di contrarre.
- D.Lgs. 31 marzo 2023, n. 36, art. 50, comma 1, lett. b): affidamento diretto.
- [altre voci, una per riga, con cosa regolano]
```

Se non hai un elenco aggiornato, fai estrarre al modello i riferimenti dell'atto dell'anno prima, tolti i dati personali, senza aggiunte né giudizi sulla vigenza; poi verifica ogni voce con i tre controlli descritti più avanti.

## Il metodo del file di stile

Lo schema dice al modello cosa scrivere. Il file di stile gli dice come.

### Dalle correzioni alle regole

Chi scrive per un responsabile conosce il ciclo: prepari la bozza, il responsabile la corregge, la volta dopo ricordi metà delle correzioni. L'IA non le conserva in modo affidabile tra una conversazione e l'altra; dove c'è una memoria, decide il sistema cosa ricordare. Il file di stile trasforma le correzioni in regole scritte, che controlli tu.

Il passaggio delicato è dalla correzione alla regola. Si mette la bozza accanto alla versione firmata e, per ogni differenza, ci si chiede se riguarda solo quel caso o un'abitudine di chi firma. Le abitudini si scrivono come regole: una riga, un obbligo o un divieto che si possa controllare, con un esempio. Una regola inventata: nell'oggetto, prima l'azione e poi la materia; quindi "Affidamento del servizio di banca dati giuridica", non "Banca dati giuridica – affidamento del servizio". Poi si prova il file su una bozza nuova: se il modello applica male una regola, va riscritta più precisa, non più lunga. Il file è stabile quando le correzioni che restano riguardano il merito, non lo stile.

### Come raccoglierle

Tieni un registro con quattro colonne.

| Data | Prima | Dopo | Regola |
|---|---|---|---|
| 12 marzo 2026 | "Il sottoscritto, visto..." | "Visto..." | Mai la prima persona |
| 19 marzo 2026 | "L'ufficio ha svolto un'accurata istruttoria" | "L'istruttoria si è conclusa il 10 marzo 2026" | Preambolo: solo fatti |

Le correzioni che tornano in almeno due atti diventano regole; le altre restano casi. Il confronto tra bozza e versione firmata può farlo anche il modello, nello strumento autorizzato e senza dati personali.

### Le regole hanno una fonte

Le preferenze di chi firma coincidono spesso con la *Guida alla redazione degli atti amministrativi* dell'allora ITTIG-CNR (oggi IGSG-CNR) e dell'Accademia della Crusca, del 2011, per la quale un testo è economico se contiene "tutto quello che è necessario e solo quello che è adeguato allo sviluppo del suo contenuto".[^19] Dalla Parte I della Guida vengono le regole 3, 4 e 5 del file che segue.[^20] Per la direttiva Frattini dell'8 maggio 2002, le frasi con più di 25 parole sono difficili da capire e ricordare: è un'indicazione, non un limite, e farne la regola 2 è una scelta di questo libro.[^21] La Guida limita l'impersonale ai casi in cui l'agente non serve e apre preambolo e motivazione con "Visto" e "Considerato";[^22] la regola 1 se ne discosta perché registra la scelta di chi firma.

### Un modello di file di stile

È il file usato nell'esperimento di questo capitolo, completato da un esempio.

```
FILE DI STILE – Servizio [nome] – versione [n] del [data]
Applica queste regole al testo degli atti. Non commentarle.
1. Premesse e motivazione impersonali ("si ritiene"). Mai la prima persona.
2. Una frase, un concetto. Di regola sotto le 25 parole.
3. Frasi affermative. Niente doppie negazioni.
4. Indicativo presente: "il responsabile trasmette", non "deve trasmettere".
5. Verbi, non nomi: "occorre liquidare", non "si procede alla liquidazione".
6. Niente aggettivi valutativi né enfasi, salvo le parole della norma applicata.
7. Premesse: solo fatti e atti con numero e data. Le ragioni, in motivazione.
8. Dispositivo: punti numerati, un'azione per punto, infinito ("di impegnare").
9. Norme: citazione completa alla prima occorrenza, poi abbreviata.
10. Sigle per esteso alla prima occorrenza, con la sigla tra parentesi.
11. Importi: "euro 1.200,00". Date: "31 dicembre 2026".
12. Nell'atto niente cortesie né chiusure; gli elenchi richiesti vanno dopo.
13. Se manca un dato o una norma: scrivi [VERIFICARE: cosa]. Non inventare.
Esempio. Prima: "Si rende necessario procedere all'impegno di spesa."
Dopo, in motivazione: "Occorre impegnare la spesa."
Nel dispositivo: "di impegnare la spesa".
```

Nel file "premesse" indica il preambolo. La regola 7 tiene le ragioni nella motivazione, dove le chiede l'art. 3 della L. 241/1990.

### Dove salvarlo

Usa solo lo strumento e l'account che l'ente ti ha messo a disposizione o autorizzato: un account personale, anche a pagamento, può essere contrario al codice di comportamento e alle regole informatiche dell'ente.[^23]

Incolla il file in ogni richiesta, o salvalo nelle istruzioni permanenti dello strumento: un progetto, un Gem, un agente.[^24] Il file di questo capitolo conta circa 1.200 caratteri: controlla i limiti. Gli atti modello vanno nei documenti di riferimento, che non sono trattati come istruzioni.[^25]

Disattiva l'addestramento sulle conversazioni e, salvo diversa indicazione dell'ente, la memoria tra le chat, che può portare in una bozza dati di un'altra pratica. Apri una chat nuova per ogni atto: nelle conversazioni lunghe il modello può perdere di vista le istruzioni iniziali.

### Come aggiornarlo

Metti versione e data in testa al file; aggiungi una regola quando una correzione torna, togli quelle già rispettate; rifai un caso di prova quando cambi regole o strumento, o quando cambia il modello.[^26]

## Prima e dopo: la stessa determina con due prompt

La prova è stata fatta il 6 ottobre 2026 con Claude, di Anthropic, lo stesso modello per entrambi i prompt. Non è una raccomandazione: lo schema vale per ogni strumento. Ogni prompt è stato eseguito tre volte, in conversazioni nuove e separate, senza ricerca sul web, file o altri documenti. I limiti: un solo modello, tre esecuzioni per prompt, un solo caso; con altre prove i numeri cambierebbero, perché anche richieste simili, o la stessa ripetuta, danno testi diversi.[^27] Gli estratti non sono modificati.

Il prompt strutturato è il prompt modello compilato; ecco le righe principali (i puntini indicano i tagli).

```
Sei un istruttore amministrativo del Servizio Affari generali
del Comune di Borgo Esempio.
Contesto: il Comune usa da tre anni una banca dati giuridica on line
di Editrice Esempio S.r.l.; l'abbonamento in corso, affidato con ATTO_1,
scade il 31 dicembre 2026.
Dati: rinnovo per un anno dal 1 gennaio 2027; importo euro 1.200,00
oltre IVA; … affidamento tramite MePA; CIG da acquisire; …
Norme (solo queste) e cosa regolano:
- D.Lgs. 18 agosto 2000, n. 267 (TUEL): art. 107, funzioni dei responsabili; …
Formato: oggetto, preambolo (Visto), motivazione (Considerato),
dispositivo (DETERMINA); circa 700 parole; testo semplice.
Compito: scrivi la bozza della determina a contrarre e di affidamento …
```

Le undici norme sono elencate in nota; lo stile era il file visto sopra. Il testo integrale è nell'allegato "Come è stato scritto questo libro".[^28]

### Tre estratti

Preambolo, testo generico:

> il DURC risulta regolare (prot. [\_\_\_\_\_\_\_\_\_\_], scadenza [\_\_/\_\_/\_\_\_\_]). Il Casellario informatico ANAC non riporta annotazioni ostative;

Nessuno aveva fornito al modello un DURC o una visura. Restano vuoti solo protocollo e scadenza: chi li compila crede di completare un dato, e invece attesta un controllo. Il testo strutturato presenta i controlli come azioni da compiere, di solito con un [VERIFICARE] sull'esito.

Motivazione della scelta del fornitore, testo generico:

> ha eseguito il precedente contratto con puntualità e nel rispetto dei tempi e dei costi pattuiti;

Testo strutturato:

> Editrice Esempio S.r.l. è l'operatore economico uscente e ha eseguito i contratti degli ultimi tre anni [VERIFICARE: esito dell'esecuzione dei contratti precedenti];

Il modello non può sapere com'è andato il contratto. Il testo generico lo afferma in tutte e tre le esecuzioni; quello strutturato qui chiede di accertarlo, altrove motiva con la continuità e con l'importo. Ma dà per certo, in tutte e tre, che ATTO_1 avesse affidato l'abbonamento proprio a Editrice Esempio: il prompt lo lasciava intendere senza dirlo. Un'ambiguità del prompt è diventata un fatto dell'atto.

E qui quella motivazione non serve: sotto i 5.000 euro l'art. 49, comma 6, del Codice consente comunque di derogare alla rotazione negli affidamenti diretti, e tutte e sei le bozze lo citano.[^29] Un fatto non verificato non rafforza la motivazione: la espone.

### Le differenze

| Aspetto | Prompt generico | Prompt strutturato |
|---|---|---|
| Parole dell'atto | 1.400-1.705 | 903-973 |
| Atti normativi citati | 14-15 | 3 |
| Riferimenti controllati | 34-36; in due esecuzioni un contenuto errato, in una un riferimento superato | 11-12, nessun contenuto errato né riferimento superato; alcuni riassunti incompleti |
| Campi tra parentesi quadre | 53-71, nessun [VERIFICARE] | 21-25, tutti [VERIFICARE] |
| Controlli dati per avvenuti | in ogni esecuzione | solo la regolarità tecnica, in ogni esecuzione |
| Punti del dispositivo | 11-15 | 16-19 |

Intervalli tra il valore minimo e il massimo delle tre esecuzioni.[^30]

*Lunghezza.* Il testo strutturato è più corto di circa il 40%, ma supera del 29-39% le 700 parole richieste; in un'esecuzione, con 973 parole, il modello definisce minimo lo sforamento. Chiedi una lunghezza, poi controllala. Sedici-diciannove punti di dispositivo sono troppi per 1.200 euro: è l'effetto della regola 8, un'azione per punto. Per un dispositivo compatto, la regola va riscritta.

*Norme.* Il testo generico conosce la materia ed è aggiornato al correttivo del 2024 (D.Lgs. 31 dicembre 2024, n. 209), ma sbaglia dove l'errore si vede meno, nei contenuti. In due esecuzioni attribuisce all'art. 52, comma 2, del Codice un contenuto che non ha;[^31] in una cita per il divieto di rinnovo tacito una norma del 2005 che modificava una disposizione abrogata nel 2006.[^32] Il testo strutturato cita solo le norme fornite, tutte pertinenti, anche se a volte le riassume in modo incompleto; in un'esecuzione chiede di verificare se ATTO_1 preveda un'opzione di rinnovo: la domanda giusta.[^33] Ma "solo queste" taglia anche ciò che serve. Nessuna bozza strutturata richiama l'art. 192 del TUEL, assente dall'elenco e sempre citato dal testo generico. Mancava anche l'art. 109, comma 2, del TUEL, sui responsabili nei Comuni senza dirigenti: un'esecuzione lo segnala come norma da cercare, un'altra non ne parla. Ora sono entrambi nell'elenco di esempio.

*Fatti e controlli.* È la differenza vera: il testo strutturato lascia aperto perfino l'importo complessivo, IVA compresa, perché il prompt non indicava l'aliquota. Ma tutte e tre le sue bozze attestano nel dispositivo la regolarità tecnica (art. 147-bis del TUEL), che chi firma rende davvero ma che il modello scrive prima di ogni controllo.

*Campi da completare.* Il testo strutturato ne ha meno, e ognuno dice cosa controllare: poco meno della metà sono dati mancanti, gli altri controlli o norme da cercare. Con oltre venti segnalazioni la bozza è più una scheda istruttoria che un testo pronto: il metodo non elimina il completamento, lo rende visibile.

### Cosa ha fatto meglio il prompt generico

Il testo generico ha anticipato questioni che il prompt strutturato non poneva: gli elementi richiesti dall'art. 192 del TUEL (fine, oggetto, forma e clausole essenziali del contratto), stipula, bollo, garanzie, pubblicazione, ricorsi. Nelle note finali ha sollevato dubbi utili, come l'aliquota IVA e l'obbligo di acquistare i servizi informatici tramite Consip. Ma li ha lasciati fuori dall'atto. In un'esecuzione la nota contraddiceva l'atto stesso, che escludeva ogni obbligo di usare il MePA.[^34] Lo schema restituisce solo ciò che chiedi: per cercare ciò che manca, dopo la bozza, usa una richiesta aperta.

```
Bozza di [tipo di atto]:
[testo]
Fine della bozza. Non riscriverla. Elenca ciò che un atto di questo tipo
dovrebbe contenere e qui manca: istruttoria, pareri, clausole, ricorsi.
Ignora i campi tra parentesi quadre. Dividi in "richiesto da una norma"
e "di prassi". Se citi una norma, aggiungi [VERIFICARE].
```

Il metodo non rende il modello più competente. Sposta gli errori da dove non li vedi a dove li vedi.

## Il prompt e i dati personali

Quello che scrivi in un prompt arriva al fornitore dello strumento. Se contiene dati personali è un trattamento, e vale il Regolamento (UE) 2016/679 (GDPR) a partire dalla minimizzazione: dati "adeguati, pertinenti e limitati a quanto necessario rispetto alle finalità".[^35] Per la bozza di un atto non serve quasi mai sapere chi è la persona.

La prima regola dipende dallo strumento. Qui "strumento autorizzato" è quello scelto dall'ente, con un contratto che designa il fornitore responsabile del trattamento (art. 28 GDPR). Un account personale, gratuito o a pagamento, si usa per il lavoro solo se l'ente o il responsabile lo ammettono per iscritto; e con un account personale, come con ogni strumento senza quel contratto, nel prompt non c'è nulla che riporti a una persona: né dati, né segnaposto, né fatti del caso. Chiedi solo testi senza persone o modelli generici. Contributi, dinieghi e sanzioni su casi concreti passano solo dallo strumento autorizzato.

Se per errore incolli dati personali in uno strumento non autorizzato, annota cosa e quando, cancella la conversazione e avvisa subito il responsabile e il responsabile della protezione dei dati. Può essere una violazione di dati personali: l'ente la valuta e, se ne ricorrono i presupposti, la notifica al Garante entro 72 ore da quando ne è venuto a conoscenza (art. 33 GDPR) e, se il rischio è elevato, la comunica agli interessati (art. 34).

### Cosa non mettere nel prompt

Vale per ogni strumento, anche quello autorizzato:

- identificativi diretti e indiretti: nome, codice fiscale, IBAN, indirizzo, targa, numero di protocollo o di pratica;
- le persone fisiche degli atti di spesa, come professionisti, ditte individuali o il RUP: anche nome e partita IVA di un professionista sono dati personali;
- negli atti su una persona, numero e data degli atti precedenti: con il nome del Comune portano all'albo online, e da lì alla persona;
- categorie particolari di dati (art. 9 GDPR), come salute, disabilità, origine etnica, convinzioni religiose;
- dati su condanne e reati (art. 10 GDPR) e dati di minori;
- dettagli che, combinati, in un piccolo Comune rendono riconoscibile qualcuno: frazione, età, mestiere, carica, parentela, un evento noto.

Per i dati sulla salute c'è un motivo in più: non possono essere diffusi (art. 2-septies, comma 8, del D.Lgs. 30 giugno 2003, n. 196, Codice privacy),[^36] e una bozza che li contiene può finire all'albo online (si veda il capitolo sulla privacy prima della pubblicazione). Nella regola del semaforo (si veda il capitolo sugli strumenti) sono rossi e restano fuori dal prompt anche con lo strumento autorizzato: al loro posto, il requisito o la norma applicata.

### Segnaposto al posto dei dati

Con lo strumento autorizzato, i dati che servono alla bozza si sostituiscono con segnaposto.

| Nel fascicolo | Nel prompt |
|---|---|
| nome e cognome del richiedente | RICHIEDENTE_1 |
| codice fiscale, IBAN, targa | niente: non servono alla bozza |
| indirizzo dell'immobile | IMMOBILE_1 |
| numero di protocollo dell'istanza | PROT_1 |
| atti precedenti sulla persona | ATTO_1, ATTO_2 |
| invalidità certificata | requisito previsto dall'art. [n] del regolamento |
| nome del Comune | un Comune di [numero] abitanti |

Anche una formula generica come "requisito previsto dall'art. [n] del regolamento", accanto a data e oggetto della pratica, può rivelare un dato sulla salute: usala solo se serve. La tabella di corrispondenza resta nell'ente, in un file separato e protetto; i dati veri si reinseriscono a mano nel sistema documentale.

### Pseudonimizzare non è anonimizzare

Sostituire i nomi con segnaposto è, nel migliore dei casi, pseudonimizzazione: i dati non si attribuiscono a una persona senza informazioni aggiuntive, conservate a parte e protette (art. 4, n. 5, GDPR). Se restano dettagli che identificano, non lo è nemmeno. E i dati pseudonimizzati restano personali, almeno per il Comune che conserva la tabella.[^37] L'anonimato richiede di neutralizzare individuazione, correlabilità e deduzione.[^38] In un piccolo Comune la deduzione è il rischio più concreto: "un'anziana della frazione alta con invalidità totale" si riconosce anche senza nome.

Il segnaposto riduce il rischio, non gli obblighi. Per trovare i dettagli che identificano, con lo strumento autorizzato:

```
Testo pseudonimizzato (RICHIEDENTE_1 e simili sostituiscono persone):
[testo pseudonimizzato]
Fine del testo. Il Comune ha circa [numero] abitanti.
Segnala ogni dettaglio che, da solo o con altri, può far riconoscere
una persona: luoghi, età, mestieri, cariche, parentele, eventi, salute,
minori, nomi o codici rimasti.
Rispondi con una tabella: dettaglio, perché identifica, formula più generica.
Non riscrivere il testo. Non dichiararlo anonimo: decide l'ufficio.
```

### Quando serve uno strumento autorizzato

Se la bozza non si può scrivere senza dati personali, serve lo strumento autorizzato dall'ente, con il contratto che designa il fornitore responsabile del trattamento e, se è un servizio cloud, qualificato dall'Agenzia per la cybersicurezza nazionale (ACN). Il fornitore tratta i dati "soltanto su istruzione documentata del titolare" (art. 28 GDPR): il contratto deve escludere l'addestramento dei suoi modelli e dire dove i dati sono trattati.[^39] Fuori dallo Spazio economico europeo servono le garanzie del capo V del GDPR.[^40]

Coinvolgi il responsabile della protezione dei dati, annota il trattamento nel registro e aggiorna l'informativa se cambiano finalità, destinatari o trasferimenti (artt. 13, 14, 30, 37 e 38 GDPR). Se il rischio può essere elevato serve la valutazione d'impatto (art. 35), che l'elenco del Garante richiede per i sistemi di IA quando ricorre almeno un altro criterio di rischio.[^41] I dettagli sono nei capitoli sul GDPR.

Se il tuo ente non ha ancora regole, chiedi al responsabile, per e-mail, quale strumento puoi usare e per quali atti, e conserva la risposta; puoi proporre di partire dai testi senza persone e dai modelli generici. Finché non hai una risposta scritta, non usare l'IA per il lavoro d'ufficio: esercitati fuori servizio su casi inventati, come quelli di Borgo Esempio. Il capitolo sul regolamento interno propone un modello di regole per l'ente.

## Chi firma risponde

La L. 23 settembre 2025, n. 132, in vigore dal 10 ottobre 2025, dedica l'art. 14 all'IA nella pubblica amministrazione. Il comma 2 fissa il punto: l'IA si usa "in funzione strumentale e di supporto all'attività provvedimentale", e la persona che decide "resta l'unica responsabile dei provvedimenti e dei procedimenti in cui sia stata utilizzata l'intelligenza artificiale".[^42]

Il comma 1 chiede di assicurare agli interessati "la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo", il comma 3 misure tecniche, organizzative e formative.[^43] Ne derivano due regole pratiche. La bozza dell'IA non è mai l'atto. L'uso dell'IA si annota nel fascicolo con strumento, data, prompt e versione del file di stile: la legge non lo prescrive, ma è una prassi coerente con la tracciabilità (si veda il capitolo sulla tracciabilità). I prompt archiviati sono accessibili come il resto del fascicolo: niente dati personali, niente commenti.

Per l'AI Act il Comune che usa l'IA è un "deployer". Qui contano tre punti; il resto è nel capitolo sull'AI Act.[^44]

- Alfabetizzazione. L'art. 4, applicabile dal 2 febbraio 2025, chiede a fornitori e deployer misure per garantire "nella misura del possibile" un "livello sufficiente" di alfabetizzazione del personale. Il Regolamento (UE) 2026/1744 lo ha riscritto; secondo le prime sintesi resta un obbligo di mezzi, non di risultato.[^45] Per l'ente, in ogni caso, valgono le misure formative dell'art. 14, comma 3, della L. 132/2025.
- Alto rischio. Scrivere una determina con un chatbot generalista non è un uso ad alto rischio: la redazione di atti non è nell'Allegato III. Lo è l'IA usata per valutare il diritto a prestazioni di assistenza pubblica essenziali, o per concederle, ridurle o revocarle (Allegato III, punto 5, lettera a)). Dal 2 dicembre 2027 questi usi comportano obblighi pesanti, tra cui la valutazione d'impatto sui diritti fondamentali (artt. 26 e 27).[^46] Nel frattempo valgono già il GDPR, la L. 132/2025 e, dell'AI Act, l'art. 4 e i divieti dell'art. 5, come quello sul punteggio sociale. Non chiedere mai all'IA se il richiedente ha diritto al contributo.
- Trasparenza. Dal 2 agosto 2026 il deployer che pubblica testi generati con l'IA per informare il pubblico su questioni di interesse pubblico deve dichiararlo, salvo revisione umana o controllo editoriale e responsabilità editoriale di una persona fisica o giuridica (art. 50, paragrafo 4). Riguarda soprattutto avvisi o notizie pubblicati sul sito senza revisione; un atto rivisto e firmato di regola rientra nell'eccezione, ma l'ente può comunque dichiarare l'uso dell'IA (si veda il capitolo sul regolamento interno).

L'art. 22 del GDPR vieta, in linea di principio, le decisioni basate unicamente sul trattamento automatizzato che producono effetti giuridici sulla persona o incidono in modo analogo significativamente su di lei. L'intervento umano deve essere significativo, non simbolico, e venire da chi può cambiare la decisione:[^47] una firma senza un esame reale non basta. Il Consiglio di Stato chiede che la decisione algoritmica sia conoscibile, non esclusiva e non discriminatoria.[^48] Va nella stessa direzione la bozza di linee guida dell'Agenzia per l'Italia Digitale (AgID), posta in consultazione nel 2025: i sistemi devono consentire "la verifica, correzione o sostituzione da parte di personale umano".[^49] La bozza non è vincolante e, a ottobre 2026, non risulta ancora adottata in via definitiva.

Rivedere, però, non significa rileggere. Quando il modello sbaglia, chi lo usa tende a sbagliare con lui: in un esperimento di Microsoft l'accuratezza degli utenti è scesa sotto il 50%,[^50] e fra i consulenti di Boston Consulting Group chi usava l'IA aveva 19 punti percentuali di probabilità in più di sbagliare.[^51] E più fiducia nell'IA si associa a meno pensiero critico.[^52] Leggi quindi prima il dispositivo, che produce gli effetti. Poi confronta numeri, date e nomi con il fascicolo, verifica le norme e chiediti se la motivazione sostiene una decisione che firmeresti.

## Le allucinazioni normative

Si chiama allucinazione un'informazione falsa che il modello presenta come vera. Negli atti la più pericolosa riguarda le norme: un articolo che non esiste, che dice altro o che non è più in vigore.

### Cosa dicono studi e giudici

Su casi giudiziari federali statunitensi, i modelli generalisti hanno sbagliato tra il 58% e l'88% delle risposte; gli strumenti professionali di ricerca giuridica, tra il 17% e il 33%.[^53] Una banca dati riduce gli errori, ma non li elimina. Lo riconoscono anche i produttori dei modelli: le loro tecniche riducono le allucinazioni senza eliminarle, e chiedere la fonte non basta.[^54]

In Italia i giudici sono passati in poco più di un anno dalla tolleranza alla sanzione.[^55] Nel 2026 la Cassazione penale ha dichiarato inammissibili due ricorsi, probabilmente scritti con l'IA e non controllati: entrambi attribuivano ai precedenti citati principi mai affermati. Nel primo caso le sentenze esistevano, ma erano di altre sezioni. Nel secondo la Corte ha precisato che citare precedenti inesistenti aggrava la colpa, e ne ha tenuto conto nella somma dovuta alla Cassa delle ammende.[^56]

Sono casi di avvocati. Per l'amministrazione, nel 2026 il TAR Marche ha respinto la censura contro una relazione istruttoria di gara con richiami giurisprudenziali inesatti, che secondo il ricorrente era scritta con l'IA: l'IA come supporto non viola di per sé la "riserva di umanità" se la decisione resta controllata, motivata e imputabile al funzionario.[^57] Nelle ricerche per questo libro non sono emersi casi di determine o delibere censurate per norme inventate dall'IA. Ma la regola è già nella legge: chi firma risponde.

### La regola [VERIFICARE]

Ogni riferimento normativo o giurisprudenziale prodotto dall'IA resta [VERIFICARE] finché non supera tre controlli.

1. Esistenza. Cerca l'atto nelle fonti istituzionali indicate in nota per estremi (tipo, numero, anno; per le sentenze anche autorità e sezione), non per il titolo suggerito dall'IA.[^58]
2. Contenuto. Leggi l'articolo o il passo citato: nel primo caso della Cassazione la sentenza esisteva, il principio no.
3. Vigenza alla data dell'atto. Usa il testo vigente a quella data e controlla gli "Aggiornamenti all'atto" su Normattiva.

Normattiva non segnala le abrogazioni implicite e i suoi testi non sono ufficiali: prevale la Gazzetta Ufficiale.[^59] Il capitolo sulla verifica delle norme descrive il controllo passo per passo e i riferimenti superati più frequenti, come l'informativa "ai sensi dell'art. 13 del D.Lgs. 196/2003", articolo abrogato dal D.Lgs. 10 agosto 2018, n. 101.[^60]

Per organizzare la verifica, nella stessa conversazione della bozza, chiedi al modello l'origine di ogni riferimento.

```
Rileggi la bozza che hai scritto. Non correggerla. Elenca in una tabella
i riferimenti a norme, regolamenti, sentenze e linee guida, con articolo
e comma, cosa regolano nell'atto e origine.
Origine: "fornito" se atto, articolo e comma sono nell'elenco qui sotto;
"articolo diverso" se c'è solo l'atto; "aggiunto" negli altri casi.
In fondo scrivi il totale. Non dire se le norme sono vigenti.
Elenco fornito: [incolla di nuovo l'elenco delle norme]
```

Non è una verifica, è una lista di lavoro: comincia dagli "aggiunti" e dagli "articolo diverso". Anche questa classificazione può sbagliare: confronta il totale con una ricerca di "art." nel testo.

Un caso dell'esperimento mostra perché servono tutti e tre i controlli. Per il divieto di rinnovo tacito, una delle bozze generiche citava l'art. 23 della L. 18 aprile 2005, n. 62. Il controllo di esistenza lo lascia passare: la legge c'è. Quello sul contenuto mostra che l'articolo è una modifica: interveniva sull'art. 6 della L. 24 dicembre 1993, n. 537. Quello sulla vigenza chiude la questione: l'art. 6 è stato abrogato dall'art. 256 del D.Lgs. 12 aprile 2006, n. 163. Il divieto resta, affermato dalla giurisprudenza amministrativa: la bozza aveva ragione sul principio e torto sulla fonte. Un riferimento esistente e pertinente è il più difficile da scartare: per questo la verifica segue il rinvio fino alla norma modificata.

## L'IA come moltiplicatore: dove fa risparmiare tempo, e dove no

Negli esperimenti il risparmio è forte: chi usava ChatGPT ha svolto compiti di scrittura con il 40% di tempo in meno e una qualità più alta del 18%.[^61] Ma i compiti erano scelti tra i più adatti all'IA, e in uno studio di Microsoft gli utenti credevano di aver risparmiato 36 minuti, ed erano 12.[^62] Anche nell'amministrazione britannica il risparmio stimato con un gruppo di confronto è risultato inferiore a quello dichiarato.[^63]

Il risparmio dipende dal compito, e il confronto giusto è con il copia e incolla, non con la pagina bianca. La tabella è una valutazione di questo libro, in parte confermata dagli studi.[^64]

| Attività | Risparmio | Perché |
|---|---|---|
| Atti ripetitivi | basso | l'atto dell'anno prima si copia già |
| Primo atto di un tipo raro | alto | il modello propone la struttura, tu la controlli |
| Riscrittura nello stile dell'ufficio | alto | regole esplicite nel file di stile |
| Sintesi di documenti forniti | medio | va controllata la completezza |
| Ricerca e citazione di norme | basso o nullo | ogni riferimento va verificato |
| Calcoli e tabelle | negativo | più lento e meno preciso |
| Motivazione di un caso nuovo | nessuno | è la decisione di chi firma |

Il guadagno viene dal metodo, non dallo strumento. Parte del tempo guadagnato sulla bozza va reinvestita nella verifica: altrimenti non hai risparmiato tempo, hai spostato il rischio su chi firma.

*Prova tu.* Prendi un atto che conosci bene e un caso inventato, e scrivilo tre volte: senza IA, partendo dall'atto dell'anno prima; con un prompt generico; con il metodo completo. Cronometra ogni versione fino al testo che firmeresti, non fino alla prima bozza: il tempo comprende prompt, lettura, verifica delle norme e correzioni, anche nella versione copiata, che può portarsi dietro riferimenti superati. Annota quanti errori trovi in ciascuna. Dalla seconda volta il caso lo conosci già: se ripeti la prova, cambia l'ordine. Un solo atto non basta per decidere: prova anche altri tipi di atto, a cominciare da quelli della tabella.

## Checklist del metodo

Prima del prompt:

1. Lo strumento è autorizzato per il tipo di dati: per testi senza persone basta l'autorizzazione scritta dell'ente o del responsabile; con dati personali, anche pseudonimizzati, serve lo strumento dell'ente con il contratto dell'art. 28 GDPR, e un'e-mail non basta.
2. Con un account personale, anche a pagamento, o uno strumento senza quel contratto, nel prompt non c'è nulla che riporti a una persona: né dati, né segnaposto, né fatti del caso.
3. Con lo strumento dell'ente, nessun identificativo né dettaglio che renda riconoscibile la persona; mai dati su salute, condanne e reati o minori: al loro posto il requisito o la norma applicata. I segnaposto non rendono anonimo il testo.
4. Prompt in cinque parti, norme da un elenco verificato, file di stile aggiornato, chat nuova.
5. Dati personali incollati per errore in uno strumento non autorizzato: avvisi subito il responsabile e il responsabile della protezione dei dati.

Dopo la bozza:

6. Hai letto i [VERIFICARE] e usato i prompt su ciò che manca e sull'origine delle norme.
7. Ogni norma ha superato i tre controlli: esistenza, contenuto, vigenza.

Prima della firma:

8. Nell'atto non restano parentesi quadre né segnaposto: cerca il carattere `[` e le parole in maiuscolo con il trattino basso.
9. Hai letto prima il dispositivo, poi la motivazione: la decisione è quella che firmeresti, e la motivazione la regge.
10. Il fascicolo registra strumento, data, prompt e versione del file di stile.

[^1]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, su un campione di 500 dipendenti pubblici, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Il 66% comprende chi usa l'IA ogni giorno o almeno una volta a settimana. Sintesi e analisi di documenti e redazione di testi sono indicate ciascuna dal 59% di chi usa l'IA. Sono dati dichiarati dagli intervistati.

[^2]: Fondazione IFEL, *Intelligenza artificiale nei Comuni italiani. Competenze, governance, territori*, 2026, fondazioneifel.it. Indagine su 664 dirigenti e funzionari comunali, svolta nell'ambito del progetto AI-PACT. La scheda dell'IFEL parla di "oltre il 40%" di utilizzatori; il 41,9% e il dato sulla formazione sono riportati da Federprivacy, *Il 55% dei dipendenti comunali che usa strumenti di intelligenza artificiale non ha ricevuto alcuna formazione*, 2026, federprivacy.org, e da ItaliaOggi, 2026, italiaoggi.it.

[^3]: ITTIG-CNR (oggi IGSG-CNR) e Accademia della Crusca, *Guida alla redazione degli atti amministrativi. Regole e suggerimenti*, 2011, ittig.cnr.it, Parte II.

[^4]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 3, comma 1, normattiva.it.

[^5]: M. Dahl, V. Magesh, M. Suzgun, D. E. Ho, *Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models*, in Journal of Legal Analysis, vol. 16, n. 1, 2024, pp. 64-93, law.stanford.edu.

[^6]: Anthropic, *Prompting best practices*, 2026, platform.claude.com; OpenAI, *GPT-4.1 Prompting Guide*, OpenAI Cookbook, 2025, github.com; Google Cloud, *Prompt Design: Best Practices*, 2025, github.com; Microsoft, *Getting more out of Microsoft 365 Copilot with purposeful prompts*, 2024, microsoft.com. La formula "ruolo, contesto, compito, formato, vincoli" è una sintesi dell'autore.

[^7]: Anthropic, *Prompting best practices*, cit., sezione "Give Claude a role". Google avverte che un modello troppo legato al personaggio a volte ignora altre istruzioni: Google Cloud, *Prompt Design: Best Practices*, cit.

[^8]: Anthropic, *Prompting best practices*, cit., sezioni "Be clear and direct" e "Add context to improve performance".

[^9]: Anthropic, *Prompting best practices*, cit., sezione "Long context prompting": nei test del produttore, con documenti di oltre 20.000 token (decine di pagine), mettere la richiesta in fondo ha migliorato la qualità fino al 30%. Per una bozza di poche pagine l'ordine conta meno.

[^10]: OpenAI, *GPT-4.1 Prompting Guide*, cit., e Google Cloud, *Prompt Design: Best Practices*, cit., suggeriscono di usare solo i documenti forniti e di trattare il contesto come unica fonte.

[^11]: Anthropic, *Prompting best practices*, cit., sezione "Use examples effectively", che ne consiglia da 3 a 5; Google Cloud, *Prompt Design: Best Practices*, cit., che ne indica da 1 a 5 e avverte che troppi esempi vengono ricalcati. Il limite di uno o due esempi per gli atti lunghi è una scelta di questo libro.

[^12]: Anthropic, *Prompt engineering for Claude's long context window*, 2023, anthropic.com. In un test interno su documenti governativi di circa 70.000-95.000 token, citazioni ed esempi pertinenti hanno ridotto gli errori del 36%.

[^13]: Google Cloud, *Prompt Design: Best Practices*, cit.

[^14]: Microsoft, *Write effective instructions for declarative agents*, 2026, github.com; Anthropic, *Prompting best practices*, cit., sezione "Control the format of responses", che consiglia di dire cosa fare, non solo cosa evitare.

[^15]: Google Cloud, *Prompt Design: Best Practices*, cit., che consiglia di chiudere con la richiesta principale e i limiti più importanti; OpenAI, *GPT-4.1 Prompting Guide*, cit., che osserva in un suo modello la tendenza a seguire l'istruzione più vicina alla fine.

[^16]: Anthropic, *Reduce hallucinations*, 2026, platform.claude.com; OpenAI, *GPT-5.2 Prompting Guide*, OpenAI Cookbook, 2025, github.com, che chiede di non inventare mai cifre o riferimenti in caso di dubbio.

[^17]: Microsoft, *Write effective instructions for declarative agents*, cit.

[^18]: OpenAI, *GPT-4.1 Prompting Guide*, cit.: "It's generally not necessary to use all-caps or other incentives like bribes or tips".

[^19]: ITTIG-CNR (oggi IGSG-CNR) e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Principi generali, che indicano chiarezza, precisione, uniformità, semplicità ed economia. La Guida è stata presentata all'Accademia della Crusca l'11 febbraio 2011.

[^20]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I: frasi affermative, indicativo presente al posto di "dovere" più infinito, verbi al posto dei nomi derivati ("si paga allo sportello", non "il pagamento si effettua allo sportello").

[^21]: Ministro per la Funzione pubblica, *Direttiva sulla semplificazione del linguaggio dei testi amministrativi*, 8 maggio 2002, in Gazzetta Ufficiale n. 141 del 18 giugno 2002, gazzettaufficiale.it. La direttiva raccomanda frasi brevi, parole comuni e verbi in forma attiva e affermativa, e di evitare, per quanto possibile, sigle, neologismi, parole straniere e latinismi.

[^22]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I, sull'uso di passivo e impersonale, e Parte II, su preambolo ("Visto") e motivazione ("Considerato"). Che lo schema sostituisca formule come "premesso che" o "dato atto che" lo esplicita R. Libertini, *Un nuovo schema per la motivazione degli atti amministrativi: i visto e i considerato*, in Informatica e diritto, 2016, n. 2, ittig.cnr.it.

[^23]: D.P.R. 16 aprile 2013, n. 62, *Codice di comportamento dei dipendenti pubblici*, art. 11-bis, inserito dal D.P.R. 13 giugno 2023, n. 81, sull'uso delle tecnologie informatiche; codice di comportamento dell'ente (art. 54, comma 5, D.Lgs. 30 marzo 2001, n. 165), normattiva.it. Nei piani personali di Claude (Free, Pro e Max) le conversazioni possono essere usate per addestrare i modelli se l'utente non disattiva l'impostazione nell'account; i servizi commerciali (Team, Enterprise e uso tramite API) ne sono esclusi: Anthropic, *Updates to Consumer Terms and Privacy Policy*, 2025, e *Commercial Terms of Service*, 2025, anthropic.com. Un piano personale resta un piano per consumatori anche se è a pagamento.

[^24]: In ChatGPT: Progetti, che riuniscono chat, file e istruzioni, oppure Istruzioni personalizzate, impostate per l'intero account e applicate alle nuove conversazioni, anche personali (per il lavoro è meglio un progetto). In Claude: istruzioni del progetto, applicate a tutte le chat del progetto. In Gemini: Gem. In Microsoft 365 Copilot: istruzioni di un agente creato con Agent Builder, fino a 8.000 caratteri. Fonti: Anthropic, *What are projects?*, 2026, support.claude.com; Microsoft, *Build agents with Agent Builder* e *Agent capabilities and licensing*, 2026, github.com; Microsoft, *Write effective instructions for declarative agents*, cit.; OpenAI, *Projects in ChatGPT* e *ChatGPT Custom Instructions*, help.openai.com. Disponibilità per piano e limiti cambiano spesso: controllali nelle pagine di assistenza dei produttori.

[^25]: Microsoft, *Write effective instructions for declarative agents*, cit. In Microsoft 365 Copilot Chat senza licenza, se l'ente non ha attivato la fatturazione a consumo (pay-as-you-go), gli agenti non possono usare come fonti i file incorporati, i dati di SharePoint e i connettori: Microsoft, *Agent capabilities and licensing*, cit.

[^26]: Microsoft, *New Future of Work Report 2024*, 2024, microsoft.com.

[^27]: Microsoft, *New Future of Work Report 2023*, 2023, microsoft.com, secondo cui anche richieste di significato simile producono risultati molto diversi e chi non è esperto di prompt fatica di più.

[^28]: Nel prompt ogni norma era indicata con cosa regola: D.Lgs. 18 agosto 2000, n. 267 (TUEL), artt. 107, 147-bis, 151, comma 4, e 183; D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici), artt. 17, commi 1 e 2, 25, 26, 49, comma 6, 50, comma 1, lett. b), e 52; L. 13 agosto 2010, n. 136, art. 3. Il file di stile era quello riportato in questo capitolo, senza l'esempio finale, con l'intestazione "Servizio Affari generali – versione 1 del 6 ottobre 2026". Il prompt comprendeva anche la riga Esempio ("nessuno") e le quattro righe di vincolo del prompt modello. Comune, servizio, ditta e atti dell'esperimento sono inventati.

[^29]: D.Lgs. 31 marzo 2023, n. 36, art. 49, comma 6, sulla deroga al principio di rotazione negli affidamenti diretti sotto i 5.000 euro, e comma 4, che ammette il riaffidamento al contraente uscente in casi motivati con riferimento alla struttura del mercato e all'effettiva assenza di alternative, nonché all'accurata esecuzione del precedente contratto, normattiva.it. In un'esecuzione il testo generico fonda la scelta sul comma 4 citando solo la buona esecuzione.

[^30]: Conteggi sui testi integrali. Le parole dell'atto vanno dall'oggetto alla firma, escluse intestazione e certificato di pubblicazione; in una bozza generica comprendono anche il visto contabile, in un'altra anche i campi vuoti tra parentesi quadre (senza, sono 1.666). Dopo l'atto il testo generico aggiunge 140-211 parole di note per la compilazione, quello strutturato 399-528 parole di elenchi dei [VERIFICARE] e delle assunzioni. Atti normativi e riferimenti sono contati solo nell'atto, gli atti normativi una volta sola: con le note, il generico arriva a 16 atti normativi e a 35-37 riferimenti. I riferimenti sono stati controllati su banche dati e siti specializzati. La ripartizione dei [VERIFICARE] tra dati mancanti, controlli e norme da cercare è stata fatta su due esecuzioni. Nelle bozze del prompt strutturato gli altri controlli sono presentati come azioni da compiere; dell'attestazione di regolarità tecnica si dice nel testo.

[^31]: Le bozze vi leggono il pagamento delle prestazioni nei limiti della loro utilità, che la norma non prevede, e tacciono comunicazione all'ANAC e sospensione dell'operatore. D.Lgs. 31 marzo 2023, n. 36, art. 52, comma 2: se la verifica non conferma i requisiti, la stazione appaltante risolve il contratto, escute l'eventuale garanzia definitiva, comunica il fatto all'ANAC e sospende l'operatore da uno a dodici mesi, normattiva.it. Il pagamento nei limiti dell'utilità ricevuta viene dalla prassi del vecchio Codice (Linee guida ANAC n. 4).

[^32]: L. 18 aprile 2005, n. 62, art. 23, che modificava l'art. 6 della L. 24 dicembre 1993, n. 537, poi abrogato dall'art. 256 del D.Lgs. 12 aprile 2006, n. 163, normattiva.it. Il divieto di rinnovo tacito resta affermato dalla giurisprudenza amministrativa.

[^33]: Un'opzione di rinnovo prevista in clausole chiare, precise e inequivocabili dei documenti di gara iniziali, e computata nel valore stimato dell'appalto, si può esercitare senza una nuova procedura: D.Lgs. 31 marzo 2023, n. 36, art. 120, comma 1, lett. a), che parla di clausole di opzione, e art. 14, comma 4, sul valore stimato comprensivo di opzioni e rinnovi esplicitamente stabiliti, normattiva.it.

[^34]: L. 28 dicembre 2015, n. 208, art. 1, comma 512, sugli acquisti di beni e servizi informatici tramite Consip o soggetti aggregatori, normattiva.it.

[^35]: Regolamento (UE) 2016/679, *Regolamento generale sulla protezione dei dati*, art. 5, par. 1, lett. c), eur-lex.europa.eu. Si veda anche l'art. 25 sulla protezione dei dati per impostazione predefinita.

[^36]: D.Lgs. 30 giugno 2003, n. 196, *Codice in materia di protezione dei dati personali*, art. 2-septies, comma 8, che vieta la diffusione dei dati genetici, biometrici e relativi alla salute indicati nel comma 1, normattiva.it.

[^37]: Regolamento (UE) 2016/679, cit., art. 4, n. 5, e considerando 26, per il quale i dati pseudonimizzati "dovrebbero essere considerati informazioni su una persona fisica identificabile"; EDPB, *Guidelines 01/2025 on Pseudonymisation*, versione adottata per la consultazione pubblica, 2025, edpb.europa.eu. Secondo la Corte di giustizia, dati pseudonimizzati possono non essere personali per un destinatario che non ha mezzi ragionevoli per reidentificare gli interessati, ma restano personali per il titolare che conserva le informazioni aggiuntive: Corte di giustizia UE, sentenza 4 settembre 2025, causa C-413/23 P, GEPD c. SRB, curia.europa.eu. La proposta della Commissione COM(2025) 837 del 19 novembre 2025 (Digital Omnibus) prevede tra l'altro modifiche al GDPR: finché non è adottata e pubblicata nella Gazzetta ufficiale dell'Unione, non è diritto vigente.

[^38]: Gruppo di lavoro Articolo 29, *Parere 05/2014 sulle tecniche di anonimizzazione* (WP216), 2014, ec.europa.eu.

[^39]: Regolamento (UE) 2016/679, cit., art. 28, paragrafi 1 e 3, lett. a). Il fornitore che decidesse da sé le finalità del trattamento sarebbe considerato titolare (art. 28, par. 10).

[^40]: Regolamento (UE) 2016/679, cit., artt. 44-46. Islanda, Norvegia e Liechtenstein fanno parte dello Spazio economico europeo e non sono Paesi terzi. Per un fornitore statunitense: la decisione di adeguatezza sul quadro UE-USA, valida solo se il fornitore è certificato (Decisione di esecuzione (UE) 2023/1795 della Commissione, del 10 luglio 2023, eur-lex.europa.eu), oppure le clausole contrattuali tipo (art. 46). Con le clausole contrattuali tipo l'esportatore deve valutare il livello di protezione garantito nel Paese terzo: Corte di giustizia UE, sentenza 16 luglio 2020, causa C-311/18, Data Protection Commissioner c. Facebook Ireland e Schrems (Schrems II), curia.europa.eu.

[^41]: Regolamento (UE) 2016/679, cit., artt. 13, 14, 30, 35 (il par. 2 prevede la consultazione del responsabile della protezione dei dati), 37, par. 1, lett. a), e 38, par. 1; Garante per la protezione dei dati personali, *Elenco delle tipologie di trattamenti soggetti al requisito di una valutazione d'impatto*, allegato 1 al provvedimento n. 467 dell'11 ottobre 2018, garanteprivacy.it, che rinvia ai criteri delle linee guida del Gruppo di lavoro Articolo 29 sulla valutazione d'impatto (WP 248 rev. 01).

[^42]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 2, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, gazzettaufficiale.it.

[^43]: L. 23 settembre 2025, n. 132, cit., art. 14, commi 1 e 3. La legge non prevede una formula da inserire nell'atto: se e come dichiarare l'uso dell'IA lo decide il regolamento dell'ente.

[^44]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, artt. 3, n. 4, 4, 5, 6, parr. 3 e 4, 25, par. 1, lett. c), 26, 27, 49, 50, par. 4, 86, 113 e Allegato III, punto 5, eur-lex.europa.eu. Gli artt. 4 e 5 si applicano dal 2 febbraio 2025 (art. 113, lett. a)). L'art. 50, par. 4, esclude l'obbligo di trasparenza anche per gli usi autorizzati dalla legge per accertare, prevenire, indagare o perseguire reati; la sua applicazione sarà precisata da linee guida e codici di condotta della Commissione. Per una sintesi delle modifiche del 2026: DirittoBancario, *Digital omnibus sull'IA: in GU UE le modifiche all'AI Act*, 2026, dirittobancario.it.

[^45]: Nel testo originario dell'art. 4 fornitori e deployer "adottano misure per garantire nella misura del possibile un livello sufficiente di alfabetizzazione in materia di IA del loro personale". La modifica è del Regolamento (UE) 2026/1744 del Parlamento europeo e del Consiglio, dell'8 luglio 2026, che modifica i regolamenti (UE) 2024/1689, (UE) 2018/1139 e (UE) 2023/1230 per quanto riguarda la semplificazione dell'attuazione di regole armonizzate sull'intelligenza artificiale (omnibus digitale sull'IA), pubblicato nella Gazzetta ufficiale dell'Unione europea, serie L, del 24 luglio 2026 e in vigore dal 27 luglio 2026, eur-lex.europa.eu. Il contenuto del nuovo art. 4 è riportato qui secondo fonti secondarie concordanti, che lo descrivono come un obbligo di mezzi: Federprivacy, *AI Literacy, cosa cambia dopo l'entrata in vigore del Digital Omnibus on AI*, 2026, federprivacy.org; DirittoBancario, cit.

[^46]: Per gli enti pubblici che usano sistemi dell'Allegato III: sorveglianza umana (art. 26, par. 2); registrazione propria e dell'uso nella banca dati dell'Unione, senza la quale il sistema non si può usare (art. 26, par. 8, e art. 49, par. 3); informazione alle persone interessate (art. 26, par. 11); valutazione d'impatto sui diritti fondamentali prima dell'uso, coordinata con quella del GDPR (art. 27); diritto alla spiegazione delle singole decisioni (art. 86). Chi usa un sistema generalista per questi scopi ne cambia la finalità e può diventarne fornitore (art. 25). La deroga dell'art. 6, par. 3, per i sistemi che non influenzano in modo sostanziale la decisione la valuta e la documenta il fornitore (art. 6, par. 4) e non vale mai se il sistema effettua profilazione. La data del 2 dicembre 2027, al posto del 2 agosto 2026, riguarda gli obblighi del capo III, sezioni 1-3, tra cui quelli degli artt. 26 e 27; è fissata dall'art. 113 del Regolamento (UE) 2024/1689, come modificato dal Regolamento (UE) 2026/1744, cit. Già oggi valgono gli artt. 22 e 35 del GDPR e l'art. 14 della L. 132/2025.

[^47]: Regolamento (UE) 2016/679, cit., art. 22 e considerando 71; Corte di giustizia UE, sentenza 7 dicembre 2023, causa C-634/21, SCHUFA Holding, curia.europa.eu, secondo cui anche il calcolo automatizzato di un punteggio è una "decisione" se da esso dipende in modo decisivo la scelta del terzo che lo riceve; Gruppo di lavoro Articolo 29, *Linee guida sul processo decisionale automatizzato relativo alle persone fisiche e sulla profilazione* (WP251 rev.01), 2018, fatte proprie dal Comitato europeo per la protezione dei dati, edpb.europa.eu.

[^48]: Consiglio di Stato, sez. VI, sentenze 13 dicembre 2019, n. 8472, e 4 febbraio 2020, n. 881, che ne conferma i principi, giustizia-amministrativa.it. Il contenzioso riguardava la mobilità dei docenti gestita con un algoritmo.

[^49]: AgID, *Linee guida per l'adozione di IA nella pubblica amministrazione*, bozza posta in consultazione pubblica dal 18 febbraio al 20 marzo 2025 con la Determinazione n. 17/2025, 2025, agid.gov.it, principio sulla supervisione umana. Dopo la consultazione l'AgID ha predisposto una nuova versione della bozza, notificata nel 2026 alla Commissione europea nella procedura TRIS; il passo citato è quello della bozza posta in consultazione.

[^50]: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers Likely Provide Meaningful Boosts to Productivity*, Microsoft, MSR-TR-2023-43, 2023, microsoft.com. Il dato viene da uno studio sulla ricerca di informazioni con un modello linguistico, su un compito costruito perché il modello sbagliasse; quando il modello rispondeva bene, non c'erano differenze significative rispetto al gruppo di controllo. Gli studi non erano ancora sottoposti a revisione paritaria.

[^51]: F. Dell'Acqua e altri, *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*, working paper, 2023, ssrn.com: esperimento su 758 consulenti, in un compito scelto apposta fuori dalle capacità dell'IA. Sintesi in Microsoft, *New Future of Work Report 2023*, cit.

[^52]: H.-P. Lee e altri, *The Impact of Generative AI on Critical Thinking*, in Proceedings of CHI 2025, 2025, microsoft.com. Indagine su 319 lavoratori della conoscenza, con dati autodichiarati: indica un'associazione, non un rapporto di causa.

[^53]: M. Dahl e altri, *Large Legal Fictions*, cit., con valori dal 58% all'88% a seconda del modello; V. Magesh e altri, *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, in Journal of Empirical Legal Studies, vol. 22, 2025, pp. 216-242, law.stanford.edu, sugli strumenti di LexisNexis e Thomson Reuters, che conta come errore anche la risposta fondata su una fonte che non dice ciò che le si attribuisce.

[^54]: Anthropic, *Reduce hallucinations*, cit., secondo cui queste tecniche riducono le allucinazioni in modo significativo ma non le eliminano del tutto, e le informazioni critiche vanno sempre verificate; Google Cloud, *Prompt Design: Best Practices*, cit., secondo cui chiedere al modello la fonte non risolve il problema.

[^55]: Trib. Firenze, sez. spec. imprese, ordinanza 14 marzo 2025, ha escluso la responsabilità aggravata (art. 96 c.p.c.) per una memoria con riferimenti a sentenze di Cassazione inesistenti, trovati con ChatGPT: non erano provati la mala fede né il danno. Hanno invece condannato la parte per responsabilità aggravata Trib. Torino, sez. lavoro, sentenza 16 settembre 2025, e Trib. Latina, sentenza n. 1034 del settembre 2025. TAR Lombardia, Milano, sentenza 21 ottobre 2025, n. 3348, ha trasmesso la sentenza all'Ordine degli avvocati di Milano, richiamando il dovere di lealtà e probità (art. 88 c.p.c.). Trib. Siracusa, sez. II civile, sentenza 20 febbraio 2026, n. 338, ha qualificato come colpa grave la citazione di precedenti inesistenti, presumibilmente generati con l'IA e non verificati, e ha condannato la parte a 14.103 euro di spese, a una somma di pari importo ex art. 96, comma 3, c.p.c. e a 2.000 euro alla Cassa delle ammende. Fonti: Diritto.it, *Intelligenza artificiale negli atti difensivi: il Tribunale di Firenze sulle allucinazioni AI*, *Atto processuale redatto con intelligenza artificiale e responsabilità aggravata* e *Responsabilità dell'avvocato e IA: il monito del TAR*, 2025, diritto.it; StudioCataldi, *Lite temeraria per il ricorso con l'IA*, 2025, studiocataldi.it; testo della sentenza di Siracusa in ecnews.it.

[^56]: Cass. pen., sez. VII, ordinanza 27 febbraio 2026 (dep. 26 marzo 2026), n. 11431, testo in ambientediritto.it: i precedenti, pur esistenti, erano attribuiti a sezioni diverse e non affermavano i principi invocati. Cass. pen., sez. III, 11 giugno 2026 (dep. 22 giugno 2026), n. 23006, che ha fissato in 5.000 euro la somma dovuta alla Cassa delle ammende: EC News, *Citazioni generate dall'AI e non controllate: la colpa è più grave e la sanzione sale*, 2026, ecnews.it. Le fonti non chiariscono se i numeri dei precedenti citati nel secondo ricorso esistessero.

[^57]: TAR Marche, sez. I, sentenza 1° giugno 2026, n. 758, giustizia-amministrativa.it, sull'art. 30 del D.Lgs. 36/2023; l'esclusione dell'operatore per grave illecito professionale (art. 98) è stata confermata. Commenti in lavoripubblici.it e codiceappalti.it, 2026.

[^58]: Norme statali: Normattiva, con riscontro sulla Gazzetta Ufficiale in caso di dubbio. Atti dell'Unione: EUR-Lex, dove fanno fede la Gazzetta ufficiale dell'Unione e gli atti di modifica, mentre le versioni consolidate hanno valore solo documentale. Leggi regionali: Bollettino ufficiale della Regione. Statuto e regolamenti dell'ente: albo online e sezione "Amministrazione trasparente". Sentenze: giustizia-amministrativa.it per TAR e Consiglio di Stato, italgiure.giustizia.it per la Cassazione, curia.europa.eu per la Corte di giustizia. Provvedimenti del Garante: garanteprivacy.it.

[^59]: Normattiva, *Guida all'uso*, *FAQ* e *Avviso legale*, 2026, normattiva.it. Normattiva ricostruisce solo le modifiche esplicite.

[^60]: D.Lgs. 10 agosto 2018, n. 101, art. 27, che tra l'altro abroga l'art. 13 del D.Lgs. 196/2003, e art. 22, comma 6, per il quale i rinvii alle norme abrogate si intendono riferiti alle corrispondenti norme del GDPR, in quanto compatibili; in Gazzetta Ufficiale n. 205 del 4 settembre 2018, normattiva.it. Oggi l'informativa si fonda sugli artt. 13 e 14 del Regolamento.

[^61]: Esperimento preregistrato su 453 professionisti laureati: S. Noy e W. Zhang, *Experimental evidence on the productivity effects of generative artificial intelligence*, in Science, vol. 381, n. 6654, 2023, pp. 187-192, science.org. Compiti brevi e simulati; la qualità è stata valutata da valutatori esterni.

[^62]: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers*, cit.: gli utenti di Copilot hanno impiegato tra il 26% e il 73% del tempo di chi lavorava senza. Gli autori avvertono che il guadagno complessivo è verosimilmente molto inferiore. Nel Copilot Common Tasks Study i partecipanti con Copilot hanno stimato in media un risparmio di 36 minuti; quello misurato era in media di 12.

[^63]: Nella sperimentazione su circa 20.000 dipendenti di una dozzina di amministrazioni britanniche, tra settembre e dicembre 2024, il risparmio dichiarato è stato di 26 minuti al giorno, senza gruppo di confronto. Il Department for Work and Pensions ne ha stimati 19, con questionari a 1.716 utenti e a un gruppo di confronto di 2.535 non utenti. Il Department for Business and Trade non ha trovato prove solide che il tempo risparmiato diventi produttività. Fonti: Government Digital Service, *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, 2025, gov.uk; The Register, *DWP finds Copilot saves civil servants 19 minutes a day*, 2026, theregister.com; Department for Business and Trade, *Microsoft 365 Copilot evaluation*, 2025, gov.uk.

[^64]: Nella prova del Department for Business and Trade l'analisi di un foglio di calcolo con l'IA è stata più lenta, di circa 4,5 minuti, e meno accurata, come riportano TechRepublic e Civil Service World: Department for Business and Trade, *Microsoft 365 Copilot evaluation*, cit. Nelle prove di Microsoft i riassunti di riunioni fatti con l'IA erano meno completi, un indizio per le sintesi di documenti: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers*, cit.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, organizzato come una redazione: ricercatori, autore, revisori, verificatori, redattore e caporedattore, ognuno affidato a un'istanza separata del modello, per oltre cento passaggi in due giri.

- Ricerca. Sei ricerche parallele hanno raccolto 116 informazioni con la fonte: linguaggio amministrativo, tecniche di prompt, allucinazioni, dati sulla PA, GDPR e AI Act, norme del caso d'esempio.
- Esperimento. I due prompt sono stati eseguiti tre volte ciascuno; ogni testo è stato contato, e i riferimenti controllati, da un analista separato.
- Revisione. Fact-checking, revisione legale e GDPR, editing, lettore tipo e prova dei prompt hanno prodotto oltre duecento segnalazioni; quelle gravi sono state ricontrollate da verificatori indipendenti prima di correggere.

Cosa ha sbagliato l'IA, e la revisione ha intercettato:

- la prima versione dell'esperimento non valeva: il modello aveva letto i capitoli del libro prima del prompt generico. È stata rifatta da capo;
- il Comune immaginario dei primi esempi, Valverde, esiste davvero, in provincia di Catania: ora è Borgo Esempio;
- la bozza scriveva che l'IA non ricorda nulla tra una conversazione e l'altra, ma le funzioni di memoria esistono;
- attribuiva alla direttiva Frattini una soglia presa da un sito scolastico, senza riscontro sul testo;
- la checklist ammetteva i dati sanitari che il testo vietava;
- l'elenco delle norme del prompt strutturato non comprendeva l'art. 192 del TUEL: un errore del metodo, non del modello.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su più fonti secondarie concordanti.
