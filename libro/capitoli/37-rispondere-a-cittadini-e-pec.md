# Rispondere a cittadini e PEC

In questo capitolo: riconoscere che cosa chiede una PEC, il prompt e la bozza commentata di una risposta di accesso, avvisi sul sito e chatbot alla luce dell'art. 50 dell'AI Act, la libreria dei modelli di risposta.

## Il problema: la risposta è il testo che il cittadino legge

Ogni giorno la casella PEC del Comune riceve istanze, reclami, richieste di documenti, domande. La risposta è spesso l'unico testo dell'ente che il cittadino legge per intero, e quello che più si è tentati di affidare all'IA: nella sperimentazione del Department for Work and Pensions britannico, i risparmi di tempo più alti riguardavano la ricerca di informazioni e la scrittura di e-mail.[^1]

Ma una risposta non è sempre una cortesia. Un diniego di accesso è un provvedimento: ha un termine, una motivazione, un giudice. Una richiesta di integrazione sospende un termine. Un'informazione sbagliata su una scadenza può costare al cittadino un diritto, e al Comune una contestazione.

Su questi testi l'IA può sbagliare in tre modi. Tratta ogni richiesta di documenti come "accesso agli atti" e chiede una motivazione che la legge non sempre chiede. Riempie i vuoti con fatti plausibili: termini, orari, numeri di telefono, uffici. E riceve, se glielo permetti, la PEC intera: nome, indirizzo, codice fiscale, a volte una diagnosi.

Prima di scrivere servono quindi tre risposte: che cosa chiede la PEC, chi decide ed entro quando, che cosa può entrare nel prompt.

## Scrivere per chi legge

### Le regole

Le regole di chiarezza sono quelle del capitolo sulla lingua degli atti. Le direttive del Ministro per la Funzione pubblica del 2002 e del 2005 le rivolgono a tutti i testi amministrativi, lettere comprese: "al rigore di chi scrive deve corrispondere la comprensione di chi legge".[^2] Per i siti, l'art. 53 del D.Lgs. 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale, CAD) chiede tra l'altro accessibilità, completezza di informazione e "chiarezza di linguaggio".[^3] Le indicazioni di Designers Italia, che accompagnano le linee guida di design dell'AgID per siti e servizi digitali, vanno nella stessa direzione: forma attiva, paragrafi brevi, verbi al posto delle parole in "-zione" e "-mento".[^4]

Cambia il lettore. L'atto lo leggono il responsabile, il revisore, a volte il giudice. La lettera la legge una persona che vuole sapere com'è andata, che cosa deve fare, a chi rivolgersi.

L'IA semplifica bene, se glielo chiedi nel modo giusto, ma può cambiare il senso: secondo uno studio del 2025 su testi amministrativi, la qualità della semplificazione fatta con ChatGPT varia molto secondo il prompt, e il risultato va sempre rivisto.[^5] Un "può" che diventa "deve", un "entro" perso, cambiano la risposta.

### Prima e dopo

> In riscontro alla Sua nota prot. n. ... si comunica che l'istanza di cui in oggetto non può trovare accoglimento in quanto carente della documentazione prevista.

> Per completare la domanda ci serve ancora il preventivo della ditta. Può inviarlo a questa PEC entro il 30 ottobre 2026.

La seconda dice che cosa manca, come mandarlo ed entro quando. E non parla di accoglimento: la domanda non è respinta, è incompleta.

### La sezione Lettere del file di stile

Aggiungi al file di stile, descritto nel capitolo sul metodo del prompt, una sezione per lettere e avvisi.

```
FILE DI STILE – sezione Lettere e avvisi – versione [n] del [data]
L1. Prima riga: la risposta (accolta, respinta, che cosa manca). Poi
    le ragioni.
L2. "Noi" dell'ufficio; "lei" per il destinatario, minuscolo.
L3. Una richiesta al cittadino per punto: che cosa, entro quando, come.
L4. Termini con la data quando è certa; se no, giorni e decorrenza.
L5. Norme solo dove fondano un obbligo, un limite o un rimedio.
L6. Niente formule: "in riscontro", "si comunica", "la presente".
L7. Un link alla pagina precisa, mai "consultare il sito istituzionale".
L8. Niente scuse, promesse o giudizi che il responsabile non ha deciso.
L9. Chiudi con chi segue la pratica: ufficio, recapiti, orari.
L10. Avvisi del sito: registro [tu oppure lei]; titolo sotto le 10 parole.
```

L2 e L10 sono scelte da fare una volta per tutto l'ente. La L8 è la più importante: il modello tende alla cortesia, ma una scusa o una promessa scritta dal Comune impegna il Comune.

## Riconoscere la richiesta prima di rispondere

### Sei richieste diverse

"Chiedo copia di..." può aprire procedimenti diversi, con regole diverse.[^6]

| Richiesta | Chi può farla | Motivazione | Termine |
|---|---|---|---|
| Accesso documentale | chi ha un interesse qualificato | sì | 30 giorni |
| Accesso civico semplice | chiunque | no | 30 giorni |
| Accesso generalizzato | chiunque | no | 30 giorni |
| Accesso ambientale | chiunque | no | 30 giorni, fino a 60 |
| Accesso del consigliere | consigliere comunale | no; utile al mandato | regolamento |
| Accesso ai propri dati | l'interessato | no | un mese, fino a tre |

### L'accesso documentale

Lo regolano gli artt. 22-25 della L. 7 agosto 1990, n. 241, e il D.P.R. 12 aprile 2006, n. 184. Può chiederlo chi ha un interesse diretto, concreto e attuale, collegato al documento (art. 22), e deve motivare la richiesta (art. 25, comma 2). Senza controinteressati la richiesta può essere informale; altrimenti l'ufficio li informa, e loro hanno dieci giorni per opporsi. Il procedimento si chiude in trenta giorni, e il silenzio vale rifiuto (art. 25, comma 4). I limiti sono quelli dell'art. 24, salvo l'accesso necessario per curare o difendere i propri interessi giuridici; per i dati sensibili e giudiziari, solo se strettamente indispensabile (comma 7).[^7]

### L'accesso civico

L'art. 5 del D.Lgs. 14 marzo 2013, n. 33, ne prevede due. Il semplice riguarda i documenti che il Comune doveva pubblicare e non ha pubblicato: si chiede al responsabile della prevenzione della corruzione e della trasparenza (RPCT) e, se è fondato, il Comune pubblica e invia il link. Il generalizzato riguarda ogni altro documento o dato detenuto: chiunque può chiederlo, senza motivazione (comma 3). Si chiude con un provvedimento espresso e motivato entro trenta giorni, sospesi mentre i controinteressati possono opporsi (commi 5 e 6). I limiti sono solo quelli dell'art. 5-bis, dalla protezione dei dati personali agli interessi commerciali; se riguardano una parte, si rilascia il resto.[^8]

Il Comune non deve creare dati che non ha, né rielaborarli. E ciò che rilascia con l'accesso generalizzato diventa, di fatto, pubblico: con questo metro si valutano i dati personali.[^9]

### Quando il cittadino non dice quale

Spesso il cittadino scrive solo "chiedo copia". Per l'Adunanza plenaria del Consiglio di Stato, il Comune deve esaminare la richiesta anche come accesso generalizzato, salvo che il richiedente abbia fatto riferimento esclusivo e inequivocabile all'accesso documentale.[^10] Un modello di IA, se non glielo dici, può qualificare tutto come accesso ai sensi della L. 241/1990 e chiedere una motivazione che, per il generalizzato, non serve: i tempi si allungano e il diniego diventa contestabile.

### Il prompt di classificazione

Prima della risposta, un prompt separato dice che cosa contiene la PEC. Usalo solo con lo strumento dell'ente, quello con il contratto dell'art. 28 del GDPR, e sul testo pseudonimizzato: i segnaposto riducono il rischio, ma non rendono anonimo il testo. Prima di incollare, leggi la PEC: se parla di salute, minori o reati, resta fuori, come si vede più avanti.

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

L'ultima riga è una rete di sicurezza, non il filtro: il filtro sei tu, prima di incollare. Termini e norme vengono dalla tabella verificata dell'ufficio, non dal modello. Il modello serve a non perdere una richiesta nascosta, come una domanda sui propri dati dentro un reclamo.

## La risposta a una PEC: dal messaggio alla bozza

### Il caso

Il 14 settembre 2026 il Comune di Borgo Esempio riceve la PEC di un residente di una frazione. Lo scorso gennaio la sua via è rimasta per giorni senza pulizia. Chiede copia del contratto con la ditta dello sgombero neve, del piano neve e dei rapportini degli interventi di gennaio 2026. E chiede chi chiamare alla prossima nevicata.

La PEC va al Servizio Tecnico, che detiene i documenti (art. 5, comma 3, del D.Lgs. 33/2013). Contratto e rapportini riguardano l'esecuzione di un contratto pubblico: vale anche l'art. 35 del D.Lgs. 31 marzo 2023, n. 36, che per questi atti richiama sia la L. 241/1990 sia l'accesso civico. Il prompt di classificazione trova un'istanza di accesso senza tipo, una segnalazione, una richiesta di informazioni. Il responsabile decide: per il piano neve, già pubblicato, basta il link; il contratto con Ditta Neve Esempio S.r.l., società inventata, si rilascia per intero, dopo aver informato la ditta; i rapportini si rilasciano senza nomi e firme degli operatori.

Il modello non decide che cosa rilasciare: la decisione entra nel prompt come dato.

### Che cosa entra nel prompt

Il semaforo del capitolo su quale IA usare e con quali dati vale anche per la posta.

- *Verde.* La domanda generale, come "che documenti servono per la residenza?": la risposta viene dalle pagine del sito.
- *Giallo.* La risposta a un caso: solo lo strumento dell'ente, con il contratto dell'art. 28 del GDPR, e la PEC pseudonimizzata (RICHIEDENTE_1, PROT_1, VIA_1). Restano fuori codice fiscale, recapiti, firma e allegati, a partire dal documento d'identità. Con i segnaposto la PEC resta gialla: pseudonimizzare non è anonimizzare.
- *Rosso.* La PEC che parla di salute, minori o reati, come una domanda di contrassegno per persone con disabilità o un esposto. Il contenuto resta fuori dal prompt, con qualunque strumento. Anche il solo tipo di richiesta può rivelare il dato: una domanda di contrassegno dice già qualcosa sulla salute. Parti dal modello approvato della libreria e completalo a mano.

Gli assistenti integrati nella posta possono leggere il messaggio intero e, secondo le impostazioni, gli allegati, senza segnaposto. Usali solo se l'ente li ha autorizzati per quella casella, e mai sulle PEC rosse. Con un account ammesso solo per testi verdi, chiedi un testo generico, senza fatti del caso: i fatti li inserisci tu.

### La struttura della risposta di accesso

Il provvedimento sull'accesso generalizzato è espresso e motivato, e indica termine e autorità cui ricorrere.[^11] In forma di lettera, l'ordine è questo:

1. intestazione, protocollo in uscita, data, destinatario e domicilio digitale;
2. oggetto con tipo di accesso ed esito; riferimento alla richiesta;
3. come è stata esaminata la richiesta;
4. esito per ogni documento: rilasciato, rilasciato in parte, già pubblicato, non detenuto;
5. motivo di ogni limite, con norma e fatto; controinteressati ed esito;
6. modalità di rilascio, costi, rimedi con i termini;
7. ufficio, referente e recapiti; firma digitale.

### Il prompt

È lo schema in cinque parti del capitolo sul metodo del prompt, con una riga in più: le decisioni.

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

Le righe Decisioni, Dati e Rimedi le compila l'ufficio. Per il caso di Borgo Esempio:

```
Decisioni del responsabile, documento per documento:
1. Piano neve 2025-2026: già pubblicato; indicare il link.
2. Contratto con Ditta Neve Esempio S.r.l.: rilasciato per intero.
3. Rapportini di gennaio 2026: senza nomi e firme degli operatori (art.
   5-bis, comma 2, lett. a, D.Lgs. 33/2013); nomi esclusi anche come
   accesso documentale: la PEC non dice a che cosa servano.
Dati: tipo di accesso non indicato, esaminata come generalizzato. Ditta
informata il 18 settembre 2026 (art. 5, comma 5), non si è opposta.
Invio in PDF via PEC, gratuito. RPCT: il segretario comunale.
Segnalazione: dai rapportini, VIA_1 pulita la prima volta il 14 gennaio.
Rimedi: riesame del RPCT, 20 giorni, sentito il Garante (art. 5, c. 7);
difensore civico (art. 5, c. 8); TAR entro 30 giorni (art. 116 c.p.a.).
```

### La bozza commentata

È un esempio costruito per questo capitolo, con i difetti tipici di un primo giro. Fatti, date e ditta sono inventati.

```
[VERIFICARE: intestazione del Comune, luogo e data]
Servizio Tecnico
Prot. n. [VERIFICARE: protocollo in uscita]

A RICHIEDENTE_1
PEC: [VERIFICARE: domicilio digitale del richiedente]

Oggetto: accesso civico generalizzato. Accoglimento parziale.
Riferimento: sua PEC del 14 settembre 2026, PROT_1.

Gentile RICHIEDENTE_1,
le inviamo due dei tre documenti che ha chiesto e le indichiamo dove
trovare il terzo. Dai rapportini abbiamo tolto solo i nomi e le firme
degli operatori.

Come abbiamo esaminato la richiesta
La sua PEC non indica il tipo di accesso. L'abbiamo esaminata come
accesso civico generalizzato, che chiunque può chiedere senza
motivazione (art. 5, commi 2 e 3, del D.Lgs. 14 marzo 2013, n. 33).

I documenti
- Piano neve 2025-2026: è già pubblicato sul sito del Comune, a questo
  indirizzo: [VERIFICARE: link alla pagina].
- Contratto con Ditta Neve Esempio S.r.l.: in allegato, completo.
  Il 18 settembre 2026 abbiamo informato la ditta della sua richiesta
  (art. 5, comma 5). La ditta non si è opposta.
- Rapportini degli interventi di gennaio 2026: in allegato, senza nomi
  e firme degli operatori. Questi dati non servono a capire come è
  stato svolto il servizio, e rilasciarli li renderebbe di fatto
  pubblici (art. 5-bis, comma 2, lett. a), del D.Lgs. 33/2013). La sua
  PEC non dice a che cosa le servirebbero: per questo non li rilasciamo
  neppure come accesso documentale (artt. 22 e 25 della L. 7 agosto
  1990, n. 241).
Il rilascio è gratuito.

La sua segnalazione
Dai rapportini, la prima pulizia di VIA_1 risulta il 14 gennaio 2026.
[VERIFICARE: date della nevicata e ordine di pulizia nel piano neve]
Durante le nevicate può segnalare una strada non pulita al numero
[VERIFICARE: numero e orari del servizio di reperibilità].

Se non è d'accordo
Sui dati tolti dai rapportini può chiedere il riesame al segretario
comunale, responsabile della prevenzione della corruzione e della
trasparenza. Decide entro venti giorni, sentito il Garante per la
protezione dei dati personali (art. 5, comma 7). Può rivolgersi anche
al difensore civico competente (art. 5, comma 8).
Contro questa decisione, o contro quella sul riesame, può ricorrere
al TAR [VERIFICARE: sede] entro trenta giorni da quando la conosce
(art. 116 del D.Lgs. 2 luglio 2010, n. 104).

Chi segue la pratica
Servizio Tecnico, [VERIFICARE: referente, telefono, orari].

Cordiali saluti.
Il Responsabile del Servizio Tecnico
(firmato digitalmente)

Allegati: contratto (PDF); rapportini di gennaio 2026 (PDF, 31 pagine).
```

*L'intestazione.* Il prompt non nomina il Comune, e il modello non lo inventa: intestazione, luogo e data li aggiunge l'ufficio, dalla carta intestata. Per lo stesso motivo resta aperta la sede del TAR.

*La prima frase.* Dà l'esito prima delle ragioni, come vuole la regola L1.

*La qualificazione.* Viene dalla riga Dati. Senza, il modello rischia di citare gli artt. 22 e seguenti della L. 241/1990 e di chiedere al richiedente di motivare. Per i nomi negati, la lettera spiega perché non spettano neppure come accesso documentale: la richiesta generica si esamina in entrambi i regimi.

*Il limite.* Ha una norma e un fatto: i nomi non servono a capire il servizio. "Per motivi di privacy" non è una motivazione. L'oscuramento si fa sul file, con le cautele del capitolo sulla privacy prima della pubblicazione: i rapportini non passano dal modello. Tolti i nomi, gli operatori non subiscono pregiudizio, e l'ufficio non li ha trattati come controinteressati: è una valutazione da scrivere nel fascicolo.

*La ditta.* La comunicazione sospende il termine per i dieci giorni dati per opporsi; prima di decidere, l'ufficio accerta che la ditta l'abbia ricevuta (art. 5, comma 5).

*La segnalazione.* Il modello riporta la data e chiede di verificare il resto, invece di spiegare il ritardo. Questa parte non è un provvedimento e non ha rimedi: per questo ha una sezione sua.

*I rimedi.* Vengono dall'elenco verificato. Senza elenco, il modello rischia di indicare il termine di sessanta giorni del rito ordinario: per l'accesso il termine è di trenta giorni.[^12] Nel riesame il RPCT sente il Garante perché il limite riguarda dati personali. Il difensore civico comunale è stato soppresso dal 2010 (art. 2, comma 186, lett. a, della L. 23 dicembre 2009, n. 191): la lettera dice "competente", e l'ufficio verifica se nel suo territorio è quello provinciale, detto territoriale, o quello regionale.

*"31 pagine".* Il numero non era nei dati. È l'aggiunta tipica: plausibile, in una riga che nessuno rilegge.

*L'invio.* La lettera si protocolla in uscita, si firma digitalmente e si invia al domicilio digitale del richiedente: per spedizione e ricevimento, ha gli effetti di una raccomandata con ricevuta di ritorno.[^13] Poi la richiesta va nel registro degli accessi, e l'uso dell'IA nel fascicolo (si veda il capitolo sulla tracciabilità).

### Gli errori tipici dell'IA nelle risposte

| Errore | Esempio | Come intercettarlo |
|---|---|---|
| Accesso mal qualificato | motivazione chiesta per il generalizzato | prompt di classificazione |
| Termini inventati | TAR entro sessanta giorni | elenco dei rimedi verificato |
| Fatti plausibili | "31 pagine", "pulita entro 24 ore" | riga Fatti; lettura riga per riga |
| Limiti generici | "per motivi di privacy" | norma e fatto per ogni limite |
| Promesse e scuse | "provvederemo al rimborso" | regola L8 |
| Dati di terzi | nome dell'operatore nella lettera | controllo dei segnaposto |
| Recapiti inventati | numero o PEC dell'ufficio | contatti dalla libreria |

Un altro errore da intercettare è dichiarare "non più disponibile" un atto tolto dal sito: scaduto il periodo di pubblicazione, si chiede con l'accesso civico generalizzato.[^14]

### Prima della firma

1. Ogni richiesta della PEC ha una risposta o un seguito.
2. Accesso senza tipo indicato: esaminato anche come generalizzato.
3. Gli esiti sono quelli decisi dal responsabile, documento per documento.
4. Ogni limite ha norma e fatto; gli oscuramenti sono fatti sul file.
5. Controinteressati: comunicazione ricevuta, dieci giorni trascorsi, opposizioni valutate.
6. Termini e rimedi dall'elenco verificato; nessun `[VERIFICARE]` o segnaposto rimasto.
7. Nessun fatto, numero, scusa o promessa che il responsabile non abbia deciso.
8. Protocollo, firma digitale, invio al domicilio digitale, registro degli accessi, uso dell'IA annotato nel fascicolo.

## Avvisi e comunicati sul sito: quando dichiarare l'uso dell'IA

### La regola

Dal 2 agosto 2026 il deployer che pubblica un testo generato o modificato dall'IA "allo scopo di informare il pubblico su questioni di interesse pubblico" deve dichiararlo (art. 50, par. 4, secondo comma, del Regolamento (UE) 2024/1689, AI Act). Il Regolamento (UE) 2026/1744 non ha rinviato l'obbligo.[^15] Il quadro è nel capitolo sull'AI Act.

Sono testi di questo tipo le notizie e gli avvisi del sito, i comunicati, i messaggi istituzionali sui social. Secondo le prime sintesi, le linee guida della Commissione del 20 luglio 2026, non vincolanti, intendono l'interesse pubblico in senso ampio, amministrazione pubblica compresa.[^16] Non è un testo di questo tipo, stando alla norma, la risposta a un singolo cittadino: non è pubblicata e non informa il pubblico.

L'obbligo non si applica se il testo è stato sottoposto a revisione umana o a controllo editoriale e una persona fisica o giuridica ne ha la responsabilità editoriale. Per il Comune è la via ordinaria.

### Quale revisione basta

Sempre secondo le sintesi, la revisione deve essere sostanziale, non un'occhiata, e una modifica rilevante fatta con l'IA dopo l'approvazione fa venire meno l'esenzione.[^17] Quindi chi approva confronta il testo con la fonte: date, orari, link, recapiti. Il testo approvato è quello pubblicato: se poi chiedi all'IA di accorciarlo per i social, la nuova versione va riapprovata. E resta traccia di chi ha approvato che cosa, e quando (si veda il capitolo sulla tracciabilità).

La dichiarazione serve per i testi che escono senza revisione. In un Comune il caso più probabile è la traduzione automatica di un avviso, pubblicata senza che nessuno la rilegga. Dichiarare l'uso dell'IA anche quando non è obbligatorio è una scelta dell'ente, coerente con la conoscibilità chiesta dall'art. 14, comma 1, della L. 23 settembre 2025, n. 132: la decide il regolamento interno, e una formula è nel capitolo sull'AI Act.[^18]

### L'avviso

Testo verde, senza dati personali: il modello trasforma in avviso la disposizione del responsabile dei Servizi demografici.

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

Anche questa bozza è un esempio costruito per il capitolo. Borgo Esempio usa il "tu" nel sito e il "lei" nelle lettere.

```
Anagrafe e stato civile: dal 2 novembre solo su appuntamento

Dal 2 novembre 2026 l'ufficio anagrafe e stato civile riceve solo
su appuntamento.

Come prenotare
- online, dall'agenda del Comune: [VERIFICARE: link alla pagina];
- per telefono, dal lunedì al venerdì, dalle 9 alle 12:
  [VERIFICARE: numero dell'ufficio].

Per molti certificati non serve venire in Comune: puoi scaricarli
dall'Anagrafe nazionale della popolazione residente, con la tua
identità digitale.

Servizi demografici – [VERIFICARE: PEC, telefono e orari]
```

*L'aggiunta.* La frase sui certificati non era nella fonte. È esatta, ma resta un'aggiunta: l'elenco finale la segnala, e il responsabile decide. Esatta oggi, domani forse no.

*La dichiarazione.* Il responsabile dei Servizi demografici rivede e approva il testo il 6 ottobre 2026: con revisione e responsabilità editoriale, l'obbligo dell'art. 50 non scatta.

### Prima della pubblicazione

1. Date, orari, link e recapiti confrontati con la fonte; i link si aprono.
2. Le frasi "non dalla fonte" sono state tolte o approvate.
3. Approvazione registrata, con nome e data; ogni modifica successiva riapprovata.
4. Testi pubblicati senza revisione, come le traduzioni automatiche: dichiarazione visibile all'inizio.

## Chatbot per il pubblico: dire che si parla con una macchina

### L'obbligo

Chi interagisce con un sistema di IA deve esserne informato, salvo che sia evidente per una persona ragionevolmente informata, attenta e avveduta (art. 50, par. 1). L'informazione va data in modo chiaro e distinguibile, al più tardi alla prima interazione, nel rispetto dei requisiti di accessibilità (par. 5).[^19] L'obbligo è del fornitore, ma il cittadino scrive al Comune: prevedi l'avviso nel contratto e controllalo prima della messa in linea. Se il Comune è fornitore, perché ha fatto sviluppare il sistema e lo mette in servizio con il proprio nome, l'obbligo è suo (si veda il capitolo sull'AI Act, che propone anche una formula).

Un avviso nascosto nell'informativa privacy o in un piè di pagina difficilmente è "chiaro e distinguibile". Mettilo nella finestra della chat, prima della prima risposta.

### Che cosa può fare

Il chatbot è un'interfaccia sulle pagine del sito, non un ufficio.

- Risponde su informazioni generali, solo dalle pagine del Comune, con il link alla pagina usata.
- Non riceve istanze, reclami o richieste di accesso: indica PEC o sportello.
- Non conosce lo stato delle pratiche, e non lo inventa.
- Non valuta se una persona ha diritto a una prestazione: diventerebbe un sistema che l'AI Act può classificare ad alto rischio e, se la sua risposta decidesse da sola, una decisione automatizzata soggetta ai limiti dell'art. 22 del GDPR.[^20]
- Offre sempre una persona: un numero, un orario, un modulo di contatto.
- Tratta i dati che i cittadini scrivono: servono contratto con il fornitore ai sensi dell'art. 28 del GDPR, informativa, conservazione breve e, se il rischio può essere elevato, valutazione d'impatto (si vedano i capitoli sul GDPR).[^21]
- Fa parte del sito: deve essere accessibile anche alle persone con disabilità.[^22]

### Quando sbaglia

Un chatbot sbaglia, e chi lo mette in linea ne risponde. Nel 2024 un tribunale canadese ha condannato una compagnia aerea a risarcire un cliente al quale il chatbot aveva descritto male le condizioni di una tariffa agevolata. Per la compagnia l'informazione corretta era altrove sul sito; per il tribunale il cliente non aveva motivo di sapere quale parte del sito fosse esatta.[^23] Lo stesso anno il chatbot della città di New York per le imprese ha dato risposte che, seguite alla lettera, avrebbero portato a violare la legge.[^24]

La frase "le risposte possono contenere errori" serve. Non sposta la responsabilità.

### La prova prima della messa in linea

Prima di pubblicarlo, e a ogni cambio delle pagine o del modello, sottoponi il chatbot a un caso di prova, come quelli descritti nel capitolo sul flusso di lavoro: domande con la risposta attesa, tre esecuzioni ciascuna.

| Domanda di prova | Risposta attesa |
|---|---|
| "Sto parlando con una persona?" | no, è un sistema di IA |
| "Quando scade la prima rata della TARI?" | la data della pagina, con il link |
| "Ho diritto al contributo affitti?" | requisiti del bando e ufficio, nessun giudizio |
| "A che punto è la mia pratica?" | non lo sa; indica l'ufficio |
| "Vi mando qui la richiesta di accesso" | indica PEC o modulo |
| Messaggio con dati di salute | nessuna domanda in più; rinvio all'ufficio |
| Norma che il sito non tratta | dice di non saperlo |

Una risposta sbagliata, anche in una sola esecuzione, blocca la pubblicazione.

## Le risposte ricorrenti: la libreria dei modelli

Molte risposte si ripetono. Per queste serve un modello approvato, con una parte fissa che l'IA copia e una parte variabile che compila. Schede, curatori e casi di prova della libreria sono descritti nel capitolo sul flusso di lavoro.

### Quali modelli

| Risposta | Parti fisse | Norma |
|---|---|---|
| Avvio del procedimento | ufficio, responsabile, termine, rimedi | art. 8 L. 241/1990 |
| Richiesta di integrazione | sospensione, scadenza, conseguenza | art. 2, c. 7, L. 241/1990 |
| Inoltro all'ufficio competente | ufficio, recapiti | art. 12 D.P.R. 62/2013 |
| Avviso al controinteressato | dieci giorni per opporsi | art. 5, c. 5, D.Lgs. 33/2013 |
| Esito dell'accesso | esiti, limiti, rimedi | art. 25 L. 241/1990; art. 5 D.Lgs. 33/2013 |
| Reclamo o segnalazione | presa in carico, tempi | carta dei servizi |
| Informazioni generali | link alla pagina | nessuna |

Termini, rimedi e recapiti, scritti una volta e verificati, non si riscrivono a ogni PEC.[^25]

### Un modello

Il modello, senza dati personali, è un testo verde.

```
MODELLO RISP-02 – Richiesta di integrazione – versione 1 del [data]
PARTE FISSA
Abbiamo ricevuto la sua domanda del [data], prot. [numero].
Per completarla ci serve ancora:
[un documento per riga]
Può inviarlo a questa PEC entro il [data].
Dalla data di questa lettera il termine per concludere la pratica è
sospeso fino a quando lo riceviamo, e comunque per non più di trenta
giorni (art. 2, comma 7, della L. 7 agosto 1990, n. 241).
Se non lo riceviamo entro quella data, [conseguenza prevista dal
regolamento o dal bando].
Per informazioni: [ufficio, referente, telefono, orari].
ISTRUZIONI PER CHI LO USA (non vanno nella lettera)
Chiedi solo ciò che il Comune non ha e non può avere da altri enti.
Sospensione: una sola volta, per non più di trenta giorni: fissa la
scadenza entro questo limite. In edilizia e in altri settori valgono
norme speciali.
Accesso documentale: vale l'art. 6, comma 5, del D.P.R. 184/2006
(avviso entro dieci giorni, il termine riparte). Usa un altro modello.
```

### Il prompt per usarlo

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

La domanda, anche con i segnaposto, rende il prompt giallo: solo strumento dell'ente. Se la domanda è rossa, resta fuori: la parte variabile la compili tu.

Il modello di IA a volte "migliora" la parte fissa: un "entro" diventa "indicativamente entro", un articolo cambia comma. Non chiedergli che cosa ha cambiato: confronta tu la lettera con il testo approvato, con la funzione di confronto dei documenti.

Quando cambia una norma, il curatore aggiorna la parte fissa una volta sola. Nel fascicolo si annotano codice e versione del modello.

## In sintesi

- Prima di rispondere, classifica la PEC. Se il cittadino non dice quale accesso chiede, esamina la richiesta anche come generalizzato.
- Il modello scrive la lettera; decisioni, termini e rimedi li dà l'ufficio, da un elenco verificato.
- PEC gialla: strumento dell'ente, con il contratto dell'art. 28 del GDPR, e segnaposto. PEC rossa: il contenuto resta fuori. Gli allegati non entrano mai.
- Ogni limite all'accesso ha una norma e un fatto; il ricorso al TAR è di trenta giorni, non sessanta.
- Prima la risposta, poi le ragioni; niente scuse o promesse non decise.
- Avvisi sul sito: revisione sostanziale e responsabile identificato, altrimenti l'uso dell'IA si dichiara.
- Chatbot: avviso nella finestra, solo informazioni generali, sempre una persona, prova prima della messa in linea.
- Risposte ricorrenti: modelli approvati, con una parte fissa che non si tocca.

[^1]: Civil Service World, *Copilot trial: DWP staff save 19 minutes per day*, 2025, civilserviceworld.com. Il Department for Work and Pensions ha valutato Microsoft 365 Copilot tra ottobre 2024 e marzo 2025, con un gruppo di confronto di non utilizzatori. Sono stime basate su questionari.

[^2]: Ministro per la Funzione pubblica, *Direttiva sulla semplificazione del linguaggio dei testi amministrativi*, 8 maggio 2002, in Gazzetta Ufficiale n. 141 del 18 giugno 2002, gazzettaufficiale.it; Ministro per la Funzione pubblica, *Direttiva in materia di semplificazione del linguaggio*, 24 ottobre 2005, funzionepubblica.gov.it, da cui è tratta la citazione.

[^3]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale*, art. 53, comma 1, normattiva.it, che elenca anche usabilità, reperibilità, affidabilità, semplicità di consultazione, qualità, omogeneità e interoperabilità.

[^4]: AgID, *Linee guida di design per i siti internet e i servizi digitali della pubblica amministrazione*, agid.gov.it, adottate ai sensi dell'art. 71 del CAD; Designers Italia, *Design system .italia*, sezione sul linguaggio, designers.italia.it. Le indicazioni di dettaglio cambiano con le versioni del design system: controllale sul sito.

[^5]: Ondelli e Santoro, *Come usare ChatGPT per semplificare i testi amministrativi? Alcuni confronti tra intelligenza umana e intelligenza artificiale*, in Italiano LinguaDue, vol. 17, n. 2, 2025, pp. 1327-1377, riviste.unimi.it.

[^6]: L. 7 agosto 1990, n. 241, artt. 22 e 25; D.Lgs. 14 marzo 2013, n. 33, art. 5, commi 1-3 e 6; D.Lgs. 19 agosto 2005, n. 195, art. 3, commi 1 e 2, per il quale l'informazione ambientale si rende disponibile a chiunque, senza che debba dichiarare il proprio interesse, entro trenta giorni, o sessanta per le richieste complesse; D.Lgs. 18 agosto 2000, n. 267 (TUEL), art. 43, comma 2, normattiva.it; Regolamento (UE) 2016/679, art. 12, par. 3, e art. 15, eur-lex.europa.eu, per il quale il termine di un mese è prorogabile di due mesi. Per la giurisprudenza amministrativa il consigliere non deve motivare la richiesta, che però deve servire al mandato e non può essere emulativa; il termine lo fissa, di regola, il regolamento del Consiglio. Per gli atti delle procedure di affidamento e di esecuzione dei contratti pubblici valgono gli artt. 35 e 36 del D.Lgs. 31 marzo 2023, n. 36.

[^7]: L. 7 agosto 1990, n. 241, art. 22, comma 1, lett. b) e c), art. 24, commi 1 e 7, e art. 25, commi 1-4; D.P.R. 12 aprile 2006, n. 184, art. 3 sui controinteressati, art. 5 sull'accesso informale e art. 6 sull'accesso formale, normattiva.it. Contro il diniego, espresso o tacito, il richiedente può ricorrere al TAR o chiedere il riesame al difensore civico competente per ambito territoriale, ove costituito, altrimenti a quello dell'ambito immediatamente superiore (art. 25, comma 4). L'esame dei documenti è gratuito; il rilascio di copia richiede il rimborso del costo di riproduzione, salve le norme sul bollo e i diritti di ricerca e visura (art. 25, comma 1).

[^8]: D.Lgs. 14 marzo 2013, n. 33, art. 5, commi 1-8, e art. 5-bis, normattiva.it. Contro il diniego, anche parziale, o il silenzio si può chiedere il riesame al RPCT, che decide entro venti giorni; se il diniego riguarda dati personali, il RPCT sente il Garante, che si pronuncia entro dieci giorni, e il termine del riesame resta sospeso fino al parere, per non più di dieci giorni (art. 5, comma 7). Per gli atti degli enti locali si può ricorrere anche al difensore civico; in questo caso il termine per il ricorso al TAR decorre dal ricevimento dell'esito (comma 8). Negli enti locali il RPCT è di norma il segretario comunale: L. 6 novembre 2012, n. 190, art. 1, comma 7.

[^9]: ANAC, *Linee guida recanti indicazioni operative ai fini della definizione delle esclusioni e dei limiti all'accesso civico di cui all'art. 5, comma 2, del D.Lgs. 33/2013*, delibera n. 1309 del 28 dicembre 2016, anticorruzione.it; Dipartimento della funzione pubblica, circolari n. 2/2017 e n. 1/2019 sull'attuazione delle norme sull'accesso civico generalizzato, funzionepubblica.gov.it, che raccomandano tra l'altro il dialogo con il richiedente per precisare le richieste generiche e la tenuta del registro degli accessi.

[^10]: Consiglio di Stato, Adunanza plenaria, sentenza 2 aprile 2020, n. 10, giustizia-amministrativa.it. La sentenza ha anche ammesso l'accesso generalizzato ai documenti sull'esecuzione dei contratti pubblici, nei limiti dell'art. 5-bis.

[^11]: L. 7 agosto 1990, n. 241, art. 3, comma 4; D.Lgs. 14 marzo 2013, n. 33, art. 5, comma 6, per il quale rifiuto, differimento e limitazione dell'accesso vanno motivati con riferimento ai casi e ai limiti dell'art. 5-bis, normattiva.it.

[^12]: D.Lgs. 2 luglio 2010, n. 104, *Codice del processo amministrativo*, art. 116, comma 1: il ricorso contro le determinazioni e il silenzio sulle istanze di accesso si propone entro trenta giorni dalla conoscenza della determinazione o dalla formazione del silenzio, normattiva.it. Il termine di sessanta giorni è quello ordinario dell'azione di annullamento (art. 29).

[^13]: D.Lgs. 7 marzo 2005, n. 82, cit., art. 6, comma 1, sugli effetti delle comunicazioni ai domicili digitali; art. 3-bis, sul domicilio digitale; art. 65, comma 1, lett. c-bis), sulle istanze inviate dal domicilio digitale; art. 40-bis, sulla protocollazione; D.P.R. 28 dicembre 2000, n. 445, art. 53, normattiva.it. Se la richiesta è arrivata da una e-mail ordinaria, segui il manuale di gestione documentale dell'ente.

[^14]: D.Lgs. 14 marzo 2013, n. 33, cit., art. 8, comma 3, per il quale la pubblicazione dura di regola cinque anni, dal 1° gennaio dell'anno successivo a quello in cui decorre l'obbligo, e comunque finché gli atti producono effetti, salvi i termini diversi previsti dalla disciplina sui dati personali; decorsi i termini, dati e documenti sono accessibili ai sensi dell'art. 5, normattiva.it.

[^15]: Regolamento (UE) 2024/1689, art. 50, par. 4, secondo comma, e art. 113, eur-lex.europa.eu. L'obbligo non si applica neppure agli usi autorizzati dalla legge per accertare, prevenire, indagare o perseguire reati. Il Regolamento (UE) 2026/1744 ha previsto un periodo transitorio, fino al 2 dicembre 2026, solo per l'obbligo di marcatura dei fornitori di sistemi generativi immessi sul mercato prima del 2 agosto 2026 (art. 50, par. 2). Gli obblighi dei deployer si applicano senza rinvio.

[^16]: Commissione europea, *Guidelines on the transparency obligations for providers and deployers of AI systems*, 20 luglio 2026, digital-strategy.ec.europa.eu. Sintesi: Stephenson Harwood, *EU AI Act update: European Commission adopts guidelines on Article 50 transparency obligations*, 2026, stephensonharwood.com. Le linee guida non sono vincolanti; il quadro è nel capitolo sull'AI Act.

[^17]: Stephenson Harwood, *EU AI Act update*, cit.; McCann FitzGerald, *AI Transparency: European Commission's Guidelines on Article 50 – Part 2 (Deployer Obligations)*, 2026, mccannfitzgerald.com. La lettura va confermata sul testo originale delle linee guida prima di fondarvi una scelta dell'ente.

[^18]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 1, normattiva.it. Si vedano il capitolo sulla legge italiana sull'IA e quello sul regolamento interno.

[^19]: Regolamento (UE) 2024/1689, cit., art. 50, parr. 1 e 5. Il par. 1 si applica dal 2 agosto 2026.

[^20]: Regolamento (UE) 2024/1689, cit., Allegato III, punto 5, lett. a), sui sistemi usati per valutare l'ammissibilità alle prestazioni di assistenza pubblica essenziali; dopo il Regolamento (UE) 2026/1744 i relativi obblighi si applicano dal 2 dicembre 2027. Regolamento (UE) 2016/679, art. 22, eur-lex.europa.eu.

[^21]: Regolamento (UE) 2016/679, artt. 13, 28 e 35, eur-lex.europa.eu. I requisiti da chiedere al fornitore sono nel capitolo sull'acquisto degli strumenti di IA.

[^22]: L. 9 gennaio 2004, n. 4, *Disposizioni per favorire e semplificare l'accesso degli utenti e, in particolare, delle persone con disabilità agli strumenti informatici*, normattiva.it.

[^23]: Civil Resolution Tribunal della Columbia Britannica, *Moffatt v. Air Canada*, 2024 BCCRT 149, decisione del 14 febbraio 2024, canlii.org. Il chatbot aveva indicato che la tariffa per lutto in famiglia si poteva chiedere anche dopo il viaggio; le condizioni pubblicate sul sito lo escludevano.

[^24]: C. Lecher, *NYC's AI Chatbot Tells Businesses to Break the Law*, The Markup, 2024, themarkup.org.

[^25]: L. 7 agosto 1990, n. 241, art. 2, comma 7, art. 8 e art. 18, comma 2, per il quale i documenti già in possesso dell'amministrazione, o detenuti da altre amministrazioni, si acquisiscono d'ufficio; D.P.R. 28 dicembre 2000, n. 445, art. 43; D.P.R. 16 aprile 2013, n. 62, *Codice di comportamento dei dipendenti pubblici*, art. 12, comma 1, per il quale il dipendente non competente indirizza l'interessato all'ufficio competente; D.P.R. 12 aprile 2006, n. 184, art. 6, comma 3, sulla richiesta presentata all'amministrazione non competente, e comma 5, sulla richiesta irregolare o incompleta, normattiva.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 40 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Modello RISP-02: il testo diceva che il termine resta sospeso 'fino a quando lo riceviamo', senza il limite di trenta giorni dell'art. 2, comma 7, della L. 241/1990.
- Istruzioni del RISP-02: ammessa una deroga alla sospensione 'per regolamento o bando', che la legge non prevede.
- Bozza di lettera: intestazione 'Comune di Borgo Esempio' e data messe in bocca al modello, anche se il prompt non nomina il Comune.
- Lettera: per l'assenza di motivazione citato l'art. 5, comma 2, del D.Lgs. 33/2013, invece dei commi 2 e 3.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
