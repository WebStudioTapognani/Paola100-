# Verbali, decreti e ordinanze

In questo capitolo: il verbale della seduta dalla registrazione alla firma del segretario, il decreto sindacale di nomina, le ordinanze ordinarie e quelle contingibili e urgenti, con sanzioni, termini e ricorsi.

## Il problema: tre atti, tre rischi diversi

In questi tre atti l'IA sbaglia in modi diversi. Il verbale attesta fatti, e un modello non può attestare chi era presente o come si è votato. Il decreto riguarda una persona e una competenza precisa: il modello confonde organi e formule e, se glielo permetti, valuta le persone al posto del sindaco. L'ordinanza limita diritti: il modello tende a dichiararla "contingibile e urgente" per abitudine e a inventare sanzioni.

Lo schema del prompt è quello del capitolo sul metodo del prompt. Da un atto all'altro cambia il colore del semaforo (si veda il capitolo sugli strumenti).

| Atto | Colore | Perché |
|---|---|---|
| Verbale di seduta pubblica | giallo | voci e nomi dei presenti |
| Parte in seduta segreta | rosso | riservatezza della seduta |
| Decreto di nomina | giallo | riguarda un dipendente |
| Ordinanza a un proprietario | giallo | destinatario persona fisica |
| Ordinanza sugli orari | verde | nessuna persona |

## Il verbale della seduta

### Le norme

Il segretario comunale "partecipa con funzioni consultive, referenti e di assistenza alle riunioni del consiglio e della giunta e ne cura la verbalizzazione" (art. 97, comma 4, lett. a), del D.Lgs. 18 agosto 2000, n. 267, TUEL). Le sedute del Consiglio sono pubbliche, salvi i casi previsti dal regolamento; nei Comuni fino a 15.000 abitanti le presiede il sindaco, salvo diversa previsione dello statuto.[^1] Il regolamento del Consiglio decide il resto, dal verbale sommario o integrale alla seduta segreta: il modello non lo conosce.

### Che cosa attesta il verbale

Il verbale è un atto pubblico. Fa piena prova, fino a querela di falso, dei fatti che il segretario attesta avvenuti in sua presenza: presenze, voti, dichiarazioni ricevute (art. 2700 c.c.). Non copre le sue valutazioni, come la sintesi di un intervento.[^2]

La sintesi della discussione è scrittura: il modello ne prepara la bozza, il segretario la fa propria. Presenze, voti e dichiarazioni sono attestazioni: vengono solo da ciò che il segretario ha visto. L'IA resta "strumentale e di supporto", e la persona "l'unica responsabile" (art. 14, comma 2, della L. 23 settembre 2025, n. 132).[^3] Il regolamento può prevedere che il Consiglio approvi il verbale nella seduta successiva, con le rettifiche richieste. Poi, ciò che il verbale attesta si contesta solo con la querela di falso: l'errore va trovato prima, con una revisione vera.[^4]

### Dalla registrazione al testo

Registrare e trasmettere le sedute è ammesso se il regolamento lo disciplina e i presenti ne sono informati; le informazioni sulla salute non si diffondono.[^5] La trascrizione automatica usa di regola un sistema di IA, di cui il Comune è deployer (si veda il capitolo sull'AI Act). Lo strumento lo sceglie l'ente, con il responsabile della protezione dei dati: in una seduta pubblica possono emergere dati che nessuno aveva previsto. Tre cautele:

- *lo strumento*: voci e nomi fanno della registrazione un uso giallo, solo nello strumento dell'ente, con il contratto dell'art. 28 GDPR e l'addestramento escluso. Le parti in seduta segreta sono rosse: restano fuori da registrazione, trascrizione e prompt;
- *chi parla*: separare gli interventi ("voce 1", "voce 2") va bene; riconoscere la persona confrontando la voce con un'impronta registrata è un trattamento di dati biometrici (art. 4, n. 14, e art. 9 GDPR).[^6] Se lo strumento la offre, la funzione resta spenta: i nomi li attribuisce il segretario;
- *la qualità*: la trascrizione sbaglia proprio dove il verbale non può sbagliare (nomi, numeri, articoli di legge, voci sovrapposte, un "non" perso). Il controllo si fa sull'audio, al minuto indicato dal modello.

### La scheda del segretario

I fatti da attestare non passano dal modello: il segretario li annota su una scheda, o li prende dal sistema di voto.

```
SCHEDA DEL SEGRETARIO – Consiglio comunale del [data], punto [n]
Presenti alla trattazione: [ruoli e segnaposto]; assenti: [segnaposto]
Entrate e uscite durante il punto: [chi, a che ora]
Emendamenti: [n], presentati da [segnaposto], testo in allegato
Votazioni: [oggetto] – favorevoli [n]; contrari [n, chi]; astenuti [n, chi]
Dichiarazioni a verbale consegnate per iscritto: [chi]
Parti in seduta segreta: [da ora a ora]
```

La scheda entra nel prompt come "Dati certi"; la trascrizione, un punto alla volta, dopo una rilettura. Nella rilettura:

- i nomi diventano ruoli e segnaposto (SINDACO, ASSESSORE_1, CONSIGLIERE_1); la legenda resta al segretario;
- i passaggi su salute, reati o minori si tolgono e si sostituiscono con una nota tra parentesi tonde, come "(passaggio omesso, min. 19-20)": sono rossi, e nel prompt non entrano neppure con lo strumento dell'ente;
- i riferimenti a persone estranee alla seduta si riducono a ciò che serve al resoconto.

Pseudonimizzare non è anonimizzare. Anche con i segnaposto la trascrizione resta un dato personale: in un paese di 6.500 abitanti un ruolo, un'opinione e una data bastano a riconoscere chi parla. Per questo passa solo dallo strumento autorizzato.

### Il prompt

```
Sei l'assistente del segretario comunale di un Comune di 6.500 abitanti.
Trascrizione automatica del punto [n] del Consiglio del [data]: [testo].
Dati certi, dalla scheda del segretario: [presenze, votazioni, orari].
Compito: resoconto sommario del punto, in forma indiretta, al presente,
nell'ordine degli interventi; 40-100 parole ciascuno; niente giudizi.
Fatti: presenze e voti solo dai Dati certi; mai dedurli dal testo.
Norme citate da chi parla: riportale come dette; [VERIFICARE: minuto].
Passaggi incomprensibili, nomi e numeri dubbi: [VERIFICARE: minuto].
Dichiarazioni "a verbale": non riassumerle; [VERIFICARE: testo].
Passaggi omessi: non ricostruirli; segnalali con il minuto.
Dopo il resoconto, elenca i [VERIFICARE] e le parti omesse, con il minuto.
```

La riga Fatti impedisce al modello di trasformare un "approvato" della trascrizione in un esito di voto. La riga sulle norme gli impedisce di "correggere" chi parla: il verbale riporta ciò che è stato detto. La riga sui passaggi omessi gli impedisce di riempire il vuoto con una frase plausibile. Se un dato rosso è sfuggito alla rilettura, il prompt non lo ripara: cancella la conversazione e segui le regole dell'ente, che di solito chiedono di avvisare il responsabile della protezione dei dati (si veda il capitolo sul metodo del prompt).

### La bozza commentata

È il punto 3 della seduta, come esce dal prompt, prima della revisione del segretario. Fatti e numeri sono inventati.

```
COMUNE DI BORGO ESEMPIO – CONSIGLIO COMUNALE
Seduta pubblica del 29 settembre 2026, prima convocazione
Punto 3 dell'ordine del giorno: Approvazione del regolamento per l'uso
delle sale comunali.

Presenti alla trattazione: SINDACO e 10 consiglieri. Assenti:
CONSIGLIERE_4, CONSIGLIERE_9. Presiede il Sindaco. Assiste il segretario
comunale, che cura la verbalizzazione (art. 97, comma 4, lett. a), del
D.Lgs. 18 agosto 2000, n. 267, TUEL).

ASSESSORE_2 illustra la proposta. Il regolamento prevede una tariffa
oraria per i privati e l'uso gratuito delle sale per le associazioni
iscritte all'albo comunale fino a [VERIFICARE: min. 14, "dieci" o
"dodici"] giornate l'anno.
CONSIGLIERE_3 dichiara che la minoranza condivide l'impianto del
regolamento, ma ritiene troppo bassa la soglia di gratuità.
Presenta un emendamento all'art. 6, che la porta a venti giornate.
[VERIFICARE: min. 19-20, passaggio omesso nella trascrizione; si veda
l'elenco finale]
ASSESSORE_2 risponde che la soglia tiene conto dei costi di gestione
e richiama "l'articolo 42" [VERIFICARE: min. 23, norma come detta].
CONSIGLIERE_5 chiede di riportare a verbale la propria dichiarazione.
[VERIFICARE: testo integrale consegnato per iscritto da CONSIGLIERE_5]

Votazione dell'emendamento all'art. 6, in forma palese: favorevoli 3;
contrari 8; astenuti nessuno. L'emendamento è respinto.
Votazione della proposta, in forma palese: favorevoli 8; contrari 2
(CONSIGLIERE_3, CONSIGLIERE_5); astenuti 1 (CONSIGLIERE_7).
La proposta è approvata.
Votazione dell'immediata eseguibilità (art. 134, comma 4, TUEL):
favorevoli 8 su 13 componenti; contrari 2; astenuti 1.
La deliberazione è dichiarata immediatamente eseguibile.

Il Presidente                          Il Segretario comunale
(firmato digitalmente)                 (firmato digitalmente)
```

*Presenze e voti.* Vengono dalla scheda. Se gli astenuti si computano tra i votanti lo dice il regolamento. Per l'immediata eseguibilità serve la maggioranza dei componenti, non dei presenti: 8 voti su 13, sindaco compreso.[^7]

*Sintesi.* Forma indiretta, nessun aggettivo: "ampio dibattito" è una valutazione che il segretario non ha fatto.

*Il passaggio omesso.* Al minuto 19 CONSIGLIERE_3 aveva parlato della salute del figlio di una famiglia del paese. Il segretario l'ha tolto dalla trascrizione prima del prompt; il modello l'ha segnalato senza ricostruirlo. Il verbale va all'albo, e i dati sulla salute non si diffondono: se e come ricordare l'intervento lo decide il segretario, senza nulla che renda riconoscibile la famiglia (si veda il capitolo sulla privacy prima della pubblicazione).

*La norma e la dichiarazione.* "42" o "142": lo stabilisce l'ascolto al minuto 23. La dichiarazione a verbale si riporta per intero, dal testo consegnato.

Lo stesso metodo vale per i verbali di Giunta e delle commissioni.

### Gli errori tipici dell'IA nei verbali

| Errore | Esempio | Come intercettarlo |
|---|---|---|
| Voti dedotti | "approvata all'unanimità" | scheda del segretario |
| Interventi scambiati | frase della minoranza al sindaco | ascolto al minuto |
| Senso rovesciato | "condivido" per "non condivido" | ascolto al minuto |
| Norme "corrette" | art. 142 al posto di art. 42 | riga sulle norme citate |
| Dichiarazioni riassunte | sintesi di un testo consegnato | testo integrale |
| Dati di terzi | malattia di un cittadino | rilettura prima del prompt |
| Maggioranze sbagliate | "a maggioranza dei presenti" | art. 134, c. 4, TUEL |

### Prima della firma

1. presenze, entrate, uscite e voti vengono dalla scheda o dal sistema di voto;
2. ogni [VERIFICARE] è chiuso ascoltando la registrazione al minuto indicato;
3. dichiarazioni a verbale per intero, interventi attribuiti alla persona giusta;
4. nel testo per l'albo nulla rende riconoscibili le persone di cui si è parlato per salute, reati o minori;
5. la parte in seduta segreta non è passata da nessuno strumento di IA, e i passaggi rossi sono stati tolti prima del prompt;
6. segnaposto sostituiti; strumento e prompt annotati nel fascicolo (si veda il capitolo sulla tracciabilità).

## Il decreto sindacale di nomina

### Le norme

Il sindaco nomina i responsabili degli uffici e dei servizi (art. 50, comma 10, del TUEL). Nei Comuni senza dirigenti attribuisce loro, con provvedimento motivato, le funzioni dell'art. 107, commi 2 e 3 (art. 109, comma 2), secondo i criteri del regolamento sull'ordinamento degli uffici e dei servizi, adottato dalla Giunta (art. 48, comma 3).[^8] Si aggiungono tre fonti:

- i contratti collettivi del comparto Funzioni locali: quello del 16 novembre 2022 ha trasformato le posizioni organizzative in incarichi di elevata qualificazione; quello del 23 febbraio 2026, secondo le sintesi pubblicate, ha alzato il tetto della retribuzione di posizione da 18.000 a 22.000 euro;[^9]
- il D.Lgs. 8 aprile 2013, n. 39: la dichiarazione sull'assenza di cause di inconferibilità è condizione di efficacia anche quando le funzioni dirigenziali vanno a chi non è dirigente (artt. 2, comma 2, e 20);[^10]
- la L. 23 dicembre 2000, n. 388, che consente di affidare la responsabilità di un servizio a un assessore solo nei Comuni sotto i 5.000 abitanti (art. 53, comma 23): non a Borgo Esempio, che ne ha 6.500.[^11]

### La persona e la scelta

Il decreto riguarda un dipendente: uso giallo, con DIPENDENTE_1 al posto del nome. Curriculum, fascicolo e valutazioni restano fuori dal prompt; entrano le ragioni della scelta, già decise dal sindaco.

Non chiedere al modello di confrontare i candidati. Sarebbe un uso per decisioni sul rapporto di lavoro, che l'AI Act classifica ad alto rischio (Allegato III, punto 4), con obblighi dal 2 dicembre 2027. E chi destina a questa finalità un chatbot generalista rischia di diventarne fornitore (art. 25; si veda il capitolo sull'AI Act). Già oggi, poi, il GDPR vieta di regola le decisioni basate unicamente su un trattamento automatizzato che incidono in modo significativo sulla persona (art. 22), e la L. 132/2025 lascia la decisione a chi firma.[^12] Il modello scrive la motivazione; non la decide.

### La struttura

Numero e data del registro dei decreti; oggetto; "Visto"; "Considerato"; "DECRETA"; comunicazioni e pubblicazione; firma. Il modello tende ad aggiungere i pareri dell'art. 49 del TUEL, propri delle deliberazioni, e il ricorso al TAR. Ma l'incarico a un dipendente è un atto di gestione del rapporto di lavoro, adottato con i poteri del privato datore di lavoro (art. 5, comma 2, del D.Lgs. 30 marzo 2001, n. 165): le controversie vanno al giudice ordinario, in funzione di giudice del lavoro (art. 63, comma 1).[^13]

### Il prompt

```
Sei un istruttore del Servizio Affari generali di un Comune di 6.500
abitanti senza dirigenti.
Contesto: il Sindaco conferisce a DIPENDENTE_1 l'incarico di elevata
qualificazione del Servizio [servizio] dal [data] al [data].
Dati: atti dell'ente con n. e data [regolamento, graduazione, avviso];
retribuzione di posizione [importo]; ragioni della scelta: [testo].
Norme (solo queste) e cosa regolano: [elenco]. Fuori elenco: non citarle.
Compito: bozza del decreto; Visti, Considerato, DECRETA; 450 parole.
Fatti: non valutare la persona; usa le ragioni date, senza aggettivi.
Dichiarazioni e comunicazioni: da acquisire, non già avvenute.
Niente pareri dell'art. 49 TUEL né indicazione del ricorso al TAR.
Se un dato manca: [VERIFICARE: cosa]. Poi elenca i [VERIFICARE].
```

Nella riga Norme vanno le fonti appena viste; la riga Fatti vieta i giudizi.

### La bozza commentata

Numeri e date degli atti sono inventati.

```
COMUNE DI BORGO ESEMPIO
Decreto del Sindaco n. [numero] del [data]
OGGETTO: Conferimento dell'incarico di elevata qualificazione di
responsabile del Servizio Finanziario e attribuzione delle funzioni
dell'art. 107, commi 2 e 3, del TUEL.

IL SINDACO
Visti:
- gli artt. 50, comma 10, 107, commi 2 e 3, e 109, comma 2, del D.Lgs.
  18 agosto 2000, n. 267 (TUEL);
- i contratti collettivi del comparto Funzioni locali del 16 novembre
  2022 e del 23 febbraio 2026, sugli incarichi di elevata qualificazione;
- gli artt. 2, comma 2, e 20 del D.Lgs. 8 aprile 2013, n. 39;
- il regolamento sull'ordinamento degli uffici e dei servizi e la
  graduazione delle posizioni (deliberazioni della Giunta n. 87 del
  14 ottobre 2025 e n. 102 del 9 settembre 2026);
Considerato che:
- all'avviso interno del 15 settembre 2026 ha risposto DIPENDENTE_1,
  inquadrato nell'area dei funzionari e dell'elevata qualificazione;
- DIPENDENTE_1 possiede i requisiti dell'art. [VERIFICARE: articolo del
  regolamento e requisiti] e cura dal 2021 la predisposizione del
  bilancio e del rendiconto dell'ente;
- questa esperienza è coerente con gli obiettivi assegnati al Servizio
  [VERIFICARE: obiettivi del DUP 2027-2029 per il Servizio Finanziario];
DECRETA
1. di conferire a DIPENDENTE_1 l'incarico di elevata qualificazione di
   responsabile del Servizio Finanziario dal 1° novembre 2026 al
   31 dicembre 2028 [VERIFICARE: durata massima prevista dal contratto
   collettivo e dal regolamento];
2. di attribuire a DIPENDENTE_1, per il Servizio Finanziario, le
   funzioni dell'art. 107, commi 2 e 3, del TUEL;
3. di riconoscere la retribuzione di posizione di euro 14.000,00 annui
   lordi per tredici mensilità, secondo la graduazione approvata, e la
   retribuzione di risultato prevista dal sistema di valutazione;
4. di dare atto che l'incarico acquista efficacia con la dichiarazione
   sull'insussistenza di cause di inconferibilità (art. 20 del D.Lgs.
   39/2013), da acquisire prima del 1° novembre 2026;
5. di comunicare il decreto a DIPENDENTE_1, al segretario comunale e
   all'ufficio personale, e di pubblicarlo all'albo online e in
   Amministrazione trasparente [VERIFICARE: dati da pubblicare].
IL SINDACO (firmato digitalmente)
```

*Competenza.* Senza l'art. 109, comma 2, l'art. 107 attribuirebbe le funzioni a dirigenti che Borgo Esempio non ha.

*Contratti.* "Posizione organizzativa" e "categoria D" sono formule superate, che il modello ripete se l'esempio è un atto vecchio. Gli articoli dei due contratti si citano solo dopo averli letti nel testo firmato.

*Motivazione.* Solo le ragioni del sindaco: "spiccate doti organizzative" non motiva nulla. I requisiti si controllano nel fascicolo, non nella bozza.

*Efficacia.* La dichiarazione sull'inconferibilità è "da acquisire" e va pubblicata sul sito (art. 20, comma 3). Ogni anno l'incaricato rende anche quella sull'assenza di cause di incompatibilità (art. 20, comma 2).

### Gli altri decreti

Lo schema vale per le altre nomine. Vicesindaco e assessori si comunicano al Consiglio nella prima seduta; sopra i 3.000 abitanti nessuno dei due sessi può essere sotto il 40 per cento della Giunta. I rappresentanti presso enti si nominano sugli indirizzi del Consiglio, entro 45 giorni.[^14] Sono atti amministrativi, che si impugnano davanti al TAR: qui termine e autorità del ricorso si indicano.

### Gli errori tipici dell'IA nei decreti

- formule superate: "posizione organizzativa", "categoria D", "responsabile di P.O.";
- pareri dell'art. 49 del TUEL e "immediata eseguibilità", propri delle deliberazioni;
- l'art. 19 del D.Lgs. 165/2001, sugli incarichi dirigenziali nelle amministrazioni statali, al posto dell'art. 109 del TUEL;
- giudizi sulla persona; dichiarazioni date per già rese; ricorso al TAR.

### Prima della firma

1. competenza del sindaco; regolamento, graduazione e avviso con numero e data;
2. requisiti verificati nel fascicolo; motivazione con le sole ragioni del sindaco;
3. durata e retribuzione coerenti con contratto collettivo, regolamento e graduazione;
4. dichiarazione sull'inconferibilità acquisita prima che l'incarico produca effetti;
5. nessuna formula superata; segnaposto sostituiti; uso dell'IA annotato nel fascicolo.

## Le ordinanze

### Chi firma che cosa

"Ordinanza" indica atti diversi, con firme diverse, che il modello confonde perché si somigliano.

| Tipo | Norma | Chi firma | Presupposto |
|---|---|---|---|
| Di gestione | legge; art. 107, c. 5 | responsabile | caso previsto dalla norma |
| Sugli orari | art. 50, c. 7 e 7-bis | sindaco | indirizzi; area, evento |
| Sanità e degrado | art. 50, c. 5 | sindaco | emergenza locale |
| Incolumità e sicurezza | art. 54, c. 4 | sindaco | grave pericolo |

Le norme che attribuiscono agli organi di governo atti di gestione si intendono riferite ai dirigenti, salvi i poteri di ordinanza degli artt. 50, comma 3, e 54 (art. 107, comma 5, TUEL). Per questo le ordinanze sulla circolazione, che l'art. 7 del Codice della strada chiama "del sindaco", le firma di regola il responsabile del servizio.[^15]

Il sindaco coordina e riorganizza gli orari degli esercizi e dei servizi pubblici, sulla base degli indirizzi del Consiglio (art. 50, comma 7). Per la tranquillità e il riposo dei residenti, con ordinanza non contingibile, può anche limitare per non più di trenta giorni gli orari di vendita, anche per asporto, e di somministrazione di alcolici in aree di forte afflusso, anche per singoli eventi (comma 7-bis).

Le contingibili e urgenti sono due poteri distinti. Come rappresentante della comunità locale il sindaco provvede nelle emergenze sanitarie o di igiene pubblica a carattere esclusivamente locale e nelle situazioni di grave incuria o degrado (art. 50, comma 5). Come ufficiale del Governo, "nel rispetto dei principi generali dell'ordinamento", previene ed elimina gravi pericoli per l'incolumità pubblica, cioè l'integrità fisica delle persone, e per la sicurezza urbana, informando prima il prefetto (art. 54, commi 4 e 4-bis). Dal 2011 l'art. 54, comma 4, non consente più ordinanze non contingibili.[^16]

### Presupposti e motivazione dell'ordinanza contingibile e urgente

L'ordinanza contingibile può derogare alle regole ordinarie. Per questo la giurisprudenza ne richiede in modo costante i presupposti:[^17]

- un pericolo grave, concreto e attuale, accertato con un'istruttoria;
- l'impossibilità di affrontarlo in tempo con gli strumenti ordinari;
- misure temporanee e proporzionate;
- un destinatario individuato, di regola, in chi ha la disponibilità del bene da cui il pericolo deriva.

La motivazione lega ogni presupposto a un fatto e a un documento. L'avviso di avvio si omette per esigenze di celerità, dicendo perché (art. 7 della L. 7 agosto 1990, n. 241). Il provvedimento cautelare e urgente è immediatamente efficace (art. 21-bis); se il destinatario non esegue, il sindaco può provvedere d'ufficio, a spese del destinatario (art. 54, comma 7, TUEL).[^18] Il modello usa le formule ("ravvisata la necessità e l'urgenza") come riempitivo; il giudice cerca il pericolo concreto e l'istruttoria che lo prova.

### Il caso e il prompt

Dopo il temporale del 5 ottobre 2026 il Servizio Tecnico di Borgo Esempio rileva con un sopralluogo (ATTO_1) che il muro di cinta di un'area privata, IMMOBILE_1, è lesionato e inclinato verso una strada comunale, STRADA_1, e transenna il marciapiede. Nel verbale il tecnico indica in 48 ore il termine per la messa in sicurezza. Il proprietario, PROPRIETARIO_1, è una persona fisica: uso giallo. Nell'elenco delle norme: art. 54, commi 4, 4-bis e 7, TUEL; artt. 3, comma 4, 7 e 21-bis della L. 241/1990.

```
Sei un istruttore del Servizio Tecnico di un Comune di 6.500 abitanti.
Contesto: [fatti del verbale di sopralluogo ATTO_1, citati come tali].
Dati: bene IMMOBILE_1 su STRADA_1; destinatario PROPRIETARIO_1; misure
già adottate [quali]; ricorso: TAR [regione], 60 giorni; straordinario 120.
Norme (solo queste) e cosa regolano: [elenco]. Fuori elenco: non citarle.
Compito: bozza di ordinanza contingibile e urgente del Sindaco (art. 54,
comma 4, TUEL). Motivazione: pericolo, prova, perché non bastano gli
strumenti ordinari, perché manca l'avviso di avvio. Circa 450 parole.
Fatti: solo quelli del verbale; non aggravarli né attenuarli.
Sanzioni: non sceglierle; scrivi [VERIFICARE: norma applicabile].
Se un dato manca o è incoerente: [VERIFICARE: cosa].
Dopo l'atto, separati, elenca i [VERIFICARE] e le assunzioni fatte.
```

La riga Fatti vale nei due sensi: il modello tende a drammatizzare ("imminente pericolo di crollo"), ma la misura va proporzionata al pericolo accertato dal tecnico.

### La bozza commentata

```
COMUNE DI BORGO ESEMPIO
Ordinanza del Sindaco n. [numero] del [data]
OGGETTO: Ordinanza contingibile e urgente per la messa in sicurezza del
muro di cinta di IMMOBILE_1, lungo STRADA_1.

IL SINDACO, in qualità di ufficiale del Governo
Visti:
- l'art. 54, commi 4, 4-bis e 7, del D.Lgs. 18 agosto 2000, n. 267
  (TUEL), e gli artt. 3, 7 e 21-bis della L. 7 agosto 1990, n. 241;
- il verbale di sopralluogo del Servizio Tecnico ATTO_1, con le foto;
- la comunicazione preventiva al Prefetto [VERIFICARE: protocollo e
  data];
Considerato che:
- dal verbale risulta che, dopo il temporale del 5 ottobre 2026, il
  muro di cinta di IMMOBILE_1 presenta una lesione verticale di
  [VERIFICARE: misura riportata nel verbale] ed è inclinato verso
  STRADA_1, percorsa da pedoni e veicoli;
- secondo il tecnico il crollo è possibile [VERIFICARE: valutazione
  del verbale sui tempi], con pericolo per l'integrità fisica di chi
  transita;
- il 6 ottobre 2026 il Servizio Tecnico ha transennato il marciapiede;
  la misura è provvisoria e non elimina il pericolo;
- la messa in sicurezza spetta al proprietario, PROPRIETARIO_1, e non
  si può ottenere in tempo utile con gli strumenti ordinari
  [VERIFICARE: strumento ordinario e perché non basta];
- l'urgenza non consente di comunicare l'avvio del procedimento;
ORDINA
a PROPRIETARIO_1:
1. di mettere in sicurezza il muro entro 48 ore dalla notifica, con le
   opere indicate da un tecnico abilitato;
2. di comunicare al Servizio Tecnico, entro lo stesso termine, la fine
   dei lavori, con la dichiarazione del tecnico sulla messa in
   sicurezza;
DISPONE
3. che, in caso di inottemperanza, il Comune esegua i lavori d'ufficio
   a spese di PROPRIETARIO_1 (art. 54, comma 7, TUEL) e ne informi
   l'autorità giudiziaria [VERIFICARE: norma applicabile];
4. che l'ordinanza, immediatamente efficace, sia notificata a
   PROPRIETARIO_1 e pubblicata all'albo online.
Contro l'ordinanza è ammesso ricorso al TAR [VERIFICARE: TAR
competente] entro 60 giorni dalla notifica, o ricorso straordinario al
Presidente della Repubblica entro 120 giorni (art. 3, comma 4, della
L. 241/1990).
IL SINDACO (firmato digitalmente)
```

*Il potere.* Solo l'art. 54, comma 4: il pericolo riguarda l'incolumità di chi passa. Il modello tende a citare insieme gli artt. 50 e 54, ma sono poteri diversi: scegli quello che i fatti giustificano.

*Il prefetto.* La comunicazione è preventiva: "si darà comunicazione al Prefetto" descrive un passaggio saltato.

*Pericolo e termine.* Misura della lesione e tempi del crollo vengono dal verbale, non da stime del modello, che qui li ha lasciati da verificare. Le 48 ore sono il termine indicato dal tecnico: è il termine che rende la misura temporanea.

*Gli strumenti ordinari.* È il [VERIFICARE] più importante: se non sai spiegare perché il procedimento ordinario non basta, forse l'ordinanza contingibile non serve.

*Il marciapiede.* La sua chiusura è un provvedimento sulla circolazione, del responsabile del servizio.

### L'ordinanza sugli orari

Per la Festa d'autunno il sindaco limita la vendita notturna di alcolici per asporto (art. 50, comma 7-bis): nessuna persona nel prompt, uso verde. Ecco il dispositivo.

```
ORDINA
nelle notti del 16, 17 e 18 ottobre 2026, dalle ore 22.00 alle ore
6.00, nell'area indicata nella planimetria allegata, il divieto di
vendita per asporto di bevande alcoliche, anche con distributori
automatici.
AVVERTE
che la violazione è punita con la sanzione amministrativa pecuniaria
da euro 500,00 a euro 5.000,00 (art. 50, comma 7-bis.1, TUEL) e che è
ammesso il pagamento in misura ridotta (art. 16 della L. 24 novembre
1981, n. 689) [VERIFICARE: importo eventualmente stabilito dalla
Giunta].
```

Il modello tende a mettere la sanzione tra i punti dell'"ORDINA"; ma una sanzione non si ordina, si richiama. Non serve un'emergenza; servono ragioni legate all'area e all'evento, documentate, e una durata entro i trenta giorni. La sanzione è quella speciale del comma 7-bis.1, non quella generale dell'art. 7-bis del TUEL, da 25 a 500 euro, che il modello tende ad applicare a ogni ordinanza.[^19]

### Gli errori tipici dell'IA nelle ordinanze

- "IL SINDACO" sulle ordinanze di circolazione e sugli altri atti di gestione;
- "contingibile e urgente" per un evento in calendario da mesi;
- formule al posto dei fatti; pericolo aggravato rispetto al verbale del tecnico;
- artt. 50 e 54 citati insieme; prefetto informato dopo;
- sanzioni inventate o messe tra gli ordini; quella generale al posto di quella speciale.

Per la revisione usa, in una conversazione nuova, il prompt di controllo del capitolo sulle determine, con domande su potere, prove del pericolo, sanzioni, termine e ricorso. La bozza contiene PROPRIETARIO_1: anche il controllo passa dallo strumento dell'ente.

### Prima della firma

1. potere giusto (art. 50, comma 5, o art. 54, comma 4) e firma giusta;
2. pericolo concreto e attuale, provato da un documento citato con gli estremi;
3. motivazione: perché gli strumenti ordinari non bastano, perché manca l'avviso di avvio;
4. misure proporzionate, con il termine indicato dal tecnico;
5. prefetto informato prima; destinatario corretto; solo sanzioni previste dalla legge;
6. termine e autorità del ricorso; segnaposto sostituiti; versione per l'albo controllata.

## Sanzioni, termini e indicazione del ricorso

### Le sanzioni

Salvo diversa disposizione di legge, chi viola i regolamenti comunali, o le ordinanze del sindaco adottate sulla base di leggi o di norme regolamentari, paga da 25 a 500 euro; l'autorità che irroga la sanzione si individua con l'art. 17 della L. 24 novembre 1981, n. 689 (art. 7-bis del TUEL).[^20] Il modello salta proprio "salvo diversa disposizione di legge": dove c'è una sanzione speciale, vale quella.

Il pagamento in misura ridotta, entro sessanta giorni dalla contestazione o dalla notificazione, è pari a un terzo del massimo o, se più favorevole, al doppio del minimo, oltre alle spese del procedimento; per regolamenti e ordinanze comunali la Giunta può stabilire un importo diverso, entro i limiti della sanzione (art. 16). Il modello calcola spesso solo il terzo del massimo: i conti si fanno a mano.

| Sanzione | Un terzo del massimo | Doppio del minimo | Si paga |
|---|---|---|---|
| da 25 a 500 euro | 166,67 euro | 50,00 euro | 50,00 euro |
| da 500 a 5.000 euro | 1.666,67 euro | 1.000,00 euro | 1.000,00 euro |

La violazione si contesta subito o si notifica entro novanta giorni (art. 14); entro trenta giorni l'interessato può presentare scritti difensivi (art. 18). Contro l'ordinanza-ingiunzione si fa opposizione al giudice ordinario, di regola il giudice di pace, entro trenta giorni dalla notificazione.[^21]

Nessuna ordinanza può creare una sanzione: le sanzioni amministrative le stabilisce solo la legge (art. 1 della L. 689/1981). Per l'ordinanza contingibile rivolta a una persona, la legge prevede l'esecuzione d'ufficio a spese del destinatario. Se alla violazione di un'ordinanza contingibile si applichi anche la sanzione generale dell'art. 7-bis, comma 1-bis, è questione discussa: la valuta l'ufficio, con il segretario, non il modello. L'inosservanza può integrare il reato dell'art. 650 del codice penale, ma lo valuta l'autorità giudiziaria: l'ordinanza può richiamarlo, non "comminarlo".[^22]

### Termini ed efficacia

Il provvedimento che limita la sfera giuridica di un privato è efficace con la comunicazione; quello cautelare e urgente lo è subito (art. 21-bis della L. 241/1990). Il termine per adempiere decorre dalla notifica e sta nel dispositivo. Le ordinanze rivolte a tutti si pubblicano all'albo online.[^23]

### Il termine e l'autorità cui ricorrere

Ogni atto notificato indica il termine e l'autorità cui ricorrere (art. 3, comma 4, della L. 241/1990). Al TAR si ricorre entro sessanta giorni dalla notificazione, dalla comunicazione o dalla piena conoscenza; per gli atti non notificati, dalla fine della pubblicazione prevista dalla legge. In alternativa, ricorso straordinario al Presidente della Repubblica entro centoventi giorni.[^24]

| Atto | Davanti a chi | Termine |
|---|---|---|
| Ordinanza contingibile o sugli orari | TAR, o ricorso straordinario | 60 o 120 giorni |
| Ordinanza-ingiunzione | giudice ordinario | 30 giorni |
| Nomina di rappresentanti | TAR, o ricorso straordinario | 60 o 120 giorni |
| Incarico a un dipendente | giudice del lavoro | non quelli del TAR |

Il modello confonde spesso giudici e termini: il TAR per la sanzione, il giudice di pace per l'ordinanza, i sessanta giorni "dalla pubblicazione" per un atto notificato. Termine e autorità li scrivi tu nella riga Dati: il modello li copia.

## In sintesi

- Nel verbale presenze, voti e dichiarazioni vengono dalla scheda del segretario, mai dal modello.
- Trascrizione gialla, seduta segreta rossa; salute, reati e minori si tolgono prima del prompt; i dubbi si chiudono sull'audio.
- Nel decreto di nomina il modello scrive la motivazione, il sindaco sceglie la persona.
- Elevata qualificazione, non posizione organizzativa; niente art. 49; per l'incarico a un dipendente, giudice del lavoro e non TAR.
- Le ordinanze di gestione le firma il responsabile, anche quando la legge dice "sindaco".
- L'ordinanza contingibile vive di fatti provati, non di formule.
- Solo sanzioni previste dalla legge, misura ridotta calcolata a mano, ricorso in ogni atto notificato.

[^1]: D.Lgs. 18 agosto 2000, n. 267, *Testo unico delle leggi sull'ordinamento degli enti locali*, art. 97, comma 4, lett. a); art. 38, commi 2 e 7; art. 39, comma 3, normattiva.it.

[^2]: Codice civile, art. 2700, normattiva.it. Per la giurisprudenza civile la fede privilegiata non si estende alle valutazioni e agli apprezzamenti di chi redige l'atto. Che il verbale delle sedute degli organi collegiali sia un atto pubblico è orientamento consolidato anche della giurisprudenza amministrativa. Forma del verbale, approvazione e rettifiche sono disciplinate dal regolamento del Consiglio.

[^3]: L. 23 settembre 2025, n. 132, *Disposizioni e deleghe al Governo in materia di intelligenza artificiale*, art. 14, comma 2, normattiva.it. Si veda il capitolo sulla legge italiana sull'IA.

[^4]: Anche se il verbale pubblicato rientrasse tra i testi che informano il pubblico su questioni di interesse pubblico, l'obbligo di dichiarare l'uso dell'IA non varrebbe per un testo rivisto da una persona e pubblicato sotto la responsabilità editoriale di chi lo firma: Regolamento (UE) 2024/1689, art. 50, par. 4, secondo comma, applicabile dal 2 agosto 2026 e non modificato dal Regolamento (UE) 2026/1744, eur-lex.europa.eu. Si vedano il capitolo sull'AI Act e quello su come rispondere a cittadini e PEC.

[^5]: Garante per la protezione dei dati personali, indicazioni sulle riprese audiovisive e sulla diffusione delle sedute dei consigli comunali, garanteprivacy.it. Per il Garante il regolamento può anche indicare i casi in cui limitare le riprese, per esempio quando possono emergere dati sulla salute o altri dati delicati. I dati relativi alla salute non possono essere diffusi: D.Lgs. 30 giugno 2003, n. 196, art. 2-septies, comma 8, normattiva.it.

[^6]: Regolamento (UE) 2016/679, art. 4, n. 14, e art. 9, par. 1, eur-lex.europa.eu. Nella regola del semaforo i dati biometrici sono rossi.

[^7]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 134, comma 4. Nei Comuni tra 3.000 e 10.000 abitanti il Consiglio è composto dal sindaco e da dodici consiglieri: D.L. 13 agosto 2011, n. 138, art. 16, comma 17, lett. b), come sostituito dalla L. 7 aprile 2014, n. 56, art. 1, comma 135, normattiva.it. L'immediata eseguibilità è trattata nel capitolo sulle delibere.

[^8]: D.Lgs. 18 agosto 2000, n. 267, cit., artt. 48, comma 3, 50, comma 10, 107, commi 2 e 3, e 109, commi 1 e 2, normattiva.it. Il sindaco può conferire funzioni anche al segretario comunale (art. 97, comma 4, lett. d)).

[^9]: ARAN, *Contratto collettivo nazionale di lavoro relativo al personale del comparto Funzioni locali*, triennio 2019-2021, 16 novembre 2022, e triennio 2022-2024, 23 febbraio 2026, aranagenzia.it. Sul nuovo limite della retribuzione di posizione: LentePubblica, *Rinnovo CCNL enti locali 2022-2024 firmato definitivamente: tutte le novità*, 2026, lentepubblica.it. Articoli e importi si leggono nel testo firmato.

[^10]: D.Lgs. 8 aprile 2013, n. 39, art. 2, comma 2, che assimila agli incarichi dirigenziali negli enti locali il conferimento di funzioni dirigenziali a personale non dirigenziale, e art. 20, commi 1, 2, 3 e 4, normattiva.it.

[^11]: L. 23 dicembre 2000, n. 388, art. 53, comma 23, normattiva.it, che riguarda gli enti locali con meno di 5.000 abitanti.

[^12]: Regolamento (UE) 2024/1689, Allegato III, punto 4, lett. a) e b), art. 25, par. 1, lett. c), e art. 113, come modificato dal Regolamento (UE) 2026/1744; Regolamento (UE) 2016/679, art. 22, eur-lex.europa.eu; L. 23 settembre 2025, n. 132, cit., art. 14, comma 2. Si veda il capitolo sull'AI Act.

[^13]: D.Lgs. 30 marzo 2001, n. 165, art. 5, comma 2, e art. 63, comma 1, che devolve al giudice ordinario anche le controversie sul conferimento e sulla revoca degli incarichi dirigenziali, normattiva.it.

[^14]: L. 7 aprile 2014, n. 56, art. 1, comma 137; D.Lgs. 18 agosto 2000, n. 267, cit., art. 42, comma 2, lett. m), sugli indirizzi del Consiglio, art. 46, comma 2, e art. 50, commi 8 e 9, per i quali le nomine dei rappresentanti si fanno entro 45 giorni dall'insediamento o entro la scadenza del precedente incarico, normattiva.it.

[^15]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 107, comma 5; D.Lgs. 30 aprile 1992, n. 285, *Nuovo codice della strada*, artt. 6 e 7, normattiva.it.

[^16]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 50, commi 5, 7 e 7-bis, nel testo modificato dal D.L. 20 febbraio 2017, n. 14, convertito dalla L. 18 aprile 2017, n. 48, e art. 54, commi 4 e 4-bis, normattiva.it; Corte costituzionale, sentenza n. 115 del 2011, cortecostituzionale.it, che ha dichiarato illegittimo l'art. 54, comma 4, nella parte in cui, con la parola "anche", consentiva al sindaco ordinanze non contingibili e urgenti.

[^17]: Sui limiti delle ordinanze di necessità, a partire dal rispetto dei principi generali dell'ordinamento, dalla motivazione e dalla durata limitata: Corte costituzionale, sentenze n. 8 del 1956 e n. 26 del 1961, cortecostituzionale.it, e n. 115 del 2011, cit. I presupposti elencati sono quelli che la giurisprudenza amministrativa richiama in modo ricorrente; le pronunce si cercano su giustizia-amministrativa.it.

[^18]: L. 7 agosto 1990, n. 241, art. 7, comma 1, e art. 21-bis; D.Lgs. 18 agosto 2000, n. 267, cit., art. 54, comma 7, normattiva.it.

[^19]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 50, commi 7-bis e 7-bis.1, normattiva.it.

[^20]: D.Lgs. 18 agosto 2000, n. 267, cit., art. 7-bis, commi 1, 1-bis e 2, normattiva.it.

[^21]: L. 24 novembre 1981, n. 689, artt. 14, 16, 17, 18 e 22; D.Lgs. 1° settembre 2011, n. 150, art. 6, normattiva.it. La competenza del giudice di pace o del tribunale dipende dalla materia e dall'importo.

[^22]: L. 24 novembre 1981, n. 689, cit., art. 1, sul principio di legalità delle sanzioni amministrative; D.Lgs. 18 agosto 2000, n. 267, cit., art. 7-bis, comma 1-bis, e art. 54, comma 7; Codice penale, art. 650, *Inosservanza dei provvedimenti dell'Autorità*, che punisce chi non osserva un provvedimento legalmente dato per ragioni di giustizia, di sicurezza pubblica, di ordine pubblico o d'igiene, se il fatto non costituisce un reato più grave, normattiva.it.

[^23]: L. 7 agosto 1990, n. 241, cit., art. 21-bis; L. 18 giugno 2009, n. 69, art. 32, sull'albo online, normattiva.it.

[^24]: L. 7 agosto 1990, n. 241, cit., art. 3, comma 4; D.Lgs. 2 luglio 2010, n. 104, *Codice del processo amministrativo*, artt. 29 e 41, comma 2; D.P.R. 24 novembre 1971, n. 1199, artt. 8 e 9, normattiva.it.

## Dietro le quinte

Questo capitolo è stato scritto con Claude, di Anthropic, in due passaggi distinti: una stesura completa, basata sulla ricerca condivisa del libro, e una revisione separata con fact-checking, revisione legale e GDPR ed editing, che ha apportato 44 correzioni. Tra gli errori della stesura intercettati dalla revisione:

- Il prompt del verbale lasciava entrare nel prompt i passaggi su salute, reati e minori e chiedeva al modello di ometterli.
- Il commento alla bozza del verbale presupponeva che il dato sanitario di una famiglia fosse passato dal modello.
- Il prompt chiedeva un resoconto 'al passato', ma la bozza commentata era al presente.
- Sull'AI Act il testo rinviava al solo Allegato III, punto 4, lett. b), e diceva che l'art. 22 GDPR si applica comunque.

Le fonti istituzionali (Normattiva, Gazzetta Ufficiale, EUR-Lex) non erano raggiungibili dall'ambiente di lavoro: i riscontri sono stati fatti su fonti secondarie concordanti, e i punti da ricontrollare sui testi ufficiali sono stati annotati per la revisione finale.
