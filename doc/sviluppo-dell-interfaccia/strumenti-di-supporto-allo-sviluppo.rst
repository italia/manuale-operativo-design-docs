Strumenti di supporto allo sviluppo del software
===================================================

In questo capitolo andremo ad esplorare le risorse essenziali e le buone pratiche che accompagnano ogni fase del ciclo di vita del software, per migliorare la produttività, garantire qualità, coerenza e facilitare la collaborazione tra i membri del team sin dalla realizzazione in un contesto tecnologico sempre più complesso e dinamico.  

Feature detection
-------------------


Verificare le feature disponibili con Can I use
------------------------------------------------

Uno strumento molto utile per una verifica a monte delle feature disponibili nei browser è `caniuse.com <https://caniuse.com/>`_. Questo portale ti permette di ricercare e verificare se per i browser supportati è necessaria una gestione ad-hoc di determinate funzionalità oppure no. 

Una volta individuati i dispositivi supportati e le feature da realizzare, è buona norma scegliere uno stack di sviluppo che ottimizzi il lavoro.


Strumenti e risorse per CSS e JavaScript 
---------------------------------------------
In ambito **CSS**, è ormai pressoché d’obbligo l’utilizzo di pre-processori (`SASS <https://sass-lang.com/>`_, `LESS <https://lesscss.org/>`_, e `PostCSS <https://postcss.org/>`_ sono i più utilizzati), che migliorano la leggibilità e la modularità del codice sorgente, agevolando allo stesso tempo l’applicazione di pratiche virtuose quali l’utilizzo di `Block Element Modifier (BEM) <https://getbem.com/>`_, una metodologia per scrivere classi CSS “parlanti”, o di `Autoprefixer <https://autoprefixer.github.io/>`_ per la gestione automatica di prefissi CSS a supporto dei vari motori di rendering presenti nei browser. 

Per quanto riguarda **Javascript** invece, la scelta degli strumenti è talmente ampia e mutevole che delineare uno scenario ottimale in termini di framework o librerie non avrebbe senso senza un’analisi approfondita del progetto da realizzare. In questo ambito è necessaria una formazione continua, e un’attenzione particolare a ciò che permetta di ottenere codice modulare, scalabile e performante, senza appesantire l’esecuzione e l’interfaccia utente. Alcune risorse interessanti, in inglese, sono `MDN <https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics>`_ e `You don’t know JS <https://www.gitbook.com/?utm_source=legacy&utm_medium=redirect&utm_campaign=close_legacy>`_.

Alcune pratiche sono comunque sempre raccomandabile, come la compressione del codice e il caricamento dei file JavaScript stessi in modo asincrono oppure al termine della pagina HTML, al fine di non bloccare il rendering della pagina stessa; o ancora, l’utilizzo di strumenti di analisi della sintassi come `ESLint <https://eslint.org/>`_ o `StyleLint <https://stylelint.io/>`_ per rendere il codice leggibile e coerente con regole condivise dalla comunità degli sviluppatori.

Supporto browser 
----------------------
Come regola generale, per lo sviluppo di un sito web o servizio digitale per la Pubblica Amministrazione, è necessario assicurare la compatibilità con versioni dei browser che abbiano una penetrazione media tra la popolazione di almeno 1 persona ogni 100 abitanti. A questo proposito, puoiutilizzare come riferimento operativo la `configurazione condivisa Browserslist <https://github.com/italia/browserslist-config-design-italia>`_ dedicata alla Pubblica Amministrazione italiana.

È buona norma inoltre analizzare regolarmente le statistiche d’uso dei dispositivi e delle diverse risoluzioni che gli utenti adoperano per accedere al sito. Per fare questo, puoi avvalerti di diverse sorgenti di dati, tra le quali `StatCounter.com <https://statcounter.com/>`_ che permette di filtrare i dati per paese e ti indica le `versioni browser più usate in Italia <https://gs.statcounter.com/browser-version-market-share/all/italy>`_.
