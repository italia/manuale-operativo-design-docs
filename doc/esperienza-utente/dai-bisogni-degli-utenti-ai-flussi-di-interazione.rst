Dai bisogni degli utenti ai flussi di interazione 
=================================================

.. include:: /banner.rst

I punti di partenza da cui avviare l’attività di progettazione possono essere sintetizzati in alcuni strumenti operativi che abbiamo affrontato nel capitolo dedicato al service design: 

-  `personas <../../doc/service-design/gestione-dei-progetti.html#personas-e-profili-utente>`__,
   ossia profili verosimili di utenti del servizio delineati in base ai risultati della ricerca, rappresentativi di un gruppo di utenti; 

-  `user
   journey <../../doc/service-design/gestione-dei-progetti.html#user-journey>`__,
   ovvero la rappresentazione del percorso compiuto dall’utente interagendo con i touchpoint fisici o digitali del servizio, elaborata a partire dalle personas e dalle loro esperienze d’uso del servizio in questione.

In questo capitolo faremo un passo in avanti, introducendo strumenti quali gli **scenari d’uso** e i **flussi di interazione**, che ci aiutano a concentrarci sulle personas che useranno il servizio, assumere il loro punto di vista e avere una lista chiara dei loro bisogni, evidenziando priorità e possibili criticità. Sulla base di scenari e flussi procederemo poi alla fase di prototipazione vera e propria.

Gli `scenari d’uso <https://docs.google.com/spreadsheets/d/1G2OHLvQ25efMf_mSUA-DgKXs8PyT9fLK2eiA1BbCdhI/edit#gid=1918884779>`__ sono narrazioni che collocano le Personas di riferimento al centro di contesti d’uso e situazioni emersi come ricorrenti e/o rilevanti grazie alla ricerca e sono pertanto utili a identificare le caratteristiche più importanti del servizio dal punto di vista degli utenti. 

+--------+-------------------------------------+-------------------------------------------------------+
| CODICE | NOME SCENARIO                       | DESCRIZIONE                                           |
+--------+-------------------------------------+-------------------------------------------------------+
| S01    | Approfondire un tema                | Giorgio vede un cartello informativo vicino al        |
|        | importante per la città             | cantiere sotto casa sua, si collega al sito del       |
|        |                                     | comune tramite QR. Da qui si informa sui lavori       |
|        |                                     | in corso nella sua via e invia una segnalazione       |
|        |                                     | per alcuni danni causati dal cantiere.                |
+--------+-------------------------------------+-------------------------------------------------------+
| S02    | Scoprire gli eventi in programma e  | Alessandra si trova in città per lavoro e cerca       |
|        | l’orario di apertura di uno spazio  | qualcosa di interessante da fare nel fine settimana.  |
|        | espositivo                          | Dalla homepage del sito trova tutte le iniziative     |
|        |                                     | del periodo estivo e quelle organizzate nel prossimo  |
|        |                                     | weekend. Si interessa a una mostra in particolare     |
|        |                                     | e trova le informazioni che le servono per visitarla. |
+--------+-------------------------------------+-------------------------------------------------------+
| S03    | Iscrivere un figlio all’asilo nido  | Giorgio vuole iscrivere suo figlio all’asilo nido     |
|        |                                     | e cerca le informazioni che gli servono sul sito      |
|        |                                     | del comune. Seguendo la procedura indicata presenta   |
|        |                                     | la domanda di iscrizione. Giorni dopo riceve la       |
|        |                                     | notifica della pubblicazione delle graduatorie,       |
|        |                                     | conferma la domanda e procede al pagamento della      |
|        |                                     | quota di iscrizione.                                  |
+--------+-------------------------------------+-------------------------------------------------------+

Per specificare con maggior dettaglio un preciso caso d’uso del servizio, all’interno degli scenari si possono generare le cosiddette *user stories* (storie dell'utente), ossia **descrizioni informali delle funzioni di un servizio**, espresse dal punto di vista dell’utente secondo una struttura che definisce il ruolo di chi la esprime, l’azione che vuole o deve compiere e l’obiettivo che muove all’azione. 

Io come [*personas*] vorrei [*funzione*] per [*bisogno*].

Le *user stories* facilitano la comprensione delle caratteristiche richieste al servizio da parte dei membri del team di lavoro. 

Ecco una lista di esempi di alcune risposte (funzioni) ai bisogni degli utenti del sito di un Comune, espressi in termini di *user stories*. 

+-------------+-------------------------+---------------------------------+---------------------------------------+
| PERSONAS    | BISOGNI                 | FUNZIONI                        | USER STORIES                          |
+-------------+-------------------------+---------------------------------+---------------------------------------+
|  Cittadino  | Controllare le          | Visualizzare l’elenco delle     | Io come cittadino vorrei accedere     |
|             | contravvenzioni         | multe in una pagina personale   | a una pagina web riservata dove       |
|             | ricevute                |                                 | controllare le contravvenzioni che    |
|             |                         |                                 | ho ricevuto                           |
+-------------+-------------------------+---------------------------------+---------------------------------------+
|  Cittadino  | Rinnovare la carta di   | Prenotare online l’appuntamento | Io come cittadino vorrei prenotare    |
|             | identità                | per il rinnovo nel Comune       | online l’appuntamento all’ufficio     |
|             |                         | di residenza                    | comunale, in modo da rinnovare la mia |
|             |                         |                                 | carta d’identità                      |
+-------------+-------------------------+---------------------------------+---------------------------------------+
|  Cittadino  | Essere in regola con il | Effettuare il pagamento         | Io come cittadino vorrei poter pagare |
|             | pagamento della tassa   | on line della TARI in modo      | i servizi pubblici online in modo     |
|             | sui rifiuti (TARI)      | facile e sicuro.                | facile e sicuro, inclusa la TARI,     |
|             |                         |                                 | in modo da essere in regola con i     |
|             |                         |                                 | pagamenti                             |
+-------------+-------------------------+---------------------------------+---------------------------------------+

Si può dire che ciascuna *user story* corrisponde a una funzione del sistema e, quindi, a un possibile obiettivo dell’utente; per raggiungere tale obiettivo, l’utente deve svolgere dei compiti (*task*), che a loro volta sono costituiti da una serie di azioni dell’utente (*sub-task*) e risposte del sistema. 
A questo punto della progettazione, è necessario scendere nel dettaglio di queste azioni e definire le conseguenti risposte del sistema, in modo da mappare tutti i possibili percorsi che un utente può svolgere per raggiungere un obiettivo. 
Tali percorsi sono rappresentati dai flussi di interazione.

Per `costruire i flussi di interazione <https://docs.google.com/spreadsheets/d/19u8t0EuGCck3yNS12F4V9IjuwETJhVXOB_PvPpGSTnU/edit#gid=1918884779>`__ è necessario quindi descrivere ogni singola interazione dell'utente con il sistema, indicando anche il dettaglio di funzioni e/o contenuti proposti dal sistema come risposta alle azioni dell’utente. L’analisi deve coprire ogni *task*, fino al raggiungimento dell’obiettivo e tenere presente che un obiettivo potrebbe essere raggiunto dall’utente attraverso sequenze di azioni diverse, individuando quindi percorsi alternativi, anche in base al livello di esperienza dell’utente stesso.

Molto utile è visualizzare i flussi di interazione in una `versione grafica <https://docs.google.com/presentation/d/1qzEtt75yfSaQihD6jy0WGElrvQeyp37MCgJuqEG8Q_U/edit#slide=id.gb8eece2fcb_3_175>`__, che fornisce una visione complessiva e immediata dei percorsi possibili per l’utente all’interno del sistema.

Una volta completata la costruzione di ciascun flusso di interazione, sarà possibile evidenziare i potenziali snodi critici di ogni percorso e avanzare soluzioni progettuali in risposta ad esse. In questo modo, i flussi di interazione aiutano a progettare un’interfaccia in modo accurato e realmente centrato sull’utente.
A questo punto, raggiunto questo livello di dettaglio, è possibile avviare il processo di prototipazione.
