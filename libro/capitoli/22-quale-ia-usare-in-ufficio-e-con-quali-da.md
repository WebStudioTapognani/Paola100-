# Quale IA usare in ufficio e con quali dati

In questo capitolo: le quattro famiglie di strumenti di IA disponibili nel 2026, la differenza tra account personale e strumento dell'ente, la regola del semaforo per i dati, le istruzioni persistenti, i modelli in locale e le domande da fare all'amministratore di sistema.

## Due domande prima del prompt

Il capitolo sul metodo del prompt spiega come chiedere una bozza. Prima vengono due domande, che vanno insieme: con quale strumento e con quali dati. Un prompt sbagliato produce una bozza peggiore, che si corregge. Uno strumento sbagliato, con i dati sbagliati, può produrre una violazione di dati personali, che nessuna correzione cancella.

Nella scena con cui si apre il capitolo sull'IA già in ufficio, l'istruttrice dei Servizi sociali di Borgo Esempio incolla in un chatbot gratuito, dal telefono, prima un bando regionale e poi l'e-mail di una cittadina con la diagnosi del figlio. Al piano di sopra il tecnico scrive una determina con l'assistente della suite d'ufficio, di cui il Comune ha le licenze. Con la regola di questo capitolo i tre casi si separano. Il bando è un testo pubblico: va bene, purché l'ente abbia ammesso lo strumento, e a Borgo Esempio nessuno l'aveva fatto. L'e-mail non doveva entrare in nessun prompt. La determina nasce nello strumento giusto, ma cita un codice abrogato: lo strumento dell'ente protegge i dati, non la correttezza dell'atto.

Situazioni come queste non sono rare. Secondo la ricerca FPA del giugno 2026, nel 59% dei casi l'uso dell'IA da parte dei dipendenti pubblici è lasciato all'iniziativa individuale: avviene senza regole interne, formazione specifica, strumenti sicuri o linee guida.[^1] In quella condizione ciascuno risponde da solo alle due domande, spesso senza sapere di farlo. Questo capitolo dà un criterio per rispondere; le basi giuridiche sono nei capitoli sul GDPR e sull'AI Act.

## Le famiglie di strumenti

Nel 2026 un ufficio comunale incontra l'IA generativa in quattro forme. Si distinguono per tre aspetti: dove vanno i dati, chi ha firmato il contratto con il fornitore, che cosa il modello può leggere.

### I chatbot generalisti

Sono i servizi che si usano dal browser o da un'app: ChatGPT, Claude, Gemini, Copilot nella versione per il pubblico. Scrivono, riassumono, riformulano, rispondono a domande. Molti cercano sul web, leggono i file caricati e conservano informazioni tra una conversazione e l'altra.

Quasi tutti esistono in due versioni. Quella per i consumatori si attiva con un account personale, gratuito o a pagamento. Quella per le organizzazioni si attiva con un contratto dell'ente: per esempio ChatGPT Business, nome che dall'agosto 2025 ha preso il piano ChatGPT Team, o i piani Team ed Enterprise di Claude.[^2] Il modello può essere lo stesso. Cambiano le condizioni sui dati.

### L'IA nella suite d'ufficio

È l'assistente integrato nei programmi che l'ente usa già: Copilot nelle applicazioni di Microsoft 365, Gemini in Google Workspace. Rispetto al chatbot cambiano due cose. Si accede con l'account di lavoro, sotto il contratto che l'ente ha già firmato per la suite. E l'assistente, se l'ente lo consente, può leggere posta, documenti e cartelle condivise.

Una parte di queste funzioni è compresa nelle licenze che l'ente ha già. Microsoft 365 Copilot Chat è disponibile senza costi aggiuntivi per chi accede con l'account di lavoro, con la protezione prevista per i dati dell'organizzazione. Dal 2025 Microsoft porta la chat anche nel riquadro laterale di Word, Excel, PowerPoint e Outlook, pure per chi non ha la licenza Copilot, con impostazioni che l'amministratore può gestire.[^3] La licenza a pagamento di Microsoft 365 Copilot aggiunge la ricerca nei dati dell'organizzazione: posta, file, riunioni. Google, secondo la sua documentazione, ha inserito l'app Gemini tra i servizi principali di Workspace, con le garanzie contrattuali degli altri servizi, nelle principali edizioni Business, Enterprise ed Education.[^4] Le funzioni disponibili dipendono dall'edizione: chiedile all'amministratore.

Qui c'è un rischio che il chatbot, senza collegamenti ai dati dell'ente, non ha. L'assistente della suite può mostrare all'utente ogni contenuto che i suoi permessi gli consentono di vedere.[^5] Una cartella condivisa con permessi troppo larghi, che nessuno apriva, diventa leggibile con una domanda. Prima di collegare l'assistente ai dati dell'ente, i permessi vanno rivisti.

### Gli strumenti verticali

Sono prodotti costruiti per un settore: banche dati giuridiche con ricerca e sintesi assistite dall'IA, gestionali di atti e protocollo con funzioni di bozza o di classificazione, programmi di trascrizione delle sedute, assistenti virtuali per il sito istituzionale. Lavorano su fonti selezionate e dentro programmi che l'ufficio conosce già.

Non sono infallibili. In uno studio su tre strumenti professionali statunitensi di ricerca giuridica, che rispondono a partire da una banca dati, le risposte con errori sono state tra il 17% e il 33%.[^6] Meno di quanto misurato sui chatbot generalisti, ma non zero: le regole del capitolo sulla verifica delle norme valgono anche qui.

C'è poi un problema di contratto. Le funzioni di IA arrivano spesso con l'aggiornamento di un programma che l'ente usa da anni, e a volte si trovano già attive. Prima di usarle, il responsabile del servizio chiede al fornitore se il contratto e l'accordo sul trattamento dei dati le coprono, dove sono trattati i dati, se servono ad addestrare modelli e se le funzioni si possono disattivare.

### I modelli in locale

Sono modelli scaricati e fatti girare su un computer o su un server dell'ente. Prompt e risposte non escono dall'ente. Servono in pochi casi e hanno limiti precisi: ne parla una sezione più avanti.

| Famiglia | Dove vanno i dati | Contratto dell'ente | Uso tipico |
|---|---|---|---|
| Chatbot, account personale | al fornitore | nessuno | testi senza dati |
| Chatbot, piano per l'ente | al fornitore | sì | bozze con segnaposto |
| Suite d'ufficio | al fornitore della suite | sì, con la suite | bozze, posta, sintesi |
| Strumento verticale | al fornitore del prodotto | da verificare | ricerca, gestione atti |
| Modello in locale | restano nell'ente | solo licenza | casi delicati, con cautela |

### Non chiederlo al modello

Un modello non conosce il contratto con cui lo stai usando né le impostazioni del tuo account. Se gli chiedi se i tuoi dati sono al sicuro, risponde con ciò che è probabile, come fa con le norme. Le risposte vere sono nelle condizioni d'uso, nell'accordo sul trattamento e nelle impostazioni, e le verifica chi gestisce i sistemi dell'ente.

## Account personale o strumento dell'ente

### Non conta il prezzo, conta il contratto

Il capitolo sul GDPR dedicato ai fornitori lo spiega in dettaglio. Un abbonamento personale a pagamento resta un servizio per consumatori, in cui le conversazioni possono servire ad addestrare i modelli se l'utente non lo esclude.[^7] Di regola solo il servizio per l'ente prevede un accordo che rende il fornitore responsabile del trattamento per conto del Comune (art. 28 del Regolamento (UE) 2016/679, GDPR). Qui contano le conseguenze pratiche.

### L'indirizzo dell'ente non basta

Registrarti a un servizio per consumatori con l'indirizzo di posta dell'ente non lo trasforma in uno strumento dell'ente. Il contratto resta quello che hai accettato tu, come persona.

Vale anche il contrario: lo strumento dell'ente protegge i dati solo se entri con l'account di lavoro. Il caso più frequente è Copilot. Lo stesso nome indica il servizio per il pubblico, a cui si accede con un account Microsoft personale, e Microsoft 365 Copilot Chat, a cui si accede con l'account di lavoro gestito dall'ente: solo il secondo ha la protezione prevista per i dati delle organizzazioni.[^8] Lo stesso vale per Gemini, con l'account Google personale o con quello di Workspace. Prima di incollare un testo, controlla con quale account sei entrato. Se nello stesso browser è aperto anche un account personale, il rischio di confonderli è concreto: tieni separati i profili del browser.

### Che cosa dà all'ente lo strumento dell'ente

Oltre al contratto, lo strumento dell'ente dà ciò che un account personale non può dare.

- *Accessi.* L'amministratore attiva e disattiva gli utenti, impone l'autenticazione a più fattori, sceglie quali funzioni lasciare accese.
- *Continuità.* Quando un dipendente cambia ufficio o lascia l'ente, l'ente può decidere che cosa conservare, nei limiti delle funzioni del servizio. Su un account personale non decide nulla.
- *Tracciabilità.* La L. 23 settembre 2025, n. 132, chiede alle amministrazioni di assicurare "la tracciabilità" dell'uso dell'IA (art. 14, comma 1).[^9] Con lo strumento dell'ente almeno si sa chi lo usa. Con gli account personali no.
- *Condivisione.* Progetti e istruzioni si condividono con i colleghi, e la libreria dell'ufficio diventa possibile (si veda il capitolo sul flusso di lavoro).
- *Regole.* Il codice di comportamento disciplina l'uso delle tecnologie informatiche da parte dei dipendenti pubblici, e ogni ente lo integra con il proprio.[^10] Usare lo strumento dell'ente è il modo più semplice per rispettare queste regole.

### Se l'ente ammette l'account personale

In attesa di uno strumento proprio, alcuni enti ammettono per iscritto l'account personale per i testi senza dati. Se è il tuo caso:

- usa solo testi verdi, secondo la regola del semaforo che segue;
- disattiva l'uso delle conversazioni per l'addestramento, se l'impostazione esiste;
- disattiva la memoria tra le conversazioni;
- non collegare all'account la posta, i file o il calendario dell'ente;
- non installare app o estensioni del browser sui computer dell'ente senza autorizzazione;
- conserva l'autorizzazione scritta.

Disattivare l'addestramento riduce un rischio, ma non cambia il contratto. I testi restano a un fornitore che li tratta secondo condizioni proprie, che può modificare.

## La regola del semaforo

Il semaforo classifica ciò che entra nel prompt, compresi i file caricati. Il colore dipende dai dati e dalle informazioni, non dal tipo di atto: la stessa determina può essere verde o gialla secondo ciò che scrivi. A ogni colore corrisponde uno strumento.

| Colore | Cosa entra nel prompt | Strumento | Esempio |
|---|---|---|---|
| Verde | nessun dato personale né riservato | ogni strumento ammesso per iscritto | avviso di chiusura di una strada |
| Giallo | dati comuni con segnaposto; informazioni riservate | solo quello dell'ente, con l'art. 28 | ordinanza a PROPRIETARIO_1 |
| Rosso | salute, reati, minori, segreti, credenziali | nessuno: restano fuori | relazione sociale su un minore |

### Verde

Verde è ciò che non riguarda nessuna persona e non contiene informazioni riservate: norme, circolari, bandi già pubblicati, modelli generici, regole di stile, bozze di atti di routine senza persone fisiche. Va bene ogni strumento ammesso per iscritto dall'ente, compreso l'account personale se l'ente lo consente.

A Borgo Esempio sono verdi, per esempio:

- per gli Affari generali, la determina di rinnovo dell'abbonamento a una banca dati di Editrice Esempio S.r.l., senza il nome del RUP;
- per il Finanziario, la sintesi delle novità della legge di bilancio per i Comuni, a partire dal testo pubblicato;
- per il Tecnico, l'avviso ai cittadini sulla chiusura di una strada per lavori.

Il verde si perde facilmente. I dati di una società non sono dati personali; il nome di un professionista o di una ditta individuale sì. La determina di contributo all'ASD Borgo Esempio è verde; diventa gialla quando aggiungi il nome del presidente. E verde non vuol dire verificato: le norme di una bozza verde si controllano come tutte le altre. Se poi il testo generato è pubblicato per informare i cittadini su questioni di interesse pubblico, conta anche l'obbligo di trasparenza dell'AI Act, che non si applica al testo rivisto da una persona che ne ha la responsabilità editoriale (si veda il capitolo sull'AI Act).[^11]

### Giallo

Giallo sono i dati personali comuni e le informazioni interne riservate, che l'ente non ha deciso di rendere note: trattative, valutazioni, scelte ancora in discussione. Entrano solo nello strumento dell'ente, con il contratto dell'art. 28 GDPR, e solo nella misura necessaria: identificativi sostituiti dai segnaposto e dettagli ridotti al minimo, come spiega il capitolo sul metodo del prompt.

A Borgo Esempio sono gialli, per esempio:

- per il Tecnico, l'ordinanza di rimozione di rifiuti abbandonati su un terreno privato, con PROPRIETARIO_1 e IMMOBILE_1 al posto di nome e dati catastali;
- per i Demografici, la comunicazione di avvio del procedimento di cancellazione anagrafica per irreperibilità, con DESTINATARIO_1 e senza indirizzo;
- per gli Affari generali, la lettera che contesta un disservizio a Editrice Esempio S.r.l. e annuncia una penale: non ci sono persone, ma è una contestazione ancora aperta, che l'ente non ha reso nota.

Il segnaposto riduce il rischio, non lo azzera, e non rende il testo anonimo. Per questo il giallo resta giallo anche dopo la sostituzione dei nomi, e non va mai in un account personale.

### Rosso

Rosso è ciò che resta fuori dal prompt con qualunque strumento, anche con quello dell'ente:

- le categorie particolari di dati dell'art. 9 GDPR: salute e disabilità, origine razziale o etnica, opinioni politiche, convinzioni religiose o filosofiche, appartenenza sindacale, vita o orientamento sessuale, dati genetici e biometrici;
- i dati relativi a condanne penali e reati (art. 10 GDPR);
- i dati dei minori, che il GDPR protegge in modo specifico (considerando 38);
- i documenti sottratti all'accesso o coperti da segreto (art. 24 della L. 7 agosto 1990, n. 241);
- password, credenziali e configurazioni dei sistemi informatici.

A questi si aggiungono i dettagli che, combinati, rendono riconoscibile una persona in un paese di 6.500 abitanti: frazione, età, mestiere, parentela, un fatto noto. Vanno tolti anche dai testi gialli.

Rosso non vuol dire che il Comune non possa trattare quei dati. Li tratta ogni giorno nei procedimenti, nei casi previsti dalla legge.[^12] Vuol dire che per scrivere una bozza non servono, e che il prompt non è il posto dove metterli. Al loro posto scrivi il requisito o la norma applicata: "in possesso del requisito previsto dall'art. [n] del regolamento", non la diagnosi. Usa anche questa formula solo se serve: accanto a data e oggetto della pratica, può rivelare il dato che volevi tenere fuori. Il ragionamento completo è nel capitolo sui principi del GDPR.

Per chi scrive, il rosso non ha eccezioni. Diverso è il caso in cui il dato rosso è l'oggetto stesso del lavoro, come nel controllo di un atto prima della pubblicazione. Lì non decide il singolo con un prompt. Decide l'ente, con uno strumento scelto per quel compito, il parere del responsabile della protezione dei dati e la valutazione d'impatto: se ne parla nella sezione sui modelli in locale.

A Borgo Esempio sono rossi, per esempio: i permessi chiesti da un dipendente per assistere un familiare con disabilità, per gli Affari generali; la pratica di un'unione civile, per i Demografici; la verifica dei requisiti di un operatore economico con una condanna, per il Tecnico.

### Una pratica, tre colori

Il colore non dipende dalla pratica, ma dalla parte della pratica che entra nel prompt. I Servizi sociali istruiscono la domanda di contributo per l'affitto di una famiglia con due figli.

- *Verde.* La sintesi dei requisiti del bando regionale e lo schema della comunicazione di esito, senza alcun dato della famiglia.
- *Giallo.* La comunicazione di avvio del procedimento a RICHIEDENTE_1, con il protocollo della domanda come PROT_1 e l'importo richiesto, nello strumento dell'ente.
- *Rosso.* La relazione dell'assistente sociale, che parla della salute di un figlio. Resta nel fascicolo. Se nella motivazione serve un requisito, si scrive il requisito.
- *Uso rosso.* Chiedere al modello se la famiglia ha diritto al contributo, o in quale posizione deve entrare in graduatoria.

Il colore vale per tutta la conversazione. Se in una chat verde incolli un testo giallo, la chat diventa gialla, e con lei il progetto in cui si trova.

### Gli usi rossi

Alcuni usi sono rossi qualunque siano i dati e qualunque sia lo strumento. Non chiedere all'IA:

- se una persona ha diritto a una prestazione, a un contributo, a un'esenzione;
- di assegnare punteggi a persone o di ordinarle in una graduatoria;
- di valutare l'attendibilità di una dichiarazione o il comportamento di una persona;
- quale decisione prendere in un provvedimento.

È una scelta prudente di questo libro, che si appoggia su tre norme. Le decisioni basate unicamente sul trattamento automatizzato, che producono effetti giuridici sulla persona o incidono in modo analogo significativamente su di lei, sono vietate in linea di principio (art. 22 GDPR). I sistemi usati per valutare il diritto a prestazioni di assistenza pubblica essenziali sono ad alto rischio (AI Act, Allegato III, punto 5, lettera a)). E per la L. 132/2025 l'IA opera "in funzione strumentale e di supporto", mentre la persona "resta l'unica responsabile" del provvedimento (art. 14, comma 2).[^13] I dettagli sono nel capitolo sull'AI Act.

### Nel dubbio

Nel dubbio scegli il colore più prudente e chiedi al responsabile della protezione dei dati. Quattro domande, prima di incollare:

1. Se questo testo finisse domani sul sito del Comune, dovrei oscurare qualcosa? Se sì, non è verde.
2. Contiene informazioni che l'ente non ha ancora deciso di rendere note? Se sì, non è verde.
3. Qualcuno in paese potrebbe riconoscere la persona, anche senza nome? Se sì, togli i dettagli.
4. C'è un dato di salute, di un reato, di un minore? Se sì, è rosso.

Le domande le fai tu, prima del prompt. Chiedere al modello se un testo contiene dati personali significa averglielo già dato.

## Le istruzioni persistenti: Progetti, Gem, agenti Copilot

Ruolo, file di stile, elenco delle norme e vincoli si ripetono in ogni richiesta. Gli strumenti permettono di salvarli una volta sola, come istruzioni persistenti, insieme ai documenti di riferimento. Il capitolo sul metodo del prompt spiega che cosa scrivere; qui si vede dove salvarlo e con quali cautele.

| Prodotto | Funzione | Senza costi aggiuntivi |
|---|---|---|
| ChatGPT | Progetti | sì, dal settembre 2025, con limiti |
| Claude | Progetti | sì, fino a cinque progetti |
| Gemini | Gem | sì, dal marzo 2025 |
| Copilot Chat | agenti | istruzioni e web; file solo a consumo |
| NotebookLM | taccuini di fonti | sì |

*Progetti.* In ChatGPT e in Claude raccolgono conversazioni, documenti di riferimento e istruzioni valide per tutte le chat del progetto. In ChatGPT la memoria si può limitare al progetto, senza attingere a quella del resto dell'account.[^14]

*Gem.* In Gemini sono versioni personalizzate dell'assistente, con istruzioni e, se servono, file. Dal settembre 2025 si possono condividere come un file di Google Drive, decidendo chi può solo usarli e chi anche modificarli.[^15]

*Agenti.* In Microsoft 365 Copilot Chat si creano con Agent Builder, con istruzioni fino a 8.000 caratteri. Senza licenza Copilot gli agenti usano istruzioni e ricerca web. File incorporati, dati di SharePoint e connettori richiedono che l'ente attivi la fatturazione a consumo.[^16]

*Taccuini.* NotebookLM, che dal 16 luglio 2026 si chiama Gemini Notebook, serve meno a salvare istruzioni e più a raccogliere fonti: risponde a partire dai documenti caricati e indica il passo da cui prende ogni informazione.[^17] È utile quando devi leggere molti documenti (si veda il capitolo sull'istruttoria).

Disponibilità e limiti cambiano spesso: numero di progetti, di file, di caratteri. Prima di costruire il lavoro dell'ufficio su una funzione, verificala nelle pagine di assistenza del produttore.

### Come organizzarle

- Un progetto per tipo di atto e per servizio: "Determine di affidamento – Affari generali", non "Lavoro".
- Nelle istruzioni: ruolo, rinvio al file di stile, vincoli. Nei documenti di riferimento: file di stile, atti modello senza dati personali ed elenco delle norme verificate, con la data della verifica.
- Nessun dato personale nei documenti di riferimento: restano nel progetto per tutte le conversazioni future, e chi riceve il progetto condiviso li vede.
- Il semaforo vale anche per il progetto. Un progetto in un account personale è verde, sempre.
- Versione e data in testa alle istruzioni. Quando cambi il file di stile, aggiorni il progetto e rifai un caso di prova.
- Progetti, Gem e agenti si condividono solo nello strumento dell'ente, con i colleghi che ne hanno bisogno. Le credenziali di un account non si condividono mai.

### Le istruzioni di un progetto

Un modello da adattare. Il file di stile e l'elenco delle norme vanno tra i documenti di riferimento.

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

La riga sul colore del progetto non è una protezione. Quando il modello si accorge di un dato rosso, il dato è già arrivato al fornitore; e il modello può anche non accorgersene. Serve a farti notare l'errore subito. In quel caso fai come indica il capitolo sul metodo del prompt per i dati incollati per errore: annota cosa e quando, cancella la conversazione, avvisa il responsabile e il responsabile della protezione dei dati. Il controllo vero resta il tuo, prima di incollare. Allo stesso modo, se il modello valuta comunque una persona, cancella la valutazione dalla bozza.

### Che cosa offrono, e che cosa no, le versioni gratuite

Le versioni gratuite hanno quasi sempre le funzioni di base: progetti o Gem, caricamento di file, spesso la memoria. Mancano tre cose: il contratto con l'ente, la gestione degli accessi, la condivisione controllata. Bastano per esercitarsi su casi inventati come quelli di Borgo Esempio e, se l'ente lo ammette per iscritto, per i testi verdi. Per tutto il resto no.

## Modelli in locale per i dati delicati

### Che cosa sono

Un modello in locale è un modello linguistico scaricato e fatto girare su un computer o su un server dell'ente. Molti modelli sono distribuiti "a pesi aperti": si possono scaricare e usare secondo la loro licenza. Programmi appositi li installano e offrono una finestra di chat simile a quella dei servizi on line.[^18] Dopo l'installazione possono funzionare senza collegamento a internet: prompt e risposte restano sul computer.

### Quando servono

Il modello in locale non è la soluzione per tutto. Serve soprattutto in due casi:

- un testo giallo va lavorato e l'ente non ha ancora uno strumento in cloud con un contratto adeguato;
- il compito richiede proprio il testo con i dati e l'ente ha scelto il modello in locale per quel compito: per esempio, cercare in una delibera i dati personali da oscurare prima della pubblicazione (si veda il capitolo sulla privacy prima della pubblicazione).

Il semaforo non cambia colore da solo. Il modello in locale elimina la trasmissione al fornitore, non gli altri obblighi: minimizzazione, sicurezza, registro dei trattamenti. Il dato che non serve resta fuori anche qui, e i dati rossi restano fuori dai tuoi prompt. Se un compito richiede davvero quei dati, come il controllo prima della pubblicazione, lo decide l'ente, non il singolo: con il parere del responsabile della protezione dei dati, misure di sicurezza adeguate e la valutazione d'impatto, di regola necessaria quando l'IA tratta dati di questo tipo.[^19]

### I limiti

*Qualità.* I modelli che girano su un computer d'ufficio sono molto più piccoli di quelli dei servizi on line. Scrivono peggio, seguono meno le istruzioni lunghe e conoscono meno fatti, quindi anche meno norme. Usali su testi che fornisci tu, non per cercare informazioni.

*Aggiornamento.* Il modello conosce solo ciò che ha visto in addestramento e non cerca sul web. Una norma cambiata dopo quella data, per lui, non esiste (si veda il capitolo che spiega come funziona un modello linguistico).

*Hardware.* Un modello piccolo gira su un computer recente con molta memoria; uno più capace richiede una scheda grafica dedicata o un server. Su un computer d'ufficio datato una risposta può richiedere minuti.

*Sicurezza.* I dati non vanno al fornitore, ma restano sul computer: cronologia delle chat, file caricati, copie temporanee. Quel computer va protetto come ogni archivio dell'ente.

*Licenza e installazione.* Ogni modello ha la sua licenza: alcune sono libere, altre pongono limiti d'uso. Non installare tu né il programma né il modello. Lo decide e lo fa l'amministratore di sistema, che controlla anche la licenza e che il programma non trasmetta dati all'esterno.

*Ruoli.* Il Comune che usa così com'è un programma con un modello scaricato è un deployer, come con un servizio on line. Se invece integra il modello in un proprio programma, o lo modifica, può assumere obblighi da fornitore, anche se lo usa solo al proprio interno.[^20] Ne parla il capitolo sull'AI Act.

### Un prompt per il modello in locale

I modelli piccoli rendono meglio con compiti brevi e istruzioni semplici: un compito per volta, nessuna richiesta di norme. Il prompt che segue serve al controllo prima della pubblicazione: usalo solo con il modello che l'ente ha scelto per quel compito.

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

Prova il prompt prima su un atto inventato di Borgo Esempio, in cui sai quali dati hai messo, e conta quanti ne trova. Un modello piccolo ne perde qualcuno: la tabella aiuta la rilettura, non la sostituisce. Se ne perde molti, il modello non è adatto al compito.

## Licenze, costi e permessi: cosa chiedere all'amministratore di sistema

### Chi decide

Lo strumento lo sceglie l'ente, titolare del trattamento, non il singolo dipendente. A Borgo Esempio il responsabile del Servizio Affari generali, competente per i sistemi informatici, cura l'acquisto e firma la determina. L'amministratore di sistema, una ditta esterna, configura account, permessi e impostazioni. Il responsabile per la transizione al digitale coordina le scelte tecnologiche;[^21] il responsabile della protezione dei dati dà il suo parere su contratto, rischi e valutazione d'impatto; il segretario comunale coordina la stesura delle regole interne sull'uso dell'IA (si veda il capitolo sul regolamento interno).

### Quanto costa

- *Gratis, ma non per i dati.* Le versioni per consumatori. Vanno bene per esercitarsi e, se l'ente lo ammette per iscritto, per i testi verdi.
- *Compreso nelle licenze.* Copilot Chat con l'account di lavoro, l'app Gemini nelle edizioni di Workspace che la prevedono. Non costano nulla in più, ma vanno configurati.
- *Per utente.* La licenza di Microsoft 365 Copilot, i piani per le organizzazioni di ChatGPT e Claude e le edizioni di Workspace si pagano per utente, con canone mensile o annuale. Dalla fine del 2025 Microsoft offre alle organizzazioni fino a 300 utenti una versione a listino più basso, Microsoft 365 Copilot Business.[^22]
- *A consumo.* Alcune funzioni si pagano in base all'uso, come gli agenti con accesso ai file dell'ente in Copilot Chat. Il costo va stimato prima e controllato dopo.
- *In locale.* Molti modelli sono gratuiti; non lo sono il computer adatto e il tempo di chi lo installa e lo mantiene.

Non serve una licenza a pagamento per tutti. Si comincia dai servizi che scrivono più atti, si misura il risultato e poi si decide se estendere (si veda il capitolo sulla scelta e l'acquisto di uno strumento).

### Come si acquista

L'acquisto segue il Codice dei contratti pubblici (D.Lgs. 31 marzo 2023, n. 36) e le regole sui beni e servizi informatici. Per questi le amministrazioni usano gli strumenti di acquisto e negoziazione di Consip o dei soggetti aggregatori, per ciò che è disponibile presso di loro, salvo le deroghe motivate previste dalla stessa legge (art. 1, commi 512 e 516, della L. 28 dicembre 2015, n. 208).[^23] I servizi in cloud usati dalla pubblica amministrazione devono essere qualificati dall'Agenzia per la cybersicurezza nazionale (ACN).[^24] Nel marzo 2026 l'Agenzia per l'Italia Digitale (AgID) ha posto in consultazione una bozza di linee guida sul procurement di IA nella pubblica amministrazione, che alla data di aggiornamento del volume non risulta adottata in via definitiva.[^25] Il percorso completo, dal fabbisogno al contratto, è nel capitolo sulla scelta e l'acquisto di uno strumento.

### Le impostazioni che contano

Le impostazioni contano quanto il contratto. Tre meritano attenzione particolare.

- *Connettori.* Collegano l'assistente a posta, cartelle condivise e gestionali. Sono utili, ma estendono ciò che il modello legge: vanno attivati solo dopo la revisione dei permessi.
- *Ricerca sul web.* Porta nella risposta fonti non controllate. Per gli atti è meglio partire dall'elenco delle norme verificate e usare la ricerca solo quando serve.
- *Estensioni del browser.* Quelle con funzioni di IA possono leggere le pagine che apri, compresi i gestionali dell'ente.

### La richiesta all'amministratore di sistema

Per sapere come stanno le cose nel tuo ente, scrivi all'amministratore di sistema. Una richiesta da adattare:

```
Oggetto: strumenti di IA – impostazioni per il Servizio [nome]

All'amministratore di sistema
e p.c. al responsabile del Servizio [nome],
al responsabile per la transizione al digitale
e al responsabile della protezione dei dati

Per usare l'IA nel lavoro del servizio, secondo le regole dell'ente,
chiedo di sapere:
1. quali strumenti di IA sono autorizzati e con quale account si accede;
2. se per ciascuno è in vigore un accordo sul trattamento dei dati
   (art. 28 GDPR) e se esclude l'uso dei dati per addestrare i modelli;
3. dove sono trattati i dati, per quanto sono conservati prompt e
   risposte e se il servizio cloud è qualificato dall'ACN;
4. se sono attive la memoria tra le conversazioni, la ricerca sul web
   e il caricamento di file, e se posso disattivarle;
5. a quali dati dell'ente può accedere lo strumento (posta, cartelle
   condivise, gestionali) e se i permessi sono stati rivisti;
6. se posso creare e condividere progetti, Gem o agenti, e con chi;
7. se l'uso viene registrato e chi può consultare i registri;
8. se posso usare estensioni del browser o modelli in locale, o se
   devo chiederlo caso per caso;
9. a chi segnalare un errore, come dati incollati per sbaglio.

[nome e cognome], [qualifica]
```

Conserva la risposta. Anche un "non lo so" è un'informazione: finché manca una risposta sui punti 1, 2 e 5, lo strumento non è pronto per i testi gialli.

## In sintesi

- Prima del prompt, due domande: con quale strumento e con quali dati.
- Non conta il prezzo, conta il contratto. Un account personale resta personale anche se a pagamento o registrato con l'indirizzo dell'ente; lo strumento dell'ente protegge i dati solo se entri con l'account di lavoro.
- Verde: nessun dato personale né riservato, con ogni strumento ammesso per iscritto. Giallo: dati comuni ridotti e con segnaposto, informazioni interne riservate, solo nello strumento dell'ente con l'accordo dell'art. 28 GDPR. Rosso: salute, reati, minori, segreti, credenziali, fuori dai tuoi prompt con qualunque strumento; un controllo che li richieda lo decide l'ente, con la valutazione d'impatto.
- Alcuni usi sono rossi in ogni caso: stabilire chi ha diritto a una prestazione, fare graduatorie di persone, decidere il provvedimento.
- Le istruzioni persistenti (Progetti, Gem, agenti) si organizzano per tipo di atto: regole nelle istruzioni, atti modello senza dati nei documenti di riferimento.
- Il modello in locale elimina la trasmissione al fornitore, non gli altri obblighi: è meno capace, non si aggiorna, va protetto e installato dall'ente.
- Contratto, impostazioni e permessi si chiedono per iscritto all'amministratore di sistema, non al modello.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 34 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Dato FPA distorto: il 59% era attribuito ai 'dipendenti pubblici intervistati', mentre la fonte parla del 59% dei casi d'uso lasciati all'iniziativa individuale.
- Citato un numero del Centro messaggi Microsoft (MC1096218) non verificabile, con l'affermazione non riscontrata che la chat nelle app compare solo se l'amministratore la abilita.
- Lo studio di Stanford sugli strumenti giuridici (17-33%) era presentato come 'negli studi', al plurale, e confrontato con i chatbot generalisti come se il dato venisse dallo stesso studio.
- Nella sezione sull'account personale, usato solo per testi verdi, si diceva che 'i dati' restano al fornitore: corretto in 'i testi'.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.

[^1]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, su un campione di 500 dipendenti pubblici, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Solo il 41% segnala azioni di supporto della propria amministrazione. Sono dati dichiarati dagli intervistati.

[^2]: OpenAI, *ChatGPT Team is now ChatGPT Business*, 2025, help.openai.com: il cambio di nome, dalla fine di agosto 2025, non ha modificato funzioni, prezzi e limiti; nel piano Business i dati sono esclusi per impostazione predefinita dall'addestramento. Per Claude: Anthropic, *Commercial Terms of Service*, 2025, anthropic.com, che si applicano ai piani Team ed Enterprise e all'uso tramite API. I nomi dei piani cambiano spesso: verificali sulle pagine dei produttori.

[^3]: Microsoft, *Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat*, 2026, learn.microsoft.com, secondo cui la protezione si applica senza costi aggiuntivi a chi accede con un account Microsoft Entra di lavoro o di istituto. L'estensione della chat alle applicazioni di Microsoft 365 per gli utenti senza licenza Microsoft 365 Copilot è stata annunciata da Microsoft nel 2025 nel Centro messaggi di Microsoft 365, che l'amministratore dell'ente può consultare.

[^4]: Google, *Google Workspace with Gemini FAQ*, 2026, knowledge.workspace.google.com: con le edizioni che la comprendono, l'app Gemini è un servizio principale di Workspace con protezione dei dati di livello aziendale, e prompt e risposte non sono letti da revisori umani né usati per addestrare i modelli senza autorizzazione. Per scuole e università: Google, *NotebookLM and Gemini app core services for education customers*, 2025, workspaceupdates.googleblog.com.

[^5]: Microsoft, *Data, Privacy, and Security for Microsoft 365 Copilot*, 2026, learn.microsoft.com: l'assistente mostra i contenuti dell'organizzazione per i quali l'utente ha almeno il permesso di visualizzazione. Si veda anche il capitolo sui principi del GDPR.

[^6]: V. Magesh, F. Surani, M. Dahl, M. Suzgun, C. D. Manning, D. E. Ho, *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, in Journal of Empirical Legal Studies, vol. 22, 2025, pp. 216-242, law.stanford.edu, sugli strumenti di LexisNexis e Thomson Reuters. Lo studio conta come errore anche la risposta fondata su una fonte che non dice ciò che le si attribuisce. Riguarda il diritto statunitense; nelle ricerche per questo libro non sono emerse misure comparabili sulle banche dati italiane. Per i chatbot generalisti si veda il capitolo sul metodo del prompt.

[^7]: Per esempio, con l'aggiornamento dei termini per i consumatori annunciato il 28 agosto 2025, nei piani personali di Claude (Free, Pro e Max) le conversazioni possono essere usate per addestrare i modelli se l'utente non disattiva l'impostazione: Anthropic, *Updates to Consumer Terms and Privacy Policy*, 2025, anthropic.com. Anche gli altri produttori distinguono in genere tra condizioni per consumatori e per organizzazioni: vanno lette, strumento per strumento, alla data d'uso.

[^8]: Microsoft, *Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat*, cit.; per Gemini, Google, *Google Workspace with Gemini FAQ*, cit.

[^9]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 1, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, gazzettaufficiale.it. Il comma 1 chiede di assicurare agli interessati "la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo".

[^10]: D.P.R. 16 aprile 2013, n. 62, *Regolamento recante codice di comportamento dei dipendenti pubblici*, art. 11-bis, inserito dal D.P.R. 13 giugno 2023, n. 81; D.Lgs. 30 marzo 2001, n. 165, art. 54, comma 5, sul codice di comportamento di ciascuna amministrazione, normattiva.it.

[^11]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale (AI Act), art. 50, par. 4, secondo comma, eur-lex.europa.eu. L'obbligo di rendere noto che il testo è stato generato o manipolato artificialmente si applica ai deployer dal 2 agosto 2026 e non è stato rinviato dal Regolamento (UE) 2026/1744. Non si applica se il contenuto è stato sottoposto a revisione umana o a controllo editoriale e una persona fisica o giuridica ha la responsabilità editoriale della pubblicazione.

[^12]: Per le categorie particolari di dati, Regolamento (UE) 2016/679, art. 9, par. 2, lett. g), e D.Lgs. 30 giugno 2003, n. 196, art. 2-sexies, sui trattamenti necessari per motivi di interesse pubblico rilevante; per i dati giudiziari, art. 10 GDPR e art. 2-octies del D.Lgs. 196/2003; per i minori, considerando 38 GDPR; per i documenti esclusi dall'accesso, L. 7 agosto 1990, n. 241, art. 24, normattiva.it ed eur-lex.europa.eu. I dati relativi alla salute non possono essere diffusi (art. 2-septies, comma 8, D.Lgs. 196/2003).

[^13]: Regolamento (UE) 2016/679, art. 22; Regolamento (UE) 2024/1689, cit., Allegato III, punto 5, lettera a), i cui obblighi per i deployer dei sistemi ad alto rischio si applicano dal 2 dicembre 2027 per effetto del Regolamento (UE) 2026/1744, eur-lex.europa.eu; L. 23 settembre 2025, n. 132, cit., art. 14, comma 2.

[^14]: OpenAI, *Projects in ChatGPT*, 2026, help.openai.com, che indica per ciascun piano, compreso quello gratuito, i limiti di file per progetto e le opzioni di memoria del progetto; i progetti sono disponibili anche nel piano gratuito dal settembre 2025. Anthropic, *What are projects?*, 2026, support.claude.com, secondo cui nel piano gratuito si possono creare fino a cinque progetti.

[^15]: Tom's Guide, *Google Gemini Gems now available to all users without a subscription*, 2025, tomsguide.com, sulla disponibilità gratuita dal marzo 2025; TechCrunch, *Google now lets you share your custom Gemini AI assistants known as Gems*, 2025, techcrunch.com, sulla condivisione dal settembre 2025. Prima dell'uso va verificato se la funzione è attiva per l'account Workspace dell'ente.

[^16]: Microsoft, *Agent capabilities and licensing*, 2026, e *Write effective instructions for declarative agents*, 2026, github.com (documentazione ufficiale MicrosoftDocs). La fatturazione a consumo (pay-as-you-go) è addebitata in Copilot Credits.

[^17]: Google, *NotebookLM is now Gemini Notebook*, 2026, blog.google. Secondo l'annuncio cambiano nome e logo, non il funzionamento dello strumento.

[^18]: Due programmi diffusi sono Ollama (ollama.com) e LM Studio (lmstudio.ai). Sono citati come esempi, non come raccomandazione: condizioni d'uso per il lavoro, licenze dei modelli ed eventuali trasmissioni di dati all'esterno vanno verificate dall'amministratore di sistema prima dell'installazione.

[^19]: Regolamento (UE) 2016/679, artt. 5, 30, 32 e 35; Garante per la protezione dei dati personali, *Elenco delle tipologie di trattamenti soggetti al requisito di una valutazione d'impatto*, allegato 1 al provvedimento n. 467 dell'11 ottobre 2018, garanteprivacy.it, che comprende i trattamenti con tecnologie innovative, tra cui i sistemi di IA, quando ricorre almeno un altro dei criteri indicati dal Gruppo di lavoro Articolo 29 nelle linee guida WP 248 rev. 01. Tra quei criteri ci sono i dati sensibili o di carattere altamente personale.

[^20]: Regolamento (UE) 2024/1689, cit., art. 3, n. 3 (fornitore), n. 4 (deployer) e n. 11 (messa in servizio, che comprende la fornitura per uso proprio), e art. 25, sulle modifiche e sui cambi di finalità dei sistemi ad alto rischio, eur-lex.europa.eu. Quali obblighi ne derivino dipende dal livello di rischio del sistema.

[^21]: D.Lgs. 7 marzo 2005, n. 82, *Codice dell'amministrazione digitale* (CAD), art. 17, normattiva.it.

[^22]: Office Watch, *Microsoft Launches Cheaper Microsoft 365 Copilot Business, AI Add-On for Small Organizations*, 2025, office-watch.com. Secondo le fonti di settore il prezzo di listino era di 21 dollari per utente al mese, con promozioni temporanee. Prezzi, sconti e condizioni per la pubblica amministrazione cambiano e dipendono dal canale di acquisto: vanno verificati alla data della determina.

[^23]: L. 28 dicembre 2015, n. 208, art. 1, commi 512 e 516, normattiva.it. Il comma 516 ammette acquisti fuori da quegli strumenti solo con autorizzazione motivata dell'organo di vertice amministrativo, nei casi che indica, e ne prevede la comunicazione all'Autorità nazionale anticorruzione e all'AgID.

[^24]: Agenzia per la cybersicurezza nazionale, decreto direttoriale n. 21007/24 del 27 giugno 2024, che adotta il regolamento unico per le infrastrutture digitali e i servizi cloud della pubblica amministrazione, in vigore dal 1° agosto 2024, acn.gov.it.

[^25]: AgID, Determinazione n. 43 del 10 marzo 2026, che ha posto in consultazione, dal 12 marzo all'11 aprile 2026, le bozze di *Linee guida per lo sviluppo di sistemi di IA nella PA* e di *Linee guida per il procurement di IA nella PA*, agid.gov.it. L'iter prevede il parere della Conferenza unificata e le osservazioni del Garante privacy (art. 71 del CAD).
