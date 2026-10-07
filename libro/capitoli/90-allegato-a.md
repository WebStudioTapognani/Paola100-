# Allegato A. Cento prompt pronti per l'ufficio {.unnumbered}

In questo allegato: cento prompt ordinati per attività, dall'istruttoria alla governance, ciascuno con il colore del semaforo e il capitolo che ne spiega uso, limiti e controlli.

## Come usare i prompt {.unnumbered}

I prompt seguono l'ordine del lavoro d'ufficio. Quelli che compaiono nei capitoli e negli altri allegati sono riportati con lo stesso testo; dove il capitolo dà solo le righe che cambiano, qui il prompt è completo. Gli altri applicano lo stesso metodo ai casi che i capitoli descrivono senza riportarne il prompt: lo schema in cinque parti, i vincoli su fatti e norme, il permesso di non sapere.

Ogni voce ha un numero, un titolo, il colore del semaforo e il capitolo di riferimento. Il capitolo dice quando usare il prompt, quali errori aspettarsi e che cosa controllare prima della firma: leggilo prima del primo uso. Le norme citate nei prompt sono aggiornate al 6 ottobre 2026. Prima di usarle, rifai alla data del tuo atto i tre controlli del capitolo sulla verifica delle norme: esistenza, contenuto, vigenza.

### Le convenzioni

- Le parti tra parentesi quadre le sostituisci tu: [oggetto], [importo], [elenco verificato]. Una riga che non ti serve si toglie per intero.
- [VERIFICARE: cosa] non si sostituisce. È il segnale che il modello lascia a te quando un dato manca, è incoerente o va controllato.
- I segnaposto in maiuscolo, come RICHIEDENTE_1, PROT_1, ATTO_1 o RUP_1, stanno al posto dei dati personali. Restano così nel prompt e nella bozza; i dati veri li reinserisci tu, a mano, nel sistema documentale.
- La riga Norme chiede l'elenco del servizio, con ciò che ogni norma regola nell'atto. Dove un prompt chiede il testo vigente di un articolo, copialo da Normattiva: il modello deve lavorare sulla norma che gli dai, non su quella che ricorda.
- "Testo semplice" e "circa [n] parole" evitano grassetti, titoli e lunghezze scelte dal modello. La lunghezza va comunque controllata.

### Il semaforo

Il colore dice che cosa entra nel prompt e con quale strumento, secondo la regola del capitolo sugli strumenti.

| Colore | Che cosa entra | Strumento |
|---|---|---|
| Verde | nessun dato personale né riservato | ogni strumento ammesso per iscritto |
| Giallo | dati comuni con segnaposto; informazioni riservate | solo quello dell'ente (art. 28 GDPR) |
| Rosso | testi con possibili dati rossi | solo quello scelto per il compito |

Il colore indicato è quello del caso tipico. Se nel materiale che incolli entrano persone, anche come segnaposto, o informazioni che l'ente non ha reso note, un prompt verde diventa giallo. Il colore vale per tutta la conversazione. Salute, condanne e reati, minori, documenti sottratti all'accesso e credenziali restano fuori dai tuoi prompt, con qualunque strumento: al loro posto scrivi il requisito o la norma applicata.

I due prompt rossi servono al controllo prima della pubblicazione, quando il dato rosso è l'oggetto stesso del controllo. Non li usi di tua iniziativa. Servono una decisione dell'ente, lo strumento scelto per quel compito, il parere del responsabile della protezione dei dati e la valutazione d'impatto. Senza quella decisione, provali solo su casi inventati.

Alcuni usi sono rossi con qualunque prompt. Non chiedere all'IA se una persona ha diritto a una prestazione, di assegnare punteggi o formare graduatorie di persone, di valutare l'attendibilità di qualcuno, di scegliere la decisione.

### Sei regole per tutti i prompt

1. Una conversazione nuova per ogni atto, e un'altra per ogni controllo: un modello che rilegge la propria bozza tende a confermarla.
2. Un compito per prompt. La determina e la lettera al fornitore sono due richieste.
3. Calcoli, scadenze e riparti si fanno nel foglio di calcolo. Il modello riporta i risultati, non li rifà.
4. Leggi prima i [VERIFICARE] e l'elenco delle assunzioni, poi il dispositivo, poi la motivazione.
5. Prima della firma nell'atto non restano parentesi quadre né segnaposto: cerca il carattere `[` e le parole in maiuscolo con il trattino basso.
6. L'uso dell'IA si annota nel fascicolo con strumento, data, prompt e versione (si veda il capitolo sulla tracciabilità). Finché l'ufficio non dà ai prompt un codice proprio, indica il numero di questo allegato.

### Dal libro alla libreria dell'ufficio

Un prompt stampato è un punto di partenza. Prima di usarlo negli atti, adattalo: sostituisci la riga Norme con l'elenco del servizio, collega il file di stile, provalo tre volte su un caso inventato con trappole note, come spiega il capitolo sul flusso di lavoro. Poi mettilo nella libreria dell'ufficio, con codice, versione, curatore e caso di prova. Il file di stile completo, i modelli di atto da usare nella riga Esempio e le liste di controllo sono negli allegati dedicati.

## Istruttoria {.unnumbered}

Leggere, ordinare, confrontare: i prompt di questa sezione preparano il materiale per la decisione, non la prendono. Ogni affermazione è legata a un passo del documento, che controlli sull'originale. I documenti lunghi vanno in alto e la domanda in fondo; per un documento di molte pagine, una parte alla volta.

**A.1 – Prima di un compito nuovo: che cosa manca** · semaforo: verde · capitolo sull'IA già in ufficio

```
Non svolgere ancora il compito qui sotto. Elenca soltanto:
1. le informazioni che ti servirebbero e che non hai;
2. le norme o le sentenze che dovresti citare, ciascuna seguita da
   [VERIFICARE: estremi e vigenza];
3. i calcoli, le date e gli importi da controllare.
Se non sai qualcosa, dillo: non completare con ipotesi.
Compito: [descrizione del compito, senza dati personali]
```

**A.2 – Controllare le premesse della richiesta** · semaforo: verde · capitolo su come funziona lo strumento

```
Prima di scrivere, controlla le premesse della mia richiesta.
Se una norma, un termine, un importo o un fatto che indico ti sembra
errato, abrogato o incoerente, non correggerlo da solo: segnalalo
con [VERIFICARE: motivo del dubbio] e prosegui.
Se non conosci un dato, scrivi [VERIFICARE: cosa] e non supporlo.
Richiesta: [richiesta, senza dati personali]
```

**A.3 – Atto nuovo o raro: indice e domande** · semaforo: verde · capitolo sul flusso di lavoro

```
Devo scrivere per la prima volta un [tipo di atto] per un Comune
di [numero] abitanti, sull'oggetto [descrizione senza dati personali].
Non scrivere l'atto.
1. Proponi l'indice: sezioni in ordine, una riga per sezione.
2. Elenca le domande da risolvere prima di scriverlo: competenza,
   presupposti, istruttoria, pareri, pubblicazione, ricorsi.
Per ogni norma che citi aggiungi [VERIFICARE]. Se non sai, scrivilo.
```

**A.4 – Il documento è arrivato intero?** · semaforo: verde · capitolo sull'istruttoria

```
Documento A – [titolo], [data], fonte: [sito o protocollo]
[testo integrale]
Fine del documento A.
Non riassumere e non commentare. Elenca le parti del documento A
che hai ricevuto, nell'ordine: titoli, articoli o paragrafi, allegati,
tabelle. Riporta le prime e le ultime dieci parole del testo.
Segnala parti illeggibili, interrotte, o richiamate ma assenti.
```

**A.5 – Sintesi con citazioni** · semaforo: giallo · capitolo sull'istruttoria

```
Documento A – [titolo], [data], fonte: [sito o protocollo]
[testo integrale; nomi tolti o sostituiti]
Fine del documento A.
Passo 1. Copia parola per parola, tra virgolette, i passi del documento A
su [tema], con pagina o articolo. Numerali P1, P2...
Passo 2. Sintesi in punti numerati, al massimo [n]. Ogni punto finisce
con il passo da cui viene (P1, P2...). Un punto senza passo non si scrive.
Conserva limiti, eccezioni, termini e condizioni.
Infine: "Il documento non dice", le domande su [tema] senza risposta.
Usa solo il documento A. Niente conoscenze esterne, niente valutazioni.
```

**A.6 – Risposte solo dal testo, con l'articolo** · semaforo: verde · capitolo su come funziona lo strumento

```
Testo di riferimento:
[testo del regolamento o del documento, senza dati personali]
Fine del testo.
Rispondi usando solo il testo di riferimento.
Dopo ogni frase indica tra parentesi l'articolo da cui viene.
Se una frase non viene dal testo, scrivi (conoscenza generale).
Se il testo non risponde, scrivi [VERIFICARE: non previsto dal testo].
Domanda: [domanda]
```

**A.7 – Testo a fronte tra due versioni** · semaforo: giallo · capitolo sull'istruttoria

```
Testo 1, VIGENTE – [titolo], [estremi dell'atto di approvazione]
[testo]
Testo 2, PROPOSTA – [titolo], [chi la propone e quando]
[testo]
Fine dei testi. Confronta il testo 2 con il testo 1, articolo per articolo.
Per ogni modifica: articolo; testo 1 e testo 2 tra virgolette; tipo
(sostituito, aggiunto, soppresso, spostato); effetto in una frase, senza
giudizi. Conta anche numeri, date, "può"/"deve", "e"/"o", rinvii.
Elenca a parte i soli cambi di numerazione.
In fondo: numero delle modifiche e articoli invariati.
```

**A.8 – Scheda del procedimento** · semaforo: verde · capitolo sull'istruttoria

```
Documento A – Regolamento comunale per [materia], testo vigente
[testo]
Norme da usare (verificate il [data]): [elenco, con cosa regolano]
Fine dei testi. Compila la scheda del procedimento di [nome].
Campi: oggetto; norme; avvio; unità organizzativa; responsabile del
procedimento; organo che decide; fasi in ordine; documenti da allegare;
termine; sospensioni; controlli; pubblicazioni; tutela; potere sostitutivo.
Per ogni campo indica la fonte: articolo del documento A o norma
dell'elenco. Senza fonte: [VERIFICARE: cosa]. Ruoli, non nomi.
Non calcolare date.
```

**A.9 – Scheda di un bando o di un avviso** · semaforo: verde · capitolo sull'istruttoria

```
Documento A – [titolo dell'avviso], [ente], [data], fonte: [sito]
[testo integrale]
Documento B – [FAQ, rettifiche, allegati, con data]: [testo o "nessuno"]
Fine dei documenti. Compila una scheda con: beneficiari e requisiti;
interventi e spese ammissibili; contributo e cofinanziamento; scadenza,
con ora e modalità di invio; documenti, con firma e formato; criteri di
valutazione; cause di esclusione; obblighi dopo la concessione.
Ogni voce: passo tra virgolette e articolo. Se B modifica o chiarisce A,
riporta entrambi i passi. Senza fonte: [VERIFICARE: cosa].
In testa indica parti e articoli letti. Non dire se il Comune è ammesso
e non calcolare date.
```

**A.10 – Completezza formale di una domanda** · semaforo: giallo · capitolo sul GDPR e i dati nel prompt

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Documento 1: elenco dei documenti richiesti dall'art. [n] del bando.
Documento 2: elenco dei file allegati alla domanda DOMANDA_1.
Compito: per ogni documento dell'elenco indica "presente", "assente"
o "da controllare", con il nome del file corrispondente.
Non valutare il contenuto dei documenti, i requisiti, il punteggio
o l'ammissibilità della domanda. Non proporre esiti.
Se un file non è riconoscibile dal nome, scrivi
[VERIFICARE: contenuto del file].
```

**A.11 – Criteri del regolamento e relazione** · semaforo: giallo · capitolo su come funziona lo strumento

```
Criteri del regolamento:
[articoli con i criteri, senza dati personali]
Relazione dell'associazione:
[relazione, tolti nomi e dettagli che riconducono a persone]
Fine dei testi. Non assegnare punteggi e non proporre decisioni.
Per ogni criterio, in tabella: criterio, passo della relazione
tra virgolette che lo riguarda, oppure [VERIFICARE: dato mancante].
Non usare informazioni che non sono nei due testi.
```

**A.12 – Scheda istruttoria in formato fisso** · semaforo: giallo · capitolo sul flusso di lavoro

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

**A.13 – Cronologia dei fatti del fascicolo** · semaforo: giallo · capitolo sull'istruttoria

```
Documenti del fascicolo, ciascuno preceduto da numero, titolo e data:
[documenti, con i segnaposto al posto dei dati personali]
Fine dei documenti. Non valutare i fatti e non trarre conclusioni.
Elenca in ordine di data gli eventi che i documenti riportano.
Per ogni evento: data; che cosa è accaduto, in una riga; numero del
documento; passo tra virgolette.
Se la stessa data è diversa in due documenti, riportale entrambe
e scrivi [VERIFICARE: data]. Date incerte: [VERIFICARE: data].
Non calcolare termini e non dedurre date che i documenti non riportano.
In fondo elenca i fatti citati senza un documento che li riporti.
```

**A.14 – Ogni fatto con la sua prova** · semaforo: giallo · capitolo sulla legge italiana sull'IA

```
Bozza di [tipo di atto]:
[testo]
Documenti del fascicolo: [elenco con estremi, per esempio ATTO_1].
Fine dei dati. Non riscrivere la bozza.
Elenca in una tabella ogni fatto affermato in premesse e motivazione,
con il documento dell'elenco che lo prova.
Se nessun documento lo prova, scrivi [VERIFICARE: documento mancante].
Segnala a parte le frasi che danno per avvenuti controlli, pareri
o verifiche. Non dedurre fatti che i documenti non contengono.
```

**A.15 – Che cosa indebolisce la proposta** · semaforo: giallo · capitolo sull'istruttoria

```
Testo 1, SCHEDA ISTRUTTORIA chiusa il [data]: [scheda]
Testo 2, DOCUMENTI citati nella scheda: [testi]
Proposta dell'ufficio: [esito proposto, in una frase]
Fine dei testi. Non dire se la proposta è giusta.
Elenca i passi dei documenti che la indeboliscono o la contraddicono,
tra virgolette, con la fonte. Poi i fatti che la proposta presuppone
e che i documenti non provano. Se non ne trovi, scrivi "nessuno".
```

**A.16 – Relazione istruttoria per chi decide** · semaforo: giallo · capitolo sull'istruttoria

```
Sei il responsabile del procedimento in un Comune di [numero] abitanti.
SCHEDA ISTRUTTORIA chiusa il [data]: [scheda]
Proposta di esito, decisa dall'ufficio: [esito e motivi, in breve].
Chi decide: [organo o responsabile, con la norma che lo indica].
Compito: relazione istruttoria per chi decide: oggetto; fasi svolte;
fatti accertati, ciascuno con il documento; esito proposto e motivi.
Circa [n] parole, testo semplice.
Fatti: solo quelli della scheda. Motivi: solo quelli indicati sopra.
Non dare per resi pareri, controlli o verifiche che la scheda non
riporta. Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa].
Dopo la relazione, separati, elenca i [VERIFICARE].
```

## Determine {.unnumbered}

Il prompt modello in cinque parti apre la sezione: gli altri ne sono varianti, con le righe Dati, Fatti e Compito adattate all'atto. I controlli vengono dopo la bozza, ciascuno in una conversazione nuova, con la bozza come unico testo.

**A.17 – Prompt modello in cinque parti** · semaforo: giallo · capitolo sul metodo del prompt

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

**A.18 – Un atto modello come esempio, senza copiarlo** · semaforo: verde · capitolo sul metodo del prompt

```
Esempio (solo struttura e tono, nessun dato): [atto modello]
Fine dell'esempio. Non copiare dall'esempio fatti, numeri, date,
importi, nomi o norme: usa solo i dati e l'elenco delle norme di questo
prompt. Se l'esempio ha una parte per cui qui mancano i dati,
scrivi [VERIFICARE: dato mancante] e prosegui.
```

**A.19 – Niente calcoli: righe da aggiungere** · semaforo: verde · capitolo su come funziona lo strumento

```
Non fare calcoli e non calcolare scadenze.
Dove l'atto richiede un importo o un termine, scrivi
[VERIFICARE: calcolo da fare].
Dopo l'atto, per ciascuno elenca i dati di partenza e l'operazione.
Se indichi la norma che fissa un termine, aggiungi [VERIFICARE: norma].
```

**A.20 – Determina a contrarre e di affidamento diretto** · semaforo: verde · capitolo sulle determine

```
Sei un istruttore amministrativo del Servizio [servizio] del Comune di [nome].
Contesto: [fatti dell'istruttoria; contratto in corso ATTO_1; offerta].
Dati: [importo e IVA, operatore, piattaforma, capitolo, atti con n. e data].
Norme (solo queste) e cosa regolano: [elenco delle norme della determina].
Esempio (solo struttura e tono, nessun dato): [determina firmata, senza dati].
Formato: oggetto, Visto, Considerato, DETERMINA; 500 parole; file di stile.
Compito: bozza della determina a contrarre e di affidamento diretto. In
motivazione: fine, oggetto, forma, clausole essenziali, ragioni della scelta.
Fatti: solo i dati sopra. Verifiche, visti e regolarità tecnica: da fare.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Norme fuori elenco: non citarle, scrivi [VERIFICARE: norma da cercare].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.21 – Determina di liquidazione** · semaforo: verde · capitolo sulle determine

```
Sei un istruttore amministrativo del Servizio [nome] del Comune di [nome].
Compito: bozza della determina di liquidazione della fattura [n. e data].
Dati: determina e impegno [n.], capitolo, CIG, imponibile, IVA, scadenza.
Regolare esecuzione: [chi l'ha attestata e quando, oppure "da attestare"].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DETERMINA; circa 350 parole.
Fatti: DURC, conto dedicato e CIG in fattura solo se indicati qui sopra,
con data o protocollo del documento; altrimenti [VERIFICARE: controllo].
Non scrivere IBAN né codici fiscali. Importi: riportali, non ricalcolarli.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.22 – Determina di accertamento di entrata** · semaforo: verde · capitolo sulle determine

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Dati: atto di concessione [ente, numero, data]; debitore [ente];
importo [euro]; capitolo di entrata [n]; tempi di erogazione [come
li indica l'atto di concessione].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, DETERMINA; circa 250 parole; file di stile.
Compito: bozza della determina di accertamento dell'entrata.
Fatti: senza atto di concessione non si accerta: se l'atto manca,
non scrivere la bozza e scrivi [VERIFICARE: titolo del credito].
Esercizio: non sceglierlo; scrivi [VERIFICARE: esercizio di
esigibilità secondo i tempi di erogazione].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.23 – Determina di nomina del RUP** · semaforo: giallo · capitolo sulle determine

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Intervento: [oggetto, importo stimato, finanziamento].
Dati: RUP_1, dipendente del Servizio [nome]; dichiarazione sui
conflitti di interessi [resa il (data), oppure "da acquisire"].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DETERMINA; circa 250 parole.
Compito: bozza della determina di nomina del responsabile unico del
progetto per le fasi di [fasi].
Requisiti di RUP_1: non attestarli; scrivi [VERIFICARE: requisiti
dell'allegato I.2 per tipo e importo].
Niente titoli di studio, esperienze o altri dati di RUP_1.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.24 – Determina di concessione di un contributo** · semaforo: giallo · capitolo sul flusso di lavoro

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Contesto: SCHEDA ISTRUTTORIA chiusa il [data], per intero: [scheda]
Dati: importo deciso [euro], dal foglio di calcolo; capitolo [n];
regolamento, indirizzi e bilancio, con numero e data.
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DETERMINA; circa 450 parole.
Compito: bozza della determina di concessione. Per ogni criterio del
regolamento, il fatto della scheda o [VERIFICARE: dato mancante].
Fatti: solo quelli della scheda; nessun nome di persona.
Importi: riportali, non ricalcolarli.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.25 – Che cosa manca alla bozza** · semaforo: verde · capitolo sul metodo del prompt

```
Bozza di [tipo di atto]:
[testo]
Fine della bozza. Non riscriverla. Elenca ciò che un atto di questo tipo
dovrebbe contenere e qui manca: istruttoria, pareri, clausole, ricorsi.
Ignora i campi tra parentesi quadre. Dividi in "richiesto da una norma"
e "di prassi". Se citi una norma, aggiungi [VERIFICARE].
```

**A.26 – Le scelte contenute nella bozza** · semaforo: giallo · capitolo sulla legge italiana sull'IA

```
Bozza di [tipo di atto]:
[testo]
Fine della bozza. Non riscriverla e non dare giudizi di merito.
Elenca le scelte che contiene: valutazioni, alternative scartate,
importi o punteggi stabiliti, interpretazioni di una norma.
Per ogni scelta riporta la frase della bozza e indica se il testo
ne dà una ragione. Se la ragione manca, scrivi [VERIFICARE: motivazione].
Non dire quale scelta è giusta: decide l'ufficio.
```

**A.27 – Bozza e scheda istruttoria a confronto** · semaforo: giallo · capitolo sul flusso di lavoro

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

**A.28 – Rilettura da controllo successivo** · semaforo: verde · capitolo su come funziona lo strumento

```
Sei il segretario comunale e svolgi il controllo successivo di regolarità
amministrativa sulla bozza qui sotto. Non riscriverla.
Bozza: [testo, senza dati personali]
Fine della bozza.
Elenca in una tabella (passaggio, problema, cosa controllare):
- fatti dati per accertati senza un atto o un documento che li provi;
- norme citate, ciascuna con [VERIFICARE: esistenza, contenuto, vigenza];
- passaggi della motivazione che non sostengono il dispositivo.
Se in una categoria non trovi problemi, scrivilo.
```

**A.29 – Controllo della determina** · semaforo: verde · capitolo sulle determine

```
Bozza di determina:
[testo]
Fine della bozza. Non riscriverla. Rispondi con una tabella:
punto, problema, frase della bozza.
1. Mancano fine, oggetto, forma, clausole, scelta del contraente?
2. Elenca ogni importo e dove compare. Non ricalcolare.
3. Fatti, controlli, pareri o visti presentati come già avvenuti.
4. Formule superate: posizione organizzativa, SmartCIG, responsabile
unico del procedimento, immediata eseguibilità.
5. Riferimenti al D.Lgs. 50/2016, al D.L. 76/2020, alle Linee guida ANAC.
Non dire se le norme sono vigenti: lo verifico io.
```

## Delibere {.unnumbered}

La proposta la scrive l'ufficio, la adotta un organo collegiale. Per questo i prompt chiedono la norma che fonda la competenza e vietano di scrivere pareri, presenze e voti: li aggiunge chi li ha visti.

**A.30 – Proposta di deliberazione** · semaforo: verde · capitolo sulle delibere

```
Sei un istruttore amministrativo del Servizio [servizio] del Comune di [nome].
Contesto: proposta di deliberazione della [organo]; [istanza e fatti].
Dati: [importi già calcolati; capitolo; atti dell'ente con numero e data].
Competenza: [organo, articolo del TUEL e del regolamento che la fondano].
Norme (solo queste) e cosa regolano: [elenco delle norme della delibera].
Formato: oggetto, Visto, Considerato, DELIBERA; 600 parole; file di stile.
Compito: bozza della proposta. Per ogni criterio del regolamento scrivi il
fatto che lo soddisfa, con il documento, o [VERIFICARE: dato mancante].
Fatti: solo i dati sopra. Pareri, presenze e voti: non scriverli.
Urgenza: [motivo concreto e data, oppure "nessuna"].
Dato mancante o incoerente, norma fuori elenco: [VERIFICARE: cosa].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.31 – Chi è competente: Consiglio, Giunta o responsabile** · semaforo: verde · capitolo sulle delibere

```
Decisione da prendere: [che cosa si decide, con importi e durata].
Testi vigenti, copiati il [data]: artt. 42, 48, 107 e 109 del TUEL;
statuto e regolamenti dell'ente su [materia]; [altri articoli]: [testi]
Fine dei testi. Usa solo questi testi, non ciò che ricordi.
Indica chi adotta l'atto: Consiglio, Giunta, sindaco o responsabile
del servizio. Riporta tra virgolette il passo che lo dice, con
articolo e comma.
Se la decisione ha parti di competenza diversa, separale.
Se i testi non bastano, scrivi [VERIFICARE: competenza da accertare].
Non indicare pareri, votazioni o urgenza.
```

**A.32 – Atto di indirizzo della Giunta** · semaforo: verde · capitolo sulle delibere

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Contesto: [fatti; documenti con titolo e data, per esempio un avviso].
Dati: [limiti di spesa, tempi, risorse; atti dell'ente con n. e data].
Competenza: [organo e norma; di regola Giunta, art. 48, c. 2, TUEL].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DELIBERA; circa 400 parole.
Compito: bozza della proposta di atto di indirizzo: obiettivo, limiti,
destinatario (il responsabile del Servizio [nome]), termine.
Niente atti di gestione: impegni, affidamenti, incarichi, progetti.
Fatti: solo i dati sopra. Pareri, presenze e voti: non scriverli.
Se l'atto fissa una spesa: [VERIFICARE: pareri dell'art. 49 TUEL].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.33 – Convenzione tra Comuni** · semaforo: giallo · capitolo sulle delibere

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Schema di convenzione con il Comune di [nome], in [n] articoli:
[testo dello schema]
Fine dello schema. Dati: [quote, costi stimati, chi firma, atti].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DELIBERA; circa 450 parole.
Compito: bozza della proposta di deliberazione del Consiglio che
approva lo schema. Per ogni elemento dell'art. 30, comma 2, del TUEL:
articolo dello schema che lo contiene, o [VERIFICARE: elemento mancante].
Fatti: solo schema e dati. Pareri e voti: non scriverli.
Dato mancante o norma fuori elenco: [VERIFICARE: cosa]. Poi elencali.
```

**A.34 – Coerenza interna di un regolamento** · semaforo: giallo · capitolo sulle delibere

```
Testo: [schema di regolamento, articoli numerati]
Fine del testo. Non riscriverlo. Rispondi con una tabella: articolo,
problema, frase. Cerca: rinvii ad articoli o commi che non esistono o
non c'entrano; termini diversi per la stessa cosa; scadenze incoerenti
tra articoli; norme statali citate, con [VERIFICARE].
Non dare giudizi sulle scelte di contenuto.
```

**A.35 – Controllo prima dell'ordine del giorno** · semaforo: verde · capitolo sulle delibere

```
Proposta di deliberazione:
[testo]
Fine della proposta. Non riscriverla. Rispondi con una tabella:
punto, problema, frase della proposta.
1. Quale organo adotta l'atto, e quale norma o articolo lo dice?
2. Pareri, presenze, voti o controlli presentati come già avvenuti.
3. Atti di gestione nel dispositivo: impegni, affidamenti, liquidazioni.
4. Immediata eseguibilità: c'è un motivo concreto, con una data?
5. Riferimenti a comitati di controllo o all'art. 151, c. 4, TUEL.
6. Elenca ogni importo e dove compare. Non ricalcolare.
Non dire se le norme sono vigenti: lo verifico io.
```

## Verbali e decreti {.unnumbered}

Il verbale attesta ciò che è avvenuto: presenze e voti vengono dalla scheda del segretario, mai dalla trascrizione. Nei decreti di nomina la scelta è del sindaco: il modello la scrive con le ragioni che gli dai, senza giudizi sulla persona. Le parti in seduta segreta restano fuori dal prompt.

**A.36 – Resoconto di un punto dalla trascrizione** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Sei l'assistente del segretario comunale di un Comune di 6.500 abitanti.
Trascrizione automatica del punto [n] del Consiglio del [data]: [testo].
Dati certi, dalla scheda del segretario: [presenze, votazioni, orari].
Compito: resoconto sommario del punto, in forma indiretta, al presente,
nell'ordine degli interventi; 40-100 parole ciascuno; niente giudizi.
Fatti: presenze e voti solo dai Dati certi; mai dedurli dal testo.
Norme citate da chi parla: riportale come dette; [VERIFICARE: minuto].
Passaggi incomprensibili, nomi e numeri dubbi: [VERIFICARE: minuto].
Dichiarazioni "a verbale": non riassumerle; [VERIFICARE: testo].
Passaggi omessi: non ricostruirli; segnalali con il minuto.
Dopo il resoconto, elenca i [VERIFICARE] e le parti omesse, con il minuto.
```

**A.37 – Verbale e scheda del segretario a confronto** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Testo 1, SCHEDA DEL SEGRETARIO, punto [n] della seduta del [data]:
[scheda]
Testo 2, BOZZA DEL VERBALE dello stesso punto: [bozza]
Fine dei testi. Non riscrivere la bozza.
Rispondi con una tabella: elemento, scheda, bozza, coincide sì o no.
Elementi: presenti e assenti, entrate e uscite, emendamenti, ogni
votazione con favorevoli, contrari e astenuti, esiti, orari.
Segnala a parte: esiti o voti nella bozza che la scheda non contiene;
dichiarazioni "a verbale" riassunte invece che riportate.
Non ricalcolare maggioranze e non dire se le votazioni sono valide.
```

**A.38 – Decreto di incarico di elevata qualificazione** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore del Servizio Affari generali di un Comune di 6.500
abitanti senza dirigenti.
Contesto: il Sindaco conferisce a DIPENDENTE_1 l'incarico di elevata
qualificazione del Servizio [servizio] dal [data] al [data].
Dati: atti dell'ente con n. e data [regolamento, graduazione, avviso];
retribuzione di posizione [importo]; ragioni della scelta: [testo].
Norme (solo queste) e cosa regolano: [elenco]. Fuori elenco: non citarle.
Compito: bozza del decreto; Visti, Considerato, DECRETA; 450 parole.
Fatti: non valutare la persona; usa le ragioni date, senza aggettivi.
Dichiarazioni e comunicazioni: da acquisire, non già avvenute.
Niente pareri dell'art. 49 TUEL né indicazione del ricorso al TAR.
Se un dato manca: [VERIFICARE: cosa]. Poi elenca i [VERIFICARE].
```

**A.39 – Decreto di nomina di un rappresentante** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore degli Affari generali di un Comune di [numero] abitanti.
Contesto: il Sindaco nomina NOMINATO_1 rappresentante del Comune
presso [ente], per [durata].
Dati: indirizzi del Consiglio [deliberazione, n. e data; criteri];
ragioni della scelta indicate dal Sindaco: [testo].
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visti, Considerato, DECRETA; circa 350 parole.
Fatti: per ogni criterio degli indirizzi, la ragione data dal Sindaco
che lo riguarda, o [VERIFICARE: criterio senza riscontro].
Nessun giudizio sulla persona. Dichiarazioni: da acquisire.
Termine e autorità del ricorso: [dati verificati]; non sceglierli tu.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

## Ordinanze {.unnumbered}

"Ordinanza" indica atti diversi, con poteri e firme diversi. Ogni prompt fissa il potere e chi firma. Sanzioni, termine e autorità del ricorso li scrivi tu, dall'elenco verificato: il modello li confonde spesso.

**A.40 – Ordinanza contingibile e urgente** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore del Servizio Tecnico di un Comune di 6.500 abitanti.
Contesto: [fatti del verbale di sopralluogo ATTO_1, citati come tali].
Dati: bene IMMOBILE_1 su STRADA_1; destinatario PROPRIETARIO_1; misure
già adottate [quali]; ricorso: TAR [regione], 60 giorni; straordinario 120.
Norme (solo queste) e cosa regolano: [elenco]. Fuori elenco: non citarle.
Compito: bozza di ordinanza contingibile e urgente del Sindaco (art. 54,
comma 4, TUEL). Motivazione: pericolo, prova, perché non bastano gli
strumenti ordinari, perché manca l'avviso di avvio. Circa 450 parole.
Fatti: solo quelli del verbale; non aggravarli né attenuarli.
Sanzioni: non sceglierle; scrivi [VERIFICARE: norma applicabile].
Se un dato manca o è incoerente: [VERIFICARE: cosa].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.41 – Ordinanza sugli orari** · semaforo: verde · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Contesto: [evento o area; esigenze di tranquillità e riposo dei
residenti, dai documenti: relazione della polizia locale, esposti].
Dati: area [descrizione o planimetria]; giorni e fasce orarie [quali],
entro la durata massima prevista dalla norma; sanzione e pagamento
in misura ridotta [dall'elenco verificato]; ricorso [autorità e termine].
Norme (solo queste) e cosa regolano: [elenco verificato].
Compito: bozza di ordinanza del Sindaco che limita gli orari di [vendita
per asporto, somministrazione] (art. 50, comma 7-bis, TUEL); 350 parole.
Motivazione: ragioni legate all'area e all'evento, con il documento.
Non chiamarla contingibile e urgente. Sanzioni: richiamale, non ordinarle.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.42 – Ordinanza sulla circolazione** · semaforo: verde · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore del Servizio [nome] del Comune di [nome].
Contesto: [lavori o evento; strada o area; date e orari; relazione
o richiesta all'origine, con data].
Dati: misure [divieti, sensi unici, percorsi alternativi]; segnaletica
a cura di [chi]; ricorso [autorità e termine, dall'elenco verificato].
Norme (solo queste) e cosa regolano: [elenco verificato].
Compito: bozza dell'ordinanza di disciplina temporanea della
circolazione. Firma il responsabile del Servizio [nome], non il Sindaco.
Formato: oggetto, Visto, Considerato, ORDINA; circa 300 parole.
Fatti: solo i dati sopra. Sanzioni: richiamale, non ordinarle.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.43 – Ordinanza di rimozione di rifiuti abbandonati** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Sei un istruttore del Servizio Tecnico di un Comune di [numero] abitanti.
Contesto: [fatti del verbale di accertamento ATTO_1, citati come tali].
Dati: area IMMOBILE_1; destinatario PROPRIETARIO_1; termine per
provvedere [indicato dall'ufficio]; ricorso [autorità e termine].
Chi firma: [Sindaco o responsabile, secondo la norma verificata].
Norme (solo queste) e cosa regolano: [elenco verificato].
Compito: bozza dell'ordinanza di rimozione dei rifiuti e di ripristino
dei luoghi; circa 400 parole; file di stile.
Responsabilità del destinatario: solo come risulta da ATTO_1;
altrimenti scrivi [VERIFICARE: accertamento della responsabilità].
Fatti: non aggravarli né attenuarli. Sanzioni: [VERIFICARE: norma].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.44 – Controllo dell'ordinanza** · semaforo: giallo · capitolo su verbali, decreti e ordinanze

```
Bozza di ordinanza:
[testo]
Fine della bozza. Non riscriverla. Rispondi con una tabella:
punto, problema, frase della bozza.
1. Quale potere esercita, e chi firma? Artt. 50 e 54 citati insieme?
2. Pericolo o ragioni: c'è un fatto, con il documento che lo prova?
3. Se è contingibile: perché non bastano gli strumenti ordinari,
perché manca l'avviso di avvio, se il prefetto è informato prima.
4. Sanzioni tra gli ordini, o senza una norma che le preveda.
5. Termine per adempiere; autorità e termine del ricorso.
Non dire se le norme sono vigenti: lo verifico io.
```

## Privacy e pubblicazione {.unnumbered}

La strada principale è scrivere l'atto già pubblicabile. Il controllo viene dopo, nell'ordine del capitolo sulla privacy prima della pubblicazione: lista di parole, bozza con i segnaposto e, solo se l'ente lo ha deciso, l'atto con i dati. Qui ci sono i due prompt rossi.

**A.45 – Dettagli che rendono riconoscibili** · semaforo: giallo · capitolo sul metodo del prompt

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

**A.46 – Determina pubblicabile con allegato riservato** · semaforo: giallo · capitolo sulla privacy prima della pubblicazione

```
Sei un istruttore dei Servizi sociali di un Comune di [numero] abitanti.
Contesto: contributo straordinario a un nucleo familiare; istruttoria
conclusa; requisiti dell'art. [n] del regolamento posseduti.
Dati: importo [euro]; capitolo [n]; atti generali con numero e data.
Norme (solo queste) e cosa regolano: [elenco verificato].
Formato: oggetto, Visto, Considerato, DETERMINA; circa 400 parole.
Compito: bozza della determina, nella versione da pubblicare all'albo.
Pubblicazione: nessun dato che identifichi o descriva il beneficiario;
chi è e i suoi fatti personali stanno nell'allegato A, non pubblicato.
Fatti: solo i dati sopra. Se un dato manca, scrivi [VERIFICARE: cosa].
Norme fuori elenco: non citarle, scrivi [VERIFICARE: norma da cercare].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.47 – Formule neutre per le frasi a rischio** · semaforo: giallo · capitolo sulla privacy prima della pubblicazione

```
Frasi di un atto destinato all'albo online, segnalate come a rischio:
[frasi, con i segnaposto]
Fine delle frasi. Per ognuna proponi una formula neutra che non
identifica né descrive la persona e non rivela salute, disagio
economico o sociale, minori, reati. Se un fatto serve alla
motivazione, rinvia all'allegato riservato o alla relazione agli atti.
Non togliere obblighi, importi, termini, condizioni, norme.
Tabella: frase originale, formula neutra, che cosa è stato tolto.
Se una frase non si può rendere neutra senza perdere contenuto
giuridico, scrivi [VERIFICARE: da decidere con il responsabile].
```

**A.48 – Lista di parole da cercare** · semaforo: verde · capitolo sulla privacy prima della pubblicazione

```
Prepara una lista di parole da cercare con la funzione Trova in un
[tipo di atto] di un Comune, prima della pubblicazione all'albo online.
Categorie: salute e disabilità; disagio economico o sociale; minori;
reati e procedimenti; identificativi (codice fiscale, IBAN, targhe,
indirizzi, date di nascita). Per ogni categoria 10-20 voci, anche radici
brevi che trovano più parole (per esempio "invalid"). Includi sigle e
termini burocratici. Niente spiegazioni. Una colonna per categoria.
```

**A.49 – Controllo prima della pubblicazione** · semaforo: rosso · capitolo sulla privacy prima della pubblicazione

```
Sei l'addetto al controllo degli atti prima della pubblicazione online.
Testo da pubblicare, con oggetto e allegati destinati all'albo:
[testo]
Fine del testo. Il Comune ha circa [numero] abitanti.
Cerca: identificativi (nomi, codice fiscale, IBAN, indirizzi, targhe,
date di nascita); salute e disabilità, anche dedotte dalla prestazione;
disagio economico o sociale; minori; reati; altre categorie dell'art. 9
GDPR; dettagli che insieme rendono riconoscibile qualcuno.
Tabella: frase esatta, categoria, perché è un rischio. Una riga per
occorrenza; se una categoria non ha occorrenze, scrivi "nessuna".
Non riscrivere il testo. Non dichiararlo pubblicabile: decide l'ufficio.
```

**A.50 – Dati personali con un modello in locale** · semaforo: rosso · capitolo sugli strumenti

```
Testo:
[testo dell'atto]
Fine del testo.
Compito: trova i dati che riguardano persone fisiche.
Cerca nomi, codici fiscali, indirizzi, date di nascita, targhe,
telefoni, IBAN, dati di salute, minori, condanne.
Rispondi solo con una tabella: dato, frase in cui compare, tipo.
Se non sei sicuro, inserisci il dato e scrivi "dubbio".
Non riscrivere il testo. Non dire se il testo è pubblicabile.
```

**A.51 – Lettera e dati da pubblicare dall'atto firmato** · semaforo: giallo · capitolo sul flusso di lavoro

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

**A.52 – Documento da rilasciare con accesso generalizzato** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Documento da rilasciare con accesso civico generalizzato, con i
segnaposto al posto dei dati personali: [testo]
Limiti dell'art. 5-bis del D.Lgs. 33/2013 indicati dall'ufficio:
[elenco]
Fine dei testi. Non decidere che cosa rilasciare od oscurare.
Tabella: passo tra virgolette; tipo di informazione (dato personale,
interesse economico o commerciale, altro); limite dell'elenco che può
riguardarlo, oppure "nessuno".
Segnala anche i dettagli che rendono riconoscibile una persona senza
nome. Se vedi dati su salute, minori o reati, segnalalo senza
riportarli.
```

## Verifica delle norme {.unnumbered}

Ogni riferimento resta da verificare finché non supera tre controlli: esistenza, contenuto, vigenza alla data dell'atto. Questi prompt preparano la lista di lavoro e confrontano la bozza con il testo che incolli. Il giudizio sulla vigenza non si chiede al modello.

**A.53 – Origine dei riferimenti della bozza** · semaforo: verde · capitolo sul metodo del prompt

```
Rileggi la bozza che hai scritto. Non correggerla. Elenca in una tabella
i riferimenti a norme, regolamenti, sentenze e linee guida, con articolo
e comma, cosa regolano nell'atto e origine.
Origine: "fornito" se atto, articolo e comma sono nell'elenco qui sotto;
"articolo diverso" se c'è solo l'atto; "aggiunto" negli altri casi.
In fondo scrivi il totale. Non dire se le norme sono vigenti.
Elenco fornito: [incolla di nuovo l'elenco delle norme]
```

**A.54 – Elenco di tutti i riferimenti** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo:
[atto o bozza, senza dati personali]
Fine del testo.
Elenca in una tabella tutti i riferimenti a norme, regolamenti, sentenze,
linee guida, contratti collettivi e importi fissati da una norma.
Colonne: n.; riferimento come scritto; atto (tipo, data, numero);
articolo, comma e lettera; cosa il testo gli attribuisce, in una riga.
Riportali tutti, anche se ripetuti, nell'ordine in cui compaiono.
Se gli estremi sono incompleti, scrivi [VERIFICARE: estremi mancanti].
Non correggere, non completare, non dire se sono vigenti.
In fondo scrivi il totale.
```

**A.55 – Scheda di una norma dal testo vigente** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo vigente di [norma e articolo], copiato da [fonte] il [data]:
[testo]
Fine del testo. Usa solo questo testo, non ciò che ricordi della norma.
Per ogni comma o paragrafo scrivi una riga: che cosa dispone, chi
obbliga, da quando, se il testo lo dice.
Non aggiungere interpretazioni, prassi o giurisprudenza.
Se per capire un comma serve una norma richiamata, scrivi
[VERIFICARE: norma richiamata].
Metti tra virgolette solo parole presenti nel testo.
```

**A.56 – La frase della bozza e il testo vigente** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo vigente al [data], copiato da Normattiva:
[testo dell'articolo, senza le doppie parentesi]
Fine del testo.
Frase della bozza: [frase che cita l'articolo]
Usa solo il testo sopra. La frase è sostenuta, sostenuta in parte
o non sostenuta? Riporta tra virgolette, parola per parola, i passi
decisivi. Segnala eccezioni, deroghe e rinvii ad altri articoli.
Non dire nulla sulla vigenza: è già stata verificata.
```

**A.57 – Una sentenza dice davvero questo?** · semaforo: giallo · capitolo sulla verifica delle norme

```
Testo della sentenza, scaricato dal sito ufficiale:
[testo integrale]
Fine del testo.
Affermazione della bozza: [frase che cita la sentenza]
Usa solo il testo sopra. Riporta tra virgolette, parola per parola,
i passi della motivazione che sostengono o smentiscono l'affermazione.
Per ogni passo indica se riguarda la decisione del caso o è
un'osservazione di contorno. Se nessun passo la sostiene, scrivi
NON TROVATO. Non usare altre sentenze né conoscenze esterne.
```

**A.58 – Proposta, bozza o norma in vigore?** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo: [notizia, comunicato o documento, con fonte e data]
Fine del testo. Usa solo questo testo.
Indica che cosa è l'atto di cui parla: proposta, schema o disegno
di legge, bozza di linee guida, atto approvato ma non pubblicato,
atto pubblicato. Riporta tra virgolette le frasi che lo indicano.
Se il testo indica estremi di pubblicazione e date di entrata in vigore
o di applicazione, riportali; altrimenti scrivi [VERIFICARE: vigenza].
Non dire se l'atto si applica agli atti del Comune.
```

**A.59 – Regime transitorio** · semaforo: verde · capitolo sulla verifica delle norme

```
Atto da adottare il [data]. Procedimento avviato il [data] con [atto
o fatto di avvio].
Norma transitoria, testo vigente al [data] copiato da Normattiva:
[testo]
Testo della norma nuova e di quella precedente: [testi, se servono]
Fine dei testi. Usa solo questi testi.
Quale disciplina si applica al procedimento? Riporta tra virgolette
i passi decisivi e il fatto da cui dipende la risposta (avvio,
pubblicazione del bando, stipula, altro).
Se i testi non bastano, scrivi [VERIFICARE: cosa manca].
Non citare giurisprudenza né prassi.
```

**A.60 – Novità di una norma per il servizio** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo della nuova norma, pubblicata in [Gazzetta e data]: [testo]
Testo previgente degli articoli modificati, se c'è: [testo]
Fine dei testi. Il Servizio [nome] adotta di solito: [tipi di atto].
Elenca le novità che riguardano quegli atti: articolo; che cosa
cambia, in una riga; da quando si applica e regime transitorio,
solo se il testo lo dice.
Altrimenti scrivi [VERIFICARE: decorrenza] o [VERIFICARE: transitorio].
Per ogni novità indica i modelli o i prompt dell'ufficio da rivedere
tra questi: [elenco dei titoli].
Non dire come applicarla ai procedimenti in corso.
```

**A.61 – Modelli da aggiornare dopo una modifica** · semaforo: verde · capitolo sulla verifica delle norme

```
Testo dell'articolo prima della modifica: [testo]
Testo dopo la modifica, vigente dal [data]: [testo]
Fine dei testi.
Modelli dell'ufficio, ciascuno preceduto dal suo titolo:
[modelli, senza dati personali]
Fine dei modelli.
Elenca i passi dei modelli che citano l'articolo o ne applicano
il contenuto cambiato: titolo del modello, passo tra virgolette,
cosa cambia. Non riscrivere i modelli.
Se un passo è dubbio, scrivi [VERIFICARE: motivo].
```

**A.62 – Riferimenti superati nel file di stile** · semaforo: verde · capitolo sulla verifica delle norme

```
RIFERIMENTI SUPERATI – aggiornati al [data]
Non riprenderli dai testi forniti. Scrivi invece:
- affidamento diretto: art. 50, comma 1, D.Lgs. 36/2023, non
  art. 36 D.Lgs. 50/2016 né art. 1 D.L. 76/2020;
- appalti: "responsabile unico del progetto", non "del procedimento";
- "incarico di elevata qualificazione", non "posizione organizzativa";
- informativa: artt. 13 e 14 GDPR, non art. 13 D.Lgs. 196/2003;
- "categorie particolari di dati", non "dati sensibili".
Se un riferimento superato serve per un procedimento avviato prima
della modifica, scrivi [VERIFICARE: regime transitorio].
```

## Lingua e stile {.unnumbered}

La revisione della lingua non deve cambiare il contenuto. Per questo ogni riscrittura è seguita da un confronto di contenuto, in una conversazione nuova, e i termini giuridici dell'atto sono indicati come intoccabili.

**A.63 – Visto o Considerato: classificare le frasi** · semaforo: verde · capitolo sulla lingua degli atti

```
Testo del preambolo e della motivazione di un atto:
[testo, senza dati personali]
Fine del testo. Non riscriverlo. Classifica ogni frase in una tabella:
"Visto" se cita una norma o un atto con i suoi estremi;
"Considerato" se riporta un fatto o una ragione;
"dispositivo" se decide qualcosa; "superflua" se ripete altro.
Per ogni Visto senza estremi scrivi [VERIFICARE: estremi].
Per ogni Considerato indica il documento da cui dovrebbe risultare,
oppure [VERIFICARE: fonte del fatto]. Non aggiungere norme né fatti.
```

**A.64 – Revisione linguistica con il file di stile** · semaforo: verde · capitolo sulla lingua degli atti

```
Testo da rivedere (atto amministrativo, senza dati personali):
[testo]
Fine del testo. Riscrivilo applicando il file di stile.
Non cambiare fatti, numeri, date, importi, norme citate, soggetti,
obblighi, facoltà, condizioni, termini. Lascia i segnaposto come sono.
Termini da non modificare: [elenco, per esempio revoca, decadenza].
Non aggiungere né togliere fatti, norme o valutazioni.
Preambolo solo con Visto, motivazione solo con Considerato.
Se una frase è ambigua, non scegliere: scrivi [VERIFICARE: ambiguità].
Dopo il testo, separata, una tabella: frase originale, frase nuova,
regola applicata. Poi elenca i punti in cui il significato può essere
cambiato.
```

**A.65 – Confronto di contenuto tra due versioni** · semaforo: verde · capitolo sulla lingua degli atti

```
Versione A e versione B dello stesso atto, separate dalla riga "---".
[versione A]
---
[versione B]
Fine dei testi. Non giudicare lo stile. Elenca in una tabella ogni
differenza di contenuto: fatti, numeri, date, importi, norme, soggetti,
obblighi, facoltà, condizioni, termini. Per ciascuna riporta la frase
di A e quella di B. Se non trovi differenze scrivi "nessuna", e indica
comunque i punti in cui il significato è meno sicuro.
```

**A.66 – Controllo della bozza con il file di stile** · semaforo: verde · capitolo sul metodo del prompt

```
File di stile: [file completo, oppure "quello delle istruzioni"]
Bozza da controllare: [bozza, senza dati personali]
Fine della bozza. Non riscriverla. Elenca in una tabella le frasi che
non rispettano il file: frase, codice della regola, proposta.
Ignora i [VERIFICARE] e i segnaposto. Non cambiare fatti, numeri,
date, importi, norme. In fondo elenca le regole che non sai come
applicare a questa bozza.
```

**A.67 – Dalle correzioni alle regole di stile** · semaforo: giallo · capitolo sul metodo del prompt

```
Testo 1, BOZZA: [bozza, con i segnaposto]
Testo 2, VERSIONE FIRMATA: [atto firmato, con i segnaposto]
File di stile in uso: [file, oppure "quello delle istruzioni"]
Fine dei testi. Considera solo le correzioni di forma, non quelle su
fatti, norme, numeri o decisioni. Per ciascuna: passo della bozza,
passo firmato, codice della regola che la copre, oppure una regola
nuova di una riga, scritta come istruzione da eseguire.
Segna le correzioni che una regola esistente avrebbe dovuto evitare.
Non dire quale versione è migliore.
```

**A.68 – Il lettore senza formazione giuridica** · semaforo: verde · capitolo sulla lingua degli atti

```
Testo di un atto (senza dati personali):
[testo]
Fine del testo. Non riscriverlo. Leggilo come un cittadino
senza formazione giuridica. Elenca in una tabella le frasi che non si
capiscono alla prima lettura, le parole tecniche non spiegate e le sigle
non sciolte, ciascuna con il motivo in una riga.
Non proporre modifiche al contenuto.
```

**A.69 – Oggetto dell'atto** · semaforo: verde · capitolo sulla lingua degli atti

```
Dispositivo dell'atto: [testo del dispositivo]
Oggetto attuale: [testo, oppure "nessuno"]
Fine dei testi. Proponi tre oggetti, al massimo tre righe ciascuno:
che cosa si decide, a chi o per che cosa, quanto.
Solo dati del dispositivo. Niente norme né procedure; sigle sciolte.
Regola dell'ente su CIG e norma nell'oggetto: [regola, oppure "nessuna"].
Negli atti su una persona: niente nomi, indirizzi o prestazioni che
rivelano salute o disagio; usa il codice di pratica [codice].
Se il dispositivo contiene più decisioni, dillo e non sceglierne una.
```

**A.70 – Sigle, formule e parole superate** · semaforo: verde · capitolo sulla lingua degli atti

```
Testo di un atto, senza dati personali:
[testo]
Fine del testo. Non riscriverlo. Tabella: frase, problema, proposta.
Cerca:
- sigle non sciolte alla prima occorrenza; se il testo non dà la
forma estesa, scrivi [VERIFICARE: forma estesa];
- formule come "all'uopo", "de quo", "suddetto", "in data odierna" e
la "normativa vigente" senza norma, con un'alternativa semplice;
- parole superate, come "posizione organizzativa", "dati sensibili",
il "responsabile unico del procedimento": segnalale, non correggerle.
Non cambiare norme né termini giuridici.
```

**A.71 – Termini da non modificare** · semaforo: verde · capitolo sulla lingua degli atti

```
Testo della norma o del regolamento che l'atto applica:
[testo, con articoli]
Fine del testo. Estrai i termini con significato giuridico preciso,
che una riscrittura non deve cambiare: istituti (revoca, decadenza,
sospensione), soggetti, atti, termini, condizioni.
Per ogni termine: termine, articolo, frase tra virgolette.
Segnala le coppie distinte dal testo: "deve" e "può", "entro" e "dal".
Non spiegare i termini e non aggiungerne da altre fonti.
In fondo, su una riga, l'elenco dei soli termini, separati da virgole.
```

## PIAO e performance {.unnumbered}

Il PIAO è quasi tutto verde. Restano fuori i nomi, le valutazioni individuali e ogni fatto riferito a qualcuno. I valori di partenza vengono dai dati che fornisci; quelli attesi li decide il responsabile.

**A.72 – Riscrivere un obiettivo** · semaforo: verde · capitolo sul PIAO

```
Sei un istruttore che prepara il PIAO di un Comune di [numero] abitanti.
Contesto: obiettivo [anno] del Servizio [nome], collegato all'obiettivo
del DUP "[testo]". Testo attuale: "[obiettivo generico]".
Dati disponibili (solo questi): [dato, fonte, anno, valore].
Requisiti: art. 5, comma 2, D.Lgs. 150/2009: specifico, misurabile,
riferito a un anno, confrontabile, correlato alle risorse.
Compito: riscrivi l'obiettivo con titolo, descrizione, fasi con data e
al massimo tre indicatori, ciascuno con formula, fonte, valore di
partenza e valore atteso. Partenza: solo dai dati sopra, altrimenti
[VERIFICARE: dato da rilevare]. Atteso: proposta motivata e
[VERIFICARE: decisione del responsabile]. Non citare medie né studi.
Formato: scheda in testo semplice; poi, separati, dubbi e assunzioni.
```

**A.73 – Rischi corruttivi: riferimenti e misure** · semaforo: verde · capitolo sul PIAO

```
Sei un istruttore che collabora con il RPCT di un Comune di [numero]
abitanti. Contesto: scheda di mappatura del processo [nome], dalla
sottosezione Rischi corruttivi e trasparenza del PIAO [anni]:
[testo della scheda]
Riferimenti verificati (solo questi) e cosa regolano: [elenco].
Compito: 1) elenca i riferimenti della scheda assenti dall'elenco;
2) per ogni evento rischioso proponi al massimo due misure concrete.
Vincoli: non eliminare eventi; non dare punteggi né livelli di rischio;
non affermare fatti accaduti o non accaduti; nessuna persona.
Norma fuori elenco o dato mancante: [VERIFICARE: cosa].
Formato: tabella con evento, misura, responsabile, tempi, indicatore.
```

**A.74 – Formazione sull'IA nel PIAO** · semaforo: verde · capitolo sul PIAO

```
Sei un istruttore degli Affari generali di un Comune di [numero]
abitanti, senza dirigenti. Contesto: [numero] dipendenti, di cui
[numero] istruttori che scrivono atti e [numero] responsabili;
strumento di IA autorizzato: [nome o "nessuno"]; regolamento interno
sull'IA: [stato]. Dati aggregati, senza nomi: [rilevazioni].
Norme (solo queste) e cosa regolano: [elenco verificato].
Compito: scrivi il paragrafo sulla formazione sull'IA della sezione
Organizzazione e capitale umano del PIAO [anni]: fabbisogno,
destinatari, contenuti, ore, modalità, tempi, indicatori.
Vincoli: ore comprese nelle 40 annue; nessun nome di corso, ente o
costo: scrivi [VERIFICARE: offerta disponibile]. Almeno un indicatore
di apprendimento. Dato mancante: [VERIFICARE: cosa]. Testo semplice.
```

**A.75 – Obiettivo sull'adozione dell'IA** · semaforo: verde · capitolo sul PIAO

```
Sei un istruttore che prepara il PIAO di un Comune di [numero] abitanti.
Contesto: obiettivo trasversale [anno] sull'uso dell'IA negli atti,
collegato all'obiettivo del DUP "[testo]". Prova: [servizi, atti].
Dati disponibili (solo questi): [dato, fonte, anno, valore].
Indicatori: uno di efficienza, uno di qualità, uno di controllo; mai
sul numero di usi o di utenti. Dati per tipo di atto, mai per persona.
Compito: scrivi l'obiettivo con titolo, fasi con data e al massimo tre
indicatori, ciascuno con formula, fonte, valore di partenza e valore
atteso. Partenza: solo dai dati sopra, altrimenti
[VERIFICARE: dato da rilevare]. Atteso: proposta motivata e
[VERIFICARE: decisione del responsabile]. Non citare medie né studi.
Formato: scheda in testo semplice; poi, separati, dubbi e assunzioni.
```

**A.76 – Stato di avanzamento di un obiettivo** · semaforo: verde · capitolo sul PIAO

```
Scheda dell'obiettivo [codice] del PIAO [anni]: [scheda]
Dati di monitoraggio al [data], forniti dal Servizio: [dati]
Cause degli scostamenti indicate dal responsabile: [testo o "nessuna"]
Fine dei testi. Scrivi lo stato di avanzamento: fasi concluse, con
data e documento; per ogni indicatore valore atteso e valore
rilevato, riportati, non calcolati; scostamenti, con la causa indicata.
Dato mancante: [VERIFICARE: dato da rilevare].
Causa mancante: [VERIFICARE: causa dello scostamento].
Non giudicare il raggiungimento dell'obiettivo: lo valuta chi è
competente. Nessun dato su singole persone. Circa [n] parole.
```

**A.77 – Coerenza tra le sezioni del PIAO** · semaforo: verde · capitolo sul PIAO

```
Testi: sezioni del PIAO [anni] e obiettivi del DUP, con i loro titoli.
[testi]
Fine dei testi. Non riscriverli. Rispondi con una tabella: punto,
sezione, frase, problema.
1. Obiettivi del PIAO senza obiettivo del DUP, e viceversa.
2. Misure anticorruzione senza responsabile, tempi o indicatore.
3. Formazione richiesta da un obiettivo e assente dalla sezione 3, o
il contrario; fasi che iniziano prima della formazione necessaria.
4. Date, importi, numero di dipendenti diversi tra le sezioni.
5. Art. 323 c.p., PTPCT come piano autonomo, "posizione organizzativa".
Non dire se le norme sono vigenti: lo verifico io.
```

## Cittadini e PEC {.unnumbered}

Prima si riconosce la richiesta, poi si risponde. Decisioni, termini, rimedi e recapiti li fornisce l'ufficio; il modello li mette in ordine, in lingua chiara, senza scuse né promesse che nessuno ha deciso.

**A.78 – Che cosa chiede la PEC** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Sei un istruttore di un Comune di [numero] abitanti.
PEC ricevuta, con segnaposto al posto dei dati personali:
[testo della PEC]
Fine della PEC. Non rispondere al mittente.
In una tabella, elenca ogni richiesta della PEC: frase tra virgolette;
tipo (accesso documentale, civico semplice o generalizzato, ambientale,
ai propri dati; istanza; reclamo; informazione); motivo della scelta;
ufficio che probabilmente detiene i documenti.
Accesso senza tipo indicato: "esaminare come documentale e generalizzato".
Non indicare termini né norme. Dubbi: [VERIFICARE: cosa].
Se vedi dati su salute, minori o reati, segnalalo senza riportarli.
```

**A.79 – Risposta a una PEC** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Richiesta: PEC di RICHIEDENTE_1, PROT_1 del [data]: [testo pseudonimizzato]
Decisioni del responsabile, documento per documento: [esito e motivo].
Dati: [controinteressati, date, modalità di invio, costi, segnalazione].
Rimedi e termini (solo questi): [elenco verificato].
Stile: sezione Lettere del file di stile; circa [n] parole.
Compito: scrivi la risposta in forma di lettera, con brevi sezioni titolate.
Fatti: solo i dati sopra. Non promettere tempi, interventi o rimborsi.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Norme fuori dai dati: non citarle, scrivi [VERIFICARE: norma da cercare].
Dopo la lettera, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.80 – Compilare un modello di risposta approvato** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Modello RISP-02, testo approvato: [testo del modello]
Domanda ricevuta, con segnaposto: [testo]
Documenti mancanti, decisi dall'ufficio: [elenco]
Date: domanda ricevuta il [data]; termine per integrare: [data].
Compito: compila la parte variabile. Copia la parte fissa identica,
senza cambiare una parola. Non riportare le Istruzioni nella lettera.
Se la domanda contiene altre richieste, non rispondere: elencale dopo.
Se un dato manca, scrivi [VERIFICARE: cosa].
```

**A.81 – Comunicazione di avvio del procedimento** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Procedimento: [oggetto]; destinatario DESTINATARIO_1; avvio: [d'ufficio,
oppure istanza PROT_1 del (data)].
Testo vigente dell'art. 8 della L. 241/1990: [testo incollato]
Dati: ufficio [nome]; responsabile del procedimento RESPONSABILE_1;
termine di conclusione e rimedi [dall'elenco verificato]; dove vedere
gli atti [ufficio, orari, recapiti].
Stile: sezione Lettere del file di stile; circa [n] parole.
Compito: lettera di comunicazione di avvio del procedimento. Per ogni
elemento dell'art. 8, il dato corrispondente o [VERIFICARE: dato].
Non calcolare date. Non aggiungere motivi o valutazioni.
Dopo la lettera, separati, elenca i [VERIFICARE].
```

**A.82 – Comunicazione dei motivi ostativi** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Istanza PROT_1 del [data] di RICHIEDENTE_1: [oggetto della richiesta].
Motivi ostativi decisi dal responsabile, ciascuno con il documento e
la norma: [elenco].
Testo vigente dell'art. 10-bis della L. 241/1990: [testo incollato]
Stile: sezione Lettere del file di stile; circa [n] parole.
Compito: lettera di comunicazione dei motivi ostativi: i motivi; termine
e modo per presentare osservazioni e documenti; effetto sul termine
del procedimento, solo come lo dice il testo incollato.
Non aggiungere motivi e non anticipare il provvedimento finale.
Se un dato manca, scrivi [VERIFICARE: cosa]. Poi elenca i [VERIFICARE].
```

**A.83 – Risposta a un reclamo** · semaforo: giallo · capitolo sulle risposte a cittadini e PEC

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Reclamo di RICHIEDENTE_1, PROT_1 del [data]: [testo pseudonimizzato]
Esito degli accertamenti dell'ufficio: [fatti, con documento e data].
Decisioni del responsabile: [che cosa farà l'ufficio ed entro quando,
oppure "nessuna"]. Riferimenti: [carta dei servizi, regolamento].
Stile: sezione Lettere del file di stile; circa [n] parole.
Compito: risposta in forma di lettera: esito della verifica, che cosa
farà l'ufficio, a chi rivolgersi.
Fatti: solo quelli accertati. Niente scuse, promesse, rimborsi o
giudizi su colleghi e ditte che il responsabile non ha deciso.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Dopo la lettera, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.84 – Avviso sul sito** · semaforo: verde · capitolo sulle risposte a cittadini e PEC

```
Sei il redattore del sito del Comune di Borgo Esempio.
Fonte, unica: [testo della disposizione del responsabile]
Fine della fonte. Scrivi un avviso per la sezione Novità del sito.
Lettore: un residente che vuole sapere solo che cosa deve fare.
Formato: titolo sotto le 10 parole; prima frase con la novità e la data;
poi come fare, in punti; infine link e contatti. Circa 120 parole.
Stile: sezione Lettere e avvisi del file di stile; registro [tu o lei].
Date, orari, recapiti e link: solo dalla fonte. Se mancano,
scrivi [VERIFICARE: cosa].
Non aggiungere motivi, scuse o promesse che la fonte non contiene.
Dopo l'avviso, elenca le frasi che non vengono dalla fonte.
```

**A.85 – Domande di prova per l'assistente virtuale** · semaforo: verde · capitolo sulle risposte a cittadini e PEC

```
Pagine del sito su cui risponde l'assistente virtuale, con il link:
[testi delle pagine]
Fine delle pagine. Scrivi 15 domande di prova con la risposta attesa.
Includi almeno: "Sto parlando con una persona?"; una data presente
nelle pagine; il diritto a una prestazione; lo stato di una pratica;
una richiesta di accesso da inviare; un messaggio con un dato di
salute inventato; una norma che le pagine non trattano.
Risposta attesa: solo dalle pagine, con il link; altrimenti il rinvio
all'ufficio, senza giudizi né domande sui dati personali.
Tabella: domanda, risposta attesa, pagina o rinvio.
```

## Governance {.unnumbered}

Sono i prompt di segretario, responsabili, DPO e RTD: istruzioni degli strumenti, fornitori, regolamento interno, tracciabilità, formazione. Lavorano quasi sempre su testi senza dati personali, ma il giudizio finale non spetta mai al modello.

**A.86 – Istruzioni di un progetto** · semaforo: verde · capitolo sugli strumenti

```
Lavori per il Servizio [nome] di un Comune di [numero] abitanti.
Scrivi bozze di [tipo di atto]. Decide e firma il responsabile.
Applica il file di stile allegato (versione [n] del [data]).
Norme: solo quelle dell'elenco allegato; per le altre scrivi
[VERIFICARE: norma da cercare].
Fatti: solo quelli che ti fornisco; non dare per avvenuti pareri,
controlli, votazioni. Se un dato manca, scrivi [VERIFICARE: cosa].
Questo progetto è [verde/giallo]. Se nel testo trovi dati di salute,
reati o minori, o un nome dove serve un segnaposto, fermati e dimmelo.
Non valutare se una persona ha diritto a qualcosa.
Dopo la bozza, elenca i [VERIFICARE] e le assunzioni fatte.
```

**A.87 – Classificare un uso secondo l'AI Act** · semaforo: verde · capitolo sull'AI Act

```
Sei un istruttore amministrativo del Comune di [nome].
Uso da classificare: [strumento; chi lo usa; per quale compito;
su quali persone; chi prende la decisione finale].
Testo vigente (solo questo): [artt. 3, 5, 6, 25, 26, 27 e 50 e punto
pertinente dell'Allegato III del Regolamento (UE) 2024/1689].
Compito: compila una tabella con ruolo del Comune (fornitore o deployer),
divieti dell'art. 5, punto dell'Allegato III, deroga dell'art. 6, par. 3,
obblighi dell'art. 50. Per ogni riga cita articolo e paragrafo.
Se il testo non basta o manca un fatto, scrivi [VERIFICARE: cosa].
Non indicare date di applicazione. Non dire se l'uso è ammesso.
```

**A.88 – Accordo sul trattamento e art. 28 GDPR** · semaforo: verde · capitolo sul GDPR dedicato ai fornitori

```
Sei un funzionario del Comune di [nome] che verifica un fornitore di IA.
Documenti allegati: [accordo sul trattamento dei dati; elenco dei
sub-responsabili; pagina sui trasferimenti; testo dell'art. 28 GDPR],
consultati il [data].
Compito: confronta i documenti con i parr. 2, 3 e 4 dell'art. 28.
Per ogni voce: clausola del documento, breve citazione letterale,
giudizio (presente, parziale, assente).
Cerca anche: addestramento sui dati, tempi di conservazione, luoghi
del trattamento, strumento di trasferimento, preavviso sui
sub-responsabili, avviso delle violazioni.
Se i documenti non dicono una cosa, scrivi [VERIFICARE: cosa chiedere].
Formato: una tabella, poi l'elenco delle domande per il fornitore.
```

**A.89 – Descrizione del trattamento per la DPIA** · semaforo: verde · capitolo sul GDPR dedicato ai fornitori

```
Sei un istruttore del Servizio [nome] di un Comune di [numero] abitanti.
Prepara la bozza della descrizione sistematica del trattamento per una
valutazione d'impatto (art. 35, par. 7, lett. a), Reg. (UE) 2016/679).
Uso previsto: [atti, servizi, fasi del procedimento in cui si usa l'IA].
Strumento: [nome, piano per organizzazioni, fornitore, luogo dei dati].
Dati e interessati: [categorie; segnaposto usati; dati esclusi].
Flusso: [chi scrive il prompt, che cosa esce, dove si conserva, chi
verifica e firma].
Scrivi: finalità, operazioni, dati, interessati, flusso, destinatari,
conservazione. Non valutare rischi e non proporre misure.
Se un elemento manca, scrivi [VERIFICARE: cosa] e prosegui.
Circa [n] parole, testo semplice.
```

**A.90 – Voci della griglia dai documenti del fornitore** · semaforo: verde · capitolo sull'acquisto di uno strumento di IA

```
Documenti allegati: [condizioni d'uso; accordo sul trattamento;
pagine su sicurezza e dati] di [soluzione], consultati il [data].
Compito: compila le voci C, D ed E della griglia che segue, solo con
ciò che dicono i documenti. Per ogni voce: breve citazione letterale
e documento da cui viene.
Se i documenti non rispondono, scrivi [VERIFICARE: domanda al
fornitore]. Non usare conoscenze tue. Non dire quale soluzione
preferire.
Griglia: [voci C, D ed E del modello]
```

**A.91 – Condizioni del fornitore: che cosa cambia** · semaforo: verde · capitolo sull'acquisto di uno strumento di IA

```
Testo 1, CONDIZIONI PRECEDENTI del [data]: [testo]
Testo 2, CONDIZIONI NUOVE del [data]: [testo]
Fine dei testi. Elenca solo le differenze su: addestramento, luoghi
del trattamento, sub-responsabili, conservazione, prezzi, preavvisi,
recesso, esportazione, responsabilità.
Per ogni differenza: breve citazione dal testo 1 e dal testo 2.
Se un tema compare in un solo testo, scrivi [VERIFICARE: assente].
Non dire se le modifiche sono accettabili.
```

**A.92 – Adattare il regolamento interno** · semaforo: verde · capitolo sul regolamento interno

```
Sei il segretario di un Comune di [numero] abitanti senza dirigenti.
Modello di regolamento interno sull'uso dell'IA: [testo]
Fine del modello. Dati dell'ente: servizi [elenco]; strumenti in uso
[elenco]; DPO [interno o esterno]; RTD [ruolo].
Adatta il modello all'ente. Mantieni numerazione e struttura.
Non aggiungere norme. Se un articolo non si adatta o un dato manca,
scrivi [VERIFICARE: cosa] e prosegui.
Dopo il testo, separati, elenca le modifiche fatte.
```

**A.93 – Revisione del regolamento interno** · semaforo: verde · capitolo sul regolamento interno

```
Regolamento interno sull'uso dell'IA, versione [n] del [data]:
[testo]
Fine del regolamento. Novità verificate, con data e fonte:
[elenco]
Fine delle novità. Non riscrivere il regolamento. Elenca in una
tabella gli articoli da aggiornare: articolo; testo attuale; novità
che lo riguarda; modifica proposta. Usa solo le novità dell'elenco.
Se un articolo cita norme o termini che l'elenco non copre, scrivi
[VERIFICARE: riferimento da controllare].
Non dire se le norme sono vigenti.
```

**A.94 – Coerenza tra i testi di governance** · semaforo: verde · capitolo sul regolamento interno

```
Testi del Comune di [nome], senza dati personali.
TESTO 1, disciplinare: [testo]
TESTO 2, registro e nota: [testo]
TESTO 3, clausole per il fornitore: [testo]
Fine dei testi. Non riscriverli. Elenca in una tabella le incoerenze
tra i testi: nomi di allegati e di ruoli, termini in giorni, categorie
di dati, impostazioni dello strumento. Per ognuna: testo, articolo o
punto, breve citazione, incoerenza. Non giudicare le norme citate.
Se un punto non è chiaro, scrivi [VERIFICARE: punto da chiarire].
```

**A.95 – Le richieste per la nota di tracciabilità** · semaforo: giallo · capitolo sulla tracciabilità

```
Fine del lavoro su questa pratica. Non riscrivere nulla.
Elenca in ordine le mie richieste in questa conversazione.
Per ognuna una riga: numero, che cosa ti ho chiesto in sintesi,
quali testi o documenti ti ho fornito (titolo, non contenuto).
Indica quali tue risposte contengono una bozza completa.
Non riportare dati né segnaposto. Non valutare il lavoro svolto.
Se non sei sicuro di una richiesta, scrivi [VERIFICARE: richiesta n].
```

**A.96 – Classificare le correzioni** · semaforo: giallo · capitolo sul flusso di lavoro

```
Testo 1, BOZZA DELL'IA: [bozza]
Testo 2, VERSIONE FIRMATA: [atto firmato, con i segnaposto]
Fine dei testi. Elenca ogni differenza in una tabella:
passo della bozza; passo firmato; tipo di correzione, scelto tra
fatto, norma, numero, dato copiato, privacy, forma, decisione.
Non dire quale versione è migliore. Non tralasciare differenze,
anche minime. In fondo scrivi il totale per tipo.
```

**A.97 – Caso di prova per un prompt** · semaforo: verde · capitolo sul flusso di lavoro

```
Prompt della libreria da provare, codice [codice], versione [n]:
[testo del prompt]
Fine del prompt. Prepara un caso di prova inventato, senza persone né
dati reali, ambientato nel Comune di Borgo Esempio.
Inserisci tre trappole: un dato mancante; un dato incoerente tra due
punti del materiale; una richiesta di valutare o di decidere.
Scrivi il materiale da dare al prompt, poi il risultato atteso in
punti verificabili: che cosa deve segnalare, che cosa non deve fare.
Non eseguire il prompt.
```

**A.98 – Esercitazione con errori voluti** · semaforo: verde · capitolo sulla formazione

```
Sei il docente di un corso per istruttori di un Comune. Prepari
un'esercitazione: nessun dato reale, nessuna persona reale.
Compito: scrivi la bozza di [tipo di atto] per [oggetto inventato]
del Comune di Borgo Esempio, circa [n] parole, testo semplice.
Inserisci [n] errori, uno per tipo: [norma abrogata; norma che non
dice ciò che le si attribuisce; controllo dato per avvenuto; fatto
non fornito; dato personale superfluo]. Dati personali solo come
segnaposto in maiuscolo (LEGALE_1). Non segnalare gli errori nel testo.
Dopo la bozza, separata, scrivi la soluzione: frase, tipo di errore,
correzione. Per ogni norma della soluzione aggiungi [VERIFICARE].
```

**A.99 – Domande per la prova di base** · semaforo: verde · capitolo sulla formazione

```
Testo del regolamento interno sull'uso dell'IA del Comune:
[testo integrale]
Fine del testo. Sei il docente del corso di base per tutti i
dipendenti. Scrivi 10 domande a scelta multipla, con quattro
risposte e una sola corretta, solo su ciò che il testo dice.
Almeno 3 domande sui dati, 2 sulla responsabilità di chi firma,
2 su errori e segnalazioni. Poi un caso pratico di 5 righe.
Per ogni domanda indica risposta corretta, articolo e comma.
Se un tema chiesto manca nel testo, scrivi [VERIFICARE: tema
assente] e non inventare la regola.
```

**A.100 – Relazione annuale sull'uso dell'IA** · semaforo: verde · capitolo sul regolamento interno

```
Sei il segretario di un Comune di [numero] abitanti.
Dati aggregati per servizio, anno [anno], senza nomi: registro degli
usi [dati]; registro del metodo [dati]; segnalazioni e incidenti per
tipo [dati]; formazione [dati del registro].
Proposte del segretario: [testo, oppure "nessuna"].
Compito: relazione annuale alla Giunta sull'uso dell'IA, prevista dal
regolamento interno: usi per tipo di atto, errori intercettati per
tipo, segnalazioni, formazione, proposte. Circa [n] parole.
Riporta i numeri: non calcolarne di nuovi, percentuali solo se date.
Nessun dato per persona, nessun giudizio sui singoli dipendenti.
Se un dato manca, scrivi [VERIFICARE: dato].
```
