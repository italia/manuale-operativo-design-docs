Strumenti di supporto allo sviluppo del software
===================================================

In questo capitolo andremo ad esplorare le risorse essenziali e le buone pratiche che accompagnano ogni fase del ciclo di vita del software, per migliorare la produttività, garantire qualità, coerenza e facilitare la collaborazione tra i membri del team sin dalla realizzazione in un contesto tecnologico sempre più complesso e dinamico.  

Feature detection
-------------------
Gli approcci allo sviluppo possono essere realizzati attraverso la cosiddetta *feature detection (riconoscimento delle caratteristiche)*: il sito web può rilevare una varietà di proprietà che caratterizzano il metodo di accesso al sito da parte del cittadino. 

Attraverso una feature detection puntuale, puoi comprendere come indirizzare ogni aspetto dell’informazione che vuoi trasmettere. Tali caratteristiche possono spaziare dallo schermo utilizzato, in termini di dimensioni, risoluzione e densità dei pixel, fino ai metodi di input (mouse, touch-screen, tastiera, input vocale, ecc.); senza dimenticare le opzioni per la stampa e le tecnologie di ausilio per le persone con disabilità. 

Ad esempio, attraverso semplici *media-queries* nel CSS (attraverso la regola @media), puoi mostrare versioni diverse di una pagina web a seconda che le persone stiano usando uno smartphone, un televisore o vogliano stampare la pagina stessa con la propria stampante::

@media screen and (min-width: 900px) { 
  article { 
    padding: 1rem 3rem; 
  } 
} 



Oppure attraverso la regola @support (in modo simile a quanto avviene per la più conosciuta regola @media), puoi verificare la corretta interpretazione di proprietà CSS da parte dei browser su cui viene usata. Ecco, ad esempio, come puoi verificare attraverso il codice se il browser prevede il supporto della funzionalità CSS grid: 

.. admonition:: example          
   :class: admonition-example display-page          
                                 
   .. role:: admonition-internal-title        
      :class: admonition-internal-title
                                    
   `Esempio di media-queries con la regola @support`:admonition-internal-title:  

   .. code-block:: rst

      @supports (display: flex) { 
        @media screen and (min-width: 900px) { 
          article { 
            display: flex; 
          } 
        } 
      } 


Anche JavaScript ti permette di analizzare qualsiasi funzionalità presente tra le Web API (Application Programming Interface): ad esempio, attraverso la geo-localizzazione di un dispositivo, è possibile fornire un servizio più preciso a seconda della posizione dell’utente nello spazio, a patto che tale feature sia disponibile nel dispositivo utilizzato. Ecco un esempio: 

.. admonition:: example          
   :class: admonition-example display-page          
                                 
   .. role:: admonition-internal-title        
      :class: admonition-internal-title
                                    
   `Esempio di JavaScript per geo-localizzazione`:admonition-internal-title:  

   .. code-block:: rst

      if ("geolocation" in navigator) { 
        /* geolocalizzazione disponibile */ 
      } else { 
       /* geolocalizzazione NON disponibile */ 
      } 


 
Esistono anche librerie ed esempi di codice che hanno l’obiettivo di arginare le differenze tra i vari Browser fornendo il supporto di alcune funzionalità altrimenti mancanti, le cosiddette pratiche di *polyfill* e *shim*. 

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

Misurare le prestazioni
-------------------------
Le prestazioni di un sito o servizio digitale concorrono direttamente a una maggiore facilità d’uso e un’esperienza più soddisfacente per le persone. In questo senso, è bene differenziare due principali ambiti che possono avere impatto determinante sull’esperienza finale: i **tempi di caricamento della pagina** e le **performance di esecuzione della pagina stessa**.

Per analizzare i tempi di caricamento e rendering della pagina puoi utilizzare semplici strumenti online come `Google PageSpeed <https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect>`_ e `WebPagetest.org <https://www.webpagetest.org/>`_. Con questi strumenti, puoi verificare problemi di immediata risoluzione, come l’utilizzo di immagini esageratamente grandi o poco ottimizzate, oppure calibrare altri fattori, come sfruttare al meglio il caching del browser o dare priorità ai contenuti immediatamente visibili.

Per ottenere invece informazioni più dettagliate riguardo eventuali inefficienze di esecuzione del codice a *runtime*, puoi fare riferimento agli strumenti di analisi presenti nei principali browser (`Google Chrome <https://developer.chrome.com/docs/devtools/>`_, `Mozilla Firefox <https://firefox-source-docs.mozilla.org/devtools-user/index.html>`_, `Microsoft Edge <https://learn.microsoft.com/en-us/archive/microsoft-edge/legacy/developer/>`_) i quali possono dare indicazioni su eventuali problemi che avvengono durante la navigazione stessa di una singola pagina.

Chrome developer tools ti fornisce anche un’analisi approfondita di una pagina web nella sua sezione «Audits», permettendo di portare alla luce problemi in ambito di *progressive web apps*, *performance*, *accessibilità*, e *utilizzo di best practices*. 

In caso di progettazione di progressive web apps ideate per essere usate principalmente su dispositivi mobili, è bene tenere a mente anche il concetto di *offline first*, fornendo un’esperienza di base anche in caso di limitata connettività. 
