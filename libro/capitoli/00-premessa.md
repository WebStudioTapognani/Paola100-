# Premessa {.unnumbered}

In questa premessa: perché il libro e per chi, come è stato scritto, come leggerlo secondo il proprio ruolo, le convenzioni e la data di aggiornamento.

## Perché questo libro e per chi {.unnumbered}

Negli uffici pubblici l'intelligenza artificiale (IA) generativa si usa già. Secondo una ricerca FPA del giugno 2026, il 66% dei dipendenti pubblici intervistati la usa nel lavoro almeno una volta a settimana, e nel 59% dei casi senza regole interne, formazione specifica o strumenti sicuri.[^1] Fra i dirigenti e i funzionari comunali intervistati dalla Fondazione IFEL, il 41,9% la usa nelle attività quotidiane; oltre la metà non ha ricevuto formazione o ha seguito solo qualche webinar.[^2]

Intanto le regole sono arrivate. Per il Regolamento (UE) 2024/1689, noto come AI Act, il Comune che usa un sistema di IA, anche un chatbot generalista, è un deployer: deve sostenere l'alfabetizzazione del personale e, dal 2 agosto 2026, rispettare gli obblighi di trasparenza che lo riguardano.[^3] Per la L. 23 settembre 2025, n. 132, nella pubblica amministrazione l'uso dell'IA avviene "in funzione strumentale e di supporto all'attività provvedimentale", la persona "resta l'unica responsabile dei provvedimenti e dei procedimenti" e l'uso va reso conoscibile e tracciabile (art. 14).[^4] Per ogni dato personale scritto in un prompt vale il Regolamento (UE) 2016/679 (GDPR).

Gli errori hanno già un costo. Dal 2025 tribunali, giudici amministrativi e Corte di cassazione hanno rilevato, e spesso sanzionato, atti difensivi con precedenti inesistenti o non pertinenti, prodotti con l'IA e non verificati.[^5] Nel 2026 il TAR Marche ha ritenuto che l'uso dell'IA come supporto all'istruttoria di una gara non viola di per sé la riserva di umanità, se la decisione resta controllata, motivata e imputabile al funzionario e all'amministrazione.[^6]

Questo libro propone un metodo per scrivere atti con l'IA che rispetti le norme, protegga i dati e lasci traccia.

È scritto per chi prepara, firma o controlla gli atti in un Comune piccolo o medio: istruttori e funzionari, responsabili di servizio, segretari comunali. E per chi presidia dati e sistemi: il responsabile della protezione dei dati (DPO) e il responsabile per la transizione al digitale (RTD). Presuppone che il lettore conosca il proprio lavoro, non l'IA.

Non è un manuale di informatica né una guida a un prodotto: i nomi commerciali, come ChatGPT, Claude, Gemini, Copilot o NotebookLM, compaiono solo quando servono. Alla fine dovresti saper fare cinque cose:

- decidere che cosa chiedere all'IA e che cosa no;
- scrivere un prompt che dica al modello che cosa sa e che cosa non sa;
- controllare ogni riferimento di una bozza prima della firma;
- tenere fuori dal prompt i dati che non servono;
- documentare l'uso dell'IA nel fascicolo e nelle regole dell'ufficio.

## Scritto con l'IA, non da un'IA {.unnumbered}

La copertina lo dichiara: questo libro è scritto con l'intelligenza artificiale, con il metodo che insegna. Lo strumento è Claude, di Anthropic. Non è una raccomandazione: per scegliere in ufficio valgono i criteri del capitolo sull'acquisto di uno strumento di IA. Il lavoro è stato diviso come in una redazione.

- *Chi ha deciso.* L'autore ha scelto tema, lettori e vincoli: nessun atto, dato o nome dell'ente presso cui lavora, esempi solo inventati, uso dell'IA dichiarato. Il modello ha proposto l'indice in quattro parti; l'autore lo ha adottato e ha approvato regole di stile e convenzioni.
- *Chi ha scritto.* Ricerche e bozze di capitoli e allegati, compresa questa premessa, le ha scritte il modello, con un'istanza separata per ogni compito.
- *Chi ha corretto.* Revisioni in conversazioni separate hanno segnalato errori di fatto, di diritto e di lingua; le segnalazioni gravi sono state ricontrollate prima di correggere. Rilettura e ultima parola sono dell'autore.
- *Chi ha verificato.* Il modello ha controllato i fatti su fonti secondarie concordanti, perché i siti istituzionali non erano raggiungibili dall'ambiente di lavoro. Il riscontro sui testi ufficiali è dell'autore, ultimo passaggio prima della stampa.

La formula "con l'IA" ha una ragione di diritto. L'art. 25 della L. 132/2025 ha modificato la legge sul diritto d'autore: sono protette le opere "dell'ingegno umano", "anche laddove create con l'ausilio di strumenti di intelligenza artificiale, purché costituenti risultato del lavoro intellettuale dell'autore".[^7] Qui progetto, scelte e controlli sono dell'autore; il modello è lo strumento. È il principio che l'art. 14 fissa per gli atti: lo strumento propone, la persona decide e ne risponde. Degli errori di queste pagine risponde l'autore.

La dichiarazione in copertina non è imposta dall'AI Act, che esonera dall'obbligo i testi rivisti da una persona che ne ha la responsabilità editoriale (art. 50).[^8] È una scelta di metodo: il libro fa per sé ciò che chiede agli uffici, cioè rendere conoscibile l'uso dell'IA.

L'allegato su come è stato scritto questo libro racconta il processo intero, errori e limiti compresi. Un limite va detto subito: il capitolo sul metodo del prompt ha avuto otto revisioni separate, gli altri, di regola, un solo giro che riunisce i diversi controlli.

## Come leggerlo {.unnumbered}

Il libro ha quattro parti.

| Parte | Tema | Che cosa contiene |
|---|---|---|
| I | Il quadro | dati, AI Act, legge italiana, GDPR |
| II | Il metodo | strumenti, prompt, lingua, verifica |
| III | Atto per atto | istruttoria, atti, privacy, PIAO, PEC |
| IV | La governance | regole, tracciabilità, formazione, acquisti |

Ogni capitolo della Parte III parte da un problema concreto, di regola un caso di Borgo Esempio. Poi il prompt, la bozza commentata, gli errori tipici dell'IA e i controlli prima della firma. Gli allegati raccolgono gli strumenti di lavoro: prompt, modelli, checklist, norme, glossario, fonti.

Non serve leggerlo nell'ordine. Ecco tre percorsi.

*Istruttore o funzionario che scrive gli atti.* Comincia dal capitolo sull'IA già in ufficio, poi leggi la Parte II per intero: il capitolo sul metodo del prompt è il centro del libro. Prima di incollare qualunque testo, leggi anche il primo capitolo sul GDPR, sui dati nel prompt. Poi passa ai capitoli della Parte III sugli atti che scrivi, con a portata di mano prompt, file di stile e checklist.

*Responsabile di servizio e segretario comunale.* Chi firma o controlla parte dalla responsabilità: il capitolo sulla legge italiana sull'IA e quello sull'AI Act. Poi i capitoli sulla verifica e sul flusso di lavoro. Nella Parte III guarda prima i controlli che precedono la firma; il segretario anche delibere e verbali. La Parte IV serve a chi organizza l'ufficio, con i modelli di governance dell'allegato.

*DPO e RTD.* Leggi la Parte I per intero, con i due capitoli sul GDPR. Poi il capitolo su quale IA usare e con quali dati, quello sulla privacy prima della pubblicazione e quello su cittadini e PEC, per avvisi e chatbot. Nella Parte IV, soprattutto tracciabilità e acquisto dello strumento.

## Le convenzioni {.unnumbered}

*Borgo Esempio.* Gli esempi sono ambientati nel Comune di Borgo Esempio, che non esiste: circa 6.500 abitanti, un segretario comunale, nessun dirigente. I servizi Affari generali, Finanziario, Tecnico, Demografici e Sociali sono guidati da responsabili con incarico di elevata qualificazione, cui il sindaco attribuisce le funzioni dirigenziali ai sensi dell'art. 109, comma 2, del D.Lgs. 18 agosto 2000, n. 267 (TUEL).[^9] Anche fornitori e associazioni sono inventati: Editrice Esempio S.r.l., ASD Borgo Esempio. Nessun esempio viene da atti veri o dall'ente presso cui l'autore lavora. Le opinioni sono personali e non impegnano alcuna amministrazione.

*I prompt.* Stanno nei riquadri grigi, in non più di dodici righe; l'allegato con i cento prompt li raccoglie per attività. Ecco due righe del prompt modello.

```
Dati: [importi, date, codici richiesti; persone fisiche come RICHIEDENTE_1].
Se un dato manca o è incoerente, scrivi [VERIFICARE: cosa] e prosegui.
```

Tre segni li rendono leggibili.

- Le parti tra parentesi quadre, come [oggetto] o [importo], le sostituisci tu prima di inviare il prompt.
- [VERIFICARE: cosa] non si sostituisce: è il segnale che il modello lascia nella bozza quando un dato manca o una norma va cercata, e dopo i due punti dice che cosa controllare. Una bozza con un [VERIFICARE] aperto non è pronta per la firma.
- I segnaposto in maiuscolo e senza parentesi, come RICHIEDENTE_1, ATTO_1 o RUP_1, stanno al posto delle persone e degli atti che vi riportano. Restano così nel prompt e nella bozza; i dati veri li rimetti tu, fuori dallo strumento. Il segnaposto riduce il rischio, non lo toglie: il primo capitolo sul GDPR spiega perché.

*Il semaforo.* Ogni prompt dell'allegato ha un colore, che dice quale strumento puoi usare. Verde: nessun dato personale né riservato. Giallo: dati comuni sostituiti da segnaposto, o informazioni riservate. Rosso: testi che possono contenere i dati più delicati, da trattare solo nei controlli decisi dall'ente. La regola è nel capitolo su quale IA usare in ufficio.

*Norme e note.* Ogni norma è citata per esteso la prima volta, poi in forma abbreviata. Le note indicano il sito ufficiale e, spesso, la fonte secondaria del riscontro.

*Dietro le quinte.* Chiude ogni capitolo: quali istruzioni ha ricevuto il modello, che cosa ha sbagliato, che cosa è stato corretto. È la tracciabilità che il libro chiede per gli atti, applicata al libro.

## Aggiornato al 6 ottobre 2026 {.unnumbered}

Norme, giurisprudenza, dati e strumenti sono aggiornati al 6 ottobre 2026. A quella data, secondo le fonti consultate:[^10]

- l'AI Act si applica nel testo modificato dal Regolamento (UE) 2026/1744, in vigore dal 27 luglio 2026;
- della L. 132/2025 è in vigore il D.Lgs. 9 settembre 2026, n. 160, mentre il decreto su autorità nazionali e formazione, approvato il 4 agosto 2026, non risulta pubblicato;
- le Linee guida dell'Agenzia per l'Italia digitale (AgID) sull'IA nella pubblica amministrazione sono ancora in bozza;
- le modifiche al GDPR proposte dalla Commissione europea nel novembre 2025 non risultano adottate.

Alcune date sono già fissate: dal 2 dicembre 2026 nuovi divieti dell'AI Act; dal 2 dicembre 2027 gli obblighi sui sistemi ad alto rischio dell'Allegato III, tra cui quelli usati per le prestazioni di assistenza pubblica; dal 2 agosto 2028 quelli sui sistemi integrati in prodotti regolati. Altro cambierà senza preavviso: soglie dei contratti pubblici, orientamenti dei giudici, nomi e condizioni d'uso degli strumenti. NotebookLM, per esempio, dal 16 luglio 2026 si chiama Gemini Notebook.

Dove controllare:

- le norme italiane su Normattiva, nel testo vigente alla data dell'atto; fa fede la Gazzetta Ufficiale;[^11]
- le norme europee su EUR-Lex, nella versione consolidata, guardando la data del consolidamento;
- le Linee guida sul sito dell'AgID, i provvedimenti sui dati personali sui siti del Garante e del Comitato europeo per la protezione dei dati (EDPB);
- gli strumenti nelle pagine di assistenza dei produttori, il giorno in cui li usi.

Il calendario completo è nell'allegato sulle norme essenziali; il modo di controllare un riferimento, nel capitolo sulla verifica.

Una norma citata in questo libro è il punto di partenza di una verifica, non il suo esito. Vale per il libro ciò che il libro dice delle bozze dell'IA. Il metodo, invece, dipende poco dalle date: dire al modello che cosa sa, fargli segnalare ciò che non sa, verificare, lasciare traccia.

[^1]: Ricerca FPA *La Pubblica Amministrazione infrastruttura strategica del Paese*, su un campione di 500 dipendenti pubblici, presentata all'apertura di FORUM PA 2026 il 9 giugno 2026, come riportata da ANSA, *Forum PA: il 66% dei dipendenti pubblici usa strumenti di IA nelle attività lavorative*, 2026, ansa.it. Il 66% comprende chi usa l'IA ogni giorno o almeno una volta a settimana. Sono dati dichiarati dagli intervistati.

[^2]: Fondazione IFEL, *Intelligenza artificiale nei Comuni italiani. Competenze, governance, territori*, 2026, fondazioneifel.it. Indagine su 664 dirigenti e funzionari comunali, svolta nell'ambito del progetto AI-PACT. Le indagini FPA e IFEL hanno popolazioni e domande diverse: non si sommano né si confrontano.

[^3]: Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale, artt. 3, n. 4, 4 e 50, eur-lex.europa.eu. L'art. 4 sull'alfabetizzazione è stato riscritto dal Regolamento (UE) 2026/1744 del Parlamento europeo e del Consiglio, dell'8 luglio 2026, in vigore dal 27 luglio 2026, che non ha rinviato gli obblighi dei deployer dell'art. 50. Ne tratta il capitolo sull'AI Act.

[^4]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, in Gazzetta Ufficiale, Serie generale, n. 223 del 25 settembre 2025, in vigore dal 10 ottobre 2025, art. 14, commi 1, 2 e 3, normattiva.it. Il comma 3 chiede alle amministrazioni misure tecniche, organizzative e formative per un uso responsabile dell'IA.

[^5]: Tra gli altri: Trib. Firenze, sez. specializzata in materia di impresa, ordinanza 14 marzo 2025, che ha riconosciuto il disvalore dell'omessa verifica ma ha escluso la condanna per responsabilità aggravata; TAR Lombardia, Milano, sez. V, sentenza 21 ottobre 2025, n. 3348; Trib. Siracusa, sez. II civile, sentenza 20 febbraio 2026, n. 338; Cass. pen., sez. III, sentenza 11 giugno 2026, n. 23006, depositata il 22 giugno 2026. Commenti in Diritto.it, *Intelligenza artificiale negli atti difensivi: il Tribunale di Firenze sulle allucinazioni AI*, 2025, diritto.it; Il Sole 24 Ore NT+ Diritto, *Quattro sentenze fantasma e conto da 30.000 euro*, 2026, ilsole24ore.com; Ecnews, *Citazioni generate dall'AI e non controllate: la colpa è più grave e la sanzione sale*, 2026, ecnews.it. Le pronunce sono discusse nel capitolo su cosa fa un modello linguistico.

[^6]: TAR Marche, sez. I, sentenza 1° giugno 2026, n. 758, giustizia-amministrativa.it; commento in LavoriPubblici.it, *Intelligenza artificiale negli appalti pubblici: quando l'IA non rende illegittima la decisione amministrativa*, 2026, lavoripubblici.it. La riserva di umanità è nell'art. 30 del D.Lgs. 31 marzo 2023, n. 36, normattiva.it.

[^7]: L. 23 settembre 2025, n. 132, cit., art. 25, che modifica l'art. 1 della L. 22 aprile 1941, n. 633, *Protezione del diritto d'autore e di altri diritti connessi al suo esercizio*, normattiva.it. La legge non fissa una soglia: quanto contributo umano basti si valuta caso per caso. Il tema è trattato nel capitolo sulla legge italiana sull'IA.

[^8]: Regolamento (UE) 2024/1689, cit., art. 50, par. 4, secondo comma, eur-lex.europa.eu. L'obbligo grava sul deployer e non si applica se il contenuto è stato sottoposto a revisione umana o a controllo editoriale e una persona fisica o giuridica ne detiene la responsabilità editoriale. La disposizione si applica dal 2 agosto 2026 e non è stata modificata dal Regolamento (UE) 2026/1744.

[^9]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, artt. 107 e 109, comma 2, normattiva.it. L'incarico di elevata qualificazione ha preso il posto della posizione organizzativa con il contratto collettivo nazionale di lavoro del comparto Funzioni locali per il triennio 2019-2021.

[^10]: Regolamento (UE) 2026/1744, cit., che modifica tra l'altro l'art. 113 del Regolamento (UE) 2024/1689, in Gazzetta ufficiale dell'Unione europea, serie L, del 24 luglio 2026, eur-lex.europa.eu; D.Lgs. 9 settembre 2026, n. 160, in Gazzetta Ufficiale n. 214 del 15 settembre 2026, in vigore dal 30 settembre 2026, normattiva.it; AgID, Determinazione n. 17/2025, sulla bozza di Linee guida per l'adozione di IA nella pubblica amministrazione, e Determinazione n. 43 del 10 marzo 2026, sulle bozze di Linee guida per lo sviluppo e per il procurement di IA nella pubblica amministrazione, agid.gov.it; Commissione europea, proposta di regolamento COM(2025) 837 del 19 novembre 2025 (Digital Omnibus), eur-lex.europa.eu. Lo stato di ciascun atto va ricontrollato alla data della lettura.

[^11]: Normattiva, *Avviso legale* e *Guida all'uso*, normattiva.it. I testi di Normattiva non hanno carattere di ufficialità: fa fede la Gazzetta Ufficiale, consultabile gratuitamente nel formato autentico, gazzettaufficiale.it. Normattiva consente di leggere ogni atto nel testo originario, nel testo vigente e nel testo vigente a una data passata.
