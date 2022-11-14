Web analytics
-------------

.. include:: /banner.rst

Premessa
~~~~~~~~

Questa guida ha l’obiettivo di aiutare chi si occupa a vario titolo di *touchpoint* (punti di contatto) e servizi digitali di una pubblica amministrazione a:

-  comprendere il funzionamento di una piattaforma di web analytics
-  capire come collezionare i principali indicatori di performance di un
   sito o servizio
-  capire come interpretare determinati set di dati per trarre
   informazioni utili rispetto al comportamento degli utenti e il loro
   livello di soddisfazione
-  comprendere quali azioni migliorative applicare ai contenuti, ai
   metadati e alla struttura del sito in base ai risultati dell’analisi
   dei dati
-  comprendere come configurare una piattaforma di web analytics su uno
   o più siti
-  comprendere come produrre e distribuire un report di analytics, per
   condividere i dati di utilizzo con i vari *stakeholder* e il team di
   lavoro interno
-  comprendere come una lettura sistematica dei dati possa influenzare
   positivamente la comprensione dei comportamenti online degli utenti e
   consentire l’avvio di azioni migliorative dei servizi digitali

Introduzione
~~~~~~~~~~~~

L’analisi delle performance di un ambiente digitale è un’attività cruciale
per comprendere in che maniera *touchpoint* e servizi rispondono in maniera adeguata ai bisogni informativi e/o di
servizio degli utenti.

Questa tipologia di analisi consente di rispondere, ad esempio, in modo
puntuale alle seguenti domande:

-  Quanti utenti visitano il sito/servizio, per quanto tempo e quali e quante
   pagine visitano?
-  Quali sono le principali aree geografiche da cui provengono i visitatori del sito?
-  Quali sono i contenuti più visitati dagli utenti in un dato
   intervallo di tempo?
-  In quale momento della settimana o dell’anno il sito registra il
   maggiore o il minore numero di visite? Queste oscillazioni sono
   causate da un’eventuale stagionalità delle tematiche trattate o
   coincidono con la pubblicazione di nuovi contenuti?
-  Quali sono i termini tramite cui gli utenti arrivano al sito mendiante
   un motore di ricerca? Rappresentano per la maggior parte il
   nome/dominio del sito oppure fanno riferimento a informazioni/servizi
   trattati al suo interno?
-  Quali sono i principali termini di ricerca digitati nel motore di
   ricerca interno del sito, se presente?
-  In che percentuale gli utenti visitano il sito da
   dispositivi mobili?

Le risposte a tali domande derivano dall’analisi continuativa di
indicatori di performance che offrono ad esempio informazioni su quali
siano volumi di traffico, il comportamento degli utenti, la qualità dei contenuti pubblicati e l’efficienza
tecnologica del sito o del servizio nel suo complesso.

Metriche e dimensioni
~~~~~~~~~~~~~~~~~~~~~

I dati generati dalle piattaforme di web analytics sono il frutto di
combinazioni eterogenee di metriche (dati quantitativi) e dimensioni
(attributi qualitativi dei dati). È bene sottolineare che il numero reale dei visitatori conteggiati per un dato intervallo di tempo è soggetto a distorsioni — per eccesso o per difetto — dovute al fatto che il calcolo degli utenti in web analytics è basato su *cookies* e tende quindi a generare più o meno utenti unici al variare di determinate circostanze (accesso al sito da dispositivi diversi, *browser* diversi, cancellazione dei *cookies*). Di seguito una panoramica
delle principali metriche e dimensioni utilizzate per l'analisi del traffico web. Si
precisa che la nomenclatura di metriche e dimensioni può variare a
seconda della piattaforma di raccolta utilizzata.

Principali Metriche (dati quantitativi)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Visite**
   *Definizione:* numero totale di visite al sito in un dato intervallo
   di tempo (anche da parte dello stesso utente)

   *A cosa serve:* rappresenta il volume di traffico che il sito riceve
   in un determinato lasso temporale. È una delle metriche più usate per
   costruire uno storico dei volumi di traffico del sito, su cui basare
   comparazioni e/o proiezioni

**Visite uniche**
   *Definizione:* numero di singoli individui (o singoli IP - Internet Protocol Address) che ha
   effettuato almeno una visita al sito

   *A cosa serve:* è la metrica che restituisce in maniera accurata il
   numero di singoli individui che ha interagito con il sito in un dato
   lasso di tempo

**Visualizzazioni di pagina**
   *Definizione:* numero totale di pagine visitate, anche da parte dello
   stesso utente, in un dato intervallo di tempo. Comprende
   visualizzazioni ripetute della stessa pagina

   *A cosa serve:* indica il volume complessivo dei contenuti del sito
   acceduti dagli utenti

**Pagine visitate per visita**
   *Definizione:* media aritmetica del numero di pagine visitate per
   visita al sito. Comprende le visualizzazioni ripetute della stessa
   pagina

   *A cosa serve:* offre indicazioni sulla “profondità” delle visite al
   sito e sul livello di coinvolgimento dei contenuti. Tale metrica deve
   essere interpretata a seconda della natura del sito e dei suoi
   obiettivi (es. rispetto al numero minimo di pagine desiderate per
   visita)

**Durata delle visite**
   *Definizione:* media aritmetica della durata di una singola visita al
   sito

   *A cosa serve:* indica il tempo medio trascorso dai visitatori sul
   sito. Tale metrica deve essere interpretata a seconda della natura
   del sito e dei suoi obiettivi

**Tempo sulla pagina**
   *Definizione:* media aritmetica del tempo trascorso dagli utenti su
   una determinata pagina (o un insieme di pagine)

   *A cosa serve:* determina l’efficacia di un contenuto, a seconda
   della sua tipologia e dei suoi obiettivi

**Frequenza di rimbalzo**
   *Definizione:* percentuale di visitatori che ha abbandonato il sito
   dopo una pagina

   *A cosa serve:* misura la quota di utenti che arrivano al sito e lo
   abbandonano subito, senza proseguire la navigazione o compiere azioni. La percentuale di frequenza di rimbalzo
   può essere interpretata in maniera opposta a seconda della natura del
   sito: ad esempio una frequenza di rimbalzo alta per un sito
   informativo è indice del fatto che le pagine potrebbero essere
   scarsamente utili/interessanti, mentre può essere considerata un dato
   positivo per un sito o una pagina che hanno il semplice scopo di
   direzionare gli utenti altrove

**Nuove visite**
   *Definizione:* percentuale delle prime visite al sito sul totale
   delle visite

   *A cosa serve:* metrica utile in particolare quando l’obiettivo del
   sito è quello di accrescere i volumi di traffico provenienti da nuove
   tipologie di visitatori

**Nuovi utenti/utenti di ritorno**
   *Definizione:* rapporto fra prime visite al sito e utenti che hanno
   già visitato il sito precedentemente, in un dato intervallo di tempo

   *A cosa serve:* a seconda degli obiettivi del sito, serve a
   comprendere in che misura i volumi di traffico si suddividono fra
   nuovi utenti e utenti fidelizzati

**Velocità di caricamento del sito**
   *Definizione:* quantità di tempo media (espressa in secondi)
   impiegato da una pagina del sito per caricarsi, dall’avvio della
   visualizzazione nel browser alla fine del suo caricamento

   *A cosa serve:* metrica fondamentale per monitorare l’efficienza del
   sito in termini di velocità, anche e soprattutto per la fruizione da
   dispositivi mobili

Principali Dimensioni (attributi qualitativi dei dati)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tempo**
   intervallo di tempo su cui impostare una rilevazione (giorno,
   settimana, mese, anno, intervallo personalizzato)

**Provenienza geografica e lingua**
   luogo da cui provengono le visite
   degli utenti (paese, città, continente, subcontinente); impostazioni
   relative alle preferenze di lingua

**Tecnologia utilizzata**
   strumenti tecnologici utilizzati dagli utenti
   per la navigazione sul sito (tipologia di dispositivo, browser, sistema
   operativo, provider di rete)

**Contenuti**
   le pagine, le pagine di entrata e di uscita, gli “eventi”
   compiuti sul sito (es. download di documenti, click su link outbound)

**Canali di acquisizione del traffico**
   canali web tramite cui gli
   utenti arrivano al sito. Il raggruppamento di canali principali
   comprende: traffico diretto, ricerca organica (cioè traffico non a
   pagamento proveniente dai motori di ricerca), siti referenti, social.
   Altri canali - se attivi - sono ad esempio: email marketing, digital
   advertising, affiliazioni

**Ricerca su sito**
   monitora la funzione di search del motore interno
   di un sito web, restituendo i termini di ricerca immessi dagli utenti,
   il numero di ricerche per termine e altri indicatori

**Obiettivi**
   per tracciare il completamento di determinate azioni
   eseguite degli utenti sul sito (es. compilazione di un form, durata
   minima di una visita, numero minimo di pagine per visita)

Analizzare le ricerche degli utenti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le ricerche degli utenti sono quasi sempre il più ampio vettore di
traffico verso i contenuti web. Per questa ragione, non soltanto è
fondamentale fare in modo che le pagine di un sito siano `“ottimizzate”
per essere trovate dagli utenti attraverso i motori di
ricerca <../content-design/seo.html>`__, ma è altrettanto importante
analizzare i dati di web analytics provenienti dalle ricerche interne ed
esterne al sito per conoscere le performance dei singoli
contenuti.

Di seguito i principali indicatori da tenere in considerazione quando si
analizzano le ricerche degli utenti e le relative azioni migliorative
che si possono intraprendere:

Ricerca esterna al sito
^^^^^^^^^^^^^^^^^^^^^^^

**Top motori di ricerca referenti**
   *Definizione:* Principali motori di ricerca (Google, Bing, Yahoo…)
   che portano traffico al sito

   *Azione:* Usa i relativi webmaster tools (es. `Google Search
   Console <../content-design/seo.html>`__) per ottimizzare i contenuti
   e la struttura del sito e renderli così più facilmente scansionabili
   dai *crawler* (software che raccolgono dati dalle pagine web) dei motori e “trovabili” dagli utenti

**Top termini/frasi di ricerca**
   *Definizione:* Le principali parole e frasi digitate nei motori di
   ricerca tramite cui gli utenti arrivano al sito

   *Azione:* Verifica che i termini utilizzati dagli utenti coincidano o
   siano simili a quelli utilizzati nel sito. Puoi prendere spunto da
   parole e frasi utilizzate dagli utenti per migliorare la terminologia
   che usi nei titoli, nei metadati, nelle URL (Uniform Resource Locator)e in generale all’interno
   dei contenuti, in modo da favorire l’ottimizzazione sui motori di
   ricerca

**Top termini di ricerca con basso CTR (click through rate)**
   *Definizione:* Parole e frasi digitate nei motori di ricerca che
   portano la minore quota di traffico al sito

   *Azione:* Revisiona e aggiorna i contenuti che gli utenti visitano
   dopo aver cercato tali termini, per renderli più appetibili e utili

Ricerca su sito
^^^^^^^^^^^^^^^

**Top termini/frasi di ricerca**
   *Definizione:* Le principali parole e frasi digitate dagli utenti nel
   motore di ricerca interno del sito

   *Azione:* Crea nuovi contenuti o aggiorna quelli già presenti,
   incorporando la terminologia degli utenti nei metadati, negli
   eventuali tag e nel testo stesso, in modo da aiutare i visitatori a
   trovare le informazioni più aderenti ai bisogni espressi nella
   ricerca

**Top ricerche che non generano risultati**
   *Definizione:* Parole e frasi digitate dagli utenti nel motore
   interno del sito che non restituiscono risultati, per mancanza di
   contenuti associati o non rappresentati nella maniera corretta

   *Azione:* Analizza i contenuti per capire se è il caso di aggiornarli
   o di pubblicarne di nuovi che rappresentino il bisogno espresso
   dall’utente nella ricerca

**Top termini di ricerca con basso CTR (click through rate)**
   *Definizione:* Parole e frasi digitate nel motore di ricerca interno
   che restituiscono il più basso numero di visualizzazioni di pagina

   *Azione:* Incorpora la terminologia valida nei testi e nei metadati
   per rendere le pagine più rilevanti rispetto a quei termini

**Principali oscillazioni nelle top ricerche**
   *Definizione:* Macro cambiamenti nel *ranking* (ordinamento, classifica) dei termini più cercati
   nel motore di ricerca interno del sito

   *Azione:* Cerca di analizzare le ragioni per cui alcuni termini
   diventano meno ricercati di altri e viceversa; assicurati che per i
   nuovi termini di ricerca diventati popolari siano presenti contenuti
   che soddisfano i nuovi bisogni espressi dai visitatori

**Utenti che utilizzano la ricerca su sito**
   *Definizione:* Percentuale dei visitatori unici del sito che utilizza
   la funzione di ricerca interna

   *Azione:* Ti aiuta a capire se è il caso di ottimizzare le
   funzionalità di ricerca e l’architettura informativa del sito,
   facendo in modo che i contenuti più ricercati siano il più possibile
   visibili

La segmentazione
~~~~~~~~~~~~~~~~
La segmentazione in web analytics consiste nell’isolare dal traffico web aggregato sottoinsiemi di visite (o di utenti unici) che condividono attributi (qualitativi e/o quantitativi) comuni. La segmentazione del traffico in sottogruppi, ha l’obiettivo di far emergere il “valore” di uno specifico insieme di utenti rispetto al traffico aggregato - che è tipicamente quello più rappresentato nei report, ma meno rappresentativo delle specificità dei singoli gruppi di utenza.

Nelle principali piattaforme di web analytics la segmentazione può essere applicata utilizzando segmenti preimpostati (laddove disponibili) oppure creando dei segmenti di utenza ad hoc. Si possono creare segmenti sulla base di attributi demografici dei visitatori, delle tecnologie utilizzate per navigare il sito, del comportamento, della data di prima visita dell’utente, delle sorgenti di traffico, e così via.

Il traffico "segmentato" può essere poi quindi comparato nei rapporti e nelle configurazioni *dashboard* (pannelli dinamici di analisi dei dati).

Per maggiori dettagli sulla segmentazione utenti si rimanda al `Kit Web Analytics <https://designers.italia.it/kit/analytics/>`__.


Cosa fare per adempiere alla normativa sui cookie
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Tipo di cookie                                                                           | Segnalarli nell’informativa | Inserire il banner e chiedere il consenso ai visitatori | Notificare al Garante                                      |
+==========================================================================================+=============================+=========================================================+============================================================+
| Nessun cookie                                                                            | No                          | No                                                      | No                                                         |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Tecnici/analitici di prima parte                                                         | Si                          | No                                                      | No                                                         |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Analitici terze parti (con strumenti che riducono il potere identificativo dei cookie)   | Si                          | No                                                      | No                                                         |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Analitici terze parti (senza strumenti che riducono il potere identificativo dei cookie) | Si                          | Si                                                      | Si                                                         |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Di profilazione prima parte                                                              | Si                          | Si                                                      | Si                                                         |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+
| Di profilazione terze parti                                                              | Si                          | Si                                                      | No* (la notificazione è a carico del soggetto terza parte) |
+------------------------------------------------------------------------------------------+-----------------------------+---------------------------------------------------------+------------------------------------------------------------+

Per approfondimenti si rimanda al sito del `Garante della Privacy <http://www.garanteprivacy.it/cookie>`__.

La reportistica
~~~~~~~~~~~~~~~

Un’analisi sistematica dei dati statistici di performance e
soddisfazione utente è fondamentale per decidere quali azioni
migliorative intraprendere su un servizio digitale.

È altrettanto fondamentale la creazione di una reportistica ad hoc che
abbia la finalità di essere condivisa all’interno di un team di lavoro
(o con altri stakeholder). In linea generale è possibile creare e
inviare report customizzati direttamente dalle principali piattaforme di
web analytics.

Per un approfondimento sul tema, si rimanda al `Kit Web Analytics <https://designers.italia.it/kit/analytics/>`__.

Strumenti di web analytics: Web Analytics Italia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In questa sezione puoi trovare informazioni e alcuni link di approfondimento che ti aiuteranno a comprendere come adottare uno strumento di web analytics per i tuoi siti e servizi digitali.

Esistono numerosi software *open source* per la raccolta e l'analisi dei dati di traffico di siti e servizi digitali, che è possibile utilizzare per ottenere informazioni statistiche relative all'uso di una soluzione digitale e nel rispetto della normativa vigente, quali ad esempio `Matomo analytics <https://developers.italia.it/it/software/italia-software-matomo-32c75d.html>`__ e `Plausible analytics <https://developers.italia.it/it/software/italia-software-plausible-a9b3cb>`__. 

A partire dalla prima metà del 2020, è disponibile inoltre gratuitamente **una soluzione di web analytics open source dedicata alle pubbliche amministrazioni italiane**, `Web Analytics Italia <https://webanalytics.italia.it/>`__ (WAI).

Il servizio WAI si colloca nel contesto delle `Linee guida di design per i siti internet e i servizi digitali della PA <https://docs.italia.it/italia/design/lg-design-servizi-web/it/versione-corrente/index.html>`__ italiana, oltre che nel Piano Triennale per l'Informatica nella PA. 

Nel paragrafo seguente ti proponiamo inoltre una serie di link di approfondimento per comprendere come installare/configurare le principali piattaforme di web analytics open source sopra menzionate.


Strumenti di web analytics: Matomo analytics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Scheda software Matomo analytics
   <https://developers.italia.it/it/software/italia-software-matomo-32c75d.html>`__
-  `Aggiungere un sito a Matomo
   <https://matomo.org/guide/manage-matomo/websites/>`__
-  `Implementare il tracciamento del motore di ricerca interno al sito
   <https://matomo.org/guide/reports/site-search/>`__
-  `Impostare un obiettivo
   <https://matomo.org/guide/reports/goals-and-conversions/>`__
-  `La segmentazione
   <https://matomo.org/docs/segmentation/>`__
-  `Creazione ed invio di report customizzati
   <https://matomo.org/guide/manage-matomo/email-reports/>`__
-  `Importare dati da GA a Matomo
   <https://matomo.org/blog/2012/08/google-analytics-to-piwik/>`__

Strumenti di web analytics: Plausible analytics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Scheda software Plausible analytics
   <https://developers.italia.it/it/software/italia-software-plausible-a9b3cb>`__
-  `Guida utente di Plausible analytics
   <https://plausible.io/docs>`__
 
