Approccio allo sviluppo
===========================

In questa sezione andremo ad analizzare le attività preliminari e gli approcci riguardanti lo sviluppo dell’interfaccia. 

Attività preliminari
-----------------------------

Durante le fasi iniziali dello sviluppo, è di fondamentale importanza dedicare tempo e risorse ad alcune attività che avranno impatto sull’intero ciclo di vita del progetto: 

- una **analisi di componenti** (librerie, linguaggi, documentazione, ecc.) e **migliori pratiche** già utilizzate e validate dalla community, che possano semplificare e standardizzare la realizzazione del servizio;
- una **revisione dei requisiti di progetto** con lo scopo di creare un documento di specifiche condiviso, che possa anche definire ruoli e responsabilità;
- la **selezione di una metodologia di sviluppo agile** ottimale per il team di lavoro, con una conseguente definizione precisa delle procedure di comunicazione, di testing e di rilascio cadenzato. 

Contestualmente a questa fase di kick-off tecnico, è preferibile avviare sin da subito una fase di prototipazione avanzata, con la quale iniziare a validare in modo iterativo ogni progresso raggiunto. Questo obiettivo può essere ottenuto sia con classici test manuali, che attraverso un’adeguata *continuous integration* che faccia uso di test automatici.

In caso di applicazioni ad alta interattività o di grandi dimensioni, anche la metodologia di lavoro è fondamentale. Un approccio di *sviluppo guidato dal comportamento* (Behavior-driven development, abbreviato in BDD) per la stesura delle funzionalità e l’uso della stessa metodologia per l’applicazione di test funzionali, “unit test” e test di integrazione, possono essere elementi chiave per il buon funzionamento e la solidità dell’applicazione. 

Web design responsivo e accessibile
------------------------------------------

Il sito web deve sempre essere progettato e sviluppato con un approccio responsive, con l’obiettivo di fornire un’esperienza d’uso ottimale indipendentemente dalla risoluzione dello schermo e dal tipo di dispositivo utilizzato, consentendo in ogni situazione facilità di lettura, interazione e navigazione. 

Al concetto di responsive web design vanno associate pratiche di semplificazione delle interfacce in ottica mobile first, e un’attenzione particolare va messa nel curarne l’accessibilità per fornire un’esperienza soddisfacente a tutte le persone, indipendentemente dalle loro caratteristiche personali, conoscenze o condizioni di disabilità, temporanee o permanenti, o dal loro uso di dispositivi con limitazioni o connessioni lente.

Mobile first
--------------------
L’approccio mobile first consiste nel valutare in prima istanza l’esperienza e le necessità per gli utilizzatori di dispositivi mobili, per poi arricchire di elementi e funzionalità la composizione della pagina mano a mano che la dimensione, le capacità computazionali e di rete del dispositivo aumentano. 

Nell’approccio mobile first si parte dall’essenziale. La forzatura nella progettazione di un’applicazione con ridotte disponibilità di spazio, di interazione, di velocità di caricamento costringe a stabilire delle priorità e a fare delle scelte che risulteranno utili all’usabilità del prodotto.

Progressive enhancement e Graceful degradation 
-----------------------------------------------------
Per *progressive enhancement* si intende una pratica fondante per lo sviluppo di una nuova applicazione web flessibile e a prova di future evoluzioni di dispositivi e browser, con la quale la lavorazione inizia da un nucleo solido e fondamentale di contenuti che vengono via via arricchiti man mano che il dispositivo utilizzato dal cittadino è più performante e all’avanguardia. 

Esiste anche una pratica che si muove in direzione opposta ma con lo stesso fine di rendere il contenuto fruibile su dispositivi con diverse caratteristiche e potenzialità: la *graceful degradation*. Con questo metodo ci si fa carico di verificare che l’interfaccia, inizialmente pensata per i dispositivi più moderni, rimanga navigabile e permetta comunque di accedere alle sue funzioni fondamentali anche attraverso tecnologie meno moderne o interattive. In questo secondo caso, si può pensare anche in termini di tolleranza del sito all’assenza di alcune funzionalità. 
