# PIAO e obiettivi

In questo capitolo: il Piano integrato di attività e organizzazione con l'IA come supporto, dagli obiettivi misurabili alla mappatura dei rischi corruttivi e alla formazione, fino all'adozione dell'IA come obiettivo del Piano.

## Il problema: il piano dell'anno prima

Il Piano integrato di attività e organizzazione (PIAO) dice che cosa il Comune vuole ottenere nei tre anni successivi, con quali persone e con quali cautele. Spesso è il piano dell'anno prima con le date cambiate: obiettivi generici, rischi mappati con norme superate, formazione ridotta a un elenco di corsi.

L'IA può aiutare: riscrive un obiettivo vago con indicatori, confronta una scheda di rischio con le norme vigenti, ordina un piano formativo. Ma non conosce i dati del Comune, come i giorni di attesa per la carta d'identità. Se il prompt non glieli dà, può inventarli; e un numero inventato in un obiettivo pesa sulla valutazione di qualcuno e sui premi.

La regola del capitolo è una: l'IA propone la forma, l'ente mette i numeri e fa le scelte.

Il PIAO è quasi tutto verde, nel senso del semaforo del capitolo sugli strumenti: va bene ogni strumento ammesso per iscritto dall'ente. Restano fuori dal prompt i nomi nelle schede degli obiettivi, al cui posto va il ruolo; le cessazioni nominative del piano dei fabbisogni; gli esiti delle valutazioni individuali. Resta fuori anche ogni fatto corruttivo o disciplinare riferito a qualcuno, pure senza nome: in un ente piccolo il fatto basta a riconoscere la persona, e se riguarda un reato è un dato rosso, che non entra con nessuno strumento.

## Il PIAO in breve

### Le norme

L'art. 6 del D.L. 9 giugno 2021, n. 80, convertito dalla L. 6 agosto 2021, n. 113, obbliga le amministrazioni con più di cinquanta dipendenti ad adottare il PIAO entro il 31 gennaio di ogni anno: il Piano dura tre anni e si aggiorna ogni anno. Per quelle con meno di cinquanta dipendenti il comma 6 prevede modalità semplificate. Il comma 2 elenca i contenuti, tra cui obiettivi di performance, obiettivi formativi per "la completa alfabetizzazione digitale", anticorruzione e procedure da semplificare "anche mediante il ricorso alla tecnologia". Se il Piano manca, si applicano le sanzioni richiamate dal comma 7: tra queste, il divieto di erogare la retribuzione di risultato ai dirigenti che hanno concorso alla mancata adozione e quello di assumere personale.[^1]

Il D.P.R. 24 giugno 2022, n. 81, ha assorbito nel PIAO, tra gli altri, i piani della performance, della prevenzione della corruzione, dei fabbisogni di personale, del lavoro agile e delle azioni positive; negli enti locali vi confluisce anche il piano dettagliato degli obiettivi.[^2] Per un Comune, un piano anticorruzione adottato come documento a sé è un riferimento superato: oggi è una sottosezione del PIAO.

Il D.M. 30 giugno 2022, n. 132, ha definito il contenuto del Piano.[^3]

| Parte del Piano | Contenuto | Sotto i 50 dipendenti |
|---|---|---|
| Sezione 1 | scheda anagrafica | dovuta |
| 2.1 Valore pubblico | obiettivi generali | non dovuta |
| 2.2 Performance | obiettivi e indicatori | non dovuta |
| 2.3 Rischi corruttivi e trasparenza | mappatura e misure | semplificata |
| Sezione 3 | struttura, lavoro agile, fabbisogni, formazione | in parte |
| Sezione 4 | monitoraggio | non dovuta |

### Il piano semplificato di Borgo Esempio

Borgo Esempio ha 38 dipendenti e adotta il piano semplificato dell'art. 6 del decreto. Nel triennio aggiorna la sottosezione sui rischi corruttivi solo in presenza di fatti corruttivi, modifiche organizzative rilevanti, disfunzioni amministrative significative o modifiche degli obiettivi di performance. Alla scadenza del triennio la rivede sui risultati dei monitoraggi. Anche la sezione 3 è ridotta: controlla sull'art. 6 quali parti sono dovute.

Il Piano lo approva la Giunta entro il 31 gennaio o, se il termine per il bilancio di previsione è differito, entro trenta giorni dall'approvazione del bilancio. Deve essere coerente con il Documento unico di programmazione (DUP) e con il bilancio.[^4]

Il decreto non chiede agli enti sotto i cinquanta dipendenti le sottosezioni sul valore pubblico e sulla performance. Ma gli enti locali adeguano i propri ordinamenti ai principi del D.Lgs. 27 ottobre 2009, n. 150, su obiettivi, valutazione e premi,[^5] e senza obiettivi non si valuta la performance. Chiedi al segretario dove li scrive il tuo ente: nella sottosezione 2.2, come Borgo Esempio, o in un piano degli obiettivi collegato al piano esecutivo di gestione (PEG).

## Obiettivi misurabili

### Cosa chiede la legge

L'art. 5, comma 2, del D.Lgs. 150/2009 vuole obiettivi rilevanti, specifici e misurabili, capaci di migliorare in modo significativo i servizi, riferiti di norma a un anno, confrontabili con standard, con enti omologhi e con il triennio precedente, correlati alle risorse. L'acronimo SMART, molto diffuso, non è nella legge. Pesi, scale e procedura li fissa il sistema di misurazione e valutazione della performance dell'ente (art. 7).

Un obiettivo misurabile ha almeno un indicatore, con formula, fonte del dato, valore di partenza e valore atteso. Una classificazione diffusa distingue quattro tipi di indicatori; quelli validi per il tuo ente, con le loro definizioni, li indica il sistema di misurazione.

| Tipo | Domanda | Esempio |
|---|---|---|
| Efficienza | con quali risorse? | ore di lavoro per pratica |
| Efficacia | il risultato arriva all'utente, e quando? | giorni medi di attesa |
| Qualità | come lo giudica chi lo riceve? | reclami, questionario |
| Stato di attuazione | la fase è fatta nei tempi? | atto adottato entro una data |

Gli indicatori di stato di attuazione dicono che qualcosa è stato fatto, non che è servito: accanto a loro serve un indicatore di risultato.

### Il prompt di riscrittura

Il prompt è quello del capitolo sul metodo del prompt, con due righe nuove: Dati disponibili e Requisiti.

```
Sei un istruttore che prepara il PIAO di un Comune di [numero] abitanti.
Contesto: obiettivo [anno] del Servizio [nome], collegato all'obiettivo
del DUP "[testo]". Testo attuale: "[obiettivo generico]".
Dati disponibili (solo questi): [dato, fonte, anno, valore].
Requisiti: art. 5, comma 2, D.Lgs. 150/2009: specifico, misurabile,
riferito a un anno, confrontabile, correlato alle risorse.
Compito: riscrivi l'obiettivo con titolo, descrizione, fasi con data e
al massimo tre indicatori, ciascuno con formula, fonte, valore di
partenza e valore atteso. Partenza: solo dai dati sopra, altrimenti
[VERIFICARE: dato da rilevare]. Atteso: proposta motivata e
[VERIFICARE: decisione del responsabile]. Non citare medie né studi.
Formato: scheda in testo semplice; poi, separati, dubbi e assunzioni.
```

La riga Dati disponibili è l'unica fonte dei valori di partenza. Il valore atteso è una scelta: il modello lo propone, il responsabile lo decide con il segretario, la Giunta lo approva. Il divieto di medie e studi esclude frasi come "in linea con la media nazionale".

### La bozza commentata

L'obiettivo 2026 del Servizio Demografici era: "Migliorare l'efficienza e la qualità dei servizi demografici, garantendo la massima soddisfazione dell'utenza". Dall'agenda on line il servizio ha estratto un solo dato: nel 2025 l'attesa media per la carta d'identità elettronica (CIE) è stata di 24 giorni. La bozza, con dati e date inventati:

```
PIAO 2027-2029 – Sottosezione 2.2 Performance – Obiettivo 2027/04
Servizio: Demografici
Obiettivo DUP: "Semplificare l'accesso ai servizi anagrafici"
Titolo: Ridurre l'attesa per la carta d'identità elettronica (CIE)
Descrizione: due aperture pomeridiane al mese per la CIE e promozione
dei certificati anagrafici on line, per liberare tempo allo sportello.
Fasi:
1. nuovo orario approvato: entro 28 febbraio 2027 [VERIFICARE: atto
   e organo competente];
2. avviso ai cittadini sul sito e allo sportello: entro 15 marzo 2027;
3. rilevazione dei tempi: 30 giugno, 30 settembre, 31 dicembre 2027.
Indicatori:
I1 Attesa media per la CIE (efficacia). Formula: media dei giorni
   tra prenotazione e appuntamento. Fonte: agenda on line.
   Partenza 2025: 24 giorni. Atteso 2027: 15 giorni
   [VERIFICARE: decisione del responsabile].
I2 Appuntamenti entro 20 giorni (efficacia). Formula: appuntamenti
   entro 20 giorni dalla prenotazione / totali x 100. Fonte: agenda
   on line. Partenza 2025: [VERIFICARE: dato da rilevare].
   Atteso 2027: 80% [VERIFICARE: decisione del responsabile].
I3 Certificati on line (efficacia). Formula: certificati scaricati
   on line dai residenti / certificati totali x 100.
   Fonte: [VERIFICARE: disponibilità del dato].
Peso: [VERIFICARE: sistema di misurazione e valutazione].
Risorse: personale del servizio [VERIFICARE: costo delle aperture].
```

I punti critici.

*Valori di partenza.* Solo I1 ne ha uno, perché solo quello era nel prompt. Gli altri si chiudono con un'estrazione, non con una stima.

*Valori attesi.* Quindici giorni sono una proposta. Per deciderli serve un conto che il modello non può fare: quanti appuntamenti in più danno due pomeriggi al mese. Se il conto non torna, il valore si cambia prima dell'approvazione.

*Fonte.* Se il Comune non può estrarre il dato di I3, l'indicatore si toglie: un indicatore che non si può misurare è una promessa.

*Risorse e fasi.* Le aperture pomeridiane costano, e gli obiettivi vanno correlati alle risorse. Chi fissa l'orario di apertura al pubblico va verificato sul regolamento degli uffici e dei servizi: per questo la fase 1 ha un [VERIFICARE].

*Tipi.* I tre indicatori sono tutti di efficacia. Va bene: il tipo serve a scegliere che cosa misurare, non a riempire caselle.

*Persone.* La scheda indica il servizio, non chi lo dirige.

### Errori tipici dell'IA negli obiettivi

| Errore | Esempio | Rimedio |
|---|---|---|
| Valori inventati | "partenza: 30 giorni" senza dato | riga Dati disponibili |
| Confronti inventati | "media nazionale: 18 giorni" | divieto di medie e studi |
| Attività ordinaria | "garantire l'apertura dello sportello" | chiedere un miglioramento |
| Solo stato di attuazione | "adozione dell'atto entro giugno" | un indicatore di risultato |
| Indicatore senza fonte | "soddisfazione dell'utenza" | fonte e costo della rilevazione |
| Troppi indicatori | sei indicatori per un obiettivo | al massimo tre |

### Prima dell'approvazione

1. Ogni obiettivo è collegato a un obiettivo del DUP.
2. Ogni indicatore ha formula, fonte, valore di partenza estratto e valore atteso deciso dal responsabile.
3. Il valore atteso è sostenibile con le risorse indicate.
4. Peso e scala sono quelli del sistema di valutazione dell'ente.
5. Nella scheda non restano nomi né [VERIFICARE].

## Rischi corruttivi: aggiornare mappature e riferimenti

### Le norme e la struttura

La sottosezione 2.3 sostituisce il vecchio piano anticorruzione. Per la L. 6 novembre 2012, n. 190, negli enti locali il responsabile della prevenzione della corruzione e della trasparenza (RPCT) è di norma il segretario comunale; l'organo di indirizzo fissa gli obiettivi strategici e adotta il piano su proposta del RPCT. La sottosezione indica anche i responsabili della trasmissione e della pubblicazione dei dati.[^6]

Le indicazioni di dettaglio sono dell'Autorità nazionale anticorruzione (ANAC). Il Piano nazionale anticorruzione (PNA) 2022 è stato integrato dall'Aggiornamento 2024, dedicato ai Comuni sotto i 5.000 abitanti e i cinquanta dipendenti.[^7] Le sue semplificazioni sono pensate per enti più piccoli di Borgo Esempio, che ha 6.500 abitanti, ma restano un riferimento utile. Secondo le notizie diffuse nel gennaio 2026, l'ANAC ha poi approvato in via definitiva il PNA 2025, per il triennio 2026-2028.[^8] Leggilo sul sito dell'Autorità prima di aggiornare la sottosezione: può cambiare le indicazioni precedenti.

Negli enti sotto i cinquanta dipendenti la mappatura non si rifà: si aggiorna. Riguarda i processi delle aree dell'art. 1, comma 16, della L. 190/2012 (autorizzazioni e concessioni, contratti, contributi, concorsi) e quelli che il RPCT e i responsabili ritengono più rilevanti per gli obiettivi di performance. Ogni scheda indica processo e fasi, eventi rischiosi, fattori abilitanti, esposizione al rischio, con un giudizio qualitativo e motivato,[^9] e misure con responsabile, tempi e indicatore.

### Abuso d'ufficio e indebita destinazione

L'art. 323 del codice penale, sull'abuso d'ufficio, è abrogato dal 25 agosto 2024 per effetto della L. 9 agosto 2024, n. 114; la Corte costituzionale ha ritenuto l'abrogazione non censurabile.[^10] Molte schede lo citano ancora.

Il reato non c'è più; l'evento sì. Per l'ANAC la corruzione da prevenire è più ampia dei reati: un criterio applicato in modo diverso tra due richiedenti resta un evento rischioso. Gli errori da evitare sono due, opposti: lasciare l'art. 323, o cancellare l'evento insieme al reato.

Il D.L. 4 luglio 2024, n. 92, ha introdotto l'art. 314-bis c.p., "Indebita destinazione di denaro o cose mobili". In sintesi, fuori dai casi di peculato, punisce il pubblico ufficiale o l'incaricato di pubblico servizio che destina denaro o cose mobili altrui, di cui ha la disponibilità per ragione dell'ufficio, a un uso diverso da quello previsto da specifiche norme di legge, o da atti con forza di legge, che non lasciano margini di discrezionalità. Serve che procuri intenzionalmente a sé o ad altri un ingiusto vantaggio patrimoniale, o ad altri un danno ingiusto.[^11] Interessa i processi in cui l'ufficio dispone di denaro o beni, come l'economato e i pagamenti. La L. 114/2024 ha anche riscritto il traffico di influenze illecite (art. 346-bis c.p.).

Descrivi gli eventi come comportamenti, senza etichette penali. Se la scheda cita reati, ogni articolo passa i tre controlli del capitolo sulla verifica delle norme. E l'obbligo di astenersi in caso di conflitto di interessi resta.[^12]

### Il prompt

```
Sei un istruttore che collabora con il RPCT di un Comune di [numero]
abitanti. Contesto: scheda di mappatura del processo [nome], dalla
sottosezione Rischi corruttivi e trasparenza del PIAO [anni]:
[testo della scheda]
Riferimenti verificati (solo questi) e cosa regolano: [elenco].
Compito: 1) elenca i riferimenti della scheda assenti dall'elenco;
2) per ogni evento rischioso proponi al massimo due misure concrete.
Vincoli: non eliminare eventi; non dare punteggi né livelli di rischio;
non affermare fatti accaduti o non accaduti; nessuna persona.
Norma fuori elenco o dato mancante: [VERIFICARE: cosa].
Formato: tabella con evento, misura, responsabile, tempi, indicatore.
```

Il giudizio sul rischio spetta al RPCT con i responsabili. Il divieto sui fatti ha un motivo preciso: l'assenza di fatti corruttivi nel triennio è una delle condizioni per confermare il piano, e il modello potrebbe affermarla senza saperlo.

### La bozza commentata

Il processo è quello dei contributi visto nel capitolo sulle delibere. La scheda 2026 citava l'abuso d'ufficio e aveva una sola misura: "controlli". La scheda dopo il primo giro di lavoro:

```
PIAO 2027-2029 – Sottosezione 2.3 Rischi corruttivi e trasparenza
Scheda 7 – Area: contributi e vantaggi economici (art. 1, comma 16,
lett. c), L. 190/2012). Servizio responsabile: Affari generali.
Processo: contributi ordinari e straordinari ad associazioni.
Eventi rischiosi:
E1 criteri del regolamento applicati in modo diverso tra richiedenti;
E2 stessa spesa finanziata da contributo ordinario e straordinario;
E3 liquidazione senza rendiconto, o con rendiconto non verificato;
E4 liquidazione di importo o a beneficiario diversi dalla concessione;
E5 mancata astensione di chi istruisce o decide, se in conflitto.
Fattori abilitanti: istruttoria e controllo del rendiconto svolti
dalla stessa persona; verifiche non documentate.
Esposizione al rischio: [VERIFICARE: giudizio motivato del RPCT con
il responsabile, sui dati del triennio].
Misure, dal 1 gennaio 2027, con indicatore:
M1 scheda istruttoria che motiva la valutazione con i criteri del
   regolamento (art. 12 L. 241/1990): schede / concessioni = 100%;
M2 verifica del cumulo prima della proposta: verifiche documentate /
   concessioni = 100%;
M3 rendiconto controllato da un addetto diverso dall'istruttore:
   rendiconti controllati da altro addetto / totali = 100%;
M4 confronto tra concessione e liquidazione prima della firma:
   confronti documentati / liquidazioni = 100%;
M5 dichiarazione sui conflitti di interessi di chi istruisce e decide
   (art. 6-bis L. 241/1990): dichiarazioni / pratiche = 100%.
Trasparenza: concessioni sopra i mille euro annui per beneficiario
pubblicate prima della liquidazione (artt. 26, comma 3, e 27
D.Lgs. 33/2013); responsabile: Responsabile del Servizio Affari
generali. Controllo semestrale a campione del RPCT.
Nota: tolto il riferimento all'art. 323 c.p., abrogato dalla
L. 114/2024. Gli eventi restano.
```

I punti critici.

*Eventi.* Restano quelli del 2026, senza l'art. 323. E4 riguarda il denaro, l'area a cui guarda il nuovo art. 314-bis. Ma se un fatto sia reato non lo stabilisce la scheda, che infatti non cita l'articolo: va bene così.

*Esposizione.* Il campo resta [VERIFICARE]. Lasciato libero, il modello può proporre punteggi di probabilità per impatto, secondo il metodo quantitativo del PNA 2013, che l'ANAC ha superato nel 2019.

*Misure.* Ogni misura ha un indicatore che si conta: "controlli" non lo era. M3 separa chi istruisce da chi controlla: negli uffici piccoli è una delle alternative alla rotazione indicate dall'ANAC.

### Errori tipici dell'IA nella sottosezione

- L'art. 323 c.p. ancora citato, o gli eventi cancellati insieme al reato.
- Il "PTPCT" come piano autonomo, da adottare a parte.
- Punteggi numerici di probabilità e impatto al posto del giudizio motivato.
- Misure generiche, come "formazione" o "controlli", senza indicatore.
- La rotazione ordinaria proposta per un ufficio con un solo addetto.

### Prima della proposta del RPCT

1. Ogni processo delle aree obbligatorie è mappato.
2. Nessun riferimento all'art. 323 c.p.; ogni reato citato è vigente e pertinente.
3. Il giudizio di esposizione è del RPCT con i responsabili, ed è motivato.
4. Ogni misura ha responsabile, tempi e indicatore.
5. Le affermazioni sui fatti del triennio vengono dagli atti dell'ente.

## La formazione nel PIAO

### Le norme

Gli obiettivi formativi sono contenuto del PIAO (art. 6, comma 2, lett. b), del D.L. 80/2021). Se il tuo ente adotta il piano semplificato, controlla sull'art. 6 del D.M. 132/2022 se la parte sulla formazione è dovuta: scriverla comunque documenta le misure sull'IA.

La direttiva del Ministro per la pubblica amministrazione del 14 gennaio 2025 chiede, dal 2025, almeno 40 ore di formazione l'anno per ogni dipendente, affida a chi dirige il compito di assicurare la partecipazione e lega la formazione alla performance.[^13] Nei Comuni senza dirigenti il compito spetta ai responsabili di servizio cui il sindaco ha attribuito le funzioni dirigenziali (art. 109, comma 2, del D.Lgs. 18 agosto 2000, n. 267, testo unico delle leggi sull'ordinamento degli enti locali, TUEL).

Sull'IA, l'art. 4 del Regolamento (UE) 2024/1689 (AI Act), riscritto dal Regolamento (UE) 2026/1744, chiede ai deployer, tra cui il Comune, misure per sostenere lo sviluppo dell'alfabetizzazione del personale: un obbligo di mezzi, non di risultato.[^14] L'art. 14, comma 3, della L. 23 settembre 2025, n. 132, chiede misure "tecniche, organizzative e formative" per un uso responsabile dell'IA, da attuare con le risorse disponibili (comma 4).[^15] Il decreto legislativo attuativo approvato in via definitiva dal Consiglio dei ministri il 4 agosto 2026 prevede, secondo le sintesi disponibili, percorsi per i dipendenti pubblici con la Scuola nazionale dell'amministrazione e Formez PA. Alla chiusura del volume le fonti consultate non ne riportano la pubblicazione: controllala, e leggi il testo definitivo.[^16]

Nessuna norma fissa le ore sull'IA. Le 40 ore sono un totale, a cui concorre anche la formazione obbligatoria, come quella su anticorruzione e sicurezza. Il bisogno c'è: nell'indagine IFEL, oltre il 55% di dirigenti e funzionari comunali non ha ricevuto formazione o ha seguito solo qualche webinar informativo.[^17] Contenuti ed esercitazioni sono nel capitolo sulla formazione del personale.

### Il prompt

```
Sei un istruttore degli Affari generali di un Comune di [numero]
abitanti, senza dirigenti. Contesto: [numero] dipendenti, di cui
[numero] istruttori che scrivono atti e [numero] responsabili;
strumento di IA autorizzato: [nome o "nessuno"]; regolamento interno
sull'IA: [stato]. Dati aggregati, senza nomi: [rilevazioni].
Norme (solo queste) e cosa regolano: [elenco verificato].
Compito: scrivi il paragrafo sulla formazione sull'IA della sezione
Organizzazione e capitale umano del PIAO [anni]: fabbisogno,
destinatari, contenuti, ore, modalità, tempi, indicatori.
Vincoli: ore comprese nelle 40 annue; nessun nome di corso, ente o
costo: scrivi [VERIFICARE: offerta disponibile]. Almeno un indicatore
di apprendimento. Dato mancante: [VERIFICARE: cosa]. Testo semplice.
```

### La bozza commentata

A Borgo Esempio scrivono atti 14 istruttori e 5 responsabili; il regolamento interno sull'IA è in preparazione. La bozza:

```
PIAO 2027-2029 – Sezione 3 – Formazione
Paragrafo: uso responsabile dell'intelligenza artificiale
Fabbisogno: [VERIFICARE: dipendenti che usano già l'IA, da una
rilevazione anonima, in forma aggregata]. Regolamento interno in
approvazione.
Riferimenti: art. 14, comma 3, L. 132/2025; art. 4 Reg. (UE) 2024/1689,
come modificato dal Reg. (UE) 2026/1744; direttiva ministeriale del
14 gennaio 2025.
Percorsi 2027, compresi nelle 40 ore annue pro capite:
A. Base, tutti i 38 dipendenti, 4 ore: che cosa fa e non fa un
   modello; regolamento interno; dati esclusi dal prompt; a chi
   segnalare errori e incidenti.
B. Atti, 14 istruttori e 5 responsabili, 12 ore in tre incontri su
   casi inventati: metodo del prompt, verifica delle norme,
   tracciabilità nel fascicolo.
C. Governo, segretario e responsabili di servizio, compreso il
   responsabile per la transizione al digitale, 6 ore: AI Act,
   L. 132/2025, acquisto degli strumenti, valutazione d'impatto.
Modalità: A con il percorso sull'IA di Syllabus [VERIFICARE: offerta
disponibile]; B e C interni o in forma associata [VERIFICARE: costo].
Tempi: A entro 31 marzo 2027; B e C entro 30 giugno 2027.
Indicatori:
- dipendenti che completano A / in servizio: 100% entro 31 marzo;
- partecipanti a B che superano la prova pratica finale /
  partecipanti: 90%;
- ore documentate da registro presenze o attestato: 100%.
Responsabile: segretario comunale, con i responsabili di servizio.
```

I punti critici.

*Fabbisogno.* La bozza non inventa quanti usano già l'IA: il dato viene da una rilevazione anonima, letta solo in forma aggregata. In un servizio di due persone il dato per servizio non è anonimo.

*Ore.* Per un istruttore A e B fanno 16 ore, due quinti del monte annuo; per un responsabile, con C, 22, più della metà. Valuta se distribuire B su due anni.

*Contenuti.* Si insegna ciò che l'ente permette: senza uno strumento autorizzato, solo casi inventati.

*Modalità.* Su Syllabus, la piattaforma del Dipartimento della funzione pubblica, c'è un percorso sull'IA su tre livelli.[^18] Il modello non conosce l'offerta aggiornata e può inventare titoli di corsi: il [VERIFICARE] resta finché non hai letto il catalogo.

*Indicatori.* Il secondo misura l'apprendimento, non la presenza. Registri e attestati documentano anche le misure dell'art. 4 dell'AI Act.

### Errori tipici dell'IA nella formazione

- L'art. 4 dell'AI Act nella versione anteriore al 2026, con il "livello sufficiente" da garantire.
- Un numero di ore sull'IA "obbligatorio per legge", che non esiste.
- Corsi, enti formatori e costi inventati.
- Le 40 ore presentate come aggiuntive, o come ore tutte sull'IA.

### Prima dell'approvazione

1. Destinatari e ore per ruolo sono coerenti con le 40 ore e con la formazione obbligatoria.
2. I contenuti seguono il regolamento interno.
3. Corsi e costi sono verificati sul catalogo; la spesa, se c'è, ha copertura.
4. C'è almeno un indicatore di apprendimento.

## L'adozione dell'IA tra gli obiettivi

### Perché un obiettivo

Secondo la ricerca FPA del 2026, nel 59% dei casi l'IA si usa senza regole interne, formazione specifica, strumenti sicuri o linee guida: è lasciata all'iniziativa individuale.[^19] Un obiettivo nel PIAO dice chi guida l'adozione, entro quando, con quali dati e chi decide. Le basi sono due: l'art. 6, comma 2, lett. e), del D.L. 80/2021, sulle procedure da semplificare anche con la tecnologia; l'art. 14 della L. 132/2025, che vuole l'IA usata per efficienza, tempi e qualità, con conoscibilità e tracciabilità, "in funzione strumentale e di supporto".[^20]

Per un Comune piccolo l'obiettivo giusto non è "introdurre l'IA". È provarla su pochi tipi di atto, con regole e misure, e decidere sui dati se estenderla, limitarla o sospenderla.

### Indicatori di efficienza e di controllo

*Efficienza.* Si misura, non si chiede. In uno studio di Microsoft i partecipanti stimavano di aver risparmiato in media 36 minuti; ne avevano risparmiati 12.[^21] Il dato utile è il tempo totale dell'atto, dall'istruttoria alla pubblicazione, raccolto con il registro del metodo del capitolo sul flusso di lavoro e confrontato con una misura senza IA fatta prima.

*Qualità.* Il controllo successivo di regolarità amministrativa, diretto dal segretario (art. 147-bis, comma 2, del TUEL), dà un dato già disponibile: i rilievi sugli atti estratti.[^22] Con pochi atti il confronto è un segnale, non una prova.

*Controllo.* Misura le cautele: uso dell'IA annotato nel fascicolo, riferimenti verificati a campione.

Non vanno misurati il numero di usi o di utenti, che premia l'uso per sé; i tempi dei singoli, che sono dati personali dei lavoratori;[^23] gli "zero incidenti", che premiano chi non segnala. In un ufficio di una o due persone anche il dato per ufficio descrive il lavoro di chi scrive: resta un dato personale, da trattare con le cautele del capitolo sul flusso di lavoro.

E l'IA non si usa per valutare le persone. Un sistema destinato a valutare prestazioni e comportamento dei lavoratori è ad alto rischio per l'AI Act (Allegato III, punto 4, lett. b)), con obblighi dal 2 dicembre 2027; una valutazione basata unicamente su un trattamento automatizzato incontra già oggi il limite dell'art. 22 del Regolamento (UE) 2016/679 (GDPR).[^24]

### Il prompt e la bozza

Il prompt è quello di riscrittura degli obiettivi. Al posto delle due righe Requisiti metti queste.

```
Indicatori: uno di efficienza, uno di qualità, uno di controllo; mai
sul numero di usi o di utenti. Dati per tipo di atto, mai per persona.
```

La bozza per Borgo Esempio:

```
PIAO 2027-2029 – Sottosezione 2.2 Performance – Obiettivo 2027/01
Obiettivo trasversale. Responsabile: segretario comunale.
Prova: Servizio Affari generali. Fasi 1 e 2: tutti i servizi.
Obiettivo DUP: [VERIFICARE: obiettivo di digitalizzazione del DUP]
Titolo: Provare l'IA generativa negli atti, con regole e misure
Fasi:
1. proposta di regolamento interno sull'IA: entro 28 febbraio 2027;
2. formazione A e B (sezione 3): entro 30 giugno 2027;
3. misura dei tempi senza IA sui due tipi di atto: marzo 2027;
4. prova su liquidazioni e contributi ad associazioni, con lo
   strumento autorizzato e il registro del metodo: dal 1 aprile al
   30 settembre 2027;
5. relazione alla Giunta con dati e proposta (estendere, limitare o
   sospendere): entro 15 novembre 2027.
Indicatori:
I1 Efficienza. Tempo medio totale per atto, dall'istruttoria alla
   pubblicazione, con l'IA / senza IA (fase 3). Fonte: registro del
   metodo, per tipo di atto. Atteso: minore di 1 [VERIFICARE: soglia
   proposta dal segretario].
I2 Qualità. Rilievi del controllo successivo sugli atti della prova /
   atti estratti. Fonte: verbali del controllo (art. 147-bis, comma 2,
   TUEL). Atteso: non superiore al dato 2026 degli stessi tipi di atto
   [VERIFICARE: dato da rilevare].
I3 Controllo. Atti della prova con l'uso dell'IA annotato nel
   fascicolo / atti della prova. Atteso: 100%.
Segnalazioni di errori e incidenti: procedura del regolamento interno.
Vincolo: i dati dei registri non servono a valutare i singoli.
Peso: [VERIFICARE: sistema di misurazione e valutazione].
```

I punti critici.

*Fase 5.* È il cuore dell'obiettivo: la Giunta decide sui dati. Un obiettivo che si chiude con "IA introdotta" ha già deciso l'esito.

*I1.* Il rapporto vale se la misura senza IA precede la prova e usa gli stessi tipi di atto e lo stesso metodo di rilevazione. Si calcola per tipo di atto, non per persona.

*I2.* Chiede di non peggiorare: dice se il tempo risparmiato è stato pagato con la qualità.

*Segnalazioni.* La bozza non le conta: un obiettivo di "zero incidenti" premia chi tace. Le gestisce la procedura del regolamento interno. Una violazione di dati personali segue invece la procedura dell'ente sui data breach, con il responsabile della protezione dei dati: il titolare la notifica al Garante entro 72 ore da quando ne è venuto a conoscenza, salvo che sia improbabile un rischio per le persone.[^25]

*Dati.* La prova usa solo lo strumento autorizzato dall'ente, con il contratto dell'art. 28 GDPR, e solo pratiche di associazioni. I segnaposto come RICHIEDENTE_1 pseudonimizzano, non anonimizzano. Dati sanitari, giudiziari e di minori restano fuori dal prompt anche qui: per questo i contributi a persone seguite dai Servizi sociali non entrano nella prova.

*Date.* La prova parte il 1° aprile, la formazione B finisce il 30 giugno: chi prova potrebbe non essere formato. È l'incoerenza che cerca il controllo della prossima sezione.

## Coerenza tra le sezioni e controlli finali

### Le sezioni si parlano

Il PIAO è integrato solo se le sezioni sono coerenti. La legge lo chiede anche per l'anticorruzione: i suoi obiettivi strategici sono contenuto necessario della programmazione, e la trasparenza si traduce in obiettivi organizzativi e individuali.[^26]

| Da | A | Cosa controllare |
|---|---|---|
| DUP | 2.2 Performance | ogni obiettivo ha un obiettivo del DUP |
| Bilancio | Sezione 3 | fabbisogni e formazione con copertura |
| 2.3 Rischi corruttivi | 2.2 Performance | misure principali anche come obiettivi |
| Sezione 3, formazione | obiettivo sull'IA | stessi percorsi, date compatibili |
| Regolamento interno | obiettivo sull'IA | stesse regole su dati e registri |

### Il prompt di controllo

Incolla le sezioni in una conversazione nuova, ciascuna con il suo titolo.

```
Testi: sezioni del PIAO [anni] e obiettivi del DUP, con i loro titoli.
[testi]
Fine dei testi. Non riscriverli. Rispondi con una tabella: punto,
sezione, frase, problema.
1. Obiettivi del PIAO senza obiettivo del DUP, e viceversa.
2. Misure anticorruzione senza responsabile, tempi o indicatore.
3. Formazione richiesta da un obiettivo e assente dalla sezione 3, o
il contrario; fasi che iniziano prima della formazione necessaria.
4. Date, importi, numero di dipendenti diversi tra le sezioni.
5. Art. 323 c.p., PTPCT come piano autonomo, "posizione organizzativa".
Non dire se le norme sono vigenti: lo verifico io.
```

Il punto 5 cerca riferimenti superati. Le posizioni organizzative, per esempio, sono diventate incarichi di elevata qualificazione con il contratto collettivo delle Funzioni locali del 16 novembre 2022.[^27]

A Borgo Esempio il punto 3 riguarda la prova sull'IA: si anticipa al 31 marzo il percorso B per chi vi partecipa, o si sposta la prova a luglio. La scelta la propone il segretario e la approva la Giunta con il Piano, non il modello.

### Dalla bozza alla Giunta

La proposta di deliberazione segue il capitolo sulle delibere: competenza della Giunta, pareri dell'art. 49 TUEL, compreso quello contabile se il Piano ha riflessi sul bilancio. La sottosezione 2.3 arriva su proposta del RPCT. Approvato, il Piano si pubblica sul sito istituzionale e si trasmette al Dipartimento della funzione pubblica per la pubblicazione sul suo portale.[^28]

### Prima della Giunta

1. Le sezioni dovute ci sono e sono coerenti con DUP e bilancio.
2. Gli indicatori hanno valori di partenza estratti e valori attesi decisi.
3. La sottosezione 2.3 è proposta dal RPCT, senza l'art. 323 c.p., con misure e indicatori.
4. La formazione sull'IA e l'obiettivo sull'IA hanno date compatibili; nessun indicatore è per persona.
5. Date, numeri e responsabili sono uguali in tutte le sezioni.
6. Non restano nomi, parentesi quadre o segnaposto; l'uso dell'IA è annotato nel fascicolo.

## In sintesi

- Sotto i cinquanta dipendenti si adotta il PIAO semplificato del D.M. 132/2022, ma gli obiettivi di performance servono comunque.
- L'IA propone la forma degli obiettivi; valori di partenza, valori attesi e pesi vengono dall'ente. Un indicatore senza fonte si toglie.
- Nella mappatura l'art. 323 c.p. si toglie, gli eventi restano; il giudizio sul rischio è del RPCT.
- La formazione sull'IA sta nelle 40 ore annue, si misura con una prova e si documenta.
- L'adozione dell'IA è un obiettivo da provare e decidere sui dati, con indicatori di efficienza, qualità e controllo, mai per persona.
- Nel prompt non entrano nomi, valutazioni individuali né fatti riferiti a persone; i dati raccolti sul lavoro non servono a valutare i singoli.
- Prima della Giunta, un controllo di coerenza tra le sezioni.

[^1]: D.L. 9 giugno 2021, n. 80, *Misure urgenti per il rafforzamento della capacità amministrativa delle pubbliche amministrazioni funzionale all'attuazione del Piano nazionale di ripresa e resilienza (PNRR) e per l'efficienza della giustizia*, convertito dalla L. 6 agosto 2021, n. 113, art. 6, commi 1, 2, 4, 6 e 7, normattiva.it. Il comma 7 richiama le sanzioni dell'art. 10, comma 5, del D.Lgs. 27 ottobre 2009, n. 150, e dell'art. 19, comma 5, lett. b), del D.L. 24 giugno 2014, n. 90, convertito dalla L. 11 agosto 2014, n. 114. Per l'art. 10, comma 5, in caso di mancata adozione del piano è vietato erogare la retribuzione di risultato ai dirigenti che vi hanno concorso, e l'amministrazione non può assumere personale né conferire incarichi di consulenza o di collaborazione.

[^2]: D.P.R. 24 giugno 2022, n. 81, *Regolamento recante individuazione degli adempimenti relativi ai Piani assorbiti dal Piano integrato di attività e organizzazione*, art. 1, normattiva.it.

[^3]: Ministro per la pubblica amministrazione, D.M. 30 giugno 2022, n. 132, *Regolamento recante definizione del contenuto del Piano integrato di attività e organizzazione*, artt. 2-6, gazzettaufficiale.it. La sezione 2 è disciplinata dall'art. 3, la sezione 3 dall'art. 4, il monitoraggio dall'art. 5, le modalità semplificate dall'art. 6.

[^4]: D.M. 30 giugno 2022, n. 132, cit., art. 6, sulle modalità semplificate; art. 7, comma 1, sul termine; art. 8, commi 1 e 2, sul raccordo con i documenti di programmazione finanziaria e sul differimento del termine; art. 11, sull'approvazione da parte della Giunta negli enti locali, gazzettaufficiale.it. Per la parte sui rischi corruttivi si veda anche la L. 6 novembre 2012, n. 190, art. 1, comma 8, per il quale negli enti locali il piano è approvato dalla Giunta, normattiva.it.

[^5]: D.Lgs. 27 ottobre 2009, n. 150, *Attuazione della legge 4 marzo 2009, n. 15, in materia di ottimizzazione della produttività del lavoro pubblico e di efficienza e trasparenza delle pubbliche amministrazioni*, art. 5, comma 2; art. 7; art. 16, comma 2, per il quale gli enti locali adeguano i propri ordinamenti ai principi degli artt. 3, 4, 5, comma 2, 7, 9 e 15, comma 1, normattiva.it. Sul raccordo con il piano esecutivo di gestione: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, artt. 108 e 169, normattiva.it.

[^6]: L. 6 novembre 2012, n. 190, *Disposizioni per la prevenzione e la repressione della corruzione e dell'illegalità nella pubblica amministrazione*, art. 1, commi 7, 8, 9 e 16, normattiva.it; D.Lgs. 14 marzo 2013, n. 33, *Riordino della disciplina riguardante il diritto di accesso civico e gli obblighi di pubblicità, trasparenza e diffusione di informazioni da parte delle pubbliche amministrazioni*, art. 10, comma 1, normattiva.it.

[^7]: ANAC, *Piano nazionale anticorruzione 2022*, approvato con delibera n. 7 del 17 gennaio 2023; ANAC, *Aggiornamento 2024 al Piano nazionale anticorruzione 2022*, approvato con delibera n. 31 del 30 gennaio 2025, anticorruzione.it. L'Aggiornamento 2024 si rivolge ai Comuni con popolazione inferiore a 5.000 abitanti e con meno di cinquanta dipendenti.

[^8]: ANAC, *Piano nazionale anticorruzione 2025*, riferito al triennio 2026-2028, anticorruzione.it. L'approvazione definitiva da parte del Consiglio dell'Autorità, il 28 gennaio 2026, è riportata, tra gli altri, da Italpress, 2026, italpress.com, e da Orizzonte Scuola, 2026, orizzontescuola.it. Estremi della delibera, testo e indicazioni per i Comuni piccoli vanno controllati sul sito dell'ANAC.

[^9]: ANAC, *Piano nazionale anticorruzione 2019*, approvato con delibera n. 1064 del 13 novembre 2019, Allegato 1, *Indicazioni metodologiche per la gestione dei rischi corruttivi*, che sostituisce il metodo quantitativo dell'Allegato 5 del PNA 2013 con una valutazione qualitativa e motivata, e Allegato 2, sulla rotazione ordinaria del personale e sulle misure alternative negli enti di piccole dimensioni, anticorruzione.it.

[^10]: L. 9 agosto 2024, n. 114, *Modifiche al codice penale, al codice di procedura penale, all'ordinamento giudiziario e al codice dell'ordinamento militare*, art. 1, che abroga l'art. 323 c.p. e riscrive l'art. 346-bis c.p., normattiva.it; Corte costituzionale, sentenza n. 95 del 2025, cortecostituzionale.it.

[^11]: D.L. 4 luglio 2024, n. 92, *Misure urgenti in materia penitenziaria, di giustizia civile e penale e di personale del Ministero della giustizia*, convertito dalla L. 8 agosto 2024, n. 112, art. 9, che inserisce l'art. 314-bis c.p., normattiva.it. Il testo riportato è una sintesi: prima di citare l'articolo in un atto, leggilo nella versione vigente.

[^12]: L. 7 agosto 1990, n. 241, *Nuove norme in materia di procedimento amministrativo e di diritto di accesso ai documenti amministrativi*, art. 6-bis; D.P.R. 16 aprile 2013, n. 62, *Regolamento recante codice di comportamento dei dipendenti pubblici*, artt. 6 e 7, normattiva.it.

[^13]: Ministro per la pubblica amministrazione, *Valorizzazione delle persone e produzione di valore pubblico attraverso la formazione. Principi, obiettivi e strumenti*, direttiva del 14 gennaio 2025, funzionepubblica.gov.it.

[^14]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024 (AI Act), art. 4, come modificato dal Regolamento (UE) 2026/1744 dell'8 luglio 2026, pubblicato nella Gazzetta ufficiale dell'Unione europea, serie L, del 24 luglio 2026, eur-lex.europa.eu. La nuova formulazione è riportata da fonti secondarie concordanti e va riscontrata sulla Gazzetta ufficiale; si veda il capitolo sull'AI Act.

[^15]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, commi 3 e 4, normattiva.it.

[^16]: L. 23 settembre 2025, n. 132, cit., art. 24; MySolution, *Adeguamento normativa nazionale IA: decreto approvato in CDM 4 agosto 2026*, 2026, mysolution.it. Gli schemi erano stati approvati in esame preliminare il 10 giugno 2026. Estremi, testo e data di entrata in vigore vanno controllati su Normattiva; si veda il capitolo sulla formazione del personale.

[^17]: Fondazione IFEL, *Intelligenza artificiale nei Comuni italiani. Competenze, governance, territori*, 2026, fondazioneifel.it. Indagine su 664 dirigenti e funzionari comunali, svolta nell'ambito del progetto AI-PACT.

[^18]: Corriere Comunicazioni, *Fastweb e Funzione Pubblica alleati per le competenze digitali nella PA*, 2025, corrierecomunicazioni.it. Contenuti e livelli del percorso vanno controllati sulla piattaforma Syllabus alla data del Piano.

[^19]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Campione di 500 dipendenti pubblici; dati dichiarati dagli intervistati.

[^20]: D.L. 9 giugno 2021, n. 80, cit., art. 6, comma 2, lett. e); L. 23 settembre 2025, n. 132, cit., art. 14, commi 1 e 2, normattiva.it.

[^21]: A. Cambon e altri, *Early LLM-based Tools for Enterprise Information Workers Likely Provide Meaningful Boosts to Productivity*, Microsoft, MSR-TR-2023-43, 2023, microsoft.com, per il Copilot Common Tasks Study. Nella sperimentazione dell'amministrazione britannica i partecipanti hanno dichiarato in media 26 minuti risparmiati al giorno, senza gruppo di confronto: Government Digital Service, *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, 2025, gov.uk. La valutazione del Department for Work and Pensions, con un gruppo di confronto di non utilizzatori, ha stimato 19 minuti: Civil Service World, 2025, civilserviceworld.com.

[^22]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 147-bis, comma 2, normattiva.it.

[^23]: Regolamento (UE) 2016/679, *Regolamento generale sulla protezione dei dati* (GDPR), art. 88, sui trattamenti nell'ambito dei rapporti di lavoro, eur-lex.europa.eu; L. 20 maggio 1970, n. 300, art. 4, come sostituito dall'art. 23 del D.Lgs. 14 settembre 2015, n. 151; D.Lgs. 30 giugno 2003, n. 196, art. 114, normattiva.it. Si vedano i capitoli sul flusso di lavoro e sul regolamento interno.

[^24]: Regolamento (UE) 2024/1689, cit., Allegato III, punto 4, lett. b), e art. 113, come modificato dal Regolamento (UE) 2026/1744, per il quale gli obblighi sui sistemi ad alto rischio dell'Allegato III si applicano dal 2 dicembre 2027; Regolamento (UE) 2016/679, cit., art. 22, eur-lex.europa.eu.

[^25]: Regolamento (UE) 2016/679, cit., art. 33, par. 1, eur-lex.europa.eu. Si veda il capitolo sul GDPR dedicato a fornitori, trasferimenti, DPIA e incidenti.

[^26]: L. 6 novembre 2012, n. 190, cit., art. 1, comma 8; D.Lgs. 14 marzo 2013, n. 33, cit., art. 10, comma 3, per il quale la promozione di maggiori livelli di trasparenza "deve tradursi nella definizione di obiettivi organizzativi e individuali", normattiva.it.

[^27]: Contratto collettivo nazionale di lavoro del personale del comparto Funzioni locali, triennio 2019-2021, sottoscritto il 16 novembre 2022, che disciplina gli incarichi di elevata qualificazione, aranagenzia.it.

[^28]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 49; D.L. 9 giugno 2021, n. 80, cit., art. 6, comma 4, normattiva.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 44 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Art. 6 D.L. 80/2021 presentato solo come obbligo sopra i 50 dipendenti, senza le modalità semplificate del comma 6 per gli enti più piccoli: aggiunte.
- Sanzioni per mancato PIAO: retribuzione di risultato negata 'a chi ha concorso', mentre l'art. 10, comma 5, D.Lgs. 150/2009 parla dei dirigenti; mancava il divieto di assumere.
- Aggiornamento del piano semplificato riferito alla sola 'mappatura' e a 'nuovi obiettivi'; il D.M. 132/2022 parla della sottosezione e di 'modifiche degli obiettivi di performance', con revisione a fine triennio.
- Classificazione degli indicatori presentata come regola ('sono di quattro tipi') e giorni di attesa del cittadino classificati come efficienza: corretti in efficacia, nella tabella e nella bozza CIE.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
