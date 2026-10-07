# L'istruttoria con l'IA: leggere, sintetizzare, confrontare

In questo capitolo: come far leggere all'IA documenti lunghi, ottenere sintesi con citazioni, confrontare due versioni di un testo, preparare la scheda di un procedimento e quella di un bando, e che cosa resta al funzionario.

## Il problema: una sintesi sembra neutrale

L'istruttoria non si vede nell'atto finito, ma lo regge. La motivazione indica i presupposti di fatto e le ragioni giuridiche della decisione "in relazione alle risultanze dell'istruttoria" (art. 3 della L. 7 agosto 1990, n. 241). Il responsabile del procedimento valuta requisiti e presupposti, accerta d'ufficio i fatti, può chiedere di rettificare dichiarazioni e istanze erronee o incomplete. L'organo che adotta il provvedimento, se è diverso, non può discostarsi dalle risultanze dell'istruttoria senza motivarlo (art. 6).[^1]

Leggere e riassumere è anche tra i lavori che più spesso si chiedono all'IA. Nella ricerca FPA del 2026 sintesi e analisi di documenti sono indicate dal 59% dei dipendenti pubblici che la usano, alla pari con la redazione di testi.[^2] Fra i dirigenti e i funzionari comunali intervistati da IFEL, oltre il 40% usa l'IA generativa nelle attività quotidiane, per esempio per sintetizzare documenti o scrivere bozze.[^3]

Una sintesi sembra neutrale, ma non lo è: sceglie che cosa tenere, e ciò che lascia fuori non si vede. In uno studio del 2025 su 4.900 riassunti di articoli scientifici, la maggior parte dei modelli ha reso le conclusioni più generali del testo originale, anche quando si chiedeva precisione; i loro riassunti contenevano generalizzazioni ampie quasi cinque volte più spesso di quelli scritti da persone.[^4] In un testo giuridico la cautela persa è un "salvo che", un "entro", un "di regola".

Il tema tocca già gli atti degli enti. Nel 2026 il TAR Marche ha esaminato una relazione istruttoria di gara con richiami giurisprudenziali inesatti, scritta con l'IA secondo il ricorrente. Ha respinto la censura: la relazione non era l'atto conclusivo, e valutazione e decisione erano rimaste umane, controllate, motivate e imputabili all'amministrazione.[^5] Per ogni procedimento la stessa regola è scritta nell'art. 14 della L. 23 settembre 2025, n. 132: l'IA si usa "in funzione strumentale e di supporto", e la persona resta "l'unica responsabile".[^6]

Il capitolo procede per esempi su Borgo Esempio. Documenti e risposte sono costruiti per questo libro: non sono uscite reali di un modello, ma contengono errori di tipi documentati, indicati nel commento. La regola è una: l'IA legge e ordina, tu accerti e valuti.

## Documenti lunghi: prima i testi, poi la domanda

### Quale documento, con quale strumento

Prima di caricare un documento, classificalo con la regola del semaforo del capitolo sugli strumenti. Il colore dipende da ciò che il documento contiene, non dal suo tipo.

| Documento | Colore | Strumento |
|---|---|---|
| circolare, bando, regolamento vigente | verde | ogni strumento ammesso per iscritto |
| bozza non approvata, testo in trattativa | giallo | solo quello dell'ente |
| istanza o relazione, nomi sostituiti | giallo | solo quello dell'ente |
| sentenza, nomi di persone sostituiti | giallo | solo quello dell'ente |
| relazione sociale, certificato medico | rosso | nessuno |
| atti su reati o su minori | rosso | nessuno |

"Quello dell'ente" è lo strumento autorizzato, con il contratto che designa il fornitore responsabile del trattamento (art. 28 GDPR). Sostituire i nomi con segnaposto riduce il rischio, ma non rende il testo anonimo: pseudonimizzare non è anonimizzare, e il giallo resta giallo. Per gli articoli delle banche dati a pagamento controlla anche la licenza.

### Il testo intero, leggibile, nella versione giusta

Il modello lavora su ciò che riceve, non su ciò che credi di avergli dato.

- Dai il testo, non il collegamento: uno strumento con ricerca sul web può aprire un'altra versione o una pagina di commento. Conserva nel fascicolo la copia caricata.
- Nei PDF scansionati e nelle tabelle il testo estratto può perdere righe, unire colonne, alterare cifre.
- Allegati, risposte ai quesiti (FAQ) e rettifiche sono documenti distinti: se non li carichi, per il modello non esistono.

Prima della domanda, chiedi un controllo di lettura.

```
Documento A – [titolo], [data], fonte: [sito o protocollo]
[testo integrale]
Fine del documento A.
Non riassumere e non commentare. Elenca le parti del documento A
che hai ricevuto, nell'ordine: titoli, articoli o paragrafi, allegati,
tabelle. Riporta le prime e le ultime dieci parole del testo.
Segnala parti illeggibili, interrotte, o richiamate ma assenti.
```

Confronta l'elenco con l'indice e le ultime parole con l'ultima pagina. Se manca qualcosa, correggi il caricamento prima di chiedere altro.

### L'ordine del prompt

Come anticipato nel capitolo sul metodo del prompt, i documenti lunghi vanno in alto, la richiesta in fondo: nei test di Anthropic, con documenti di decine di pagine, quest'ordine ha migliorato la qualità delle risposte fino al 30%.[^7] Dai a ogni documento un'etichetta con titolo, data e fonte, e chiudilo con "Fine del documento": così il modello distingue meglio i testi tra loro e dalle istruzioni.

Che un documento entri tutto nel prompt non significa che il modello lo legga tutto con la stessa attenzione. In uno studio del 2024 i modelli usavano meglio le informazioni all'inizio e alla fine di un testo lungo che quelle a metà.[^8] Per un documento di molte decine di pagine fai la stessa domanda per parti, un capo o un gruppo di articoli alla volta.

### Molti documenti: i taccuini di fonti

Quando i documenti sono molti, come un avviso con allegati e FAQ, sono utili i taccuini di fonti come NotebookLM, che dal luglio 2026 si chiama Gemini Notebook: rispondono a partire dai documenti caricati e indicano il passo da cui prendono ogni informazione.[^9] Le regole non cambiano: la scelta delle fonti è tua, il rinvio al passo va controllato, e il semaforo decide che cosa caricare e con quale account.

## Sintesi con citazioni: ogni affermazione legata a un passo

### A che cosa serve, com'è fatta

La sintesi istruttoria è un documento di lavoro: aiuta ad accertare i fatti (art. 6 della L. 241/1990) e prepara la motivazione (art. 3). Resta nel fascicolo, accanto ai documenti che riassume.

Una sintesi controllabile ha quattro parti:

1. intestazione: documento, data, fonte, numero di pagine;
2. passi rilevanti copiati parola per parola, numerati, con pagina o articolo;
3. punti della sintesi, ciascuno con il numero del passo da cui viene;
4. "il documento non dice": le domande rimaste senza risposta.

Anthropic dà due indicazioni utili qui. Per i documenti lunghi, far estrarre prima le citazioni pertinenti e rispondere solo dopo. Contro le invenzioni, fondare la risposta su citazioni letterali e ritirare ogni affermazione priva di un passo a sostegno.[^10] Il prompt le applica entrambe.

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

### L'esempio: la relazione dell'ASD Borgo Esempio

Il Servizio Affari generali istruisce la domanda di contributo annuale dell'ASD Borgo Esempio, il caso introdotto nel capitolo su come funziona lo strumento. La relazione sull'attività della stagione 2025/2026 conta sei pagine. Sono stati tolti i nomi di dirigenti, allenatori e atleti e i dettagli che permettono di riconoscerli; il testo resta comunque un dato personale, e si usa lo strumento dell'ente. Il tema del prompt è "attività della stagione, iscritti, uso degli impianti comunali, entrate e spese".

```
SINTESI CON CITAZIONI
Documento A: relazione sull'attività della stagione 2025/2026
dell'ASD Borgo Esempio, allegata alla domanda PROT_1, 6 pagine.

PASSI
P1 «Nella stagione 2025/2026 l'associazione ha svolto corsi di
pallavolo e ginnastica per bambini, ragazzi e adulti, da ottobre
a giugno» (pag. 1)
P2 «Gli iscritti alla stagione 2025/2026 sono 142, di cui 96 di età
inferiore a 18 anni» (pag. 2, tabella 1)
P3 «I corsi si svolgono nella palestra comunale tre pomeriggi alla
settimana» (pag. 2)
P4 «Le entrate per quote associative ammontano a euro 21.300,00»
(pag. 5)
P5 «Per la stagione 2026/2027 si chiede un contributo per l'acquisto
di attrezzature» (pag. 6)

SINTESI
1. Nella stagione 2025/2026 l'associazione ha tenuto corsi di
pallavolo e ginnastica per tre fasce d'età, da ottobre a giugno (P1).
2. Ha 142 iscritti, di cui 96 minorenni (P2).
3. Usa la palestra comunale tre pomeriggi alla settimana (P3).
4. È iscritta al Registro nazionale delle attività sportive
dilettantistiche (P1).
5. Le entrate da quote associative sono di euro 21.300,00 (P4).
6. Chiede un contributo per attrezzature (P5).

IL DOCUMENTO NON DICE
- quante ore di uso della palestra siano gratuite;
- quali spese l'associazione abbia sostenuto nella stagione.
```

### Il commento

*Il punto 4.* P1 non parla di alcun registro. Il modello ha aggiunto un fatto verosimile per un'associazione sportiva e lo ha agganciato a un passo: il rinvio lo fa sembrare verificato. Controlla il punto con il suo passo, non solo il passo con il documento. L'iscrizione a un registro, se il regolamento la richiede, si accerta comunque d'ufficio.

*Il documento non dice.* L'ultima riga è falsa: a pagina 5 il rendiconto riporta anche le uscite. Il modello ha estratto il passo sulle entrate e ha concluso che il resto mancasse. Un'assenza dichiarata si controlla come un'affermazione.

*I passi.* Cercali nel file originale con un frammento di quattro o cinque parole: nei PDF a capo e sillabazioni fanno fallire la ricerca di frasi intere. Qui si trovano tutti. I dati sugli iscritti minorenni sono aggregati e non identificano nessuno.

### Errori tipici

- Fatti verosimili agganciati a un passo che non li contiene.
- Citazioni ritoccate: parole cambiate tra virgolette, passi chiusi prima di una condizione.
- Generalizzazioni: "può" diventa "deve", "di regola" sparisce, l'eccezione diventa regola.
- Assenze false: "il documento non dice" su ciò che c'è.

## Confrontare due versioni: regolamenti, convenzioni, capitolati

### Quando serve, come si divide il lavoro

Il confronto serve quando si modifica un regolamento e se ne prepara il testo a fronte. Di regola lo approva il Consiglio comunale; il regolamento sull'ordinamento degli uffici e dei servizi spetta invece alla Giunta. Lo prevede l'art. 42, comma 2, lettera a), del D.Lgs. 18 agosto 2000, n. 267 (TUEL).[^11] Il confronto serve anche quando si rinnova una convenzione, o si scrive un capitolato partendo dal precedente. La domanda è doppia: che cosa cambia, e con quale effetto.

Alla prima risponde meglio un programma. La funzione di confronto dell'elaboratore di testi (in Word, Confronta nella scheda Revisione; in LibreOffice Writer, il comando Confronta documento) segnala in modo meccanico le differenze tra i due file: non ne inventa, ma non spiega nulla. Se hai solo PDF, convertili e controlla la conversione: il confronto vale quanto il testo che riceve. L'IA spiega l'effetto, ma può perdere una modifica o inventarla. Usa prima il programma, poi l'IA, articolo per articolo; infine controlla che i due elenchi coincidano.

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

### L'esempio: la convenzione per la palestra comunale

La convenzione con cui l'ASD Borgo Esempio usa la palestra comunale scade il 31 dicembre 2026, e l'associazione propone un nuovo testo di nove articoli. È una trattativa in corso, quindi un documento giallo: si usa lo strumento dell'ente.

```
CONFRONTO – Convenzione per l'uso della palestra comunale
Testo 1: convenzione vigente. Testo 2: proposta dell'ASD.

1. Art. 2, durata. Tipo: sostituito.
T1 «La convenzione ha durata triennale, dal 1 gennaio 2024
al 31 dicembre 2026.»
T2 «La convenzione ha durata triennale, dal 1 gennaio 2027
al 31 dicembre 2029, e si rinnova tacitamente per uguale periodo
in assenza di disdetta.»
Effetto: aggiunge il rinnovo automatico.

2. Art. 4, orari. Tipo: sostituito.
T1 «L'associazione può utilizzare la palestra il lunedì, il mercoledì
e il venerdì dalle 17 alle 21.»
T2 «L'associazione utilizza la palestra dal lunedì al venerdì dalle 17
alle 21 e il sabato dalle 9 alle 13.»
Effetto: le fasce settimanali passano da tre a sei.

3. Art. 6, manutenzione. Tipo: sostituito.
T1 «La manutenzione ordinaria è a carico dell'associazione.»
T2 «La manutenzione ordinaria è a carico del Comune.»
Effetto: la manutenzione ordinaria passa al Comune.

4. Art. 7, corrispettivo. Tipo: invariato.
T1 «L'associazione versa al Comune euro 1.500,00 annui.»
T2 «L'associazione versa al Comune euro 1.500,00 annui.»

5. Art. 9, recesso. Tipo: aggiunto.
T2 «Il Comune può recedere con un preavviso di dodici mesi.»
Effetto: introduce il recesso del Comune, con preavviso.

TOTALE: 4 modifiche. Articoli invariati: 1, 3, 5, 7, 8.
```

### Il commento

Il programma segnala sei articoli modificati: 2, 4, 6, 7, 8 e 9. L'elenco dell'IA ne riconosce quattro.

*Art. 7.* Nella proposta il corrispettivo è di euro 1.050,00. Il modello ha riportato nel testo 2 la cifra del testo 1 e ha dichiarato l'articolo invariato: la citazione tra virgolette era sbagliata. Numeri e date si prendono dal confronto del programma.

*Art. 8.* La proposta toglie il massimale minimo della polizza di responsabilità civile; il modello lo dà per invariato.

*Il totale.* "4 modifiche" torna con l'elenco dell'IA, non con il documento: la coerenza interna non prova la completezza. Per questo si conta con il programma.

*Art. 2.* Il rinnovo tacito è descritto senza giudizi, come chiesto. Se la clausola sia ammissibile non lo dice il confronto: è una questione giuridica da valutare con il segretario comunale.

*Art. 4.* L'effetto conta le fasce, ma tace sul passaggio da "può utilizzare" a "utilizza": da una facoltà a un orario riservato. Pesa sulle scuole e sulle altre associazioni: se ne parla nell'ultima sezione.

### Errori tipici

- Numeri e date di una versione copiati nell'altra.
- Modifiche piccole perse: "può" e "deve", "e" e "o", "entro" e "dopo", un rinvio.
- Spostamenti letti come soppressione e aggiunta; cambi di numerazione letti come modifiche.
- Effetti con giudizi: "migliorativa", "più favorevole al Comune".
- Confronto interrotto a metà nei testi lunghi, con un totale che sembra tornare.

## La scheda di procedimento: fasi, termini e responsabile

### Le norme

La L. 241/1990 fissa l'ossatura di ogni procedimento: unità organizzativa e responsabile (artt. 4-6), termine di conclusione (art. 2), comunicazione di avvio (artt. 7 e 8), preavviso di rigetto nei procedimenti a istanza di parte (art. 10-bis). Per i contributi servono criteri predeterminati e pubblicati (art. 12).[^12]

Sul termine, l'art. 2 dà quattro regole. Il termine lo fissano la legge o il regolamento dell'ente; in mancanza è di trenta giorni. Può essere sospeso una sola volta, per non più di trenta giorni, per acquisire informazioni o certificazioni su fatti, stati o qualità che non risultano da documenti già in possesso dell'amministrazione e non si possono acquisire direttamente da altre amministrazioni. In caso di inerzia interviene il titolare del potere sostitutivo. Nei provvedimenti adottati in ritardo su istanza di parte si indicano il termine previsto e quello effettivamente impiegato.[^13]

La scheda di procedimento raccoglie queste informazioni per un tipo di pratica. È la mappa del fascicolo, la traccia della comunicazione di avvio e la base della pagina che l'art. 35 del D.Lgs. 14 marzo 2013, n. 33, chiede di pubblicare in Amministrazione trasparente per ogni tipologia di procedimento.[^14] L'IA la ricava dal regolamento e dalle norme che le dai; le date della singola pratica le calcoli tu.

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

### L'esempio: i contributi ordinari alle associazioni

Il prompt contiene il Regolamento comunale di Borgo Esempio per la concessione di contributi. L'elenco delle norme comprende gli artt. 2, 5, 10-bis e 12 della L. 241/1990 e gli artt. 26 e 27 del D.Lgs. 33/2013. Non ci sono persone: il documento è verde.

```
SCHEDA DEL PROCEDIMENTO
Contributi ordinari annuali alle associazioni – Comune di Borgo Esempio

Oggetto: contributi ad associazioni senza scopo di lucro per attività
svolte nel territorio comunale (Reg. art. 1).
Avvio: a istanza di parte, entro il 31 marzo (Reg. art. 5).
Unità organizzativa: Servizio Affari generali (Reg. art. 3).
Responsabile del procedimento: il responsabile del Servizio o il
dipendente da lui assegnato (L. 241/1990, art. 5).
Organo che decide: Giunta comunale (Reg. art. 9).
Fasi:
1. domanda con il modulo comunale (Reg. art. 5);
2. ammissibilità e richiesta di integrazioni (Reg. art. 6);
3. valutazione con i criteri e i punteggi (Reg. art. 7);
4. graduatoria e proposta di riparto (Reg. art. 8);
5. concessione con determinazione (Reg. art. 9);
6. rendiconto e liquidazione (Reg. artt. 11 e 12).
Termine: 60 giorni dalla scadenza delle domande (Reg. art. 8).
Sospensioni: una volta, al massimo 30 giorni, per acquisire
informazioni o certificazioni (L. 241/1990, art. 2, comma 7).
Il preavviso di rigetto interrompe il termine (L. 241/1990,
art. 10-bis).
Controlli: [VERIFICARE: controlli sulle dichiarazioni sostitutive].
Pubblicazioni: albo online; Amministrazione trasparente se i
contributi superano mille euro nell'anno (D.Lgs. 33/2013, art. 26).
Tutela: [VERIFICARE: autorità e termine per il ricorso].
Potere sostitutivo: segretario comunale [VERIFICARE: atto che lo
individua].
```

### Il commento

*L'organo.* La scheda indica la Giunta e, poche righe sotto, la "concessione con determinazione". L'art. 9 del regolamento affida la concessione al responsabile del servizio, sulla base degli indirizzi della Giunta: il modello ha fuso i due soggetti. Concedere contributi secondo criteri predeterminati è di regola un atto di gestione (art. 107, comma 3, lett. f), TUEL). A Borgo Esempio spetta al responsabile del servizio, cui il sindaco ha attribuito le funzioni dirigenziali con decreto motivato (art. 109, comma 2).[^15] Un organo sbagliato nella scheda rischia di diventare un atto dell'organo incompetente.

*Il preavviso di rigetto.* "Interrompe" è il testo anteriore al 2020. Dopo il D.L. 16 luglio 2020, n. 76, la comunicazione dei motivi ostativi sospende il termine, che riprende dieci giorni dopo le osservazioni o, se mancano, alla scadenza dei dieci giorni concessi per presentarle.[^16] L'articolo era nell'elenco, ma il modello lo ha descritto a memoria. Nell'elenco scrivi che cosa dice ogni norma, o incolla il testo vigente degli articoli che contano. Resta poi una domanda che la scheda non pone: l'art. 10-bis non si applica alle procedure concorsuali, e una graduatoria tra associazioni potrebbe rientrarvi. Valutala con il segretario comunale.

*Le pubblicazioni.* La soglia c'è, ma manca l'effetto: oltre i mille euro nell'anno solare allo stesso beneficiario, la pubblicazione è condizione legale di efficacia del provvedimento (art. 26, comma 3).[^17]

*Ciò che manca.* Non c'è la comunicazione di avvio (artt. 7 e 8), che nei procedimenti a istanza di parte indica anche la data dell'istanza.[^18] Gli articoli non erano nell'elenco, e il prompt ammette solo le fonti date. Come si è visto nel capitolo sul metodo del prompt, limitare le norme taglia anche ciò che serve: dopo la scheda, usa la richiesta aperta di quel capitolo per cercare ciò che manca.

*Il potere sostitutivo.* Il [VERIFICARE] è giusto: cerca l'atto che individua il titolare; in mancanza vale la regola dell'art. 2, comma 9-bis.

### Errori tipici

- Organo competente sbagliato: Giunta, Consiglio e responsabile scambiati.
- Norme descritte in una versione superata, come il preavviso che "interrompe".
- Termine di trenta giorni dove il regolamento ne fissa un altro.
- Fasi "di prassi" aggiunte senza fonte, come un parere che il regolamento non prevede.
- Nomi di persone al posto dei ruoli, date calcolate nonostante il divieto.

## Bandi e avvisi di finanziamento: requisiti, scadenze e documenti

### Le norme e la struttura

L'avviso è la regola della procedura: vincola chi partecipa e chi lo ha pubblicato, e un'ora di ritardo può bastare per l'esclusione. La candidatura coinvolge più servizi: di solito la Giunta decide se partecipare e approva il progetto, il Servizio finanziario verifica la copertura del cofinanziamento, il Servizio tecnico prepara il progetto e acquisisce il codice unico di progetto (CUP). Gli atti che dispongono il finanziamento pubblico o autorizzano l'esecuzione di progetti di investimento pubblico sono nulli senza il CUP (art. 11, comma 2-bis, della L. 16 gennaio 2003, n. 3).[^19]

La scheda del bando riporta, per ogni voce, il passo e l'articolo. Un avviso pubblicato è verde: va bene ogni strumento ammesso per iscritto.

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

### L'esempio: il bando "Sport in Comune 2027"

La Fondazione Esempio, un ente inventato per questo libro, pubblica un avviso per gli impianti sportivi comunali. Il responsabile del Servizio tecnico deve capire se proporre alla Giunta la candidatura della palestra. L'avviso ha quattordici pagine e dodici articoli; c'è una pagina di FAQ.

```
SCHEDA AVVISO – "Sport in Comune 2027", Fondazione Esempio
Letti: A, avviso, articoli 1-11; B, FAQ 1-5.

Beneficiari: «Comuni con popolazione inferiore a 10.000 abitanti»
(A, art. 3, comma 1).
Impianti: «di proprietà comunale e aperti all'uso di associazioni
sportive del territorio» (A, art. 3, comma 2).
Spese ammissibili: lavori, forniture e spese tecniche «nel limite del
10% dell'importo dei lavori» (A, art. 5, comma 2). IVA: «ammissibile
solo se non recuperabile» (B, FAQ 3).
Contributo: «fino all'80% della spesa ammissibile e comunque non oltre
euro 150.000,00» (A, art. 6, comma 1). Il resto è a carico del
Comune (A, art. 6, comma 2).
Scadenza e invio: «entro le ore 12:00 del 15 gennaio 2027» (A, art. 8,
comma 1), «esclusivamente tramite la piattaforma della Fondazione»
(A, art. 8, comma 2).
Documenti: progetto di fattibilità tecnico-economica; cronoprogramma;
CUP; deliberazione che approva il progetto e assicura il cofinanziamento
(A, art. 9). Firma: [VERIFICARE: firma digitale richiesta?].
Criteri: qualità del progetto 40 punti; risparmio energetico 30; utenza
giovanile 20; cofinanziamento oltre la quota minima 10 (A, art. 10).
Esclusione: «domande pervenute oltre il termine o con modalità diverse»
(A, art. 8, comma 3).
Obblighi: avvio dei lavori «entro sei mesi» e conclusione «entro
diciotto mesi dalla comunicazione di concessione» (A, art. 11).
Rendicontazione: [VERIFICARE: termine non trovato].
```

### Il commento

*Gli articoli letti.* L'intestazione dice "articoli 1-11", ma l'avviso ne ha dodici. L'ultima pagina, con l'art. 12 sulla rendicontazione, era un'immagine scansionata e non è entrata nel testo: il [VERIFICARE] finale nasce qui. Il controllo di lettura lo avrebbe segnalato prima.

*I beneficiari.* La citazione si chiude dopo "abitanti", ma l'art. 3, comma 1, prosegue: "che non abbiano ottenuto contributi dalla Fondazione nel triennio precedente". Tra virgolette chiuse è sparito un requisito che esclude. Cercando il passo nel file, lo vedi continuare.

*Scadenza e invio.* Ricontrollali sull'avviso, ora compresa, e segui FAQ e rettifiche fino alla scadenza: il modello conosce solo ciò che hai caricato quel giorno.

*Cofinanziamento e ammissibilità.* La quota del Comune la calcola il Servizio finanziario, non il modello. La scheda non dice se Borgo Esempio può partecipare, ed è corretto: popolazione e contributi ricevuti si accertano negli atti dell'ente. Per la proposta alla Giunta si veda il capitolo sulle delibere.

### Errori tipici

- Scadenze confuse: invio della domanda, inizio e fine dei lavori, rendicontazione; l'ora persa.
- Requisiti presi dall'edizione precedente del bando o da bandi simili.
- Criteri premiali letti come requisiti, e viceversa.
- Percentuali applicate alla base sbagliata: spesa ammissibile o costo totale.
- FAQ e rettifiche ignorate, o trattate come se prevalessero sempre sull'avviso.

## Cosa non delegare: valutazione dei fatti e bilanciamento degli interessi

In tutti gli esempi l'IA ha letto, ordinato, confrontato. Non ha accertato né deciso nulla, e non deve farlo.

*Accertare i fatti.* Il modello sa che la relazione dichiara 142 iscritti, non che siano 142. L'accertamento spetta al responsabile del procedimento (art. 6 della L. 241/1990): i documenti già in possesso di una pubblica amministrazione si acquisiscono d'ufficio, e sulle dichiarazioni sostitutive si fanno controlli, anche a campione (art. 18 della L. 241/1990 e artt. 43 e 71 del D.P.R. 28 dicembre 2000, n. 445).[^20]

*Valutare.* "Qualità del progetto" e "rilevanza sociale dell'attività" sono giudizi discrezionali. L'IA può accostare ogni criterio al passo che lo riguarda, come nella scheda istruttoria del capitolo sul flusso di lavoro; il punteggio lo assegna chi ne risponde, e i conti li fa il foglio di calcolo.

*Bilanciare.* La proposta di convenzione riserva all'ASD sei fasce settimanali. Le stesse ore possono servire alle scuole, ad altre associazioni, ai corsi del Comune. Scegliere tra questi interessi, con l'imparzialità chiesta dall'art. 97 della Costituzione, è il cuore della discrezionalità amministrativa. L'IA può elencare gli interessi che compaiono nei documenti; non conosce gli altri, e non ha titolo per pesarli. Lo stesso vale per il bando: candidarsi e garantire il cofinanziamento sono scelte della Giunta.

Per il Consiglio di Stato la decisione assistita da un algoritmo deve restare conoscibile e non esclusiva, con un contributo umano capace di controllarla, validarla o smentirla.[^21] Se una decisione su una persona fisica si basasse unicamente su un trattamento automatizzato, varrebbe anche l'art. 22 del GDPR, descritto nel capitolo sul GDPR e i dati nel prompt. E dove l'istruttoria riguarda prestazioni di assistenza pubblica essenziali, come molte prestazioni dei Servizi sociali, l'AI Act classifica ad alto rischio i sistemi destinati a valutarne l'ammissibilità. Il Comune che usa per questo scopo un chatbot generalista può diventarne fornitore (art. 25). La deroga per i compiti preparatori la valuta e la documenta il fornitore, e non vale mai in caso di profilazione. Il quadro, con le date, è nel capitolo sull'AI Act.[^22]

C'è infine un rischio più sottile: l'IA tende ad assecondare la tesi che le proponi (si veda il capitolo su come funziona lo strumento). Prima di chiudere l'istruttoria, chiedile di cercare ciò che non torna. Se la scheda riguarda persone, usa lo strumento dell'ente.

```
Testo 1, SCHEDA ISTRUTTORIA chiusa il [data]: [scheda]
Testo 2, DOCUMENTI citati nella scheda: [testi]
Proposta dell'ufficio: [esito proposto, in una frase]
Fine dei testi. Non dire se la proposta è giusta.
Elenca i passi dei documenti che la indeboliscono o la contraddicono,
tra virgolette, con la fonte. Poi i fatti che la proposta presuppone
e che i documenti non provano. Se non ne trovi, scrivi "nessuno".
```

Leggi l'elenco e decidi tu se cambia la proposta. Poi annota nel fascicolo l'uso dell'IA: strumento, data, prompt, documenti caricati e loro versione (si veda il capitolo sulla tracciabilità).

## Checklist prima della firma

Prima di caricare:

1. Il documento è classificato con il semaforo, e lo strumento è quello ammesso per quel colore.
2. Il testo caricato è intero e nella versione giusta, con allegati, FAQ e rettifiche; il controllo di lettura torna.

Su sintesi, confronti e schede:

3. Ogni passo tra virgolette si ritrova nel documento, intero, e ogni punto dice ciò che dice il suo passo, con limiti ed eccezioni.
4. Le voci "il documento non dice" e i [VERIFICARE] sono controllati e chiusi per iscritto.
5. Numeri, date, ore e importi sono confrontati con l'originale; i calcoli li hai rifatti tu.
6. Le modifiche trovate dall'IA coincidono con quelle del programma di confronto.
7. Organo competente, responsabile e termini vengono dal regolamento e da norme lette nel testo vigente.

Sulla decisione:

8. I fatti sono accertati negli atti e con i controlli, non nella sintesi.
9. Valutazioni, punteggi e scelte tra interessi sono tuoi o dell'organo competente, e la motivazione li spiega.
10. Il fascicolo registra strumento, data, prompt e documenti caricati.

## In sintesi

- Classifica ogni documento con il semaforo prima di caricarlo: nomi sostituiti non vuol dire testo anonimo.
- Dai all'IA il testo intero, non il collegamento; chiedi il controllo di lettura; metti i documenti in alto e la domanda in fondo.
- Una sintesi istruttoria lega ogni affermazione a un passo copiato parola per parola. Controlla il passo con il documento e il punto con il passo, assenze comprese.
- Nel confronto tra versioni il programma conta le modifiche, l'IA ne spiega l'effetto: i due elenchi devono coincidere.
- La scheda di procedimento nasce dal regolamento e da norme lette nel testo vigente; organo e termini si controllano uno per uno.
- La scheda di un bando cita ogni requisito e non dice se il Comune è ammesso.
- Accertare i fatti, valutare e bilanciare gli interessi restano al funzionario e all'organo che decide.

[^1]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 3, comma 1, e art. 6, comma 1, lett. a), b) ed e), normattiva.it.

[^2]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, su un campione di 500 dipendenti pubblici, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Segue la ricerca di informazioni, con il 57%. Sono dati dichiarati dagli intervistati.

[^3]: Fondazione IFEL, *Intelligenza artificiale nei Comuni italiani. Competenze, governance, territori*, 2026, fondazioneifel.it. L'indagine, su 664 dirigenti e funzionari comunali, è stata svolta nell'ambito del progetto AI-PACT. La scheda dell'IFEL parla di "oltre il 40%"; le sintesi pubblicate riportano il 41,9%.

[^4]: U. Peters e B. Chin-Yee, *Generalization bias in large language model summarization of scientific research*, in Royal Society Open Science, 2025, royalsocietypublishing.org. Lo studio confronta 4.900 riassunti prodotti da dieci modelli con i testi originali; per alcuni modelli le generalizzazioni eccessive riguardano tra il 26% e il 73% dei casi, e i modelli più recenti sono risultati in genere meno accurati dei precedenti.

[^5]: TAR Marche, sez. I, sentenza 1° giugno 2026, n. 758, giustizia-amministrativa.it. Il TAR ha confermato l'esclusione di un operatore economico per grave illecito professionale e ha escluso la violazione della riserva di umanità prevista dall'art. 30 del D.Lgs. 31 marzo 2023, n. 36: la relazione istruttoria del RUP non era l'atto conclusivo, e la responsabilità della scelta restava al dirigente competente. Commento in lavoripubblici.it, 2026.

[^6]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 2, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it.

[^7]: Anthropic, *Prompting best practices*, 2026, platform.claude.com, sezione sui prompt con contesto lungo: il dato riguarda documenti di oltre 20.000 token. La stessa sezione consiglia di racchiudere ogni documento in un'etichetta con la fonte e gli altri dati che lo identificano.

[^8]: N. F. Liu e altri, *Lost in the Middle: How Language Models Use Long Contexts*, in Transactions of the Association for Computational Linguistics, vol. 12, 2024, pp. 157-173, aclanthology.org. Lo studio riguarda modelli disponibili nel 2023.

[^9]: Google, *NotebookLM is now Gemini Notebook*, 2026, blog.google.

[^10]: Anthropic, *Prompting best practices*, cit., sezione sui prompt con contesto lungo, che consiglia di chiedere prima le citazioni pertinenti; Anthropic, *Reduce hallucinations*, 2026, platform.claude.com, che suggerisce di fondare le risposte su citazioni letterali e di ritirare le affermazioni prive di una citazione a sostegno, e avverte che queste tecniche riducono gli errori ma non li eliminano.

[^11]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, art. 42, comma 2, lett. a), che attribuisce al Consiglio i regolamenti, salvo quelli sull'ordinamento degli uffici e dei servizi, di competenza della Giunta (art. 48, comma 3), normattiva.it.

[^12]: L. 7 agosto 1990, n. 241, cit., artt. 2, 4, 5, 6, 7, 8, 10-bis e 12, normattiva.it. L'art. 12 subordina la concessione di sovvenzioni, contributi, sussidi e vantaggi economici alla predeterminazione e alla pubblicazione dei criteri e delle modalità.

[^13]: L. 7 agosto 1990, n. 241, cit., art. 2, commi 2, 7, 9-bis e 9-quinquies, normattiva.it. Il comma 2 fissa i trenta giorni per le amministrazioni statali e gli enti pubblici nazionali. Per gli enti locali, le disposizioni sulla conclusione del procedimento entro il termine e sulla sua durata massima attengono ai livelli essenziali delle prestazioni (art. 29, comma 2-bis): per questo il termine di trenta giorni si applica di regola anche ai Comuni che non ne abbiano fissato uno diverso.

[^14]: D.Lgs. 14 marzo 2013, n. 33, *Riordino della disciplina riguardante il diritto di accesso civico e gli obblighi di pubblicità, trasparenza e diffusione di informazioni da parte delle pubbliche amministrazioni*, art. 35, comma 1, normattiva.it.

[^15]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 107, comma 3, lett. f), che attribuisce ai dirigenti i provvedimenti di autorizzazione, concessione o analoghi il cui rilascio presuppone accertamenti e valutazioni, anche discrezionali, nel rispetto di criteri predeterminati dalla legge, dai regolamenti o da atti generali di indirizzo; art. 109, comma 2, che nei Comuni privi di personale con qualifica dirigenziale consente di attribuire queste funzioni ai responsabili degli uffici e dei servizi con provvedimento motivato del sindaco, normattiva.it.

[^16]: L. 7 agosto 1990, n. 241, cit., art. 10-bis, come modificato dall'art. 12 del D.L. 16 luglio 2020, n. 76, convertito dalla L. 11 settembre 2020, n. 120, normattiva.it. Prima della modifica la comunicazione interrompeva i termini, che iniziavano di nuovo a decorrere dalla presentazione delle osservazioni o dalla scadenza del termine per presentarle. Lo stesso articolo non si applica alle procedure concorsuali e ai procedimenti in materia previdenziale e assistenziale sorti a istanza di parte e gestiti dagli enti previdenziali.

[^17]: D.Lgs. 14 marzo 2013, n. 33, cit., art. 26, commi 2 e 3, normattiva.it. Che cosa pubblicare e come, e i limiti per i dati personali dei beneficiari, sono descritti nel capitolo sulla privacy prima della pubblicazione.

[^18]: L. 7 agosto 1990, n. 241, cit., art. 7 e art. 8, comma 2, lett. c-ter); sulla ricevuta che attesta la presentazione delle istanze, art. 18-bis, normattiva.it.

[^19]: L. 16 gennaio 2003, n. 3, *Disposizioni ordinamentali in materia di pubblica amministrazione*, art. 11, comma 2-bis, inserito dall'art. 41 del D.L. 16 luglio 2020, n. 76, convertito dalla L. 11 settembre 2020, n. 120, normattiva.it. La norma qualifica il CUP come elemento essenziale dell'atto.

[^20]: L. 7 agosto 1990, n. 241, cit., art. 6, comma 1, lett. b), e art. 18; D.P.R. 28 dicembre 2000, n. 445, *Testo unico delle disposizioni legislative e regolamentari in materia di documentazione amministrativa*, artt. 43 e 71, normattiva.it. L'art. 71 prevede controlli anche a campione, in misura proporzionale al rischio e all'entità del beneficio, e nei casi di ragionevole dubbio.

[^21]: Consiglio di Stato, sez. VI, sentenze 13 dicembre 2019, n. 8472, e 4 febbraio 2020, n. 881, giustizia-amministrativa.it. Il contenzioso riguardava la mobilità dei docenti gestita con un algoritmo.

[^22]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, art. 6, parr. 3, lett. d), e 4, art. 25, par. 1, lett. c), e Allegato III, punto 5, lett. a), eur-lex.europa.eu. Per i sistemi dell'Allegato III gli obblighi del capo III, sezioni 1-3, che comprendono l'art. 25, si applicano dal 2 dicembre 2027, per effetto del Regolamento (UE) 2026/1744.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 30 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- TAR Marche n. 758/2026: la bozza diceva che la decisione era 'rimasta del funzionario'.
- La bozza presentava l'art. 14 della L. 132/2025 come la regola applicata dal TAR Marche.
- Dato IFEL attribuito ai soli 'funzionari comunali' (l'indagine riguarda dirigenti e funzionari) e reso come 'la sintesi è tra gli usi quotidiani'.
- Art. 6 L. 241/1990: 'chiede di rettificare le istanze incomplete'.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
