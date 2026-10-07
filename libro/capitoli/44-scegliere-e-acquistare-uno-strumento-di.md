# Scegliere e acquistare uno strumento di IA

In questo capitolo: dal fabbisogno al contratto, con la valutazione comparativa, i requisiti su dati e sicurezza, i modi di affidamento, la prova pilota e l'uscita dal fornitore; per ogni passaggio, un modello pronto.

## Il fabbisogno: partire dai processi, non dal prodotto

### La domanda viene prima dell'offerta

Di solito la scelta comincia da un'offerta: il modulo di IA del gestionale degli atti, l'assistente della suite d'ufficio proposto dal rivenditore, il chatbot di cui parla un collega. Ogni proposta risponde a una domanda che il Comune non ha ancora fatto.

L'ordine giusto è l'inverso: prima i processi, poi i requisiti, alla fine i prodotti. L'art. 14 della L. 23 settembre 2025, n. 132, dice a che cosa serve l'IA nella pubblica amministrazione: efficienza, procedimenti più brevi, servizi migliori, assicurando "la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo".[^1] Con gli stessi criteri, dopo, si giudica se l'acquisto è servito.

### La scheda del fabbisogno

Il fabbisogno si scrive. A Borgo Esempio lo scrive il responsabile del Servizio Affari generali, che è anche responsabile per la transizione al digitale (RTD), con gli altri responsabili di servizio. Parte dalla ricognizione anonima fatta per il regolamento interno e, se c'è, dal registro del metodo (si vedano i capitoli sul regolamento interno e sul flusso di lavoro).

```
SCHEDA DEL FABBISOGNO – strumento di IA generativa
Comune di [nome] – a cura di [RTD] – versione del [data]
1. Processi: [tipi di atto o attività; servizio; numero annuo]
2. Fase: [istruttoria / bozza / revisione / sintesi]
3. Utenti: [numero, servizi]; utenti della prova: [numero]
4. Dati: verdi [sì/no]; gialli con segnaposto [sì/no]; rossi esclusi
5. Funzioni necessarie: [istruzioni persistenti; documenti di
   riferimento; caricamento di file; esportazione]
6. Funzioni da disattivare: [memoria; ricerca web; connettori]
7. Strumenti già disponibili nell'ente: [licenze in uso, piani inclusi]
8. Vincoli: [budget annuo; durata; competenze interne]
9. Risultati attesi: [rinvio agli indicatori del PIAO]
10. Usi esclusi: [decisioni su persone; graduatorie; valutazioni]
Sentiti: [responsabili dei servizi; DPO; segretario comunale]
```

Tre righe decidono quasi tutto. La riga Dati dice se bastano i dati verdi, per i quali va bene ogni strumento ammesso per iscritto dall'ente, o servono i gialli, che entrano solo nello strumento dell'ente con il contratto dell'art. 28 del GDPR (si veda il capitolo su quale IA usare in ufficio). I rossi restano fuori in ogni caso. La riga Funzioni necessarie separa ciò che serve da ciò che piace. La riga Strumenti già disponibili evita di comprare ciò che l'ente ha già.

La scheda di Borgo Esempio descrive la prova prevista dall'obiettivo proposto per il PIAO 2027-2029: liquidazioni e contributi ad associazioni del Servizio Affari generali, quattro utenti, dati gialli con segnaposto, dal 1° aprile al 30 settembre 2027 (si veda il capitolo sul PIAO). Servono istruzioni persistenti, documenti di riferimento ed esportazione delle conversazioni. Il Comune ha già le licenze della suite d'ufficio, con un assistente di chat incluso.

Sotto i 140.000 euro l'acquisto non deve figurare nel programma triennale degli acquisti di beni e servizi,[^2] ma la spesa va prevista in bilancio: il budget è un dato della scheda, non una conseguenza dell'offerta.

## La valutazione comparativa

### Che cosa chiede l'art. 68 del CAD

Per i programmi informatici la scelta ha una regola propria. L'art. 68 del D.Lgs. 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale, CAD) chiede, prima dell'acquisto, una valutazione comparativa tecnica ed economica tra le soluzioni disponibili: software sviluppato apposta per l'amministrazione, riuso di software già sviluppato per conto della pubblica amministrazione, software libero o a codice sorgente aperto, software in cloud, software proprietario in licenza, o una combinazione. I criteri sono tre:

- il costo complessivo: acquisto, avvio, mantenimento e supporto;
- l'uso di formati di dati e interfacce aperti e di standard per l'interoperabilità;
- le garanzie del fornitore su sicurezza, protezione dei dati e livelli di servizio.

La licenza proprietaria è ammessa quando la valutazione dimostra, con motivazione, che non ci sono soluzioni già disponibili nella pubblica amministrazione, né software libero, adeguati alle esigenze.[^3] Le modalità sono nelle linee guida AgID sull'acquisizione e il riuso del software; le soluzioni in riuso sono nel catalogo di Developers Italia.[^4]

Un servizio di IA generativa in abbonamento è software fruibile in cloud: la regola vale anche in questo caso. Per un piccolo Comune può bastare un documento breve, che mostri le alternative esaminate e dica, per ciascuna, perché è stata scelta o scartata. Formati e interfacce aperti contano anche dopo: sono ciò che permette, un giorno, di cambiare fornitore.

### La bozza AgID e il costo per bozza usata

Le Linee guida AgID per il procurement di IA nella pubblica amministrazione sono ancora una bozza. L'AgID l'ha adottata con la Determinazione n. 43 del 10 marzo 2026 e l'ha posta in consultazione fino all'11 aprile 2026; per l'adozione definitiva servono i passaggi previsti dall'art. 71 del CAD.[^5] La bozza non obbliga, ma indica una direzione. Secondo le sintesi pubblicate, descrive principi e fasi dell'acquisto e propone uno schema di capitolato tecnico, con allegati che comprendono l'inventario dei componenti del sistema (*AI Bill of Materials*) e un piano di portabilità e di uscita. Per i progetti pilota e le iniziative circoscritte a basso rischio prevede un percorso semplificato.[^6]

Dalla bozza viene un'idea utile anche a un Comune di 38 dipendenti: il costo livellato dell'IA (LCOAI), cioè il costo dell'intero ciclo di vita diviso per i risultati validi che lo strumento produce. Adattato agli atti, diventa il costo per bozza usata: licenze, configurazione, formazione e assistenza, divisi per le bozze arrivate alla firma. Il prezzo per utente dice poco: dieci licenze usate di rado possono costare, per bozza, molto più di due usate ogni giorno.

### La griglia

```
VALUTAZIONE COMPARATIVA (art. 68 D.Lgs. 82/2005) – [oggetto]
Comune di [nome] – RUP: RUP_1 – data: [data] – scheda del [data]
Per ogni soluzione:
A. Tipo (art. 68, comma 1): [sviluppo; riuso; libero; cloud; licenza;
   mista]
B. Funzioni necessarie della scheda: [coperte / in parte / no]
C. Dati: accordo art. 28 [sì/no]; addestramento [escluso/no];
   luoghi del trattamento [SEE / fuori SEE, con quale garanzia]
D. Sicurezza: qualificazione ACN [estremi]; certificazioni [quali]
E. Uscita: esportazione [formati]; preavviso; cancellazione
F. Costo per [durata]: iniziale; ricorrente; ore interne;
   costo per bozza usata stimato
G. Convenzione, accordo quadro o MePA: [quale / nessuno]
H. Giudizio motivato: [ammessa / esclusa perché]
Conclusione: [soluzione scelta]; perché non riuso, software libero
e altre soluzioni: [motivi]
```

L'esito per Borgo Esempio:

| Soluzione | Tipo | Punto critico | Esito |
|---|---|---|---|
| Assistente incluso nella suite | cloud, già in licenza | niente documenti di riferimento | resta per tutti |
| Licenze aggiuntive della suite | cloud, licenza | costo per utente | scelta per la prova |
| Chatbot, piano per organizzazioni | cloud, licenza | nuovo contratto da esaminare | alternativa |
| Modulo IA del gestionale | cloud, licenza | modello e luoghi non dichiarati | esclusa per ora |
| Modello libero in locale | software libero | nessun tecnico interno | esclusa |
| Riuso da Developers Italia | riuso | nessuna soluzione adatta | esclusa |

La licenza aggiuntiva non vince perché è la migliore in assoluto. Vince perché resta nello stesso quadro: condizioni del produttore, accordo sul trattamento, account e amministrazione sono quelli già esaminati. Verificato che l'accordo copra anche il nuovo servizio, il fascicolo dello strumento si aggiorna invece di rifarsi (si veda il capitolo su fornitori, trasferimenti e DPIA). Il costo nascosto è la dipendenza da un solo fornitore, di cui si parla alla fine del capitolo. Il fornitore del gestionale, invece, non ha saputo dire quale modello usi e dove passino i dati. L'IA aggiunta a un software già in uso è un trattamento nuovo, da valutare come tale, non un semplice aggiornamento.

### Farsi aiutare dal modello

Condizioni d'uso, accordi sul trattamento e pagine sulla sicurezza sono documenti pubblici, senza dati personali. Il modello può estrarne le voci della griglia.

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

Il modello estrae, tu decidi: riscontra ogni citazione. Le pagine dei fornitori cambiano: salva una copia datata nel fascicolo.

## I requisiti minimi: dati, residenza, addestramento, log, sicurezza

### Requisiti che escludono

I requisiti minimi escludono: se ne manca uno, la soluzione esce dalla griglia, qualunque sia il prezzo. Gli altri servono a scegliere tra le soluzioni rimaste. La protezione dei dati è trattata nel capitolo su fornitori, trasferimenti e DPIA; qui diventa una condizione d'acquisto.[^7]

| Requisito minimo | Perché | Dove si verifica |
|---|---|---|
| Contratto dell'ente con accordo sul trattamento | art. 28 GDPR | accordo del fornitore |
| Niente addestramento sui dati del Comune | finalità del trattamento | contratto e impostazioni |
| Trattamento nello SEE o trasferimenti garantiti | capo V GDPR | sub-responsabili |
| Tempi di conservazione e cancellazione | artt. 5 e 28 GDPR | accordo; console |
| Registri ed esportazione | art. 14 L. 132/2025 | prova prima della firma |
| Account di lavoro, revoca, più fattori | art. 32 GDPR | console |
| Qualificazione ACN del servizio | disciplina cloud PA | catalogo ACN |
| Uscita: preavviso ed esportazione | Data Act; art. 68 CAD | contratto |

*Residenza.* "Dati in Europa" vale spesso per i dati conservati, non per l'elaborazione delle richieste o per l'assistenza: leggi le eccezioni. La L. 132/2025 chiede allo Stato e alle autorità pubbliche di indirizzare le piattaforme di e-procurement in modo che, nella scelta dei fornitori di IA, si possano privilegiare le soluzioni che localizzano ed elaborano in data center nazionali i dati strategici. È una possibilità, non un obbligo, e difficilmente riguarda le bozze ordinarie di un ufficio comunale.[^8]

*Log.* Il registro degli usi lo tiene il Comune (si veda il capitolo sulla tracciabilità). Allo strumento si chiedono un registro degli accessi e l'esportazione di conversazioni, istruzioni e file. Chiedi un'esportazione di prova prima di firmare.

*Sicurezza.* I servizi cloud acquistati dalla pubblica amministrazione devono essere qualificati dall'Agenzia per la cybersicurezza nazionale (ACN). La qualificazione riguarda il singolo servizio, a un livello che dipende dai dati che l'ente vi tratta: cerca nel catalogo quello che compri.[^9] Servono poi account di lavoro con autenticazione a più fattori, revoca immediata quando un dipendente cambia ufficio, amministratori distinti dagli utenti.

*AI Act.* Uno strumento per scrivere bozze, di regola, non è un sistema ad alto rischio. Lo diventa se lo si usa per valutare chi ha diritto a una prestazione di assistenza pubblica (Allegato III, punto 5, lett. a). Chi gli attribuisce questa finalità ne diventa fornitore, con i relativi obblighi, dal 2 dicembre 2027 (art. 25), come spiega il capitolo sull'AI Act. Il regolamento interno vieta questo uso. Il contratto riporta perciò la destinazione d'uso dichiarata dal fornitore e l'impegno del Comune a non usare il servizio per le finalità dell'Allegato III. Un sistema per quelle finalità sarebbe un altro acquisto, fuori da questo capitolo: progettato e dichiarato per lo scopo, con istruzioni per l'uso, registrazione nella banca dati dell'Unione, log conservati almeno sei mesi e valutazione d'impatto sui diritti fondamentali. Chiedi invece come il fornitore marca, in formato leggibile da una macchina, i contenuti generati (art. 50, par. 2).[^10]

*Clausole tipo.* Un riferimento sono le clausole contrattuali tipo per l'acquisto di IA promosse dalla Commissione europea, aggiornate all'AI Act nel marzo 2025, anche in una versione leggera per i sistemi non ad alto rischio. Non sono vincolanti.[^11]

### Il questionario per il fornitore

Le domande si fanno per iscritto, al fornitore o al rivenditore, prima dell'affidamento.

```
QUESTIONARIO PER IL FORNITORE – [soluzione] – risposte entro [data]
Per ogni risposta indicate il documento o la pagina che la conferma.
1. Con quale società firma il Comune? Chi produce il modello?
2. Accordo sul trattamento (art. 28 GDPR): titolo, versione, testo.
3. I dati del Comune sono esclusi dall'addestramento? Dove è scritto?
4. Dove sono conservati ed elaborati prompt, file e risposte, con
   quali eccezioni, per quanto tempo? Elenco dei sub-responsabili.
5. Quali registri sono disponibili all'ente? In quale formato si
   esportano conversazioni, istruzioni e file?
6. Il servizio è qualificato dall'ACN? Con quali estremi?
7. Quale destinazione d'uso dichiarate ai sensi del Regolamento (UE)
   2024/1689? Come applicate l'art. 50?
8. Con quanto preavviso comunicate modifiche di condizioni, prezzi e
   modello? In quali tempi comunicate una violazione di dati personali?
9. Uscita: preavviso, esportazione, costi, attestazione di
   cancellazione.
10. Quale documentazione avete sull'accessibilità del servizio?
```

Le risposte vanno nel fascicolo dello strumento. Una risposta vaga su un requisito minimo vale come un no. La domanda 10 non è una cortesia. Negli acquisti di servizi informatici l'accessibilità è un motivo di preferenza, e la scelta di un servizio non accessibile va motivata. L'ente deve poi dare ai dipendenti con disabilità strumenti adeguati.[^12]

### Le condizioni particolari

Un piccolo Comune non negozia con un grande produttore: accetta le sue condizioni o cambia prodotto. Negozia con il rivenditore, che risponde di ciò che controlla. Sul mercato elettronico le condizioni del Comune si allegano alla trattativa diretta.

```
CONDIZIONI PARTICOLARI DI FORNITURA – [oggetto] – CIG [codice]
Art. 1 Oggetto. [n] utenze del servizio [nome commerciale], piano
[piano per organizzazioni], dal [data] al [data], con l'opzione
dell'art. 7.
Art. 2 Condizioni del produttore. Il servizio è reso alle condizioni
per le organizzazioni del produttore, compreso l'accordo sul
trattamento [titolo, versione], allegate all'offerta. L'affidatario
garantisce che le utenze sono attivate in quel piano.
Art. 3 Dati e modifiche. I dati del Comune non sono usati per
addestrare modelli. L'affidatario comunica appena note le modifiche
annunciate dal produttore su dati, sub-responsabili e modello. Se
accede ai dati del Comune, per l'attivazione o l'assistenza, è
designato responsabile del trattamento con l'accordo allegato.
Art. 4 Registri ed esportazione. L'affidatario assiste il Comune
nell'attivazione dei registri e nell'esportazione in formati aperti
o di uso comune.
Art. 5 Incidenti. L'affidatario comunica gli incidenti sulle utenze
del Comune senza ritardo, e comunque entro [24] ore.
Art. 6 Destinazione d'uso. Il servizio supporta la redazione di
testi. Il Comune non lo usa per le finalità dell'Allegato III del
Regolamento (UE) 2024/1689.
Art. 7 Opzione. Il Comune può estendere la fornitura a [n] ulteriori
utenze e per [durata], alle stesse condizioni economiche, con
comunicazione entro il [data]. L'opzione è compresa nel valore
stimato.
Art. 8 Prezzo. Euro [importo] oltre IVA per l'intera durata, salva
la clausola di revisione dei prezzi: [clausola dell'ente ai sensi
dell'art. 60 del D.Lgs. 31 marzo 2023, n. 36].
Art. 9 Tracciabilità. L'affidatario assume gli obblighi di
tracciabilità dei flussi finanziari dell'art. 3 della L. 13 agosto
2010, n. 136.
Art. 10 Durata e uscita. Il contratto non si rinnova tacitamente.
Alla scadenza l'affidatario assiste il Comune nell'esportazione e
attesta la disattivazione delle utenze.
```

L'art. 2 è il più importante: lega le utenze al piano coperto dall'accordo sul trattamento. L'art. 9 non è facoltativo: la legge chiede la clausola sulla tracciabilità a pena di nullità.[^13]

## Come affidare: licenze in uso, convenzioni, mercato elettronico

### Prima le licenze che l'ente ha già

Spesso il Comune ha già uno strumento di IA senza averlo comprato: l'assistente incluso nelle licenze della suite d'ufficio. Non serve una procedura, perché non c'è un acquisto; serve un atto. Il RTD verifica che l'accordo sul trattamento della suite copra l'assistente e lo configura con l'amministratore di sistema. Con il responsabile della protezione dei dati (DPO) valuta se serve la valutazione d'impatto sulla protezione dei dati (DPIA). Poi aggiorna il fascicolo dello strumento e, con determinazione, l'allegato del regolamento interno sugli strumenti autorizzati. Incluso nel prezzo non vuol dire fuori dalle regole.

Le funzioni pagate a consumo, come gli agenti che leggono i file dell'ente, sono invece un acquisto, e seguono le regole di questo capitolo. Richiedono anche un impegno con un importo massimo e un tetto di spesa impostato nella console: una spesa che cresce con l'uso, senza tetto, non ha copertura.[^14]

### Poi Consip, soggetti aggregatori e mercato elettronico

Per i beni e servizi informatici le amministrazioni si approvvigionano tramite Consip o i soggetti aggregatori, comprese le centrali di committenza regionali, per ciò che è disponibile presso di loro (art. 1, comma 512, della L. 28 dicembre 2015, n. 208). La prima verifica riguarda quindi convenzioni e accordi quadro. Si esce da quegli strumenti solo con un'autorizzazione motivata dell'organo di vertice amministrativo, se il servizio non è disponibile o idoneo al fabbisogno, o per necessità e urgenza; l'acquisto si comunica all'ANAC e all'AgID (comma 516).[^15] Anche quando, con quell'autorizzazione, il Comune non aderisce a una convenzione per servizi comparabili, i parametri di prezzo e qualità della convenzione sono il limite massimo.[^16]

Il mercato elettronico della pubblica amministrazione (MePA) è gestito da Consip. Per i Comuni il ricorso al MePA, a un altro mercato elettronico o al sistema telematico della centrale regionale è obbligatorio per gli acquisti di beni e servizi da 5.000 euro alla soglia europea (art. 1, comma 450, della L. 27 dicembre 2006, n. 296); il comma 512, per l'informatica, non prevede quella soglia minima.[^17] Le licenze dei grandi produttori si acquistano di solito dai rivenditori abilitati. La procedura, anche l'affidamento diretto, si svolge su una piattaforma di approvvigionamento digitale certificata, da cui si acquisisce il codice identificativo di gara (CIG).[^18]

Non comprare online con una carta. L'abbonamento sottoscritto sul sito del produttore salta procedura, CIG e tracciabilità dei pagamenti. Se il piano è per singoli, salta anche il contratto per le organizzazioni e il suo accordo sul trattamento.[^19] Anche se costa poco.

### L'affidamento diretto

Sotto i 140.000 euro servizi e forniture si possono affidare direttamente, con un'unica determina che contiene la decisione di contrarre e la scelta del contraente.[^20] Il capitolo sulle determine spiega come scriverla con l'IA. Per uno strumento di IA contano tre punti in più.

*Valore stimato.* Comprende durata, utenze e opzioni. Un'opzione di estensione scritta in modo chiaro nei documenti iniziali, e compresa nel valore stimato, si esercita senza una nuova procedura.[^21] Se con l'opzione il valore stimato raggiunge i 140.000 euro, l'affidamento diretto non è più possibile.

*Rotazione.* Al contraente uscente, di regola, non si affida un secondo contratto consecutivo nello stesso settore; sotto i 5.000 euro si può derogare.[^22] Se la prova va bene, l'estensione passa dall'opzione, non da un nuovo affidamento allo stesso operatore. Si decide ora, nella determina.

*Prezzo.* I listini sono spesso in dollari e cambiano. Chiedi un prezzo in euro per tutta la durata, e confrontalo con il listino del produttore e con le convenzioni attive. Un nuovo listino non cambia il prezzo del contratto: le variazioni passano dalla clausola di revisione dei prezzi, che il Codice dei contratti vuole nei documenti iniziali.[^23]

### La determina

Il modello è quello di Borgo Esempio: affidamento diretto sul MePA di quattro utenze per la prova, con l'opzione di estensione. Le norme del preambolo vanno verificate prima dell'uso, come spiega il capitolo sulla verifica.

```
COMUNE DI BORGO ESEMPIO – SERVIZIO AFFARI GENERALI
DETERMINAZIONE N. [n] DEL [data]
Oggetto: Determinazione a contrarre e affidamento diretto, tramite
MePA, della fornitura di 4 utenze del servizio di IA generativa
[nome commerciale] per la prova dell'obiettivo 2027/01 del PIAO
2027-2029, con opzione di estensione. CIG [codice].
IL RESPONSABILE DEL SERVIZIO
Visti:
- il D.Lgs. 18 agosto 2000, n. 267 (TUEL), artt. 107, 109, comma 2,
  151, comma 4, 183 e 192;
- il D.Lgs. 7 marzo 2005, n. 82 (CAD), art. 68;
- il D.Lgs. 31 marzo 2023, n. 36, artt. 14, comma 4, 15, 17, commi 1
  e 2, 25, 49, 50, comma 1, lett. b), 52, 60 e 120, comma 1, lett. a);
- la L. 27 dicembre 2006, n. 296, art. 1, comma 450;
- la L. 28 dicembre 2015, n. 208, art. 1, comma 512;
- la deliberazione del Consiglio comunale n. [n] del [data], di
  approvazione del bilancio di previsione [anni];
- la deliberazione della Giunta comunale n. [n] del [data], di
  approvazione del PIAO 2027-2029;
- il decreto sindacale n. [n] del [data] di conferimento dell'incarico;
- la scheda del fabbisogno e la valutazione comparativa, allegate;
Considerato che:
- l'obiettivo 2027/01 del PIAO prevede una prova dell'IA generativa
  negli atti del Servizio dal 1° aprile al 30 settembre 2027;
- non risultano soluzioni in riuso o software libero adeguati, per i
  motivi indicati nella valutazione comparativa;
- alla verifica del [data] non risultano convenzioni o accordi quadro
  attivi per il servizio, che è offerto sul MePA;
- il servizio è qualificato dall'ACN [estremi];
- l'accordo [titolo, versione] costituisce il contratto previsto
  dall'art. 28 del Regolamento (UE) 2016/679 ed è stato esaminato dal
  DPO il [data]; [esito della DPIA o motivi per cui non è necessaria];
- il valore stimato, compresa l'opzione, è di euro [importo] oltre IVA;
- [operatore] ha offerto euro [importo] oltre IVA nella trattativa
  diretta n. [n]; il prezzo è congruo perché [motivo];
- [operatore] ha esperienze pregresse documentate [quali] e ha
  dichiarato il possesso dei requisiti; [esito delle verifiche];
- [rotazione: art. 49, comma 6, o motivazione ai sensi del comma 4];
DETERMINA
1. di affidare a [operatore] la fornitura di 4 utenze del servizio
   [nome commerciale], piano [piano], dal 1° marzo 2027 al 29
   febbraio 2028, per euro [importo] oltre IVA, alle condizioni
   particolari allegate, riservandosi l'opzione del loro art. 7;
2. di impegnare euro [importo IVA compresa] al capitolo [n], esercizi
   [anni];
3. di stipulare il contratto con il documento generato dal MePA;
4. di dare atto che il RUP è RUP_1;
5. di aggiornare il fascicolo dello strumento e trasmettere il
   presente atto al DPO e al segretario comunale.
```

Scheda e valutazione comparativa sono allegate perché motivano la scelta. La verifica delle convenzioni ha una data, perché l'offerta di Consip cambia. Manca, di proposito, l'attestazione di regolarità tecnica: la rende chi firma, dopo i controlli.

## La prova pilota e la misura dei risultati

### Perché una prova

Le impressioni ingannano. In uno studio di Microsoft chi usava l'assistente stimava di aver risparmiato in media 36 minuti; il risparmio misurato era di 12.[^24] Nella valutazione di un ministero britannico il tempo risparmiato non si è tradotto in prove solide di maggiore produttività.[^25] Una prova breve, con misure decise prima, costa meno di un acquisto sbagliato.

### Come si progetta

- *Perimetro stretto.* Un servizio, due tipi di atto, pochi utenti.
- *Misura prima.* I tempi senza IA si rilevano prima della prova, sugli stessi atti e con lo stesso metodo.
- *Dati in due tempi.* Prima i dati verdi; i gialli dopo la valutazione d'impatto e la verifica delle impostazioni. I segnaposto pseudonimizzano, non anonimizzano: i gialli restano dati personali. I rossi non entrano mai.
- *Indicatori.* A quelli dell'obiettivo del PIAO, su efficienza, qualità e controllo, la prova aggiunge quelli dello strumento.
- *Criteri scritti prima.* Che cosa porta a estendere, limitare o sospendere si decide prima di vedere i dati.
- *Mai le persone.* I dati sono per atto e per ufficio, mai per dipendente: lo chiedono il PIAO e i limiti al controllo a distanza dei lavoratori (si vedano i capitoli sul PIAO e sulla tracciabilità).

```
PIANO DELLA PROVA PILOTA – [strumento] – Comune di [nome]
Riferimenti: PIAO [anno], obiettivo [n]; determina [n, data]
Perimetro: Servizio [nome]; atti: [tipi]; utenti: [n]
Periodo: dal [data] al [data]; misura senza IA: [periodo]
Dati: verdi dal [data]; gialli dal [data], dopo [DPIA o valutazione]
Indicatori dell'obiettivo: [rinvio al PIAO]
Indicatori dello strumento:
- costo per bozza usata: costi del periodo / bozze arrivate alla firma
- giorni con disservizi; segnalazioni al fornitore e tempi di risposta
- modifiche di condizioni, prezzi o modello durante la prova
Fonti: registro del metodo; registro degli usi; fatture; segnalazioni;
questionario anonimo finale
Decisione (criteri fissati prima): estendere se [condizioni];
limitare se [condizioni]; sospendere se [condizioni]
Relazione alla Giunta: [chi], entro [data]
```

### La prova gratuita

Molti fornitori offrono una prova gratuita. Anche la prova è un contratto, alle condizioni del fornitore, spesso diverse da quelle a pagamento: controlla, tra l'altro, se i contenuti possono essere usati per l'addestramento. Se l'ente la accetta, lo fa con un atto del responsabile del servizio, con i soli dati verdi e senza impegni d'acquisto. E la valutazione comparativa si fa prima, non dopo: chi ha già provato un prodotto tende a comprarlo.

### Leggere i risultati

Con quattro utenti e sei mesi i numeri sono segnali, non prove. Un risparmio di tempo non basta se crescono i rilievi del controllo successivo. Un costo per bozza alto può dipendere da poche bozze, non dal prezzo. La relazione la porta alla Giunta il segretario, responsabile dell'obiettivo del PIAO, con i dati raccolti dal RTD. La Giunta dà l'indirizzo; l'acquisto resta del responsabile del servizio, perché è gestione.[^26]

## Uscita, portabilità e dipendenza dal fornitore

### Dove nasce la dipendenza

La dipendenza nasce da ciò che si accumula dentro lo strumento: istruzioni dei progetti, file di stile, atti modello caricati, agenti, cronologia delle conversazioni, collegamenti con posta e cartelle, abitudini del personale. Più lo strumento è integrato nella suite, più è comodo e più è difficile lasciarlo.

E il fornitore cambia: prezzi, condizioni, funzioni, modello. Un cambio di modello cambia le bozze, anche con lo stesso prompt. Il Comune non lo controlla; può solo accorgersene in tempo.

### Tenere il patrimonio fuori dallo strumento

La difesa più efficace non è nel contratto. Prompt, file di stile, elenchi di norme e casi di prova sono documenti del Comune: stanno nel sistema documentale, con versione e data, e lo strumento ne ha una copia. Le conversazioni che servono al fascicolo si salvano nel fascicolo (si veda il capitolo sulla tracciabilità). A ogni cambio di modello o di strumento si rifanno i casi di prova (si veda il capitolo sul flusso di lavoro). Così cambiare fornitore significa riconfigurare e formare, non ricominciare.

### Che cosa dicono le norme

*Data Act.* Dal 12 settembre 2025 il Regolamento (UE) 2023/2854 obbliga i fornitori di servizi di trattamento dei dati, compresi i servizi in cloud, a consentire al cliente il passaggio a un altro fornitore o a un'infrastruttura propria: preavviso massimo di due mesi, transizione di regola entro trenta giorni, esportazione dei dati. Fino al 12 gennaio 2027 il passaggio può costare al più quanto costa al fornitore; da quella data, nulla.[^27]

*Formati aperti.* L'art. 68 del CAD li mette tra i criteri della valutazione comparativa: un'esportazione leggibile solo dallo stesso prodotto vale poco.

*Rotazione.* Il contraente uscente si può riconfermare in casi motivati dalla struttura del mercato e dall'effettiva assenza di alternative, oltre che dall'accurata esecuzione del contratto (art. 49, comma 4, del Codice). Una dipendenza creata dal Comune stesso difficilmente dimostra che le alternative mancano.

*Rinnovo.* Nei contratti pubblici il rinnovo tacito non è ammesso.[^28] Disattiva il rinnovo automatico dell'abbonamento e segna la scadenza nello scadenzario del servizio.

### Il piano di uscita

Si scrive all'inizio, quando non serve, e si aggiorna a ogni rinnovo.

```
PIANO DI USCITA – [strumento] – aggiornato al [data]
1. Patrimonio fuori dallo strumento: prompt, file di stile, casi di
   prova, elenchi di norme in [archivio, posizione]
2. Da esportare prima della scadenza: [istruzioni; file caricati;
   registri d'uso; conversazioni non ancora nel fascicolo]; formato
3. Tempi: preavviso [giorni]; esportazione entro [data];
   disattivazione delle utenze il [data]
4. Cancellazione: richiesta il [data]; attestazione ricevuta il [data]
5. Alternativa: [soluzione]; casi di prova rifatti il [data]
6. Personale: comunicazione il [data]; aggiornamento dell'allegato
   del regolamento interno sugli strumenti autorizzati
7. Responsabile: [RTD]; sentito il DPO il [data]
```

### Quando cambiano le condizioni

I fornitori aggiornano spesso condizioni e accordi sul trattamento. Sono testi pubblici: il confronto si può affidare al modello.

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

Porta l'elenco e i due testi al RTD e al DPO. Se una modifica tocca un requisito minimo, si riapre la valutazione.

## Ruoli, atti e tempi

| Chi | Che cosa fa | Con quale atto |
|---|---|---|
| Giunta | obiettivo e indirizzo dopo la prova | PIAO; deliberazione |
| Segretario | coordina, controlla, riferisce | relazione sulla prova |
| Responsabile Affari generali e RTD | fabbisogno, valutazione, affidamento | determina |
| Responsabile Finanziario | copertura e tetto di spesa | visto contabile |
| Altri responsabili | fabbisogno del servizio, utenti | scheda del fabbisogno |
| DPO | accordo, trasferimenti, DPIA | parere scritto |
| Amministratore di sistema | account, impostazioni, registri | rapporto al RTD |

Il DPO non sceglie lo strumento: consiglia, e il suo parere entra nel fascicolo prima della determina. La Giunta non sceglie il fornitore: fissa l'obiettivo e, dopo la prova, l'indirizzo. Nel controllo successivo il segretario verifica che scheda, valutazione e parere ci siano.

Il calendario di Borgo Esempio segue l'obiettivo del PIAO e il percorso del regolamento interno.

| Quando | Passaggio | Chi |
|---|---|---|
| ottobre-novembre 2026 | scheda del fabbisogno | RTD, responsabili |
| dicembre 2026 | valutazione comparativa, questionario | RTD |
| entro 15 gennaio 2027 | parere su accordo e DPIA | DPO |
| febbraio 2027 | determina e contratto | RTD |
| marzo 2027 | configurazione, misura senza IA, formazione | RTD, responsabili |
| 1° aprile-30 settembre 2027 | prova | Servizio Affari generali |
| entro 15 novembre 2027 | relazione e proposta | segretario |
| entro gennaio 2028 | opzione, nuova procedura o uscita | RTD |

La formazione di chi partecipa alla prova va anticipata a marzo, come propone il capitolo sul PIAO: altrimenti la prova misura la formazione mancante, non lo strumento.

## In sintesi

- Prima i processi e i dati, poi il prodotto: la scheda del fabbisogno precede ogni offerta.
- L'art. 68 del CAD chiede una valutazione comparativa scritta anche per un servizio in abbonamento; il costo che conta è quello per bozza usata.
- Senza un requisito minimo la soluzione è esclusa: accordo sul trattamento, niente addestramento, luoghi e tempi del trattamento, registri ed esportazione, account di lavoro, qualificazione ACN, uscita.
- Il contratto lega le utenze al piano coperto dall'accordo sul trattamento, esclude gli usi ad alto rischio e contiene la clausola sulla tracciabilità.
- Prima le licenze in uso, poi convenzioni, accordi quadro e MePA; mai un abbonamento con la carta sul sito del produttore.
- L'opzione di estensione si scrive nella prima determina e si conta nel valore stimato.
- La prova ha perimetro stretto, misura iniziale, criteri scritti prima e dati mai per persona.
- Contro la dipendenza: prompt, file di stile e casi di prova fuori dallo strumento, e un piano di uscita scritto all'inizio.

[^1]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 1, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it.

[^2]: D.Lgs. 31 marzo 2023, n. 36, *Codice dei contratti pubblici*, art. 37, che limita il programma triennale degli acquisti di beni e servizi agli acquisti di importo stimato pari o superiore alla soglia dell'art. 50, comma 1, lett. b), normattiva.it.

[^3]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale*, art. 68, commi 1, 1-bis e 1-ter, normattiva.it.

[^4]: AgID, *Linee guida su acquisizione e riuso di software per le pubbliche amministrazioni*, 2019, agid.gov.it; catalogo del software a riuso e open source per la pubblica amministrazione, developers.italia.it. Sul riuso si veda anche l'art. 69 del CAD.

[^5]: AgID, Determinazione n. 43 del 10 marzo 2026, che ha posto in consultazione, dal 12 marzo all'11 aprile 2026, le bozze di *Linee guida per il procurement di IA nella PA* e di *Linee guida per lo sviluppo di sistemi di IA nella PA*, agid.gov.it; D.Lgs. 7 marzo 2005, n. 82, cit., art. 71, sul procedimento di adozione, che prevede il parere della Conferenza unificata e, nelle materie di competenza, il Garante per la protezione dei dati personali. Lo stato dell'iter va verificato alla data d'uso.

[^6]: AgID, *Linee guida per il procurement di IA nella PA*, bozza per la consultazione pubblica, con lo schema di capitolato tecnico, 2026, agid.gov.it. I contenuti sono riportati secondo sintesi concordanti pubblicate da siti giuridici e tecnici, tra cui altalex.com e certifico.com, e vanno riscontrati sul testo della bozza o, se adottata, della versione definitiva. Nelle sintesi il costo livellato (LCOAI) è dato dai costi di investimento più i costi operativi, divisi per il numero di risultati validi prodotti nel periodo. Il costo per bozza usata è un adattamento di questo libro.

[^7]: Regolamento (UE) 2016/679 (GDPR), artt. 5, par. 1, lett. e), 28, 32 e 44-49, eur-lex.europa.eu. Se il fornitore usasse i dati del Comune per finalità proprie, come l'addestramento, per quel trattamento sarebbe titolare (art. 28, par. 10).

[^8]: L. 23 settembre 2025, n. 132, cit., art. 5, comma 1, lett. d), normattiva.it. La disposizione chiede di indirizzare le piattaforme in modo che queste soluzioni "possano essere privilegiate", nel rispetto della normativa sulla concorrenza e dei principi di non discriminazione e proporzionalità: una possibilità, non un obbligo per il singolo acquisto.

[^9]: Agenzia per la cybersicurezza nazionale, decreto direttoriale n. 21007/24 del 27 giugno 2024, che adotta il regolamento unico per le infrastrutture digitali e i servizi cloud della pubblica amministrazione, in vigore dal 1° agosto 2024, e catalogo dei servizi cloud qualificati, acn.gov.it. La qualificazione riguarda il singolo servizio, non il fornitore; il livello richiesto dipende da come l'ente classifica dati e servizi (ordinari, critici, strategici).

[^10]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024 (AI Act), artt. 6, par. 2, 13, 25, par. 1, lett. c), 26, parr. 6 e 8, 27, 49, 50, par. 2, e Allegato III, punto 5, lett. a), eur-lex.europa.eu. La data del 2 dicembre 2027 per gli obblighi sui sistemi dell'Allegato III è fissata dall'art. 113, come modificato dal Regolamento (UE) 2026/1744 dell'8 luglio 2026, in vigore dal 27 luglio 2026. L'obbligo di marcatura dell'art. 50, par. 2, si applica dal 2 agosto 2026; per i sistemi di IA generativa immessi sul mercato prima di quella data, dal 2 dicembre 2026.

[^11]: Comunità di pratica sugli appalti pubblici di IA, promossa dalla Commissione europea, *EU Model Contractual AI Clauses* (versione per i sistemi ad alto rischio e versione *Light*), aggiornate nel marzo 2025, public-buyers-community.ec.europa.eu.

[^12]: L. 9 gennaio 2004, n. 4, *Disposizioni per favorire e semplificare l'accesso degli utenti e, in particolare, delle persone con disabilità agli strumenti informatici*, art. 4, sull'accessibilità negli acquisti di beni e servizi informatici e sulla strumentazione da mettere a disposizione dei dipendenti con disabilità, normattiva.it.

[^13]: L. 13 agosto 2010, n. 136, art. 3, comma 8, normattiva.it.

[^14]: D.Lgs. 18 agosto 2000, n. 267 (TUEL), art. 183, comma 1, sull'impegno, che indica la somma da pagare, e art. 191, comma 1, per il quale si effettuano spese solo con impegno contabile registrato e attestazione della copertura finanziaria, normattiva.it.

[^15]: L. 28 dicembre 2015, n. 208, art. 1, commi 512 e 516, normattiva.it. Quale sia, in un Comune, l'organo di vertice amministrativo che autorizza è una questione discussa: chiariscila con il segretario prima di usare la deroga.

[^16]: L. 23 dicembre 1999, n. 488, art. 26, comma 3, normattiva.it.

[^17]: L. 27 dicembre 2006, n. 296, art. 1, comma 450, normattiva.it. Per gli acquisti informatici sotto i 5.000 euro verifica con il servizio finanziario e con il segretario l'interpretazione seguita dall'ente.

[^18]: D.Lgs. 31 marzo 2023, n. 36, cit., artt. 25 e 26, sulle piattaforme di approvvigionamento digitale e sulla loro certificazione, normattiva.it.

[^19]: L. 13 agosto 2010, n. 136, cit., art. 3, sulla tracciabilità dei flussi finanziari e sull'indicazione del CIG negli strumenti di pagamento; D.L. 24 aprile 2014, n. 66, art. 25, per il quale la pubblica amministrazione non può pagare le fatture elettroniche prive del CIG, normattiva.it.

[^20]: D.Lgs. 31 marzo 2023, n. 36, cit., artt. 17, commi 1 e 2, e 50, comma 1, lett. b); TUEL, art. 192, normattiva.it. Negli affidamenti diretti il contratto si può stipulare mediante corrispondenza secondo l'uso commerciale (art. 18, comma 1), e sotto la soglia europea non si applica il termine dilatorio (art. 55, comma 2).

[^21]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 14, comma 4, sul valore stimato comprensivo di opzioni e rinnovi esplicitamente stabiliti, e art. 120, comma 1, lett. a), sulle modifiche previste in clausole chiare, precise e inequivocabili dei documenti iniziali, normattiva.it.

[^22]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 49, commi 2, 4 e 6, normattiva.it.

[^23]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 60, normattiva.it. Soglie e modalità della revisione sono state modificate dal correttivo, il D.Lgs. 31 dicembre 2024, n. 209: verificale sul testo vigente e usa la clausola tipo adottata dall'ente.

[^24]: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers Likely Provide Meaningful Boosts to Productivity*, Microsoft, MSR-TR-2023-43, 2023, microsoft.com, Copilot Common Tasks Study.

[^25]: Department for Business and Trade, valutazione della sperimentazione di Microsoft 365 Copilot, 2025, gov.uk, sulla prova con 1.000 licenze da ottobre a dicembre 2024.

[^26]: TUEL, artt. 107 e 109, comma 2, normattiva.it.

[^27]: Regolamento (UE) 2023/2854 del Parlamento europeo e del Consiglio, del 13 dicembre 2023 (Data Act), artt. 23, 25 e 29, eur-lex.europa.eu. Il capo VI, sul passaggio tra servizi di trattamento dei dati, si applica dal 12 settembre 2025 (art. 50). Fino al 12 gennaio 2027 i costi di passaggio ridotti non possono superare quelli sostenuti dal fornitore e direttamente collegati al passaggio. Il periodo di transizione si può prolungare se il passaggio entro trenta giorni è tecnicamente impossibile.

[^28]: Il divieto di rinnovo tacito dei contratti pubblici era espresso, da ultimo, dall'art. 57, comma 7, del D.Lgs. 12 aprile 2006, n. 163, abrogato con l'intero codice dal D.Lgs. 18 aprile 2016, n. 50; la giurisprudenza amministrativa lo considera ancora un principio dei contratti pubblici. Il rinnovo è ammesso solo se previsto nei documenti iniziali e compreso nel valore stimato (D.Lgs. 31 marzo 2023, n. 36, cit., art. 14, comma 4), normattiva.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 38 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Art. 68 CAD: al criterio dei formati aperti veniva attribuito uno scopo ('permettono di cambiare') che la norma non indica; il criterio riguarda formati, interfacce aperte e standard di interoperabilità.
- Bozza AgID sul procurement di IA: dettagli precisi non riscontrabili (otto principi, cinque fasi, allegati E e H, elenco dei principi) presentati come certi; ridotti a quanto attribuibile alle sintesi pubblicate.
- AI Act: il testo chiedeva di mettere nei contratti gli obblighi per l'alto rischio subito dopo aver escluso l'uso ad alto rischio (contraddizione), e taceva l'art. 25: il deployer che cambia la finalità diventa fornitore.
- Incoerenza con il capitolo sul PIAO: la relazione sulla prova andava 'al segretario', ma il segretario è responsabile dell'obiettivo ed è lui a presentarla alla Giunta.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
