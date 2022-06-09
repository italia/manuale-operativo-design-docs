# Manuale operativo di design - Designers Italia
Questo repository contiene il testo del *Manuale operativo di design - Designers Italia*, per progettare siti internet e servizi digitali della Pubblica amministrazione, in formato reStructredText.

Il manuale è uno strumento di lavoro per la Pubblica Amministrazione e serve ad orientare la progettazione di ambienti digitali fornendo indicazioni relative al *service design*, alla *user research*, al *content design* e alla *user interface*. Per discutere sul design dei servizi pubblici [è disponibile il nostro forum](https://forum.italia.it/c/design). Per collaborare al manuale è possibile usare gli strumenti descritti di seguito.

## Sviluppo collaborativo
Il manuale è documento pubblico, e chiunque può partecipare al processo di revisione e aggiornamento attraverso gli strumenti messi a disposizione attraverso GitHub, in particolare le [issues](https://guides.github.com/features/issues/) (per le discussioni) e le [pull request](https://help.github.com/articles/about-pull-requests/) (per le proposte di modifica).

I contenuti del manuale sono scritti in file .rst e possono essere aggiornati via GitHub. Qui è disponibile una [guida alla sintassi RST](http://docutils.sourceforge.net/docs/user/rst/quickref.html).

Altre risorse per l'editing in formato .rst sono:
- [Editor per il testo](http://rst.ninjs.org/)
- [Editor per le tabelle](http://truben.no/table/)
- [Estensione Chrome per Google spreadsheet](https://chrome.google.com/webstore/detail/markdowntablemaker/cofkbgfmijanlcdooemafafokhhaeold)
- [Altro](http://docutils.sourceforge.net/docs/user/links.html#editors)

## Version control e release della documentazione
Il manuale beneficia del *version control system* di GitHub, per cui esiste una traccia pubblica di tutte le modifiche effettuate e dei relativi autori.

Il manuale adotta un sistema di release basato sui tag di GitHub. Ogni release è etichettata secondo un sistema basato su anno e versione. Le versioni sono espresse attraverso un numero progressivo. Il sistema delle release è in vigore dal 2022, quindi la prima release delle linee guida è 2022.1 (prima release del 2022).

I nuovi contenuti e le modifiche a contenuti esistenti dopo essere approvati vengono pubblicati nella [versione *latest* del manuale](#), disponibile per una discussione pubblica e revisione da parte della community ma priva di valore ufficiale.

Solo successivamente, in occasione di una nuova release del manuale, il team di Designers Italia decide di consolidarle e farle confluire, dopo eventuali modifiche, nella [versione ufficiale *stable* del manuale](#).

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
[La documentazione è disponibile su **Docs Italia**](#), la piattaforma di gestione della documentazione pubblica creata da [Team per la Trasformazione Digitale](https://teamdigitale.governo.it/).

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

------

_Il presente README.md è in lavorazione e contiene link provvisori o da sostituire_
