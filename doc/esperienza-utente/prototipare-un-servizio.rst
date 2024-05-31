Prototipare un servizio
=======================

.. include:: /banner.rst

Un **prototipo** è un modello sperimentale che permette di testare un’idea in maniera rapida ed economica, permettendo al team di rifinire il progetto o di valutare cambiamenti di approccio, se si rivelano necessari, prima di investire tempo e denaro nello sviluppo vero e proprio. Uno dei principali vantaggi del processo di prototipazione consiste nella possibilità di effettuare delle sessioni di validazione dell’esperienza e del *concept* già nelle prime fasi della progettazione, mantenendo gli utenti al centro del processo di *design*. 

Un prototipo aiuta a coinvolgere gli *stakeholder* fin dall'inizio, mostrando le soluzione proposte dal team per risolvere le necessità degli utenti e raggiungere gli obiettivi del progetto. Inoltre, un prototipo rende più semplice valutare l'effetto tecnologico, evidenziando limiti o opportunità tecnologiche.

Nella prima fase il **prototipo** è **low-fi (low fidelity)**, a bassa fedeltà. Questo tipo di manufatto ha diversi vantaggi:

-  **aiuta il designer a elaborare il modello d’interazione** a supporto dell’esperienza desiderata, verificando le proprie scelte direttamente “in pagina”;
-  **favorisce l’iterazione**, permettendo al designer di rielaborare in tempi ridotti i feedback ricevuti da altri membri del team o dagli stakeholder in tempi ridotti;
-  **elimina potenziali distrazioni** derivanti da elementi grafici e contenuti dettagliati, dando quindi la possibilità di concentrarsi solamente sulle funzionalità e i flussi.

La prototipazione **hi-fi (high fidelity)** interviene in un secondo momento, quando l’organizzazione semantica e i flussi d’interazione sono stati validati grazie al prototipo *low-fi* ed è possibile progredire nella progettazione delle schermate inserendo gli elementi d’interfaccia. Il prototipo *hi-fi* prevede la definizione precisa di tutti gli elementi di interfaccia utente e design dei contenuti, lavorando in tre direzioni: 

-  **alimenta il processo di condivisione** con gli *stakeholder* e gli altri membri della squadra di progetto;
-  consente di **indirizzare e documentare il lavoro di sviluppo front-end** del servizio digitale, facilitando la collaborazione di designer e developers;
-  permette di **validare l’interfaccia e le scelte progettuali** attraverso sessioni di test di usabilità con utenti finali. 


I wireframe
-----------

Un *wireframe* è una illustrazione dell’interfaccia di una pagina, che ha come obiettivi:

- organizzare gli elementi interattivi e i blocchi di contenuto nello spazio disponibile sullo schermo;
- evidenziare le funzionalità disponibili;
- mostrare la sequenza di passaggi (flusso di interazione) che l’utente deve fare per concludere un processo. 

Date queste priorità, i *wireframe* non comprendono stili, colore o grafica, motivo per cui possono essere definiti prototipi a bassa definizione. 

.. figure:: media/image2.png
    :alt: Un esempio di “wireframe”, o prototipo a “bassa fedeltà”
    :name: Un esempio di “wireframe”, o prototipo a “bassa fedeltà”

*Figura 1 - Un esempio di “wireframe”, o prototipo a “bassa fedeltà”.*

La finalità di condurre progressivamente l’utente al raggiungimento dei propri obiettivim - mettendo in evidenza le relazioni tra i contenuti e i flussi di interazione - è assolta in modo specifico dai **prototipi interattivi**: questi sono sequenze di *wireframe*, connessi fra loro attraverso link e menu di navigazione che permettono di **simulare il percorso interattivo dell’utente**. 

.. figure:: media/image3.jpg
    :alt: Wireframe interattivo (user flow) per il rinnovo della carta di identità:
    :name: Wireframe interattivo (user flow) per il rinnovo della carta di identità:

    *Figura 2*

    *Wireframe interattivo (user flow) per il rinnovo della carta di
    identità:*

1. Entro sul sito dedicato al rinnovo della carta d’identità

2. Seleziono la richiesta di rinnovo

3. Seleziono il Comune di appartenenza

4. Scelgo una data e ora tra quelle disponibili nel calendario

5. Ricevo conferma della prenotazione dell’appuntamento

La prototipazione attraverso *wireframe* fa largo utilizzo di *pattern*, ovvero di modelli di rappresentazione dei contenuti e forme di interazione standard nel mondo web. 

Il kit Prototipazione
~~~~~~~~~~~~~~~~~~~~~

Il  `kit Prototipazione <https://designers.italia.it/kit/prototipazione/>`__ di Designers Italia, offre una serie di *pattern* che definiscono alcuni modelli di contenuto e forme di interazione tipiche dei siti e servizi della Pubblica amministrazione italiana e che facilitano il processo di prototipazione di un servizio, offrendo una solida base da cui partire. 
Esempi di *pattern* sono il *content type* “scheda servizio”, che definisce il modello di presentazione di un servizio pubblico, oppure le modalità di interrogazione di un motore di ricerca. 

.. figure:: media/image5.png
    :alt: Tipi di content  type presenti nel wireframe kit
    :name: Tipi di content  type presenti nel wireframe kit

    *Figura 3 - Tipi di content type presenti nel kit Prototipazione*
    
.. figure:: media/image4.png
    :alt: Pattern di ricerca: user flow
    :name: Pattern di ricerca: user flow

    *Figura 4 - Pattern di ricerca: user flow*
    
I modelli di pagina e di interazione sono costruiti attraverso una libreria di componenti rappresentati da pulsanti, campi di input, blocchi di testo, ecc. I componenti sono “i mattoncini” attraverso cui si costruiscono le interfacce, gli elementi base della grammatica che regola l’interazione tra l’utente e il sistema. 

.. figure:: media/ui-wireframe-kit-esempio-animato.gif
    :alt: UI Wireframe kit Esempio animato
    :name: UI Wireframe kit Esempio animato

    *Figura 5 - Un esempio di composizione dei componenti del kit Prototipazione per creare o adattare un content type alle esigenze del prototipo. Il software scelto per costruire il Wireframe Kit è* `Sketch <https://www.sketchapp.com/>`__ *, uno strumento che
    permette la gestione dinamica dei simboli e la condivisione della libreria in modo trasversale a tutti i file su cui si intende         lavorare. Sketch permette di cambiare le caratteristiche dei singoli elementi e personalizzarli in modo rapido e intuitivo.*
    *Alternativamente, è possibile importare il file Sketch in altri programmi di prototipazione, come* `Adobe XD                           <https://www.adobe.com/it/products/xd.html>`__ *,* `Studio <https://studio.design/>`__ *,
    o* `Figma <https://www.figma.com/>`__ *.*
    
Nella risorsa **kit wireframe** all'interno del kit dedicato alla prototipazione, il focus è sulle tipologie di componenti e non sulle loro caratteristiche specifiche, che saranno oggetto di definizione nella successiva fase di prototipazione ad alta fedeltà. 

Per costruire un *wireframe* si possono usare diversi metodi: oltre ai numerosi software specifici presenti sul mercato, da cui utilizzare la libreria di Designers Italia, è possibile realizzarli anche in modo analogico, facendo semplici disegni o utilizzando il `kit per i wireframe di carta <https://drive.google.com/file/d/1wdb4JWlcJRYum2LpnllFy2zlxx2EptYx/view>`__\. 
Per progettare la sequenza delle schermate di un sito o di una app utilizzando il queste risorse, sarà quindi sufficiente scegliere e assemblare i componenti e i pattern di cui il kit è composto. 

Il kit è realizzato con il software Sketch, ma può essere esportato e utilizzato con altri software di prototipazione; è pubblicato su Github, una piattaforma che permette di visionare tutte le fasi di progettazione e sviluppo grazie al controllo di versione.

Una volta costruito, testato e migliorato il prototipo a bassa fedeltà, si può passare quindi alla **realizzazione di un prototipo ad alta fedeltà** per agevolare la comprensione e la condivisione del progetto, realizzare test di usabilità e facilitare l’avvio della fase di sviluppo.

A supporto della realizzazione del prototipo ad alta fedeltà, è possibile utilizzare le seguenti risorse: 

- la sezione del manuale operativo di design relativa alla **progettazione dell’interfaccia utente e all’architettura dell’informazione**; 
- il `kit Progettazione interfaccia <https://designers.italia.it/kit/progettazione-interfaccia/>`__ di Designers Italia, un set di componenti visive già pronte per assemblare l’interfaccia di un sito o di un’app; 
- la sezione del manuale operativo relativa al **content design** e il `kit Contenuti e linguaggio <https://designers.italia.it/kit/contenuti-linguaggio/>`__\. 
