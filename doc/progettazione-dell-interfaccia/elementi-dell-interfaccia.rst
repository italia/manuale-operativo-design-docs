Elementi dell'interfaccia
===========================

L'interfaccia utente (UI) è composta da una serie di contenuti e componenti, interattivi e non, che consentono alle persone di interagire con un prodotto digitale. Questi elementi devono essere progettati in modo tale da facilitare l'uso del prodotto, migliorare l'esperienza d’uso e garantire l'accessibilità per tutte le persone. In questo capitolo, riepiloghiamo i principali elementi che compongono un'interfaccia utente. 

Elementi di composizione
---------------------------
Gli elementi che compongono un'interfaccia utente sono fondamentali per presentare le informazioni in modo chiaro e creare un'esperienza piacevole, che attiri e mantenga l'attenzione.

I principali elementi di composizione sono: 

- il **layout**,  per organizzare gli elementi su pagina e mantenere coerenza ed equilibrio visivo tramite l'uso di griglie;  
- la **palette dei colori**, per definire l’identità visiva del prodotto, garantire la leggibilità dei contenuti e distinguere i diversi elementi dell'interfaccia; 
- la **tipografia**, con la selezione dei font e la gerarchia tipografica, definisce lo stile e la leggibilità del testo, differenziando titoli, sottotitoli e paragrafi;  
- le **icone**, come rappresentazioni grafiche di azioni, funzioni o contenuti, e le loro eventuali alternative o descrizioni accessibili, che devono essere coerenti e facilmente riconoscibili per garantire una comprensione immediata.

La combinazione di questi elementi permette di creare un'interfaccia unica che, da un lato, rispetta l'esigenza di identità del prodotto e, dall'altro, guida le persone al suo utilizzo. 

.. admonition:: Risorse disponibili

   Nei fondamenti del design system .italia trovi tutte le indicazioni pratiche per progettare interfacce semplici e accessibili: `Griglia <https://designers.italia.it/design-system/fondamenti/griglia/>`_, `Spaziature <https://designers.italia.it/design-system/fondamenti/spaziature/>`_, `Ombre <https://designers.italia.it/design-system/fondamenti/ombre/>`_, `Bordi e raggi <https://designers.italia.it/design-system/fondamenti/bordi-e-raggi/>`_, `Dimensioni <https://designers.italia.it/design-system/fondamenti/dimensioni/>`_, `Colori <https://designers.italia.it/design-system/fondamenti/colori/>`_, `Tipografia <https://designers.italia.it/design-system/fondamenti/tipografia/>`_, `Proporzioni media <https://designers.italia.it/design-system/fondamenti/proporzioni-media/>`_, `Icone <https://designers.italia.it/design-system/fondamenti/icone/>`_.
  
Elementi interattivi
------------------------
Gli elementi interattivi di un'interfaccia utente consentono alle persone di interagire direttamente con il prodotto digitale, rendendo l'esperienza d'uso dinamica e coinvolgente. 

**Pulsanti**

I pulsanti, per esempio, sono elementi cliccabili o attivabili che permettono di eseguire azioni specifiche sulla pagina, come "Invia" o "Annulla". Questi devono presentare stati distinti per indicare se sono attivi, disabilitati o in hover. Per garantire l'accessibilità dell'interazione con gli elementi interattivi come i bottoni, gli stati non devono essere comunicati solo mediante elementi visivi, ma anche in modo tale che siano determinabili programmaticamente dalle tecnologie assistive. A tal fine, gestire gli attributi HTML per dichiarare lo stato degli elementi interattivi (ad esempio "checked" per le check box). Solo nel caso in cui non fossero disponibili specifici attributi HTML per definire uno stato, utilizzare gli attributi ARIA appropriati (ad esempio aria-expanded per dichiarare lo stato aperto/chiuso di un accordion).

**Moduli (form)**

I moduli (form) rappresentano un altro elemento chiave: campi di input, checkbox e select a tendina consentono agli utenti di inserire o selezionare dati. Questi devono essere accompagnati da etichette e istruzioni chiare per prevenire confusione, ed essere accompagnati da sistemi di validazione degli errori che ne guidino la risoluzione.

Quando si definiscono le etichette, è importante considerare che vengono utilizzate anche da persone che si avvalgono di tecnologie assistive, sia per la lettura vocale sia per il controllo tramite comandi vocali. Ad esempio, le persone che navigano utilizzando la voce, possono aver necessità di pronunciare il nome di un'etichetta per raggiungere uno specifico campo in un modulo. Pertanto, le etichette devono essere non solo facilmente leggibili visivamente, ma anche chiare e semplici da ascoltare e pronunciare. Ad esempio, un’etichetta composta esclusivamente da consonanti può risultare difficile da comprendere attraverso un lettore vocale e poco riconoscibile per un software di riconoscimento vocale quando pronunciata. Nel caso in cui sia necessario utilizzare etichette di questo tipo (ad esempio, per vincoli legali), è consigliabile integrarle con un nome esteso più facile da ascoltare e pronunciare.

Le istruzioni per l’utilizzo dei form devono essere progettate tenendo conto di diversi scenari d’uso. Ad esempio, durante l’uso in mobilità, alcune parti della pagina potrebbero non essere visibili come su uno schermo di grandi dimensioni. Inoltre, le persone che utilizzano tecnologie assistive, spesso navigano la pagina basandosi sulle relazioni logiche tra gli elementi piuttosto che sulle loro posizioni visive. Per queste ragioni, le istruzioni non devono fare riferimento esclusivamente al contesto visivo, ma devono includere indicazioni che menzionino esplicitamente i nomi degli elementi coinvolti, rendendole comprensibili anche in assenza di riferimenti spaziali. Ad esempio, il messaggio "Per proseguire, clicca sul pulsante rosso in alto a destra" contiene solo riferimenti visivi. Il seguente messaggio include sia caratteristiche visive sia informazioni di testo per individuare l'elemento: "Per proseguire, clicca sul bottone Avanti, in rosso in alto a destra".

**Menu di navigazione**

I menu di navigazione, come le barre di navigazione e le breadcrumb, guidano gli utenti attraverso le varie sezioni del prodotto, facilitando un'esplorazione semplice e intuitiva. 

**Link**

I link permettono di navigare verso altre pagine o risorse e devono essere facilmente identificabili.


Questi elementi rappresentano solo una parte dei componenti interattivi utilizzabili in un'interfaccia. Quando implementati correttamente, con particolare attenzione anche al loro uso con tecnologie assistive, questi elementi non solo rendono l'interfaccia funzionale per tutte le persone, ma anche intuitiva e di facile utilizzo, migliorandone l’efficacia e l'esperienza d’uso.

.. admonition:: Risorse disponibili

   Nel del design system .italia trovi tutti i `componenti <https://designers.italia.it/design-system/componenti/>`_ da usare per creare interfacce semplici e accessibili.


Elementi testuali (microtesti)
-----------------------------------
I microtesti, in inglese microcopy, sono i **testi dell’interfaccia che guidano le persone a navigare siti, app e altre esperienze digitali** nel modo più intuitivo e semplice possibile. Progettare i microtesti come parte integrante dell’interfaccia è fondamentale per creare un prodotto o servizio facile da usare.

I principali tipi di microtesti per le interfacce sono: 

- i **testi di onboarding**, che guidano alla registrazione, al primo accesso a un servizio o al primo uso di una funzionalità; 
- i **messaggi di errore**, che informano le persone di eventuali problemi e come risolverli; 
- i **messaggi di conferma**, che confermano di aver svolto correttamente un’azione; 
- i **tooltip**, i testi che appaiono in sovrimpressione al passaggio del mouse, al tap o all’attivazione da tastiera, che danno maggiori informazioni sulle funzionalità di un prodotto; 
- i **segnaposto nei campi dei form** e i **messaggi di errore durante la loro validazione**, per dare indicazioni chiare su come compilare senza commettere errori; 
- gli **empty state**, ovvero i testi che indicano l’assenza di contenuti, come nei risultati di ricerca; 
- i **messaggi di caricamento**, che spiegano alle persone cosa sta succedendo e perché si è in attesa; 
- le **notifiche** del servizio o prodotto.

.. admonition:: Risorse disponibili

   Approfondisci il tema nel capitolo `Progettazione dei contenuti <../../doc/progettazione-dei-contenuti/scrittura-e-linguaggio.html#microtesti>`_ e nel `fondamento Microtesti <https://designers.italia.it/design-system/fondamenti/microtesti/>`_ del design system .italia.


