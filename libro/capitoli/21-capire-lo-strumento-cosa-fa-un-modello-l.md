# Capire lo strumento: cosa fa un modello linguistico

In questo capitolo: come nasce una risposta, che cosa il modello sa e che cosa no, perché inventa norme e sentenze, come hanno reagito i giudici, perché chi rivede smette di controllare e quali compiti affidargli in ufficio.

## Perché un funzionario deve capire lo strumento

Per usare l'IA negli atti non serve diventare tecnici. Servono però tre nozioni: da dove viene il testo che ricevi, che cosa il modello può sapere, quando e perché sbaglia. Senza queste nozioni, le regole del metodo sembrano prudenza eccessiva. Con queste, diventano ovvie.

Sono anche il contenuto minimo dell'alfabetizzazione in materia di IA. Il Regolamento (UE) 2024/1689 (AI Act) la definisce come l'insieme di competenze, conoscenze e comprensione che consentono, tra l'altro, di "acquisire consapevolezza in merito alle opportunità e ai rischi dell'IA e ai possibili danni che essa può causare" (art. 3, n. 56). L'art. 4, riscritto dal Regolamento (UE) 2026/1744, chiede a fornitori e deployer, quindi anche al Comune che usa l'IA, di adottare misure per sostenere lo sviluppo di questa alfabetizzazione nel personale, tenendo conto delle conoscenze di ciascuno e del contesto d'uso.[^1]

Secondo la Commissione europea, il punto di partenza è una comprensione generale: che cos'è l'IA, come funziona, quali sistemi usa l'ente, quali opportunità e quali rischi comporta, tra cui le allucinazioni dell'IA generativa. Affidarsi alle sole istruzioni d'uso dello strumento, di regola, non basta.[^2] Per la pubblica amministrazione si aggiunge l'art. 14, comma 3, della L. 23 settembre 2025, n. 132, che chiede misure formative per "sviluppare le capacità trasversali degli utilizzatori".[^3]

Il capitolo sull'AI Act descrive l'obbligo, quello sulla formazione del personale il percorso. Questo capitolo ne fornisce il contenuto.

## Previsione di testo, non ricerca di norme: come nasce una risposta

### Un pezzo alla volta

Un modello linguistico è un programma addestrato su enormi quantità di testo a fare una cosa: prevedere come continua un testo. Il testo è diviso in pezzi, detti token: una parola breve, una parte di una parola lunga, un segno di punteggiatura.

Quando invii un prompt, il modello legge tutto ciò che ha davanti: le istruzioni che il fornitore dà allo strumento, il tuo testo, i documenti allegati, la conversazione fin lì. Calcola quanto è probabile ciascun token successivo, ne sceglie uno, lo aggiunge e ricomincia. Una determina di due pagine nasce così, token dopo token, in un migliaio di passaggi o più.

Prendi il preambolo di una determina di Borgo Esempio. Dopo "visto il D.Lgs. 18 agosto 2000, n." la continuazione più probabile è "267", il testo unico delle leggi sull'ordinamento degli enti locali (TUEL). Il modello non ha consultato Normattiva: ha completato una sequenza che ha letto migliaia di volte. Qui probabile e vero coincidono.

Ora la riga successiva: "visto il regolamento comunale per la concessione di contributi, approvato con deliberazione del Consiglio comunale n.". Il modello non ha mai letto il regolamento di Borgo Esempio. Sa però come è fatta una citazione di questo tipo, e la completa con un numero e una data plausibili. La forma è perfetta. Il contenuto è inventato.

Da qui discende tutto il capitolo: il modello conosce la forma delle citazioni, non l'elenco delle norme che esistono.

Mentre scrive, il modello può anticipare ciò che verrà dopo, come la rima di un verso.[^4] Ma in nessun passaggio confronta l'atto con una banca dati di norme. Se lo strumento cerca sul web o nei tuoi documenti, i testi trovati si aggiungono a ciò che il modello ha davanti: il modo di scrivere resta lo stesso.

### Dal completamento di testi all'assistente

Il modello di base completa testi; non è fatto per rispondere a domande. Per farne un assistente, i produttori lo addestrano ancora: con esempi di richieste e risposte, e con i giudizi di valutatori umani che confrontano più risposte alla stessa richiesta e indicano le migliori.[^5] Da qui vengono la cortesia e la disponibilità del chatbot, e due effetti che chi scrive atti deve conoscere.

Il primo: il modello tende a rispondere comunque. Secondo uno studio del 2025 firmato in prevalenza da ricercatori di OpenAI, l'addestramento e le prove con cui si confrontano i modelli premiano chi tenta una risposta più di chi ammette di non sapere, come uno studente che, a un esame senza penalità per gli errori, tira a indovinare. E i fatti che compaiono di rado nei testi di addestramento sono quelli su cui l'errore è più probabile.[^6] Il regolamento di un Comune di 6.500 abitanti, o il comma di un decreto modificato due volte, sono fatti rari.

Il secondo: il modello tende ad assecondarti. Gli assistenti addestrati con il giudizio umano tendono a dare ragione all'utente, anche quando sbaglia. Una delle cause probabili: in una parte dei casi anche i valutatori preferiscono la risposta che conferma ciò che pensano.[^7] Se il prompt contiene una premessa falsa, il modello spesso la segue.

### Il tono non misura nulla

Gli atti sono scritti in forma assertiva, e il modello riproduce quel registro anche quando la continuazione è un'ipotesi. Il tono sicuro non dice quanto è probabile che il contenuto sia vero; e il modello stesso, spesso, non sa quando sta sbagliando (si veda più avanti la sezione sulle allucinazioni).

In più, il modello non sceglie sempre il token più probabile: ne estrae uno secondo le probabilità, con un margine di casualità che il fornitore regola. Per questo la stessa richiesta, ripetuta, dà testi diversi, come ha mostrato l'esperimento descritto nel capitolo sul metodo del prompt. Una prova riuscita non garantisce la successiva.

Ne derivano tre regole pratiche:

- la forma corretta di una citazione non prova che la norma esista;
- una risposta giusta oggi non garantisce la stessa risposta domani;
- il modello va autorizzato a non sapere e invitato a contestare le tue premesse.

La terza regola si traduce in poche righe, da mettere in testa alla richiesta.

```
Prima di scrivere, controlla le premesse della mia richiesta.
Se una norma, un termine, un importo o un fatto che indico ti sembra
errato, abrogato o incoerente, non correggerlo da solo: segnalalo
con [VERIFICARE: motivo del dubbio] e prosegui.
Se non conosci un dato, scrivi [VERIFICARE: cosa] e non supporlo.
Richiesta: [richiesta, senza dati personali]
```

Se chiedi un paragrafo sull'informativa "ai sensi dell'art. 13 del D.Lgs. 196/2003", senza queste righe il modello può scriverlo così come lo chiedi, anche se quell'articolo del Codice privacy è stato abrogato nel 2018.[^8] Con queste righe è più probabile che lo segnali. Non è certo: il controllo resta tuo.

## Contesto, memoria e data di addestramento: perché l'IA cita ancora il D.Lgs. 50/2016

### Due fonti diverse

Ciò che il modello "sa" viene da due fonti, con un'affidabilità molto diversa.

| Aspetto | Addestramento | Contesto |
|---|---|---|
| Che cos'è | testi letti fino a una data | prompt, file, ricerche, chat |
| Si aggiorna | no | sì, lo aggiorni tu |
| Si controlla | no | sì: hai il testo |
| Negli atti serve per | forma e struttura | fatti, dati e norme |

L'addestramento lascia nel modello una conoscenza diffusa, non un archivio: nessun indice dice dove si trova l'art. 50 del Codice dei contratti pubblici, né in quale versione. Il contesto è il testo che il modello ha davanti adesso: lo usa in modo molto più affidabile di ciò che ricorda. Per questo il metodo del prompt vi mette fatti, dati ed elenco delle norme verificate.

### La data di addestramento e il peso del passato

I testi dell'addestramento si fermano a una data, che il fornitore indica nella documentazione del modello. Di ciò che è accaduto dopo, il modello non sa nulla, a meno che lo strumento non cerchi sul web o tu non gli fornisca i testi. Non chiedere la data al modello: spesso non la conosce con precisione.

Conta anche quanto si è scritto su ciascun argomento. Il D.Lgs. 18 aprile 2016, n. 50 è stato il Codice dei contratti pubblici per sette anni: modelli di determina, commenti, circolari, atti pubblicati negli albi online. È abrogato dal 1° luglio 2023, data da cui è efficace il D.Lgs. 31 marzo 2023, n. 36.[^9] È probabile che anche un modello addestrato dopo il 2023 abbia letto più pagine sul codice vecchio che su quello nuovo. Per il modello, il probabile è spesso il passato.

I modelli recenti, di regola, conoscono il nuovo Codice: nell'esperimento del capitolo sul metodo del prompt, il testo generico era aggiornato perfino al correttivo del 2024. Il passato riemerge nei dettagli, dove si vede meno. In quell'esperimento, in due bozze, una prassi nata con il vecchio Codice era attribuita a un articolo del nuovo, e in un'altra bozza compariva una norma del 2005 che modificava una disposizione abrogata nel 2006. Altre tracce tipiche:

- "responsabile unico del procedimento" invece di "responsabile unico del progetto" (art. 15 del D.Lgs. 36/2023);[^10]
- l'affidamento diretto "sotto i 40.000 euro" dell'abrogato art. 36, comma 2, lett. a), del D.Lgs. 50/2016, al posto dei limiti dell'art. 50 del D.Lgs. 36/2023;
- l'informativa "ai sensi dell'art. 13 del D.Lgs. 196/2003";
- le soglie europee, aggiornate ogni due anni, nella versione del biennio precedente.

Lo stesso accade con le norme cambiate dopo la data di addestramento. Un modello i cui testi si fermano all'inizio del 2026 può descrivere l'art. 4 dell'AI Act nel testo originario, scambiare la proposta di modifica per il testo approvato o collocare al 2 agosto 2026 gli obblighi per i sistemi ad alto rischio dell'Allegato III, che il Regolamento (UE) 2026/1744 ha rinviato al 2 dicembre 2027.[^11] Il capitolo sulla verifica delle norme raccoglie i riferimenti superati più frequenti.

Infine, il modello non sa che giorno è, se lo strumento non glielo dice. Per una scadenza o per la vigenza di una norma, scrivi la data nel prompt.

### La finestra di contesto

Anche il contesto ha un limite, la finestra di contesto, misurata in token: da qualche decina di pagine a molte centinaia, secondo il prodotto e il piano. Quando i documenti superano il limite, alcuni strumenti passano al modello solo i brani che ritengono pertinenti: il modello non legge tutto, e tu non lo vedi. E anche quando il testo entra per intero, contenerlo non significa usarlo bene. In uno studio pubblicato nel 2024 i modelli trovavano meglio un'informazione all'inizio o alla fine di un documento lungo che a metà.[^12] I modelli sono cambiati, ma la cautela resta: in un bando di quaranta pagine, il requisito a pagina venti è quello che rischia di sparire dalla sintesi. Chiedi al modello di riportare tra virgolette il passo da cui ricava ogni requisito. Nelle conversazioni lunghe, poi, le istruzioni iniziali perdono peso: per questo il capitolo sul metodo del prompt consiglia una chat nuova per ogni atto.

### La memoria non è apprendimento

Il modello non impara dalla tua conversazione: finita la chat, è identico a prima. Alcuni strumenti offrono una memoria, cioè salvano appunti sulle conversazioni passate e li rimettono nel contesto di quelle nuove. Non è conoscenza verificata: è testo aggiunto al prompt, scelto dal sistema, che può portare in una bozza il dato di un'altra pratica, anche un dato personale. Per questo il capitolo sul metodo del prompt consiglia di disattivarla, salvo diversa indicazione dell'ente. Diverso ancora è l'addestramento sulle conversazioni, con cui il fornitore, se l'account lo consente, migliora i modelli futuri. Il capitolo su quale IA usare in ufficio indica quali account e impostazioni usare.

### Ricerca sul web e documenti caricati

Quando lo strumento cerca sul web o nei documenti caricati, i testi trovati entrano nel contesto e il modello risponde su quella base. È la tecnica detta generazione aumentata dal recupero (in inglese, RAG). Riduce le invenzioni, non le elimina: il modello può attribuire a una fonte ciò che non dice, preferire una pagina vecchia o secondaria, mescolare il testo trovato con ciò che ricorda. Anche gli strumenti professionali di ricerca giuridica, costruiti così su banche dati curate, sbagliano ancora in misura non trascurabile, come si vede nella sezione seguente.

Per sapere da dove viene ogni affermazione, chiedilo in modo da poter controllare.

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

Controlla per prime le frasi marcate "conoscenza generale". Poi le altre: anche il rinvio a un articolo del testo può essere sbagliato.

## Le allucinazioni misurate: gli studi su domande giuridiche

### Perché il modello inventa

Si chiama allucinazione un contenuto falso o infondato che il modello presenta come vero. Il termine è discusso, perché il modello non percepisce nulla, ma è entrato nell'uso, anche dei giudici.

Le spiegazioni viste finora sono statistiche: l'errore è più probabile sui fatti rari, e l'addestramento premia il tentativo più dell'astensione. Una ricerca di Anthropic sul funzionamento interno di un suo modello ha individuato anche un possibile meccanismo. Per impostazione, il modello tende a dire che non sa. Quando riconosce un nome familiare, questa prudenza si spegne e il modello risponde. Se il nome è familiare ma i fatti mancano, la prudenza si spegne lo stesso: il modello si comporta come se sapesse, e inventa.[^13]

Nel diritto i nomi familiari sono ovunque: "D.Lgs. 36/2023", "art. 52", "Consiglio di Stato, sez. V". Il loro contenuto preciso, comma per comma, è molto meno noto al modello.

### Le domande sulle sentenze: lo studio di Dahl e altri

Nel primo studio sistematico sulle allucinazioni giuridiche, pubblicato nel 2024, un gruppo di ricercatori statunitensi ha posto ai modelli generalisti un gran numero di domande verificabili su sentenze dei tribunali federali scelte a caso: se la causa esiste, quale corte l'ha decisa, quale giudice ha scritto la motivazione, quale principio afferma. Le risposte sbagliate andavano dal 58% all'88%, secondo il modello.[^14]

Tre risultati riguardano direttamente chi scrive atti.

- Più la domanda è sostanziale, più l'errore è frequente. Nella versione preliminare dello studio, sulle domande relative al principio affermato dalla sentenza le risposte errate erano almeno il 75%.[^15] Sapere che una sentenza esiste è più facile che sapere cosa dice.
- Gli errori aumentano scendendo nella gerarchia dei giudici: sono meno frequenti sulle sentenze della Corte suprema, più frequenti su quelle dei tribunali di primo grado, di cui si scrive meno.
- I modelli spesso non correggono una premessa giuridica falsa contenuta nella domanda, e non sanno prevedere quando sbagliano.

### Gli strumenti professionali: lo studio di Magesh e altri

Il secondo studio ha messo alla prova gli strumenti di ricerca giuridica con IA di due grandi editori del mercato statunitense, LexisNexis e Thomson Reuters. Usano la generazione aumentata dal recupero su banche dati curate, e i produttori ne sottolineavano l'affidabilità proprio sulle allucinazioni. Hanno sbagliato tra il 17% e il 33% delle risposte, secondo lo strumento.[^16] Lo studio conta come errore anche la risposta che rinvia a una fonte vera che non dice ciò che le si attribuisce: è l'errore più difficile da scoprire, perché il rinvio c'è.

Una banca dati riduce gli errori, non li elimina. Lo riconoscono anche i produttori dei modelli. Anthropic, per esempio, indica che le tecniche che consiglia, come autorizzare il modello a dire "non lo so" o chiedere citazioni letterali dei documenti, riducono le allucinazioni ma non le azzerano.[^17]

### Che cosa valgono questi numeri per un Comune

Gli studi riguardano il diritto federale statunitense, in inglese, e modelli del 2023 e del 2024. I modelli sono cambiati da allora: le percentuali non vanno trasferite agli strumenti di oggi, né in meglio né in peggio. Nelle ricerche per questo libro non sono emersi studi equivalenti sul diritto amministrativo italiano.

Il meccanismo, però, è lo stesso, e indica dove essere più prudenti: sulle fonti di cui si scrive meno. Leggi regionali, regolamenti comunali, delibere, sentenze dei TAR, circolari sono, per un modello, fatti rari.

Gli errori normativi hanno forme ricorrenti.

| Tipo di errore | Esempio | Controllo |
|---|---|---|
| Norma inesistente | un decreto mai emanato | esistenza |
| Contenuto attribuito | un comma che dice altro | contenuto |
| Norma abrogata | art. 36 del D.Lgs. 50/2016 | vigenza |
| Estremi spostati | comma o lettera vicini | contenuto |
| Precedente snaturato | sentenza vera, principio falso | contenuto |
| Atto locale inventato | la delibera di un regolamento | archivio dell'ente |
| Premessa accolta | una norma abrogata citata da te | vigenza |

Esistenza, contenuto e vigenza sono i tre controlli descritti nel capitolo sulla verifica delle norme. Per gli atti dell'ente, che nessuna banca dati pubblica raccoglie per intero, la fonte è l'archivio dell'ente.

## Le citazioni inventate davanti ai giudici: la giurisprudenza italiana 2025-2026

In Italia il problema è arrivato nelle aule nel 2025. In poco più di un anno i giudici sono passati dal richiamo alla sanzione.[^18]

| Data | Giudice | Nell'atto | Esito |
|---|---|---|---|
| marzo 2025 | Trib. Firenze | sentenze inventate | nessuna condanna |
| settembre 2025 | Trib. Torino | citazioni inconferenti | art. 96 c.p.c. |
| settembre 2025 | Trib. Latina | atti non pertinenti | art. 96 c.p.c. |
| ottobre 2025 | TAR Milano | precedenti inesistenti | sentenza all'Ordine |
| febbraio 2026 | Trib. Siracusa | passi inventati | oltre 30.000 euro |
| febbraio 2026 | Cass. pen., sez. VII | precedenti mal attribuiti | inammissibile |
| giugno 2026 | Cass. pen., sez. III | principi mai affermati | 5.000 euro |

Nel primo caso, a Firenze, il Tribunale ha riconosciuto il disvalore dell'omessa verifica, ma ha escluso la responsabilità aggravata: mancavano le prove della mala fede e del danno. Da settembre 2025 le condanne si susseguono. A Siracusa l'attrice aveva riportato tra virgolette quattro precedenti di legittimità: alcuni non esistevano, altri riguardavano altre materie, e i passi citati non comparivano in nessuna sentenza. Il Tribunale ha qualificato come colpa grave la produzione di precedenti presumibilmente generati con l'IA e non verificati sulle fonti primarie.[^19]

Nel 2026 è intervenuta la Cassazione penale. Nel primo caso i precedenti esistevano, ma erano attribuiti a sezioni diverse da quelle indicate e non affermavano i principi invocati; la Corte ha parlato di una probabile "allucinazione informatica" e ne ha tenuto conto, come indice di negligenza, nel fissare la somma dovuta alla Cassa delle ammende.[^20] Nel secondo ha precisato che citare precedenti mai pronunciati non attenua la responsabilità, ma la aggrava: il ricorso, secondo le sintesi della pronuncia, è stato proposto "in violazione del dovere di controllo e con un grado di negligenza che supera la soglia dell'errore scusabile".[^21]

### Tre lezioni per chi scrive atti

La prima: in nessuno di questi casi il giudice ha sanzionato l'uso dell'IA in sé. Ha sanzionato l'omessa verifica.

La seconda: nei casi più recenti l'errore non è solo la sentenza inventata, ma anche quella vera che non dice ciò che le si attribuisce. Un controllo limitato all'esistenza non basta: il testo va letto.

La terza: le pronunce riguardano atti di parte, scritti da avvocati, ma il principio vale per chi firma un atto. Per la pubblica amministrazione lo dice la L. 132/2025: la persona "resta l'unica responsabile dei provvedimenti e dei procedimenti in cui sia stata utilizzata l'intelligenza artificiale" (art. 14, comma 2).

### Le prime sentenze sugli atti amministrativi

Nel 2026 sono arrivate anche le prime sentenze su atti dell'amministrazione. Il TAR Marche ha esaminato la relazione istruttoria di un responsabile unico del progetto con richiami giurisprudenziali inesatti, scritta con l'IA secondo il ricorrente. Ha escluso che l'uso dell'IA come supporto alla redazione o alla ricerca di precedenti violi di per sé la "riserva di umanità" del Codice dei contratti pubblici, se la valutazione e la decisione finale restano controllate, motivate e imputabili a chi esercita il potere.[^22]

Secondo i primi commenti, nello stesso senso si è espresso il TAR Puglia sull'uso dell'IA generativa nella redazione di un annullamento in autotutela di permessi di costruire. Conta che la decisione resti il frutto di un percorso logico e giuridico autonomo, riconoscibile e imputabile a chi esercita il potere. Sempre secondo i commenti, nemmeno i riferimenti giurisprudenziali inesistenti o non pertinenti invalidano per forza l'atto, quando il nucleo della motivazione resta autonomo, comprensibile e verificabile.[^23]

Non è un via libera. L'atto scritto con l'IA regge se la motivazione regge da sola. Se invece la decisione poggia su una norma inventata o abrogata, o su un precedente che non esiste, l'atto è esposto all'annullamento per violazione di legge o per eccesso di potere (art. 21-octies, comma 1, della L. 7 agosto 1990, n. 241).[^24] I profili di responsabilità di chi firma sono descritti nel capitolo sulla legge italiana sull'IA.

Per un responsabile di servizio di Borgo Esempio la conclusione è pratica: una citazione non verificata non rafforza la motivazione. Se la decisione non ne ha bisogno, va tolta. Se ne ha bisogno, va verificata.

## L'eccesso di fiducia: quando chi rivede smette di controllare

Gli errori del modello si possono trovare. Il rischio maggiore è che chi rivede smetta di cercarli.

### Il pregiudizio dell'automazione

Gli studi su aviazione e medicina lo chiamano pregiudizio dell'automazione (in inglese, automation bias): la tendenza a usare il suggerimento di un sistema automatico al posto della propria ricerca e valutazione delle informazioni. Produce due tipi di errori. Di omissione: non vedi un problema che il sistema non ti ha segnalato. Di commissione: segui un'indicazione sbagliata del sistema. Secondo una rassegna degli studi, si osserva sia nei principianti sia negli esperti, non si elimina con la sola formazione o con le istruzioni, e cresce quando l'attenzione è divisa tra più compiti. E più il sistema è affidabile, meno lo si controlla.[^25]

Con l'IA generativa il fenomeno ha un'aggravante: il testo è scritto bene. Una bozza ordinata, nel lessico giusto, corretta quasi sempre, abitua a leggere in fretta anche la volta in cui non lo è. E gli errori stanno dove l'occhio passa veloce: il contenuto di un comma citato, un controllo dato per fatto, un importo. Il capitolo sull'IA già in ufficio riporta gli esperimenti in cui, quando il modello sbagliava, chi lo usava sbagliava più di chi lavorava senza, e l'indagine che associa più fiducia nell'IA a meno pensiero critico.[^26] Il lavoro non sparisce: si sposta dalla scrittura alla verifica.

### La catena dei controlli in un piccolo Comune

A Borgo Esempio un atto passa per più mani. L'istruttore prepara la bozza. Il responsabile del servizio la firma e rilascia il parere di regolarità tecnica. Se c'è una spesa, il responsabile del servizio finanziario appone il visto di regolarità contabile. Sotto la direzione del segretario comunale, gli atti estratti a campione sono sottoposti al controllo successivo di regolarità amministrativa (art. 147-bis del TUEL). Ogni passaggio è un controllo. Ma se l'istruttore pensa "tanto lo rilegge il responsabile" e il responsabile pensa "l'ha preparato l'istruttore, che conosce la pratica", nessuno controlla davvero.

Servono misure semplici, più che buone intenzioni.

- Dichiara l'uso: chi firma deve sapere che la bozza viene dall'IA, e da quale prompt, per sapere dove guardare (si veda il capitolo sulla tracciabilità).
- Chiudi per iscritto ogni [VERIFICARE]: per ciascuno, l'esito e la fonte consultata.
- Controlla per regola, non per sensazione: ogni norma con i tre controlli, ogni fatto con il fascicolo, ogni numero ricalcolato.
- Annota gli errori che trovi, nel registro delle correzioni descritto nel capitolo sul metodo del prompt. Se per settimane non ne trovi nessuno, prima di fidarti di più dello strumento chiediti se stai ancora controllando.
- Rivedi con attenzione piena: non tra una telefonata e l'altra, non a dieci minuti dalla scadenza.
- Considerati responsabile del modo in cui usi lo strumento, non solo dell'atto. Negli esperimenti di volo simulato, chi doveva rendere conto del proprio operato, o si sentiva responsabile del modo in cui usava il sistema automatico, ne verificava di più le indicazioni e sbagliava meno.[^27] Per il funzionario, quella responsabilità è già scritta nella legge.

Il modello può fare anche da secondo lettore, con lo strumento autorizzato e senza dati personali.

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

Questa rilettura è un'altra previsione di testo: trova alcuni problemi, ne trascura altri e a volte ne inventa. Serve a orientare il tuo controllo, non a sostituirlo.

## Cosa l'IA fa bene in un ufficio comunale, e cosa no

### Il criterio

L'IA lavora bene quando il materiale è nel contesto e il compito riguarda la forma: riassumere, ordinare, riscrivere, proporre una struttura. Lavora male quando deve fornire ciò che non ha: fatti della pratica, numeri, norme precise e vigenti, giudizi sul caso.

| Compito | Esito | Perché |
|---|---|---|
| Sintesi di un documento fornito | buono; controlla le omissioni | il testo è nel contesto |
| Riscrittura in linguaggio chiaro | buono, con revisione | è un lavoro sulla forma |
| Struttura di un atto raro | buono | ha letto molti atti simili |
| Norme e sentenze a memoria | scarso | prevede la forma della citazione |
| Calcoli, termini, conteggi | inaffidabile | lavora su token, non su numeri |
| Fatti della pratica | impossibile | non li ha, se non glieli dai |
| Decisione sul caso | non ammessa | decide la persona |

Sulla riscrittura in linguaggio chiaro, uno studio del 2025 su testi amministrativi italiani conferma: il risultato dipende molto dal prompt, e serve la revisione umana.[^28] Le regole da dare al modello sono nel capitolo sulla lingua degli atti.

Sui numeri serve una cautela in più. Per il modello un importo IVA compresa o un termine di trenta giorni sono sequenze di testo da prevedere, non operazioni. Alcuni strumenti eseguono un programma per i calcoli; anche allora controlla dati di partenza e risultato. Lo stesso vale per i conteggi: nell'esperimento del capitolo sul metodo del prompt, il modello ha superato del 29-39% la lunghezza richiesta. Se l'atto contiene importi o scadenze, aggiungi al prompt queste righe.

```
Non fare calcoli e non calcolare scadenze.
Dove l'atto richiede un importo o un termine, scrivi
[VERIFICARE: calcolo da fare].
Dopo l'atto, per ciascuno elenca i dati di partenza e l'operazione.
Se indichi la norma che fissa un termine, aggiungi [VERIFICARE: norma].
```

Sulla decisione, infine, non c'è margine. L'IA si usa "in funzione strumentale e di supporto all'attività provvedimentale" (art. 14, comma 2, L. 132/2025). Per le decisioni che producono effetti giuridici su una persona, o che incidono in modo analogo significativamente su di essa, vale anche l'art. 22 del Regolamento (UE) 2016/679 (GDPR): salvo eccezioni, l'interessato ha diritto di non essere sottoposto a una decisione basata unicamente su un trattamento automatizzato. Ne parla il capitolo sul GDPR e i dati nel prompt.

### Un caso a Borgo Esempio: il contributo all'ASD

Il Servizio Affari generali istruisce la domanda di contributo annuale dell'ASD Borgo Esempio, da concedere secondo i criteri fissati dal regolamento comunale, come chiede l'art. 12 della L. 241/1990.[^29] L'istruttrice scompone il lavoro.

- Sintesi della relazione sulle attività allegata alla domanda: all'IA, solo con lo strumento autorizzato dall'ente e coperto da un contratto con il fornitore ai sensi dell'art. 28 del GDPR. Prima togli i nomi di dirigenti, allenatori e atleti: per la sintesi non servono. I dati dei minori e quelli sulla salute, come una disabilità, non entrano nel prompt.
- Confronto tra relazione e criteri del regolamento: all'IA, con il testo del regolamento e il prompt che segue.
- Punteggio e importo: al foglio di calcolo.
- Estremi del regolamento e della delibera che lo approva: dall'archivio dell'ente, non dal modello.
- Ammissione e importo: all'istruttrice, che propone, e al responsabile del servizio, che decide e firma.
- Motivazione in linguaggio chiaro: all'IA, partendo dagli esiti dell'istruttoria, poi riletta riga per riga.

Togliere i nomi non basta a rendere anonimo il testo. In un paese di 6.500 abitanti l'unica allenatrice della squadra femminile si riconosce anche senza nome. Togli anche i dettagli che permettono di riconoscere qualcuno, e tratta comunque il testo come dato personale: pseudonimizzare non è anonimizzare, e il testo resta nello strumento autorizzato.

Per il confronto con i criteri basta un prompt breve.

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

La tabella che ne esce è un appunto istruttorio, non una valutazione. Controlla ogni passo tra virgolette sulla relazione originale: il modello può citare male anche un testo che ha davanti.

L'IA ha lavorato su gran parte del testo e non ha deciso nulla. È la divisione del lavoro che la legge chiede. Il capitolo sull'istruttoria con l'IA e quello sulle determine riprendono questo modo di dividere il lavoro.

## In sintesi

- Un modello linguistico prevede come continua un testo, un token alla volta. Conosce la forma delle citazioni, non l'elenco delle norme che esistono.
- L'addestramento lo spinge a rispondere comunque e ad assecondarti: autorizzalo a non sapere e chiedigli di contestare le tue premesse.
- Ciò che ha imparato si ferma a una data e pesa il passato: per questo riaffiora il D.Lgs. 50/2016. Ciò che gli dai nel contesto puoi aggiornarlo e controllarlo: fatti, dati e norme vanno lì. Memoria e ricerca sul web aggiungono testo, non certezze.
- Gli studi misurano errori frequenti sulle domande giuridiche, anche negli strumenti professionali: più la domanda è sostanziale e la fonte rara, più l'errore è probabile.
- I giudici sanzionano l'omessa verifica, non l'uso dell'IA. Per le prime sentenze sugli atti amministrativi, l'uso dell'IA non basta a renderli illegittimi se la motivazione regge da sola e la decisione resta umana.
- Il rischio maggiore è smettere di controllare: dichiara l'uso, chiudi per iscritto i [VERIFICARE], controlla per regola.
- Nel contesto metti solo ciò che serve. Con dati personali usa solo lo strumento autorizzato dall'ente; dati dei minori, sanitari e giudiziari mai. Togliere i nomi non rende anonimo un testo.
- Affida all'IA la forma del materiale che le dai; tieni per te fatti, numeri, norme e decisione.

[^1]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, art. 3, n. 56, e art. 4, eur-lex.europa.eu. L'art. 4 è stato sostituito dal Regolamento (UE) 2026/1744 del Parlamento europeo e del Consiglio, dell'8 luglio 2026 (omnibus digitale sull'IA), pubblicato nella Gazzetta ufficiale dell'Unione europea, serie L, del 24 luglio 2026 e in vigore dal 27 luglio 2026. Il nuovo testo e la sua portata sono descritti nel capitolo sull'AI Act.

[^2]: Commissione europea, *AI Literacy – Questions & Answers*, 2025, digital-strategy.ec.europa.eu. Le risposte, pubblicate nel maggio 2025, precedono la modifica dell'art. 4, che ha trasformato l'obbligo in un obbligo di mezzi; restano un riferimento utile sui contenuti.

[^3]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 3, in Gazzetta Ufficiale n. 223 del 25 settembre 2025, normattiva.it. La legge è in vigore dal 10 ottobre 2025.

[^4]: Anthropic, *Tracing the thoughts of a large language model*, 2025, anthropic.com; J. Lindsey e altri, *On the Biology of a Large Language Model*, 2025, transformer-circuits.pub. Le ricerche riguardano un modello di Anthropic, e gli autori avvertono che i loro metodi colgono solo una parte dei calcoli interni.

[^5]: L. Ouyang e altri, *Training language models to follow instructions with human feedback*, in Advances in Neural Information Processing Systems, vol. 35, 2022, arxiv.org. Nello studio i valutatori ordinavano più risposte alla stessa richiesta dalla migliore alla peggiore. La tecnica è nota come apprendimento per rinforzo dal feedback umano (in inglese, RLHF).

[^6]: A. T. Kalai, O. Nachum, S. S. Vempala, E. Zhang, *Why Language Models Hallucinate*, 2025, arxiv.org. Gli autori lavorano per OpenAI e per il Georgia Institute of Technology; il paragone con lo studente che tira a indovinare è loro.

[^7]: M. Sharma e altri, *Towards Understanding Sycophancy in Language Models*, in Proceedings of the International Conference on Learning Representations (ICLR 2024), 2024, arxiv.org. Lo studio ha osservato la tendenza in cinque assistenti di IA diffusi, e ha rilevato che persone e modelli di valutazione preferiscono, in una parte non trascurabile dei casi, risposte accondiscendenti ben scritte a risposte corrette.

[^8]: D.Lgs. 10 agosto 2018, n. 101, art. 27, che ha abrogato tra l'altro l'art. 13 del D.Lgs. 30 giugno 2003, n. 196, *Codice in materia di protezione dei dati personali*, in Gazzetta Ufficiale n. 205 del 4 settembre 2018, normattiva.it. Oggi l'informativa si fonda sugli artt. 13 e 14 del Regolamento (UE) 2016/679.

[^9]: D.Lgs. 31 marzo 2023, n. 36, *Codice dei contratti pubblici*, art. 226, comma 1, sull'abrogazione del D.Lgs. 18 aprile 2016, n. 50 dal 1° luglio 2023, e art. 229, sull'efficacia del nuovo Codice dalla stessa data, normattiva.it. Gli artt. 225 e 226 dettano il regime transitorio per le procedure già avviate.

[^10]: D.Lgs. 31 marzo 2023, n. 36, cit., art. 15; "responsabile unico del procedimento" era la formula dell'art. 31 del D.Lgs. 50/2016. L'art. 50, comma 1, lett. a) e b), del D.Lgs. 36/2023 ammette l'affidamento diretto per lavori sotto i 150.000 euro e per servizi e forniture sotto i 140.000 euro. Le soglie europee in vigore dal 1° gennaio 2026 sono di 5.404.000 euro per i lavori e, per i Comuni, di 216.000 euro per servizi e forniture: ANCE, *Appalti pubblici: dal 1° gennaio 2026 si applicheranno le nuove soglie comunitarie*, 2025, ance.it.

[^11]: Regolamento (UE) 2024/1689, cit., art. 113, come modificato dal Regolamento (UE) 2026/1744, cit. Per i sistemi ad alto rischio dell'Allegato I il termine passa dal 2 agosto 2027 al 2 agosto 2028.

[^12]: N. F. Liu e altri, *Lost in the Middle: How Language Models Use Long Contexts*, in Transactions of the Association for Computational Linguistics, vol. 12, 2024, pp. 157-173, aclanthology.org. Lo studio riguarda modelli disponibili nel 2023.

[^13]: Anthropic, *Tracing the thoughts of a large language model*, cit.; J. Lindsey e altri, *On the Biology of a Large Language Model*, cit., parte sulle allucinazioni e sul riconoscimento delle entità note. In un esperimento, attivando artificialmente il segnale di "nome noto", i ricercatori hanno indotto il modello a inventare dettagli su una persona inesistente.

[^14]: M. Dahl, V. Magesh, M. Suzgun, D. E. Ho, *Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models*, in Journal of Legal Analysis, vol. 16, n. 1, 2024, pp. 64-93, academic.oup.com. I valori si riferiscono alla versione pubblicata e ai modelli generalisti disponibili nel 2023. Lo studio descrive anche la tendenza ad accettare le premesse giuridiche errate dell'utente e la scarsa capacità dei modelli di prevedere i propri errori.

[^15]: Stanford Law School, *Hallucinating Law: Legal Mistakes with Large Language Models are Pervasive*, 2024, law.stanford.edu, che sintetizza la versione preliminare dello studio, anche sulla differenza tra Corte suprema e tribunali di primo grado.

[^16]: V. Magesh, F. Surani, M. Dahl, M. Suzgun, C. D. Manning, D. E. Ho, *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, in Journal of Empirical Legal Studies, vol. 22, 2025, pp. 216-242, law.stanford.edu. Gli strumenti esaminati sono Lexis+ AI di LexisNexis e, di Thomson Reuters, Westlaw AI-Assisted Research e Ask Practical Law AI.

[^17]: Anthropic, *Reduce hallucinations*, 2026, platform.claude.com, secondo cui queste tecniche riducono le allucinazioni in modo significativo ma non le eliminano del tutto, e le informazioni critiche vanno sempre verificate.

[^18]: Trib. Firenze, sez. spec. imprese, ordinanza 14 marzo 2025; Trib. Torino, sez. lavoro, sentenza 16 settembre 2025, con condanna a 500 euro per ciascuna controparte e a 500 euro alla Cassa delle ammende (art. 96, commi 3 e 4, c.p.c.); Trib. Latina, sentenza 23 settembre 2025, n. 1034; TAR Lombardia, Milano, sez. V, sentenza 21 ottobre 2025, n. 3348, giustizia-amministrativa.it, che ha trasmesso la sentenza al Consiglio dell'Ordine degli avvocati di Milano richiamando il dovere di lealtà e probità (art. 88 c.p.c.); Trib. Siracusa, sez. II civile, sentenza 20 febbraio 2026, n. 338; Cass. pen., sez. VII, ordinanza 27 febbraio 2026 (dep. 26 marzo 2026), n. 11431; Cass. pen., sez. III, sentenza 11 giugno 2026 (dep. 22 giugno 2026), n. 23006. Commenti in Diritto.it, *Intelligenza artificiale negli atti difensivi: il Tribunale di Firenze sulle allucinazioni AI*, 2025, e *Atto processuale redatto con intelligenza artificiale e responsabilità aggravata*, 2025, diritto.it.

[^19]: Trib. Siracusa, n. 338/2026, cit., che ha condannato la parte a 14.103 euro di spese di lite, a una somma di pari importo ex art. 96, comma 3, c.p.c. e a 2.000 euro in favore della Cassa delle ammende ex art. 96, comma 4. Il Sole 24 Ore NT+ Diritto, *Quattro sentenze fantasma e conto da 30.000 euro*, 2026, ntplusdiritto.ilsole24ore.com.

[^20]: Cass. pen., sez. VII, n. 11431/2026, cit., in materia di stupefacenti, con la somma dovuta alla Cassa delle ammende determinata ai sensi dell'art. 616 c.p.p. Sistema Penale, *Intelligenza artificiale: una prima pronuncia di inammissibilità di un ricorso per cassazione imputabile anche a richiami giurisprudenziali non pertinenti*, 2026, sistemapenale.it.

[^21]: Cass. pen., sez. III, n. 23006/2026, cit., in un incidente di esecuzione sulla revoca di un ordine di demolizione; la Corte ha determinato in via equitativa in 5.000 euro la somma dovuta alla Cassa delle ammende. Il passo è riportato da EC News, *Citazioni generate dall'AI e non controllate: la colpa è più grave e la sanzione sale*, 2026, ecnews.it.

[^22]: TAR Marche, sez. I, sentenza 1° giugno 2026, n. 758, giustizia-amministrativa.it, sulla "riserva di umanità" dell'art. 30 del D.Lgs. 36/2023: la relazione del RUP non era l'atto conclusivo e la scelta restava al dirigente competente. L'esclusione dell'operatore per grave illecito professionale (art. 98) è stata confermata. Commento in LavoriPubblici.it, *Intelligenza artificiale negli appalti pubblici: quando l'IA non rende illegittima la decisione amministrativa*, 2026, lavoripubblici.it.

[^23]: TAR Puglia, sez. III, sentenza 3 agosto 2026, n. 956, giustizia-amministrativa.it. Il contenuto è riferito sulla base del commento in Il Sole 24 Ore NT+ Diritto, *IA generativa, l'uso nei provvedimenti Pa non è illegittimo e resta responsabilità umana*, 2026, ntplusdiritto.ilsole24ore.com.

[^24]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 21-octies, normattiva.it. Il comma 2 esclude l'annullamento per la violazione di norme sul procedimento o sulla forma quando, per la natura vincolata del provvedimento, è palese che il contenuto non avrebbe potuto essere diverso.

[^25]: R. Parasuraman e D. H. Manzey, *Complacency and Bias in Human Use of Automation: An Attentional Integration*, in Human Factors, vol. 52, n. 3, 2010, pp. 381-410, journals.sagepub.com. La distinzione tra errori di omissione e di commissione è in L. J. Skitka, K. L. Mosier, M. Burdick, *Does automation bias decision-making?*, in International Journal of Human-Computer Studies, vol. 51, n. 5, 1999, pp. 991-1006, sciencedirect.com.

[^26]: F. Dell'Acqua e altri, *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*, Harvard Business School Working Paper n. 24-013, 2023, ssrn.com; A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers Likely Provide Meaningful Boosts to Productivity*, Microsoft, MSR-TR-2023-43, 2023, microsoft.com; H.-P. Lee e altri, *The Impact of Generative AI on Critical Thinking*, in Proceedings of CHI 2025, ACM, 2025, microsoft.com, con dati autodichiarati che indicano un'associazione, non un rapporto di causa.

[^27]: L. J. Skitka, K. L. Mosier, M. Burdick, *Accountability and automation bias*, in International Journal of Human-Computer Studies, vol. 52, n. 4, 2000, pp. 701-717, sciencedirect.com; K. L. Mosier e altri, *Automation bias: decision making and performance in high-tech cockpits*, in International Journal of Aviation Psychology, vol. 8, n. 1, 1998, pp. 47-63, tandfonline.com.

[^28]: S. Ondelli e A. Santoro, *Come usare ChatGPT per semplificare i testi amministrativi? Alcuni confronti tra intelligenza umana e intelligenza artificiale*, in Italiano LinguaDue, vol. 17, n. 2, 2025, pp. 1327-1377, riviste.unimi.it.

[^29]: L. 7 agosto 1990, n. 241, cit., art. 12, che subordina la concessione di sovvenzioni, contributi, sussidi e ausili finanziari e l'attribuzione di vantaggi economici alla predeterminazione e alla pubblicazione dei criteri e delle modalità, normattiva.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 35 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Il testo diceva che Thomson Reuters è un editore statunitense.
- Nel caso dell'ASD la bozza diceva di togliere i nomi degli atleti 'soprattutto se minori'.
- Nella tabella degli errori normativi la colonna 'Lo scopri con' usava la voce 'lettura'.
- 'Nessun giudice ha sanzionato l'uso dell'IA in sé' generalizzava oltre i casi citati.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
