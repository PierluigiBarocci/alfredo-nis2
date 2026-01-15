# User Stories - Gestione Requisiti

**Epica**: Framework
**Macro-argomento**: Gestione Requisiti (Anagrafica)
**Data**: 2025-12-11
**Versione**: 1.0

---

## Indice User Stories

- [US-FWK-001] Visualizzare lista requisiti (Admin)
- [US-FWK-002] Creare nuovo requisito (Admin)
- [US-FWK-003] Visualizzare dettaglio requisito (Admin)
- [US-FWK-004] Modificare requisito (Admin)
- [US-FWK-005] Eliminare requisito con validazione vincoli (Admin)

---

## US-FWK-001 - Visualizzare lista requisiti (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare la lista completa dei requisiti
**In modo che** possa avere una panoramica di tutti i requisiti disponibili e accedere rapidamente ai loro dettagli

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla sezione "Requisiti" dal menu principale
**Allora** il sistema deve mostrare:

1. **Pagina lista requisiti** con:

   - Titolo pagina: "Requisiti"
   - Breadcrumb: "Requisiti"
   - Pulsante "Nuovo Requisito" (arancione, top-right)
   - Filtri ricerca (Nome, Requisito)
   - Tabella paginata con le seguenti colonne (fisse):
     - **Nome** (Nome requisito, sortable)
     - **Requisito** (Nome requisito, sortable)
     - **Descrizione** (Descrizione requisito, sortable)
     - **Data creazione** (Data creazione formato DD/MM/YYYY, sortable)
     - **Azioni** (Menu contestuale: Dettaglio, Modifica, Elimina)

2. **Paginazione**:

   - Rows per page: 10 (default), con opzioni 10/25/50
   - Indicatore "X-Y di Z" (es. "1-4 di 4")
   - Frecce navigazione prev/next

3. **Comportamento click su riga**:

   - Click su icona menu (tre puntini): mostra dropdown con opzioni:
     - Dettaglio (icona occhio)
     - Modifica (icona matita)
     - Elimina (icona cestino, colore arancione)

4. **Stato vuoto**:

   - Se non ci sono requisiti: mostrare messaggio "Nessun requisito registrato" + pulsante "Crea primo requisito"

### Edge Cases

- **Nessun risultato filtro**: Se il filtro non restituisce risultati, mostrare "Nessun risultato trovato. Modifica il filtro di ricerca."
- **Errore caricamento dati**: Mostrare notifica di errore "Impossibile caricare i requisiti. Riprova."
- **Ordinamento default**: Ordinamento default per "Data creazione" decrescente (più recenti prima)

### Dipendenze

- Nessuna

---

## US-FWK-002 - Creare nuovo requisito (Admin)

**Come** Admin di piattaforma
**Voglio** creare un nuovo requisito
**In modo che** possa arricchire l'anagrafica requisiti riutilizzabile nei framework

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Nuovo requisito" dalla lista requisiti
**Allora** il sistema deve mostrare:

1. **Pagina creazione** con:
   - Titolo: "Nuovo"
   - Breadcrumb: "Requisiti > Nuovo"
   - Form con campi:

#### Campi Requisito

| Campo          | Tipo     | Label          | Validazione   | Required |
| -------------- | -------- | -------------- | ------------- | -------- |
| nome_requisito | Text     | Nome requisito | Max 255 char  | Si       |
| requisito      | Textarea | Requisito      | Max 1000 char | Si       |
| descrizione    | Textarea | Descrizione    | Max 255 char  | No       |

**Nota informativa sotto i campi**:
"La descrizione e ad uso interno per identificare meglio il requisito. Non verra visualizzata nei framework o negli audit."

2. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna alla lista senza salvare
   - **Salva** (blu): valida e salva

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare tutti i campi obbligatori**:

   - Se mancano campi obbligatori: mostrare messaggio di errore sotto ogni campo invalido
   - Evidenziare i campi con errore con bordo rosso
   - Scroll automatico al primo campo con errore

2. **Validare univocita nome requisito**:

   - Se nome gia esistente: mostrare errore "Nome requisito gia esistente. Utilizza un nome diverso."

3. **Se validazione OK**:
   - Creare record requisito
   - Mostrare notifica di successo: "Requisito creato con successo"
   - Redirect a pagina listato requisiti

### Edge Cases

- **Nome duplicato**: "Nome requisito gia esistente. Utilizza un nome diverso."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."

---

## US-FWK-003 - Visualizzare dettaglio requisito (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare tutti i dettagli di un requisito
**In modo che** possa consultare le informazioni complete in modalita sola lettura

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su un requisito dalla lista o dal menu contestuale "Dettaglio"
**Allora** il sistema deve mostrare:

1. **Pagina dettaglio** con:

   - Titolo: "Dettaglio"
   - Breadcrumb: "Requisiti > Dettaglio"
   - Pulsante "Modifica" (arancione, top-right)

2. **Sezione "Informazioni Requisito"** (read-only):

**Layout**: Form a colonna singola (campi disabilitati)

| Campo          | Label          | Formato Display         |
| -------------- | -------------- | ----------------------- |
| nome_requisito | Nome requisito | Text (disabilitato)     |
| requisito      | Descrizione    | Textarea (disabilitato) |
| descrizione    | Descrizione    | Text (disabilitato)     |

3. **Sezione "Utilizzo"** (informativa):
   - Contatore: "Utilizzato in X framework"
   - Se X > 0: link "Visualizza framework" che apre lista framework filtrata per questo requisito
   - Se X = 0: messaggio "Non ancora utilizzato in nessun framework"

### Edge Cases

- **Nessuna descrizione**: Se campo "Descrizione" vuoto, non mostrare il campo
- **Errore caricamento**: Mostrare notifica "Impossibile caricare i dettagli. Riprova."
- **Requisito eliminato**: Se requisito non esiste piu, redirect a lista con messaggio "Requisito non trovato"

---

## US-FWK-004 - Modificare requisito (Admin)

**Come** Admin di piattaforma
**Voglio** modificare i dati di un requisito
**In modo che** possa aggiornare le informazioni quando necessario

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Modifica" dalla pagina dettaglio o dal menu contestuale
**Allora** il sistema deve mostrare:

1. **Pagina modifica** con:

   - Titolo: "Modifica"
   - Breadcrumb: "Requisiti > Dettaglio > Modifica"
   - Form con gli stessi campi di creazione (US-FWK-002), pre-compilati con i valori attuali

2. **Campi modificabili** (TUTTI i campi sono modificabili):

| Campo          | Tipo     | Label          | Validazione   | Required |
| -------------- | -------- | -------------- | ------------- | -------- |
| nome_requisito | Text     | Nome requisito | Max 255 char  | Si       |
| requisito      | Textarea | Requisito      | Max 1000 char | Si       |
| descrizione    | Textarea | Descrizione    | Max 255 char  | No       |

3. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna al dettaglio senza salvare
   - **Salva** (blu): valida e salva modifiche

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare tutti i campi** (stesse regole di creazione US-FWK-002)

2. **Validare univocita nome requisito**:

   - Se nome gia esistente (escludendo se stesso): mostrare errore "Nome requisito gia esistente. Utilizza un nome diverso."

3. **Se validazione OK**:
   - Aggiornare record requisito
   - Mostrare notifica di successo: "Modifiche salvate con successo"
   - Redirect a listato

### Edge Cases

- **Nessuna modifica**: Se clicco "Salva" senza modificare nulla, salvare comunque e aggiornare `modificato_il`
- **Nome duplicato** (se modificato): "Nome requisito gia esistente. Utilizza un nome diverso."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."

### Dipendenze

- US-FWK-003 (dettaglio requisito)

---

## US-FWK-005 - Eliminare requisito con validazione vincoli (Admin)

**Come** Admin di piattaforma
**Voglio** eliminare un requisito rispettando i vincoli di business
**In modo che** non vengano eliminati requisiti associati a framework esistenti senza warning

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Elimina" dal menu contestuale di un requisito (lista o dettaglio)
**Allora** il sistema deve:

1. **Verificare utilizzo in framework**:

   - Controllare se il requisito e associato a righe di framework esistenti
   - Se SI: Mostrare dialog di WARNING (non blocco hard)

2. **Mostrare dialog di warning se requisito utilizzato**:

   ```
   Attenzione!
   Il requisito "[Nome Requisito]" e utilizzato nelle seguenti righe di framework:

   Framework: [Nome Framework 1]
   - Riga: [Ambito] > [Tematica] > [Categoria] > [Misura]

   Framework: [Nome Framework 2]
   - Riga: [Ambito] > [Tematica] > [Categoria] > [Misura]

   ... (max 5 righe mostrate, se > 5 mostrare "e altri X framework")

   Eliminando questo requisito, le righe associate nei framework verranno eliminate.

   Sei sicuro di voler procedere?

   [Annulla] [Conferma eliminazione]
   ```

3. **Se NON utilizzato**, mostrare dialog di conferma standard:

   ```
   Conferma eliminazione requisito

   Sei sicuro di voler eliminare il requisito "[Nome Requisito]"?

   Questa operazione NON e reversibile.

   [Annulla] [Conferma eliminazione]
   ```

4. **Se conferma eliminazione**:
   - Eliminare (soft delete) record requisito
   - Mostrare notifica: "Requisito eliminato con successo"
   - Elimina le righe in cui è utilizzato
   - Redirect a lista requisiti (US-FWK-001)

### Edge Cases

- **Requisito utilizzato in molti framework**: Mostrare max 5 framework nel dialog + contatore "e altri X"
- **Errore eliminazione**: "Errore durante l'eliminazione. Riprova."
- **Requisito gia eliminato**: Se nel frattempo e stato eliminato, mostrare "Requisito non trovato" e refresh lista

### Vincoli di Business

- **WARNING (non blocco)**: L'Admin puo eliminare requisiti anche se utilizzati (dopo conferma warning)

---

## Riepilogo User Stories - Gestione Requisiti

| ID         | Titolo                              | Complessita | Priorita |
| ---------- | ----------------------------------- | ----------- | -------- |
| US-FWK-001 | Visualizzare lista requisiti        | L           | MUST     |
| US-FWK-002 | Creare nuovo requisito              | L           | MUST     |
| US-FWK-003 | Visualizzare dettaglio requisito    | L           | MUST     |
| US-FWK-004 | Modificare requisito                | L           | MUST     |
| US-FWK-005 | Eliminare requisito con validazione | M           | MUST     |

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

1. **Nome requisito**: Max 255 char + univocita (case-insensitive)
2. **Descrizione**: Max 1000 char (optional)

### Pattern UI Comuni

1. **Form layout**: 1 colonna responsive
2. **Pulsanti azione**: Sempre bottom-right (Annulla + Azione primaria)
3. **Notifiche**: Toast top-right, auto-dismiss 5s
4. **Dialog conferma**: Modale centrato, overlay scuro 50%
5. **Menu contestuale**: Dropdown aligned right, 3 puntini verticali

### Regole di Visibilita

1. **Admin**: CRUD completo
2. **Consulenti**: NO accesso alla lista requisiti (vedono solo dropdown nei Template Audit)
3. **Requisiti globali**: Condivisi tra tutti i framework

### Gestione Eliminazione

1. **Hard delete**: Record eliminato definitivamente
2. **Warning utilizzo**: Dialog informativo ma NON bloccante
3. **Graceful degradation**: Righe framework con requisito eliminato mostrano placeholder "Requisito non disponibile"

---

**Fine User Stories - Gestione Requisiti**
