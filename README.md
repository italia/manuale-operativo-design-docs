# Manuale operativo di design - Designers Italia
Questo repository contiene il testo del *Manuale operativo di design - Designers Italia*, per progettare siti internet e servizi digitali della Pubblica amministrazione, in formato reStructredText.

Il manuale è uno strumento di lavoro per la Pubblica Amministrazione e serve ad orientare la progettazione di ambienti digitali fornendo indicazioni relative al *service design*, alla *user research*, al *content design* e alla *user interface*. Per discutere sul design dei servizi pubblici [è disponibile il nostro forum](https://forum.italia.it/c/design). Per collaborare al manuale è possibile usare gli strumenti descritti di seguito.

## Sviluppo collaborativo
Il presente manuale è un documento pubblico e chiunque può partecipare al processo di revisione e aggiornamento attraverso gli strumenti messi a disposizione attraverso l'apposito `repository GitHub <https://github.com/italia/manuale-operativo-design-docs/>`_. Per poter contribuire, devi `accedere con un account GitHub <https://github.com/login>`_.

Per **lasciare commenti e suggerimenti generali**, puoi `aprire una nuova issue <https://github.com/italia/manuale-operativo-design-docs/issues>`_.

Per **proporre modifiche specifiche** al manuale, puoi usare la funzione `pull request <https://help.github.com/articles/about-pull-requests/>`_:

1. vai alla pagina del manuale su cui vuoi proporre delle modifiche;
2. clicca sul collegamento “Sorgente” (presente in alto a destra su ogni pagina, nell’header);
3. edita il file con le modifiche che vuoi proporre, usando la `sintassi RST <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ e ponendo attenzione alla gerarchia dei contenuti e le indentazioni;
4. invia una una richiesta di contribuzione (pull request) verso il repository che contiene il sorgente del manuale.

I contenuti del manuale e i contributi di modifica devono essere redatti usando la **sintassi RST**. Ecco alcune risorse utili:

- `Guida alla sintassi RST <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.
- `Editor per il testo <https://rsted.info.ucl.ac.be/>`_
- `Editor per le tabelle <http://truben.no/table/>`_
- `Altre informazioni sugli editor RSR <http://docutils.sourceforge.net/docs/user/links.html#editors>`_

I nuovi contenuti e le modifiche a contenuti esistenti vengono valutati dal team di Designers Italia e integrati, se necessario con modifiche, nella versione corrente del manuale.

## Stile della documentazione
Il manuale è scritto seguendo la [style guide di redazione dei testi pubblici](#). In particolare:
- linguaggio semplice e comprensibile ad un pubblico ampio
- brevità e uso di elenchi
- ricorso ad esempi, meglio se supportati da immagini e link

Nella guida usiamo delle etichette per evidenziare alcuni passaggi, specificando se l'applicazione della indicazione è obbligatoria o facoltativa, come segue
- si deve (devi)
- si può (puoi)
- si dovrebbe (dovresti)
- best practice

## Consultazione della documentazione
**[Il Manuale operativo è disponibile su Docs Italia](https://docs.italia.it/italia/designers-italia/manuale-operativo-design-docs)**.

Le funzioni di hosting e di ricerca sono basate su [ReadTheDocs](https://readthedocs.org/) e la documentazione viene pubblicata attraverso il tool [Sphinx](http://www.sphinx-doc.org/en/stable/) e il linguaggio [RST](http://docutils.sourceforge.net/rst.html).

Tutti i documenti di *Docs Italia* possono essere fruiti anche in formato .epub e .pdf


## Dipendenze

Il repository è strutturato per essere compatibile con [Docs Italia](https://docs.italia.it/).
La piattaforma accetta documenti in formato RST o MD.
Per informazioni sulla struttura di questo repository visita il [repository
dedicato](https://github.com/italia/docs-italia-starter-kit).

## Preview

Per lavorare utilizzando una preview del documento è sufficiente lanciare Docker

```shell
docker-compose up
```

la preview sarà visibile all'indirizzo [http://localhost:8000/](http://localhost:8000/)

## Come contribuire

Ogni contributo è benvenuto!
È possibile aprire delle issue per segnalare errori, problemi o per la richiesta di nuove funzionalità.
Inoltre, è possibile aprire delle Pull Request per proporre direttamente delle modifiche.

## Licenza

Questo documento è rilasciato con una licenza CC BY 4.0.
