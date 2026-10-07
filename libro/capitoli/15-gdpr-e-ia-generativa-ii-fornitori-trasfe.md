# GDPR e IA generativa (II): fornitori, trasferimenti, DPIA e incidenti

In questo capitolo: il contratto con il fornitore ai sensi dell'art. 28 GDPR, i trasferimenti verso paesi terzi, la valutazione d'impatto e il raccordo con l'AI Act, la verifica del modello, la gestione dell'incidente e il ruolo di DPO e RTD.

## Versione gratuita o versione per l'ente

Il Comune di Borgo Esempio ha deciso di dare al personale uno strumento di IA generativa. Prima della determina di affidamento, il responsabile del Servizio Affari generali deve rispondere alle domande lasciate aperte dal capitolo sui principi del GDPR: con chi il Comune firma, dove vanno i dati, che cosa si valuta prima dell'uso, che cosa si fa quando qualcosa va storto. Gli articoli senza altra indicazione sono del Regolamento (UE) 2016/679 (GDPR).[^1]

### Tre differenze

Quasi tutti i produttori offrono due famiglie di servizi: quelli per i consumatori, con account personale, gratuiti o a pagamento, e quelli per le organizzazioni, con un contratto dell'ente. Per il Comune contano tre differenze.[^2]

*Addestramento.* Nei piani per consumatori le conversazioni possono servire ad addestrare i modelli, se l'utente non lo esclude nelle impostazioni. Nei servizi per le organizzazioni, di regola, il contratto lo esclude.

*Conservazione.* Nei piani per consumatori i tempi li decide il fornitore, e possono dipendere dall'impostazione sull'addestramento. Nei servizi per le organizzazioni li regolano il contratto e, in parte, l'amministratore dell'ente; può restare una conservazione breve per la sicurezza e il controllo degli abusi. Cancellare una conversazione la toglie dalla cronologia, non sempre e non subito dai sistemi del fornitore.

*Contratto.* Solo il servizio per le organizzazioni prevede un accordo che rende il fornitore responsabile del trattamento per conto del Comune. Con l'account personale il fornitore tratta i dati come titolare autonomo.

| Aspetto | Account personale | Servizio per l'ente |
|---|---|---|
| Chi contratta | il dipendente | il Comune |
| Addestramento | possibile, salvo esclusione | di regola escluso |
| Conservazione | la decide il fornitore | regolata dal contratto |
| Accordo ex art. 28 | assente | presente |
| Gestione degli accessi | nessuna | amministratore dell'ente |

### Non conta il prezzo, conta chi firma

Un abbonamento personale a pagamento resta un servizio per consumatori. Al contrario, alcuni servizi per le organizzazioni sono compresi nelle licenze che l'ente ha già. Microsoft, per esempio, dichiara che la chat di Copilot usata con l'account di lavoro gode della protezione prevista per i dati dell'organizzazione, e che prompt e risposte non servono ad addestrare i modelli di base.[^3] Il discrimine è il contratto: chi lo firma, che cosa dice, se copre il servizio che usi.

Il contratto serve anche se nei prompt non ci sono dati dei cittadini. Il fornitore tratta comunque dati personali dei dipendenti: nome, indirizzo di posta, registri d'uso. E se usa i dati del Comune per finalità proprie, come l'addestramento, per quel trattamento diventa titolare (art. 28, par. 10).[^4]

Per chi scrive atti la regola resta quella del capitolo sul metodo del prompt: dati personali solo nello strumento autorizzato, e solo quelli necessari. Quale strumento scegliere è il tema del capitolo su quale IA usare in ufficio; come acquistarlo, del capitolo sull'acquisto di uno strumento di IA.

## L'accordo sul trattamento dei dati

Il Comune può affidare un trattamento solo a un responsabile che presenti "garanzie sufficienti" (art. 28, par. 1). Il rapporto è regolato da un contratto o da un altro atto giuridico, anche in formato elettronico. L'atto stabilisce materia, durata, natura e finalità del trattamento, tipo di dati, categorie di interessati, obblighi e diritti del titolare (parr. 3 e 9). I fornitori lo chiamano di solito *Data Processing Agreement* o *Addendum* (DPA). La Commissione ha adottato clausole contrattuali tipo per questo rapporto: usarle non è obbligatorio, ma sono un buon termine di confronto.[^5]

### Le clausole da controllare

| Clausola | Art. 28 | Che cosa cercare |
|---|---|---|
| Istruzioni | par. 3, lett. a) | niente addestramento; trasferimenti su istruzione |
| Riservatezza e sicurezza | lett. b) e c) | impegno del personale; misure dell'art. 32 |
| Sub-responsabili | lett. d); parr. 2 e 4 | elenco, preavviso, opposizione |
| Diritti degli interessati | lett. e) | assistenza su accesso, rettifica, cancellazione |
| Violazioni e DPIA | lett. f) | avviso senza ritardo; informazioni |
| Fine del servizio | lett. g) | cancellazione o restituzione, con tempi |
| Verifiche | lett. h) | documenti, audit, certificazioni |

### I sub-responsabili

Un fornitore di IA si appoggia ad altri: chi ospita i server, chi sviluppa il modello, chi gestisce l'assistenza. Ognuno è un sub-responsabile. Il responsabile non può ricorrervi senza un'autorizzazione scritta del titolare, specifica o generale. Con l'autorizzazione generale deve informarlo dei cambiamenti e consentirgli di opporsi (par. 2). Al sub-responsabile si impongono gli stessi obblighi, e del suo inadempimento il responsabile iniziale risponde per intero verso il titolare (par. 4).

Secondo il Comitato europeo per la protezione dei dati (EDPB), il titolare deve avere sempre a disposizione l'identità di tutti i soggetti della catena: nome, indirizzo, persona di contatto. Deve verificarne le garanzie qualunque sia il rischio; il rischio decide quanto approfondire.[^6] In pratica: scarica l'elenco dei sub-responsabili, annota la data, iscriviti agli avvisi di modifica se il fornitore li offre, e conserva tutto nel fascicolo dello strumento.

### Contratti che non si negoziano

Un piccolo Comune non negozia con un grande produttore. Il DPA è standard e si accetta all'attivazione del servizio. Non serve mandare al fornitore il modulo di nomina a responsabile usato con le ditte locali: non lo firmerà. Serve leggere il DPA prima dell'affidamento, verificare che copra il servizio acquistato e decidere. Se il DPA non dà le garanzie necessarie, si cambia strumento: le istruzioni al personale non possono supplire a ciò che il contratto non garantisce.

Se compri la licenza da un rivenditore, per esempio sul mercato elettronico, controlla con chi è concluso l'accordo sul trattamento: di solito con il produttore. Se accede ai dati, per esempio per l'assistenza o l'amministrazione, anche il rivenditore è responsabile del trattamento, e serve un accordo anche con lui. Per i servizi in cloud verifica anche la qualificazione dell'Agenzia per la cybersicurezza nazionale (ACN), richiesta per i servizi acquistati dalla pubblica amministrazione e trattata nel capitolo sull'acquisto.[^7]

Nella determina di affidamento l'accordo va richiamato in modo che si capisca che è il contratto dell'art. 28. Una formula da adattare, per la motivazione:

```
Considerato che [fornitore] tratterà dati personali per conto del
Comune quale responsabile del trattamento, secondo l'accordo [titolo],
versione del [data], che costituisce il contratto previsto dall'art. 28
del Regolamento (UE) 2016/679 ed è stato esaminato dal responsabile
della protezione dei dati il [data];
```

L'IA può aiutarti a leggere il DPA, che di solito è un documento pubblico e non contiene dati personali. Il prompt che segue confronta il testo con l'art. 28 e prepara le domande per il fornitore. Allega anche il testo dell'articolo: il modello deve lavorare sulla norma che gli dai, non su quella che ricorda.

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

Il giudizio finale non spetta al modello. Riscontra ogni citazione sul documento e porta la tabella al responsabile della protezione dei dati.

## Trasferimenti verso paesi terzi

### Quando c'è un trasferimento

I dati personali lasciano lo Spazio economico europeo solo con le garanzie del capo V del GDPR (artt. 44-49). Per l'EDPB c'è trasferimento quando un titolare o un responsabile soggetto al GDPR trasmette dati, o li rende accessibili, a un altro soggetto che si trova in un paese terzo.[^8] Anche l'accesso da remoto, quindi, è un trasferimento: per esempio quello dei tecnici di una società del gruppo o di un sub-responsabile che prestano assistenza dagli Stati Uniti.

### Gli strumenti

*Decisione di adeguatezza (art. 45).* Per gli Stati Uniti è la Decisione di esecuzione (UE) 2023/1795 della Commissione, del 10 luglio 2023, sul quadro UE-USA per la protezione dei dati (*Data Privacy Framework*, DPF). Copre solo le organizzazioni statunitensi che vi hanno aderito e che compaiono nell'elenco pubblico del Dipartimento del commercio.[^9] Verifica che ci siano il fornitore e i suoi sub-responsabili statunitensi, e che l'adesione sia attiva.

*Clausole contrattuali tipo (art. 46).* Sono quelle della Decisione di esecuzione (UE) 2021/914. Dopo la sentenza Schrems II della Corte di giustizia, che nel 2020 ha annullato il precedente accordo UE-USA, chi le usa deve valutare se il diritto del paese di destinazione ne consente il rispetto. Se non lo consente, servono misure supplementari.[^10]

*Deroghe (art. 49).* Sono eccezioni per situazioni specifiche. Non coprono l'uso quotidiano di uno strumento d'ufficio.

### Un quadro in vigore, ma conteso

Il 3 settembre 2025 il Tribunale dell'Unione europea ha respinto il ricorso di annullamento contro il DPF (causa T-553/23, *Latombe c. Commissione*). Secondo le notizie disponibili, il ricorrente ha impugnato la sentenza davanti alla Corte di giustizia.[^11] Il precedente accordo, il *Privacy Shield*, era caduto proprio davanti alla Corte. Conviene quindi che il DPA preveda le clausole tipo anche quando il fornitore aderisce al DPF: se la decisione di adeguatezza cadesse, il trasferimento avrebbe già un'altra base.

### La residenza dei dati

Molti fornitori offrono, nei servizi per le organizzazioni, la conservazione dei dati in Europa. È utile, ma non esclude ogni trasferimento. Nella documentazione cerca tre cose:

- se l'impegno riguarda solo i dati conservati o anche l'elaborazione delle richieste;
- quali eccezioni elenca, come l'assistenza tecnica o la sicurezza;
- se vale per tutte le funzioni dello strumento o solo per alcune.

Quello che trovi va nell'informativa e nel registro dei trattamenti, come spiegato nel capitolo sui principi del GDPR.

## La valutazione d'impatto e il raccordo con l'AI Act

### Quando serve

La valutazione d'impatto sulla protezione dei dati (DPIA) è obbligatoria, prima del trattamento, quando un tipo di trattamento, "in particolare" con l'uso di nuove tecnologie, può presentare un rischio elevato per i diritti e le libertà delle persone (art. 35, par. 1). Una sola valutazione può esaminare un insieme di trattamenti simili con rischi analoghi. Il titolare si consulta con il responsabile della protezione dei dati (par. 2).[^12]

Il Garante per la protezione dei dati personali ha pubblicato l'elenco dei trattamenti soggetti a DPIA (art. 35, par. 4). Vi rientrano i trattamenti effettuati con tecnologie innovative, tra cui i sistemi di intelligenza artificiale, quando ricorre anche almeno un altro dei criteri delle linee guida europee sulla DPIA.[^13] Tra quei criteri ci sono le categorie particolari di dati e i dati di natura molto personale, gli interessati vulnerabili, i trattamenti su larga scala, le valutazioni e i punteggi, le decisioni automatizzate. Le stesse linee guida raccomandano di fare la DPIA quando non è chiaro se serva.[^14]

Per un Comune i casi tipici sono tre.

- Lo strumento usato solo per testi senza dati personali, come circolari, avvisi e modelli generici, non richiede DPIA. Annota nel fascicolo perché.
- Lo strumento usato con i segnaposto per atti su persone, per esempio nei servizi demografici o tecnici, richiede una valutazione documentata, con il DPO. Spesso si conclude con la DPIA.
- Lo strumento usato nei servizi sociali riguarda in modo non occasionale interessati vulnerabili, anche quando nel prompt ci sono solo segnaposto: la DPIA va fatta. Dati sulla salute, su condanne e reati e dati di minori restano comunque fuori dal prompt, come spiega il capitolo sul metodo del prompt.

### Che cosa contiene

La DPIA contiene almeno quattro parti: la descrizione sistematica dei trattamenti e delle finalità; la valutazione di necessità e proporzionalità; la valutazione dei rischi per gli interessati; le misure previste per affrontarli (art. 35, par. 7). Va riesaminata quando il rischio cambia (par. 11): nuovo strumento, nuove funzioni, nuovi servizi. Se, nonostante le misure, il rischio resta elevato, il Comune consulta il Garante prima di iniziare (art. 36).

Se applica il metodo di questo libro, il Comune ha già molte misure: segnaposto, dati esclusi, addestramento escluso, memoria disattivata, verifica umana, formazione. La DPIA serve a scriverle, a controllare che funzionino e a dire chi ne risponde.

La descrizione è la parte più lunga e la meno delicata. Puoi farne preparare la bozza al modello, senza dati personali.

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

Il prompt vieta di valutare i rischi. Rischi e misure li valuti tu, con il DPO: sono il cuore della DPIA, e la responsabilità è del Comune.

### Il raccordo con la FRIA

L'AI Act prevede una valutazione diversa: la valutazione d'impatto sui diritti fondamentali (in inglese FRIA) dell'art. 27. La fanno gli organismi di diritto pubblico prima di usare un sistema ad alto rischio dell'Allegato III, come quelli che valutano l'ammissibilità alle prestazioni di assistenza pubblica (si veda il capitolo sull'AI Act).[^15] Un chatbot generalista usato per scrivere bozze, di regola, non è ad alto rischio: la FRIA non serve, la DPIA può servire.

| Aspetto | DPIA | FRIA |
|---|---|---|
| Fonte | art. 35 GDPR | art. 27 AI Act |
| Quando | rischio elevato per gli interessati | sistema ad alto rischio |
| Oggetto | protezione dei dati | tutti i diritti fondamentali |
| Chi | il titolare | l'ente che usa il sistema |
| Si applica | dal 25 maggio 2018 | dal 2 dicembre 2027 |
| Esito | se serve, consultazione del Garante | notifica all'autorità di vigilanza del mercato |

Le due valutazioni si coordinano. Il deployer, cioè l'ente che usa un sistema ad alto rischio, si serve per la DPIA delle informazioni che il fornitore deve dargli (art. 26, par. 9, AI Act). Se un obbligo della FRIA è già assolto dalla DPIA, la FRIA integra la DPIA (art. 27, par. 4). In pratica: un unico fascicolo, una DPIA che descrive il trattamento, una FRIA che aggiunge i diritti diversi dalla protezione dei dati, come la non discriminazione e l'accesso alle prestazioni.

## Verificare il modello

### Il parere EDPB 28/2024

Il Comune usa modelli addestrati da altri, spesso anche su testi raccolti dal web, che possono comprendere dati pubblicati dagli stessi Comuni. Con il parere 28/2024 del 17 dicembre 2024 l'EDPB ha chiarito tre punti che riguardano chi li usa.[^16]

1. Un modello addestrato con dati personali non è anonimo per definizione. Lo è solo se è insignificante la probabilità di estrarne quei dati, direttamente o con domande mirate.
2. Se il modello è stato sviluppato trattando illecitamente dati personali, può esserne compromessa la liceità dell'uso da parte di un altro titolare, salvo che il modello sia stato reso anonimo.
3. Chi usa il modello deve svolgere, in base al principio di responsabilizzazione, una valutazione adeguata per accertare che non sia stato sviluppato in modo illecito. La profondità dipende dai rischi. Contano, tra l'altro, la fonte dei dati e le violazioni eventualmente accertate da un'autorità o da un giudice.

Per un Comune non si tratta di analizzare i dati di addestramento, cosa impossibile. Si tratta di raccogliere le informazioni disponibili, conservarle e non ignorare i segnali di allarme.

### Il Garante e l'IA generativa

Il Garante è intervenuto più volte sui servizi di IA generativa.[^17]

- Il 30 marzo 2023 ha limitato in via provvisoria il trattamento dei dati degli utenti italiani di ChatGPT.
- Con il provvedimento n. 755 del 2 novembre 2024, reso noto il 20 dicembre, ha inflitto a OpenAI una sanzione di 15 milioni di euro. Tra le violazioni contestate c'erano la base giuridica dell'addestramento, la trasparenza, la verifica dell'età e la mancata notifica di una violazione di dati del marzo 2023. OpenAI ha impugnato il provvedimento e, secondo le notizie di stampa, nel marzo 2026 il Tribunale di Roma lo ha annullato. I commenti collegano la decisione alla competenza del Garante: per i trattamenti transfrontalieri, il meccanismo dello sportello unico affida il caso all'autorità del paese in cui il fornitore ha lo stabilimento principale nell'Unione.
- Il 30 gennaio 2025 ha disposto la limitazione urgente del trattamento nei confronti delle società che offrono DeepSeek.

Un provvedimento riguarda anche i Comuni come gestori di siti: le indicazioni del 20 maggio 2024 per difendere i dati personali pubblicati online dalla raccolta massiva finalizzata all'addestramento dei modelli (*web scraping*).[^18] Il tema tocca l'albo online e torna nel capitolo sulla privacy prima della pubblicazione.

### Le domande da fare

Prima di adottare uno strumento, raccogli nel fascicolo le risposte a queste domande. Il produttore dello strumento e quello del modello possono essere diversi: le domande valgono per entrambi.

- Il fornitore è stabilito nell'Unione? Con quale società firma il Comune? Quale autorità di controllo è capofila?
- Ci sono provvedimenti di autorità o sentenze sul servizio o sul modello? Con quale esito?
- Che cosa dichiara il fornitore sui dati di addestramento? Dal 2 agosto 2025 i fornitori di nuovi modelli per finalità generali devono pubblicare una sintesi dei contenuti usati per l'addestramento, secondo un modello della Commissione.[^19]
- I dati del Comune sono esclusi dall'addestramento, nel contratto e nelle impostazioni?
- Quali certificazioni di sicurezza ha il servizio, e chi le ha rilasciate?

## Il prompt sbagliato come violazione di dati

### Che cos'è una violazione

È violazione dei dati personali la violazione di sicurezza che comporta, accidentalmente o in modo illecito, la distruzione, la perdita, la modifica, la divulgazione non autorizzata o l'accesso ai dati personali (art. 4, n. 12). Le linee guida europee distinguono violazioni di riservatezza, di integrità e di disponibilità.[^20] Con l'IA generativa i casi più probabili riguardano la riservatezza:

- dati personali incollati in uno strumento non autorizzato o in un account personale;
- una conversazione condivisa con un link pubblico;
- una bozza che riporta dati di un'altra pratica, recuperati dalla memoria dello strumento, e che parte verso un destinatario;
- un collegamento a cartelle condivise che mostra a un utente file che non doveva vedere;
- una violazione nei sistemi del fornitore.

I link pubblici non sono un rischio teorico. Nell'estate del 2025 migliaia di conversazioni di ChatGPT, condivise con l'opzione che le rendeva rintracciabili, sono comparse nei risultati dei motori di ricerca, e OpenAI ha ritirato l'opzione.[^21]

### Prevenire: l'art. 32

Titolare e responsabile mettono in atto misure tecniche e organizzative adeguate al rischio. Chi agisce sotto la loro autorità tratta i dati solo se istruito (art. 32, parr. 1 e 4).[^22] Per uno strumento di IA le misure minime sono:

- accesso solo con l'account dell'ente e autenticazione a più fattori;
- addestramento escluso, nel contratto e nelle impostazioni;
- memoria e link di condivisione disattivati;
- collegamenti a posta e cartelle solo se servono, dopo aver rivisto i permessi;
- istruzioni scritte e formazione del personale.

Sono le impostazioni del capitolo sui principi del GDPR: qui rendono l'incidente meno probabile e meno grave.

### Le prime ore

Il termine per notificare decorre da quando il Comune è venuto a conoscenza della violazione. Per le linee guida europee ciò avviene quando il titolare ha una ragionevole certezza che un incidente di sicurezza ha compromesso dati personali.[^23] Il Comune lo sa attraverso le persone: chi se ne accorge deve segnalarlo subito, senza aspettare di capire se è grave.

Se ti accorgi di aver incollato dati personali dove non dovevi:

1. non continuare la conversazione e non incollare altro;
2. annota strumento, account, data e ora, categorie di dati, numero di persone;
3. se c'era un link di condivisione, revocalo; se l'addestramento era attivo, disattivalo;
4. cancella la conversazione e annota quando l'hai fatto;
5. avvisa subito il tuo responsabile e il DPO con la segnalazione interna.

Nella segnalazione non ripetere i dati coinvolti: bastano le categorie. Valutare il rischio e decidere sulla notifica spetta a chi l'ente ha individuato nella propria procedura sulle violazioni, sentito il DPO.

```
SEGNALAZIONE INTERNA DI POSSIBILE VIOLAZIONE DI DATI PERSONALI
(artt. 33 e 34 del Regolamento (UE) 2016/679)
Comune di [nome] – Servizio [nome]
A: responsabile del servizio; responsabile della protezione dei dati;
RTD; segretario comunale
Data e ora della segnalazione: [data, ora]
Segnalante: [nome e ruolo]

1. Che cosa è successo: [poche righe, senza riportare i dati]
2. Quando: fatto avvenuto il [data, ora]; scoperto il [data, ora]
3. Strumento: [nome]; account [dell'ente / personale]
   Addestramento sulle conversazioni: [attivo / disattivato / non so]
   Link di condivisione: [no / sì, revocato il (data, ora)]
   Conversazione cancellata il: [data, ora / no]
4. Dati coinvolti (solo categorie): [es. nome e indirizzo; salute;
   dati di minori]
   Persone interessate: [numero, anche stimato; categorie]
   Riconoscibili: [sì / no / solo con altre informazioni]
5. Misure già prese: [es. cancellazione, revoca del link]
6. Altre informazioni: [colleghi coinvolti; contatti con il fornitore]

Parte riservata alla valutazione (sentito il DPO)
Rischio per gli interessati: [improbabile / non improbabile / elevato]
Motivi: [natura dei dati, numero, riconoscibilità, misure prese]
Notifica al Garante (art. 33): [sì, il (data) / no, perché (motivi)]
Comunicazione agli interessati (art. 34): [sì / no, perché (motivi)]
Registro delle violazioni (art. 33, par. 5): [numero, data]
Firma: [chi decide secondo la procedura dell'ente]
```

### Notificare e comunicare

Il titolare notifica la violazione al Garante senza ingiustificato ritardo e, ove possibile, entro 72 ore da quando ne è venuto a conoscenza. Non la notifica se è improbabile che la violazione presenti un rischio per i diritti e le libertà delle persone. Oltre le 72 ore la notifica indica i motivi del ritardo (art. 33, par. 1), e le informazioni si possono dare per fasi (par. 4). Si usa la procedura telematica del Garante.[^24]

Se il rischio è elevato, il titolare comunica la violazione anche agli interessati, senza ingiustificato ritardo e con un linguaggio semplice e chiaro (art. 34). La comunicazione non serve se le misure successive rendono improbabile il rischio elevato. Se richiede sforzi sproporzionati, si sostituisce con una comunicazione pubblica (par. 3).

Ogni violazione, anche quella non notificata, va documentata: fatti, effetti, provvedimenti adottati (art. 33, par. 5). Il registro delle violazioni dimostra che la valutazione è stata fatta. Se la violazione avviene nei sistemi del fornitore, il fornitore ne informa il Comune senza ingiustificato ritardo (art. 33, par. 2): per questo la clausola sugli avvisi va controllata nel DPA.

La proposta di regolamento presentata dalla Commissione il 19 novembre 2025, il cosiddetto Digital Omnibus, prevede di limitare la notifica al Garante alle violazioni a rischio elevato, di portare il termine a 96 ore e di creare un punto unico europeo per le notifiche. A ottobre 2026 il negoziato è ancora in corso e il testo può cambiare: valgono l'art. 33 vigente e le 72 ore.[^25]

### Due casi a Borgo Esempio

*Primo caso.* Un istruttore dei Servizi demografici, per rispondere in fretta, incolla nel chatbot gratuito del proprio telefono una PEC con nome e indirizzo di un cittadino che chiede un certificato. L'addestramento era attivo. Dopo un'ora si rende conto dell'errore, cancella la conversazione e lo segnala. Sono dati comuni di una sola persona, senza link pubblico. Il Comune, sentito il DPO, può ritenere improbabile il rischio: la violazione si annota nel registro, con i motivi della mancata notifica.

*Secondo caso.* Un'istruttrice dei Servizi sociali incolla in un account personale la relazione su un minore, con dati sulla salute, per farne una sintesi. Sono categorie particolari di dati di un interessato vulnerabile, in un Comune piccolo, dove la famiglia è riconoscibile. Il rischio non è improbabile e può essere elevato: la notifica al Garante va fatta entro 72 ore. Sulla comunicazione alla famiglia decide il titolare, sentito il DPO.

In entrambi i casi il danno maggiore viene dal silenzio. Una segnalazione tardiva riduce i margini per limitare le conseguenze e consuma le 72 ore.

## DPO e RTD: chi consultare e quando

### Il responsabile della protezione dei dati

Il Comune deve designare un responsabile della protezione dei dati (DPO). Può essere un dipendente o un professionista esterno, anche condiviso con altri enti, tenuto conto della loro struttura e dimensione (art. 37, parr. 1, lett. a), 3 e 6). Il titolare lo coinvolge "tempestivamente e adeguatamente" in tutte le questioni sulla protezione dei dati (art. 38, par. 1). Il DPO informa e consiglia, sorveglia l'osservanza delle regole, compresa la formazione del personale, fornisce su richiesta pareri sulla DPIA e coopera con il Garante (art. 39).[^26]

Il DPO consiglia; decide il titolare. Non è il DPO a fare la DPIA, né a rispondere della conformità al posto del Comune. Se nella DPIA il Comune non segue il suo parere, le linee guida europee chiedono di motivarlo per iscritto.

### Il responsabile per la transizione al digitale

Il responsabile per la transizione al digitale (RTD) guida la trasformazione digitale dell'ente. Tra i suoi compiti ci sono il coordinamento dei sistemi informativi e la sicurezza informatica (art. 17 del D.Lgs. 7 marzo 2005, n. 82, Codice dell'amministrazione digitale). Negli enti senza dirigenti è scelto tra le posizioni apicali.[^27] Per uno strumento di IA porta lo sguardo tecnico: account, autenticazione, integrazioni, registri, qualificazione cloud, coerenza con la pianificazione informatica dell'ente.

A Borgo Esempio il RTD è il responsabile del Servizio Affari generali; il DPO è un professionista esterno, condiviso con altri Comuni.

| Quando | Chi | Che cosa porti |
|---|---|---|
| Scelta dello strumento | DPO e RTD | DPA, sub-responsabili, trasferimenti |
| Prima dei dati personali | DPO | DPIA o motivi per non farla |
| Nuovo servizio o funzione | DPO e RTD | DPIA e registro aggiornati |
| Incidente | DPO e RTD, subito | segnalazione interna |
| Nuove condizioni del fornitore | DPO e RTD | testo nuovo e differenze |
| Richiesta di un interessato | DPO | prompt e cronologia della pratica |

### Il fascicolo dello strumento

A DPO e RTD non servono opinioni sull'IA: servono documenti. Raccoglili in un unico fascicolo e aggiornalo a ogni cambiamento. Lo stesso fascicolo serve al segretario per i controlli e al responsabile del servizio per motivare l'affidamento.

```
FASCICOLO DELLO STRUMENTO DI IA – versione [n] del [data]
Comune di [nome] – a cura di [responsabile del servizio]

1. Strumento: [nome commerciale; piano o licenza; numero di utenze]
2. Fornitore: [denominazione e sede della società che firma];
   rivenditore: [se diverso]
3. Affidamento: [determina n., data]
4. Accordo sul trattamento (art. 28): [titolo, versione, data]
5. Sub-responsabili: [elenco, data di consultazione]
6. Luoghi del trattamento e trasferimenti: [paesi; DPF o clausole
   tipo; eccezioni dichiarate]
7. Impostazioni: addestramento [escluso]; memoria [attiva /
   disattivata]; cronologia [giorni]; link di condivisione [sì / no];
   collegamenti [quali]
8. Qualificazione ACN: [estremi]
9. Classificazione AI Act: [rischio minimo / trasparenza / alto]
10. Usi ammessi: [servizi, tipi di atto]; dati esclusi: [quali]
11. Verifica sul modello: [documenti raccolti, data]
12. Valutazione d'impatto (art. 35): [esito, data] oppure motivi per
    cui non è necessaria
13. Parere del DPO: [data, sintesi]; parere del RTD: [data, sintesi]
14. Informativa e registro aggiornati il: [data]
15. Istruzioni al personale: [estremi]; formazione: [date]
16. Violazioni: [rinvio al registro delle violazioni]
17. Prossima revisione: [data]
```

## In sintesi

- Non conta il prezzo, conta il contratto. Un account personale, anche a pagamento, non ha l'accordo sul trattamento; il servizio per l'ente sì.
- L'accordo dell'art. 28 si legge prima dell'affidamento: istruzioni, niente addestramento, sub-responsabili, avvisi sulle violazioni, cancellazione, verifiche.
- I trasferimenti verso gli Stati Uniti si fondano sul DPF o sulle clausole tipo. Il DPF ha superato il primo grado ma risulta impugnato: conviene che il contratto preveda entrambi.
- La residenza dei dati in Europa riduce i trasferimenti, non sempre li esclude: leggi le eccezioni.
- IA e interessati vulnerabili richiedono la DPIA. La FRIA dell'AI Act riguarda i sistemi ad alto rischio dal 2 dicembre 2027 e integra la DPIA.
- Chi usa un modello verifica, in proporzione al rischio, che non sia stato sviluppato in modo illecito.
- Dati incollati nello strumento sbagliato possono essere una violazione. Segnalala subito: salvo che il rischio sia improbabile, il Comune deve notificarla al Garante entro 72 ore da quando ne è venuto a conoscenza.
- DPO e RTD si consultano prima, non dopo, con un fascicolo dello strumento completo.

[^1]: Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016, *relativo alla protezione delle persone fisiche con riguardo al trattamento dei dati personali, nonché alla libera circolazione di tali dati e che abroga la direttiva 95/46/CE (regolamento generale sulla protezione dei dati)*, eur-lex.europa.eu.

[^2]: Per esempio, nei piani personali di Claude (Free, Pro e Max) le conversazioni possono essere usate per l'addestramento se l'utente non disattiva l'impostazione, e in quel caso sono conservate fino a cinque anni; se la disattiva, la conservazione è di 30 giorni. I servizi per le organizzazioni e l'uso tramite API ne sono esclusi: Anthropic, *Updates to Consumer Terms and Privacy Policy*, 2025, anthropic.com. Per i servizi aziendali di OpenAI: OpenAI, *Enterprise privacy at OpenAI*, 2026, openai.com. Le condizioni cambiano spesso: vanno lette, strumento per strumento, alla data d'uso.

[^3]: Microsoft, *Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat*, 2026, learn.microsoft.com.

[^4]: GDPR, art. 28, par. 10; EDPB, *Linee guida 07/2020 sui concetti di titolare del trattamento e di responsabile del trattamento ai sensi del GDPR*, versione 2.0, 2021, edpb.europa.eu.

[^5]: GDPR, art. 28, parr. 1, 3, 7 e 9; Decisione di esecuzione (UE) 2021/915 della Commissione, del 4 giugno 2021, *relativa alle clausole contrattuali tipo tra titolari del trattamento e responsabili del trattamento a norma dell'articolo 28, paragrafo 7, del regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio e dell'articolo 29, paragrafo 7, del regolamento (UE) 2018/1725 del Parlamento europeo e del Consiglio*, eur-lex.europa.eu.

[^6]: EDPB, *Opinion 22/2024 on certain obligations following from the reliance on processor(s) and sub-processor(s)*, adottato il 7 ottobre 2024, edpb.europa.eu.

[^7]: Agenzia per la cybersicurezza nazionale, decreto direttoriale n. 21007/24 del 27 giugno 2024, che adotta il regolamento unico per le infrastrutture digitali e i servizi cloud della pubblica amministrazione, in vigore dal 1° agosto 2024, e catalogo dei servizi cloud qualificati, acn.gov.it. La qualificazione riguarda il singolo servizio, non il fornitore.

[^8]: GDPR, artt. 44-49; EDPB, *Linee guida 05/2021 sull'interazione tra l'applicazione dell'articolo 3 e le disposizioni sui trasferimenti internazionali di cui al capo V del GDPR*, versione 2.0, 2023, edpb.europa.eu.

[^9]: Decisione di esecuzione (UE) 2023/1795 della Commissione, del 10 luglio 2023, sul livello di protezione adeguato dei dati personali nell'ambito del quadro UE-USA per la protezione dei dati personali, eur-lex.europa.eu. L'elenco delle organizzazioni aderenti è su dataprivacyframework.gov.

[^10]: Corte di giustizia dell'Unione europea, Grande Sezione, sentenza 16 luglio 2020, causa C-311/18, *Data Protection Commissioner c. Facebook Ireland e Maximillian Schrems* (Schrems II), curia.europa.eu; Decisione di esecuzione (UE) 2021/914 della Commissione, del 4 giugno 2021, *relativa alle clausole contrattuali tipo per il trasferimento di dati personali verso paesi terzi a norma del regolamento (UE) 2016/679*, eur-lex.europa.eu; EDPB, *Raccomandazioni 01/2020 relative alle misure che integrano gli strumenti di trasferimento al fine di garantire il rispetto del livello di protezione dei dati personali dell'UE*, versione 2.0, 2021, edpb.europa.eu.

[^11]: Tribunale dell'Unione europea, sentenza 3 settembre 2025, causa T-553/23, *Latombe c. Commissione*, curia.europa.eu. Sull'impugnazione, che risulta proposta alla fine di ottobre 2025: Digital Policy Alert, *Latombe filed appeal against General Court dismissal of challenge to European Union-United States Data Protection Framework adequacy decision*, 2025, digitalpolicyalert.org. Numero di causa e stato del giudizio vanno verificati su curia.europa.eu alla data di lettura.

[^12]: GDPR, artt. 35, parr. 1, 2, 4, 7 e 11, e 36, par. 1.

[^13]: Garante per la protezione dei dati personali, provvedimento n. 467 dell'11 ottobre 2018, *Elenco delle tipologie di trattamenti soggetti al requisito di una valutazione d'impatto sulla protezione dei dati ai sensi dell'art. 35, comma 4, del Regolamento (UE) n. 2016/679*, allegato 1, garanteprivacy.it.

[^14]: Gruppo di lavoro Articolo 29 per la protezione dei dati, *Linee guida in materia di valutazione d'impatto sulla protezione dei dati e determinazione della possibilità che il trattamento "possa presentare un rischio elevato" ai fini del regolamento (UE) 2016/679* (WP248 rev.01), 2017, ec.europa.eu. Le linee guida sono state fatte proprie dall'EDPB.

[^15]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale (AI Act), artt. 26, par. 9, e 27, parr. 1, 3 e 4, e Allegato III, punto 5, lett. a), eur-lex.europa.eu. La data del 2 dicembre 2027 è fissata dall'art. 113, come modificato dal Regolamento (UE) 2026/1744 dell'8 luglio 2026, in vigore dal 27 luglio 2026.

[^16]: EDPB, *Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models*, adottato il 17 dicembre 2024, edpb.europa.eu.

[^17]: Garante per la protezione dei dati personali, provvedimento 30 marzo 2023 (doc. web n. 9870832), provvedimento n. 755 del 2 novembre 2024 e comunicato stampa del 20 dicembre 2024, provvedimento 30 gennaio 2025 nei confronti delle società che forniscono DeepSeek, garanteprivacy.it. Sull'annullamento della sanzione, secondo fonti di stampa: Diritto.it, *OpenAI vince contro il Garante privacy: perché il Tribunale di Roma ha annullato la sanzione da 15 milioni*, 2026, diritto.it; Cybersecurity360, *Chi governa l'AI? Il Tribunale annulla la sanzione a OpenAI e ridefinisce i confini del Garante privacy*, 2026, cybersecurity360.it. Data, motivi e stato del giudizio, che può proseguire in Cassazione, vanno verificati sul testo della sentenza. Sullo sportello unico: GDPR, artt. 56 e 60.

[^18]: Garante per la protezione dei dati personali, provvedimento 20 maggio 2024, n. 329, *Indicazioni per difendere i dati personali pubblicati online da soggetti pubblici e privati in qualità di titolari del trattamento dal web scraping finalizzato all'addestramento di modelli di intelligenza artificiale generativa*, in Gazzetta Ufficiale n. 132 del 7 giugno 2024, garanteprivacy.it.

[^19]: AI Act, cit., art. 53, par. 1, lett. d), applicabile dal 2 agosto 2025; il modello per la sintesi è stato pubblicato dalla Commissione europea nel luglio 2025, digital-strategy.ec.europa.eu. Per i modelli immessi sul mercato prima di quella data il termine è il 2 agosto 2027 (art. 111, par. 3).

[^20]: GDPR, art. 4, n. 12; EDPB, *Linee guida 9/2022 sulla notifica delle violazioni dei dati personali ai sensi del GDPR*, versione 2.0, 2023, edpb.europa.eu; EDPB, *Linee guida 01/2021 su esempi riguardanti la notifica di una violazione dei dati personali*, 2021, edpb.europa.eu.

[^21]: Malwarebytes, *OpenAI kills "short-lived experiment" where ChatGPT chats could be found on Google*, 2025, malwarebytes.com. L'opzione permetteva di rendere rintracciabili dai motori di ricerca le conversazioni condivise con un link; OpenAI l'ha ritirata tra la fine di luglio e l'inizio di agosto 2025.

[^22]: GDPR, art. 32, parr. 1 e 4; sulle impostazioni predefinite dello strumento, art. 25.

[^23]: EDPB, *Linee guida 9/2022*, cit., sul momento in cui il titolare viene a conoscenza della violazione.

[^24]: GDPR, artt. 33 e 34. La notifica si effettua con la procedura telematica indicata nella pagina dedicata alle violazioni di dati personali del sito garanteprivacy.it.

[^25]: Commissione europea, proposta di regolamento COM(2025) 837 del 19 novembre 2025, che modifica tra l'altro l'art. 33 del GDPR, eur-lex.europa.eu. L'EDPB e il Garante europeo della protezione dei dati hanno adottato un parere congiunto sulla proposta nel febbraio 2026, edpb.europa.eu. Sullo stato del negoziato si veda il capitolo sui principi del GDPR; l'iter va comunque verificato su eur-lex.europa.eu alla data di lettura.

[^26]: GDPR, artt. 35, par. 2, 37, 38 e 39; Gruppo di lavoro Articolo 29 per la protezione dei dati, *Linee guida sui responsabili della protezione dei dati* (WP243 rev.01), 2017, ec.europa.eu, fatte proprie dall'EDPB.

[^27]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale*, art. 17, commi 1 e 1-sexies, normattiva.it; Ministro per la pubblica amministrazione, *Circolare n. 3 del 1° ottobre 2018 sul Responsabile per la transizione al digitale*, 2018, funzionepubblica.gov.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 29 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- L'esempio di accesso da remoto ('tecnici dell'assistenza del fornitore che lavorano negli Stati Uniti') era impreciso.
- Per l'impugnazione Latombe la bozza indicava un numero di causa preciso (C-703/25 P) e una data di deposito che non sono nella base fattuale e non si possono verificare.
- La bozza dava per certo l'annullamento della sanzione OpenAI 'il 18 marzo 2026', con i relativi motivi, senza una fonte primaria.
- La sintesi finale diceva 'se c'è un rischio, il Comune ha 72 ore', che è il criterio sbagliato.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
