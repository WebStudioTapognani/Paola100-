# Le determine

In questo capitolo: la determinazione del responsabile di servizio costruita con il metodo, dal contenuto obbligatorio alla firma, sul caso guida di un abbonamento da 1.200 euro, e poi liquidazione, accertamento di entrata e nomina del RUP.

## Il problema: l'atto più frequente

Con la determinazione il responsabile di servizio affida, impegna, liquida, accerta, nomina. In un Comune di 6.500 abitanti se ne firmano centinaia l'anno, quasi sempre partendo dalla precedente. Sembra l'atto più adatto all'IA, ed è quello in cui gli errori passano più facilmente: chi rilegge la centesima determina dell'anno guarda importo e fornitore, non il preambolo.

Il capitolo sul metodo del prompt ha usato una determina come banco di prova. Le bozze del prompt strutturato erano più prudenti di quelle generiche, ma non citavano l'art. 192 del D.Lgs. 18 agosto 2000, n. 267 (TUEL), che mancava dall'elenco delle norme. Qui lo stesso caso arriva fino alla firma; poi lo schema si applica alle altre determine ricorrenti.

Prima di scrivere il prompt, classifica il testo con la regola del semaforo (si veda il capitolo sugli strumenti). L'affidamento a una società, senza il nome del RUP né del legale rappresentante, è verde: va bene ogni strumento ammesso per iscritto dall'ente. Con RUP_1, o con una ditta individuale come fornitore, diventa giallo anche con i segnaposto. Allora passa solo dallo strumento dell'ente, con il contratto dell'art. 28 del Regolamento (UE) 2016/679 (GDPR). Il prompt del caso guida contiene RUP_1: è giallo.

## Il caso guida e il contenuto obbligatorio dell'atto

### Il caso

Il Servizio Affari generali di Borgo Esempio usa da tre anni una banca dati giuridica on line di Editrice Esempio S.r.l. Il contratto in corso, affidato con ATTO_1, scade il 31 dicembre 2026 e non prevede opzioni di rinnovo. Nella trattativa diretta avviata sul Mercato elettronico della pubblica amministrazione (MePA) il fornitore ha offerto per il 2027 euro 1.200,00 oltre IVA al 22%, il prezzo del 2026, e ha dichiarato di avere i requisiti. Lo stanziamento è sul capitolo 1043. Il RUP, RUP_1, ha dichiarato di non avere conflitti di interessi.

Senza un'opzione nel contratto in corso, "rinnovo" vuol dire nuovo affidamento, con una nuova decisione di contrarre. Il rinnovo tacito non è ammesso.[^1]

### Cosa deve dire l'atto

Due norme fissano il contenuto minimo, e si citano insieme. L'art. 192 del TUEL chiede una determinazione che indichi fine, oggetto, forma e clausole essenziali del contratto, modalità di scelta del contraente e ragioni. L'art. 17 del D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici, di seguito Codice) chiede la decisione di contrarre prima della procedura. Nell'affidamento diretto l'atto è unico e individua "l'oggetto, l'importo e il contraente, unitamente alle ragioni della sua scelta, ai requisiti di carattere generale e, se necessari, a quelli inerenti alla capacità economico-finanziaria e tecnico-professionale".[^2] Il Codice non ha abrogato l'art. 192. Si aggiungono gli elementi dell'impegno di spesa (art. 183 TUEL) e la motivazione, con "i presupposti di fatto e le ragioni giuridiche" della decisione (art. 3 della L. 7 agosto 1990, n. 241).

| Elemento | Norma | Dove nell'atto |
|---|---|---|
| Fine del contratto | art. 192 TUEL | motivazione |
| Oggetto, forma, clausole essenziali | art. 192 TUEL | motivazione e dispositivo |
| Modalità di scelta e ragioni | art. 192 TUEL | motivazione |
| Importo | art. 17, c. 2, Codice | dispositivo |
| Contraente e ragioni della scelta | art. 17, c. 2, Codice | motivazione e dispositivo |
| Requisiti generali e, se servono, speciali | art. 17, c. 2, Codice | motivazione |
| Somma, creditore, ragione, scadenza | art. 183 TUEL | dispositivo |

### La struttura

La determina ha otto parti: intestazione, con numero e data assegnati dal sistema documentale; oggetto; preambolo ("Visto"); motivazione ("Considerato"); dispositivo ("DETERMINA"); regolarità tecnica e firma digitale; visto contabile, se c'è spesa; attestazione della pubblicazione all'albo online. La forma di preambolo e motivazione è nel capitolo sulla lingua degli atti; qui conta il contenuto.

## Competenza e preambolo

### Chi firma

Ai dirigenti spettano, tra l'altro, la responsabilità delle procedure d'appalto, la stipulazione dei contratti e l'assunzione di impegni di spesa (art. 107, comma 3, TUEL). Nei Comuni senza dirigenti, come Borgo Esempio, il sindaco può attribuire queste funzioni ai responsabili degli uffici e dei servizi con provvedimento motivato (art. 109, comma 2).[^3] Il preambolo cita entrambi gli articoli e il decreto sindacale, con numero e data. Dal contratto collettivo del comparto Funzioni locali del 16 novembre 2022 l'incarico si chiama "di elevata qualificazione". "Titolare di posizione organizzativa" è una formula superata, che l'IA ripete perché ricorre in molti atti degli anni passati.[^4]

La competenza si controlla, non basta citarla: il decreto riguarda quel servizio ed è in vigore alla data dell'atto. Chi firma e il RUP si astengono se hanno un conflitto di interessi, anche potenziale, e lo segnalano.[^5]

### La programmazione

La spesa si fonda sul documento unico di programmazione (DUP), sul bilancio di previsione e sul piano esecutivo di gestione (PEG), che assegna le risorse ai responsabili. Il PEG è facoltativo solo sotto i 5.000 abitanti (art. 169, comma 3, TUEL): Borgo Esempio, che ne ha 6.500, deve adottarlo. Il programma triennale degli acquisti riguarda gli acquisti da 140.000 euro in su (art. 37, comma 3, Codice): per 1.200 euro non si cita.[^6]

### Un preambolo essenziale

Il preambolo dice su che cosa si fonda la decisione, non che cosa il responsabile ha letto. Nell'esperimento del capitolo sul metodo il prompt generico ha accumulato 14-15 atti normativi per 1.200 euro. Qui ne bastano tre, TUEL, Codice e L. 13 agosto 2010, n. 136, più gli atti dell'ente: decreto di nomina, delibera del bilancio, delibera del PEG.

Ogni "Visto" riferito a un atto dell'ente ha numero e data. È qui che l'IA inventa più volentieri: un numero di delibera plausibile non si distingue da uno vero. Li fornisci tu nel prompt; altrimenti il modello scrive [VERIFICARE].

## Il prompt per la determina a contrarre e di affidamento

### L'elenco delle norme

È l'elenco del capitolo sul metodo, completato. Ogni voce supera prima i tre controlli descritti nel capitolo sulla verifica delle norme.

```
NORME DA USARE (verificate su Normattiva il [data])
- D.Lgs. 18 agosto 2000, n. 267 (TUEL), artt. 107 e 109, c. 2: competenza.
- TUEL, art. 192: contenuto della determinazione a contrattare.
- TUEL, artt. 183 e 151, c. 4: impegno; esecutività con il visto.
- TUEL, art. 147-bis: regolarità tecnica e contabile.
- D.Lgs. 31 marzo 2023, n. 36, art. 17, c. 1 e 2: decisione di contrarre.
- D.Lgs. 36/2023, art. 50, c. 1, lett. b): affidamento diretto.
- D.Lgs. 36/2023, art. 49, c. 6: deroga alla rotazione sotto 5.000 euro.
- D.Lgs. 36/2023, artt. 15 e 16: nomina del RUP; conflitto di interessi.
- D.Lgs. 36/2023, artt. 25 e 26: piattaforme; art. 52: verifiche.
- D.Lgs. 36/2023, art. 18, c. 1: stipula; art. 53, c. 4: garanzia.
- L. 13 agosto 2010, n. 136, art. 3: tracciabilità dei flussi finanziari.
```

Gli articoli 15, 16 e 18 del Codice non erano nell'elenco dell'esperimento: servono perché la determina nomina il RUP, ne riporta la dichiarazione sul conflitto di interessi e decide la forma del contratto.

### Il prompt

È il prompt modello del capitolo sul metodo, compilato per la determina. Le righe che cambiano davvero sono due, Compito e Fatti; la riga Stile è riassunta in Formato.

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

La riga Compito elenca gli elementi dell'art. 192. Il prompt restituisce solo ciò che chiedi: nell'esperimento, fine, forma e clausole essenziali li aveva trattati il testo generico, non quello strutturato. La riga Fatti nomina la regolarità tecnica, perché nell'esperimento tutte le bozze strutturate la attestavano già, prima di ogni controllo.

Cambia anche la regola 8 del file di stile. "Un'azione per punto" ha prodotto, nell'esperimento, dispositivi di 16-19 punti. Per le determine scrivi: "Dispositivo: un punto per decisione; non ripetere gli obblighi di legge". Con un dispositivo compatto basta chiedere circa 500 parole.

### La bozza commentata

Ecco la bozza dopo il primo giro: l'istruttore ha fornito i dati mancanti e ha riletto il testo. Restano i [VERIFICARE] che si chiudono prima della firma. Numeri e date degli atti sono inventati.

```
COMUNE DI BORGO ESEMPIO – SERVIZIO AFFARI GENERALI
Determinazione n. [numero] del [data]
OGGETTO: Abbonamento 2027 a una banca dati giuridica on line. Decisione
di contrarre e affidamento diretto a Editrice Esempio S.r.l. Impegno di
spesa di euro 1.464,00. CIG [VERIFICARE: CIG della trattativa diretta].

IL RESPONSABILE DEL SERVIZIO AFFARI GENERALI
Visti:
- gli artt. 107, 109, comma 2, 147-bis, 151, comma 4, 183 e 192 del
  D.Lgs. 18 agosto 2000, n. 267 (TUEL);
- gli artt. 15, 16, 17, 18, 25, 26, 49, 50, 52 e 53 del D.Lgs. 31 marzo
  2023, n. 36 (Codice);
- l'art. 3 della L. 13 agosto 2010, n. 136;
- il decreto del Sindaco n. 3 del 2 gennaio 2026, di conferimento
  dell'incarico di elevata qualificazione per il Servizio;
- la deliberazione del Consiglio comunale n. 48 del 19 dicembre 2025,
  di approvazione del bilancio di previsione 2026-2028;
- la deliberazione della Giunta comunale n. 4 del 13 gennaio 2026, di
  approvazione del piano esecutivo di gestione (PEG) 2026-2028;
Considerato che:
- l'abbonamento in corso, affidato con ATTO_1, scade il 31 dicembre 2026
  e non prevede opzioni di rinnovo;
- il fine del contratto è assicurare agli uffici, nel 2027, una fonte
  aggiornata di norme e giurisprudenza per l'istruttoria degli atti;
- l'oggetto è l'abbonamento dal 1° gennaio al 31 dicembre 2027 per
  [VERIFICARE: numero di accessi previsto dall'offerta];
- le clausole essenziali sono durata, prezzo, pagamento a 30 giorni dalla
  fattura elettronica e obblighi di tracciabilità;
- l'importo, euro 1.200,00 oltre IVA, consente l'affidamento diretto
  (art. 50, comma 1, lett. b), Codice);
- Editrice Esempio S.r.l. ha presentato l'offerta nella trattativa
  diretta sul Mercato elettronico della pubblica amministrazione (MePA),
  al prezzo del 2026 [VERIFICARE: confronto con listino o prodotti simili];
- il MePA è uno strumento di Consip; convenzioni o accordi quadro per
  servizi comparabili: [VERIFICARE: esito della consultazione];
- l'operatore ha eseguito per il Comune i contratti 2024-2026 [VERIFICARE:
  esito attestato dal RUP]; la stessa banca dati evita di riorganizzare
  archivi e ricerche degli uffici;
- sotto euro 5.000,00 è consentito derogare alla rotazione (art. 49,
  comma 6, Codice);
- l'operatore ha dichiarato il possesso dei requisiti generali; la
  dichiarazione si verifica con le modalità dell'art. 52 del Codice;
- dato l'importo, non si richiede la garanzia definitiva (art. 53,
  comma 4, Codice);
- RUP_1 ha dichiarato l'assenza di conflitti di interessi;
DETERMINA
1. di affidare a Editrice Esempio S.r.l. l'abbonamento per il 2027 alla
   banca dati, per euro 1.200,00 oltre IVA al 22%;
2. di stipulare il contratto sul MePA, con la clausola sugli obblighi
   dell'art. 3 della L. 136/2010;
3. di impegnare euro 1.464,00 a favore di Editrice Esempio S.r.l. sul
   capitolo 1043, esercizio 2027, in cui l'obbligazione è esigibile;
4. di nominare RUP_1 responsabile unico del progetto (RUP);
5. di trasmettere l'atto al servizio finanziario per il visto di
   regolarità contabile, dal quale dipende l'esecutività;
6. di pubblicare l'atto all'albo online e in "Amministrazione
   trasparente".
Regolarità tecnica (art. 147-bis TUEL): [VERIFICARE: da attestare con
la firma, dopo i controlli].
IL RESPONSABILE DEL SERVIZIO AFFARI GENERALI (firmato digitalmente)
```

*Oggetto.* Dice cosa, a chi, quanto e con quale CIG. L'importo contrattuale è al netto dell'IVA; l'impegno la comprende. Le soglie del Codice, 140.000 euro per l'affidamento diretto e 5.000 per la deroga alla rotazione, si calcolano al netto.[^7] Il CIG è quello della trattativa sulla piattaforma: una bozza dell'esperimento chiedeva di acquisirlo "prima dell'affidamento" nello stesso atto che affidava.

*Preambolo.* Numeri e date vengono dal prompt, non dal modello. C'è l'art. 109, comma 2: senza, l'art. 107 attribuisce le funzioni ai dirigenti, che Borgo Esempio non ha.

*Fine, forma e clausole.* Il fine non è "rinnovare l'abbonamento": è ciò che il contratto serve a ottenere. Le clausole essenziali sono quelle che il Comune potrà far valere.

*Ragioni della scelta.* Sono tre: l'importo, la continuità d'uso, la deroga alla rotazione. L'art. 50 chiede operatori con "documentate esperienze pregresse idonee": tre anni di contratti con il Comune lo sono, se l'esito è documentato. Il modello non può sapere com'è andata, e nell'esperimento il testo generico lo affermava in tutte e tre le esecuzioni: per questo resta il [VERIFICARE].[^8]

*Prezzo e Consip.* "Al prezzo del 2026" non dimostra che il prezzo è congruo: aggiungi un confronto con il listino o con un prodotto simile. Se una convenzione Consip copre servizi comparabili, i suoi parametri di prezzo e qualità sono il limite massimo. Se poi la banca dati on line si considera un servizio informatico, l'acquisto deve passare dagli strumenti di Consip o dei soggetti aggregatori, anche sotto i 5.000 euro. Se nessuna convenzione o accordo quadro copre il servizio, la trattativa diretta sul MePA, che è uno strumento di Consip, rispetta la regola. Scrivilo nell'atto; nel dubbio sulla natura del servizio, decidi con il servizio finanziario (si veda anche il capitolo sulla scelta e l'acquisto di uno strumento di IA).[^9]

*Requisiti e garanzia.* "Ha dichiarato" e "si verifica": la bozza distingue ciò che è avvenuto da ciò che resta da fare. La rinuncia alla garanzia definitiva è motivata con l'importo (art. 53, comma 4).[^10]

*Regolarità tecnica.* La attesta chi firma, dopo i controlli: il modello lascia la formula aperta. L'esecutività, poi, dipende dal visto contabile.

## Rotazione, piattaforma digitale, CIG, verifiche e tracciabilità

### La rotazione

Il principio di rotazione vieta di affidare una nuova commessa al contraente uscente quando i due affidamenti consecutivi riguardano lo stesso settore merceologico, la stessa categoria di opere o lo stesso settore di servizi (art. 49, comma 2, Codice). Si può derogare in casi motivati con riferimento alla struttura del mercato e all'effettiva assenza di alternative, nonché all'accurata esecuzione del precedente contratto (comma 4). Negli affidamenti diretti sotto i 5.000 euro la deroga è comunque consentita (comma 6).[^11]

Nel caso guida basta il comma 6, con una riga di motivazione. Il comma 4 serve sopra i 5.000 euro, e la sola buona esecuzione non basta: una bozza generica dell'esperimento lo invocava citando solo quella.

### La piattaforma e il CIG

Dal 1° gennaio 2024 ogni affidamento, anche diretto e di pochi euro, si svolge su una piattaforma di approvvigionamento digitale certificata, collegata alla Banca dati nazionale dei contratti pubblici dell'Autorità nazionale anticorruzione (ANAC). Il CIG si acquisisce tramite la piattaforma; lo SmartCIG non esiste più.

Gli obblighi sono due, e diversi. Il MePA, o un altro mercato elettronico, è obbligatorio per beni e servizi da 5.000 euro fino alla soglia europea (art. 1, comma 450, della L. 27 dicembre 2006, n. 296). La piattaforma certificata serve sempre. Sotto i 5.000 euro l'ANAC ammette anche l'interfaccia web della propria Piattaforma dei contratti pubblici, con un comunicato del giugno 2025 che non fissa una nuova scadenza: controlla che valga alla data dell'atto.[^12]

Borgo Esempio usa il MePA. L'atto non lo dice obbligatorio in base al comma 450: sotto i 5.000 euro non lo è. Un obbligo può venire solo dall'art. 1, comma 512, della L. 28 dicembre 2015, n. 208, se la banca dati si considera un servizio informatico, come si è visto a proposito del prezzo.

### Le verifiche

Negli affidamenti diretti sotto i 40.000 euro l'operatore attesta i requisiti con una dichiarazione sostitutiva, che la stazione appaltante verifica, anche a campione, con un sorteggio dalle modalità fissate ogni anno. Se i requisiti non sono confermati, il Comune risolve il contratto, escute l'eventuale garanzia definitiva, informa l'ANAC e sospende l'operatore, da uno a dodici mesi, dalle proprie procedure di affidamento (art. 52, comma 2). I requisiti generali sono quelli degli artt. 94-98, non più dell'art. 80 del vecchio Codice.[^13] La regolarità contributiva (DURC) si controlla anche prima di ogni pagamento.[^14]

La determina non anticipa gli esiti: li riporta, con gli estremi del documento, solo se ci sono; altrimenti dice come si verifica.

### Stipula e tracciabilità

Nell'affidamento diretto il contratto si può stipulare per corrispondenza secondo l'uso commerciale, cioè con uno scambio di lettere, anche via posta elettronica certificata (art. 18, comma 1). Sul MePA lo scambio avviene con il documento di stipula generato dalla piattaforma. Sotto soglia non si applica il termine dilatorio di 32 giorni; sotto i 40.000 euro non si paga l'imposta di bollo.[^15]

Per la tracciabilità l'operatore usa un conto dedicato e ne comunica gli estremi entro sette giorni; ogni pagamento riporta il CIG; il contratto contiene la clausola di tracciabilità, a pena di nullità assoluta (art. 3 della L. 136/2010). Anche la fattura elettronica riporta il CIG: senza, il Comune non può pagarla.[^16]

## Impegno di spesa, visto contabile e controlli

### L'impegno

L'impegno è la prima fase della spesa: a seguito di un'obbligazione giuridicamente perfezionata si determinano somma, creditore, ragione e scadenza, e si vincola lo stanziamento (art. 183, comma 1, TUEL). La spesa si imputa all'esercizio in cui l'obbligazione è esigibile:[^17] l'abbonamento 2027 va sul 2027, anche se la determina si firma a dicembre 2026. Chi impegna verifica anche la compatibilità dei pagamenti con la cassa (comma 8).

Capitolo, disponibilità ed esercizio si chiedono al servizio finanziario, non al modello. I conti li fai tu: 1.200 euro più il 22% fa 1.464 euro. L'aliquota la indica l'offerta e la conferma il servizio finanziario: alcune pubblicazioni elettroniche hanno un'aliquota ridotta, e il modello tende a dare per scontato il 22%.

### Il visto e l'esecutività

Le determine che comportano impegni diventano esecutive con il visto di regolarità contabile del responsabile del servizio finanziario, che attesta la copertura (art. 151, comma 4, e art. 183, comma 7, TUEL). Solo dopo il responsabile ordina la prestazione e, nello stesso momento, comunica al fornitore le informazioni sull'impegno (art. 191, comma 1). L'"immediata eseguibilità" appartiene alle deliberazioni di Giunta e Consiglio (art. 134, comma 4): se compare in una bozza di determina, va tolta.[^18]

### I controlli

L'art. 147-bis del TUEL prevede due momenti. Prima dell'atto, il responsabile del servizio attesta la regolarità tecnica e la correttezza dell'azione amministrativa; il servizio finanziario rende il parere di regolarità contabile e il visto. Dopo l'atto, sotto la direzione del segretario, si controllano a campione determine di impegno, contratti e altri atti.[^19] Il controllo parte dal testo: la motivazione deve reggersi da sola, senza spiegazioni a voce. L'art. 49 del TUEL, citato spesso nelle determine, riguarda invece i pareri sulle proposte di deliberazione.

Dopo il visto la determina va all'albo online, e i dati dell'affidamento in "Amministrazione trasparente", attraverso la Banca dati nazionale dei contratti pubblici.[^20] Prima, fai il controllo descritto nel capitolo sulla privacy prima della pubblicazione.

## Gli errori più frequenti dell'IA nelle determine

Gli errori della tabella vengono dall'esperimento del capitolo sul metodo e dai riferimenti sbagliati o superati più frequenti nei modelli di atto, molti dei quali descritti nel capitolo sulla verifica delle norme. In ogni caso il testo resta credibile.

| Errore | Esempio | Come intercettarlo |
|---|---|---|
| Codice abrogato | artt. 32 e 36 D.Lgs. 50/2016 | elenco delle norme |
| Formule superate | posizione organizzativa; RUP "del procedimento" | file di stile |
| Articolo giusto, contenuto altro | art. 52, c. 2, Codice; art. 49 TUEL | lettura dell'articolo |
| Controlli dati per fatti | "DURC regolare", "nessuna convenzione" | riga Fatti |
| Attestazioni anticipate | regolarità tecnica, visto favorevole | formula alla firma |
| Procedure superate | SmartCIG; termine dilatorio di 35 giorni | elenco delle norme |
| Esecutività sbagliata | "immediatamente eseguibile" | art. 151, c. 4, TUEL |
| Importi incoerenti | impegno senza IVA; soglie con l'IVA | ricalcolo a mano |

I più insidiosi sono il terzo e il quarto: un articolo che esiste supera il controllo di esistenza, e un controllo dato per fatto non ha neppure un riferimento da verificare. Per il controllo apri una conversazione nuova, con la bozza come unico testo: il modello non è condizionato dalle istruzioni e dalle risposte precedenti (si veda il capitolo sul flusso di lavoro). Il testo contiene RUP_1: anche il controllo passa dallo strumento dell'ente.

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

La tabella dice da dove cominciare; gli importi li confronti tu con offerta e impegno.

## Prima della firma

Alla checklist del metodo aggiungi, per la determina a contrarre:

1. decreto di nomina valido per il servizio; spesa nelle risorse assegnate dal PEG;
2. nessun conflitto di interessi tuo o del RUP, con le dichiarazioni nel fascicolo;
3. tutti gli elementi dell'art. 192 TUEL e dell'art. 17, comma 2, del Codice;
4. importo netto, IVA e impegno coerenti; soglie calcolate al netto;
5. rotazione rispettata, o deroga motivata; prezzo confrontato; convenzioni e accordi quadro Consip consultati;
6. CIG nell'oggetto, uguale a quello della procedura sulla piattaforma;
7. verifiche descritte come da fare, o con esito ed estremi del documento;
8. capitolo, esercizio e disponibilità confermati dal servizio finanziario;
9. nessun riferimento al D.Lgs. 50/2016 né formula superata; ogni norma controllata;
10. nessuna parentesi quadra né segnaposto; nome del RUP reinserito a mano; uso dell'IA annotato nel fascicolo.

## Altre determine ricorrenti: liquidazione, accertamento, nomine

Lo schema non cambia: elenco delle norme dell'atto, prompt in cinque parti, bozza, controllo. Nel prompt cambiano le righe Compito, Dati e Fatti.

### La liquidazione

La liquidazione determina, sui documenti che provano il diritto del creditore, la somma certa e liquida da pagare, nei limiti dell'impegno, dopo il riscontro della regolarità della prestazione. L'atto va al servizio finanziario per i controlli (art. 184 TUEL).[^21] Servono il DURC, la fattura elettronica con il CIG, il conto dedicato e, sopra i 5.000 euro, la verifica presso l'agente della riscossione. L'IVA si versa all'Erario con la scissione dei pagamenti, prorogata fino al 30 giugno 2029. Il termine di pagamento è di regola di 30 giorni.[^22]

```
Compito: bozza della determina di liquidazione della fattura [n. e data].
Dati: determina e impegno [n.], capitolo, CIG, imponibile, IVA, scadenza.
Regolare esecuzione: [chi l'ha attestata e quando, oppure "da attestare"].
Fatti: DURC, conto dedicato e CIG in fattura solo se indicati qui sopra,
con data o protocollo del documento; altrimenti [VERIFICARE: controllo].
Non scrivere IBAN né codici fiscali. Importi: riportali, non ricalcolarli.
```

Gli estremi del conto non servono alla bozza: basta dire che la comunicazione c'è, con la sua data. Se il fornitore è una ditta individuale, il conto e i suoi delegati sono dati personali e il testo diventa giallo.

```
COMUNE DI BORGO ESEMPIO – SERVIZIO AFFARI GENERALI
OGGETTO: Liquidazione a Editrice Esempio S.r.l. della fattura n. 15 del
12 gennaio 2027. Abbonamento 2027 alla banca dati giuridica on line.

IL RESPONSABILE DEL SERVIZIO AFFARI GENERALI
Visti gli artt. 107, 109, comma 2, e 184 del D.Lgs. 18 agosto 2000,
n. 267 (TUEL) e l'art. 3 della L. 13 agosto 2010, n. 136;
Vista la determinazione n. 412 del 9 dicembre 2026, di affidamento e di
impegno della spesa (impegno n. 58/2027, capitolo 1043);
Considerato che:
- la fattura elettronica n. 15 del 12 gennaio 2027 riporta il CIG
  dell'affidamento, euro 1.200,00 di imponibile ed euro 264,00 di IVA;
- RUP_1 ha attestato il 20 gennaio 2027 l'attivazione dell'abbonamento,
  conforme all'offerta;
- il documento unico di regolarità contributiva (DURC) [VERIFICARE:
  esito, protocollo e scadenza];
- l'operatore ha comunicato il 5 gennaio 2027 gli estremi del conto
  corrente dedicato;
DETERMINA
1. di liquidare a Editrice Esempio S.r.l. euro 1.200,00 sul conto
   dedicato, entro la scadenza della fattura;
2. di versare all'Erario l'IVA di euro 264,00 con la scissione dei
   pagamenti (art. 17-ter del D.P.R. 26 ottobre 1972, n. 633);
3. di imputare la spesa di euro 1.464,00 all'impegno n. 58/2027;
4. di trasmettere l'atto al servizio finanziario per i controlli e il
   mandato di pagamento (art. 184, comma 3, TUEL).
IL RESPONSABILE DEL SERVIZIO AFFARI GENERALI (firmato digitalmente)
```

Il punto critico è il DURC: il modello non l'ha visto, e la bozza ne lascia aperto l'esito. La regolare esecuzione è riportata da chi l'ha attestata. Per un abbonamento annuale, a gennaio si può attestare solo l'attivazione conforme all'offerta: che il pagamento avvenga a inizio anno lo deve prevedere il contratto, non la bozza. Gli importi vengono dalla fattura e si sommano a mano. Errori tipici: liquidare su un impegno diverso o incapiente; dare il DURC per regolare; pagare al fornitore anche l'IVA; confondere la liquidazione con l'ordinazione e il pagamento, fasi successive curate dal servizio finanziario.

Prima della firma: fattura con CIG e importi coerenti con l'impegno; regolare esecuzione, o attivazione, attestata con data; DURC, conto dedicato e, sopra i 5.000 euro, verifica presso l'agente della riscossione nel fascicolo; termine di pagamento rispettato.

### L'accertamento di entrata

L'accertamento è la prima fase dell'entrata: sulla base di idonea documentazione si verificano ragione del credito e titolo giuridico, si individuano debitore e somma, si fissa la scadenza. La documentazione va al servizio finanziario (art. 179, commi 1 e 3, TUEL). L'entrata si imputa all'esercizio in cui il credito è esigibile.[^23] Se l'accertamento richieda una determina lo dice il regolamento di contabilità.

Il caso: la Regione ha concesso a Borgo Esempio 25.000 euro per la copertura della scuola primaria. Nel prompt la riga Dati indica atto di concessione, debitore, capitolo di entrata e tempi di erogazione; la riga Fatti aggiunge: "senza atto di concessione non si accerta". Non ci sono persone: il testo è verde. Decreto e capitolo della bozza sono inventati.

```
COMUNE DI BORGO ESEMPIO – SERVIZIO TECNICO
OGGETTO: Accertamento del contributo regionale di euro 25.000,00 per la
manutenzione straordinaria della copertura della scuola primaria.
IL RESPONSABILE DEL SERVIZIO TECNICO
Visti gli artt. 107, 109, comma 2, e 179 del D.Lgs. 18 agosto 2000,
n. 267 (TUEL) e l'allegato 4/2 al D.Lgs. 23 giugno 2011, n. 118;
Visto il decreto della Regione n. 1187 del 15 settembre 2026, titolo del
credito, che concede il contributo e ne disciplina l'erogazione;
DETERMINA
1. di accertare euro 25.000,00 a carico della Regione sul capitolo di
   entrata 2150, esercizio [VERIFICARE: esercizio di esigibilità secondo
   i tempi di erogazione del decreto];
2. di trasmettere l'atto e il decreto al servizio finanziario.
IL RESPONSABILE DEL SERVIZIO TECNICO (firmato digitalmente)
```

L'errore più serio è accertare su una domanda: finché l'ente che finanzia non concede, non c'è credito. Il secondo è l'esercizio, che dipende dall'esigibilità, spesso legata dal decreto all'avanzamento dei lavori o alla rendicontazione. Il terzo è confondere accertamento e incasso. Prima della firma: atto di concessione con numero e data; importo e condizioni coincidenti; esercizio concordato con il servizio finanziario.

### La nomina del RUP

Nel primo atto di avvio dell'intervento la stazione appaltante nomina il responsabile unico del progetto per programmazione, progettazione, affidamento ed esecuzione. Lo sceglie tra i dipendenti, preferibilmente dell'unità organizzativa titolare del potere di spesa, con i requisiti dell'allegato I.2. Se la nomina manca, l'incarico spetta al responsabile dell'unità organizzativa competente.[^24] Nel caso guida la nomina è un punto del dispositivo; per la copertura della scuola si fa con un atto a sé. Nel prompt il dipendente è RUP_1; il nome si reinserisce a mano. Il testo riguarda una persona ed è giallo: solo lo strumento dell'ente. Titolo di studio, esperienze e dichiarazioni di RUP_1 restano nel fascicolo.

```
COMUNE DI BORGO ESEMPIO – SERVIZIO TECNICO
OGGETTO: Manutenzione straordinaria della copertura della scuola
primaria. Nomina del responsabile unico del progetto (RUP).
IL RESPONSABILE DEL SERVIZIO TECNICO
Visti gli artt. 107 e 109, comma 2, del D.Lgs. 18 agosto 2000, n. 267
(TUEL) e gli artt. 15 e 16 e l'allegato I.2 del D.Lgs. 31 marzo 2023,
n. 36 (Codice);
Considerato che RUP_1, dipendente del Servizio tecnico, ha i requisiti
dell'allegato I.2 [VERIFICARE: titolo ed esperienza per questo importo]
e ha dichiarato l'assenza di conflitti di interessi (art. 16);
DETERMINA
1. di nominare RUP_1 responsabile unico del progetto per le fasi di
   programmazione, progettazione, affidamento ed esecuzione;
2. di comunicare la nomina a RUP_1.
IL RESPONSABILE DEL SERVIZIO TECNICO (firmato digitalmente)
```

Il punto critico sono i requisiti: non chiederli al modello, leggili nell'allegato I.2, perché variano con il tipo e l'importo dell'intervento. Gli errori tipici vengono dal vecchio Codice: "responsabile unico del procedimento", l'art. 31 del D.Lgs. 50/2016, le Linee guida ANAC n. 3. Prima della firma: nomina nel primo atto dell'intervento; requisiti documentati; dichiarazione sul conflitto di interessi nel fascicolo; il nome al posto del segnaposto.

## In sintesi

- Una determina con una società come fornitore e senza persone è verde; con RUP_1 o una ditta individuale è gialla, e passa solo dallo strumento dell'ente.
- Gli elementi dell'art. 192 TUEL e dell'art. 17, comma 2, del Codice vanno nella riga Compito del prompt.
- Numero e data degli atti dell'ente, capitolo ed esercizio li fornisci tu; i conti li fai tu.
- Le soglie si calcolano al netto dell'IVA; l'impegno la comprende.
- Piattaforma certificata sempre, MePA da 5.000 euro, CIG dalla piattaforma; prezzo confrontato e strumenti Consip controllati anche per piccoli importi.
- Verifiche, DURC, visti e regolarità tecnica: da fare, o con l'esito documentato.
- La determina con impegno è esecutiva con il visto contabile; solo dopo si ordina la prestazione.
- Liquidazione, accertamento e nomina: stesso schema, controllo in una conversazione nuova.

[^1]: Il divieto di rinnovo tacito dei contratti pubblici è affermato da tempo dalla giurisprudenza amministrativa. Un'opzione di rinnovo prevista in clausole chiare, precise e inequivocabili dei documenti iniziali, e computata nel valore stimato dell'appalto, si esercita senza una nuova procedura: D.Lgs. 31 marzo 2023, n. 36, *Codice dei contratti pubblici*, art. 120, comma 1, lett. a), e art. 14, comma 4, normattiva.it. Se ne parla anche nel capitolo sul metodo del prompt.

[^2]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, art. 192, comma 1; D.Lgs. 31 marzo 2023, n. 36, cit., art. 17, commi 1 e 2; L. 7 agosto 1990, n. 241, art. 3, comma 1, sulla motivazione, normattiva.it. Il Codice è efficace dal 1° luglio 2023 (art. 229) ed è stato modificato, tra l'altro, dal D.Lgs. 31 dicembre 2024, n. 209: si usa il testo vigente alla data dell'atto.

[^3]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 107, comma 3, lett. b), c) e d), e art. 109, comma 2, normattiva.it. L'art. 109, comma 2, fa salva l'applicazione dell'art. 97, comma 4, lett. d), sulle funzioni che il sindaco può conferire al segretario comunale.

[^4]: ARAN, *Contratto collettivo nazionale di lavoro relativo al personale del comparto Funzioni locali, triennio 2019-2021*, sottoscritto il 16 novembre 2022, aranagenzia.it, che ha sostituito le posizioni organizzative con gli incarichi di elevata qualificazione.

[^5]: L. 7 agosto 1990, n. 241, cit., art. 6-bis; D.Lgs. 31 marzo 2023, n. 36, cit., art. 16; D.P.R. 16 aprile 2013, n. 62, *Codice di comportamento dei dipendenti pubblici*, artt. 6 e 7, normattiva.it.

[^6]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 169, comma 3, sul PEG, e art. 170, sul DUP; D.Lgs. 31 marzo 2023, n. 36, cit., art. 37, comma 3, che rinvia alla soglia dell'art. 50, comma 1, lett. b), normattiva.it.

[^7]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 14, comma 4, per il quale il valore stimato si calcola sull'importo totale pagabile al netto dell'IVA, comprese le opzioni e i rinnovi esplicitamente stabiliti, normattiva.it.

[^8]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 50, comma 1, lett. b), che consente l'affidamento diretto di servizi e forniture sotto i 140.000 euro "anche senza consultazione di più operatori economici", assicurando che siano scelti soggetti "in possesso di documentate esperienze pregresse idonee all'esecuzione delle prestazioni contrattuali", normattiva.it. Nell'esperimento del capitolo sul metodo una delle bozze strutturate tralasciava questo requisito.

[^9]: L. 23 dicembre 1999, n. 488, art. 26, comma 3, sull'adesione alle convenzioni Consip o sull'uso dei loro parametri di prezzo e qualità come limiti massimi; L. 28 dicembre 2015, n. 208, art. 1, comma 512, sugli acquisti di beni e servizi informatici e di connettività tramite gli strumenti di acquisto e di negoziazione di Consip o dei soggetti aggregatori, per i beni e i servizi disponibili presso di loro, senza una soglia minima di importo, normattiva.it. Se una banca dati on line sia un servizio informatico ai fini del comma 512 dipende dalle sue caratteristiche: la norma non lo dice.

[^10]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 53, comma 4, che negli affidamenti sotto soglia consente, in casi motivati, di non richiedere la garanzia definitiva, normattiva.it.

[^11]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 49, commi 2, 4 e 6, normattiva.it. Condizioni e soglie si leggono nel testo vigente alla data dell'atto.

[^12]: D.Lgs. 31 marzo 2023, n. 36, cit., artt. 23, 25 e 26, e art. 225 sulla decorrenza della digitalizzazione dal 1° gennaio 2024; L. 27 dicembre 2006, n. 296, art. 1, comma 450, normattiva.it; ANAC, *Comunicato del Presidente del 18 giugno 2025*, anticorruzione.it, che consente di continuare a usare, senza fissare una nuova scadenza, l'interfaccia web della Piattaforma dei contratti pubblici per gli affidamenti diretti di importo inferiore a 5.000 euro. Sintesi in lavoripubblici.it, 2025. Le indicazioni dell'ANAC sulla digitalizzazione cambiano spesso: controlla sul sito dell'Autorità quelle in vigore alla data dell'atto.

[^13]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 24, sul fascicolo virtuale dell'operatore economico, da cui passano di regola le verifiche, art. 52, commi 1 e 2, e artt. 94-98, normattiva.it. L'art. 80 del D.Lgs. 18 aprile 2016, n. 50, è abrogato con il resto di quel Codice dal 1° luglio 2023 (art. 226 del D.Lgs. 36/2023).

[^14]: D.L. 20 marzo 2014, n. 34, convertito dalla L. 16 maggio 2014, n. 78, art. 4, sul DURC on line, e decreto del Ministro del lavoro e delle politiche sociali 30 gennaio 2015, sulla validità di 120 giorni; D.Lgs. 31 marzo 2023, n. 36, cit., art. 11, comma 6, sull'intervento sostitutivo in caso di inadempienze contributive, normattiva.it.

[^15]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 18, commi 1, 3, lett. d), e 10, art. 55, comma 2, e allegato I.4, che esenta dall'imposta di bollo i contratti di importo inferiore a 40.000 euro, normattiva.it.

[^16]: L. 13 agosto 2010, n. 136, art. 3, commi 1, 5, 7 e 8; D.L. 24 aprile 2014, n. 66, convertito dalla L. 23 giugno 2014, n. 89, art. 25, sull'indicazione del CIG nelle fatture elettroniche, normattiva.it. Il termine di sette giorni decorre dall'accensione del conto o, per un conto già esistente, dal suo primo utilizzo per la commessa.

[^17]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 183, commi 1 e 8; D.Lgs. 23 giugno 2011, n. 118, allegato 4/2, *Principio contabile applicato concernente la contabilità finanziaria*, normattiva.it e rgs.mef.gov.it.

[^18]: D.Lgs. 18 agosto 2000, n. 267, cit., artt. 151, comma 4, 183, comma 7, 191, comma 1, e 134, comma 4, normattiva.it.

[^19]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 147-bis, commi 1 e 2, inserito dal D.L. 10 ottobre 2012, n. 174, convertito dalla L. 7 dicembre 2012, n. 213; art. 49, comma 1, sui pareri sulle proposte di deliberazione, normattiva.it.

[^20]: L. 18 giugno 2009, n. 69, art. 32, sull'albo online; D.Lgs. 14 marzo 2013, n. 33, art. 37, e D.Lgs. 31 marzo 2023, n. 36, cit., art. 28, sulla trasparenza dei contratti pubblici, normattiva.it. Tempi e modalità di pubblicazione delle determine dipendono anche dallo statuto e dai regolamenti dell'ente.

[^21]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 184, commi da 1 a 4, e art. 185, sull'ordinazione e il pagamento, normattiva.it.

[^22]: D.P.R. 29 settembre 1973, n. 602, art. 48-bis, sulla verifica degli inadempimenti prima dei pagamenti superiori a 5.000 euro; D.P.R. 26 ottobre 1972, n. 633, art. 17-ter, sulla scissione dei pagamenti; D.Lgs. 9 ottobre 2002, n. 231, art. 4, sui termini di pagamento, normattiva.it. La scissione dei pagamenti è una deroga alla disciplina europea dell'IVA e vale solo finché il Consiglio dell'Unione europea la autorizza. L'autorizzazione precedente scadeva il 30 giugno 2026; la proroga fino al 30 giugno 2029 è stata autorizzata nel luglio 2026 con una decisione di esecuzione del Consiglio, secondo ANCE, *Split payment, via libera definitivo della Ue alla proroga fino al 2029*, 2026, ance.it, e ItaliaOggi, 2026, italiaoggi.it. Gli estremi della decisione vanno letti nella Gazzetta ufficiale dell'Unione europea, eur-lex.europa.eu.

[^23]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 179, commi 1 e 3; D.Lgs. 23 giugno 2011, n. 118, allegato 4/2, cit., normattiva.it.

[^24]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 15, commi 1, 2 e 4, art. 16 e allegato I.2, normattiva.it. Il comma 4 consente anche di nominare un responsabile di procedimento per singole fasi. Le Linee guida ANAC n. 3, sul responsabile unico del procedimento, erano attuative del D.Lgs. 50/2016.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 34 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- PEG presentato come scelta facoltativa di Borgo Esempio ("lo adotta"), mentre con 6.500 abitanti è obbligatorio: l'art. 169, comma 3, TUEL lo rende facoltativo solo sotto i 5.000 abitanti.
- Il dispositivo della bozza diceva "di dare atto che il RUP è RUP_1", ma il testo dice che nel caso guida la nomina è un punto del dispositivo.
- L'elenco delle norme del prompt non comprendeva gli artt. 15, 16 e 18 del Codice, eppure la bozza nominava il RUP, riportava la dichiarazione sul conflitto di interessi e decideva la stipula.
- Art. 52, comma 2, del Codice parafrasato in modo incompleto: mancava che la sospensione da uno a dodici mesi vale solo per le procedure della stessa stazione appaltante, e la garanzia escussa è quella definitiva.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
