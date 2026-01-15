# User Stories - Gestione Template Framework

**Epica**: Framework
**Macro-argomento**: Gestione Template Framework (con righe e stati)
**Data**: 2025-12-11
**Versione**: 1.0

---

## Indice User Stories

- [US-FWK-011] Visualizzare lista template framework (Admin)
- [US-FWK-012] Creare nuovo framework con righe e elementi di valutazione (Admin)
- [US-FWK-013] Gestire righe framework - Aggiungi/Modifica/Elimina in tabella anteprima (Admin)
- [US-FWK-014] Gestire freesolo con eliminazione suggerimenti tramite icona X (Admin)
- [US-FWK-015] Visualizzare dettaglio framework in modalita sola lettura (Admin)
- [US-FWK-016] Modificare framework esistente (Admin)
- [US-FWK-017] Pubblicare framework - cambio stato Bozza → Pubblicato (Admin)
- [US-FWK-018] Eliminare/Archiviare framework con validazione vincoli (Admin)

---

## US-FWK-011 - Visualizzare lista template framework (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare la lista completa dei template framework
**In modo che** possa avere una panoramica di tutti i framework disponibili e accedere rapidamente ai loro dettagli

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla sezione "Template framework" dal menu principale
**Allora** il sistema deve mostrare:

1. **Pagina lista template framework** con:
   - Titolo pagina: "Template framework"
   - Breadcrumb: "Template framework"
   - Pulsante "Nuova framework" (arancione, top-right)
   - Dropdown filtro per framework (placeholder: "Framework")
   - Tabella paginata con le seguenti colonne (fisse):
     - **Nome** (Nome framework, sortable, click apre dettaglio)
     - **Stato** (Badge colorato, sortable)
     - **N. righe** (Contatore righe framework, sortable)
     - **Elementi valutazione** (Numero elementi associati, sortable)
     - **Data creazione** (Data creazione formato DD/MM/YYYY, sortable)
     - **Azioni** (Menu contestuale: Dettaglio, Modifica, Pubblica, Elimina)

2. **Badge stato framework**:
   - **Bozza**: badge grigio "Bozza"
   - **Pubblicato**: badge verde "Pubblicato"
   - **Archiviato**: badge arancione "Archiviato"

3. **Paginazione**:
   - Rows per page: 8 (default), con opzioni 8/16/24
   - Indicatore "X of Y" (es. "8 of 25")
   - Frecce navigazione prev/next

4. **Comportamento click su riga**:
   - Click su nome framework: apre pagina dettaglio (US-FWK-015)
   - Click su icona menu (tre puntini): mostra dropdown con opzioni:
     - Dettaglio (icona occhio)
     - Modifica (icona matita)
     - **Pubblica** (icona check, solo se stato=Bozza e righe > 0)
     - **Archivia** (icona archivio, solo se stato=Pubblicato)
     - Elimina (icona cestino, colore arancione)

5. **Stato vuoto**:
   - Se non ci sono framework: mostrare messaggio "Nessun template framework registrato" + pulsante "Crea primo framework"

6. **Filtro ricerca**:
   - Dropdown con lista framework esistenti
   - Filtra per nome framework esatto
   - Opzione "Tutti" per reset filtro

### Edge Cases

- **Nessun risultato filtro**: Se il filtro non restituisce risultati, mostrare "Nessun risultato trovato. Modifica il filtro di ricerca."
- **Errore caricamento dati**: Mostrare notifica di errore "Impossibile caricare i template framework. Riprova."
- **Ordinamento default**: Ordinamento default per "Data creazione" decrescente (più recenti prima)
- **Framework con 0 righe**: Mostrare "0" nella colonna "N. righe" e disabilitare azione "Pubblica"

### Dipendenze
- Nessuna

---

## US-FWK-012 - Creare nuovo framework con righe e elementi di valutazione (Admin)

**Come** Admin di piattaforma
**Voglio** creare un nuovo framework associando elementi di valutazione e definendo righe
**In modo che** possa costruire blueprint riutilizzabili per i Template Audit

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Nuova framework" dalla lista template framework
**Allora** il sistema deve mostrare:

1. **Pagina creazione** con:
   - Titolo: "Nuovo"
   - Breadcrumb: "Template framework > Nuovo"
   - Form diviso in 3 sezioni:

#### SEZIONE 1: Informazioni Framework

| Campo | Tipo | Label | Validazione | Required |
|-------|------|-------|-------------|----------|
| nome_framework | Text | Nome framework | Max 255 char, univoco | Si |
| descrizione_framework | Textarea | Descrizione framework | Max 1000 char | No |

**Nota informativa**:
"Il nome identifica univocamente il framework (es: NIS2, CIS Controls v8, ISO27001)."

#### SEZIONE 2: Imposta Elementi di Valutazione

**Label sezione**: "Imposta Elementi di valutazione"

| Campo | Tipo | Label | Validazione | Required |
|-------|------|-------|-------------|----------|
| elementi_valutazione | Multi-select | Elementi di valutazione | Select multipla da anagrafica elementi | No |

**Comportamento multi-select**:
- Dropdown con checkbox multipli
- Ricerca incrementale nel dropdown
- Elementi selezionati mostrati come tag rimuovibili
- Se nessun elemento disponibile: messaggio "Nessun elemento di valutazione disponibile. Crea prima un elemento."

**Nota informativa**:
"Gli elementi di valutazione si applicheranno a tutte le righe del framework. Puoi selezionarne uno o piu."

#### SEZIONE 3: Crea elemento framework (Gestione Righe)

**Label sezione**: "Crea elemento framework"

**Form riga** con 5 campi affiancati:

| Campo | Tipo | Label | Validazione | Required |
|-------|------|-------|-------------|----------|
| ambito | Freesolo Autocomplete | Ambito | Max 100 char | Si |
| tematica | Freesolo Autocomplete | Tematica | Max 100 char | Si |
| categoria | Freesolo Autocomplete | Categoria | Max 100 char | Si |
| misura | Freesolo Autocomplete | Misura | Max 100 char | Si |
| requisito | Select Dropdown | Requisito | Select da anagrafica requisiti | Si |

**Comportamento Freesolo Autocomplete** (Ambito, Tematica, Categoria, Misura):
- Dropdown con suggerimenti da valori gia salvati in framework esistenti
- Possibilita di digitare nuovo valore non presente nei suggerimenti
- Icona "X" accanto ad ogni suggerimento per eliminarlo dall'anagrafica (vedi US-FWK-014)
- Placeholder: "Seleziona o digita nuovo valore"

**Comportamento Select Requisito**:
- Dropdown classico con lista requisiti da anagrafica
- Ricerca incrementale
- Se nessun requisito disponibile: messaggio "Nessun requisito disponibile. Crea prima un requisito."

**Pulsante azione riga**:
- **Aggiungi a framework** (blu, posizionato sotto i 5 campi): aggiunge riga alla tabella anteprima

**Tabella "Elementi framework"** (anteprima righe aggiunte):

**Colonne**:
- Ambito | Tematica | Categoria | Misura | Requisito | Azioni (menu tre puntini)

**Menu azioni riga** (tre puntini):
- **Modifica** (icona matita): ricontestualizza il form sopra con i valori della riga (edit mode)
- **Elimina** (icona cestino): rimuove la riga dalla tabella anteprima

**Paginazione tabella anteprima**:
- Rows per page: 5 (default)
- Indicatore "X of Y"
- Frecce navigazione

**Nota informativa sotto tabella**:
"Le righe aggiunte saranno salvate solo al click su 'Salva' in fondo alla pagina."

2. **Pulsanti azione finali** (bottom-right):
   - **Annulla** (grigio, outline): torna alla lista senza salvare
   - **Salva** (blu): valida e salva framework con tutte le righe

### Comportamento Aggiunta Riga

**Quando** clicco su "Aggiungi a framework"
**Allora** il sistema deve:

1. **Validare tutti i 5 campi**:
   - Se campi mancanti: mostrare errore sotto ogni campo invalido
   - Evidenziare campi con errore con bordo rosso

2. **Se in modalita edit** (riga in modifica):
   - Aggiornare la riga nella tabella anteprima
   - Reset form riga
   - Mostrare notifica: "Riga aggiornata"

3. **Se in modalita creazione** (nuova riga):
   - Aggiungere riga alla tabella anteprima
   - Reset form riga (tutti i campi vuoti)
   - Mostrare notifica: "Riga aggiunta"
   - Scroll automatico alla tabella anteprima

### Comportamento Modifica Riga

**Quando** clicco su "Modifica" dal menu riga nella tabella anteprima
**Allora** il sistema deve:

1. **Popolare il form riga** con i valori della riga selezionata
2. **Cambiare pulsante** "Aggiungi a framework" in "Aggiorna riga" (blu)
3. **Aggiungere pulsante** "Annulla modifica" (grigio, outline) accanto a "Aggiorna riga"
4. **Scroll automatico** al form riga
5. **Evidenziare la riga** in modifica nella tabella (bordo blu)

**Quando** clicco su "Annulla modifica"
**Allora** reset form riga e torna in modalita creazione

### Comportamento Eliminazione Riga

**Quando** clicco su "Elimina" dal menu riga nella tabella anteprima
**Allora** il sistema deve:

1. **Rimuovere la riga** dalla tabella anteprima immediatamente (no dialog conferma)
2. **Mostrare notifica**: "Riga rimossa"
3. **Aggiornare contatore** righe nella tabella

### Comportamento Salvataggio Framework

**Quando** clicco su "Salva" (pulsante finale bottom-right)
**Allora** il sistema deve:

1. **Validare campi base**:
   - Nome framework obbligatorio e univoco
   - Descrizione opzionale

2. **Validare righe**:
   - Permesso salvare framework con **0 righe** (stato Bozza)
   - Se righe presenti: validare che tutti i campi delle righe siano completi

3. **Se validazione OK**:
   - Creare record framework con **stato = Bozza**
   - Salvare associazioni elementi di valutazione (se presenti)
   - Salvare tutte le righe nella tabella anteprima
   - Per ogni campo freesolo (Ambito, Tematica, Categoria, Misura): salvare valori in anagrafica suggerimenti (se nuovi)
   - Mostrare notifica: "Framework creato con successo in stato Bozza"
   - Redirect a pagina dettaglio framework (US-FWK-015)

### Edge Cases

- **Nome duplicato**: "Nome framework gia esistente. Utilizza un nome diverso."
- **Nessun elemento di valutazione disponibile**: Multi-select vuoto con messaggio informativo
- **Nessun requisito disponibile**: Select vuoto con messaggio informativo + link "Crea requisito"
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."
- **Annulla con dati inseriti**: Dialog conferma "Sei sicuro di voler annullare? I dati inseriti andranno persi."
- **Annulla con righe in tabella**: Dialog conferma "Sei sicuro di voler annullare? Tutte le righe aggiunte andranno perse."
- **Framework vuoto** (0 righe): Salvato in Bozza, ma non pubblicabile fino all'aggiunta di almeno 1 riga

### Dipendenze
- US-FWK-001 a US-FWK-005 (anagrafica requisiti)
- US-FWK-006 a US-FWK-010 (anagrafica elementi di valutazione)
- US-FWK-011 (lista framework)

---

## US-FWK-013 - Gestire righe framework - Aggiungi/Modifica/Elimina in tabella anteprima (Admin)

**Come** Admin di piattaforma
**Voglio** gestire dinamicamente le righe del framework prima del salvataggio
**In modo che** possa costruire la struttura del framework in modo flessibile e correggere errori prima di salvare

### Criteri di Accettazione

**Dato che** sono nella pagina di creazione/modifica framework (US-FWK-012 o US-FWK-016)
**E** ho una tabella anteprima "Elementi framework"
**Allora** il sistema deve permettere:

### Operazione 1: Aggiungere Riga

**Quando** compilo i 5 campi (Ambito, Tematica, Categoria, Misura, Requisito) e clicco "Aggiungi a framework"
**Allora**:
1. Validare tutti i 5 campi required
2. Se validazione OK: aggiungere riga alla tabella anteprima
3. Reset form riga
4. Mostrare notifica: "Riga aggiunta" (toast)
5. Scroll automatico alla tabella

**Validazioni**:
- Tutti i 5 campi obbligatori
- Requisito deve esistere nell'anagrafica
- NO validazione univocita riga (duplicati ammessi)

### Operazione 2: Modificare Riga Esistente

**Quando** clicco "Modifica" dal menu riga nella tabella anteprima
**Allora**:
1. Popolare form riga con valori della riga selezionata
2. Cambiare label pulsante "Aggiungi a framework" in "Aggiorna riga"
3. Mostrare pulsante "Annulla modifica" accanto
4. Evidenziare riga in modifica (bordo blu spesso)
5. Scroll al form riga

**Quando** modifico i valori e clicco "Aggiorna riga"
**Allora**:
1. Validare tutti i 5 campi
2. Se validazione OK: aggiornare riga nella tabella anteprima
3. Reset form riga e tornare in modalita creazione
4. Rimuovere evidenziazione riga
5. Mostrare notifica: "Riga aggiornata"

**Quando** clicco "Annulla modifica"
**Allora**:
1. Reset form riga (tutti campi vuoti)
2. Tornare in modalita creazione
3. Rimuovere evidenziazione riga
4. Nessun salvataggio

### Operazione 3: Eliminare Riga

**Quando** clicco "Elimina" dal menu riga nella tabella anteprima
**Allora**:
1. Rimuovere immediatamente la riga dalla tabella (NO dialog conferma)
2. Mostrare notifica: "Riga rimossa"
3. Aggiornare contatore righe
4. Se riga era in modifica: reset form riga

### Comportamento Tabella Anteprima

**Caratteristiche**:
- Paginazione: 5 righe per pagina
- Sortable: NO (ordine di inserimento)
- Scroll verticale se > 5 righe
- Indicatore "X righe totali"

**Colonne**:
| Colonna | Width | Ellipsis |
|---------|-------|----------|
| Ambito | 15% | Si (max 50 char) |
| Tematica | 20% | Si (max 50 char) |
| Categoria | 20% | Si (max 50 char) |
| Misura | 20% | Si (max 50 char) |
| Requisito | 20% | Si (max 50 char) |
| Azioni | 5% | - |

**Menu azioni**:
- Icona tre puntini verticali
- Dropdown aligned right
- Opzioni: Modifica, Elimina

### Edge Cases

- **Eliminazione riga in modifica**: Reset form + rimozione riga
- **Aggiunta riga identica**: Consentito (NO validazione univocita)
- **Modifica con campi invalidi**: Mostrare errori sotto campi + non aggiornare riga
- **Tabella vuota**: Mostrare messaggio "Nessuna riga aggiunta. Compila i campi sopra e clicca 'Aggiungi a framework'."
- **Cambio pagina durante modifica**: Se cambio pagina lista mentre riga in modifica, reset form

### Dipendenze
- US-FWK-012 (creazione framework)
- US-FWK-016 (modifica framework)

---

## US-FWK-014 - Gestire freesolo con eliminazione suggerimenti tramite icona X (Admin)

**Come** Admin di piattaforma
**Voglio** eliminare valori salvati involontariamente nell'autocomplete freesolo
**In modo che** possa mantenere pulita l'anagrafica suggerimenti e evitare errori di battitura persistenti

### Criteri di Accettazione

**Dato che** sono nella pagina di creazione/modifica framework
**E** sto utilizzando i campi freesolo (Ambito, Tematica, Categoria, Misura)
**Quando** clicco sul dropdown di un campo freesolo
**Allora** il sistema deve mostrare:

1. **Dropdown suggerimenti** con:
   - Lista valori gia salvati in framework esistenti (ordinati alfabeticamente)
   - Ogni voce con **icona X a destra** (colore rosso/arancione)
   - Ricerca incrementale (filtra suggerimenti mentre digito)
   - Placeholder: "Seleziona o digita nuovo valore"

2. **Comportamento hover su suggerimento**:
   - Highlight riga (sfondo grigio chiaro)
   - Icona X diventa visibile/evidente

### Comportamento Click su Suggerimento

**Quando** clicco su un suggerimento (NON sull'icona X)
**Allora**:
1. Il valore viene inserito nel campo
2. Il dropdown si chiude
3. Nessuna eliminazione

### Comportamento Click su Icona X

**Quando** clicco sull'icona X accanto a un suggerimento
**Allora** il sistema deve:

1. **Verificare utilizzo del valore**:
   - Controllare se il valore e utilizzato in righe di framework esistenti (pubblicati o bozza)
   - Se SI: mostrare dialog WARNING
   - Se NO: mostrare dialog conferma standard

2. **Dialog WARNING se valore utilizzato**:
   ```
   Attenzione!
   Il valore "[Valore]" e utilizzato nelle seguenti righe di framework:

   Framework: [Nome Framework 1]
   - N. righe: X

   Framework: [Nome Framework 2]
   - N. righe: Y

   ... (max 3 framework mostrati)

   Eliminando questo suggerimento:
   - Sara rimosso dall'autocomplete
   - Le righe esistenti che lo utilizzano NON saranno modificate
   - Non sara piu disponibile per future creazioni

   Sei sicuro di voler procedere?

   [Annulla] [Conferma eliminazione]
   ```

3. **Dialog conferma standard se valore NON utilizzato**:
   ```
   Conferma eliminazione suggerimento

   Sei sicuro di voler eliminare il suggerimento "[Valore]"?

   Questa operazione NON e reversibile.

   [Annulla] [Conferma eliminazione]
   ```

4. **Se conferma eliminazione**:
   - Eliminare valore dall'anagrafica suggerimenti
   - Rimuovere voce dal dropdown immediatamente
   - Mostrare notifica: "Suggerimento eliminato con successo"
   - Dropdown rimane aperto (aggiornato senza il valore eliminato)

### Comportamento Creazione Nuovo Valore

**Quando** digito un valore non presente nei suggerimenti e premo Invio o blur campo
**Allora**:
1. Il valore viene accettato nel campo
2. **Al salvataggio del framework**, il nuovo valore viene aggiunto all'anagrafica suggerimenti
3. Nelle successive creazioni, il valore sara disponibile nei suggerimenti

### Edge Cases

- **Valore utilizzato in molti framework**: Mostrare max 3 framework nel dialog + contatore "e altri X"
- **Eliminazione durante digitazione**: Se sto digitando e elimino suggerimento che matcha, aggiornare lista filtrata
- **Errore eliminazione**: "Errore durante l'eliminazione del suggerimento. Riprova."
- **Click X per errore**: Dialog conferma previene eliminazioni accidentali
- **Suggerimenti vuoti**: Se nessun suggerimento disponibile, mostrare solo input text (no dropdown)
- **Case-insensitive**: Suggerimenti e ricerca case-insensitive

### Validazioni

1. **Eliminazione**: Solo Admin puo eliminare suggerimenti
2. **Utilizzo**: Controllo utilizzo in tempo reale (query database)
3. **Univocita**: Nuovo valore NON puo essere duplicato (case-insensitive)

### Dipendenze
- US-FWK-012 (creazione framework con freesolo)
- US-FWK-016 (modifica framework con freesolo)

---

## US-FWK-015 - Visualizzare dettaglio framework in modalita sola lettura (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare tutti i dettagli di un framework in modalita sola lettura
**In modo che** possa consultare le informazioni complete senza modifiche accidentali

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su un framework dalla lista o dal menu contestuale "Dettaglio"
**Allora** il sistema deve mostrare:

1. **Pagina dettaglio** con:
   - Titolo: "Dettaglio"
   - Breadcrumb: "Template framework > Dettaglio"
   - Pulsante "Modifica" (arancione, top-right)
   - Badge stato framework (top-right accanto a Modifica)

2. **Sezione "Informazioni Framework"** (read-only):

**Layout**: Form a colonna singola (campi disabilitati)

| Campo | Label | Formato Display |
|-------|-------|-----------------|
| nome_framework | Nome framework | Text (disabilitato) |
| descrizione_framework | Descrizione framework | Textarea (disabilitato, se presente) |
| stato_framework | Stato | Badge colorato (Bozza/Pubblicato/Archiviato) |
| elementi_valutazione | Elementi di valutazione | Tag chips disabilitati (se presenti) |
| n_righe | Numero righe | Number (es: "25 righe") |
| creato_il | Creato il | DD/MM/YYYY HH:mm |
| modificato_il | Modificato il | DD/MM/YYYY HH:mm (se presente) |
| pubblicato_il | Pubblicato il | DD/MM/YYYY HH:mm (se stato=Pubblicato) |
| archiviato_il | Archiviato il | DD/MM/YYYY HH:mm (se stato=Archiviato) |

3. **Sezione "Elementi Framework"** (read-only):

**Tabella righe framework** (non modificabile):

**Colonne**:
- Ambito | Tematica | Categoria | Misura | Requisito

**Caratteristiche tabella**:
- Paginazione: 10 righe per pagina
- Sortable: SI (tutte le colonne)
- Filtri: NO
- Azioni: NO (nessun menu contestuale)

**Nota informativa sopra tabella**:
"Per modificare le righe, clicca sul pulsante 'Modifica' in alto."

4. **Pulsante azione** (bottom-right):
   - **Modifica** (arancione): apre form modifica (US-FWK-016)

5. **Sezione "Utilizzo"** (informativa):
   - Contatore: "Utilizzato come blueprint in X template audit"
   - Se X > 0: link "Visualizza template audit" che apre lista template audit filtrata per questo framework
   - Se X = 0: messaggio "Non ancora utilizzato in nessun template audit"

### Comportamento Pulsante Modifica

**Se stato = Bozza o Pubblicato**:
- Pulsante "Modifica" abilitato
- Click: apre pagina modifica (US-FWK-016)

**Se stato = Archiviato**:
- Pulsante "Modifica" disabilitato
- Tooltip: "Non puoi modificare un framework archiviato"

### Edge Cases

- **Nessuna descrizione**: Se campo "Descrizione" vuoto, non mostrare il campo
- **Nessun elemento valutazione**: Mostrare "-" invece di tag vuoti
- **0 righe**: Tabella vuota con messaggio "Nessuna riga presente in questo framework"
- **Errore caricamento**: Mostrare notifica "Impossibile caricare i dettagli. Riprova."
- **Framework eliminato**: Se framework non esiste piu, redirect a lista con messaggio "Framework non trovato"

### Dipendenze
- US-FWK-011 (lista framework)
- US-FWK-012 (creazione framework)

---

## US-FWK-016 - Modificare framework esistente (Admin)

**Come** Admin di piattaforma
**Voglio** modificare i dati di un framework esistente
**In modo che** possa aggiornare informazioni, aggiungere/rimuovere righe e elementi di valutazione

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Modifica" dalla pagina dettaglio o dal menu contestuale
**Allora** il sistema deve mostrare:

1. **Pagina modifica** con:
   - Titolo: "Modifica"
   - Breadcrumb: "Template framework > Dettaglio > Modifica"
   - Form con gli stessi campi di creazione (US-FWK-012), pre-compilati con i valori attuali

2. **Campi modificabili**:

| Campo | Modificabile | Note |
|-------|--------------|------|
| nome_framework | SI | Validazione univocita (escludendo se stesso) |
| descrizione_framework | SI | Max 1000 char |
| elementi_valutazione | SI | Multi-select modificabile |
| righe_framework | SI | Tabella anteprima modificabile (vedi US-FWK-013) |

**Nota importante**:
"Lo stato del framework rimane invariato durante la modifica. Usa l'azione 'Pubblica' per cambiare lo stato."

3. **Sezione righe pre-popolata**:
   - Tabella "Elementi framework" gia popolata con righe esistenti
   - Form riga vuoto sopra per aggiungere nuove righe
   - Menu azioni su ogni riga: Modifica, Elimina

4. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna al dettaglio senza salvare
   - **Salva** (blu): valida e salva modifiche

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare campi base**:
   - Nome framework obbligatorio e univoco (escludendo se stesso)
   - Descrizione opzionale

2. **Validare righe**:
   - Se framework ha stato=Pubblicato: **NON permettere salvare con 0 righe** (mostrare errore: "Un framework pubblicato deve avere almeno 1 riga.")
   - Se framework ha stato=Bozza: permettere salvare con 0 righe

3. **Se validazione OK**:
   - Aggiornare record framework
   - Aggiornare associazioni elementi di valutazione (insert/delete)
   - Aggiornare righe framework:
     - Eliminare righe rimosse dalla tabella
     - Aggiornare righe modificate
     - Inserire nuove righe aggiunte
   - Aggiornare anagrafica suggerimenti freesolo (se nuovi valori)
   - Aggiornare timestamp `modificato_il`
   - Mostrare notifica: "Modifiche salvate con successo"
   - Redirect a pagina dettaglio (US-FWK-015)

### Vincoli di Modifica per Stato

**Se stato = Bozza**:
- Tutte le modifiche consentite
- Possibile salvare con 0 righe

**Se stato = Pubblicato**:
- Tutte le modifiche consentite
- **NON possibile salvare con 0 righe** (errore bloccante)

**Se stato = Archiviato**:
- Modifica NON consentita (pulsante disabilitato in dettaglio)
- Se tentativo di accesso diretto via URL: redirect a dettaglio con messaggio "Non puoi modificare un framework archiviato"

### Edge Cases

- **Nessuna modifica**: Se clicco "Salva" senza modificare nulla, salvare comunque e aggiornare `modificato_il`
- **Nome duplicato** (se modificato): "Nome framework gia esistente. Utilizza un nome diverso."
- **Eliminazione tutte righe con stato Pubblicato**: "Un framework pubblicato deve avere almeno 1 riga. Aggiungi righe o archivia il framework."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."
- **Annulla con modifiche**: Dialog conferma "Sei sicuro di voler annullare? Le modifiche andranno perse."
- **Annulla con righe modificate**: Dialog conferma "Sei sicuro di voler annullare? Le modifiche alle righe andranno perse."

### Dipendenze
- US-FWK-015 (dettaglio framework)
- US-FWK-013 (gestione righe)
- US-FWK-014 (gestione freesolo)

---

## US-FWK-017 - Pubblicare framework - cambio stato Bozza → Pubblicato (Admin)

**Come** Admin di piattaforma
**Voglio** pubblicare un framework in stato Bozza
**In modo che** diventi disponibile per la creazione di Template Audit da parte dei Consulenti

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**E** ho un framework in stato Bozza
**Quando** clicco su "Pubblica" dal menu contestuale nella lista framework
**Allora** il sistema deve:

1. **Verificare prerequisiti per pubblicazione**:
   - Controllare se framework ha **almeno 1 riga**
   - Se NO: mostrare dialog di BLOCCO
   - Se SI: mostrare dialog di CONFERMA

2. **Dialog di BLOCCO se 0 righe**:
   ```
   Impossibile pubblicare il framework

   Il framework "[Nome Framework]" non ha righe definite.

   Per pubblicare un framework devi aggiungere almeno 1 riga.

   [Chiudi] [Vai a Modifica]
   ```

   **Pulsanti**:
   - **Chiudi**: chiude dialog (rimane in lista)
   - **Vai a Modifica**: redirect a pagina modifica framework (US-FWK-016)

3. **Dialog di CONFERMA se righe >= 1**:
   ```
   Conferma pubblicazione framework

   Stai per pubblicare il framework "[Nome Framework]" con le seguenti caratteristiche:
   - N. righe: X
   - Elementi di valutazione: Y (o "Nessuno" se 0)

   Una volta pubblicato:
   - Sara visibile ai Consulenti per la creazione di Template Audit
   - Potrai ancora modificarlo (aggiungere/rimuovere righe)
   - Non potrai eliminarlo se utilizzato in Template Audit

   Confermi la pubblicazione?

   [Annulla] [Conferma pubblicazione]
   ```

4. **Se conferma pubblicazione**:
   - Aggiornare `stato_framework` = "Pubblicato"
   - Impostare `pubblicato_il` = timestamp corrente
   - Aggiornare `modificato_il` = timestamp corrente
   - Mostrare notifica: "Framework pubblicato con successo"
   - Aggiornare riga nella lista (badge diventa verde "Pubblicato")
   - Rimuovere azione "Pubblica" dal menu azioni (sostituita con "Archivia")

### Comportamento Pulsante "Pubblica" nel Menu

**Visibilita azione "Pubblica"**:
- **Visibile** solo se stato = Bozza
- **NON visibile** se stato = Pubblicato o Archiviato

**Abilitazione azione "Pubblica"**:
- **Abilitata** se n_righe >= 1
- **Disabilitata** se n_righe = 0 (tooltip: "Aggiungi almeno 1 riga per pubblicare")

### Effetti Pubblicazione

**Per Admin**:
- Framework rimane modificabile
- Cambia azione menu da "Pubblica" a "Archivia"
- Badge diventa verde

**Per Consulenti** (epica futura Template Audit):
- Framework diventa visibile nella selezione blueprint per Template Audit
- Consultabile in sola lettura

### Edge Cases

- **Framework con 0 righe**: Blocco hard con dialog esplicativo + pulsante "Vai a Modifica"
- **Framework gia pubblicato**: Azione "Pubblica" non visibile nel menu
- **Errore pubblicazione**: "Errore durante la pubblicazione. Riprova."
- **Framework eliminato durante operazione**: Mostrare "Framework non trovato" e refresh lista

### Dipendenze
- US-FWK-011 (lista framework con menu azioni)
- US-FWK-012 (creazione framework)
- US-FWK-016 (modifica framework)

---

## US-FWK-018 - Eliminare/Archiviare framework con validazione vincoli (Admin)

**Come** Admin di piattaforma
**Voglio** eliminare o archiviare un framework rispettando i vincoli di business
**In modo che** non vengano eliminati framework utilizzati come blueprint in Template Audit attivi

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su azione framework
**Allora** il sistema deve mostrare comportamenti diversi in base allo stato:

---

### CASO 1: Eliminazione Framework in Stato Bozza

**Quando** clicco su "Elimina" dal menu contestuale di un framework con stato=Bozza
**Allora** il sistema deve:

1. **Mostrare dialog di conferma**:
   ```
   Conferma eliminazione framework

   Sei sicuro di voler eliminare il framework "[Nome Framework]" in stato Bozza?

   Il framework contiene:
   - N. righe: X
   - Elementi di valutazione: Y

   Questa operazione NON e reversibile.

   [Annulla] [Conferma eliminazione]
   ```

2. **Se conferma eliminazione**:
   - Eliminare (hard delete) record framework
   - Eliminare tutte le righe associate (cascade delete)
   - Eliminare associazioni elementi di valutazione
   - Mostrare notifica: "Framework eliminato con successo"
   - Redirect a lista framework (US-FWK-011)

---

### CASO 2: Archiviazione Framework Pubblicato (NON Utilizzato)

**Quando** clicco su "Archivia" dal menu contestuale di un framework con stato=Pubblicato
**E** il framework **NON e utilizzato** in Template Audit
**Allora** il sistema deve:

1. **Mostrare dialog di conferma**:
   ```
   Conferma archiviazione framework

   Stai per archiviare il framework "[Nome Framework]".

   Una volta archiviato:
   - Non sara piu visibile ai Consulenti per nuovi Template Audit
   - Non potrai piu modificarlo
   - I Template Audit esistenti che lo utilizzano continueranno a funzionare
   - Potrai ripristinarlo in futuro (feature non implementata in MVP)

   Confermi l'archiviazione?

   [Annulla] [Conferma archiviazione]
   ```

2. **Se conferma archiviazione**:
   - Aggiornare `stato_framework` = "Archiviato"
   - Impostare `archiviato_il` = timestamp corrente
   - Aggiornare `modificato_il` = timestamp corrente
   - Mostrare notifica: "Framework archiviato con successo"
   - Aggiornare riga nella lista (badge diventa arancione "Archiviato")
   - Rimuovere azioni "Modifica" e "Archivia" dal menu (solo "Dettaglio" rimane)

---

### CASO 3: Tentativo Eliminazione Framework Pubblicato (Utilizzato)

**Quando** clicco su "Elimina" dal menu contestuale di un framework con stato=Pubblicato
**E** il framework **e utilizzato** in Template Audit
**Allora** il sistema deve:

1. **Verificare utilizzo**:
   - Controllare se framework e utilizzato come blueprint in Template Audit

2. **Mostrare dialog di BLOCCO**:
   ```
   Impossibile eliminare il framework

   Il framework "[Nome Framework]" e utilizzato come blueprint nei seguenti Template Audit:

   - Template Audit: [Nome Template 1] (Consulente: [Nome Consulente])
   - Template Audit: [Nome Template 2] (Consulente: [Nome Consulente])
   - Template Audit: [Nome Template 3] (Consulente: [Nome Consulente])

   ... (max 5 template mostrati, se > 5 mostrare "e altri X template")

   Per procedere:
   1. Puoi ARCHIVIARE il framework (lo rendera non disponibile per nuovi template)
   2. Oppure elimina i Template Audit che lo utilizzano prima di eliminare il framework

   [Chiudi] [Archivia framework]
   ```

   **Pulsanti**:
   - **Chiudi**: chiude dialog (rimane in lista)
   - **Archivia framework**: cambia stato a "Archiviato" (shortcut a CASO 2)

---

### CASO 4: Tentativo Eliminazione Framework Archiviato

**Quando** clicco su "Elimina" dal menu contestuale di un framework con stato=Archiviato
**Allora** il sistema deve:

1. **Mostrare dialog di WARNING**:
   ```
   Attenzione!

   Stai per eliminare definitivamente il framework archiviato "[Nome Framework]".

   Il framework contiene:
   - N. righe: X
   - Utilizzato in: Y Template Audit (se > 0)

   Eliminando il framework:
   - Sara rimosso definitivamente dal database
   - I Template Audit che lo utilizzano continueranno a funzionare (dati preservati)
   - Non sara piu recuperabile

   Questa operazione NON e reversibile.

   Sei sicuro di voler procedere?

   [Annulla] [Conferma eliminazione definitiva]
   ```

2. **Se conferma eliminazione**:
   - Eliminare (hard delete) record framework
   - Eliminare tutte le righe associate (cascade delete)
   - Eliminare associazioni elementi di valutazione
   - Mostrare notifica: "Framework eliminato definitivamente"
   - Redirect a lista framework

---

### Comportamento Menu Azioni per Stato

**Se stato = Bozza**:
- Azioni disponibili: Dettaglio, Modifica, **Pubblica** (se righe >= 1), **Elimina**

**Se stato = Pubblicato**:
- Azioni disponibili: Dettaglio, Modifica, **Archivia**, **Elimina** (con vincolo utilizzo)

**Se stato = Archiviato**:
- Azioni disponibili: Dettaglio, **Elimina** (con warning)
- Azione "Modifica" NON disponibile

### Edge Cases

- **Framework utilizzato in molti template**: Mostrare max 5 template nel dialog + contatore "e altri X"
- **Errore eliminazione**: "Errore durante l'eliminazione. Riprova."
- **Errore archiviazione**: "Errore durante l'archiviazione. Riprova."
- **Framework gia eliminato**: Mostrare "Framework non trovato" e refresh lista
- **Framework con 0 righe in Bozza**: Eliminazione consentita

### Vincoli di Business

- **Bozza**: Eliminazione libera (hard delete)
- **Pubblicato NON utilizzato**: Archiviazione consentita
- **Pubblicato utilizzato**: Eliminazione BLOCCATA, solo archiviazione
- **Archiviato**: Eliminazione con warning (hard delete)
- **Cascade delete**: Eliminando framework, eliminare anche righe e associazioni

### Dipendenze
- US-FWK-011 (lista framework con menu azioni)
- US-FWK-017 (pubblicazione)

---

## Riepilogo User Stories - Gestione Template Framework

| ID | Titolo | Complessita | Priorita |
|----|--------|-------------|----------|
| US-FWK-011 | Visualizzare lista template framework | M | MUST |
| US-FWK-012 | Creare nuovo framework con righe e elementi | H | MUST |
| US-FWK-013 | Gestire righe - Aggiungi/Modifica/Elimina | H | MUST |
| US-FWK-014 | Gestire freesolo con eliminazione suggerimenti | M | MUST |
| US-FWK-015 | Visualizzare dettaglio framework read-only | M | MUST |
| US-FWK-016 | Modificare framework esistente | H | MUST |
| US-FWK-017 | Pubblicare framework (Bozza → Pubblicato) | M | MUST |
| US-FWK-018 | Eliminare/Archiviare con validazione vincoli | H | MUST |

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

1. **Nome framework**: Max 255 char + univocita (case-insensitive)
2. **Descrizione framework**: Max 1000 char (optional)
3. **Campi riga freesolo**: Max 100 char ciascuno
4. **Righe framework**: Minimo 1 riga per pubblicazione
5. **Stati framework**: Bozza, Pubblicato, Archiviato (enum)

### Pattern UI Comuni

1. **Form layout**: 1 colonna responsive
2. **Tabella anteprima righe**: Paginata, sortable (in modifica)
3. **Freesolo autocomplete**: Dropdown suggerimenti + icona X eliminazione
4. **Multi-select**: Dropdown checkbox + tag chips
5. **Pulsanti azione**: Sempre bottom-right (Annulla + Azione primaria)
6. **Notifiche**: Toast top-right, auto-dismiss 5s
7. **Dialog conferma**: Modale centrato, overlay scuro 50%
8. **Menu contestuale**: Dropdown aligned right, 3 puntini verticali

### Regole Stati Framework

1. **Bozza** (default):
   - Modificabile
   - Eliminabile
   - Pubblicabile solo se righe >= 1
   - Non visibile a Consulenti

2. **Pubblicato**:
   - Modificabile
   - Archiviabile
   - Eliminabile solo se NON utilizzato
   - Visibile a Consulenti

3. **Archiviato**:
   - NON modificabile
   - Eliminabile con warning
   - Non visibile a Consulenti (per nuovi template)
   - Template esistenti continuano a funzionare

### Gestione Freesolo

1. **Anagrafica suggerimenti**: Tabella separata per valori freesolo (Ambito, Tematica, Categoria, Misura)
2. **Salvataggio automatico**: Nuovi valori salvati al salvataggio framework
3. **Eliminazione con X**: Admin puo rimuovere suggerimenti indesiderati
4. **Controllo utilizzo**: Warning se suggerimento utilizzato in framework esistenti
5. **Case-insensitive**: Suggerimenti e validazione univocita case-insensitive

### Gestione Righe Framework

1. **Tabella anteprima**: Operazioni CRUD in memoria prima del salvataggio finale
2. **Edit mode**: Riga in modifica evidenziata, form popolato, pulsante "Aggiorna riga"
3. **Eliminazione immediata**: No dialog conferma per eliminazione riga dalla tabella anteprima
4. **Validazione salvataggio**: Tutte le righe in tabella anteprima salvate al click "Salva" finale

### Gestione Eliminazione

1. **Hard delete**: Record eliminato definitivamente (framework + righe + associazioni)
2. **Cascade delete**: Eliminando framework, eliminare righe e associazioni
3. **Vincolo utilizzo**: Framework pubblicato utilizzato in Template Audit → blocco eliminazione (solo archiviazione)
4. **Warning**: Framework archiviato → warning ma eliminazione consentita

### Gestione Visibilita

1. **Admin**: CRUD completo + gestione stati
2. **Consulenti**: Solo visualizzazione framework pubblicati (per Template Audit)
3. **Framework globali**: Tutti i framework condivisi tra Admin e Consulenti

---

**Fine User Stories - Gestione Template Framework**
