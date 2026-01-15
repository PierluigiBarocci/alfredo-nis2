# User Stories - Gestione Criteri di Valutazione

**Epica**: Framework
**Macro-argomento**: Gestione Criteri di Valutazione (Anagrafica)
**Data**: 2025-12-11
**Versione**: 1.0

---

## Indice User Stories

- [US-FWK-006] Visualizzare lista criteri di valutazione (Admin)
- [US-FWK-007] Creare nuovo criterio di valutazione - Campo Libero o Scala (Admin)
- [US-FWK-008] Visualizzare dettaglio criterio di valutazione (Admin)
- [US-FWK-009] Modificare criterio di valutazione (Admin)
- [US-FWK-010] Eliminare criterio di valutazione con validazione vincoli (Admin)

---

## US-FWK-006 - Visualizzare lista criteri di valutazione (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare la lista completa dei criteri di valutazione
**In modo che** possa avere una panoramica di tutti i criteri disponibili e accedere rapidamente ai loro dettagli

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla sezione "Criteri di valutazione" dal menu principale
**Allora** il sistema deve mostrare:

1. **Pagina lista criteri di valutazione** con:

   - Titolo pagina: "Criteri di valutazione"
   - Breadcrumb: "Criteri di valutazione"
   - Pulsante "Nuovo criterio" (arancione, top-right)
   - Filtri (Nome, Tipo)
   - Tabella paginata con le seguenti colonne (fisse):

     - **Nome** (Nome criterio, sortable)
     - **Descrizione** (Descrizione criterio, sortable)
     - **Tipo** (Badge: "Campo Libero" o "Scala", sortable)
     - **Data creazione** (Data creazione formato DD/MM/YYYY, sortable)
     - **Azioni** (Menu contestuale: Dettaglio, Modifica, Elimina)

2. **Badge tipo criterio**:

   - **Campo Libero**: badge grigio "Campo Libero"
   - **Scala**: badge blu "Scala"

3. **Paginazione**:

   - Rows per page: 10 (default), con opzioni 10/25/50
   - Indicatore "X-Y di Z" (es. "1-4 di 4")
   - Frecce navigazione prev/next

4. **Comportamento click su riga**:

   - Click su icona menu (tre puntini): mostra dropdown con opzioni:
     - Dettaglio (icona occhio)
     - Modifica (icona matita)
     - Elimina (icona cestino, colore arancione)

5. **Stato vuoto**:

   - Se non ci sono criteri: mostrare messaggio "Nessun criterio di valutazione registrato" + pulsante "Crea primo criterio"

### Edge Cases

- **Nessun risultato filtro**: Se il filtro non restituisce risultati, mostrare "Nessun risultato trovato. Modifica il filtro di ricerca."
- **Errore caricamento dati**: Mostrare notifica di errore "Impossibile caricare i criteri di valutazione. Riprova."
- **Ordinamento default**: Ordinamento default per "Data creazione" decrescente (più recenti prima)

### Dipendenze

- Nessuna

---

## US-FWK-007 - Creare nuovo criterio di valutazione - Campo Libero o Scala (Admin)

**Come** Admin di piattaforma
**Voglio** creare un nuovo criterio di valutazione scegliendo tra Campo Libero e Scala
**In modo che** possa definire criteri di valutazione flessibili da associare ai framework

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Nuovo criterio" dalla lista criteri di valutazione
**Allora** il sistema deve mostrare:

1. **Pagina creazione** con:
   - Titolo: "Nuovo"
   - Breadcrumb: "Criteri di valutazione > Nuovo"
   - Form con sezioni:

#### SEZIONE 1: Informazioni Base

| Campo         | Tipo     | Label              | Validazione   | Required |
| ------------- | -------- | ------------------ | ------------- | -------- |
| nome_elemento | Text     | Nome criterio      | Max 255 char  | Si       |
| descrizione   | Textarea | Descrizione estesa | Max 1000 char | No       |

#### SEZIONE 2: Tipo Criterio (Radio Button - Scelta Obbligatoria)

**Label sezione**: "Tipo criterio di valutazione"

**Radio button options**:

- **Campo Libero** (default selezionato)
- **Scala**

**Nota informativa**:
"Scegli il tipo di criterio di valutazione. Campo Libero permette inserimento testo libero, Scala definisce valori numerici predefiniti."

### Comportamento Radio Button "Campo Libero"

**Quando** seleziono "Campo Libero"
**Allora** il sistema mostra:

**Campi aggiuntivi**:

| Campo         | Tipo   | Label                         | Validazione | Required |
| ------------- | ------ | ----------------------------- | ----------- | -------- |
| max_lunghezza | Number | Lunghezza massima (caratteri) | Integer > 0 | No       |

**Placeholder**:

- nome_elemento: "es: Note aggiuntive, Commento valutatore"
- max_lunghezza: "es: 500"

**Nota informativa sotto i campi**:
"Se non specifichi una lunghezza massima, il campo accettera testo illimitato."

### Comportamento Radio Button "Scala"

**Quando** seleziono "Scala"
**Allora** il sistema mostra:

**Campi dinamici per coppie Valore-Label**:

1. **Header sezione**: "Definisci i valori della scala"
2. **Pulsante**: "+ Aggiungi coppia" (grigio chiaro)
3. **Blocchi ripetibili** (minimo 2 coppie richieste):

| Campo           | Tipo   | Label           | Validazione                               | Required |
| --------------- | ------ | --------------- | ----------------------------------------- | -------- |
| valore_numerico | Number | Valore numerico | Decimal (2 decimali), univoco nella scala | Si       |
| label_associata | Text   | Label associata | Max 100 char                              | Si       |

**Ogni blocco coppia ha**:

- Icona "X" (top-right) per rimuovere il blocco (disabilitato se solo 2 coppie rimaste)
- Layout: 2 campi affiancati (Valore numerico | Label associata)

**Placeholder**:

- valore_numerico: "es: 0.0"
- label_associata: "es: Non conforme"

**Nota informativa sotto i campi**:
"Inserisci almeno 2 coppie. I valori numerici devono essere univoci e rappresentano il punteggio assegnabile."

**Validazione coppie Scala**:

- Almeno 2 coppie obbligatorie
- Valori numerici univoci all'interno della stessa scala
- Ordinamento automatico dei valori in ordine crescente (visivamente nella lista)

2. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna alla lista senza salvare
   - **Salva** (blu): valida e salva

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare campi base**:

   - Nome criterio obbligatorio
   - Tipo criterio selezionato

2. **Se tipo = Campo Libero**:

   - Validare "nome_campo" obbligatorio
   - Se "max_lunghezza" presente: validare > 0

3. **Se tipo = Scala**:

   - Validare almeno 2 coppie Valore-Label presenti
   - Validare valori numerici univoci
   - Validare tutti i campi obbligatori delle coppie

4. **Validare univocita nome criterio**:

   - Se nome gia esistente: mostrare errore "Nome criterio gia esistente. Utilizza un nome diverso."

5. **Se validazione OK**:
   - Creare record criterio di valutazione
   - Se tipo=Scala: salvare coppie in tabella relazionata
   - Mostrare notifica di successo: "Criterio di valutazione creato con successo"
   - Redirect a pagina dettaglio criterio appena creato (US-FWK-008)

### Edge Cases

- **Nome duplicato**: "Nome criterio gia esistente. Utilizza un nome diverso."
- **Scala con < 2 coppie**: "Inserisci almeno 2 coppie di valori per la scala."
- **Valori scala duplicati**: "I valori numerici devono essere univoci. Valore [X] e duplicato."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."

### Dipendenze

- US-FWK-006 (lista criteri di valutazione)

---

## US-FWK-008 - Visualizzare dettaglio criterio di valutazione (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare tutti i dettagli di un criterio di valutazione
**In modo che** possa consultare le informazioni complete in modalita sola lettura

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su un criterio dalla lista o dal menu contestuale "Dettaglio"
**Allora** il sistema deve mostrare:

1. **Pagina dettaglio** con:

   - Titolo: "Dettaglio"
   - Breadcrumb: "Criteri di valutazione > Dettaglio"

2. **Sezione "Informazioni Elemento"** (read-only):

**Layout**: Form a colonna singola (campi disabilitati)

### Se tipo = Campo Libero

| Campo         | Label             | Formato Display                     |
| ------------- | ----------------- | ----------------------------------- |
| nome_elemento | Nome criterio     | Text (disabilitato)                 |
| tipo_elemento | Tipo criterio     | Badge grigio "Campo Libero"         |
| nome_campo    | Nome campo        | Text (disabilitato)                 |
| max_lunghezza | Lunghezza massima | Number (disabilitato) o "-" se null |

### Se tipo = Scala

| Campo         | Label         | Formato Display                           |
| ------------- | ------------- | ----------------------------------------- |
| nome_elemento | Nome criterio | Text (disabilitato)                       |
| tipo_elemento | Tipo criterio | Badge blu "Scala"                         |
| valori_scala  | Valori scala  | Tabella read-only con coppie (vedi sotto) |

**Tabella "Valori scala"** (se tipo=Scala):

| Valore numerico | Label associata       |
| --------------- | --------------------- |
| 0.0             | Non conforme          |
| 0.5             | Parzialmente conforme |
| 1.0             | Conforme              |

- Ordinamento: per valore numerico crescente
- Colonne: non sortable (tabella read-only)

**Pulsante azione** (bottom-right):

3. **Sezione "Utilizzo"** (informativa):
   - Contatore: "Utilizzato in X framework"
   - Se X > 0: link "Visualizza framework" che apre lista framework filtrata per questo criterio
   - Se X = 0: messaggio "Non ancora utilizzato in nessun framework"

### Edge Cases

- **Errore caricamento**: Mostrare notifica "Impossibile caricare i dettagli. Riprova."
- **Elemento eliminato**: Se criterio non esiste piu, redirect a lista con messaggio "Elemento non trovato"

### Dipendenze

- US-FWK-006 (lista criteri)
- US-FWK-007 (creazione criterio)

---

## US-FWK-009 - Modificare criterio di valutazione (Admin)

**Come** Admin di piattaforma
**Voglio** modificare i dati di un criterio di valutazione
**In modo che** possa aggiornare le informazioni quando necessario

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Modifica" dalla pagina dettaglio o dal menu contestuale
**Allora** il sistema deve mostrare:

1. **Pagina modifica** con:

   - Titolo: "Modifica"
   - Breadcrumb: "Criteri di valutazione > Dettaglio > Modifica"
   - Form con gli stessi campi di creazione (US-FWK-007), pre-compilati con i valori attuali

2. **Campi modificabili**:

| Campo         | Modificabile | Note                                         |
| ------------- | ------------ | -------------------------------------------- |
| nome_elemento | SI           | Validazione univocita                        |
| tipo_elemento | NO           | Radio button disabilitato (non modificabile) |
| descrizione   | SI           | Non è required                               |
| max_lunghezza | SI           | Solo se tipo=Campo Libero                    |
| valori_scala  | SI           | Solo se tipo=Scala (vedi sotto)              |

**Nota importante**:
"Il tipo di criterio (Campo Libero / Scala) non puo essere modificato dopo la creazione."

### Modifica Valori Scala (se tipo=Scala)

**Comportamento**:

- Tabella coppie esistenti pre-popolata
- Pulsante "+ Aggiungi coppia" attivo
- Ogni coppia ha icona "X" per eliminazione (minimo 2 coppie richieste)
- Validazione: valori numerici univoci

**Operazioni consentite**:

- Modificare valore numerico o label di coppie esistenti
- Aggiungere nuove coppie
- Eliminare coppie (se > 2 coppie totali)

3. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna al dettaglio senza salvare
   - **Salva** (blu): valida e salva modifiche

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare tutti i campi** (stesse regole di creazione US-FWK-007)

2. **Validare univocita nome criterio**:

   - Se nome gia esistente (escludendo se stesso): mostrare errore "Nome criterio gia esistente. Utilizza un nome diverso."

3. **Se tipo=Scala**:

   - Validare almeno 2 coppie presenti
   - Validare valori numerici univoci

4. **Se validazione OK**:
   - Aggiornare record criterio di valutazione
   - Se tipo=Scala: aggiornare/inserire/eliminare coppie in tabella relazionata
   - Aggiornare timestamp `modificato_il`
   - Mostrare notifica di successo: "Modifiche salvate con successo"
   - Redirect a pagina dettaglio (US-FWK-008)

### Edge Cases

- **Nessuna modifica**: Se clicco "Salva" senza modificare nulla, salvare comunque e aggiornare `modificato_il`
- **Nome duplicato** (se modificato): "Nome criterio gia esistente. Utilizza un nome diverso."
- **Eliminazione coppia Scala sotto minimo**: "Devi mantenere almeno 2 coppie di valori per la scala."
- **Valori scala duplicati**: "I valori numerici devono essere univoci. Valore [X] e duplicato."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."

### Dipendenze

- US-FWK-008 (dettaglio criterio)

---

## US-FWK-010 - Eliminare criterio di valutazione con validazione vincoli (Admin)

**Come** Admin di piattaforma
**Voglio** eliminare un criterio di valutazione rispettando i vincoli di business
**In modo che** non vengano eliminati criteri associati a framework esistenti senza warning

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Elimina" dal menu contestuale di un criterio (lista o dettaglio)
**Allora** il sistema deve:

1. **Verificare utilizzo in framework**:

   - Controllare se l'criterio e associato a framework esistenti
   - Se SI: Mostrare dialog di WARNING (non blocco hard)

2. **Mostrare dialog di warning se criterio utilizzato**:

   ```
   Attenzione!
   L'criterio di valutazione "[Nome Elemento]" e utilizzato nei seguenti framework:

   - [Nome Framework 1]
   - [Nome Framework 2]
   - [Nome Framework 3]
   ... (max 5 framework mostrati, se > 5 mostrare "e altri X framework")

   Eliminando questo criterio:
   - I framework esistenti non potranno piu utilizzarlo per le valutazioni
   - Gli audit gia creati con questi framework mantengono i valori gia inseriti
   - Non sara piu disponibile per future associazioni

   Sei sicuro di voler procedere?

   [Annulla] [Conferma eliminazione]
   ```

3. **Se NON utilizzato**, mostrare dialog di conferma standard:

   ```
   Conferma eliminazione criterio di valutazione

   Sei sicuro di voler eliminare l'criterio "[Nome Elemento]"?

   Questa operazione NON e reversibile.

   [Annulla] [Conferma eliminazione]
   ```

4. **Se conferma eliminazione**:
   - Eliminare record criterio di valutazione
   - Se tipo=Scala: eliminare anche tutte le coppie Valore-Label associate (cascade delete)
   - Mostrare notifica: "Criterio di valutazione eliminato con successo"
   - Redirect a lista criteri di valutazione (US-FWK-006)

### Edge Cases

- **Elemento utilizzato in molti framework**: Mostrare max 5 framework nel dialog + contatore "e altri X"
- **Errore eliminazione**: "Errore durante l'eliminazione. Riprova."
- **Elemento gia eliminato**: Se nel frattempo e stato eliminato, mostrare "Elemento non trovato" e refresh lista

### Vincoli di Business

- **WARNING (non blocco)**: L'Admin puo eliminare criteri anche se utilizzati (dopo conferma warning)
- **Cascade delete**: Se tipo=Scala, eliminare anche tutte le coppie associate
- **Framework orfani**: I framework che utilizzavano l'criterio eliminato mantengono l'associazione ma con riferimento "null" (gestione graceful degradation) e passano automaticamente in stato "Bozza"

### Dipendenze

- US-FWK-006 (lista criteri)
- US-FWK-008 (dettaglio criterio)

---

## Riepilogo User Stories - Gestione Criteri di Valutazione

| ID         | Titolo                                       | Complessita | Priorita |
| ---------- | -------------------------------------------- | ----------- | -------- |
| US-FWK-006 | Visualizzare lista criteri di valutazione    | L           | MUST     |
| US-FWK-007 | Creare nuovo criterio - Campo Libero o Scala | H           | MUST     |
| US-FWK-008 | Visualizzare dettaglio criterio              | M           | MUST     |
| US-FWK-009 | Modificare criterio                          | H           | MUST     |
| US-FWK-010 | Eliminare criterio con validazione           | M           | MUST     |

**Legenda Complessita**:

- L (Low): 1-2 giorni
- M (Medium): 3-5 giorni
- H (High): 5-8 giorni

**Legenda Priorita**:

- MUST: Funzionalita core, necessaria per MVP
- SHOULD: Funzionalita importante, migliora UX
- COULD: Funzionalita nice-to-have, differibile

---

## Note Tecniche per Sviluppo

### Validazioni Comuni

1. **Nome criterio**: Max 255 char + univocita (case-insensitive)
2. **Nome campo** (Campo Libero): Max 100 char
3. **Max lunghezza** (Campo Libero): Integer > 0 (optional)
4. **Valore numerico** (Scala): Decimal (2 decimali) + univocita nella stessa scala
5. **Label associata** (Scala): Max 100 char
6. **Coppie Scala**: Minimo 2 coppie obbligatorie

### Pattern UI Comuni

1. **Form layout**: 1 colonna responsive
2. **Radio button**: Scelta obbligatoria con campi condizionali
3. **Blocchi ripetibili**: + Aggiungi coppia con icona X per eliminazione (minimo 2)
4. **Pulsanti azione**: Sempre bottom-right (Annulla + Azione primaria)
5. **Notifiche**: Toast top-right, auto-dismiss 5s
6. **Dialog conferma**: Modale centrato, overlay scuro 50%
7. **Menu contestuale**: Dropdown aligned right, 3 puntini verticali

### Regole di Visibilita

1. **Admin**: CRUD completo
2. **Consulenti**: NO accesso alla lista criteri (vedono solo nel multi-select Framework)
3. **Elementi globali**: Condivisi tra tutti i framework

### Gestione Tipo Elemento

1. **Tipo non modificabile**: Una volta creato, il tipo (Campo Libero / Scala) non puo essere cambiato
2. **Cambio tipo in creazione**: Warning con perdita dati sezione precedente
3. **Campi condizionali**: Mostrare/nascondere sezioni in base al tipo selezionato

### Gestione Coppie Scala

1. **Ordinamento automatico**: Le coppie vengono sempre mostrate ordinate per valore numerico crescente
2. **Minimo 2 coppie**: Icona X disabilitata se solo 2 coppie rimangono
3. **Univocita valori**: Validazione server-side + client-side per valori duplicati
4. **Cascade delete**: Eliminando criterio tipo=Scala, eliminare tutte le coppie associate

### Gestione Eliminazione

1. **Hard delete**: Record eliminato definitivamente (criterio + coppie)
2. **Warning utilizzo**: Dialog informativo ma NON bloccante
3. **Graceful degradation**: Framework con criterio eliminato mostrano placeholder "Elemento non disponibile"

---

**Fine User Stories - Gestione Criteri di Valutazione**
