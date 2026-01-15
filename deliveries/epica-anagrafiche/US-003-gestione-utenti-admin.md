# User Stories - Gestione Utenti Admin

**Epica**: Anagrafiche
**Macro-argomento**: Gestione Utenti Admin
**Data**: 2025-12-11
**Versione**: 2.0

---

## Indice User Stories

- [US-ANA-001] Visualizzare lista unificata utenti (Admin)
- [US-ANA-002] Modal selezione tipo utente per creazione (Admin)
- [US-ANA-003] Creare Admin Piattaforma (Admin)
- [US-ANA-026] Modificare Admin Piattaforma (Admin)
- [US-ANA-027] Eliminare Admin Piattaforma con validazione vincoli (Admin)
- [US-ANA-009] Filtrare e ricercare utenti (Admin)

---

## US-ANA-001 - Visualizzare lista unificata utenti (Admin)

**Come** Admin di piattaforma
**Voglio** visualizzare una lista unificata di tutti gli utenti della piattaforma (Consulenti, Utenti Aziendali, Admin)
**In modo che** possa avere una panoramica completa di tutti gli utenti e gestirli centralmente

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla sezione "Utenti" dal menu principale
**Allora** il sistema deve mostrare:

1. **Pagina lista utenti** con:

   - Titolo pagina: "Utenti"
   - Breadcrumb: "Utenti"
   - Pulsante "Crea Nuovo Utente"
   - Filtri di ricerca
   - Tabella paginata con le seguenti colonne:
     - **Nome** (Nome utente, sortable)
     - **Cognome** (Cognome utente, sortable)
     - **Email** (Email utente, sortable)
     - **Telefono** (Telefono utente, sortable)
     - **Tipo Utente** (Badge colorato, sortable)
     - **Data Creazione** (Data creazione formato DD/MM/YYYY, sortable)
     - **Azioni** (Menu contestuale: Dettaglio, Modifica, Elimina)

2. **Badge Tipo Utente** (colonne "Tipo Utente"):

   - **Consulente** (badge blu): utenti con ruolo "Admin Consulente" o "Consulente"
   - **Cliente** (badge verde): utenti con ruolo "Admin Cliente" o "Cliente"
   - **Admin** (badge rosso): utenti con ruolo "Admin Piattaforma"

3. **Comportamento click su azioni**:

   **A. Click su Modifica (icona matita) su riga CONSULENTE**:

   1. Sistema identifica l'id del consulente
   2. Redirect a: `Aziende di consulenza > Dettaglio [Nome Azienda] > Consulenti collegati > [ID Consulente]`

   **B. Click su Modifica (icona matita) su riga UTENTE AZIENDALE**:

   1. Sistema identifica l'id del cliente
   2. Redirect a: `Aziende Clienti > Dettaglio [Nome Azienda] > Utenti Aziendali > [ID Cliente]`

   **C. Click su Modifica (icona matita) su riga ADMIN PIATTAFORMA**:

   1. Redirect a: `Utenti > [ID Admin]`

   **D. Click su Elimina (icona cestino) su riga CONSULENTE**:

   1. Trigger automatico dialog eliminazione consulente

   **E. Click su Elimina (icona cestino) su riga UTENTE AZIENDALE**:

   1. Trigger automatico dialog eliminazione utente aziendale

   **F. Click su Elimina (icona cestino) su riga ADMIN PIATTAFORMA**:

   1. Sistema apre dialog eliminazione Admin

4. **Ordinamento default**:

   - Ordinamento applicato: colonna "Data Creazione" decrescente (più recenti prima)

5. **Paginazione**:

   - Rows per page: 10 (default), con opzioni 10/25/50
   - Indicatore "X-Y di Z" (es. "1-4 di 4")
   - Frecce navigazione prev/next

6. **Stato vuoto**:

   - Se non ci sono utenti (caso impossibile, esiste almeno Admin loggato): mostrare messaggio "Nessun utente trovato" + pulsante "Crea primo utente"

7. **Indicatore utente corrente**:
   - La riga corrispondente all'Admin loggato deve avere:
     - Badge aggiuntivo "Tu" (grigio) accanto al badge Tipo Utente
     - Icona Elimina disabilitata (grigio) con tooltip "Non puoi eliminare te stesso"

### Edge Cases

- **Nessun risultato filtri**: Se i filtri non restituiscono risultati, mostrare "Nessun risultato trovato. Modifica i filtri di ricerca."
- **Errore caricamento dati**: Mostrare notifica di errore "Impossibile caricare gli utenti. Riprova."
- **Ordinamento default**: Ordinamento default per "Data Creazione" decrescente (più recenti prima)
- **Consulente con azienda eliminata**: Se l'azienda di consulenza del consulente è stata eliminata, disabilitare azioni Modifica con tooltip "Azienda di consulenza non più disponibile"
- **Utente aziendale con azienda eliminata**: Se l'azienda cliente dell'utente è stata eliminata, disabilitare azioni Modifica con tooltip "Azienda cliente non più disponibile"

### Dipendenze

- Sistema autenticazione (per rilevare utente loggato e ruolo Admin)
- US-001.5 (gestione consulenti in Aziende di Consulenza)
- US-002 (gestione utenti aziendali in Aziende Clienti)
- US-ANA-026 (modifica Admin Piattaforma)
- US-ANA-027 (eliminazione Admin Piattaforma)

---

## US-ANA-002 - Modal selezione tipo utente per creazione (Admin)

**Come** Admin di piattaforma
**Voglio** selezionare il tipo di utente che desidero creare
**In modo che** possa essere indirizzato al flusso di creazione appropriato (Consulente, Utente Aziendale, Admin)

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Crea Nuovo Utente" dalla lista utenti
**Allora** il sistema deve mostrare:

1. **Modal "Crea Nuovo Utente"** con:
   - Titolo: "Seleziona tipo di utente"
   - Sottotitolo: "Scegli il tipo di utente che vuoi creare"
   - Form con campo:

#### CAMPO: Tipo di utente (Radio Buttons)

| Opzione           | Label             | Icona     | Descrizione Helper                                                            |
| ----------------- | ----------------- | --------- | ----------------------------------------------------------------------------- |
| consulente        | Consulente        | briefcase | "Utente di un'azienda di consulenza (Admin Consulente o Consulente semplice)" |
| utente_aziendale  | Utente Aziendale  | building  | "Utente di un'azienda cliente (Admin Cliente o Cliente semplice)"             |
| admin_piattaforma | Admin Piattaforma | shield    | "Amministratore con accesso completo alla piattaforma"                        |

2. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): chiude modal senza azione
   - **Avanti** (blu): procede con creazione (disabilitato se nessuna selezione)

### Scenario A: Selezione "Consulente"

**Quando** seleziono "Consulente" e clicco "Avanti"
**Allora** il sistema deve:

1. Chiudere modal "Crea Nuovo Utente"
2. Redirect a pagina: `Aziende di consulenza`
3. Mostrare messaggio informativo top-page: "Seleziona l'azienda di consulenza per cui vuoi creare un nuovo consulente"
4. Quando Admin seleziona un'azienda:
   - Naviga a dettaglio azienda
   - Clicca su widget "Elenco consulenti collegati"
   - Clicca su "Nuovo consulente"
   - Segue flusso standard creazione consulente

### Scenario B: Selezione "Utente Aziendale"

**Quando** seleziono "Utente Aziendale" e clicco "Avanti"
**Allora** il sistema deve:

1. Chiudere modal "Crea Nuovo Utente"
2. Redirect a pagina: `Aziende Clienti`
3. Mostrare messaggio informativo top-page: "Seleziona l'azienda cliente per cui vuoi creare un nuovo utente"
4. Quando Admin seleziona un'azienda:
   - Naviga a dettaglio azienda
   - Accede a sezione "Utenti Aziendali"
   - Clicca su "Aggiungi Utente"
   - Segue flusso standard creazione utente aziendale

### Scenario C: Selezione "Admin Piattaforma"

**Quando** seleziono "Admin Piattaforma" e clicco "Avanti"
**Allora** il sistema deve:

1. Redirect a `Utenti > Nuovo`
2. Mostrare form con 4 campi (Nome, Cognome, Email, Telefono)
3. Pulsanti cambiano: "Indietro" + "Salva"

### Edge Cases

- **Nessuna selezione + Avanti**: Pulsante "Avanti" disabilitato (grigio) con tooltip "Seleziona un tipo di utente per procedere"
- **Annulla**: Chiude modal senza azione, ritorna a lista utenti
- **Cambio selezione**: Permettere di cambiare radio button prima di cliccare "Avanti"
- **Escape key**: Chiude modal (equivalente ad "Annulla")

---

## US-ANA-003 - Creare Admin Piattaforma (Admin)

**Come** Admin di piattaforma
**Voglio** creare un nuovo Admin Piattaforma
**In modo che** possa delegare funzioni amministrative ad altri utenti autorizzati

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** seleziono "Admin Piattaforma" nella modal di selezione tipo e clicco "Avanti"
**Allora** il sistema deve:

1. **Fare Redirect a `Utenti > Nuovo`"** con:
   - Titolo: "Crea Admin Piattaforma"
   - Sottotitolo: "Inserisci i dati del nuovo amministratore"
   - Form con 4 campi:

#### SEZIONE: Dati Amministratore

| Campo    | Tipo  | Label    | Validazione                                              | Required |
| -------- | ----- | -------- | -------------------------------------------------------- | -------- |
| nome     | Text  | Nome     | Max 100 char, solo caratteri alfabetici e spazi          | Si       |
| cognome  | Text  | Cognome  | Max 100 char, solo caratteri alfabetici e spazi          | Si       |
| email    | Email | Email    | Formato email valido, univoca globalmente in piattaforma | Si       |
| telefono | Tel   | Telefono | Formato telefono valido (es: +39 02 1234567)             | No       |

2. **Pulsanti azione** (bottom-right):
   - **Annulla** (outline): torna a selezione tipo utente
   - **Salva** (blu): valida e salva

### Comportamento Salvataggio

**Quando** clicco su "Salva"
**Allora** il sistema deve:

1. **Validare tutti i campi**:

   - **Nome**:
     - Required: "Il campo Nome e obbligatorio"
     - Max 100 char: "Il Nome non puo superare 100 caratteri"
     - Solo alfabetici e spazi: "Il Nome puo contenere solo lettere e spazi"
   - **Cognome**:
     - Required: "Il campo Cognome e obbligatorio"
     - Max 100 char: "Il Cognome non puo superare 100 caratteri"
     - Solo alfabetici e spazi: "Il Cognome puo contenere solo lettere e spazi"
   - **Email**:
     - Required: "Il campo Email e obbligatorio"
     - Formato email: "Inserisci un indirizzo email valido"
     - Univocita globale: "Email gia registrata. Utilizza un'altra email."
   - **Telefono** (se compilato):
     - Formato valido: "Inserisci un numero di telefono valido (es: +39 02 1234567)"

2. **Se validazione FAIL**:

   - Mostrare errori inline sotto ogni campo con errore
   - Evidenziare campi con errore con bordo rosso
   - NON salvare

3. **Se validazione OK**:

   - Creare nuovo record utente con:

     - Ruolo: "Admin Piattaforma"
     - Stato: "Attivo"
     - Nome: valore inserito
     - Cognome: valore inserito
     - Email: valore inserito
     - Telefono: valore inserito (o null se vuoto)

   - Inviare email invito a [email] con:

   - Mostrare notifica success toast bottom-left, verde, 5s):
     "Admin Piattaforma creato con successo. Email di benvenuto inviata a [email]"

   - Refresh lista utenti con nuovo Admin visibile in prima posizione

### Edge Cases

- **Email duplicata**: "Email gia registrata. Utilizza un'altra email." (messaggio rosso sotto campo Email)
- **Errore salvataggio DB**: "Errore durante il salvataggio. Riprova." (notifica toast rossa)
- **Caratteri speciali in Nome/Cognome**: Permettere caratteri accentati (à, è, ì, etc.) ma bloccare numeri e simboli

---

## US-ANA-026 - Modificare Admin Piattaforma (Admin)

**Come** Admin di piattaforma
**Voglio** modificare i dati di un Admin Piattaforma esistente
**In modo che** possa aggiornare le informazioni quando necessario (tranne l'email che rimane immutabile)

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Modifica" (icona matita) su una riga con Tipo Utente "Admin" nella lista
**Allora** il sistema deve mostrare:

1. **Pagina "Modifica Admin Piattaforma"** con:
   - Titolo: "Modifica Admin Piattaforma"
   - Sottotitolo: "Aggiorna i dati dell'amministratore"
   - Form con 4 campi pre-compilati:

#### SEZIONE: Dati Amministratore

| Campo    | Tipo | Label    | Validazione                                     | Required | Modificabile   |
| -------- | ---- | -------- | ----------------------------------------------- | -------- | -------------- |
| nome     | Text | Nome     | Max 100 char, solo caratteri alfabetici e spazi | Si       | Si             |
| cognome  | Text | Cognome  | Max 100 char, solo caratteri alfabetici e spazi | Si       | Si             |
| email    | Text | Email    | -                                               | N/A      | NO (read-only) |
| telefono | Tel  | Telefono | Formato telefono valido                         | No       | Si             |

2. **Pulsanti azione** (bottom-right):
   - **Annulla** (grigio, outline): chiude modal senza salvare
   - **Salva** (blu): valida e salva modifiche

### Edge Cases

- **Nessuna modifica**: Se clicco "Salva" senza modificare alcun campo:
  - Salvare comunque (aggiornare `modificato_il`)
  - Mostrare notifica: "Modifiche salvate con successo" (anche se nessun cambiamento)
- **Errore salvataggio**: "Errore durante il salvataggio. Riprova." (toast rosso)
- **Admin eliminato da altro utente nel frattempo**:
  - Tentativo salvataggio: errore "Admin non trovato o eliminato
  - Refresh lista (Admin non appare piu)
- **Modifica del proprio account**: Permettere modifica (no restrizioni) tranne email
- **Caratteri speciali in Nome/Cognome**: Stesso comportamento di creazione (accenti ok, numeri no)

---

## US-ANA-027 - Eliminare Admin Piattaforma con validazione vincoli (Admin)

**Come** Admin di piattaforma
**Voglio** eliminare un Admin Piattaforma rispettando vincoli di sicurezza
**In modo che** non possa eliminare me stesso ne l'ultimo Admin attivo della piattaforma

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** clicco su "Elimina" (icona cestino) su una riga con Tipo Utente "Admin" nella lista (US-ANA-001)
**Allora** il sistema deve:

### FASE 1: Verificare vincoli di eliminazione

1. **Vincolo 1: Auto-eliminazione**

   - Controllare se l'Admin selezionato corrisponde all'Admin loggato
   - Se SI: BLOCCARE eliminazione

2. **Vincolo 2: Ultimo Admin attivo**
   - Contare numero di Admin Piattaforma con stato "Attivo"
   - Se count = 1: BLOCCARE eliminazione

### FASE 2A: Blocco per auto-eliminazione (Vincolo 1 violato)

**Se** Admin tenta di eliminare se stesso
**Allora** mostrare dialog errore:

```
Operazione non consentita

Non puoi eliminare il tuo stesso account.

Per rimuovere questo account, chiedi a un altro Amministratore di Piattaforma di procedere con l'eliminazione.

[Chiudi]
```

### FASE 2B: Blocco per ultimo Admin (Vincolo 2 violato)

**Se** Admin e l'unico Admin attivo
**Allora** mostrare dialog errore:

```
Impossibile eliminare l'Admin

Questo e l'unico Amministratore di Piattaforma attivo.

Per procedere con l'eliminazione:
1. Crea almeno un altro Admin Piattaforma
2. Verifica che il nuovo Admin sia attivo
3. Riprova l'eliminazione

[Chiudi]
```

### FASE 2C: Conferma eliminazione (Vincoli OK)

**Se** entrambi i vincoli sono rispettati
**Allora** mostrare dialog conferma:

```
Conferma eliminazione Admin Piattaforma

Stai per eliminare l'Amministratore:
- Nome: [Nome] [Cognome]
- Email: [email]
- Data Creazione: [DD/MM/YYYY]

Questa operazione comporta:
• Disattivazione immediata dell'accesso alla piattaforma
• Invalidazione di tutte le sessioni attive dell'utente
• L'utente non potra piu effettuare login


Questa operazione NON e reversibile.

Sei sicuro di voler procedere?

[Annulla] [Conferma eliminazione]
```

### FASE 3: Esecuzione eliminazione

**Quando** clicco su "Conferma eliminazione"
**Allora** il sistema deve:

1. **Soft delete Admin**:

   - Impostare stato: "Disattivato"
   - Impostare flag: `deleted_at = timestamp corrente`
   - Impostare: `deleted_by = ID Admin loggato`
   - NON cancellare fisicamente il record dal database

2. **Notifica e refresh**:
   - Chiudere dialog conferma
   - Mostrare notifica success toast: "Admin Piattaforma eliminato con successo"
   - Refresh lista utenti (Admin eliminato NON appare piu nella lista)

### Edge Cases

- **Auto-eliminazione**: BLOCCARE HARD con dialog errore
- **Ultimo Admin**: BLOCCARE HARD con dialog errore
- **Errore eliminazione DB**: "Errore durante l'eliminazione. Riprova." (toast rosso)
- **Admin gia eliminato da altro utente**:
  - Tentativo eliminazione: errore "Admin non trovato o gia eliminato"
  - Refresh lista automatico
- **Click Annulla nel dialog conferma**: Chiudere dialog, NO eliminazione, tornare a lista
- **Admin disattivato ma non deleted**: Permettere eliminazione (soft delete anche se gia disattivato)
- **Ripristino Admin eliminato**: NON previsto in MVP (feature futura)

### Vincoli di Business

- **BLOCCO HARD 1**: Non e possibile eliminare se stesso
- **BLOCCO HARD 2**: Non e possibile eliminare l'ultimo Admin attivo
- **Soft delete**: Record rimane in DB con flag `deleted_at` per audit trail
- **Preservazione audit**: Tutti i dati storici creati dall'Admin rimangono intatti
- **Invalidazione immediata**: Sessioni attive invalidate entro 1 secondo

---

## US-ANA-009 - Filtrare e ricercare utenti (Admin di piattaforma)

**Come** Admin di piattaforma
**Voglio** filtrare e ricercare utenti nella lista unificata
**In modo che** possa trovare rapidamente utenti specifici tra centinaia di record

### Criteri di Accettazione

**Dato che** sono loggato come Admin di piattaforma
**Quando** accedo alla lista utenti (US-ANA-001)
**Allora** il sistema deve mostrare una sezione filtri sopra la tabella con:

1. **Sezione Filtri** (posizionata tra pulsante "Crea Nuovo Utente" e tabella):

#### Filtro 1: Tipo Utente (Multi-select Checkbox)

**Layout**: Checkbox orizzontali inline

| Checkbox   | Label      | Icona            | Default |
| ---------- | ---------- | ---------------- | ------- |
| consulente | Consulente | briefcase (blu)  | Checked |
| cliente    | Cliente    | building (verde) | Checked |
| admin      | Admin      | shield (rosso)   | Checked |

**Comportamento**:

- Tutti checkbox selezionati di default (mostra tutti gli utenti)
- Click su checkbox: toggle selezione
- Almeno 1 checkbox deve rimanere selezionato (se deseleziono tutti, il sistema riseleziona tutti automaticamente)
- Logica: OR tra valori selezionati (es: se seleziono Consulente + Admin, mostra entrambi)

#### Filtro 2: Ricerca Globale (Text Input)

**Campo**: Input text con icona search (lente)

| Campo           | Tipo | Placeholder                                    | Comportamento                   |
| --------------- | ---- | ---------------------------------------------- | ------------------------------- |
| ricerca_globale | Text | "Cerca per Nome, Cognome, Email o Telefono..." | Match parziale case-insensitive |

**Ricerca applica su**:

- Nome (match parziale)
- Cognome (match parziale)
- Email (match parziale)
- Telefono (match parziale)

**Logica**: OR tra campi (se inserisco "mario", cerca in tutti e 4 i campi)

**Debounce**: 300ms (attende che l'utente finisca di digitare prima di applicare filtro)

**Nota informativa**:
"Il debounce di 300ms ottimizza le performance evitando troppe richieste al server durante la digitazione. L'aggiornamento della tabella avviene automaticamente dopo 300ms dall'ultimo carattere digitato."

2. **Pulsanti Filtro** (posizionati a destra dei filtri):

   - **Azzera filtri** (grigio chiaro, text-only, icona X): reset tutti filtri
   - **Applica filtri** (blu, icona check): applica filtri manualmente (alternativo a debounce)

3. **Indicatore Filtri Attivi**:
   - Badge blu con numero: "Filtri attivi: X"
   - Posizionato sotto la riga filtri, allineato a sinistra
   - Mostrare SOLO se almeno 1 filtro attivo (NON default)
   - Calcolo:
     - Se Tipo Utente != tutti selezionati: +1
     - Se Ricerca Globale compilata: +1
   - Click su badge: equivalente a "Azzera filtri"

### Comportamento Applicazione Filtri

**Quando** modifico i filtri (checkbox, ricerca globale) o clicco "Applica filtri"
**Allora** il sistema deve:

1. **Applicare logica filtri**:

   - **AND tra Tipo Utente e Ricerca Globale**:

     - Esempio: se seleziono "Consulente" + ricerca "mario" → mostra solo Consulenti con "mario" in nome/cognome/email/telefono

   - **OR all'interno di Tipo Utente**:

     - Esempio: se seleziono "Consulente + Admin" → mostra Consulenti OR Admin

   - **OR all'interno di Ricerca Globale**:
     - Esempio: se cerco "mario" → mostra utenti con "mario" in (nome OR cognome OR email OR telefono)

2. **Aggiornare tabella**:

   - Applicare filtri al dataset
   - Mantenere ordinamento corrente (sortable columns)
   - Reset paginazione a pagina 1
   - Mostrare numero risultati: "X risultati trovati"

3. **Gestire stato vuoto**:
   - **Se nessun risultato**:
     - Mostrare messaggio: "Nessun risultato trovato. Modifica i filtri di ricerca."
     - Mostrare pulsante prominente "Azzera filtri"
     - NON mostrare tabella vuota

### Comportamento Reset Filtri

**Quando** clicco su "Azzera filtri" o sul badge "Filtri attivi"
**Allora** il sistema deve:

1. **Reset tutti i filtri**:

   - Selezionare tutti i checkbox Tipo Utente
   - Svuotare campo Ricerca Globale
   - Nascondere badge "Filtri attivi"

2. **Ricaricare lista completa**:
   - Mostrare tutti gli utenti (senza filtri)
   - Mantenere ordinamento corrente
   - Reset paginazione a pagina 1
   - Aggiornare contatore risultati

### Edge Cases

- **Filtri vuoti + Applica**: Mostrare tutti i risultati (equivalente a "Azzera filtri")
- **Tutti checkbox Tipo Utente deselezionati**: Sistema riseleziona automaticamente tutti i checkbox + mostra tooltip "Almeno un tipo utente deve essere selezionato"
- **Caratteri speciali in Ricerca Globale**: Sanificare input per evitare SQL injection (escape caratteri speciali)
- **Ricerca con risultato singolo**: Mostrare normalmente in tabella (no redirect automatico)
- **Performance con >1000 utenti**:
  - Implementare debounce 300ms su ricerca testuale
  - Applicare filtri lato backend (no filter client-side)
  - Paginazione server-side
- **Filtri persistenti** (opzionale MVP): Salvare filtri in session storage per back navigation
- **Combinazione filtri complessa**: Es: "Consulente + ricerca mario + ordinamento per email" → sistema deve applicare correttamente tutti i criteri
- **Clear ricerca con X nel campo**: Mostrare icona X a destra del campo quando compilato, click rimuove testo e applica filtro vuoto

### Dipendenze

- US-ANA-001 (lista utenti da filtrare)

---

## Riepilogo User Stories

| ID         | Titolo                              | Complessita | Priorita |
| ---------- | ----------------------------------- | ----------- | -------- |
| US-ANA-001 | Visualizzare lista unificata utenti | H           | MUST     |
| US-ANA-002 | Modal selezione tipo utente         | M           | MUST     |
| US-ANA-003 | Creare Admin Piattaforma            | M           | MUST     |
| US-ANA-026 | Modificare Admin Piattaforma        | L           | MUST     |
| US-ANA-027 | Eliminare Admin con validazione     | M           | MUST     |
| US-ANA-009 | Filtrare e ricercare utenti         | M           | SHOULD   |

**Legenda Complessita**:

- L (Low): 1-3 giorni
- M (Medium): 3-5 giorni
- H (High): 5-8 giorni

**Legenda Priorita**:

- MUST: Funzionalita core, necessaria per MVP
- SHOULD: Funzionalita importante, migliora UX
- COULD: Funzionalita nice-to-have, differibile

---

## Note Tecniche per Sviluppo

### Validazioni Comuni

1. **Email**:

   - Regex: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
   - Verifica univocita globale in tabella `users` (tutti i ruoli)
   - Case-insensitive (normalizzare a lowercase prima di salvare)

2. **Telefono**:

   - Formato internazionale: `+[codice paese] [numero]`
   - Esempio valido: `+39 02 1234567`, `+39 348 1234567`
   - Regex: `/^\+\d{1,3}\s\d{2,4}\s\d{6,10}$/`

3. **Nome/Cognome**:

   - Max 100 caratteri
   - Solo caratteri alfabetici, spazi, accenti (à, è, ì, ò, ù)
   - NO numeri, NO simboli (tranne apostrofo per nomi come "D'Angelo")
   - Regex: `/^[a-zA-ZÀ-ÿ\s']{1,100}$/`

4. **Ricerca Globale**:
   - Match parziale case-insensitive
   - Escape caratteri speciali SQL: `'`, `"`, `;`, `--`, etc.
   - Utilizzare prepared statements

### Pattern UI Comuni

1. **Modal**:

   - Larghezza max: 600px
   - Centrato verticalmente e orizzontalmente
   - Overlay scuro: `rgba(0,0,0,0.5)`
   - Chiusura: click fuori (se no modifiche), Escape key, icona X top-right
   - Animazione: fade-in 200ms

2. **Pulsanti**:

   - Posizione: bottom-right
   - Spacing: 16px tra pulsanti
   - Ordine: Secondario (outline) | Primario (pieno)
   - Colori:
     - Primario blu: `#1976D2`
     - Secondario grigio: `#757575`
     - Elimina rosso: `#D32F2F`
     - Annulla outline: `border: 1px solid #757575`

3. **Notifiche Toast**:

   - Posizione: top-right
   - Durata: 5 secondi (auto-dismiss)
   - Larghezza: 400px max
   - Colori:
     - Success verde: `#4CAF50`
     - Error rosso: `#F44336`
     - Warning arancione: `#FF9800`
     - Info blu: `#2196F3`
   - Icone: check, error, warning, info

4. **Badge Tipo Utente**:

   - **Consulente**:
     - Background: `#E3F2FD` (blu chiaro)
     - Testo: `#1565C0` (blu scuro)
     - Icona: `briefcase`
   - **Cliente**:
     - Background: `#E8F5E9` (verde chiaro)
     - Testo: `#2E7D32` (verde scuro)
     - Icona: `building`
   - **Admin**:
     - Background: `#FFEBEE` (rosso chiaro)
     - Testo: `#C62828` (rosso scuro)
     - Icona: `shield`
   - Dimensioni: padding `4px 12px`, border-radius `16px`, font-size `12px`, font-weight `600`

5. **Tabella**:
   - Header: background grigio chiaro `#F5F5F5`, testo bold
   - Righe: alternanza bianco/grigio `#FAFAFA` (zebra striping)
   - Hover riga: background `#E0E0E0`
   - Sortable columns: icona freccia su/giu, click toggle ordinamento
   - Azioni: menu dropdown aligned right con icone matita/cestino

### Regole Multi-tenancy

1. **Admin Piattaforma**:

   - Vede TUTTI gli utenti di TUTTI i tenant (Aziende Consulenza + Aziende Clienti)
   - NO filtro tenant applicato nelle query
   - Flag: `is_platform_admin = true`

2. **Lista Unificata**:

   - Include: Consulenti (Admin Consulente + Consulente) + Utenti Aziendali (Admin Cliente + Cliente) + Admin Piattaforma
   - Query JOIN su tabelle: `users` LEFT JOIN `aziende_consulenza` LEFT JOIN `aziende_clienti`

3. **Gestione Isolamento**:
   - Consulenti: modificabili solo tramite sezione Aziende Consulenza
   - Utenti Aziendali: modificabili solo tramite sezione Aziende Clienti
   - Admin Piattaforma: modificabili direttamente in modal (no tenant)

### Gestione Stato Utenti

1. **Stati possibili**:

   - **Attivo**: `status = 'active'`, `deleted_at = null`
   - **Disattivato**: `status = 'inactive'`, `deleted_at = null` (disattivazione manuale)
   - **Eliminato (soft)**: `status = 'inactive'`, `deleted_at = timestamp` (soft delete)

2. **Soft Delete**:

   - Campo: `deleted_at` (timestamp nullable)
   - Campo: `deleted_by` (foreign key a `users.id`)
   - Record NON cancellato fisicamente
   - Query default: `WHERE deleted_at IS NULL` (escludi eliminati)
   - Preservazione audit trail completo

3. **Invalidazione Sessioni**:
   - Meccanismo: token revocation list (Redis o DB)
   - Quando: eliminazione utente, cambio password, logout forzato
   - Verifica: ogni richiesta API controlla se token e valido
   - TTL sessioni: 24 ore (rinnovate ad ogni attivita)

### Query Performance

1. **Indici Database** (raccomandati):

   - `users.email` (UNIQUE)
   - `users.deleted_at` (per filtrare soft delete)
   - `users.status` (per filtrare per stato)
   - `users.created_at` (per ordinamento default)
   - `users.role` (per filtrare per tipo utente)

2. **Paginazione**:

   - Server-side: `LIMIT` + `OFFSET`
   - Client: mostra "X of Y results"
   - Ottimizzazione: conteggio totale cachato (refresh ogni 5 min)

3. **Filtri**:
   - Debounce 300ms su ricerca testuale (evita query eccessive)
   - Prepared statements (prevenzione SQL injection)
   - Full-text search (se disponibile) per ricerca globale performante

### Email Template

**Template "Benvenuto Admin Piattaforma"**:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Benvenuto su Piattaforma Conformita NIS2</title>
  </head>
  <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div
      style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;"
    >
      <h2 style="color: #1976D2;">Benvenuto su Piattaforma Conformita NIS2</h2>

      <p>Gentile <strong>{{nome}} {{cognome}}</strong>,</p>

      <p>
        Benvenuto sulla Piattaforma Conformita NIS2. Sei stato registrato come
        <strong>Amministratore di Piattaforma</strong>.
      </p>

      <div
        style="background-color: #f5f5f5; padding: 15px; border-radius: 4px; margin: 20px 0;"
      >
        <h3 style="margin-top: 0;">
          Le tue credenziali di accesso temporanee:
        </h3>
        <p><strong>Email:</strong> {{email}}</p>
        <p>
          <strong>Password:</strong>
          <code
            style="background-color: #fff; padding: 2px 6px; border: 1px solid #ddd;"
            >{{password_temporanea}}</code
          >
        </p>
      </div>

      <div
        style="background-color: #fff3cd; padding: 15px; border-left: 4px solid #ff9800; margin: 20px 0;"
      >
        <h4 style="margin-top: 0; color: #ff9800;">
          IMPORTANTE - Primi passi:
        </h4>
        <ol style="margin-bottom: 0;">
          <li>
            Accedi alla piattaforma:
            <a href="{{url_piattaforma}}" style="color: #1976D2;"
              >{{url_piattaforma}}</a
            >
          </li>
          <li>
            Al primo accesso ti verra chiesto di
            <strong>cambiare la password</strong>
          </li>
          <li>
            Dovrai configurare l'<strong
              >autenticazione a due fattori (MFA)</strong
            >
            obbligatoria
          </li>
        </ol>
      </div>

      <p>Per qualsiasi problema o domanda, contatta il supporto tecnico.</p>

      <p>
        Cordiali saluti,<br />
        <strong>Team Piattaforma Conformita NIS2</strong>
      </p>

      <hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;" />

      <p style="font-size: 12px; color: #999;">
        Questa e una email automatica, si prega di non rispondere. Se hai
        ricevuto questa email per errore, contattaci immediatamente.
      </p>
    </div>
  </body>
</html>
```

### Sicurezza

1. **Generazione Password Temporanea**:

   - Lunghezza: 12 caratteri
   - Caratteri: maiuscole, minuscole, numeri, simboli (`!@#$%^&*`)
   - Algoritmo: cryptographically secure random (es: `crypto.randomBytes`)
   - Hash: bcrypt con salt (prima di salvare in DB)
   - Validita: 7 giorni (dopo scade, richiede reset)

2. **MFA (Multi-Factor Authentication)**:

   - Obbligatorio per Admin Piattaforma
   - Metodi supportati: TOTP (Google Authenticator, Authy)
   - Configurazione: al primo accesso (guidata)
   - Backup codes: 10 codici usa-e-getta

3. **Rate Limiting**:

   - Login: max 5 tentativi falliti in 15 minuti → blocco temporaneo 30 min
   - API create utente: max 10 creazioni/minuto per Admin
   - Filtri/ricerca: max 60 richieste/minuto

4. **Audit Trail**:
   - Loggare TUTTE le operazioni su utenti:
     - Creazione: `USER_CREATED` + dati utente + created_by
     - Modifica: `USER_UPDATED` + campi modificati + modified_by
     - Eliminazione: `USER_DELETED` + dati utente + deleted_by
     - Login: `USER_LOGIN` + IP + timestamp
     - Logout: `USER_LOGOUT` + durata sessione
   - Storico immutabile (no delete, no update)
   - Retention: 5 anni (compliance GDPR)

---

## Flussi di Navigazione

### Flusso 1: Creazione Consulente da Lista Utenti

1. Admin → Lista Utenti (US-ANA-001)
2. Click "Crea Nuovo Utente"
3. Modal Selezione Tipo (US-ANA-002)
4. Seleziona "Consulente" → Click "Avanti"
5. Redirect → Lista Aziende Consulenza (US-001.1)
6. Admin cerca/seleziona azienda consulenza
7. Click su azienda → Dettaglio (US-001.3)
8. Click widget "Elenco consulenti collegati"
9. Sezione Consulenti (US-001.5)
10. Click "Nuovo consulente"
11. Compila form → Salva
12. Consulente creato → Email invito inviata
13. Torna a Lista Utenti → nuovo Consulente visibile

### Flusso 2: Creazione Admin Piattaforma da Lista Utenti

1. Admin → Lista Utenti (US-ANA-001)
2. Click "Crea Nuovo Utente"
3. Modal Selezione Tipo (US-ANA-002)
4. Seleziona "Admin Piattaforma" → Click "Avanti"
5. Form inline in modal (US-ANA-003)
6. Compila 4 campi → Click "Salva"
7. Validazione OK → Admin creato
8. Email invito inviata
9. Modal chiusa → Lista Utenti refresh
10. Nuovo Admin visibile in lista con badge rosso "Admin"

### Flusso 3: Modifica Consulente da Lista Utenti

1. Admin → Lista Utenti (US-ANA-001)
2. Click icona matita su riga con badge "Consulente"
3. Sistema identifica azienda consulenza di appartenenza
4. Redirect → Dettaglio Azienda Consulenza → Sezione Consulenti (US-001.5)
5. Consulente pre-selezionato + modal modifica aperta
6. Admin modifica dati → Salva
7. Redirect/navigazione back → Lista Utenti
8. Riga consulente aggiornata

### Flusso 4: Eliminazione Admin con Vincoli

1. Admin → Lista Utenti (US-ANA-001)
2. Click icona cestino su riga con badge "Admin"
3. Sistema verifica vincoli (US-ANA-027):
   - Vincolo 1: Non e se stesso? ✓
   - Vincolo 2: Non e ultimo Admin? ✓
4. Vincoli OK → Dialog conferma
5. Admin legge impatti → Click "Conferma eliminazione"
6. Sistema:
   - Soft delete (deleted_at = now)
   - Invalida sessioni attive
   - Preserva audit trail
7. Dialog chiuso → Lista Utenti refresh
8. Admin eliminato NON appare piu in lista
9. Toast success: "Admin eliminato con successo"

### Flusso 5: Ricerca e Filtro Utenti

1. Admin → Lista Utenti (US-ANA-001)
2. Sezione Filtri visibile (US-ANA-009)
3. Admin deseleziona checkbox "Cliente" (vuole vedere solo Consulenti e Admin)
4. Admin digita "mario" in Ricerca Globale
5. Debounce 300ms → filtri applicati automaticamente
6. Lista aggiornata:
   - Solo Consulenti e Admin
   - Con "mario" in nome/cognome/email/telefono
7. Badge "Filtri attivi: 2"
8. Admin trova utente desiderato
9. Click "Azzera filtri" → lista completa ripristinata

---

**Fine User Stories - Gestione Utenti Admin**
