# User Stories - Gestione Aziende di Consulenza

**Epica**: Anagrafiche
**Macro-argomento**: Gestione Aziende di Consulenza
**Data**: 2025-12-11
**Versione**: 2.0

---

## Indice User Stories

- [US-ANA-004] Visualizzare lista aziende di consulenza (Admin di piattaforma)
- [US-ANA-005] Creare nuova azienda di consulenza con primo admin-consulente (Admin di piattaforma)
- [US-ANA-006] Visualizzare dettaglio azienda di consulenza (Admin di piattaforma)
- [US-ANA-007] Modificare dati azienda di consulenza (Admin di piattaforma)
- [US-ANA-008] Gestire consulenti collegati all'azienda di consulenza (Admin di piattaforma)
- [US-ANA-018] Gestire aziende clienti associate all'azienda di consulenza (Admin di piattaforma)
- [US-ANA-019] Eliminare azienda di consulenza con validazione vincoli (Admin di piattaforma)
- [US-ANA-022] Ricercare e filtrare aziende di consulenza (Admin di piattaforma)
- [US-ANA-020] Visualizzare contatori dashboard filtrati per tenant (Admin di piattaforma e Consulente)
- [US-ANA-021] Bloccare creazione aziende/utenti al raggiungimento soglia massima (Sistema)

---

## US-ANA-004 - Visualizzare lista aziende di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** visualizzare la lista completa delle aziende di consulenza registrate
**In modo che** possa avere una panoramica di tutte le aziende gestite e accedere rapidamente ai loro dettagli

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla sezione "Aziende di consulenza" dal menu principale
**Allora** il sistema deve mostrare:

1. **Pagina lista aziende di consulenza** con:

   - Titolo pagina: "Aziende di consulenza"
   - Breadcrumb: "Aziende di consulenza"
   - Pulsante "Nuova azienda" (arancione, top-right)
   - Filtri di ricerca
   - Tabella paginata con le seguenti colonne (fisse):
     - **Azienda** (Nome azienda, sortable)
     - **Indirizzo** (Indirizzo completo, sortable)
     - **Referente** (Nome referente principale, sortable)
     - **N. aziende associate** (Contatore aziende clienti collegate, sortable)
     - **N. Utenti** (Contatore consulenti collegati, sortable)
     - **Creato il** (Data creazione formato DD/MM/YYYY, sortable)
     - **Azioni** (Menu contestuale: Dettaglio, Modifica, Elimina)

2. **Paginazione**:

   - Rows per page: 10 (default), con opzioni 10/25/50
   - Indicatore "X-Y di Z" (es. "1-4 di 4")
   - Frecce navigazione prev/next

3. **Ordinamento default**:

   - Ordinamento applicato: colonna "Creato il" decrescente (più recenti prima)

4. **Comportamento click su riga**:

   - Click su icona menu (tre puntini): mostra dropdown con opzioni:
     - Dettaglio (icona occhio)
     - Modifica (icona matita)
     - Elimina (icona cestino, colore arancione)

5. **Stato vuoto**:
   - Se non ci sono aziende di consulenza: mostrare messaggio "Nessuna azienda di consulenza registrata" + pulsante "Crea prima azienda"

### Edge Cases

- **Nessun risultato filtri**: Se i filtri non restituiscono risultati, mostrare "Nessun risultato trovato. Modifica i filtri di ricerca."
- **Errore caricamento dati**: Mostrare notifica di errore "Impossibile caricare le aziende di consulenza. Riprova."

### Dipendenze

- Nessuna

---

## US-ANA-005 - Creare nuova azienda di consulenza con primo admin-consulente (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** creare una nuova azienda di consulenza con almeno un admin-consulente
**In modo che** l'azienda possa iniziare a operare sulla piattaforma con un referente autorizzato

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Nuova azienda" dalla lista aziende di consulenza
**Allora** il sistema deve mostrare:

1. **Pagina creazione** con:
   - Titolo: "Nuovo"
   - Breadcrumb: "Aziende di consulenza > Nuovo"
   - Form diviso in sezioni:

#### SEZIONE 1: Dati Azienda

| Campo          | Tipo     | Label          | Validazione                    | Required |
| -------------- | -------- | -------------- | ------------------------------ | -------- |
| nome_azienda   | Text     | Nome azienda   | Max 255 char                   | Si       |
| indirizzo      | Text     | Indirizzo      | Max 255 char                   | Si       |
| p_iva          | Text     | P.IVA          | 11 cifre numeriche             | Si       |
| codice_fiscale | Text     | Codice fiscale | 11 o 16 caratteri alfanumerici | Si       |
| email          | Email    | Email          | Formato email valido           | Si       |
| telefono       | Tel      | Telefono       | Formato telefono valido        | Si       |
| note           | Textarea | Note           | Max 1000 char                  | No       |

**Nota informativa**:
"I dati dell'azienda identificano univocamente l'entità. La P.IVA e il Codice Fiscale devono essere univoci in piattaforma."

#### SEZIONE 2: Limiti (campi obbligatori)

| Campo               | Tipo   | Label                            | Validazione | Required |
| ------------------- | ------ | -------------------------------- | ----------- | -------- |
| max_aziende_clienti | Number | N. max di aziende clienti        | Integer > 0 | Si       |
| max_utenti_aziende  | Number | N. max di utenti aziende cliente | Integer > 0 | Si       |

**Nota informativa**:
"Questi limiti determinano il numero massimo di aziende clienti e utenti che l'azienda di consulenza potrà creare. Raggiunta la soglia, il sistema bloccherà la creazione. Se modificati successivamente, i valori devono essere >= alle entità già create per evitare inconsistenze."

#### SEZIONE 3: Primo Consulente (Admin-Consulente) - OBBLIGATORIO

Header sezione: **"Consulenti collegati"**
Sottotitolo: "Crea il primo admin-consulente dell'azienda (obbligatorio)"

| Campo    | Tipo  | Label    | Validazione                                  | Required |
| -------- | ----- | -------- | -------------------------------------------- | -------- |
| nome     | Text  | Nome     | Max 100 char                                 | Si       |
| cognome  | Text  | Cognome  | Max 100 char                                 | Si       |
| email    | Email | Email    | Formato email valido, univoca in piattaforma | Si       |
| telefono | Tel   | Telefono | Formato telefono valido                      | Si       |

**Nota informativa**:
"L'admin-consulente avrà accesso a tutte le aziende clienti create dall'azienda di consulenza, indipendentemente dalle assegnazioni esplicite. Riceverà un'email di benvenuto con credenziali temporanee per il primo accesso."

#### SEZIONE 4: Consulenti Aggiuntivi (Opzionale)

Pulsante: **"+ Aggiungi consulente"** (grigio chiaro)

Quando cliccato, aggiunge un nuovo blocco ripetibile con campi:

| Campo           | Tipo         | Label                   | Validazione                                  | Required                |
| --------------- | ------------ | ----------------------- | -------------------------------------------- | ----------------------- |
| nome            | Text         | Nome                    | Max 100 char                                 | Si (se blocco presente) |
| cognome         | Text         | Cognome                 | Max 100 char                                 | Si (se blocco presente) |
| email           | Email        | Email                   | Formato email valido, univoca in piattaforma | Si (se blocco presente) |
| telefono        | Tel          | Telefono                | Formato telefono valido                      | Si (se blocco presente) |
| isAdmin         | Checkbox     | Admin                   | True/False                                   | No                      |
| aziende_clienti | Multi-select | Assegna aziende clienti | Select multipla da aziende clienti esistenti | No                      |

**Ogni blocco consulente aggiuntivo ha**:

- Icona "X" (top-right) per rimuovere il blocco
- Scroll automatico al blocco appena aggiunto dopo il click su "+ Aggiungi consulente"

**Nota informativa**:
"I consulenti semplici (non admin-consulente) vedranno solo le aziende clienti a cui sono stati esplicitamente assegnati. Se non assegni aziende in questa fase, dovrai farlo successivamente tramite modifica consulente."

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

2. **Validare univocità email**:

   - Se email già esistente in piattaforma: mostrare errore "Email già registrata. Utilizza un'altra email."

3. **Se validazione OK**:
   - Creare record azienda di consulenza
   - Creare utente admin-consulente con:
     - Ruolo: "Admin Consulente"
     - Stato: "Attivo"
     - Linked a: azienda di consulenza appena creata
     - Invio email di benvenuto con credenziali temporanee
   - Creare eventuali consulenti aggiuntivi con:
     - Ruolo: "Consulente"
     - Stato: "Attivo"
     - Linked a: azienda di consulenza appena creata
     - Assegnazioni aziende clienti (se specificate)
     - Invio email di benvenuto con credenziali temporanee
   - Mostrare notifica di successo: "Azienda di consulenza creata con successo"
   - Redirect a listato aziende di consulenza

### Edge Cases

- **Email duplicata**: "Email già registrata. Utilizza un'altra email."
- **P.IVA duplicata**: "P.IVA già registrata. Verifica i dati inseriti."
- **Codice fiscale duplicato**: "Codice fiscale già registrato. Verifica i dati inseriti."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."
- **Aziende clienti selezionate per consulente aggiuntivo ma azienda non ha ancora clienti**: Il campo multi-select è vuoto con messaggio "Nessuna azienda cliente disponibile"

---

## US-ANA-006 - Visualizzare dettaglio azienda di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** visualizzare tutti i dettagli di un'azienda di consulenza
**In modo che** possa consultare le informazioni complete e accedere alle funzioni di gestione

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco dal menu contestuale "Dettaglio"
**Allora** il sistema deve mostrare:

1. **Pagina dettaglio** con:

   - Titolo: "Dettaglio"
   - Breadcrumb: "Aziende di consulenza > Dettaglio"
   - Pulsante "Gestisci informazioni" (arancione, top-right)

2. **Widget di navigazione rapida** (5 card orizzontali):

| Widget   | Icona         | Label                       | Azione Click                          |
| -------- | ------------- | --------------------------- | ------------------------------------- |
| Widget 1 | Icona aziende | Elenco aziende associate    | Apre sezione gestione aziende clienti |
| Widget 2 | Icona utenti  | Elenco consulenti collegati | Apre sezione gestione consulenti      |
| Widget 3 | -             | (vuoto)                     | -                                     |
| Widget 4 | -             | (vuoto)                     | -                                     |
| Widget 5 | -             | (vuoto)                     | -                                     |

**Ogni widget attivo ha**:

- Pulsante arancione: "Gestisci [entita]"
- Click su widget o pulsante: apre la rispettiva sezione

**Nota informativa**:
"I widget Widget 3, Widget 4 e Widget 5 sono riservati per funzionalità future (es: statistiche audit, compliance score, notifiche)."

3. **Sezione "Informazioni Anagrafiche"** (read-only):

**Layout**: Form a due colonne

| Campo          | Label          | Formato Display |
| -------------- | -------------- | --------------- |
| nome_azienda   | Nome azienda   | Text            |
| indirizzo      | Indirizzo      | Text            |
| p_iva          | Partita Iva    | Text            |
| codice_fiscale | Codice fiscale | Text            |
| email          | Email          | Text            |
| telefono       | Telefono       | Text            |
| note           | Note           | Textarea        |

**Pulsante azione** (bottom-right):

- **Gestisci informazioni** (arancione): apre form modifica

### Edge Cases

- **Errore caricamento**: Mostrare notifica "Impossibile caricare i dettagli. Riprova."
- **Azienda eliminata**: Se azienda non esiste più, redirect a lista con messaggio "Azienda non trovata"

---

## US-ANA-007 - Modificare dati azienda di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** modificare i dati di un'azienda di consulenza
**In modo che** possa aggiornare le informazioni quando necessario

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Gestisci informazioni" dalla pagina dettaglio o "Modifica" dal menu contestuale
**Allora** il sistema deve mostrare:

1. **Pagina modifica** con:

   - Titolo: "Modifica"
   - Breadcrumb: "Aziende di consulenza > [id] > Modifica"
   - Form con gli stessi campi di creazione, pre-compilati con i valori attuali

2. **Campi modificabili** (TUTTI i campi sono modificabili):

| Campo               | Tipo     | Label                            | Validazione                    | Required |
| ------------------- | -------- | -------------------------------- | ------------------------------ | -------- |
| nome_azienda        | Text     | Nome azienda                     | Max 255 char                   | Si       |
| indirizzo           | Text     | Indirizzo                        | Max 255 char                   | Si       |
| p_iva               | Text     | P.IVA                            | 11 cifre numeriche             | Si       |
| codice_fiscale      | Text     | Codice fiscale                   | 11 o 16 caratteri alfanumerici | Si       |
| email               | Email    | Email                            | Formato email valido           | Si       |
| telefono            | Tel      | Telefono                         | Formato telefono valido        | Si       |
| note                | Textarea | Note                             | Max 1000 char                  | No       |
| max_aziende_clienti | Number   | N. max di aziende clienti        | Integer > 0                    | Si       |
| max_utenti_aziende  | Number   | N. max di utenti aziende cliente | Integer > 0                    | Si       |

**Nota**: La sezione "Consulenti collegati" NON è presente in questa pagina

3. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): torna al dettaglio senza salvare
   - **Salva** (blu): valida e salva modifiche

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare tutti i campi** (stesse regole di creazione US-ANA-005)

2. **Validare limiti aziende/utenti rispetto a valori attuali**:

   - Se `max_aziende_clienti` < numero aziende clienti già create: mostrare errore "Non puoi impostare un limite inferiore al numero di aziende clienti già create (X). Aumenta il limite o rimuovi alcune aziende."
   - Se `max_utenti_aziende` < numero utenti aziende clienti già creati: mostrare errore "Non puoi impostare un limite inferiore al numero di utenti aziende clienti già creati (X). Aumenta il limite o rimuovi alcuni utenti."

3. **Se validazione OK**:
   - Aggiornare record azienda di consulenza
   - Mostrare notifica di successo: "Modifiche salvate con successo"
   - Redirect a pagina dettaglio

### Edge Cases

- **P.IVA duplicata** (se modificata): "P.IVA già registrata. Utilizza un'altra P.IVA."
- **Codice fiscale duplicato** (se modificato): "Codice fiscale già registrato. Utilizza un altro codice fiscale."
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova."
- **Riduzione limiti sotto soglia attuale**: Mostrare errore dettagliato con numero corrente vs nuovo limite

---

## US-ANA-008 - Gestire consulenti collegati all'azienda di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** gestire i consulenti collegati a un'azienda di consulenza
**In modo che** possa aggiungere, modificare o rimuovere consulenti e controllare i loro accessi

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Gestisci consulenti collegati" dal dettaglio azienda
**Allora** il sistema deve mostrare:

1. **Pagina gestione consulenti** con:
   - Titolo: "Consulenti collegati"
   - Breadcrumb: "Aziende di consulenza > Dettaglio > Consulenti"
   - Pulsante "Nuovo consulente" (arancione, top-right)
   - Filtri di ricerca (Nome, Cognome, Email, Ruolo)
   - Tabella paginata con colonne:

| Colonna              | Descrizione                                                            | Sortable |
| -------------------- | ---------------------------------------------------------------------- | -------- |
| Nome                 | Nome consulente                                                        | Si       |
| Cognome              | Cognome consulente                                                     | Si       |
| Email                | Email consulente                                                       | Si       |
| Telefono             | Telefono consulente                                                    | Si       |
| Ruolo                | "Admin Consulente" o "Consulente"                                      | Si       |
| N. Aziende assegnate | Contatore aziende clienti assegnate (0 per admin-consulente = "Tutte") | Si       |
| Creato il            | Data creazione DD/MM/YYYY                                              | Si       |
| Azioni               | Menu contestuale: Dettaglio, Modifica, Elimina                         | -        |

2. **Paginazione**: 10/25/50 rows per page (default: 10)

3. **Ordinamento default**:

   - Ordinamento applicato: colonna "Creato il" decrescente (più recenti prima)

4. **Indicatore ruolo**:
   - Admin-Consulente: badge blu "Admin"
   - Consulente: badge grigio "Consulente"

**Nota informativa**:
"Gli Admin-Consulente hanno accesso a tutte le aziende clienti dell'azienda di consulenza. I Consulenti semplici vedono solo le aziende a cui sono esplicitamente assegnati."

### Funzionalità: Aggiungere nuovo consulente

**Quando** clicco su "Nuovo consulente"
**Allora** il sistema deve mostrare pagina con form:

| Campo           | Tipo         | Label                   | Validazione                                                | Required |
| --------------- | ------------ | ----------------------- | ---------------------------------------------------------- | -------- |
| nome            | Text         | Nome                    | Max 100 char                                               | Si       |
| cognome         | Text         | Cognome                 | Max 100 char                                               | Si       |
| email           | Email        | Email                   | Formato email valido, univoca in piattaforma               | Si       |
| telefono        | Tel          | Telefono                | Formato telefono valido                                    | Si       |
| ruolo           | Select       | Ruolo                   | "Admin Consulente" o "Consulente"                          | Si       |
| aziende_clienti | Multi-select | Assegna aziende clienti | Select multipla (disabilitata se ruolo = Admin Consulente) | No       |

**Nota informativa**:

- Se ruolo = "Admin Consulente": mostrare "L'admin-consulente avrà accesso a tutte le aziende clienti" + disabilitare campo "Assegna aziende clienti"
- Se ruolo = "Consulente": abilitare campo "Assegna aziende clienti"

**Pulsanti**:

- **Annulla**: chiude dialog senza salvare
- **Salva**: crea nuovo consulente

**Comportamento salvataggio**:

1. Validare campi
2. Verificare univocità email
3. Creare utente con ruolo selezionato
4. Linkare a azienda di consulenza corrente
5. Assegnare aziende clienti (se consulente semplice)
6. Inviare email di benvenuto con credenziali temporanee
7. Mostrare notifica: "Consulente aggiunto con successo"
8. Aggiornare lista consulenti

### Funzionalità: Modificare consulente esistente

**Quando** clicco su "Modifica" dal menu contestuale di un consulente
**Allora** il sistema deve mostrare form con gli stessi campi di creazione, pre-compilati

**Comportamento salvataggio**:

1. Validare campi
2. Aggiornare dati consulente
3. Aggiornare assegnazioni aziende clienti (se consulente semplice)
4. Mostrare notifica: "Consulente modificato con successo"
5. Aggiornare lista consulenti

### Funzionalità: Eliminare consulente

**Quando** clicco su "Elimina" dal menu contestuale di un consulente
**Allora** il sistema deve:

1. **Verificare se consulente ha aziende clienti assegnate**:

   - Se SI: mostrare dialog di avviso:

     ```
     Attenzione!
     Il consulente [Nome Cognome] è collegato alle seguenti aziende clienti:
     - Azienda 1
     - Azienda 2
     - Azienda 3

     (max 5 aziende mostrate, se > 5 aggiungere "...e altre X aziende")

     Eliminando questo consulente, perderà l'accesso a tutte queste aziende.

     Sei sicuro di voler procedere?

     [Annulla] [Conferma eliminazione]
     ```

2. **Se conferma eliminazione**:

   - Disattivare utente (stato = "Disattivato")
   - Rimuovere assegnazioni aziende clienti
   - Mostrare notifica: "Consulente eliminato con successo"
   - Aggiornare lista consulenti

3. **Vincolo admin-consulente**:
   - Se è l'UNICO admin-consulente dell'azienda: mostrare errore "Impossibile eliminare l'unico admin-consulente. Crea un altro admin-consulente prima di procedere."

### Edge Cases

- **Email duplicata in creazione**: "Email già registrata. Utilizza un'altra email."
- **Nessuna azienda cliente disponibile**: Multi-select vuoto con messaggio "Nessuna azienda cliente disponibile"
- **Eliminazione ultimo admin**: Bloccare con errore esplicito
- **Consulente con audit attivi**: Bloccare con errore esplicito

---

## US-ANA-018 - Gestire aziende clienti associate all'azienda di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** visualizzare e gestire le aziende clienti associate a un'azienda di consulenza
**In modo che** possa controllare quali clienti sono collegati e gestire le associazioni

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Gestisci aziende" dal dettaglio azienda consulenza
**Allora** il sistema deve mostrare:

1. **Pagina gestione aziende associate** con:

   - Titolo: "Aziende clienti associate"
   - Breadcrumb: "Aziende di consulenza > Dettaglio > Aziende"
   - Pulsante "Crea azienda" (arancione, top-right)
   - Filtri di ricerca (Nome azienda, P.IVA, Referente)
   - Tabella paginata con colonne: vedi story US-ANA-009

2. **Paginazione**: 10/25/50 rows per page (default: 10)

3. **Ordinamento default**:
   - Ordinamento applicato: colonna "Creato il" decrescente (più recenti prima)

**Nota informativa**:
"Questa vista mostra tutte le aziende clienti associate all'azienda di consulenza corrente. Puoi associare aziende esistenti o rimuovere associazioni (senza eliminare l'azienda cliente stessa)."

4. **Crea Azienda**: riprende il flusso di creazione di azienda cliente: vedi story US-ANA-010

### Edge Cases

- **Nessuna azienda disponibile per associazione**: Disabilitare pulsante "Associa azienda" e mostrare messaggio informativo
- **Errore rimozione**: "Errore durante la rimozione dell'associazione. Riprova."

---

## US-ANA-019 - Eliminare azienda di consulenza con validazione vincoli (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** eliminare un'azienda di consulenza rispettando i vincoli di business
**In modo che** non vengano eliminate aziende con audit attivi e i dati siano preservati correttamente

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Elimina" dal menu contestuale di un'azienda di consulenza (lista o dettaglio)
**Allora** il sistema deve:

1. **Verificare vincoli di eliminazione**:

   - Controllare se esistono **audit attivi** presso le aziende clienti associate
   - Se SI: BLOCCARE eliminazione e mostrare messaggio di errore

2. **Mostrare messaggio di errore se audit attivi**:

   ```
   Impossibile eliminare l'azienda di consulenza

   Questa azienda ha audit attivi presso le seguenti aziende clienti:
   - [Azienda Cliente 1]: 3 audit attivi
   - [Azienda Cliente 2]: 1 audit attivo
   - [Azienda Cliente 3]: 5 audit attivi

   (max 5 aziende mostrate, se > 5 aggiungere "...e altre X aziende clienti")

   Completa o archivia tutti gli audit prima di procedere con l'eliminazione.

   [Chiudi]
   ```

3. **Se NON ci sono audit attivi**, mostrare dialog di conferma:

   ```
   Conferma eliminazione azienda di consulenza

   Stai per eliminare l'azienda di consulenza: [Nome Azienda]

   Questa operazione comporta:
   - Disattivazione di tutti i consulenti collegati (X consulenti)
   - Rimozione accessi all'azienda di consulenza
   - Le aziende clienti NON saranno eliminate e manterranno i loro dati

   Questa operazione NON è reversibile.

   Sei sicuro di voler procedere?

   [Annulla] [Conferma eliminazione]
   ```

4. **Se conferma eliminazione**:
   - Disattivare tutti i consulenti collegati (stato = "Disattivato")
   - Rimuovere tutte le associazioni azienda consulenza <-> aziende clienti
   - Eliminare (soft delete) record azienda di consulenza
   - Mostrare notifica: "Azienda di consulenza eliminata con successo"
   - Redirect a lista aziende di consulenza

### Edge Cases

- **Audit attivi**: BLOCCARE eliminazione con messaggio dettagliato
- **Errore eliminazione**: "Errore durante l'eliminazione. Riprova."
- **Azienda già eliminata**: Se nel frattempo è stata eliminata, mostrare "Azienda non trovata" e refresh lista

### Vincoli di Business

- **BLOCCO HARD**: Non è possibile eliminare azienda di consulenza con audit attivi
- **Soft delete**: L'azienda viene marcata come eliminata ma i record rimangono in DB per storico (flag `deleted_at`)
- **Preservazione dati clienti**: Le aziende clienti e tutti i loro dati (audit, fornitori, azioni) NON sono eliminati
- **Disattivazione consulenti**: I consulenti non possono più accedere ma i loro dati utente sono preservati per audit trail

**Nota informativa**:
"Il soft delete garantisce la tracciabilità storica delle operazioni. L'azienda non sarà più visibile nell'interfaccia ma i dati rimarranno in database per eventuali verifiche di compliance."

---

## US-ANA-022 - Ricercare e filtrare aziende di consulenza (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** ricercare e filtrare le aziende di consulenza
**In modo che** possa trovare rapidamente le aziende che mi interessano

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla pagina lista aziende di consulenza (US-ANA-004)
**Allora** il sistema deve mostrare una sezione filtri con:

1. **Filtri disponibili** (posizionati sopra la tabella):

| Campo Filtro       | Tipo     | Label                 | Placeholder             | Comportamento                                                                      |
| ------------------ | -------- | --------------------- | ----------------------- | ---------------------------------------------------------------------------------- |
| nome               | Text     | Nome                  | "Nome"                  | Ricerca case-insensitive, match parziale, debounce 300ms                           |
| cognome            | Text     | Cognome               | "Cognome"               | Ricerca case-insensitive, match parziale (su referente principale), debounce 300ms |
| azienda_consulenza | Dropdown | Azienda di consulenza | "Azienda di consulenza" | Select singola, match esatto                                                       |

**Nota informativa**:
"I filtri testuali applicano un debounce di 300ms per ottimizzare le performance. L'aggiornamento della tabella avverrà automaticamente dopo che smetti di digitare per 300ms."

2. **Pulsanti filtro**:

   - **Azzera filtri** (grigio, text-only): reset tutti i filtri
   - **Applica filtri** (blu): applica filtri e aggiorna tabella

3. **Comportamento filtri**:

   - I filtri lavorano in **AND** (tutti i filtri applicati devono essere soddisfatti)
   - Filtri testuali: match parziale case-insensitive con debounce 300ms
   - Dropdown: match esatto

4. **Indicatore filtri attivi**:
   - Mostrare badge con numero filtri attivi: "Filtri attivi: X"
   - Se nessun filtro attivo: non mostrare badge

### Comportamento Ricerca

**Quando** inserisco valori nei filtri e clicco "Applica filtri"
**Allora** il sistema deve:

1. Applicare tutti i filtri in AND
2. Aggiornare la tabella con i risultati filtrati
3. Mantenere l'ordinamento corrente
4. Reset paginazione a pagina 1
5. Mostrare numero risultati: "X risultati trovati"

**Se nessun risultato**:

- Mostrare messaggio: "Nessun risultato trovato. Modifica i filtri di ricerca."
- Mostrare pulsante "Azzera filtri"

### Comportamento Reset Filtri

**Quando** clicco su "Azzera filtri"
**Allora** il sistema deve:

1. Pulire tutti i campi filtro
2. Ricaricare la lista completa (senza filtri)
3. Mantenere ordinamento corrente
4. Reset paginazione a pagina 1
5. Nascondere badge "Filtri attivi"

### Edge Cases

- **Filtri vuoti + Applica**: Mostrare tutti i risultati (equivalente a "Azzera filtri")
- **Caratteri speciali nei filtri**: Sanificare input per evitare SQL injection
- **Filtri persistenti**: (opzionale) Mantenere filtri in session storage per back navigation
- **Performance con molti record**: Debounce 300ms già implementato su filtri testuali

### Dipendenze

- US-ANA-004 (lista aziende)

---

## US-ANA-020 - Visualizzare contatori dashboard filtrati per tenant (Admin di piattaforma e Consulente)

**Come** Admin di piattaforma o Consulente
**Voglio** visualizzare contatori statistici nella dashboard
**In modo che** possa avere una panoramica rapida dei dati rilevanti per il mio ruolo

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma o Consulente
**Quando** accedo alla Dashboard
**Allora** il sistema deve mostrare:

### Dashboard ADMIN di piattaforma (globale)

**3 Widget KPI** (card orizzontali con icone):

| Widget | Label                 | Valore   | Descrizione                                              | Trend                  |
| ------ | --------------------- | -------- | -------------------------------------------------------- | ---------------------- |
| 1      | Aziende registrate    | [Numero] | Totale aziende di consulenza registrate                  | +X% vs anno precedente |
| 2      | Consulenti registrati | [Numero] | Totale consulenti (admin + semplici) di tutte le aziende | +X% vs anno precedente |
| 3      | Azioni attive         | [Numero] | Totale azioni aperte in tutte le aziende clienti         | +X% vs anno precedente |

**Ogni widget mostra**:

- Icona rappresentativa (building, user, arrow)
- Label principale
- Valore numerico grande
- Trend percentuale con freccia (su/giù)
- Sfondo blu chiaro per icona

**Click su widget**: Naviga a sezione di dettaglio corrispondente

**Nota informativa**:
"Gli Admin di piattaforma vedono i dati aggregati di tutte le aziende di consulenza presenti nel sistema"

### Dashboard CONSULENTE (filtrata per tenant)

**3 Widget KPI** (card orizzontali con icone):

| Widget | Label           | Valore   | Descrizione                                                  | Trend                  |
| ------ | --------------- | -------- | ------------------------------------------------------------ | ---------------------- |
| 1      | Aziende clienti | [Numero] | Totale aziende clienti della MIA azienda di consulenza       | +X% vs anno precedente |
| 2      | Consulenti      | [Numero] | Totale consulenti della MIA azienda di consulenza            | +X% vs anno precedente |
| 3      | Azioni attive   | [Numero] | Totale azioni aperte nelle aziende clienti della MIA azienda | +X% vs anno precedente |

**Filtro tenant automatico**:

- Il sistema filtra automaticamente i dati in base all'azienda di consulenza di appartenenza dell'utente loggato
- NON è possibile vedere dati di altre aziende di consulenza
- Il filtro tenant è applicato a livello middleware per garantire segregazione dati

**Nota informativa**:
"I Consulenti vedono solo i dati relativi alla propria azienda di consulenza. Gli Admin-Consulente vedono tutte le aziende clienti dell'azienda, i Consulenti semplici vedono solo le aziende a cui sono assegnati."

### Comportamento Trend

**Calcolo trend**:

- Confronto con stesso periodo anno precedente
- Trend positivo: freccia verde su, +X%
- Trend negativo: freccia rossa giù, -X%
- Nessun trend: se dati anno precedente non disponibili, mostrare solo valore corrente

### Edge Cases

- **Primo anno operativo**: Se non ci sono dati anno precedente, mostrare solo valori correnti senza trend
- **Valori zero**: Mostrare "0" invece di nascondere il widget
- **Errore caricamento dati**: Mostrare widget con icona errore e messaggio "Dati non disponibili"

---

## US-ANA-021 - Bloccare creazione aziende/utenti al raggiungimento soglia massima (Sistema)

**Come** Sistema
**Voglio** bloccare la creazione di aziende clienti e utenti quando raggiunto il limite massimo
**In modo che** le aziende di consulenza rispettino i vincoli di licenza definiti

### Criteri di Accettazione

**Dato che** un'azienda di consulenza ha limiti definiti (`max_aziende_clienti`, `max_utenti_aziende`)
**Quando** un consulente tenta di creare una nuova azienda cliente o un nuovo utente azienda cliente
**Allora** il sistema deve:

### Scenario A: Creazione Azienda Cliente

1. **Prima di mostrare il form di creazione**, verificare:

   - Numero aziende clienti correnti < `max_aziende_clienti`

2. **Se limite NON raggiunto**:

   - Mostrare form di creazione normalmente
   - Mostrare messaggio informativo in alto: "Hai creato X di Y aziende clienti consentite. Puoi crearne ancora Z."

3. **Se limite RAGGIUNTO**:

   - Mostrare messaggio di blocco INVECE del form:

     ```
     Limite aziende clienti raggiunto

     Hai raggiunto il limite massimo di aziende clienti consentite (X aziende).

     Per creare nuove aziende clienti, contatta l'amministratore della piattaforma per aumentare il tuo limite.

     [Torna alla lista]
     ```

   - Disabilitare pulsante "Nuova azienda" nella lista con tooltip "Limite raggiunto"

**Nota informativa**:
"I limiti sono configurati dall'Admin di piattaforma nella sezione 'Limiti' dell'azienda di consulenza. Modificando i limiti, il blocco viene automaticamente aggiornato."

### Scenario B: Creazione Utente Azienda Cliente

1. **Prima di mostrare il form di creazione**, verificare:

   - Numero utenti aziende clienti correnti < `max_utenti_aziende`

2. **Se limite NON raggiunto**:

   - Mostrare form di creazione normalmente
   - Mostrare messaggio informativo in alto: "Hai creato X di Y utenti aziende clienti consentiti. Puoi crearne ancora Z."

3. **Se limite RAGGIUNTO**:

   - Mostrare messaggio di blocco INVECE del form:

     ```
     Limite utenti aziende clienti raggiunto

     Hai raggiunto il limite massimo di utenti aziende clienti consentiti (X utenti).

     Per creare nuovi utenti, contatta l'amministratore della piattaforma per aumentare il tuo limite.

     [Torna alla lista]
     ```

   - Disabilitare pulsante "Nuovo utente" nella lista con tooltip "Limite raggiunto"

### Indicatori Visivi nei Listing

**Nelle pagine lista** (aziende clienti, utenti aziende clienti):

- Mostrare sempre in alto a destra un badge informativo:
  - **Se abbondanza** (< 80% limite): Badge grigio "X / Y"
  - **Se soglia attenzione** (>= 80% limite): Badge arancione "X / Y" + tooltip "Attenzione: stai raggiungendo il limite"
  - **Se limite raggiunto** (100% limite): Badge rosso "X / Y (Limite raggiunto)"

**Nota informativa**:
"Il badge informativo è sempre visibile per monitorare l'utilizzo delle licenze. La soglia di attenzione all'80% permette di pianificare per tempo l'aumento dei limiti se necessario."

### Comportamento con Modifiche Limiti

**Se Admin di piattaforma modifica i limiti** :

- Se limiti aumentati: sbloccare automaticamente creazione e aggiornare badge
- Se limiti ridotti (ma > valori correnti): aggiornare indicatori senza bloccare
- Se limiti ridotti (< valori correnti): bloccare creazione e mostrare alert in tutte le pagine di creazione

### Edge Cases

- **Creazione multipla simultanea**: Validare limite anche lato backend al momento del save (race condition)
- **Eliminazione azienda/utente**: Aggiornare immediatamente contatori e sbloccare creazione se era bloccata
- **Limiti = 0**: Trattare come "nessun limite" (infinito)

---

## Riepilogo User Stories

| ID         | Titolo                                   | Complessità | Priorità |
| ---------- | ---------------------------------------- | ----------- | -------- |
| US-ANA-004 | Visualizzare lista aziende di consulenza | M           | MUST     |
| US-ANA-005 | Creare nuova azienda di consulenza       | H           | MUST     |
| US-ANA-006 | Visualizzare dettaglio azienda           | M           | MUST     |
| US-ANA-007 | Modificare dati azienda                  | M           | MUST     |
| US-ANA-008 | Gestire consulenti collegati             | H           | MUST     |
| US-ANA-018 | Gestire aziende clienti associate        | M           | MUST     |
| US-ANA-019 | Eliminare azienda con validazione        | H           | MUST     |
| US-ANA-022 | Ricercare e filtrare aziende             | M           | SHOULD   |
| US-ANA-020 | Visualizzare contatori dashboard         | M           | SHOULD   |
| US-ANA-021 | Bloccare creazione al limite             | H           | MUST     |

**Legenda Complessità**:

- L (Low): 1-3 giorni
- M (Medium): 3-5 giorni
- H (High): 5-8 giorni

**Legenda Priorità**:

- MUST: Funzionalità core, necessaria per MVP
- SHOULD: Funzionalità importante, migliora UX
- COULD: Funzionalità nice-to-have, differibile

---

## Note Tecniche per Sviluppo

### Validazioni Comuni

1. **Email**: Regex standard email + verifica univocità in piattaforma
2. **P.IVA**: 11 cifre numeriche + verifica univocità
3. **Codice Fiscale**: 11 o 16 caratteri alfanumerici + verifica univocità
4. **Telefono**: Formato internazionale (+39 xxx xxxxxxx)
5. **Limiti numerici**: Integer > 0

### Pattern UI Comuni

1. **Form layout**: 2 colonne responsive (1 colonna su mobile)
2. **Pulsanti azione**: Sempre bottom-right (Annulla + Azione primaria)
3. **Notifiche**: Toast top-right, auto-dismiss 5s
4. **Dialog conferma**: Modale centrato, overlay scuro 50%
5. **Menu contestuale**: Dropdown aligned right, 3 puntini verticali
6. **Debounce filtri testuali**: 300ms standard
7. **Scroll automatico**: Dopo operazioni di creazione/modifica, scroll all'elemento appena aggiunto/modificato
8. **Evidenziazione temporanea**: Bordo colorato per 2 secondi dopo modifica (verde) o creazione (blu)

### Regole Multi-tenancy

1. **Admin di piattaforma**: Vede TUTTE le aziende di consulenza (globale)
2. **Admin-Consulente**: Vede TUTTE le aziende clienti della propria azienda di consulenza
3. **Consulente**: Vede SOLO le aziende clienti a cui è assegnato
4. **Isolamento dati**: Ogni query filtra automaticamente per tenant (middleware)

### Gestione Stato Utenti

1. **Attivo**: Può loggarsi e operare normalmente
2. **Disattivato**: Non può loggarsi, sessioni invalidate
3. **Soft delete**: Record rimane in DB con flag `deleted_at` per audit trail

---

**Fine User Stories - Gestione Aziende di Consulenza**
