# GDPR e IA generativa (I): i principi e i dati nel prompt

In questo capitolo: come si applicano al prompt il GDPR e il Codice privacy, cioè chi risponde dei dati, su quale base si trattano, quali restano fuori, che cosa fa davvero un segnaposto, quando la decisione rischia di diventare automatizzata e che cosa cambia in informativa e registro.

## Il prompt è un trattamento

Ai Servizi sociali del Comune di Borgo Esempio arriva la domanda di contributo per l'affitto di una famiglia con tre figli. Nel fascicolo ci sono istanza, attestazione ISEE, contratto di locazione e relazione dell'assistente sociale. Prima di aprire lo strumento di IA, l'istruttrice che prepara la determina deve sapere chi risponde dei dati, su quale base giuridica li tratta e quali possono entrare nel prompt.

Le risposte vengono dal Regolamento (UE) 2016/679 (GDPR) e dal D.Lgs. 30 giugno 2003, n. 196 (Codice in materia di protezione dei dati personali, di seguito Codice), come modificato dal D.Lgs. 10 agosto 2018, n. 101.[^1] Gli articoli senza altra indicazione sono del GDPR. Contratto con il fornitore, trasferimenti, valutazione d'impatto e violazioni dei dati sono trattati nel secondo capitolo sul GDPR e l'IA generativa.

### Dato personale e trattamento

È dato personale "qualsiasi informazione riguardante una persona fisica identificata o identificabile" (art. 4, n. 1). La persona è identificabile anche indirettamente: da un numero, da un luogo, da uno o più elementi della sua identità fisica, economica, culturale o sociale. Perché il dato sia personale non serve il nome. A Borgo Esempio "la famiglia con tre figli che abita sopra la farmacia della piazza" è un dato personale.

Il trattamento è "qualsiasi operazione" sui dati, con o senza processi automatizzati: tra le altre l'estrazione, la consultazione, l'uso e la "comunicazione mediante trasmissione" (art. 4, n. 2). Scrivere dati personali in un prompt è quindi un trattamento: li estrai dal fascicolo, li trasmetti al fornitore, ricevi una bozza che li contiene. Cancellare poi la conversazione riduce la conservazione, ma non annulla la trasmissione.

Vale anche il contrario: un prompt senza dati personali, come la richiesta di un modello generico di determina, non è un trattamento di dati personali. Per questo il metodo del libro parte, quando può, dai testi senza persone. I segnaposto, come si vedrà, riducono il rischio ma non portano il prompt fuori dal GDPR.

### Chi è chi nel Comune

Il titolare del trattamento è chi "determina le finalità e i mezzi" del trattamento (art. 4, n. 7). Nel Comune è l'ente nel suo complesso, non il sindaco o il responsabile di servizio come persone. Lo strumento di IA è uno dei mezzi: sceglierlo spetta al titolare, non al singolo dipendente. Il titolare adotta misure adeguate e deve poter dimostrare che il trattamento è conforme: è la responsabilizzazione (artt. 5, par. 2, e 24).[^2]

Il responsabile del trattamento tratta dati "per conto del titolare" (art. 4, n. 8). Il fornitore di uno strumento di IA lo diventa solo con un contratto che lo vincoli alle istruzioni documentate del Comune (art. 28, par. 3).

Chi scrive il prompt è una persona autorizzata. Chiunque agisca sotto l'autorità del titolare tratta i dati solo se istruito in tal senso (artt. 29 e 32, par. 4). Il Codice consente al titolare di attribuire compiti specifici a persone designate e gli chiede di stabilire come autorizzare chi opera sotto la sua autorità diretta (art. 2-quaterdecies). Nei Comuni senza dirigenti i designati sono di solito i responsabili di servizio incaricati ai sensi dell'art. 109, comma 2, del D.Lgs. 18 agosto 2000, n. 267 (TUEL).[^3]

| Chi | Ruolo | Che cosa decide |
|---|---|---|
| Comune | titolare | strumenti, finalità, regole |
| Responsabile di servizio | designato | applicazione nel servizio |
| Istruttore | autorizzato | uso nei limiti delle istruzioni |
| Fornitore con contratto | responsabile | nulla oltre il contratto |
| Fornitore senza contratto | terzo | le proprie finalità |

Le regole sull'uso dell'IA fanno parte delle istruzioni dell'art. 29: quali strumenti, per quali atti, con quali dati (si veda il capitolo sul regolamento interno). Senza istruzioni scritte il dipendente non ha un perimetro, e il Comune non può dimostrare di averlo istruito.

### Lo strumento non autorizzato

Con un account personale il Comune non ha alcun contratto con il fornitore. I dati del prompt arrivano a un soggetto che li tratta come titolare autonomo, secondo le proprie condizioni d'uso, e che nei piani per consumatori può usarli per addestrare i modelli se l'utente non lo esclude.[^4] Per il Comune è una comunicazione di dati a un terzo, fuori dalle istruzioni e senza base giuridica. Può costituire una violazione di dati personali, cioè una "divulgazione non autorizzata" (art. 4, n. 12), e avere rilievo disciplinare.[^5] Se ti è successo, avvisa subito il responsabile del servizio e il responsabile della protezione dei dati.

Con un account personale, quindi, nel prompt non entra nulla che riporti a una persona: né dati, né segnaposto, né fatti del caso. È la regola già vista nel capitolo sul metodo del prompt.

Anche il fornitore con contratto cambia ruolo se usa i dati per finalità proprie: per quel trattamento è considerato titolare (art. 28, par. 10). Per questo il contratto deve escludere l'addestramento dei modelli sui dati del Comune.

## La base giuridica: il compito pubblico, non il consenso

Un trattamento è lecito solo se ricorre almeno una delle condizioni dell'art. 6, par. 1. Per il Comune che istruisce un procedimento la condizione tipica è la lettera e): il trattamento è "necessario per l'esecuzione di un compito di interesse pubblico o connesso all'esercizio di pubblici poteri di cui è investito il titolare". In alcuni casi concorre la lettera c), l'obbligo di legge, come per la pubblicazione all'albo online.

La base giuridica deve essere stabilita dal diritto dell'Unione o dello Stato membro (art. 6, par. 3). Per il Codice è costituita "da una norma di legge o di regolamento o da atti amministrativi generali" (art. 2-ter, comma 1).[^6] Per il contributo all'affitto è la norma che attribuisce il compito al Comune, con il regolamento comunale.

### L'IA non richiede una base giuridica nuova

Scrivere la bozza con l'IA non cambia la finalità: il Comune tratta i dati per lo stesso procedimento, con un mezzo diverso. Non serve una base giuridica nuova. La L. 23 settembre 2025, n. 132, chiede che l'uso dell'IA garantisca un trattamento lecito, corretto e trasparente e compatibile con le finalità della raccolta (art. 4, comma 2).[^7]

Serve però che ogni operazione sia necessaria. La lettera e) non copre tutto ciò che è utile al compito, ma solo ciò che serve. Se la bozza si scrive con i segnaposto, trasmettere al fornitore il nome della famiglia non è necessario. Qui la base giuridica incontra la minimizzazione.

### Perché non il consenso né il legittimo interesse

Chiedere al cittadino di "acconsentire all'uso dell'intelligenza artificiale" sembra prudente. Non lo è. Il consenso deve essere libero, e il considerando 43 lo esclude quando c'è un evidente squilibrio tra interessato e titolare, "specie quando il titolare del trattamento è un'autorità pubblica". Chi chiede un contributo difficilmente si sente libero di dire no. Il consenso, poi, si può revocare in ogni momento (art. 7, par. 3). E sposta sul cittadino una scelta organizzativa che spetta all'ente.

Il legittimo interesse, a sua volta, "non si applica al trattamento di dati effettuato dalle autorità pubbliche nell'esecuzione dei loro compiti" (art. 6, par. 1, secondo comma). Lavorare più in fretta è un obiettivo dell'art. 14, comma 1, della L. 132/2025, non una base giuridica.

Per chi scrive atti ne derivano tre regole. Nei moduli non compaiono formule di consenso all'uso dell'IA. Nell'informativa la base giuridica resta quella del procedimento. Per le categorie particolari di dati serve in più una condizione dell'art. 9, par. 2.

## Minimizzazione e protezione fin dalla progettazione

Applicati al prompt, i principi dell'art. 5 diventano regole di lavoro.

| Principio (art. 5) | Nel prompt |
|---|---|
| Liceità, correttezza, trasparenza (lett. a) | strumento autorizzato, uso conoscibile |
| Limitazione della finalità (lett. b) | i dati della pratica solo per la pratica |
| Minimizzazione (lett. c) | solo i dati che cambiano la bozza |
| Esattezza (lett. d) | via i dati inventati dal modello |
| Limitazione della conservazione (lett. e) | cronologia breve, memoria spenta |
| Integrità e riservatezza (lett. f) | account dell'ente, accessi controllati |
| Responsabilizzazione (par. 2) | regole scritte, registro aggiornato |

### Solo i dati che cambiano la bozza

I dati devono essere "adeguati, pertinenti e limitati a quanto necessario rispetto alle finalità" (art. 5, par. 1, lett. c)).[^8] Per ogni dato chiediti se cambia il testo della bozza. Il nome del richiedente no; l'importo sì. Il valore dell'ISEE no, se l'ufficio ha già accertato il requisito. La composizione del nucleo no: se il contributo è graduato sui componenti, basta il numero.

Per il contributo all'affitto, la riga Dati dello schema in cinque parti diventa così.

```
Dati: RICHIEDENTE_1 ha presentato l'istanza PROT_1 il [data].
L'ufficio ha accertato i requisiti dell'art. [n] del regolamento
comunale (verbale istruttorio ATTO_1).
Nucleo di [numero] componenti; il contributo è graduato sul numero
dei componenti (art. [n] del regolamento).
Contributo: euro [importo], per i mesi da [mese] a [mese] [anno].
```

Restano fuori nome, codice fiscale, indirizzo, IBAN, valore dell'ISEE e contenuto della relazione sociale. L'elenco completo e la tabella dei segnaposto sono nel capitolo sul metodo del prompt.

### Finalità ed esattezza

La limitazione della finalità (art. 5, par. 1, lett. b)) riguarda anzitutto gli atti usati come esempio. La determina dell'anno scorso mostra struttura e tono, ma i dati della persona a cui si riferiva non servono alla nuova pratica: vanno tolti prima di incollarla. Riguarda poi il fornitore: addestrare i propri modelli sui dati del Comune è una finalità diversa, di un soggetto diverso.

L'esattezza (lett. d)) riguarda anche ciò che il modello aggiunge. Una data, una parentela o un importo inventati, se entrano nell'atto, sono dati inesatti su una persona. Confronta numeri, date e nomi della bozza con il fascicolo (si veda il capitolo sulla verifica).

### Protezione fin dalla progettazione e per impostazione predefinita

L'art. 25 chiede misure adeguate, "quali la pseudonimizzazione", già quando si scelgono i mezzi del trattamento (par. 1). Per impostazione predefinita si trattano solo i dati necessari, per quantità, portata, conservazione e accessibilità (par. 2).[^9]

Per uno strumento di IA questo significa che le impostazioni le decide il Comune, non il singolo utente:

- addestramento sui contenuti escluso, nel contratto e nelle impostazioni;
- memoria tra le conversazioni disattivata, salvo una scelta motivata;
- cronologia conservata per il tempo minimo utile;
- link di condivisione delle conversazioni disattivati;
- collegamenti a posta, cartelle condivise e gestionali attivati solo se servono, perché uno strumento integrato nella suite d'ufficio può leggere i file a cui l'utente ha accesso;[^10]
- accesso solo con l'account dell'ente.

Se la protezione dipende dalla memoria del singolo istruttore, non è "per impostazione predefinita".

## Dati particolari e dati giudiziari

### Le categorie particolari

L'art. 9, par. 1, vieta di trattare dati che rivelino l'origine razziale o etnica, le opinioni politiche, le convinzioni religiose o filosofiche, l'appartenenza sindacale, nonché dati genetici, dati biometrici che identificano in modo univoco una persona, dati relativi alla salute, alla vita sessuale o all'orientamento sessuale. Il divieto cade solo nei casi del par. 2; per il Comune contano soprattutto la lettera b) (lavoro e protezione sociale), la g) (interesse pubblico rilevante) e la h) (assistenza sanitaria o sociale).

Il Codice precisa la lettera g): servono disposizioni che specifichino tipi di dati, operazioni eseguibili, motivo di interesse pubblico e misure a tutela degli interessati (art. 2-sexies, comma 1). Tra le materie di interesse pubblico rilevante elencate dal comma 2 ci sono i benefici economici, le attività socio-assistenziali e sanzionatorie, lo stato civile e l'anagrafe, i rapporti di lavoro. I dati genetici, biometrici e relativi alla salute richiedono anche le misure di garanzia del Garante e "non possono essere diffusi" (art. 2-septies, commi 1 e 8).[^11]

Il divieto copre anche i dati da cui la categoria particolare si deduce: per la Corte di giustizia rientrano nell'art. 9 i dati che rivelano in modo indiretto l'orientamento sessuale, come il nome del convivente in una dichiarazione pubblica.[^12] Una dieta senza carne di maiale in mensa può rivelare una convinzione religiosa; un'esenzione per invalidità, un dato sulla salute.

### Condanne e reati

I dati relativi a condanne penali, reati e misure di sicurezza si trattano solo sotto il controllo dell'autorità pubblica o se il diritto dell'Unione o dello Stato lo autorizza, con garanzie appropriate (art. 10). Per i trattamenti che non avvengono sotto il controllo dell'autorità pubblica, il Codice richiede una norma di legge o, nei casi previsti dalla legge, di regolamento, con garanzie appropriate (art. 2-octies). La nozione è più ampia di quanto sembri: la Corte di giustizia vi ha ricondotto anche i punti di penalità per le infrazioni stradali, per la loro finalità repressiva.[^13]

### I casi tipici di un Comune

| Chi | Pratica | Dato da tenere fuori |
|---|---|---|
| Sociali | contributo con relazione sociale | salute, dipendenze |
| Sociali | dieta speciale in mensa | salute, religione |
| Demografici | unione civile | orientamento sessuale |
| Affari generali | permessi per assistere un familiare | salute |
| Finanziario | trattenuta sindacale in busta paga | appartenenza sindacale |
| Tecnico | verifica dei requisiti in un appalto | condanne e reati |
| Sindaco | ordinanza di trattamento sanitario obbligatorio | salute |

Che il Comune possa trattare questi dati nel procedimento non significa che possa inserirli in un prompt. Anche quella operazione deve essere necessaria, e per scrivere una bozza non lo è quasi mai: al posto del dato basta il requisito o la norma applicata. Per questo, nella regola del semaforo descritta nel capitolo su quale IA usare in ufficio, questi dati sono rossi anche con lo strumento autorizzato. Lo stesso vale per i dati dei minori, che il GDPR protegge in modo specifico (considerando 38). E una bozza con un dato sulla salute può finire all'albo online, dove quel dato non può comparire (si veda il capitolo sulla privacy prima della pubblicazione).

## Anonimizzare o pseudonimizzare

### Due nozioni diverse

I principi del GDPR non si applicano alle informazioni anonime, compresi i dati personali resi "sufficientemente anonimi da impedire o da non consentire più l'identificazione dell'interessato" (considerando 26). Per capire se una persona è identificabile si considerano tutti i mezzi che il titolare o un terzo può "ragionevolmente" usare, tenendo conto di costi, tempo e tecnologie disponibili.

La pseudonimizzazione è un'altra cosa: i dati non si possono più attribuire a una persona senza informazioni aggiuntive, conservate a parte e protette (art. 4, n. 5). Per il considerando 26 i dati pseudonimizzati, che con informazioni aggiuntive si possono attribuire a una persona, sono informazioni su una persona identificabile. Il Gruppo di lavoro Articolo 29 ha indicato i tre rischi che una tecnica di anonimizzazione deve neutralizzare: l'individuazione, cioè isolare una persona; la correlabilità, cioè collegare dati della stessa persona; la deduzione, cioè ricavare un'informazione su di lei.[^14]

### Il segnaposto è pseudonimizzazione

Quando nel prompt scrivi RICHIEDENTE_1 e la corrispondenza con il nome resta nell'ufficio, hai pseudonimizzato. Per il Comune quei dati restano personali, e tutti gli obblighi restano. Lo ribadiscono le linee guida del Comitato europeo per la protezione dei dati (EDPB): la pseudonimizzazione riduce i rischi e aiuta a rispettare i principi, ma non porta il trattamento fuori dal GDPR.[^15] Se poi nel testo restano dettagli che identificano, non c'è nemmeno pseudonimizzazione.

### La sentenza SRB

Il 4 settembre 2025 la Corte di giustizia ha guardato la questione dal lato del destinatario. I dati pseudonimizzati non sono personali in ogni caso e per chiunque: per il destinatario senza mezzi ragionevoli per reidentificare le persone possono non esserlo; per il titolare che conserva le informazioni aggiuntive lo restano. E l'obbligo di informare sui destinatari si valuta dal punto di vista del titolare, al momento della raccolta.[^16] Le conseguenze pratiche sono tre.

1. Per il Comune, che conserva la corrispondenza, i dati pseudonimizzati sono personali: valgono base giuridica, minimizzazione, informativa, registro.
2. Per il fornitore dipende dai mezzi di cui dispone. In un piccolo Comune il nome dell'ente, l'oggetto e la data della pratica, insieme all'albo online, possono bastare per risalire alla persona.
3. La sentenza non autorizza a usare uno strumento senza contratto con dati pseudonimizzati. Dal punto di vista del Comune resta una comunicazione di dati personali.

Il 19 novembre 2025 la Commissione ha proposto di scrivere questa lettura nella definizione di dato personale: è il cosiddetto Digital Omnibus. L'EDPB e il Garante europeo della protezione dei dati hanno chiesto di non farlo. Nei testi di compromesso del Consiglio circolati nel 2026 la nuova definizione non c'è più; al suo posto si discute di un articolo sulla pseudonimizzazione. A ottobre 2026 il negoziato è aperto e l'esito è incerto: non è diritto vigente.[^17]

### La reidentificazione nei piccoli Comuni

Borgo Esempio ha circa 6.500 abitanti, e alcuni contributi vanno a poche famiglie l'anno. "Un nucleo con un solo genitore e un figlio con disabilità, residente in frazione" in un Comune così è una famiglia sola, anche senza nome. Nei piccoli Comuni il rischio più concreto è la deduzione. Al posto del nome del Comune scrivi "un Comune di [numero] abitanti"; togli le date che non servono; generalizza età, frazione, mestiere, carica e parentela; controlla anche allegati e nomi dei file. Il prompt per trovare i dettagli che identificano è nel capitolo sul metodo del prompt. Ma se il testo è anonimo lo decide l'ufficio, non il modello.

### La tabella di corrispondenza

La corrispondenza tra segnaposto e dati veri è l'informazione aggiuntiva dell'art. 4, n. 5: va conservata separatamente e protetta. Il fascicolo della pratica, che contiene già quei dati, è il posto naturale.

```
TABELLA DI CORRISPONDENZA – pratica [numero interno] – RISERVATA
Conservare nel fascicolo. Non copiare in strumenti di IA.
RICHIEDENTE_1 = [nome e cognome]
PROT_1 = [numero e data di protocollo dell'istanza]
ATTO_1 = [estremi del verbale istruttorio]
Compilata da [iniziali] il [data].
```

Non tenerla nella chat né in cartelle che lo strumento può leggere. Non chiedere al modello di sostituire i segnaposto con i dati veri: gli trasmetteresti i dati che hai tolto. Sostituiscili tu, con "trova e sostituisci" o nel sistema documentale dell'ente.

## Decisioni automatizzate e revisione umana

### Il divieto di decisioni solo automatizzate

L'interessato ha il diritto di non essere sottoposto a "una decisione basata unicamente sul trattamento automatizzato, compresa la profilazione, che produca effetti giuridici che lo riguardano o che incida in modo analogo significativamente sulla sua persona" (art. 22, par. 1). Le condizioni sono tre: una decisione; basata unicamente su un trattamento automatizzato; con effetti giuridici o con un'incidenza analoga e significativa. Per un Comune la terza c'è quasi sempre: concedere o negare un contributo, escludere da una graduatoria, irrogare una sanzione.

Il divieto ha tre eccezioni (par. 2): il contratto, il consenso esplicito, l'autorizzazione del diritto dell'Unione o dello Stato con misure adeguate a tutela dell'interessato. Per un Comune le prime due, di regola, non sono praticabili. La terza richiederebbe una norma specifica, e la L. 132/2025 va nella direzione opposta: l'IA ha "funzione strumentale e di supporto all'attività provvedimentale" e la persona "resta l'unica responsabile" (art. 14, comma 2). Sulle categorie particolari di dati le decisioni automatizzate sono ancora più limitate (par. 4).[^18]

### Quando l'output diventa la decisione

Nella sentenza SCHUFA del 7 dicembre 2023 la Corte di giustizia ha letto in senso ampio la parola "decisione": il calcolo automatizzato di un punteggio sulla capacità di una persona di onorare i pagamenti è già una decisione, se un terzo vi fa dipendere in modo decisivo la propria scelta.[^19] Lo stesso ragionamento vale in ufficio. Se il modello classifica quaranta domande come "ammissibili" o "non ammissibili", o ne propone la graduatoria, e l'istruttore la ricopia, l'output è nella sostanza la decisione. La firma non interrompe l'automatismo.

Le linee guida europee sulle decisioni automatizzate chiedono un intervento umano significativo, non simbolico, di chi ha l'autorità e la competenza per cambiare la decisione e considera tutti i dati pertinenti.[^20] L'AI Act, per i sistemi ad alto rischio, dà un nome al pericolo: la "distorsione dell'automazione", cioè la tendenza a fare automaticamente affidamento sull'output del sistema (art. 14, par. 4, lett. b), del Regolamento (UE) 2024/1689).[^21] Sulla decisione algoritmica non esclusiva si veda anche il capitolo sulla legge italiana sull'IA.

Tre segnali che la revisione non è effettiva: hai letto la sintesi del modello e non i documenti originali; la motivazione era scritta prima della decisione; su decine di pratiche non hai mai cambiato l'esito proposto. Anche la sintesi è una scelta: se decidi sul riassunto della relazione sociale, il modello ha scelto che cosa ti è arrivato. L'IA può invece aiutare a scrivere la bozza della motivazione di una decisione già presa. Quella motivazione deve riportare le ragioni vere di chi decide (art. 3 della L. 7 agosto 1990, n. 241).

### Un esempio: il bando per il contributo all'affitto

Borgo Esempio pubblica il bando per il contributo all'affitto e riceve quaranta domande. L'IA, nello strumento autorizzato, può aiutare a controllare la completezza formale. Non valuta i requisiti, non assegna punteggi, non decide chi è ammesso.

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

Il prompt lavora sui nomi dei file, che non devono contenere nomi di persone né rivelare dati sulla salute: "certificato_invalidita" dice già troppo, "allegato_lett_c" no. La tabella che ottieni è un promemoria: poi apri i file, controlli e firmi il verbale. Quando nella richiesta al modello compaiono parole come "ha diritto", "è ammissibile" o "quale punteggio", ti stai avvicinando all'art. 22 e, per le prestazioni di assistenza pubblica essenziali, agli usi ad alto rischio dell'AI Act (si veda il capitolo sull'AI Act).

Per i bandi rivolti alle associazioni l'art. 22 non si applica, perché tutela le persone fisiche. La regola però non cambia: la decisione resta a una persona (art. 14, comma 2, della L. 132/2025).

## Informativa, registro e diritti degli interessati

### L'informativa

L'informativa si dà alla raccolta, se i dati provengono dall'interessato (art. 13), o nei termini dell'art. 14, se provengono da altri. Indica tra l'altro titolare, responsabile della protezione dei dati, finalità, base giuridica, destinatari, trasferimenti, conservazione, diritti ed eventuali decisioni automatizzate (art. 13, par. 2, lett. f)).[^22] Le informative che citano ancora l'art. 13 del D.Lgs. 196/2003, abrogato nel 2018, vanno riscritte (si veda il capitolo sulla verifica delle norme).

Con uno strumento di IA cambiano di solito due voci. La prima sono i destinatari: anche il fornitore nominato responsabile è un destinatario, perché destinatario è chi riceve comunicazione di dati, "che si tratti o meno di terzi" (art. 4, n. 9). Vale anche se gli trasmetti solo dati pseudonimizzati: per la sentenza SRB l'obbligo di informare si valuta dal punto di vista del Comune. La seconda sono i trasferimenti, se il fornitore tratta dati fuori dallo Spazio economico europeo. Finalità e base giuridica non cambiano.

Dichiarare che non ci sono decisioni automatizzate non è obbligatorio, ma è utile. La L. 132/2025 chiede di assicurare agli interessati la "conoscibilità" del funzionamento dell'IA e la "tracciabilità" del suo utilizzo (art. 14, comma 1), con informazioni in linguaggio chiaro e semplice (art. 4, comma 3).[^23] Un paragrafo da adattare con il responsabile della protezione dei dati:

```
Uso di strumenti di intelligenza artificiale. Per preparare le bozze di
alcuni atti il Comune usa [nome dello strumento], fornito da
[fornitore], nominato responsabile del trattamento (art. 28 del
Regolamento (UE) 2016/679). Di regola le bozze si scrivono senza nomi
e senza altri dati che identificano le persone. Il fornitore non può
usare i dati per addestrare i propri modelli. I dati sono trattati
[nell'Unione europea / paese e garanzia del capo V del Regolamento].
Le decisioni sono prese dal personale del Comune: non sono adottate
decisioni basate unicamente su trattamenti automatizzati. Ogni atto è
verificato e firmato da chi ne è responsabile.
```

Aggiorna moduli e pagina dell'informativa sul sito prima di usare lo strumento con dati personali.

### Il registro dei trattamenti

Il Comune tiene sempre il registro delle attività di trattamento: l'esenzione per chi ha meno di 250 dipendenti non vale per i trattamenti non occasionali, per quelli che possono presentare un rischio e per quelli su categorie particolari di dati o su condanne e reati (art. 30, par. 5). Il registro indica, tra l'altro, finalità, categorie di interessati e di dati, destinatari, trasferimenti, termini di cancellazione e, se possibile, una descrizione generale delle misure di sicurezza (art. 30, par. 1).[^24]

Si aggiornano le schede dei procedimenti in cui si usa lo strumento, aggiungendo il fornitore tra i destinatari. Conviene affiancare una scheda trasversale che descrive l'uso dell'IA e rimanda a quelle schede. Un modello:

```
REGISTRO DEI TRATTAMENTI – scheda [n] – aggiornata il [data]
Trattamento: supporto alla redazione di bozze di atti con IA generativa
Titolare: Comune di [nome]. DPO: [contatti]
Servizi: [elenco dei servizi autorizzati]
Finalità: quelle dei procedimenti delle schede [numeri]
Base giuridica: art. 6, par. 1, lett. e), GDPR; norme dei procedimenti
Interessati: richiedenti, beneficiari, contraenti, dipendenti
Dati: di regola pseudonimizzati con segnaposto; esclusi i dati degli
artt. 9 e 10 GDPR e i dati di minori
Destinatari: [fornitore], responsabile ex art. 28 ([estremi contratto])
Trasferimenti fuori dallo SEE: [no / paese e garanzia]
Conservazione: cronologia nello strumento [giorni]; prompt nel
fascicolo, senza dati personali, con i tempi del fascicolo
Misure (art. 32): account dell'ente; addestramento escluso; memoria
disattivata; collegamenti attivi: [quali]; istruzioni al personale
([estremi]); formazione ([estremi])
Decisioni automatizzate (art. 22): nessuna
Valutazione d'impatto: [esito e data]
```

### I diritti degli interessati

Le richieste degli interessati hanno risposta entro un mese, prorogabile di due mesi se necessario (art. 12, par. 3). Con l'IA quattro diritti meritano attenzione.[^25]

*Accesso (art. 15).* Comprende la copia dei dati trattati, anche tramite il responsabile: i prompt con dati della persona nella cronologia dello strumento rientrano nella richiesta. Meno dati metti nel prompt, meno devi cercare. Per le decisioni dell'art. 22 è dovuta anche l'informazione sulla logica del trattamento, che secondo la Corte di giustizia deve spiegare in modo comprensibile la procedura e i principi applicati in concreto.

*Rettifica (art. 16).* Un dato inventato dal modello ed entrato nell'atto è inesatto: si corregge, con un atto di rettifica se l'atto è già adottato, e la correzione si comunica ai destinatari (art. 19).

*Cancellazione (art. 17).* Non si applica quando il trattamento è necessario per un compito di interesse pubblico (par. 3, lett. b)): non c'è un diritto a far sparire la pratica. Resta l'obbligo di non conservare la cronologia oltre il necessario.

*Opposizione (art. 21).* Per i trattamenti basati sulla lettera e) l'interessato può opporsi per motivi connessi alla sua situazione particolare; il titolare prosegue solo se dimostra motivi legittimi cogenti. La L. 132/2025 chiede che le informazioni sui trattamenti connessi all'IA siano rese in linguaggio chiaro e semplice, anche per garantire il diritto di opporsi (art. 4, comma 3). Se un cittadino chiede che la sua pratica "non passi dall'IA", rispondi con il responsabile della protezione dei dati: spiega, se è così, che nel prompt ci sono solo segnaposto e che decide una persona. Di solito l'ufficio può anche scrivere quella bozza senza lo strumento.

Se prompt e risposte siano documenti amministrativi accessibili ai sensi della L. 241/1990 è una questione diversa, trattata nel capitolo sulla tracciabilità.

## In sintesi

- Scrivere dati personali in un prompt è un trattamento. Il Comune, titolare, sceglie lo strumento; chi scrive il prompt segue istruzioni scritte.
- Senza il contratto dell'art. 28 il fornitore è un terzo: dati personali, anche pseudonimizzati, in un account personale sono una comunicazione non autorizzata. Lì non entra nulla che riporti a una persona, nemmeno un segnaposto.
- La base giuridica è quella del procedimento, di regola l'art. 6, par. 1, lett. e): l'IA non ne richiede una nuova. Consenso e legittimo interesse non sono basi valide.
- Nel prompt entra solo ciò che cambia la bozza. Le impostazioni protettive le decide l'ente, non il singolo dipendente.
- Categorie particolari, condanne e reati, dati dei minori restano fuori dal prompt anche con lo strumento autorizzato, compresi i dati da cui si deducono.
- Il segnaposto pseudonimizza, non anonimizza: per il Comune i dati restano personali, e nei piccoli Comuni il rischio principale è la deduzione. La tabella di corrispondenza resta nel fascicolo.
- Nessuna decisione su una persona si fonda sull'output del modello. L'IA aiuta a controllare la completezza formale e a scrivere la bozza della motivazione di una decisione già presa; valutare, assegnare punteggi e ammettere spetta a chi firma, sugli originali.
- Informativa e registro vanno aggiornati prima dell'uso con dati personali: destinatari, trasferimenti, misure, assenza di decisioni automatizzate.

[^1]: Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016, *relativo alla protezione delle persone fisiche con riguardo al trattamento dei dati personali, nonché alla libera circolazione di tali dati e che abroga la direttiva 95/46/CE (regolamento generale sulla protezione dei dati)*, eur-lex.europa.eu, applicabile dal 25 maggio 2018 (art. 99, par. 2); D.Lgs. 30 giugno 2003, n. 196, *Codice in materia di protezione dei dati personali*, come modificato dal D.Lgs. 10 agosto 2018, n. 101, normattiva.it.

[^2]: GDPR, artt. 4, nn. 7 e 8, 5, par. 2, e 24. Sulla distinzione tra titolare, responsabile e persone che agiscono sotto la loro autorità: Comitato europeo per la protezione dei dati (EDPB), *Linee guida 07/2020 sui concetti di titolare del trattamento e di responsabile del trattamento ai sensi del GDPR*, versione 2.0, 2021, edpb.europa.eu.

[^3]: GDPR, artt. 4, n. 10, che esclude dalla nozione di terzo le persone autorizzate sotto l'autorità diretta del titolare, 29 e 32, par. 4; Codice, art. 2-quaterdecies, commi 1 e 2; D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, artt. 107 e 109, comma 2, normattiva.it.

[^4]: Per esempio, con l'aggiornamento dei termini per i consumatori annunciato il 28 agosto 2025, nei piani personali di Claude (Free, Pro e Max) le conversazioni possono essere usate per addestrare i modelli se l'utente non disattiva l'impostazione; i servizi per le organizzazioni e l'uso tramite API ne sono esclusi: Anthropic, *Updates to Consumer Terms and Privacy Policy*, 2025, anthropic.com. Anche gli altri produttori distinguono in genere tra condizioni per consumatori e per organizzazioni: vanno lette, strumento per strumento, alla data d'uso.

[^5]: D.P.R. 16 aprile 2013, n. 62, *Regolamento recante codice di comportamento dei dipendenti pubblici*, art. 11-bis, inserito dal D.P.R. 13 giugno 2023, n. 81; D.Lgs. 30 marzo 2001, n. 165, art. 54, comma 3, per il quale la violazione dei doveri del codice di comportamento è fonte di responsabilità disciplinare, e comma 5, sul codice di comportamento di ciascuna amministrazione, normattiva.it. Sulla gestione della violazione di dati personali e sulla notifica al Garante (artt. 33 e 34 GDPR) si veda il secondo capitolo sul GDPR e l'IA generativa.

[^6]: GDPR, art. 6, parr. 1 e 3, e considerando 45; Codice, art. 2-ter, comma 1, nel testo modificato dal D.L. 8 ottobre 2021, n. 139, convertito con modificazioni dalla L. 3 dicembre 2021, n. 205, normattiva.it.

[^7]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, artt. 4, comma 2, e 14, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it. La legge è in vigore dal 10 ottobre 2025.

[^8]: GDPR, art. 5, par. 1, lett. c). Sulla minimizzazione come regola del prompt si veda anche il capitolo sul metodo del prompt.

[^9]: GDPR, art. 25; EDPB, *Linee guida 4/2019 sull'articolo 25. Protezione dei dati fin dalla progettazione e per impostazione predefinita*, versione 2.0, 2020, edpb.europa.eu.

[^10]: Per esempio, Microsoft 365 Copilot mostra all'utente i contenuti dell'organizzazione per i quali questi ha almeno il permesso di visualizzazione: Microsoft, *Data, Privacy, and Security for Microsoft 365 Copilot*, 2026, learn.microsoft.com. Permessi troppo larghi su cartelle condivise diventano così un problema di riservatezza.

[^11]: GDPR, art. 9, parr. 1 e 2, lett. b), g) e h); Codice, artt. 2-sexies, commi 1 e 2, e 2-septies, commi 1 e 8, normattiva.it.

[^12]: Corte di giustizia dell'Unione europea, Grande Sezione, sentenza 1° agosto 2022, causa C-184/20, *OT c. Vyriausioji tarnybinės etikos komisija*, curia.europa.eu.

[^13]: GDPR, art. 10; Codice, art. 2-octies; Corte di giustizia dell'Unione europea, Grande Sezione, sentenza 22 giugno 2021, causa C-439/19, *Latvijas Republikas Saeima (Punti di penalità)*, curia.europa.eu. Negli appalti la verifica delle cause di esclusione, che comprende le condanne, è disciplinata dall'art. 94 del D.Lgs. 31 marzo 2023, n. 36, normattiva.it.

[^14]: GDPR, considerando 26 e art. 4, n. 5; Gruppo di lavoro Articolo 29 per la protezione dei dati, *Parere 05/2014 sulle tecniche di anonimizzazione* (WP216), 2014, ec.europa.eu.

[^15]: EDPB, *Guidelines 01/2025 on Pseudonymisation*, versione adottata il 16 gennaio 2025 per la consultazione pubblica, edpb.europa.eu.

[^16]: Corte di giustizia dell'Unione europea, sentenza 4 settembre 2025, causa C-413/23 P, *Garante europeo della protezione dei dati c. Comitato di risoluzione unico (SRB)*, curia.europa.eu. La sentenza interpreta il Regolamento (UE) 2018/1725, che si applica alle istituzioni e agli organi dell'Unione e usa nozioni di dato personale e di pseudonimizzazione corrispondenti a quelle del GDPR.

[^17]: Commissione europea, proposta di regolamento COM(2025) 837 del 19 novembre 2025, eur-lex.europa.eu. L'EDPB e il Garante europeo della protezione dei dati hanno adottato un parere congiunto sulla proposta nel febbraio 2026. Sui testi di compromesso del Consiglio, che tolgono la nuova definizione e propongono un nuovo articolo sulla pseudonimizzazione dopo l'art. 29, e sullo stato del negoziato: IAPP, *EU member states' leaked Digital Omnibus compromise proposal eliminates revised GDPR definition of personal data*, 2026, iapp.org; EU Perspectives, *How the EU nearly weakened the world's toughest data protection law*, 2026, euperspectives.eu; PrivacyNext, *Digital Omnibus (GDPR) Negotiations at the Council: September 2026 update*, 2026, privacynext.eu. Sono fonti secondarie su documenti non definitivi: lo stato dell'iter va controllato su eur-lex.europa.eu alla data di lettura. La parte sull'IA dello stesso pacchetto è diventata il Regolamento (UE) 2026/1744, descritto nel capitolo sull'AI Act.

[^18]: GDPR, art. 22, parr. 1, 2 e 4, e considerando 71; L. 132/2025, cit., art. 14, comma 2.

[^19]: Corte di giustizia dell'Unione europea, sentenza 7 dicembre 2023, causa C-634/21, *SCHUFA Holding (Scoring)*, curia.europa.eu.

[^20]: Gruppo di lavoro Articolo 29 per la protezione dei dati, *Linee guida sul processo decisionale automatizzato relativo alle persone fisiche e sulla profilazione ai fini del regolamento 2016/679* (WP251 rev.01), 2018, ec.europa.eu. Le linee guida sono state fatte proprie dall'EDPB.

[^21]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, art. 14, par. 4, lett. b), eur-lex.europa.eu. L'art. 14 riguarda i sistemi ad alto rischio e, per quelli dell'Allegato III, si applica dal 2 dicembre 2027, secondo l'art. 113 come modificato dal Regolamento (UE) 2026/1744. Sulla decisione algoritmica non esclusiva: Consiglio di Stato, sez. VI, sentenza 13 dicembre 2019, n. 8472, giustizia-amministrativa.it.

[^22]: GDPR, artt. 4, n. 9, 13 e 14. L'art. 13 del D.Lgs. 196/2003 è stato abrogato dall'art. 27 del D.Lgs. 101/2018, cit.

[^23]: L. 132/2025, cit., artt. 4, comma 3, e 14, comma 1. La tracciabilità dell'uso nel fascicolo è trattata nel capitolo sulla tracciabilità.

[^24]: GDPR, art. 30, parr. 1 e 5; Garante per la protezione dei dati personali, *FAQ sul registro delle attività di trattamento*, 2018, garanteprivacy.it.

[^25]: GDPR, artt. 12, par. 3, 15, 16, 17, par. 3, lett. b), 19 e 21; L. 132/2025, cit., art. 4, comma 3; Corte di giustizia dell'Unione europea, sentenza 27 febbraio 2025, causa C-203/22, *Dun & Bradstreet Austria*, curia.europa.eu, sull'informazione relativa alla logica delle decisioni automatizzate (art. 15, par. 1, lett. h)).

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 30 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- L'esempio sull'art. 22 GDPR usava un bando per associazioni sportive, ma l'art. 22 tutela solo le persone fisiche: ora è il bando per il contributo all'affitto, con una frase sulle associazioni (vale l'art. 14, comma 2, L. 132/2025).
- Il prompt dell'esempio sul bando scriveva 'Comune di [nome]' in una pratica su persone, contro la regola del capitolo sul metodo: ora è 'un Comune di [numero] abitanti'.
- 'Cancellare la conversazione non cambia nulla' era impreciso: riduce la conservazione, ma non annulla la trasmissione.
- Sui dati dell'art. 9 il testo diceva che la base giuridica 'non copre in automatico la trasmissione' al fornitore: è giuridicamente impreciso, perché il responsabile tratta per conto del titolare.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
