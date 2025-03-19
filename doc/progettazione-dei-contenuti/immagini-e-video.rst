Immagini e video
==================
L'accessibilità dei file multimediali è essenziale per garantire che tutti gli utenti, indipendentemente dalle loro abilità, possano fruire dei contenuti web. Immagini e video devono essere presentati in un modo che sia accessibile per persone con disabilità visive, uditive o cognitive.  

Alcune regole generali sono: 

- usa contenuti multimediali **solo se necessario e se aggiungono valore**. Evita di usare, ad esempio, troppe immagini solo per decorazione, poiché renderebbero più pesante il carico cognitivo dell’utente; 
- usa contenuti di **alta qualità con buona risoluzione**. Ad esempio, evita di usare immagini sgranate in cui è difficile capire i dettagli e il contenuto; 
- **evita di utilizzare immagini con testo** in sovrimpressione, poiché non è leggibile dalle tecnologie assistive e potrebbe venir troncato a seconda del dispositivo su cui viene visualizzata l’immagine; 
- **usa i testi alternativi** per descrivere il contenuto e lo scopo delle immagini; 
- **aggiungi sottotitoli** (closed captions) **e trascrizioni** per i video e i contenuti solo audio.

Per approfondire, vai alle `Linee guida per l'accessibilità dei contenuti web (WCAG) <https://www.w3.org/Translations/WCAG22-it/>`_.

Testo alternativo (alt text) per le immagini
------------------------------------------------------
Il testo alternativo è un attributo HTML utilizzato per descrivere il contenuto e lo scopo di un'immagine. È fondamentale per gli utenti che utilizzano screen reader. 

Come scrivere un testo alternativo: 

- descrivi il contenuto chiave dell'immagine in modo conciso e chiaro; 
- evita di iniziare con "Immagine di..." poiché gli screen reader identificano già l'elemento come un'immagine; 
- se l'immagine è puramente decorativa, usa un alt text vuoto (alt="") per far sì che venga ignorata dagli screen reader. 

Esempio: *<img src="foto-cane.jpg" alt="Cane che gioca in un parco al tramonto">*

Sottotitoli per i video
-----------------------------
I sottotitoli (closed captions) sono cruciali per garantire che i video siano accessibili a tutti. Seguire le best practice nella creazione dei sottotitoli assicura che il messaggio del video sia compreso da un pubblico più ampio, anche in condizioni in cui è difficile ascoltare l’audio. 

Come impostare i sottotitoli: 
 
- assicurati che i sottotitoli siano **sincronizzati con l'audio** del video;
- i sottotitoli devono includere non solo i dialoghi, ma anche **descrizioni dei suoni importanti**, come "suono della porta che si chiude";
- includi descrizioni dei suoni significativi tra parentesi, come [suono della porta che si chiude] o [musica drammatica];
- assicurati che i sottotitoli **rimangano sullo schermo abbastanza a lungo** da essere letti comodamente;
- evita di sovraccaricare lo schermo con troppi sottotitoli. **Spezza frasi lunghe in più righe**, idealmente non più di 32 caratteri per riga;
- quando ci sono più persone che parlano, i sottotitoli devono **chiarire chi sta parlando**; 
- **usa la punteggiatura correttamente** per riflettere il tono e il ritmo del discorso; 
- se il video è destinato a un pubblico internazionale, offri sottotitoli in più lingue. Assicurati che le traduzioni siano accurate e mantenere lo stesso tono e contesto dell'originale;
- non inserire i sottotitoli direttamente sulla traccia video, ma **crea un file apposito**, in modo che gli utenti possano accenderli o spegnerli in base alle necessità e per assicurare che siano leggibili su vari tipi di disposititivo. I file di sottotitoli devono essere in **formati standard** per essere compatibili con la maggior parte delle piattaforme video, come **.srt**, **.vtt**, o **.sub**.

Trascrizioni per i video
------------------------------
Le trascrizioni sono documenti testuali separati dal video. Non sono sincronizzate in modo rigido con il tempo del video, anche se possono includere timestamp per riferirsi a specifici momenti del video. Sono utili per chi non può vedere o sentire il video, o per chi preferisce leggere il contenuto per vari motivi, come per scopi di ricerca, revisione o consultazione rapida. 

Come impostare le trascrizioni:

- **trascrivi ogni parola pronunciata** nel video, includendo tutti i dialoghi, monologhi e voci fuori campo; 
- **indica chiaramente chi sta parlando**, soprattutto se ci sono più persone coinvolte;
- **descrivi tutti i suoni non verbali significativi**, come musica, rumori ambientali, risate, applausi, o silenzi importanti. Inserisci questedescrizioni tra parentesi quadre o tonde per differenziarle dal dialogo, indicando anche il tono e l'intensità se rilevanti; 
- **fornisci una descrizione delle azioni visive importanti** che contribuiscono alla narrazione o al contesto del video, come cambiamenti di scena, movimenti dei personaggi, o gesti importanti;
- in trascrizioni lunghe, è utile includi indicazioni temporali per allineare il testo con il momento esatto in cui avviene nel video; 
- fornisci la trascrizione in **formati accessibili**, come file .txt, .pdf, o come testo direttamente inserito in una pagina web; 
- **collega la trascrizione direttamente al video** o includi un link evidente che permetta agli utenti di scaricarla o visualizzarla facilmente. 
