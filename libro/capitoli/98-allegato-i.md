# Allegato I. Come è stato scritto questo libro {.unnumbered}

In questo allegato: gli strumenti, la redazione affidata all'IA, le fonti, gli errori intercettati, il lavoro dell'autore, il perché della formula "con l'IA", lo schema da riusare in ufficio e il prompt integrale dell'esperimento.

Il libro è stato scritto con Claude, di Anthropic, applicando il metodo che insegna. Qui si racconta come: chi ha deciso, chi ha scritto, chi ha controllato, che cosa è andato storto. Le pagine che seguono servono a chi vuole giudicare il libro e a chi vuole usare lo stesso schema per un testo lungo, come un regolamento, una relazione o un piano.

## Perché raccontarlo {.unnumbered}

Il libro chiede agli uffici di rendere conoscibile l'uso dell'IA. Per la pubblica amministrazione è un principio di legge: l'IA si usa "assicurando agli interessati la conoscibilità del suo funzionamento e la tracciabilità del suo utilizzo" (art. 14, comma 1, della L. 23 settembre 2025, n. 132).[^1] Un manuale che insegna la tracciabilità deve applicarla a sé stesso.

Per i testi pubblicati allo scopo di informare il pubblico su questioni di interesse pubblico, il Regolamento (UE) 2024/1689 (AI Act) chiede a chi usa il sistema di IA di rendere noto che il testo è stato generato o manipolato artificialmente. L'obbligo non si applica se il testo ha avuto una revisione umana o un controllo editoriale e una persona fisica o giuridica ne detiene la responsabilità editoriale (art. 50, par. 4).[^2] La dichiarazione in copertina non dipende da questa norma: fa parte del metodo.

Ogni capitolo si chiude con "Dietro le quinte": come è stato scritto, che cosa ha sbagliato l'IA, che cosa è stato corretto. Qui i pezzi si ricompongono nel processo intero, limiti compresi.

## Gli strumenti {.unnumbered}

Quattro elementi, ciascuno con un compito.

- *Claude*, di Anthropic, usato attraverso Claude Code: un ambiente che lavora sui file di una cartella di progetto e può affidare compiti diversi a istanze separate del modello. Non è una raccomandazione: per scegliere uno strumento in ufficio valgono i criteri del capitolo su come scegliere e acquistare uno strumento di IA.
- *Markdown*, per il testo: testo semplice, con pochi segni per titoli, elenchi e note. Un file per capitolo. Il modello lo legge e lo scrive senza perdere la formattazione; una persona lo apre con qualunque programma di testo.
- *Git e GitHub*, per le versioni: ogni modifica resta registrata con data e descrizione, si confronta con la precedente e si può annullare.
- *Pandoc e Typst*, per l'impaginazione.[^3] Pandoc riunisce i capitoli e li converte; Typst compone le pagine del PDF di stampa, nel formato 15x21 cm. Dagli stessi file escono l'EPUB e il DOCX per l'editore.

La scelta ha una ragione: tenere separati il testo e la sua forma. Il testo si scrive una volta, i formati ne derivano. A ogni modifica registrata il libro si rigenera da solo, con il conteggio delle parole e delle parti ancora da scrivere, capitolo per capitolo. Se serve un altro formato di pagina, si cambiano due righe di un file di configurazione e il libro si reimpagina. I prompt escono nel riquadro grigio perché nel testo sono blocchi di codice; le note vanno a piè di pagina senza interventi manuali.

Pandoc e Typst sono gratuiti e open source. Claude si usa con un abbonamento o a consumo, secondo il piano scelto.

## La redazione {.unnumbered}

Il lavoro è organizzato come in una casa editrice. Ogni ruolo è affidato a un'istanza separata del modello, con istruzioni proprie e solo il materiale che le serve: direttore editoriale, ricercatori, autore delle bozze, revisori, verificatori, redattore, caporedattore. Chi rivede un testo lavora in una conversazione diversa da chi l'ha scritto: vede il risultato, non il percorso. È il principio che il capitolo sul flusso di lavoro applica agli atti: un passaggio, un controllo, e la revisione in una conversazione nuova.

### Le regole scritte

Prima delle bozze vengono le regole. Le note di stile sono il file di stile del libro: lettore, tono, struttura dei capitoli operativi, convenzioni dei prompt, esempi solo inventati e ambientati a Borgo Esempio, rimandi per nome del capitolo, formula "con l'IA". Ogni istanza che scrive le riceve insieme a un brief. Ecco alcune righe del brief di scrittura, come sono state usate (i puntini indicano i tagli).

```
Sei l'autore-redattore di una grande casa editrice giuridica. …
Aggiornamento normativo: 6 ottobre 2026. Lettori: istruttori e funzionari
degli enti locali, segretari comunali, responsabili di servizio, DPO e RTD.
- Rimandi interni descrittivi, mai numerici: "nel capitolo sull'AI Act", …
- Tono: diretto e sobrio; … frasi brevi; niente marketing né enfasi.
- Non inventare esperienze personali dell'autore né aneddoti in prima
persona. Non inventare dati, percentuali, sentenze, articoli o numeri
di provvedimento: se non sei sicuro, formula in modo generale e corretto,
o non citarlo. Meglio un'affermazione generale vera che una precisa falsa.
```

Il brief segue lo schema del capitolo sul metodo del prompt: ruolo, contesto, compito, formato, vincoli. L'ultima regola fa per il libro ciò che [VERIFICARE] fa per l'atto: dà il permesso di non sapere e vieta di riempire il vuoto con un dato verosimile.

Le regole cambiano con gli errori, come quelle di ogni file di stile. La regola sul Comune immaginario vieta ancora, per nome, quello usato nelle prime bozze, perché esiste davvero.

### La ricerca condivisa

Prima dei capitoli c'è stata la ricerca. Sei ricerche parallele: linguaggio amministrativo, tecniche di prompt, allucinazioni, dati e regole della pubblica amministrazione, GDPR e AI Act, norme del caso d'esempio. Hanno raccolto 116 informazioni, ciascuna con la fonte e con il grado di affidabilità, più le avvertenze sui limiti di ogni ricerca.

Poi una verifica mirata, soprattutto sulle novità del 2025 e del 2026, su 47 affermazioni: 31 confermate, 2 da correggere, 14 non verificabili con le fonti raggiungibili. Per queste ultime la verifica ha proposto una formulazione prudente e ha indicato dove controllare prima della stampa.

Ricerca e verifica formano una base fattuale unica, con le formulazioni da usare. Tutti i capitoli attingono da lì, e questo li tiene coerenti: le date dell'AI Act dopo il Regolamento (UE) 2026/1744, per esempio, vengono in ogni capitolo dalla stessa verifica.

### Il capitolo campione

Il capitolo sul metodo del prompt è stato scritto per primo ed è il più controllato del libro: oltre cento passaggi in due giri, tra ricerca, esperimento, revisioni e verifiche.

- *Esperimento.* Due prompt per la stessa determina, tre esecuzioni ciascuno, in conversazioni nuove e separate. Un analista separato ha contato ogni testo e ne ha controllato i riferimenti.
- *Revisione.* Otto revisioni, tra fact-checking, revisione legale e GDPR, editing, lettore tipo e prova dei prompt. Oltre duecento segnalazioni.
- *Verifica.* Le segnalazioni gravi sono passate a verificatori indipendenti prima di diventare correzioni, perché anche i revisori sbagliano.

Il capitolo è diventato il riferimento per tono, densità delle note e convenzioni. Dallo stesso lavoro è nato l'indice in quattro parti.

### Gli altri capitoli e gli allegati

Per il resto del libro il ciclo è più corto: una stesura e, di regola, un solo giro di revisione, che unisce fact-checking, revisione legale e GDPR ed editing e applica le correzioni. Ogni stesura parte dagli stessi materiali: base fattuale, note di stile, capitolo campione come modello di qualità, indice completo per i rimandi.

È giusto che il lettore lo sappia. Il capitolo sul metodo del prompt ha avuto otto revisioni separate, gli altri di regola una sola, che le riunisce. Per questi il riscontro dell'autore pesa di più.

## Le fonti che non si potevano aprire {.unnumbered}

L'ambiente di lavoro aveva un accesso alla rete limitato. Normattiva, Gazzetta Ufficiale, EUR-Lex e i siti di AgID, del Garante e della giustizia amministrativa non erano raggiungibili. La ricerca si è fatta sugli estratti dei motori di ricerca e su fonti secondarie autorevoli, confrontate tra loro: riviste giuridiche, siti specializzati, commenti di studi professionali. La documentazione dei produttori di IA è stata letta, dove possibile, nelle copie ufficiali pubblicate su GitHub.

Dove le fonti concordavano, il dato è entrato nel testo. Dove non era possibile riscontrarlo, è stato formulato in modo più generale, oppure tolto. La regola era quella del brief: meglio un'affermazione generale vera che una precisa falsa.

In due delle sei ricerche si è esaurito anche il numero di ricerche web consentite. Lì una parte dei dati viene dalla conoscenza del modello, ed è stata segnata come da collazionare sul testo ufficiale. È il rischio descritto nel capitolo sulla verifica delle norme: un riferimento verosimile, scritto a memoria.

Per questo le note indicano il sito ufficiale e, spesso, la fonte secondaria su cui è stato fatto il riscontro. Il controllo sui testi ufficiali è un passaggio dell'autore, l'ultimo prima della stampa. Per il solo capitolo campione l'elenco dei punti da riscontrare ne conta trentacinque, ciascuno con il sito da aprire e il controllo da fare.

## Gli errori intercettati {.unnumbered}

L'IA ha sbagliato come il libro dice che sbaglia: con sicurezza e in modo verosimile. Questi sono i principali errori registrati nell'impianto e nel capitolo campione, tutti corretti nel testo. Quelli degli altri capitoli sono nei rispettivi "Dietro le quinte".

- *L'esperimento falsato.* Nella prima versione, l'istanza che eseguiva il prompt generico aveva letto i capitoli del libro, e ogni prompt era stato eseguito una sola volta: il confronto non valeva. È stato rifatto da capo, tre volte per prompt, in conversazioni nuove, senza file né ricerca sul web.
- *Il Comune che esiste.* Il Comune immaginario delle prime bozze portava il nome di un Comune vero, in Sicilia. Ora è Borgo Esempio, e anche fornitori e associazioni hanno nomi costruiti su "Esempio".
- *La memoria negata.* Una bozza affermava che l'IA non ricorda nulla tra una conversazione e l'altra. Alcuni strumenti hanno funzioni di memoria: il capitolo su cosa fa un modello linguistico ne spiega i limiti.
- *La soglia senza fonte.* Una bozza attribuiva alla direttiva Frattini del 2002 una soglia di 25 parole per frase, presa da un sito scolastico. La prima correzione rischiava l'errore opposto: far credere che la direttiva non ne parlasse. Secondo le fonti che ne riproducono il testo, la direttiva osserva, citando le ricerche, che le frasi con più di 25 parole sono difficili da capire e ricordare. È un'indicazione, non un limite, e il testo ora lo dice.
- *La stima diventata misura.* Il risparmio di tempo stimato con questionari da un'amministrazione britannica era presentato come misurato. I dati corretti sono nel capitolo iniziale, sull'IA già in ufficio.
- *La checklist incoerente.* Una lista di controllo ammetteva i dati sanitari che il testo dello stesso capitolo vietava.
- *L'impianto.* Le prime proposte di impostazione erano poco adatte a chi scrive da dipendente pubblico. I vincoli li ha fissati l'autore.

Un errore, invece, è del metodo e non del modello. L'elenco delle norme del prompt strutturato non comprendeva l'art. 192 del D.Lgs. 18 agosto 2000, n. 267 (TUEL), sulla determinazione a contrattare, e nessuna bozza strutturata lo ha citato: il modello ha obbedito a "solo queste". Mancava anche l'art. 109, comma 2, sui responsabili nei Comuni senza dirigenti. Ora l'elenco di esempio del capitolo li comprende entrambi.

Erano errori verosimili, che una lettura veloce non coglie. Quasi tutti li hanno trovati revisori con un compito preciso e verificatori che hanno ricontrollato le segnalazioni; l'impianto l'ha corretto l'autore. Il diario di bordo del libro li registra insieme al lavoro svolto.

## Cosa ha fatto l'IA e cosa ha fatto l'autore {.unnumbered}

Le bozze di capitoli e allegati le ha scritte il modello. Le decisioni sono dell'autore. La tabella divide il lavoro.

| Fase | IA | Autore |
|---|---|---|
| Progetto, lettori, vincoli | — | decide |
| Indice e impianto | propone | sceglie |
| Regole e convenzioni | propone, applica | approva |
| Ricerca e bozze | svolge, scrive | — |
| Revisione | segnala, corregge | rilegge, decide |
| Testi ufficiali | elenca i punti | riscontra |
| Responsabilità | nessuna | intera |

*Il progetto.* L'autore ha scelto il tema e i lettori: chi scrive gli atti in un Comune piccolo o medio. Ha fissato i vincoli: nessun atto, dato o nome dell'ente presso cui lavora; esempi solo inventati; opinioni personali, che non impegnano l'amministrazione. Ha deciso che l'uso dell'IA fosse dichiarato e diventasse il tratto distintivo del libro.

*Le decisioni editoriali.* Su richiesta dell'autore il progetto è passato da un manuale pratico a un manuale normativo e operativo in quattro parti, con particolare attenzione alla protezione dei dati: per questo il GDPR ha due capitoli, più quello sulla pubblicazione. L'indice in quattro parti l'ha proposto il modello; adottarlo è stata una scelta dell'autore. Il capitolo campione è stato scritto e controllato prima degli altri, perché fissasse il livello.

*La revisione e la responsabilità.* Restano all'autore la rilettura, la scelta sulle segnalazioni, il riscontro sui testi ufficiali e la responsabilità di ogni pagina. Il modello non risponde di nulla. Come per un atto, risponde chi firma.

## Perché "con l'IA" e non "dall'IA" {.unnumbered}

La formula ha due ragioni: una di diritto d'autore, una di responsabilità.

La prima è nella legge. L'art. 25 della L. 132/2025 ha modificato l'art. 1 della L. 22 aprile 1941, n. 633: sono protette le opere "dell'ingegno umano" di carattere creativo, "anche laddove create con l'ausilio di strumenti di intelligenza artificiale, purché costituenti risultato del lavoro intellettuale dell'autore".[^4] Un testo generato dal modello senza un contributo creativo umano non è protetto come opera dell'ingegno. Un'opera in cui una persona decide progetto, struttura, contenuti e scelte, e usa l'IA come strumento, lo è, se ne ricorrono i presupposti. La legge non fissa una soglia: quanto contributo umano basti si valuta caso per caso. Il capitolo sulla legge italiana sull'IA tratta il tema per le opere del Comune.

La seconda è la stessa degli atti. Per la L. 132/2025 la persona "resta l'unica responsabile dei provvedimenti e dei procedimenti in cui sia stata utilizzata l'intelligenza artificiale" (art. 14, comma 2).[^5] Un libro non è un provvedimento, ma il principio regge: lo strumento propone, la persona decide e ne risponde.

Dire "scritto da un'IA" sarebbe quindi inesatto due volte. Sul piano del diritto d'autore, perché descriverebbe un testo senza autore umano, mentre progetto, vincoli, scelte e riscontri finali sono dell'autore. E sul piano della responsabilità, perché degli errori di questo libro risponde una persona, non uno strumento.

## Lo schema per un testo lungo {.unnumbered}

Lo stesso schema serve in ufficio per un regolamento, una relazione, un piano. Usa lo strumento autorizzato dall'ente e, nel prompt, solo i dati che servono: per un regolamento o un piano, di solito nessun dato personale. Ne parlano il capitolo su quale IA usare in ufficio e i due capitoli sul GDPR.

1. Decidi tu scopo, lettori e indice. Il modello può proporre; la scelta è tua.
2. Costruisci prima la base dei fatti: norme, dati, atti, ciascuno con la fonte e con lo stato della verifica (confermato, da correggere, non verificabile).
3. Scrivi le regole in un file di stile e aggiornalo quando un errore torna.
4. Scrivi e controlla a fondo una parte campione, poi usala come modello per le altre.
5. Separa scrittura e revisione: conversazioni diverse, una revisione per ogni aspetto (fatti, norme, lingua, dati personali).
6. Fai ricontrollare le segnalazioni gravi prima di correggere: anche chi rivede sbaglia.
7. Tieni un diario: che cosa ha fatto l'IA, che cosa ha sbagliato, che cosa hai corretto. Per un atto è la nota di tracciabilità descritta nel capitolo sulla tracciabilità.
8. Prima della firma o dell'approvazione, riscontra sui testi ufficiali ogni norma e ogni dato.

## L'esperimento del capitolo sul prompt {.unnumbered}

Il prompt generico e il prompt strutturato sono stati eseguiti tre volte ciascuno, il 6 ottobre 2026, in conversazioni nuove e separate, senza ricerca sul web, file o altri documenti. Il prompt generico è riportato per intero nel capitolo sul metodo del prompt. Questo è il prompt strutturato integrale, come è stato eseguito: il suo elenco delle norme non comprende ancora gli artt. 109, comma 2, e 192 del TUEL, aggiunti dopo l'esperimento all'elenco di esempio del capitolo.

```
Sei un istruttore amministrativo del Servizio Affari generali
del Comune di Borgo Esempio.
Contesto: il Comune usa da tre anni una banca dati giuridica on line
di Editrice Esempio S.r.l.; l'abbonamento in corso, affidato con ATTO_1,
scade il 31 dicembre 2026.
Dati: rinnovo per un anno dal 1 gennaio 2027; importo euro 1.200,00 oltre IVA;
operatore Editrice Esempio S.r.l.; affidamento tramite MePA; CIG da acquisire;
capitolo di bilancio 1043; responsabile unico del progetto RUP_1.
Norme (solo queste) e cosa regolano:
- D.Lgs. 18 agosto 2000, n. 267 (TUEL): art. 107, funzioni dei responsabili;
art. 183, impegno di spesa; art. 151, comma 4, visto di regolarità contabile;
art. 147-bis, controllo di regolarità amministrativa e contabile.
- D.Lgs. 31 marzo 2023, n. 36: art. 17, commi 1 e 2, decisione di contrarre;
art. 50, comma 1, lett. b), affidamento diretto; art. 49, comma 6, deroga
alla rotazione sotto 5.000 euro; artt. 25 e 26, piattaforme di
approvvigionamento digitale; art. 52, verifiche negli affidamenti diretti
sotto 40.000 euro.
- L. 13 agosto 2010, n. 136, art. 3: tracciabilità dei flussi finanziari.
Esempio (solo struttura e tono, nessun dato): nessuno.
Stile:
FILE DI STILE – Servizio Affari generali – versione 1 del 6 ottobre 2026
Applica queste regole al testo degli atti. Non commentarle.
1. Premesse e motivazione impersonali ("si ritiene"). Mai la prima persona.
2. Una frase, un concetto. Di regola sotto le 25 parole.
3. Frasi affermative. Niente doppie negazioni.
4. Indicativo presente: "il responsabile trasmette", non "deve trasmettere".
5. Verbi, non nomi: "occorre liquidare", non "si procede alla liquidazione".
6. Niente aggettivi valutativi né enfasi, salvo le parole
della norma applicata.
7. Premesse: solo fatti e atti con numero e data. Le ragioni, in motivazione.
8. Dispositivo: punti numerati, un'azione per punto, infinito ("di impegnare").
9. Norme: citazione completa alla prima occorrenza, poi abbreviata.
10. Sigle per esteso alla prima occorrenza, con la sigla tra parentesi.
11. Importi: "euro 1.200,00". Date: "31 dicembre 2026".
12. Nell'atto niente cortesie né chiusure; gli elenchi richiesti vanno dopo.
13. Se manca un dato o una norma: scrivi [VERIFICARE: cosa]. Non inventare.
Formato: oggetto, preambolo (Visto), motivazione (Considerato),
dispositivo (DETERMINA); circa 700 parole; testo semplice.
Compito: scrivi la bozza della determina a contrarre e di affidamento diretto
per il rinnovo per un anno dell'abbonamento.
Fatti: solo i dati sopra. Non dare per avvenuti pareri, votazioni, controlli.
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
Norme fuori elenco: non citarle, scrivi [VERIFICARE: norma da cercare].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

I sei testi generati sono conservati integralmente nell'archivio di lavoro dell'autore, con i conteggi e il giudizio dell'analista su ciascuno.

[^1]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, in Gazzetta Ufficiale, Serie generale, n. 223 del 25 settembre 2025, in vigore dal 10 ottobre 2025, art. 14, comma 1, normattiva.it.

[^2]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, art. 50, par. 4, secondo comma, eur-lex.europa.eu. L'obbligo grava sul deployer, cioè su chi usa il sistema di IA sotto la propria autorità. La disposizione si applica dal 2 agosto 2026 e non è stata modificata dal Regolamento (UE) 2026/1744.

[^3]: Pandoc (pandoc.org) e Typst (typst.app) sono programmi open source; il libro usa Pandoc 3.1. Il formato della pagina è indicato nel file dei metadati del libro.

[^4]: L. 23 settembre 2025, n. 132, cit., art. 25, *Tutela del diritto d'autore delle opere generate con l'ausilio dell'intelligenza artificiale*, che modifica l'art. 1, primo comma, della L. 22 aprile 1941, n. 633, normattiva.it.

[^5]: L. 23 settembre 2025, n. 132, cit., art. 14, comma 2, normattiva.it.
