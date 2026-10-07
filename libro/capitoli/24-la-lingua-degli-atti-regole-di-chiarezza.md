# La lingua degli atti: regole di chiarezza da dare all'IA

In questo capitolo: le regole ufficiali della scrittura amministrativa, dalla struttura del provvedimento alla scelta delle parole, trasformate in istruzioni per l'IA e in controlli da fare sulla bozza.

## Il problema: l'IA scrive come gli atti che ha letto

Chiedi a un modello di IA una determina senza dargli regole di stile. Il testo che ricevi somiglia spesso alla media degli atti che circolano: "Premesso che", "Dato atto che", "si rende necessario procedere", "ai sensi della normativa vigente". Il modello ha imparato a scrivere da enormi quantità di testi, tra cui con ogni probabilità molti atti pubblicati on line. Senza istruzioni ne riproduce le formule più frequenti, non le migliori.

Il rischio opposto si presenta quando gli chiedi di semplificare. Il modello accorcia e cambia parole. A volte toglie una condizione, trasforma un obbligo in una facoltà o sostituisce un termine giuridico con un sinonimo che non vuol dire la stessa cosa.

La lingua di un atto non è un ornamento. La motivazione deve indicare "i presupposti di fatto e le ragioni giuridiche" della decisione, "in relazione alle risultanze dell'istruttoria" (art. 3 della L. 7 agosto 1990, n. 241).[^1] Una motivazione che il destinatario non riesce a capire non svolge la sua funzione. Se è oscura o solo apparente, espone l'atto a una censura per difetto di motivazione. Nel 1965 Italo Calvino chiamò "antilingua" l'italiano che fugge davanti alle parole concrete per sembrare ufficiale.[^2] Da allora le amministrazioni si sono date regole scritte per evitarla. Questo capitolo le traduce in istruzioni per l'IA e in controlli sulla bozza.

## Da dove vengono le regole

Le regole della scrittura amministrativa non sono preferenze di gusto. Hanno più di trent'anni di storia e una fonte per ciascuna.

Nel 1993 il Dipartimento della funzione pubblica, con il ministro Sabino Cassese, pubblica il *Codice di stile delle comunicazioni scritte ad uso delle amministrazioni pubbliche*: la prima raccolta organica di regole comuni. Nel 1997 segue il *Manuale di stile* curato da Alfredo Fioritto, con strumenti ed esempi per semplificare i testi.[^3]

Poi arrivano le direttive del Ministro per la funzione pubblica. Quella dell'8 maggio 2002, nota come direttiva Frattini, vale per tutti i testi delle amministrazioni. Chiede frasi brevi, parole del linguaggio comune, verbi in forma attiva e affermativa, il minor numero possibile di sigle; sconsiglia neologismi, parole straniere e latinismi. È la fonte della soglia indicativa delle 25 parole per frase, già usata nel file di stile del capitolo sul metodo del prompt.[^4] Quella del 24 ottobre 2005, nota come direttiva Baccini, fissa il principio di fondo: "Al rigore di chi scrive deve corrispondere la comprensione di chi legge".[^5] Una direttiva del 23 maggio 2007 sulle pari opportunità chiede di usare in tutti i documenti di lavoro "un linguaggio non discriminatorio".[^6]

Per gli atti, la fonte più completa è la *Guida alla redazione degli atti amministrativi. Regole e suggerimenti*. L'ha scritta un gruppo di lavoro dell'allora ITTIG-CNR (oggi IGSG-CNR) e dell'Accademia della Crusca, e la versione definitiva è stata presentata nel 2011. Tra i principi generali indica chiarezza, precisione, uniformità, semplicità ed economia. Si divide in tre parti: le regole linguistiche, la struttura del provvedimento, i riferimenti ad altri atti.[^7]

| Fonte | Anno | Cosa dà al prompt |
|---|---|---|
| Codice di stile | 1993 | le prime regole comuni |
| Manuale di stile | 1997 | esempi e strumenti |
| Direttiva Frattini | 2002 | frasi brevi, forma attiva, poche sigle |
| Direttiva Baccini | 2005 | scrivere per chi legge |
| Direttiva pari opportunità | 2007 | linguaggio non discriminatorio |
| Guida ITTIG-Crusca | 2011 | struttura, Visto e Considerato, lessico |

Per avvisi e pagine del sito valgono anche le indicazioni di Designers Italia: se ne parla nel capitolo sulle risposte ai cittadini.

Le direttive sono atti di indirizzo, la Guida un insieme di regole e suggerimenti. Nessuna di queste fonti rende illegittimo, da sola, un atto scritto male: il vizio, se c'è, viene dalla motivazione che non regge. Ma sono scritte, pubbliche e citabili. Una regola con una fonte si spiega a chi firma, si mette nel file di stile e si controlla.

### Dalle regole alle istruzioni

Una regola serve all'IA quando è scritta come un'istruzione da eseguire e ha un controllo che puoi fare dopo. "Scrivi in modo chiaro" non è un'istruzione: il modello deve indovinare che cosa intendi. "Di regola, frasi sotto le 25 parole" lo è, e si verifica. Anthropic, per esempio, consiglia di dire al modello che cosa fare, non solo che cosa evitare:[^8] "usa la forma attiva, con il soggetto espresso" funziona meglio di "non usare il passivo".

Il file di stile proposto nel capitolo sul metodo del prompt contiene già tredici regole. Questo capitolo ne spiega l'origine, aggiunge quelle sulla struttura e sul lessico e indica come controllarle.

## La struttura del provvedimento

La Guida divide il provvedimento in tre parti.[^9]

- La parte iniziale, cioè l'intestazione, identifica l'atto: ente e organo, tipo di atto, numero e data, oggetto.
- La parte centrale contiene preambolo, motivazione e dispositivo.
- La parte finale contiene luogo e data di adozione e firma.

### Intestazione e oggetto

Numero e data li assegna il sistema di gestione degli atti, mai il modello. L'oggetto puoi farlo scrivere all'IA, con tre vincoli. Dice che cosa l'atto decide, non quale procedura segue. Si capisce da solo, perché è ciò che si legge all'albo online, negli elenchi e nelle ricerche. E negli atti su una persona non contiene dati che la rendano riconoscibile: il capitolo sulla privacy prima della pubblicazione spiega perché.

Le coppie prima e dopo di questo capitolo sono costruite per il libro, su casi inventati del Comune di Borgo Esempio. La prima riguarda l'oggetto di una determina.

Prima:

> Determinazione a contrarre ai sensi dell'art. 17, comma 2, del D.Lgs. n. 36/2023 e dell'art. 192 del D.Lgs. n. 267/2000 e contestuale affidamento diretto ex art. 50, comma 1, lett. b), del D.Lgs. n. 36/2023 del servizio di abbonamento annuale a banca dati giuridica on line. Assunzione impegno di spesa.

Dopo:

> Abbonamento per il 2027 alla banca dati giuridica on line. Affidamento diretto a Editrice Esempio S.r.l. e impegno di spesa di euro 1.200,00 oltre IVA.

Le norme stanno nel preambolo. Se la prassi dell'ente vuole nell'oggetto anche il CIG o la norma principale, scrivilo nel file di stile.

### Preambolo, motivazione, dispositivo

Il *preambolo* elenca le norme e gli atti su cui la decisione si fonda: la norma che attribuisce la competenza, il decreto di nomina del responsabile, gli atti di programmazione e di bilancio, l'istanza o la proposta, i pareri, gli atti precedenti. Solo atti che esistono, con i loro estremi: ciascuno si può verificare.

La *motivazione* espone i presupposti di fatto e le ragioni giuridiche, in relazione alle risultanze dell'istruttoria. È la parte in cui l'IA rischia di più, perché sa scrivere ragioni plausibili che nessuno ha accertato. Il capitolo sul metodo del prompt mostra come vietarglielo.

Il *dispositivo* è introdotto da un verbo che cambia con l'organo e con il tipo di atto: determina, delibera, decreta, ordina, dispone. Si compone di uno o più paragrafi; secondo la Guida, la forma ad articoli numerati va usata solo in casi particolari.[^10] Ogni punto produce un effetto e dice chi fa che cosa, e quando se serve. Un punto che comincia con "di dare atto che" spesso non decide nulla: è un Considerato fuori posto.

Non eccedere nemmeno nel senso opposto. Nell'esperimento del capitolo sul metodo del prompt, la regola "un'azione per punto" ha prodotto da sedici a diciannove punti per un acquisto da 1.200 euro. Raggruppa per effetto: decisione, spesa, adempimenti successivi. Nel file di stile la regola 8 può diventare: "Dispositivo: punti numerati, uno per ogni effetto dell'atto, all'infinito («di impegnare»)."

La *parte finale* porta luogo, data e firma. Pareri e visti, come la regolarità tecnica e contabile, li rende chi ne ha la competenza, dopo il controllo: il modello non li scrive. Negli atti da notificare vanno indicati il termine e l'autorità cui è possibile ricorrere (art. 3, comma 4, L. 241/1990).

### Lo scheletro da dare all'IA

Uno scheletro fisso dice al modello dove va ogni cosa. Incollalo nel prompt al posto dell'elenco delle sezioni della riga Formato. Oppure salvalo tra i documenti del progetto e richiamalo in quella riga.

```
COMUNE DI BORGO ESEMPIO
Servizio [nome]
DETERMINAZIONE N. [dal sistema] DEL [dal sistema]
OGGETTO: [cosa si decide, per che cosa, quanto; al massimo tre righe]

IL RESPONSABILE DEL SERVIZIO

Visto [norma che attribuisce la competenza];
Visto [decreto del Sindaco di nomina: ATTO_1];
Vista [deliberazione di bilancio o di programmazione: ATTO_2];
Vista [istanza, proposta o altro atto presupposto: data e PROT_1];

Considerato che [fatto accertato, con il documento da cui risulta];
Considerato che [ragione giuridica che lega il fatto alla decisione];
Considerato che [valutazione degli interessi, se l'atto è discrezionale];

DETERMINA

1. di [decisione principale];
2. di [effetto sulla spesa o sull'entrata, se c'è];
3. di [adempimento successivo: chi lo compie ed entro quando];

[Termine e autorità cui ricorrere, se l'atto si notifica]

Borgo Esempio, [data]
Il Responsabile del Servizio
[firma digitale]
```

Le voci "dal sistema" restano vuote: le compila il gestionale. Se il tuo ente ha già un modello, usa quello. L'uniformità è uno dei principi della Guida, e un modello unico per tutto il Comune vale più di uno perfetto usato da una persona sola.

## Visto e Considerato

Nella prassi di molti Comuni il preambolo è una catena di formule: "Premesso che", "Dato atto che", "Preso atto che", "Rilevato che", "Richiamato", "Accertato che", "Ritenuto". Chi legge non distingue gli atti citati dai fatti, né i fatti dalle ragioni. La motivazione vera si disperde nelle premesse, e alla fine resta un "ritenuto di dover provvedere".

La Guida propone uno schema con due sole formule: ogni paragrafo del preambolo comincia con "Visto", ogni paragrafo della motivazione con "Considerato".[^11] Lo schema sostituisce "premesso che", "dato atto che" e simili, e assegna a ogni frase una funzione.

- *Visto* (concordato con il nome che segue: Vista, Visti, Viste) introduce una norma o un atto che esiste, con i suoi estremi. Si controlla sul testo.
- *Considerato* introduce un fatto accertato nell'istruttoria o una ragione. Si controlla sul fascicolo.

Per l'IA lo schema è un vantaggio, perché obbliga il modello a classificare. Un Visto senza estremi è una norma da cercare. Un Considerato senza un documento dietro è un fatto da accertare, oppure un'invenzione. Come si legge nel capitolo d'apertura, ogni Considerato che firmi deve avere dietro un documento del fascicolo, o una valutazione tua.

Se il tuo ente usa un altro schema, per esempio chiude la motivazione con "Ritenuto di", seguilo e scrivilo nel file di stile. Conta che lo schema sia fisso e uguale per tutti, non che sia proprio quello della Guida.

### Un esempio

Prima:

> Premesso che con decreto sindacale ATTO_1 è stato conferito l'incarico di responsabile del Servizio Affari generali; Dato atto che l'abbonamento alla banca dati giuridica on line in uso presso gli uffici comunali verrà a scadenza in data 31 dicembre 2026; Preso atto della necessità di garantire la continuità del servizio di aggiornamento normativo a favore degli uffici;

Dopo:

> Visto il decreto del Sindaco ATTO_1, che conferisce l'incarico di responsabile del Servizio Affari generali, con le relative funzioni, ai sensi dell'art. 109, comma 2, del D.Lgs. 18 agosto 2000, n. 267 (TUEL);
>
> Visto il contratto ATTO_2, relativo all'abbonamento alla banca dati giuridica on line, in scadenza il 31 dicembre 2026;
>
> Considerato che gli uffici usano la banca dati per l'aggiornamento normativo [VERIFICARE: uffici e frequenza d'uso];
>
> Considerato che, senza un nuovo contratto, il servizio si interrompe il 1° gennaio 2027;

"Preso atto della necessità" non è un fatto: è una ragione. Va nella motivazione, dove deve poggiare su un fatto. Il [VERIFICARE] segnala ciò che chi scrive non sa ancora: quali uffici usano la banca dati, e quanto. Lo schema ha fatto emergere anche un atto che la versione originale non citava: il contratto in scadenza.

### Il prompt per riordinare

Per un atto già scritto, o per il vecchio modello dell'ufficio, fai classificare le frasi prima di riscriverle.

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

Con la tabella davanti riscrivi tu, oppure usa il prompt di revisione più avanti. Le frasi segnate come superflue valutale una per una: a volte ripetono, a volte contengono l'unico dato utile.

## Sintassi e lessico

La Parte I della Guida e le direttive indicano le stesse regole di fondo. Qui sono riscritte come istruzioni, ciascuna con il suo controllo.

### Frasi brevi, un'informazione per frase

La Guida chiede periodi brevi e frasi semplici, la principale prima delle subordinate, pochi incisi.[^12] Per il modello: "Una frase, un'informazione. Di regola sotto le 25 parole. La principale all'inizio. Niente incisi tra soggetto e verbo." Nel preambolo e nella motivazione la regola vale per ogni paragrafo. Un Visto può essere lungo perché cita un atto, ma non deve contenere anche la ragione per cui lo cita.

### Forma attiva, soggetto espresso, indicativo presente

Il passivo nasconde chi agisce. "La domanda deve essere presentata entro il 30 novembre" non dice chi la presenta; "Il richiedente presenta la domanda entro il 30 novembre" sì. Nel dispositivo il soggetto è la responsabilità: se manca, nessuno sa chi deve fare che cosa.

Secondo la Guida l'indicativo presente ha già valore prescrittivo e sostituisce "dovere" più l'infinito: "il Servizio trasmette", non "il Servizio dovrà provvedere a trasmettere".[^13] I verbi modali restano quando esprimono una differenza giuridica. "Può" indica una facoltà, e se la norma prevede una facoltà la parola non si tocca.

Prima:

> 3. di dare atto che si provvederà alla liquidazione della spesa a seguito di presentazione di regolare fattura elettronica, previo accertamento della regolarità della prestazione;

Dopo:

> 3. di stabilire che il responsabile del Servizio Affari generali liquida la spesa con atto successivo, dopo aver verificato la fattura elettronica e la regolarità della prestazione;

### Verbi, non nomi

Le nominalizzazioni, cioè i nomi in "-zione" e "-mento" ricavati dai verbi, allungano la frase e la rendono astratta. La Guida dà l'esempio: "Il pagamento si effettua allo sportello" diventa "Si paga allo sportello".[^14] Allo stesso modo "si procede all'effettuazione della verifica" diventa "si verifica".

C'è un'eccezione che il modello deve conoscere. Alcuni nomi indicano un istituto giuridico: impegno, liquidazione, affidamento, revoca, concessione. "L'affidamento diretto" resta. L'istruzione giusta è: "Usa il verbo al posto del nome derivato, salvo quando il nome indica un istituto giuridico."

### Parole comuni, sigle sciolte, norme citate per esteso

La Guida chiede di limitare arcaismi e latinismi. Le parole straniere vanno usate solo se d'uso comune e senza equivalente italiano. Le sigle si scrivono per esteso alla prima occorrenza, con la sigla tra parentesi.[^15] La tabella raccoglie le formule più frequenti negli atti e un'alternativa. È una scelta di questo libro, sulla linea della Guida e delle direttive.

| Invece di | Scrivi |
|---|---|
| si rende necessario procedere all'impegno | occorre impegnare |
| in data odierna | oggi, o la data |
| all'uopo, de quo, ivi | a questo scopo, questo, lì |
| il suddetto, il predetto | il nome, ripetuto |
| in ordine a, in merito a | su |
| ai sensi e per gli effetti di | ai sensi di |
| ai sensi della normativa vigente | la norma, o niente |
| codesto Comune | il Comune di [nome] |

Le sigle meritano attenzione. DURC, CIG, RUP, PEG e MePA sono ovvie in ufficio, non per il destinatario. E sciogliere una sigla scopre gli errori. RUP oggi significa "responsabile unico del progetto", mentre "responsabile unico del procedimento" era la formula del Codice abrogato.[^16] Se il modello scrive la seconda, probabilmente attinge al vecchio Codice: controlla con più attenzione le norme che cita.

Le norme si citano per esteso alla prima occorrenza, poi in forma abbreviata; la Parte III della Guida regola i riferimenti ad altri atti.[^17] Il modello usa volentieri "ai sensi della normativa vigente" o "ai sensi di legge": sono formule che nessuno può smentire. Ma un riferimento che non si può verificare non motiva nulla. L'istruzione è: "Non scrivere «normativa vigente» né «ai sensi di legge»: cita la norma, o scrivi [VERIFICARE: norma]."

### Il lessico giuridico non si semplifica

Semplificare la forma non autorizza a cambiare i termini. Molte parole dell'atto sembrano sinonimi e non lo sono.

- Revoca e annullamento d'ufficio. La prima si fonda su sopravvenuti motivi di pubblico interesse, su un mutamento della situazione di fatto o, con alcune eccezioni, su una nuova valutazione dell'interesse pubblico. Il secondo si fonda sull'illegittimità dell'atto (artt. 21-quinquies e 21-nonies L. 241/1990).[^18]
- Autorizzazione e concessione, sospensione e decadenza: istituti diversi, con effetti diversi.
- "Deve" e "può", "e" e "o", "entro" e "dal": cambiano il significato quanto un numero.

Dai al modello l'elenco dei termini da non toccare, presi dalla norma o dal regolamento che l'atto applica. Più avanti, nella sezione sulle coppie prima e dopo, c'è un esempio di che cosa succede senza.

### Il genere

La direttiva del 2007 ricordata all'inizio chiede un linguaggio non discriminatorio. Nel 2023 l'Accademia della Crusca, interpellata dal Comitato pari opportunità della Corte di cassazione, ha indicato una linea per gli atti giudiziari. Niente asterischi né schwa. Uso ampio dei nomi di cariche e professioni al femminile. Maschile non marcato quando si parla dell'organo o della funzione in astratto.[^19] È una linea utile anche per gli atti comunali.

Il modello, senza regole, può scegliere ogni volta in modo diverso: tutto al maschile, doppie forme in ogni frase, perfino asterischi se gli chiedi un linguaggio inclusivo. Serve una regola dell'ente, concordata con chi firma e scritta nel file di stile. C'è anche un effetto pratico dei segnaposto. Con RICHIEDENTE_1 il modello non conosce il genere della persona e di solito concorda tutto al maschile: quando reinserisci i dati, correggi gli accordi.

### Le abitudini dell'IA

I modelli generalisti hanno abitudini proprie, che si sommano al burocratese: aggettivi di enfasi ("puntuale e approfondita istruttoria"), formule di raccordo ("in un'ottica di", "al fine di garantire"), grassetti, titoli ed elenchi puntati. Nell'esperimento del capitolo sul metodo del prompt, senza indicazioni, il modello ha scelto da solo grassetti, titoli e tabelle. Servono a questo le regole 6 e 12 del file di stile e la richiesta di testo semplice nella riga Formato.

## Misurare la leggibilità

### La lunghezza delle frasi

La misura più semplice è contare le parole di ogni frase: il programma di videoscrittura conta quelle della selezione. Non chiedere il conteggio al modello. Lavora su frammenti di parole e spesso sbaglia i conti (lo spiega il capitolo su come funziona lo strumento). Chiedigli di indicare le frasi che gli sembrano oltre le 25 parole, poi controlla tu.

### L'indice Gulpease

L'indice Gulpease è la formula di leggibilità più usata per l'italiano. L'ha messa a punto nel 1988 il Gruppo universitario linguistico pedagogico (GULP) dell'Università di Roma La Sapienza.[^20] Usa solo due misure, la lunghezza delle parole in lettere e la lunghezza delle frasi:

Gulpease = 89 + (300 × numero di frasi − 10 × numero di lettere) / numero di parole

Il risultato va da 0 a 100: più è alto, più il testo è facile.

| Indice | Testo difficile per chi ha |
|---|---|
| sotto 80 | la licenza elementare |
| sotto 60 | la licenza media |
| sotto 40 | il diploma superiore |

Un esempio dalla motivazione della determina sulla banca dati.

Prima:

> Considerato che, a seguito dell'effettuazione di un'indagine preliminare finalizzata all'individuazione dell'offerta maggiormente vantaggiosa, si è proceduto all'acquisizione del preventivo dell'operatore economico Editrice Esempio S.r.l., il quale, in relazione alle esigenze manifestate dagli uffici comunali, risulta congruo e rispondente alle necessità dell'Ente, e che pertanto si rende necessario procedere all'affidamento del servizio in oggetto;

Dopo:

> Considerato che il Servizio ha confrontato i preventivi di tre operatori;
>
> Considerato che Editrice Esempio S.r.l. offre il prezzo più basso per un servizio adatto alle esigenze degli uffici;
>
> Considerato che il prezzo è in linea con quello pagato negli anni precedenti;

La prima versione è una frase di 61 parole, con indice 31. La seconda ha tre frasi, di 11, 18 e 13 parole, e indice 58.[^21] Anche la versione nuova resta "difficile" per chi ha la licenza media: un atto contiene nomi e termini tecnici che la formula penalizza. L'indice serve a confrontare due versioni dello stesso testo, non a raggiungere una soglia.

Nota che cosa è cambiato oltre alla forma. La versione nuova dice quanti preventivi sono stati confrontati e con che cosa il prezzo è stato giudicato congruo. Il modello non può saperlo: nell'esempio i fatti vengono dal fascicolo del caso inventato. La versione chiara rende evidente se mancano, e la bozza deve mostrarli come [VERIFICARE].

### I limiti dell'indice

La formula misura solo lunghezze. Non sa se una parola è comune: "uopo" è corta e conta come facile. Non misura l'ordine delle informazioni, la coerenza, la precisione giuridica. Un testo spezzato in frasi brevi senza connettivi ottiene un indice migliore ed è più difficile da capire.

Il risultato dipende poi da come lo strumento conta le frasi. La versione nuova dell'esempio vale 58 se ogni punto e virgola chiude una frase. Vale 44 se lo strumento conta solo i punti fermi: il testo non ne ha, e diventa una frase sola. Vale circa 80 se anche i punti di "S.r.l." vengono letti come fine frase. Gli atti sono pieni di "art.", "n." e "D.Lgs.": per confrontare due versioni usa lo stesso strumento e lo stesso testo.

Esistono strumenti più raffinati. READ-IT, dell'ItaliaNLP Lab dell'Istituto di linguistica computazionale del CNR, valuta molte caratteristiche del testo oltre alla lunghezza.[^22] Altri segnalano le parole fuori dal vocabolario di base di Tullio De Mauro, cioè le parole più usate e comprese.[^23] Una rassegna dei parametri che rendono più semplice l'italiano istituzionale è uscita nel 2024.[^24] Un calcolatore on line, però, riceve il testo che incolli: usalo solo per testi senza dati personali.

### Il giudizio di un lettore

Nessuna formula dice se un testo si capisce: lo dice chi lo legge. Il modello può fare da primo lettore, se gli chiedi di segnalare i punti difficili senza riscriverli.

```
Testo di un atto (senza dati personali):
[testo]
Fine del testo. Non riscriverlo. Leggilo come un cittadino
senza formazione giuridica. Elenca in una tabella le frasi che non si
capiscono alla prima lettura, le parole tecniche non spiegate e le sigle
non sciolte, ciascuna con il motivo in una riga.
Non proporre modifiche al contenuto.
```

Il suo giudizio, però, non sostituisce quello di una persona. Uno studio del 2025 su testi amministrativi italiani ha confrontato semplificazioni fatte da persone e da ChatGPT. La qualità del risultato varia molto secondo il prompt: lo strumento è un aiuto utile, ma richiede la revisione umana.[^25]

Una prova pratica: dai la versione nuova a un collega di un altro servizio e chiedigli di dire in due righe che cosa decide l'atto e perché. Se ci riesce, il testo funziona.

## Il prompt di revisione linguistica

L'IA serve in due modi. Il primo è scrivere chiaro dall'inizio, con file di stile, scheletro e schema Visto e Considerato nel prompt per l'atto: costa meno che correggere dopo. Il secondo è rivedere un testo esistente, come il vecchio modello dell'ufficio o la bozza di un collega. Qui il rischio principale è cambiare il significato.

Un atto già firmato o una bozza vera contengono spesso dati personali: toglili prima di incollare il testo. Sostituire i nomi con segnaposto come RICHIEDENTE_1 è pseudonimizzare, non anonimizzare. Il testo resta un dato personale e va solo nello strumento dell'ente, con il contratto che designa il fornitore responsabile del trattamento (art. 28 GDPR). Dati sulla salute, su condanne e reati o su minori non vanno nel prompt nemmeno lì. Le regole complete sono nel capitolo sul metodo del prompt.

### Il prompt

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

La tabella rende visibile ogni modifica; l'elenco finale indica dove guardare per primo. Il file di stile va nelle istruzioni del progetto o incollato prima del testo.

### Il controllo: confrontare le due versioni

Il modello può cambiare il contenuto anche quando gli dici di non farlo. Fai due controlli.

Il primo è meccanico. La funzione di confronto tra documenti del programma di videoscrittura mostra ogni parola cambiata: scorri numeri, date, norme e termini giuridici. È più affidabile del modello per trovare un importo toccato.

Il secondo è un confronto di contenuto, in una conversazione nuova, senza le istruzioni di revisione.

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

Il confronto fatto dal modello non sostituisce il tuo: ti dice dove guardare.

### Coppie prima e dopo: una revisione che cambia il significato

L'ultima coppia mostra l'errore tipico della semplificazione. La frase viene dalla delibera di concessione di un contributo all'ASD Borgo Esempio.

Originale:

> Il contributo è revocato, in tutto o in parte, qualora l'iniziativa non sia realizzata o sia realizzata in misura difforme dal programma presentato.

Revisione sbagliata:

> Se l'iniziativa non si fa o cambia, il Comune può togliere il contributo.

La frase è più corta, e l'indice Gulpease salirebbe. Ma "è revocato", che vincola il Comune, è diventato "può togliere", una facoltà. Il termine giuridico è sparito. "In tutto o in parte" è caduto. "In misura difforme dal programma presentato" è diventato "cambia", che non dice rispetto a che cosa.

Revisione corretta:

> Il Comune revoca il contributo, in tutto o in parte, se l'associazione non realizza l'iniziativa o la realizza in misura diversa dal programma presentato.

Forma attiva, soggetto espresso, indicativo presente, e la stessa regola dell'originale. Due punti, però, vanno controllati. La forma attiva obbliga a dire chi agisce: "il Comune" e "l'associazione" non erano nell'originale, e vanno confermati sul regolamento. E "revoca" resta. Nei regolamenti sui contributi la parola indica spesso la perdita del beneficio per inadempimento, che è cosa diversa dalla revoca dell'art. 21-quinquies. Proprio per questo si prende dal regolamento che l'atto applica, e non si cambia. È il risultato che il prompt di revisione chiede e il confronto controlla.

### Controlli sulla lingua prima della firma

1. La struttura segue lo scheletro dell'ente.
2. Ogni Visto ha estremi verificati; ogni Considerato, un documento del fascicolo o una tua valutazione.
3. Ogni punto del dispositivo dice chi fa che cosa; nessuno attesta pareri o controlli non ancora resi.
4. Sigle sciolte alla prima occorrenza; nessuna "normativa vigente".
5. Termini giuridici identici a quelli della norma o del regolamento; "deve" e "può" al loro posto.
6. Il confronto tra le versioni non mostra numeri, date, norme o condizioni cambiati.
7. Segnaposto sostituiti e accordi di genere corretti; nell'atto non resta il carattere `[`.

## In sintesi

- Le regole di chiarezza hanno fonti scritte, dal Codice di stile del 1993 alla Guida ITTIG-Crusca del 2011. Non vincolano da sole, ma si citano, si spiegano a chi firma e si danno all'IA.
- Senza regole il modello riproduce le formule più frequenti degli atti; quando semplifica può cambiare il significato.
- Dai all'IA uno scheletro fisso. Numeri, date, pareri e visti non li scrive il modello.
- Visto per norme e atti con i loro estremi, Considerato per fatti e ragioni: ogni frase ha una funzione e un controllo.
- Frasi brevi, forma attiva, verbi al posto dei nomi, sigle sciolte, norme citate per esteso. I termini giuridici non si semplificano.
- L'indice Gulpease misura solo lunghezze e cambia con il modo di contare: serve a confrontare versioni, non come traguardo. Il giudizio di un lettore vero vale di più.
- Prima di incollare un atto vero togli i dati personali; con i segnaposto, solo lo strumento dell'ente.
- Dopo ogni revisione confronta le due versioni: il contenuto deve restare identico, la forma migliorare.

[^1]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 3, commi 1 e 4, normattiva.it. Il comma 3 ammette la motivazione per relazione ad altro atto, che va indicato e reso disponibile.

[^2]: I. Calvino, *Per ora sommersi dall'antilingua*, in Il Giorno, 3 febbraio 1965, poi con il titolo *L'antilingua* in *Una pietra sopra*, Einaudi, 1980. Calvino parla di "terrore semantico", la fuga davanti alle parole che hanno un significato preciso.

[^3]: Presidenza del Consiglio dei ministri, Dipartimento della funzione pubblica, *Codice di stile delle comunicazioni scritte ad uso delle amministrazioni pubbliche. Proposta e materiali di studio*, Istituto Poligrafico e Zecca dello Stato, 1993; A. Fioritto (a cura di), *Manuale di stile. Strumenti per semplificare il linguaggio delle amministrazioni pubbliche*, il Mulino, 1997.

[^4]: Ministro per la funzione pubblica, *Direttiva sulla semplificazione del linguaggio dei testi amministrativi*, 8 maggio 2002, in Gazzetta Ufficiale n. 141 del 18 giugno 2002, gazzettaufficiale.it. La direttiva motiva le frasi brevi con le ricerche secondo cui le frasi con più di 25 parole sono difficili da capire e ricordare. È un'indicazione, non un limite: farne una regola del file di stile è una scelta di questo libro.

[^5]: Ministro per la funzione pubblica, *Direttiva in materia di semplificazione del linguaggio*, 24 ottobre 2005, funzionepubblica.gov.it. La direttiva chiede di scrivere pensando ai destinatari e di scegliere le parole del linguaggio comune.

[^6]: Ministro per le riforme e le innovazioni nella pubblica amministrazione e Ministro per i diritti e le pari opportunità, *Misure per attuare parità e pari opportunità tra uomini e donne nelle amministrazioni pubbliche*, direttiva 23 maggio 2007, funzionepubblica.gov.it. Tra gli esempi la direttiva indica l'uso, per quanto possibile, di nomi collettivi o che comprendono persone dei due generi.

[^7]: ITTIG-CNR (oggi IGSG-CNR) e Accademia della Crusca, *Guida alla redazione degli atti amministrativi. Regole e suggerimenti*, Firenze, 2011, ittig.cnr.it. La prima versione è stata presentata all'ITTIG il 18 giugno 2010, quella definitiva all'Accademia della Crusca l'11 febbraio 2011. La Guida definisce economico il testo che "contiene tutto quello che è necessario e solo quello che è adeguato allo sviluppo del suo contenuto".

[^8]: Anthropic, *Prompting best practices*, 2026, platform.claude.com, sezione "Control the format of responses".

[^9]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte II, sulla struttura del provvedimento: parte iniziale, centrale e finale.

[^10]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte II, sul dispositivo. Per la forma ad articoli la Guida rinvia alle regole per la redazione dei testi normativi.

[^11]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte II; R. Libertini, *Un nuovo schema per la motivazione degli atti amministrativi: i visto e i considerato*, in Informatica e diritto, 2016, n. 2, ittig.cnr.it, che ricostruisce le formule della prassi ("premesso che", "dato atto che", "preso atto che") sostituite dallo schema.

[^12]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I, sulla sintassi: periodi brevi e frasi semplici, principale prima delle subordinate, pochi incisi, forma attiva, frasi affermative. La regola sugli incisi tra soggetto e verbo è una scelta di questo libro.

[^13]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I, sui verbi: l'indicativo presente al posto di "dovere" più l'infinito.

[^14]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I, sulle nominalizzazioni, da cui viene l'esempio.

[^15]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte I, sul lessico e sulle sigle.

[^16]: D.Lgs. 31 marzo 2023, n. 36, *Codice dei contratti pubblici*, art. 15, normattiva.it. "Responsabile unico del procedimento" era la formula dell'art. 31 del D.Lgs. 18 aprile 2016, n. 50, abrogato dal 1° luglio 2023 (art. 226 del D.Lgs. 36/2023).

[^17]: ITTIG-CNR e Accademia della Crusca, *Guida alla redazione degli atti amministrativi*, cit., Parte III, sui riferimenti ad altri atti, che per le citazioni degli atti normativi riprende le tecniche di redazione dei testi legislativi.

[^18]: L. 7 agosto 1990, n. 241, cit., art. 21-quinquies, sulla revoca per sopravvenuti motivi di pubblico interesse, per mutamento della situazione di fatto non prevedibile al momento dell'adozione o per nuova valutazione dell'interesse pubblico originario, quest'ultima esclusa per le autorizzazioni e per i provvedimenti che attribuiscono vantaggi economici; art. 21-nonies, sull'annullamento d'ufficio del provvedimento illegittimo, normattiva.it.

[^19]: Accademia della Crusca, *Parere sulla scrittura negli atti giudiziari rispettosa della parità di genere*, 2023, accademiadellacrusca.it. Il parere risponde a un quesito del Comitato pari opportunità del Consiglio direttivo della Corte di cassazione.

[^20]: P. Lucisano e M. E. Piemontese, *GULPEASE: una formula per la predizione della difficoltà dei testi in lingua italiana*, in Scuola e città, 1988, n. 3. Le soglie della tabella sono quelle proposte dagli autori.

[^21]: Calcolo di questo libro. Sono contate come parole le sequenze di lettere, separando quelle unite da apostrofo ("dell'Ente" vale due parole); come lettere solo i caratteri alfabetici; "S.r.l." come una parola, salvo nell'ultima variante descritta nel testo, dove vale tre parole e tre fine frase. Nella variante principale ogni paragrafo chiuso da punto e virgola conta come una frase. Altri strumenti usano criteri diversi e danno valori diversi.

[^22]: F. Dell'Orletta, S. Montemagni e G. Venturi, *READ-IT: Assessing Readability of Italian Texts with a View to Text Simplification*, in Proceedings of the Second Workshop on Speech and Language Processing for Assistive Technologies, 2011, aclanthology.org.

[^23]: T. De Mauro, *Il Nuovo vocabolario di base della lingua italiana*, 2016, internazionale.it.

[^24]: G. Fiorentino e V. Ganfi, *Parametri per semplificare l'italiano istituzionale: revisione della letteratura*, in Italiano LinguaDue, vol. 16, n. 1, 2024, pp. 220-237, riviste.unimi.it.

[^25]: S. Ondelli e A. Santoro, *Come usare ChatGPT per semplificare i testi amministrativi? Alcuni confronti tra intelligenza umana e intelligenza artificiale*, in Italiano LinguaDue, vol. 17, n. 2, 2025, pp. 1327-1377, riviste.unimi.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 27 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- La bozza diceva che una motivazione incomprensibile 'rispetta la lettera della norma'.
- L'oggetto modello parlava di 'Rinnovo' per un nuovo affidamento diretto.
- 'Visto il contratto ATTO_2, che affida l'abbonamento': un contratto non affida nulla.
- Il testo diceva 'Il modello non sa... e lo segnala', come se la versione 'Dopo' l'avesse scritta l'IA. Più avanti però dichiarava che le coppie erano costruite a mano.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
