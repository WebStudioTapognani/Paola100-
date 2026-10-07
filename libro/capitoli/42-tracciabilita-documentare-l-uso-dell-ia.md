# Tracciabilità: documentare l'uso dell'IA negli atti

In questo capitolo: la nota nel fascicolo, il registro degli usi, le formule nell'atto, l'accesso a prompt e risposte, la conservazione, i ruoli e i tempi, per rendere tracciabile e conoscibile l'uso dell'IA come chiede l'art. 14 della L. 132/2025.

## Cosa significa tracciabilità per chi scrive atti

La L. 23 settembre 2025, n. 132, chiede alle pubbliche amministrazioni di usare l'IA "assicurando agli interessati la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo" (art. 14, comma 1).[^1] La legge non dice come: non prevede registri, formule o tempi di conservazione. Le soluzioni di questo capitolo sono una proposta operativa, coerente con la norma e con le regole sul fascicolo e sull'accesso, non l'unica lettura possibile.

In questo libro le due parole hanno un campo diverso. La conoscibilità riguarda l'ente: per quali attività il Comune usa l'IA, con quali strumenti e con quali regole. La legge la deve agli interessati, e il modo più semplice di assicurarla è renderla pubblica. La tracciabilità riguarda il singolo atto: chi lo esamina deve poter ricostruire che cosa ha fatto lo strumento e che cosa ha fatto la persona. Non va confusa con la tracciabilità dei flussi finanziari della L. 13 agosto 2010, n. 136:[^2] nel gestionale degli atti usa un'etichetta diversa, come "uso dell'IA".

### Tre domande per ogni atto

Per ogni atto in cui è stata usata l'IA, il fascicolo risponde a tre domande.

1. Che cosa ha fatto l'IA? In quale fase, con quale strumento, quale prompt e quali materiali.
2. Che cosa ha fatto la persona? Chi ha verificato fatti e norme, con quale esito, che cosa ha cambiato.
3. Che cosa è rimasto? Il prompt, la risposta usata, le verifiche.

Se le risposte sono solo nella memoria di chi ha lavorato, la tracciabilità non c'è.

### A che cosa serve

A chi firma, prima di tutto: sapere che una bozza viene dall'IA, e da quale prompt, dice dove guardare (si veda il capitolo sul metodo del prompt).

Al segretario comunale, nel controllo successivo di regolarità amministrativa sugli atti estratti a campione (art. 147-bis, comma 2, del D.Lgs. 18 agosto 2000, n. 267, TUEL).[^3]

Al Comune davanti al giudice. Per il Consiglio di Stato la decisione algoritmica deve essere conoscibile e non esclusiva: serve un contributo umano capace di controllare, validare o smentire la decisione automatica.[^4] Nel 2026 il TAR Marche ha respinto la censura di chi sosteneva che la relazione istruttoria del RUP fosse scritta con l'IA: ha guardato se la decisione restava controllata, motivata e imputabile al funzionario e all'amministrazione.[^5] Un fascicolo con bozza, verifiche e correzioni risponde a quella domanda prima del giudice.

All'ente, quando qualcosa va storto. Se un prompt della libreria conteneva una norma sbagliata, il registro dice in quali atti è stato usato: è un richiamo, come per un prodotto difettoso. Senza registro, si rileggono tutti gli atti dell'anno.

### Che cosa si traccia

Si traccia ogni uso il cui risultato entra, anche in parte, in un atto, in un documento del fascicolo o in un testo che esce dal Comune. Non si traccia l'uso per studio o per esercitazione su casi inventati.

| Uso | Si traccia? | Dove |
|---|---|---|
| Bozza o sintesi per un atto | sì | nota e registro |
| Controllo privacy prima della pubblicazione | sì, senza copiare i dati | nota e registro |
| Risposta a un cittadino o a una PEC | sì | nota e registro |
| Avviso o notizia per il sito | sì, con chi ha approvato | registro |
| Ricerca di una norma | sì, se entra nell'atto | scheda di verifica |
| Esercitazione su un caso inventato | no | nessuno |

Per avvisi e notizie conta chi ha approvato il testo. Il deployer che pubblica un testo generato o manipolato dall'IA per informare il pubblico su questioni di interesse pubblico deve dichiararlo. L'obbligo non si applica se il testo è stato sottoposto a revisione umana o a controllo editoriale e una persona fisica o giuridica ne ha la responsabilità editoriale (art. 50, par. 4, dell'AI Act).[^6] Il registro prova la revisione (si veda il capitolo sull'AI Act).

## Nel fascicolo: la nota di tracciabilità

### Che cosa conservare

Il fascicolo informatico raccoglie "gli atti, i documenti e i dati del procedimento medesimo da chiunque formati" (art. 41, comma 2, del D.Lgs. 7 marzo 2005, n. 82, CAD).[^7] La norma non parla di bozze. Ma la bozza prodotta dall'IA e usata per l'atto mostra come l'atto si è formato: conviene conservarla. Nel fascicolo vanno:

- il prompt compilato, così come è stato inviato;
- la risposta da cui viene la bozza, così come l'ha prodotta lo strumento;
- la scheda di verifica dei riferimenti normativi (si veda il capitolo sulla verifica delle norme);
- la nota di tracciabilità, che tiene insieme il resto.

Se il prompt viene dalla libreria dell'ente e si compila solo con documenti già nel fascicolo, bastano codice e versione (si veda il capitolo sul flusso di lavoro). Non servono tutti i tentativi: conserva la richiesta da cui viene la bozza usata e annota quante volte hai riprovato.

Il prompt si archivia con i segnaposto; la tabella di corrispondenza con i dati veri resta nel file separato e protetto (si veda il capitolo sul metodo del prompt). Esporta prompt e risposta in un formato adatto alla conservazione indicato dal manuale di gestione documentale, come il PDF/A.

### Il modello

```
NOTA DI TRACCIABILITÀ DELL'USO DELL'IA
Fascicolo: [classificazione e numero]
Atto: [tipo e oggetto]; n. [numero] del [data], dopo l'adozione
Responsabile del procedimento: [nome]

1. Strumento: [nome commerciale]; utenza dell'ente [identificativo]
2. Modello indicato dallo strumento, se visibile: [indicazione]
3. Date d'uso: [date]; conversazioni: [n]; tentativi: [n]
4. Fasi: [sintesi / bozza / revisione della lingua /
   controllo privacy / risposta al cittadino]
5. Prompt: [codice e versione della libreria]; testo: doc. [n]
6. File di stile: versione [n]. Elenco delle norme: [nome],
   verificato il [data]
7. Materiali forniti: [documenti del fascicolo, per numero]
8. Dati nel prompt: [nessun dato personale / segnaposto]
9. Risposta dell'IA conservata: doc. [n]
10. Verifiche: scheda dei riferimenti, doc. [n]; segnalazioni
    VERIFICARE nella bozza: [n]; tutte risolte: [sì / no]
11. Modifiche sostanziali alla bozza: [sintesi in due righe]
12. Cronologia nello strumento: cancellata il [data]

Compilata da [nome e ruolo] il [data]
Vista dal responsabile del servizio il [data]
```

Il punto 2 serve perché lo strumento cambia modello nel tempo, e lo stesso prompt può dare risultati diversi. Il punto 11 è il più utile davanti a un giudice: mostra che la bozza è stata esaminata e corretta, non solo firmata.

Chi firma legge la nota prima dell'atto. Se il punto 10 è vuoto, o le segnalazioni non sono tutte risolte, la bozza non è stata verificata: l'atto non è pronto. Se è vuoto il punto 9, manca la prova di che cosa ha prodotto lo strumento.

### Farsi aiutare a compilarla

A fine conversazione il modello può elencare le tue richieste. Confronta l'elenco con la cronologia: nelle conversazioni lunghe può perdere o confondere i passaggi iniziali.

```
Fine del lavoro su questa pratica. Non riscrivere nulla.
Elenca in ordine le mie richieste in questa conversazione.
Per ognuna una riga: numero, che cosa ti ho chiesto in sintesi,
quali testi o documenti ti ho fornito (titolo, non contenuto).
Indica quali tue risposte contengono una bozza completa.
Non riportare dati né segnaposto. Non valutare il lavoro svolto.
Se non sei sicuro di una richiesta, scrivi [VERIFICARE: richiesta n].
```

## Il registro degli usi: campi minimi, chi lo tiene, quanto si conserva

La nota descrive un atto. Il registro li elenca tutti, una riga per pratica, con il rimando alla nota. Risponde in pochi minuti a domande che altrimenti richiedono giorni: quanti atti, quali servizi, quali prompt, quali versioni.

### I campi minimi

```
REGISTRO DEGLI USI DELL'IA – Servizio [nome] – anno [anno]
Una riga per pratica. Nessun dato delle persone del procedimento.

1. Numero progressivo; data dell'uso
2. Fascicolo: classificazione e numero
3. Atto o documento: tipo; numero e data dopo l'adozione
4. Fasi: sintesi / bozza / lingua / privacy / risposta / sito
5. Strumento e utenza dell'ente
6. Prompt: codice e versione della libreria, oppure "libero"
7. Dati nel prompt: nessuno / segnaposto
8. Scheda di verifica dei riferimenti: sì / non serve
9. Nota di tracciabilità nel fascicolo: sì
10. Solo per i testi del sito: approvato da [ruolo] il [data]
```

Il campo 6 è quello del richiamo. Il campo 7 mostra al responsabile della protezione dei dati (DPO) dove c'erano persone. Il campo 10 prova la revisione umana dei testi informativi.

Il campo 7 ha due sole risposte. Se nel prompt sono finiti nomi, codici fiscali o altri identificativi, o dati sulla salute, su reati o di minori, non è un dato da registrare. È una violazione delle regole dell'ente, da segnalare subito al responsabile e al DPO, che valutano se è anche una violazione di dati personali (si veda il capitolo sul GDPR dedicato ai fornitori e agli incidenti).

Il registro più semplice è un foglio di calcolo nella cartella del servizio, con accesso limitato. Meglio, se il gestionale degli atti lo consente, un campo "uso dell'IA" nella scheda dell'atto, con la nota allegata: il registro si ricava da una ricerca.

### Chi lo tiene

Compila la riga chi ha usato lo strumento, quando la bozza è pronta. Il responsabile del servizio la controlla con la nota prima della firma, e risponde del registro del proprio servizio. Il segretario comunale e il responsabile della protezione dei dati lo consultano quando serve.

Una volta l'anno il responsabile per la transizione al digitale (RTD) confronta i numeri complessivi dello strumento, se la console li fornisce, con quelli del registro, per servizio e mai per persona. In un servizio con un solo addetto anche il dato per servizio riguarda una persona: serve a verificare la regola, non a valutare chi lavora. Non tutto l'uso si registra, perché studio ed esercitazioni restano fuori. Ma centinaia di conversazioni a fronte di dieci righe di registro sono un segnale: probabilmente la regola non è applicata.

### Quanto si conserva

Il registro è un documento del Comune. Quanto conservarlo lo stabilisce il piano di conservazione, integrato con il sistema di classificazione, che il servizio per la gestione dei flussi documentali e degli archivi elabora e aggiorna (artt. 61 e 68, comma 1, del D.P.R. 28 dicembre 2000, n. 445).[^8] Chiedi al responsabile di quel servizio di inserire una voce per registro e note; finché manca, conserva il registro almeno quanto i fascicoli a cui rimanda. Lo stesso vale per la libreria dei prompt: una versione ritirata non si cancella finché esiste un atto che la cita.

## Nell'atto: formule di trasparenza e loro effetti

### Due scelte

Al 6 ottobre 2026 nessuna norma chiede di scrivere nell'atto che è stata usata l'IA (si veda il capitolo sulla legge italiana). Il decreto legislativo attuativo della L. 132/2025, approvato in via definitiva dal Consiglio dei ministri il 4 agosto 2026, riguarda anche la pubblica amministrazione. Alla chiusura del volume le fonti consultate non ne riportano la pubblicazione: leggi il testo definitivo e controlla se aggiunge obblighi di questo tipo.[^9]

Il Comune può scegliere tra due soluzioni.

- La scelta minima: la traccia resta nel fascicolo e nel registro; il sito dichiara in generale come il Comune usa l'IA.
- La scelta più trasparente: in più, una formula in calce agli atti la cui bozza è stata preparata con l'IA.

La scelta si fa una volta per tutto l'ente, nel regolamento interno, non ufficio per ufficio. Borgo Esempio, per il primo anno, ha scelto la soluzione minima (si veda il capitolo sul regolamento interno).

### La formula

```
Uso dell'intelligenza artificiale. Per preparare la bozza di questo
atto il [servizio] ha usato uno strumento di intelligenza artificiale
autorizzato dal Comune, a supporto dell'istruttoria (art. 14 della
L. 23 settembre 2025, n. 132). Il contenuto è stato verificato dal
responsabile del procedimento. L'uso è documentato nel fascicolo.
```

Va in calce, dopo il dispositivo e separata da esso: non è una premessa, non è una motivazione, non dispone nulla. Non contiene nomi di persone né il nome del prodotto, che può cambiare: quello è nella nota.

Evita "atto generato con l'intelligenza artificiale": è falso, perché l'atto lo adotta chi firma e l'IA ha prodotto una bozza. Evita anche "verificato con l'intelligenza artificiale", che sposta la fiducia sullo strumento, e le percentuali ("redatto al 70% con l'IA"), che nessuno sa misurare.

### Gli effetti

*Sulla validità.* La formula non è un requisito di validità dell'atto: nessuna norma la prescrive.

*Sulla responsabilità.* Non la sposta. La persona "resta l'unica responsabile" dei provvedimenti e dei procedimenti in cui è stata usata l'IA (art. 14, comma 2, della L. 132/2025).

*Sulla coerenza.* Se il Comune la adotta, la usa sempre nei casi previsti: altrimenti un atto senza formula fa pensare che l'IA non sia stata usata.

*Sull'accesso.* La formula può attirare richieste di accesso. È l'effetto voluto della conoscibilità, ma il fascicolo deve reggerle: introduci la formula quando note e registro funzionano.

### Fuori dall'atto: la pagina sul sito

La legge non chiede di spiegare come funziona un modello linguistico: nessun Comune potrebbe farlo. La lettura più ragionevole è che chieda di rendere conoscibile come il Comune lo usa (si veda il capitolo sulla legge italiana). Basta una pagina breve, collegata all'informativa (si veda il capitolo sui principi del GDPR): strumenti autorizzati, attività, dati esclusi, controlli, a chi chiedere.

Il regolamento interno e i suoi allegati si pubblicano in "Amministrazione trasparente", tra gli atti che dispongono in generale sull'organizzazione e sui procedimenti (art. 12, comma 1, del D.Lgs. 14 marzo 2013, n. 33).[^10]

## Prompt e risposte sono documenti amministrativi? Accesso e conservazione

### La definizione

Per l'art. 22, comma 1, lett. d), della L. 7 agosto 1990, n. 241, è documento amministrativo "ogni rappresentazione grafica, fotocinematografica, elettromagnetica o di qualunque altra specie del contenuto di atti, anche interni o non relativi ad uno specifico procedimento, detenuti da una pubblica amministrazione e concernenti attività di pubblico interesse".[^11] Prompt e risposta conservati nel fascicolo hanno tutti i requisiti: rappresentano in forma informatica il contenuto di atti, anche interni; il Comune li detiene; riguardano un'attività di pubblico interesse, il procedimento.

La giurisprudenza va nella stessa direzione. Nel 2017 il TAR Lazio ha riconosciuto l'accesso al codice sorgente dell'algoritmo usato per la mobilità dei docenti, qualificandolo come documento amministrativo informatico.[^12] Se è accessibile il codice sorgente di un algoritmo, è difficile sostenere che non lo sia un prompt scritto in italiano e conservato nel fascicolo.

Il diritto di accesso, però, non obbliga a creare documenti: riguarda quelli materialmente esistenti al momento della richiesta, e l'amministrazione non è tenuta a elaborare dati (art. 2, comma 2, del D.P.R. 12 aprile 2006, n. 184; art. 22, comma 4, della L. 241/1990).[^13] Ma l'art. 14 della L. 132/2025 chiede di assicurare la tracciabilità. Lette insieme, le due regole dicono: documenta prima, non quando arriva la richiesta.

### Dove stanno prompt e risposte

| Dove | È un documento del Comune? | Che cosa fare |
|---|---|---|
| Fascicolo | sì | conservare con il fascicolo |
| Cronologia, utenza dell'ente | probabile, ma discusso | copiare nel fascicolo, poi cancellare |
| Account personale | no, il Comune non lo controlla | solo se autorizzato; copiare subito |

La cronologia nell'utenza dell'ente è nella disponibilità del Comune, tramite il fornitore. Se sia "detenuta" ai fini dell'accesso non è chiarito: finché esiste, conviene trattarla come tale. Ciò che serve si copia nel fascicolo, il resto si cancella nei tempi fissati dall'ente; ma quando arriva una richiesta di accesso, non si cancella nulla che la riguardi finché il procedimento non è chiuso.

L'account personale è fuori dal controllo del Comune. Per il lavoro si usa solo se l'ente lo ammette per iscritto, e mai con dati personali, nemmeno come segnaposto. Ciò che entra nell'atto si copia subito nel fascicolo (si veda il capitolo su quale IA usare).

### Le richieste di accesso

Le regole sono quelle descritte nel capitolo sulle risposte a cittadini e PEC. Con l'IA si presentano quattro situazioni.

*Accesso documentale.* Chi ha un interesse diretto, concreto e attuale può chiedere nota, prompt e bozza del proprio procedimento; chi vi partecipa può prendere visione degli atti (art. 10 della L. 241/1990). Durante l'istruttoria l'accesso alle bozze si può differire, se conoscerle può compromettere il buon andamento dell'azione amministrativa (art. 9, comma 2, del D.P.R. 184/2006). Non sono ammesse richieste preordinate a un controllo generalizzato dell'operato dell'amministrazione.[^14]

*Accesso civico generalizzato.* Chiunque può chiedere prompt, note e registro, senza motivare, nei limiti dell'art. 5-bis del D.Lgs. 33/2013, a partire dalla protezione dei dati personali. Il Comune rilascia ciò che ha, senza elaborazioni nuove; per le richieste molto ampie le indicazioni nazionali raccomandano il dialogo con il richiedente.[^15]

*Consigliere comunale.* Ha diritto a tutte le notizie e informazioni utili all'espletamento del mandato (art. 43, comma 2, TUEL), compreso il registro.[^16]

*Interessato.* Se nel prompt c'erano suoi dati, ha diritto di averne copia (art. 15 del Regolamento (UE) 2016/679, GDPR; si veda il capitolo sui principi del GDPR).

Prima di rilasciare un prompt, controlla che non contenga dati personali. Se contiene solo segnaposto c'è meno da oscurare, ma i segnaposto non rendono anonimo il testo: luoghi, date e fatti del caso possono ancora far riconoscere una persona (si veda il capitolo sul metodo del prompt).

### Conservazione e scarto

Gli archivi e i singoli documenti degli enti pubblici territoriali sono beni culturali, e il loro scarto richiede l'autorizzazione del Ministero della cultura, tramite le Soprintendenze archivistiche (artt. 10, comma 2, lett. b), e 21, comma 1, lett. d), del D.Lgs. 22 gennaio 2004, n. 42).[^17] Prompt, bozza e nota entrati nel fascicolo si conservano e si scartano con il fascicolo, secondo il piano di conservazione e il manuale di gestione documentale previsti dalle Linee guida AgID sui documenti informatici.[^18]

La cronologia nello strumento è un'altra cosa. Se la copia utile è nel fascicolo, la cronologia è un duplicato di lavoro: si cancella nei tempi, di regola brevi, fissati dall'ente con il responsabile della protezione dei dati. Il GDPR chiede di conservare i dati personali solo per il tempo necessario, salvo l'archiviazione nel pubblico interesse con le garanzie dell'art. 89 (art. 5, par. 1, lett. e)).[^19] Se la copia non è nel fascicolo, cancellare la cronologia significa perdere l'unica traccia. Per questo il punto 12 della nota registra la cancellazione: prima si copia, poi si cancella.

Cancellare la cronologia dall'interfaccia non sempre cancella subito i dati presso il fornitore. I suoi tempi di conservazione si leggono nel contratto (si veda il capitolo sul GDPR dedicato ai fornitori).

Per i sistemi ad alto rischio l'AI Act chiederà al deployer di conservare i log generati automaticamente, nella misura in cui sono sotto il suo controllo, per almeno sei mesi, salvo diversa disposizione del diritto dell'Unione o nazionale (art. 26, par. 6).[^20] Un chatbot per le bozze non è ad alto rischio, ma la logica vale: ciò che ricostruisce l'uso sta dove l'ente lo controlla.

## Tracciare senza schedare: non registrare più dati del necessario

La tracciabilità riguarda l'uso dell'IA, non le persone. Vanno protetti due gruppi: le persone del procedimento e i dipendenti. Il principio è la minimizzazione: dati "adeguati, pertinenti e limitati a quanto necessario" (art. 5, par. 1, lett. c), GDPR).

### Le persone del procedimento

- Il registro non contiene nomi, codici fiscali, indirizzi né oggetti che identificano: rimanda al fascicolo per numero. "Contributo per l'affitto, fascicolo 45/2026" basta.
- La copia del prompt nel fascicolo è quella con i segnaposto; la tabella di corrispondenza non si allega.
- Per il controllo privacy prima della pubblicazione, la nota riporta data, strumento ed esito, non i dati trovati (si veda il capitolo sulla privacy prima della pubblicazione).

### I dipendenti

Il registro contiene, per forza, chi ha usato lo strumento: è un dato personale del dipendente, ed è necessario. Il problema nasce quando registro e log dello strumento diventano un modo per controllare il lavoro delle persone.

Lo Statuto dei lavoratori si applica anche al Comune, qualunque sia il numero dei dipendenti. Lo strumento con cui si scrive la bozza è, di regola, uno strumento usato per rendere la prestazione: non richiede l'accordo sindacale previsto per gli strumenti da cui deriva anche la possibilità di controllo a distanza (art. 4, comma 2). Le funzioni di monitoraggio della console sono un'altra cosa. Se permettono di controllare l'attività delle persone, ricadono nel comma 1: servono esigenze specifiche e l'accordo con le rappresentanze sindacali o, in mancanza, l'autorizzazione dell'Ispettorato del lavoro. Valuta il confine con il DPO prima dell'avvio. In ogni caso le informazioni raccolte sono utilizzabili ai fini del rapporto di lavoro solo se il dipendente è stato adeguatamente informato sulle modalità d'uso degli strumenti e sui controlli, e nel rispetto delle norme sulla protezione dei dati (art. 4, comma 3, della L. 20 maggio 1970, n. 300).[^21]

Per i metadati della posta elettronica il Garante per la protezione dei dati personali ha indicato nel 2024 una conservazione non superiore a 21 giorni; oltre, e solo per esigenze comprovate, servono le garanzie dell'art. 4, comma 1, dello Statuto.[^22] I log di uno strumento di IA non sono metadati di posta, ma il criterio aiuta: ciò che lo strumento registra da solo si conserva per il tempo che serve alla sicurezza.

Quattro regole.

1. Nel registro c'è l'utenza, non giudizi: niente tempi individuali, niente errori attribuiti a una persona. Tempi ed errori vanno nel registro del metodo, senza nomi (si veda il capitolo sul flusso di lavoro).
2. Il regolamento interno dichiara le finalità: tracciabilità degli atti, controlli, sicurezza; non la valutazione della prestazione individuale. I dati raccolti per uno scopo non si usano per uno scopo incompatibile (art. 5, par. 1, lett. b), GDPR).
3. I log della console li consulta solo l'RTD o l'amministratore di sistema, per sicurezza e incidenti, per un tempo definito.
4. Prima dell'avvio i dipendenti ricevono un'informativa su registro, note e log.

Prima di aggiungere un campo al registro, chiediti se serve a ricostruire l'atto, se è già scritto altrove, se riguarda una persona. Se le risposte sono no, sì e sì, il campo non serve.

## Ruoli, approvazione e tempi

### Chi fa che cosa

| Chi | Che cosa fa | Quando |
|---|---|---|
| Istruttore | nota, copie nel fascicolo, riga del registro | a ogni atto |
| Responsabile del servizio | controlla nota e registro, poi firma | a ogni atto |
| Segretario comunale | verifica la nota negli atti estratti | controlli successivi |
| RTD | impostazioni, cronologia, log, libreria | all'avvio e a ogni modifica |
| Gestione documentale | classificazione e piano di conservazione | all'avvio, poi ogni anno |
| DPO | parere su campi, tempi e informative | all'avvio e su richiesta |
| Giunta | approva il regolamento interno | all'avvio e alle revisioni |

A Borgo Esempio l'RTD è il responsabile del Servizio Affari generali, che cura anche protocollo e archivio; il DPO è un professionista esterno, condiviso con altri Comuni. Il segretario aggiunge alla griglia dei controlli successivi una domanda: se l'atto è stato preparato con l'IA, la nota c'è ed è completa?

### L'articolo del regolamento

Il regolamento interno sull'uso dell'IA (si veda il capitolo sul regolamento interno) dedica un articolo alla tracciabilità. Il modello di quel capitolo lo tiene in due commi; questa è una versione più completa, che lo può sostituire.

```
Art. [n] – Tracciabilità
1. Ogni uso dell'IA il cui risultato entra, anche in parte, in un
   atto, in un documento del fascicolo o in un testo destinato
   all'esterno è annotato nel registro degli usi (allegato [n]) e,
   se riguarda un procedimento, documentato nel fascicolo con la
   nota di tracciabilità (allegato [n]).
2. Nel fascicolo si conservano il prompt compilato, o codice e
   versione del prompt della libreria, la risposta da cui deriva la
   bozza usata e la scheda di verifica dei riferimenti.
3. La nota è compilata da chi ha usato lo strumento e vistata dal
   responsabile del servizio prima della firma.
4. Registro e note non contengono dati personali delle persone del
   procedimento e non servono a valutare i singoli dipendenti.
5. La cronologia nello strumento è cancellata entro [n] giorni dalla
   copia nel fascicolo, salvo richieste di accesso pendenti.
6. Il segretario comunale verifica la presenza e la completezza della
   nota negli atti estratti per il controllo successivo.
7. [Facoltativo] Gli atti la cui bozza è stata preparata con l'IA
   recano in calce la formula dell'allegato [n].
8. I modelli allegati sono aggiornati con determinazione del
   [responsabile competente], sentiti il responsabile della
   protezione dei dati e l'RTD.
```

Il comma 8 evita di tornare in Giunta per cambiare un campo. I regolamenti sull'ordinamento degli uffici e dei servizi sono di competenza della Giunta (art. 48, comma 3, TUEL);[^23] in attesa del regolamento può bastare una direttiva del segretario. La scelta dell'atto è discussa nel capitolo sul regolamento interno.

### I tempi

| Quando | Che cosa |
|---|---|
| Giorno 0 | approvazione del regolamento e dei modelli |
| Entro 15 giorni | strumento configurato; voce nel piano di conservazione |
| Entro 30 giorni | informativa ai dipendenti; un'ora di formazione |
| Dal giorno 31 | nota e registro per ogni atto |
| A ogni controllo successivo | verifica delle note negli atti estratti |
| Ogni anno | dati aggregati per il PIAO; revisione dei modelli |

Sono tempi proposti, non previsti dalla legge. I dati aggregati del registro, senza nomi, alimentano gli indicatori del PIAO (si veda il capitolo sul PIAO).

## Un esempio completo: il fascicolo della determina di Borgo Esempio

Il Servizio Affari generali rinnova per il 2027 l'abbonamento alla banca dati giuridica di Editrice Esempio S.r.l., per euro 1.200,00 oltre IVA: è il caso dei capitoli sul metodo del prompt e sulle determine. A novembre 2026 il regolamento interno è ancora in preparazione. Il Servizio Affari generali, che lo scrive e cura la libreria, applica già nota e registro. L'istruttore usa lo strumento dell'ente con il prompt DET-AFF-01 della libreria, versione 2.

### Il fascicolo

Il fascicolo n. 38/2026 contiene sei documenti: la relazione istruttoria con l'offerta presentata dal fornitore nella trattativa diretta sul MePA (doc. 1), il prompt compilato (doc. 2), la risposta dell'IA con la bozza, in PDF/A (doc. 3), la scheda di verifica dei riferimenti (doc. 4), la nota di tracciabilità (doc. 5) e la determina firmata, con il visto di regolarità contabile (doc. 6).

### La nota compilata

```
NOTA DI TRACCIABILITÀ DELL'USO DELL'IA
Fascicolo: n. 38/2026, Servizio Affari generali
Atto: determina di affidamento diretto, rinnovo dell'abbonamento
alla banca dati giuridica per il 2027; n. 214 del 12 novembre 2026
Responsabile del procedimento: RUP_1

1. Strumento: assistente di IA dell'ente; utenza AG-02
2. Modello: non indicato dallo strumento
3. Date d'uso: 10 novembre 2026; conversazioni: 2; tentativi: 1
4. Fasi: bozza; revisione della lingua
5. Prompt: DET-AFF-01 versione 2; testo compilato: doc. 2
6. File di stile: versione 4. Elenco delle norme: Affidamenti
   diretti, verificato il 2 novembre 2026
7. Materiali forniti: doc. 1, senza l'offerta
8. Dati nel prompt: segnaposto (RUP_1)
9. Risposta dell'IA conservata: doc. 3
10. Verifiche: scheda dei riferimenti, doc. 4; segnalazioni
    VERIFICARE nella bozza: 21; tutte risolte: sì
11. Modifiche sostanziali: esito dei contratti precedenti
    accertato; art. 49 TUEL sostituito con art. 147-bis
12. Cronologia nello strumento: cancellata il 13 novembre 2026

Compilata da ISTRUTTORE_1, istruttore, il 12 novembre 2026
Vista dal responsabile del servizio il 12 novembre 2026
```

Nel libro i nomi sono segnaposto. Nella nota vera ci sono i nomi di chi ha lavorato: sono dati dei dipendenti, necessari, non delle persone del procedimento.

La riga nel registro del servizio:

```
27 | 10/11/2026 | fasc. 38/2026 | determina n. 214 del 12/11/2026
   | bozza, lingua | assistente dell'ente, AG-02 | DET-AFF-01 v2
   | segnaposto | scheda: sì | nota: sì
```

La determina non porta formule in calce: Borgo Esempio ha scelto la soluzione minima, e l'uso risulta dal fascicolo e dal registro.

### Tre mesi dopo

*Una richiesta di accesso civico generalizzato.* A febbraio 2027 un cittadino chiede "i prompt usati dal Comune per scrivere le determine del 2026". Il responsabile non ricostruisce nulla: rilascia il registro dell'anno, con l'utenza oscurata perché non serve alla richiesta, e le versioni dei prompt di libreria che il registro cita. Per i prompt compilati, che stanno nei fascicoli, propone al richiedente di indicare gli atti che gli interessano.

*Un errore da richiamare.* Il curatore della libreria si accorge che DET-AFF-01 versione 2 chiedeva di attestare la regolarità tecnica "ai sensi dell'art. 49 del TUEL". L'art. 49 riguarda i pareri sulle proposte di deliberazione; per le determine il riferimento è l'art. 147-bis, comma 1.[^24] Una ricerca nei registri trova gli atti preparati con quella versione. Nella determina n. 214 l'istruttore aveva già corretto il riferimento (punto 11 della nota), ma non l'aveva segnalato al curatore: da allora ogni correzione a un prompt di libreria si segnala. Per gli altri atti, ciascun responsabile controlla la scheda e, se il riferimento è rimasto, valuta con il segretario se serve una rettifica. La versione 3 sostituisce la 2, che si ritira ma non si cancella. Senza registro, si sarebbero rilette tutte le determine dell'anno.

## In sintesi

- L'art. 14 della L. 132/2025 chiede conoscibilità e tracciabilità, ma non dice come: il Comune lo decide nel regolamento interno, una volta per tutti gli uffici.
- Ogni atto preparato con l'IA risponde a tre domande: che cosa ha fatto lo strumento, che cosa ha fatto la persona, che cosa è rimasto.
- Nel fascicolo vanno prompt compilato, risposta usata, scheda di verifica e nota di tracciabilità; nel registro del servizio, una riga per pratica, con codice e versione del prompt.
- La formula nell'atto è facoltativa e non sposta la responsabilità di chi firma. Se il Comune la adotta, la usa sempre.
- Prompt e risposte nel fascicolo sono documenti amministrativi: si accede e si conservano come il resto. La cronologia nello strumento si copia, poi si cancella, mai con una richiesta di accesso pendente.
- Si traccia l'uso, non le persone: nessun dato del procedimento nel registro, nessuna valutazione dei dipendenti con registro e log, un'informativa prima dell'avvio. Per partire basta un mese.

[^1]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 1, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it. Il comma 2 aggiunge che la persona "resta l'unica responsabile dei provvedimenti e dei procedimenti in cui sia stata utilizzata l'intelligenza artificiale"; il comma 3 chiede misure tecniche, organizzative e formative.

[^2]: L. 13 agosto 2010, n. 136, *Piano straordinario contro le mafie, nonché delega al Governo in materia di normativa antimafia*, art. 3, normattiva.it.

[^3]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, art. 147-bis, comma 2, normattiva.it. Il controllo successivo si svolge sotto la direzione del segretario, secondo principi generali di revisione aziendale e modalità definite nell'ambito dell'autonomia organizzativa dell'ente.

[^4]: Consiglio di Stato, sez. VI, sentenza 13 dicembre 2019, n. 8472, giustizia-amministrativa.it; i principi sono ripresi dalla sentenza 4 febbraio 2020, n. 881. Le pronunce riguardano decisioni prese da un algoritmo, non la redazione di bozze, ma indicano che cosa il giudice cerca.

[^5]: TAR Marche, sez. I, sentenza 1° giugno 2026, n. 758, giustizia-amministrativa.it; commento in LavoriPubblici.it, *Intelligenza artificiale negli appalti pubblici: quando l'IA non rende illegittima la decisione amministrativa*, 2026, lavoripubblici.it.

[^6]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, art. 50, par. 4, secondo comma, eur-lex.europa.eu. La disposizione si applica dal 2 agosto 2026 e non è stata modificata dal Regolamento (UE) 2026/1744.

[^7]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale*, art. 41, comma 2, normattiva.it.

[^8]: D.P.R. 28 dicembre 2000, n. 445, *Testo unico delle disposizioni legislative e regolamentari in materia di documentazione amministrativa*, artt. 61 e 68, comma 1, normattiva.it.

[^9]: MySolution, *Approvato in CdM il decreto legislativo inerente all'utilizzo dell'AI*, 2026, mysolution.it. Secondo le sintesi disponibili, il decreto riguarda tra l'altro i poteri delle autorità nazionali e l'uso dell'IA nella pubblica amministrazione, con percorsi di formazione per i dipendenti pubblici.

[^10]: D.Lgs. 14 marzo 2013, n. 33, *Riordino della disciplina riguardante il diritto di accesso civico e gli obblighi di pubblicità, trasparenza e diffusione di informazioni da parte delle pubbliche amministrazioni*, art. 12, comma 1, normattiva.it, che riguarda tra l'altro "ogni atto che dispone in generale sulla organizzazione, sulle funzioni, sugli obiettivi, sui procedimenti".

[^11]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 22, comma 1, lett. d), normattiva.it.

[^12]: TAR Lazio, Roma, sez. III-bis, sentenza 22 marzo 2017, n. 3769, giustizia-amministrativa.it. Sulla conoscibilità dell'algoritmo come principio generale si veda anche Consiglio di Stato, sez. VI, n. 8472/2019, cit.

[^13]: D.P.R. 12 aprile 2006, n. 184, *Regolamento recante disciplina in materia di accesso ai documenti amministrativi*, art. 2, comma 2, normattiva.it; L. 7 agosto 1990, n. 241, cit., art. 22, comma 4.

[^14]: L. 7 agosto 1990, n. 241, cit., artt. 10, comma 1, lett. a), 22, comma 1, lett. b), e 24, commi 3 e 4; D.P.R. 12 aprile 2006, n. 184, cit., art. 9, comma 2. Per l'art. 24, comma 4, l'accesso non può essere negato quando basta differirlo.

[^15]: D.Lgs. 14 marzo 2013, n. 33, cit., artt. 5, comma 2, e 5-bis; ANAC, *Linee guida recanti indicazioni operative ai fini della definizione delle esclusioni e dei limiti all'accesso civico di cui all'art. 5, comma 2, del D.Lgs. 33/2013*, delibera n. 1309 del 28 dicembre 2016, anticorruzione.it; Dipartimento della funzione pubblica, circolari n. 2/2017 e n. 1/2019 sull'attuazione delle norme sull'accesso civico generalizzato, funzionepubblica.gov.it.

[^16]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 43, comma 2. Il consigliere è tenuto al segreto nei casi determinati dalla legge.

[^17]: D.Lgs. 22 gennaio 2004, n. 42, *Codice dei beni culturali e del paesaggio*, artt. 10, comma 2, lett. b), e 21, comma 1, lett. d), normattiva.it.

[^18]: AgID, *Linee guida sulla formazione, gestione e conservazione dei documenti informatici*, 2021, agid.gov.it, applicabili dal 1° gennaio 2022. Prevedono tra l'altro il manuale di gestione documentale, il manuale di conservazione e i formati idonei alla conservazione.

[^19]: Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016 (GDPR), art. 5, par. 1, lett. b), c) ed e), e art. 89, eur-lex.europa.eu.

[^20]: Regolamento (UE) 2024/1689, cit., art. 26, par. 6. Per i sistemi ad alto rischio dell'Allegato III l'obbligo si applica dal 2 dicembre 2027, per effetto dell'art. 113 come modificato dal Regolamento (UE) 2026/1744 del Parlamento europeo e del Consiglio, dell'8 luglio 2026, in vigore dal 27 luglio 2026, eur-lex.europa.eu.

[^21]: L. 20 maggio 1970, n. 300, *Norme sulla tutela della libertà e dignità dei lavoratori, della libertà sindacale e dell'attività sindacale nei luoghi di lavoro e norme sul collocamento*, art. 4, commi 1-3, come sostituito dall'art. 23 del D.Lgs. 14 settembre 2015, n. 151; D.Lgs. 30 marzo 2001, n. 165, art. 51, comma 2, per l'applicazione dello Statuto alle pubbliche amministrazioni a prescindere dal numero dei dipendenti; D.Lgs. 30 giugno 2003, n. 196, art. 114, normattiva.it.

[^22]: Garante per la protezione dei dati personali, *Programmi e servizi informatici di gestione della posta elettronica nel contesto lavorativo e trattamento dei metadati*, documento di indirizzo, provvedimento 6 giugno 2024, n. 364, garanteprivacy.it.

[^23]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 48, comma 3.

[^24]: D.Lgs. 18 agosto 2000, n. 267, cit., artt. 49 e 147-bis, comma 1. Il caso dell'articolo giusto nell'atto sbagliato è descritto nel capitolo sulla verifica delle norme.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 27 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- L'esempio diceva che Borgo Esempio aveva scelto la formula in calce all'atto.
- La conoscibilità era attribuita a 'chiunque', mentre l'art. 14 della L. 132/2025 parla di 'interessati'.
- Il testo diceva che il fascicolo dell'art. 41 CAD comprende la bozza prodotta dall'IA. La norma non parla di bozze: ora conservare la bozza è presentato come una scelta prudente.
- La frase 'Se i punti 9 e 10 sono vuoti, la bozza non è stata verificata' non reggeva, perché il punto 9 riguarda la conservazione della risposta, non la verifica.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
