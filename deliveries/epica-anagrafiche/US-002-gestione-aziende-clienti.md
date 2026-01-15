# User Stories - Gestione Aziende Clienti

**Epica**: Anagrafiche
**Macro-argomento**: Gestione Aziende Clienti
**Data**: 2025-12-11
**Versione**: 2.0

---

**Descrizione Epic**: Permettere ai Consulenti e Admin di piattaforma di piattaforma di creare, gestire e monitorare le aziende clienti con relative sedi e utenti aziendali, garantendo segregazione multi-tenant e supporto per scenari multi-consulente.

---

## US-ANA-010: Visualizzare Lista Aziende Clienti

**Come** Admin di piattaforma, Admin Consulente, Consulente
**Voglio** visualizzare la lista delle aziende clienti a me assegnate
**In modo che** possa accedere rapidamente ai loro dettagli e gestire gli audit

### Criteri di Accettazione

**Scenario 1: Consulente visualizza lista delle proprie aziende**

1. Il Consulente accede alla sezione "Aziende Clienti"
2. Il sistema mostra una tabella con le aziende assegnate al consulente loggato
3. La tabella include le seguenti colonne:
   - **Ragione Sociale** (cliccabile → link a dettaglio)
   - **Partita IVA**
   - **Codice Fiscale**
   - **N° Sedi** (count delle sedi associate)
   - **N° Utenti** (count degli utenti aziendali attivi)
   - **Data Creazione** (formato DD/MM/YYYY)
   - **Azioni** (icone: Visualizza, Modifica, Elimina)
4. **Ordinamento default**:
   - Ordinamento applicato: colonna "Data Creazione" decrescente (più recenti prima)
5. **Paginazione**:
   - Rows per page: 10 (default), con opzioni 10/25/50
   - Indicatore "X-Y di Z" (es. "1-4 di 4")
   - Frecce navigazione prev/next

**Scenario 2: Admin-Consulente visualizza lista delle aziende della propria azienda di consulenza**

1. L'Admin-Consulente accede alla sezione "Aziende Clienti"
2. Il sistema mostra tutte le aziende clienti associate alla sua azienda di consulenza (indipendentemente dal consulente assegnato)
3. La tabella include una colonna aggiuntiva:
   - **Consulente Assegnato** (nome consulente)
4. Resto del comportamento identico allo Scenario 1

**Scenario 3: Admin di piattaforma di piattaforma visualizza tutte le aziende**

1. L'Admin di piattaforma accede alla sezione "Aziende Clienti"
2. Il sistema mostra **tutte** le aziende clienti presenti in piattaforma
3. La tabella include colonne aggiuntive:
   - **Consulente Assegnato** (nome consulente)
   - **Azienda di Consulenza** (nome azienda di consulenza del consulente)
4. Resto del comportamento identico allo Scenario 1

**Scenario 4: Lista vuota**

1. Se non ci sono aziende clienti visibili per il ruolo loggato
2. Il sistema mostra un messaggio: "Nessuna azienda cliente presente. Crea la prima azienda cliente per iniziare."
3. Il sistema mostra un pulsante "Crea Azienda Cliente" prominente

**Scenario 5: Paginazione**

### Field Specifications

**Tabella Aziende Clienti**:

| Campo                 | Tipo   | Required      | Validazione | Note                                                                     |
| --------------------- | ------ | ------------- | ----------- | ------------------------------------------------------------------------ |
| Ragione Sociale       | Text   | N/A (display) |             | Testo                                                                    |
| Partita IVA           | Text   | N/A (display) |             | Formato 11 cifre                                                         |
| Codice Fiscale        | Text   | N/A (display) |             | Formato 16 caratteri alfanumerici                                        |
| N° Sedi               | Number | N/A (display) |             | Count delle sedi attive                                                  |
| N° Utenti             | Number | N/A (display) |             | Count utenti attivi                                                      |
| Data Creazione        | Date   | N/A (display) |             | Formato DD/MM/YYYY                                                       |
| Consulente Assegnato  | Text   | N/A (display) |             | Visibile solo per Admin di piattaforma-Consulente e Admin di piattaforma |
| Azienda di Consulenza | Text   | N/A (display) |             | Visibile solo per Admin di piattaforma di piattaforma                    |
| Azioni                | Icons  | N/A (display) |             | Eye (view), Pencil (edit), Trash (delete)                                |

### Edge Cases

**EC1: Utente non autorizzato**

- Se un utente con ruolo "Azienda" o "Fornitore" tenta di accedere alla sezione
- Sistema: Redirect a homepage con messaggio "Accesso negato. Funzionalità disponibile solo per Consulenti e Admin."

**EC2: Azienda eliminata da altro utente**

- Se un Consulente visualizza la lista e nel frattempo un Admin di piattaforma elimina un'azienda
- Sistema: Al click su azienda eliminata → messaggio "Azienda non trovata o non più accessibile"

---

## US-ANA-011: Creare Nuova Azienda Cliente

**Come** Admin di piattaforma, Admin Consulente
**Voglio** creare una nuova azienda cliente con almeno una sede e un utente referente
**In modo che** possa avviare la gestione degli audit per quel cliente

### Criteri di Accettazione

**Scenario 1: Admin di piattaforma/Admin Consulente crea nuova azienda cliente**

1. Admin di piattaforma/Admin Consulente clicca su "Crea Azienda Cliente"
2. Il sistema mostra un form multi-step con 3 tab:
   - **Tab 1: Dati Azienda** (attivo di default)
   - **Tab 2: Sedi Aziendali** (disabilitato fino a completamento Tab 1)
   - **Tab 3: Utenti Aziendali** (disabilitato fino a completamento Tab 2)
3. Il sistema mostra un indicatore di progresso: "Step 1 di 3"

**Scenario 2: Compilazione Tab 1 - Dati Azienda**

1. Il Admin di piattaforma/Admin Consulente compila i seguenti campi:

   **Sezione "Informazioni Generali"**:

   - **Ragione Sociale** (text, required)
   - **Indirizzo** (text, required)
   - **Partita IVA** (text, required, 11 cifre numeriche)
   - **Codice Fiscale** (text, required, 16 caratteri alfanumerici uppercase)
   - **Telefono** (text, required, formato internazionale es: +39 02 1234567)
   - **PEC** (email, required, validazione formato email)
   - **Note** (textarea, optional)

   **Sezione "Consulente Assegnato"**:

   - **Consulente** (field comportamento dipendente da ruolo loggato):
     - Se loggato = **Admin-Consulente** → dropdown con lista consulenti della propria azienda di consulenza (not required)
     - Se loggato = **Admin di piattaforma** → dropdown con lista **tutti i consulenti** di tutte le aziende di consulenza (not required)

**Nota informativa**:
"Il consulente assegnato avrà accesso alla gestione degli audit e dei fornitori dell'azienda cliente."

2. Admin di piattaforma/Admin Consulente clicca "Avanti" (o "Salva e Procedi")
3. Il sistema valida i campi obbligatori:
   - Se mancano campi required → mostra errori inline sotto i campi
   - Se Partita IVA non è 11 cifre numeriche → errore "Partita IVA deve essere composta da 11 cifre numeriche"
   - Se Codice Fiscale non è 16 caratteri alfanumerici → errore "Codice Fiscale deve essere composto da 16 caratteri alfanumerici"
4. Se validazione OK → sistema abilita **Tab 2: Sedi Aziendali** e naviga automaticamente

**Scenario 3: Compilazione Tab 2 - Sedi Aziendali (OBBLIGATORIO almeno 1 sede)**

1. Il sistema mostra la sezione "Sedi Aziendali" con:

   - Messaggio informativo: "Devi inserire almeno una sede aziendale per procedere"
   - Pulsante "Aggiungi Sede" prominente
   - Tabella vuota con colonne: Tipo Sede, Indirizzo, Città, CAP, Provincia, Nazione, Azioni

2. Admin di piattaforma/Admin Consulente clicca "Aggiungi Sede"
3. Il sistema mostra un **modal** "Aggiungi Sede" con i seguenti campi:

   - **Tipo Sede** (dropdown, required) → valori: "Sede Legale", "Sede Operativa", "Filiale", "Magazzino", "Centro Dati"
   - **Indirizzo** (text, required)
   - **Civico** (text, required)
   - **CAP** (text, required, 5 cifre numeriche per IT)
   - **Città** (text, required)
   - **Provincia** (text, required, 2 caratteri uppercase per IT)
   - **Nazione** ((text, required)

4. Admin di piattaforma/Admin Consulente compila i campi e clicca "Salva Sede"
5. Il sistema valida:
   - Campi required compilati
   - CAP = 5 cifre se Nazione = Italia
   - Provincia = 2 caratteri se Nazione = Italia
6. Se validazione OK → sistema:
   - Chiude modal
   - Aggiunge riga alla tabella sedi
   - Mostra messaggio success "Sede aggiunta correttamente"
   - Scroll automatico alla tabella sedi
7. Admin di piattaforma/Admin Consulente può aggiungere altre sedi (ripetendo step 2-6) o procedere
8. Admin di piattaforma/Admin Consulente clicca "Avanti"
9. Il sistema valida:
   - Se **nessuna sede inserita** → errore "Devi inserire almeno una sede aziendale per procedere"
   - Se **almeno 1 sede presente** → abilita **Tab 3: Utenti Aziendali** e naviga automaticamente

**Scenario 4: Compilazione Tab 3 - Utenti Aziendali (OBBLIGATORIO almeno 1 utente)**

1. Il sistema mostra la sezione "Utenti Aziendali" con:

   - Messaggio informativo: "Devi inserire almeno un utente referente per l'azienda cliente"
   - Pulsante "Aggiungi Utente" prominente
   - Tabella vuota con colonne: Nome, Cognome, Email, Ruolo, Permessi, Azioni

2. Admin di piattaforma/Admin Consulente clicca "Aggiungi Utente"
3. Il sistema mostra un **modal** "Aggiungi Utente Aziendale" con i seguenti campi:

   **Sezione "Dati Personali"**:

   - **Nome** (text, required)
   - **Cognome** (text, required)
   - **Email** (email, required, validazione formato email)
   - **Telefono** (text, optional)

   **Sezione "Ruolo e Permessi"**:

   - **Ruolo** (radio buttons, required):

     - ⚪ Admin-Cliente (può gestire utenti aziendali)
     - ⚪ Cliente semplice (accesso viewer)

   - **Permessi Aggiuntivi** (checkboxes, default = unchecked):
     - ☐ Può creare fornitori
     - ☐ Può compilare Audit

   **Nota**: Le checkbox sono **modificabili solo in creazione**. Dopo il salvataggio diventeranno read-only. Se è il primo utente della lista, è per forza un admin-cliente.

4. Admin di piattaforma/Admin Consulente compila i campi e clicca "Salva Utente"
5. Il sistema valida:
   - Campi required compilati
   - Email formato valido
   - Email **non già usata nella stessa azienda cliente** → se duplicata errore "Email già utilizzata per un altro utente di questa azienda"
6. Se validazione OK → sistema:
   - Chiude modal
   - Aggiunge riga alla tabella utenti
   - Mostra messaggio success "Utente aggiunto correttamente. Riceverà un'email di invito."
7. Admin di piattaforma/Admin Consulente può aggiungere altri utenti (ripetendo step 2-6) o procedere
8. Admin di piattaforma/Admin Consulente clicca "Salva Azienda"
9. Il sistema valida:
   - Se **nessun utente inserito** → errore "Devi inserire almeno un utente per procedere"
   - Se **almeno 1 utente presente** → procede con salvataggio finale

**Scenario 5: Salvataggio Finale**

1. Il sistema salva tutti i dati in transazione:

   - Crea record Azienda Cliente
   - Associa Consulente assegnato
   - Crea record Sedi
   - Crea record Utenti Aziendali
   - Per ogni utente:
     - Se email **NON esiste** → crea account utente con stato "Invito Pending"
     - Se email **già esiste** → aggiorna account esistente aggiungendo link ad Azienda Cliente
     - Invia email invito/notifica

2. Se salvataggio OK → sistema:

   - Mostra messaggio success "Azienda cliente creata con successo. Email di invito inviata agli utenti."
   - Redirect a **Dettaglio Azienda Cliente** appena creata

3. Se errore durante salvataggio → sistema:
   - Rollback transazione completa
   - Mostra messaggio errore "Errore durante il salvataggio. Riprova."
   - Mantiene form compilato per retry

### Field Specifications

**Tab 1: Dati Azienda**

| Campo           | Label                | Tipo            | Required | Validazione                                     | Placeholder      |
| --------------- | -------------------- | --------------- | -------- | ----------------------------------------------- | ---------------- |
| ragione_sociale | Ragione Sociale      | Text            | Sì       | Max 255 caratteri                               | Es: Acme S.p.A.  |
| partita_iva     | Partita IVA          | Text            | Sì       | Esattamente 11 cifre numeriche                  | 12345678901      |
| codice_fiscale  | Codice Fiscale       | Text            | Sì       | Esattamente 16 caratteri alfanumerici uppercase | RSSMRA80A01H501Z |
| telefono        | Telefono             | Text            | Sì       | Formato internazionale                          | +39 02 1234567   |
| PEC             | Email Generale       | Email           | Sì       | Formato email valido                            | info@example.com |
| consulente_id   | Consulente Assegnato | Dropdown/Hidden | No       | FK a tabella Utenti (ruolo Consulente)          | -                |

**Tab 2: Sedi Aziendali (Modal)**

| Campo     | Label     | Tipo     | Required | Validazione                                               | Placeholder      |
| --------- | --------- | -------- | -------- | --------------------------------------------------------- | ---------------- |
| tipo_sede | Tipo Sede | Dropdown | Sì       | Enum: Sede Legale/Operativa/Filiale/Magazzino/Centro Dati | Seleziona tipo   |
| indirizzo | Indirizzo | Text     | Sì       | Max 255 caratteri                                         | Via Roma         |
| civico    | Civico    | Text     | Sì       | Max 10 caratteri                                          | 123/A            |
| cap       | CAP       | Text     | Sì       | 5 cifre se Nazione=Italia                                 | 20121            |
| citta     | Città     | Text     | Sì       | Max 100 caratteri                                         | Milano           |
| provincia | Provincia | Text     | Sì       | 2 caratteri uppercase se Nazione=Italia                   | MI               |
| nazione   | Nazione   | Text     | Sì       | Lista paesi ISO                                           | Italia (default) |

**Tab 3: Utenti Aziendali (Modal)**

| Campo                     | Label                | Tipo     | Required | Validazione                                            | Placeholder             |
| ------------------------- | -------------------- | -------- | -------- | ------------------------------------------------------ | ----------------------- |
| nome                      | Nome                 | Text     | Sì       | Max 100 caratteri                                      | Mario                   |
| cognome                   | Cognome              | Text     | Sì       | Max 100 caratteri                                      | Rossi                   |
| email                     | Email                | Email    | Sì       | Formato email + unique per azienda                     | mario.rossi@example.com |
| telefono                  | Telefono             | Text     | No       | Formato internazionale                                 | +39 333 1234567         |
| ruolo                     | Ruolo                | Radio    | Sì       | Enum: Admin-Cliente / Cliente semplice                 | -                       |
| flag_puo_creare_fornitori | Può creare fornitori | Checkbox | No       | Boolean, default false, modificabile solo in creazione | -                       |
| flag_puo_compilare_audit  | Può compilare Audit  | Checkbox | No       | Boolean, default false, modificabile solo in creazione | -                       |

### Edge Cases

**EC1: Navigazione tab senza completamento**

- Se Admin di piattaforma/Admin Consulente tenta di cliccare su Tab 2 senza aver compilato Tab 1
- Sistema: Tab 2 è disabilitato, tooltip "Completa i dati azienda per procedere"

**EC2: Email duplicata in creazione (multi-consulente)**

- Vedi US-ANA-011 per flusso completo

**EC3: Validazione Partita IVA/Codice Fiscale formale**

- Se Partita IVA contiene caratteri non numerici → errore inline
- Se Codice Fiscale non rispetta lunghezza/formato → errore inline
- Se Codice Fiscale contiene caratteri minuscoli → sistema converte automaticamente in uppercase

**EC4: Modifica flag permessi dopo salvataggio**

- I flag "Può creare fornitori" e "Può compilare Audit" sono modificabili **solo in fase di creazione**
- Dopo il salvataggio diventano **read-only**

---

## US-ANA-012: Gestire Scenario Multi-Consulente (Azienda Duplicata)

**Come** Sistema
**Voglio** gestire correttamente la creazione di un'azienda cliente già esistente da parte di un diverso consulente
**In modo che** l'utente referente possa accedere a entrambi i contesti senza duplicare account

### Criteri di Accettazione

**Scenario 1: Rilevamento Partita IVA duplicata al salvataggio**

1. **Consulente B** (diverso da Consulente A che ha già creato "Azienda X") compila form creazione azienda
2. **Consulente B** inserisce Partita IVA **già esistente** per un'altra azienda cliente assegnata a **Consulente A**
3. Il sistema, al click su "Avanti" dopo Tab 1, valida
4. Se Consulente B clicca "Annulla" → torna indietro
5. Se Consulente B clicca "Procedi" → sistema:
   - Consente di procedere con Tab 2 e Tab 3 normalmente
   - Al salvataggio finale (vedi Scenario 2)

**Scenario 2: Salvataggio con email referente già esistente**

1. **Consulente B** completa tutti i 3 tab e clicca "Salva Azienda"
2. **Consulente B** ha inserito utente referente con email "mario@example.com"
3. Il sistema valida:
   - Email "mario@example.com" **già esiste** nel sistema (associata ad Azienda Cliente #1 di Consulente A)
4. Il sistema esegue le seguenti operazioni **atomicamente** (transazione):

   a. **Crea record Azienda Cliente #2**:

   - Nuova azienda cliente associata a Consulente B
   - Dati aziendali indipendenti (Ragione Sociale, Partita IVA, ecc.)

   b. **NON crea nuovo account utente** per "mario@example.com":

   - Account "mario@example.com" già esiste

   c. **Aggiorna account esistente "mario@example.com"**:

   - Aggiunge associazione ad Azienda Cliente #2
   - Mantiene email, password, ruolo, flag permessi esistenti
   - Nota: I flag permessi sono **indipendenti per ogni azienda cliente** (se Admin-Cliente in #1, può essere Cliente semplice in #2)

   d. **Crea record Utente Aziendale #2**:

   - Link tra Account "mario@example.com" e Azienda Cliente #2
   - Ruolo e flag permessi come specificato da Consulente B (possono differire da quelli in Azienda Cliente #1)

   e. **Invia email notifica a "mario@example.com"**:

   - Oggetto: "Nuovo contesto aziendale disponibile - [Nome Azienda Cliente #2]"
   - Corpo:

     ```
     Ciao Mario,

     Hai ora accesso a un nuovo contesto aziendale sulla piattaforma:

     - **Azienda**: [Ragione Sociale Azienda Cliente #2]
     - **Consulente**: [Nome Consulente B]

     Puoi accedere alla piattaforma con le tue credenziali esistenti e utilizzare il selettore di contesto in sidebar per passare tra le aziende.

     Accedi ora: [Link piattaforma]
     ```

5. Se transazione OK → sistema:
   - Mostra messaggio success "Azienda cliente creata con successo. Email di notifica inviata agli utenti."
   - Redirect a Dettaglio Azienda Cliente #2

**Scenario 3: Utente Mario accede dopo setup multi-consulente**

1. Mario apre email di notifica e clicca su link piattaforma
2. Mario fa login con "mario@example.com" + password (già impostata in precedenza)
3. Il sistema rileva che Mario ha accesso a **2 aziende clienti**
4. Il sistema mostra **context switcher** in sidebar con:
   - 🏢 Azienda X (Consulenza Alpha) → Azienda Cliente #1
   - 🏢 Azienda X (Consulenza Beta) → Azienda Cliente #2
5. Di default, il contesto selezionato è l'**ultimo utilizzato** (o il primo se primo accesso)
6. Mario può cliccare per switchare tra i due contesti
7. Ogni contesto mostra dati **completamente segregati**:
   - Audit diversi
   - Fornitori diversi
   - Utenti aziendali diversi (gestiti da consulenti diversi)
   - Report diversi

**Scenario 4: Privacy - Nessun warning al front-end durante creazione**

1. Durante la compilazione del form (Tab 3 - Utenti Aziendali)
2. **Consulente B** inserisce email "mario@example.com" nel campo Email utente
3. Il sistema **NON mostra warning o alert** che l'email esiste già
4. Il sistema **NON impedisce il salvataggio**
5. La gestione del rilevamento duplicato avviene **solo a backend** al momento del salvataggio finale
6. Motivazione: **Privacy** - non esporre informazioni su altri contesti aziendali

### Edge Cases

**EC1: Tripla associazione (3+ consulenti)**

- Se un utente viene associato a 3+ aziende clienti da consulenti diversi
- Sistema: Context switcher mostra tutte le aziende (scroll se necessario)

**EC2: Consulente B inserisce utente con email già sua**

- Se Consulente B tenta di creare utente aziendale con propria email di consulente
- Sistema: Errore "Non puoi utilizzare la tua email personale come utente aziendale"

**EC3: Ruolo diverso in contesti diversi**

- Mario può essere **Admin-Cliente** in Azienda Cliente #1 e **Cliente semplice** in Azienda Cliente #2
- Permessi e ruolo sono **indipendenti per ogni azienda cliente**

**EC4: Consulente A elimina Azienda Cliente #1**

- Se Consulente A elimina Azienda Cliente #1
- Sistema: Account Mario rimane attivo ma perde accesso ad Azienda Cliente #1
- Context switcher di Mario mostra solo Azienda Cliente #2
- Se rimane un solo contesto, context switcher rimane visibile

**EC5: Consulente B tenta di modificare dati utente Mario**

- Consulente B può modificare **solo il ruolo e permessi di Mario relativi ad Azienda Cliente #2**
- Consulente B **non può vedere né modificare** dati personali (email, nome, cognome, telefono) se l'account è condiviso
- Dati personali sono **read-only** se account già esistente

---

## US-ANA-013: Utilizzare Context Switcher (Utente Multi-Azienda)

**Come** Utente Aziendale con accesso a più aziende clienti
**Voglio** switchare facilmente tra i diversi contesti aziendali
**In modo che** possa gestire le attività per ciascuna azienda senza dover effettuare logout/login

### Criteri di Accettazione

**Scenario 1: Visualizzazione context switcher in sidebar**

1. L'utente Mario (con ruolo "Azienda") fa login con credenziali "mario@example.com"
2. Il sistema rileva che Mario ha accesso a **2 aziende clienti**:
   - Azienda Cliente #1: "Azienda X" (Consulenza Alpha)
   - Azienda Cliente #2: "Azienda X" (Consulenza Beta)
3. Il sistema mostra in **sidebar** (parte alta, sotto il nome utente) un **context switcher** con:
   - Icona 🏢
   - Label "Contesto Aziendale"
   - Dropdown con lista aziende:
     - **Azienda X (Consulenza Alpha)** ← selezionato (badge "Attivo")
     - Azienda X (Consulenza Beta)
4. Il contesto selezionato è evidenziato con background colorato e checkmark ✓

**Scenario 2: Switch tra contesti**

1. Mario clicca sul dropdown context switcher
2. Il sistema mostra menu a tendina con lista aziende
3. Mario seleziona "Azienda X (Consulenza Beta)"
4. Il sistema:
   - Mostra spinner "Caricamento contesto..."
   - Effettua chiamata API per switchare contesto
   - Ricarica la pagina corrente con dati del nuovo contesto
   - Aggiorna sidebar con nuovo contesto selezionato
   - Mostra toast success "Contesto cambiato: Azienda X (Consulenza Beta)"
5. Da questo momento, **tutti i dati visualizzati** (audit, fornitori, utenti, report) sono relativi ad Azienda Cliente #2

**Scenario 3: Context switcher con un solo contesto**

1. L'utente Luca (con ruolo "Azienda") fa login
2. Il sistema rileva che Luca ha accesso a **1 sola azienda cliente**: "Azienda Y (Consulenza Gamma)"
3. Il sistema mostra comunque il **context switcher** in sidebar con:
   - Icona 🏢
   - Label "Contesto Aziendale"
   - Dropdown con **un solo item**: "Azienda Y (Consulenza Gamma)" (selezionato, badge "Attivo")
4. Il dropdown è comunque cliccabile ma mostra solo l'unico contesto disponibile

**Scenario 4: Persistenza contesto tra sessioni**

1. Mario seleziona contesto "Azienda X (Consulenza Beta)"
2. Mario esegue logout
3. Mario fa nuovamente login il giorno dopo
4. Il sistema:
   - Recupera l'**ultimo contesto utilizzato** da database
   - Seleziona automaticamente "Azienda X (Consulenza Beta)" al login
   - Mario riprende da dove aveva lasciato

**Scenario 5: Context switcher non visibile per Consulenti/Admin**

1. Un Consulente o Admin di piattaforma fa login
2. Il sistema **non mostra** context switcher in sidebar
3. Consulenti e Admin di piattaforma vedono tutte le aziende a loro assegnate nella lista "Aziende Clienti" senza bisogno di switch

**Formato Nome Contesto**:

```
[Ragione Sociale Azienda Cliente] ([Nome Azienda di Consulenza del Consulente Assegnato])

Esempio:
- "Acme S.p.A. (Consulenza Alpha)"
- "Beta Industries (Consulenza Compliance Pro)"
```

### Edge Cases

**EC1: Switch durante modifica form non salvato**

- Se Mario sta compilando un form (es: creazione fornitore) e clicca su context switcher, le modifiche vanno perse

**EC2: Contesto eliminato da consulente mentre utente è loggato**

- Se Mario è nel contesto "Azienda X (Consulenza Beta)" e nel frattempo Consulente B elimina Azienda Cliente #2
- Sistema: Al prossimo reload/navigazione → mostra errore "Contesto non più disponibile. Sei stato spostato nell'ultimo contesto valido."
- Switcha automaticamente al primo contesto disponibile

**EC3: Permessi diversi tra contesti**

- Se Mario è **Admin-Cliente** in Azienda X (Consulenza Alpha) e **Cliente semplice** in Azienda X (Consulenza Beta)
- Sistema: Mostra menu/funzionalità diversi in base al ruolo del contesto attivo
- Es: Nel contesto Alpha vede "Gestione Utenti", nel contesto Beta NON la vede

**EC4: URL con parametro contesto**

- Se Mario condivide un link con contesto specifico (es: /audit/123?context=azienda_cliente_2)
- Sistema: Switcha automaticamente al contesto corretto prima di caricare la risorsa
- Se Mario non ha accesso a quel contesto → errore 403 "Non hai accesso a questa risorsa"

---

## US-ANA-014: Visualizzare Dettaglio Azienda Cliente

**Come** Admin di piattaforma/Admin Consulente/Consulente
**Voglio** visualizzare tutti i dettagli di un'azienda cliente
**In modo che** possa consultare informazioni, sedi, utenti e stato conformità

### Criteri di Accettazione

**Scenario 1: Accesso al dettaglio azienda**

1. Il Consulente clicca su una riga nella lista "Aziende Clienti" (o su icona "Visualizza")
2. **Widget di navigazione rapida** (5 card orizzontali):

| Widget   | Icona         | Label                   | Azione Click                        |
| -------- | ------------- | ----------------------- | ----------------------------------- |
| Widget 1 | Icona aziende | Elenco sedi azienda     | Apre sezione sedi                   |
| Widget 2 | Icona utenti  | Elenco fornitori        | Apre sezione fornitori              |
| Widget 3 | Icona utenti  | Elenco utenti aziendali | Apre sezione utenti azienda cliente |
| Widget 4 | Icona audit   | Elenco Audit            | Apre sezione audit                  |
| Widget 5 | Icona azioni  | Elenco Azioni           | Apre sezione azioni                 |

3. **Sezione "Informazioni Anagrafiche"** (read-only):

**Layout**: Form a due colonne

| Campo          | Label          | Formato Display |
| -------------- | -------------- | --------------- |
| nome_azienda   | Nome azienda   | Text            |
| indirizzo      | Indirizzo      | Text            |
| p_iva          | Partita Iva    | Text            |
| codice_fiscale | Codice fiscale | Text            |
| PEC            | Email          | Text            |
| telefono       | Telefono       | Text            |
| note           | Note           | Textarea        |

**Scenario 2: Sezione Sedi Aziendali**

1. Il sistema mostra la pagina "Sedi Aziendali" con tabella:

   | Tipo Sede      | Indirizzo Completo | Città  | Provincia | CAP   | Nazione | Azioni   |
   | -------------- | ------------------ | ------ | --------- | ----- | ------- | -------- |
   | Sede Legale    | Via Roma 123/A     | Milano | MI        | 20121 | Italia  | 👁️ ✏️ 🗑️ |
   | Sede Operativa | Corso Italia 45    | Torino | TO        | 10121 | Italia  | 👁️ ✏️ 🗑️ |

2. Pulsante "Aggiungi Sede" in alto a destra della card
3. Icone azioni:
   - 👁️ Visualizza (apre dettaglio)
   - ✏️ Modifica (apre modifica)
   - 🗑️ Elimina (con confirm)

**Scenario 3: Sezione Fornitori**

1. Il sistema mostra la pagina "Fornitori" con tabella:

   | Nome  | Cognome | Email             | Creato Il        | Azioni   |
   | ----- | ------- | ----------------- | ---------------- | -------- |
   | Mario | Rossi   | mario@example.com | 08/12/2025 15:30 | 👁️ ✏️ 🗑️ |
   | Laura | Bianchi | laura@example.com | 08/12/2025 15:30 | 👁️ ✏️ 🗑️ |

2. Pulsante "Aggiungi Fornitore" in alto a destra della card
3. Colonna "Permessi": Mostra badge per ogni flag attivo (es: "Crea Fornitori" se true)

4. Icone azioni:

- 👁️ Visualizza (apre dettaglio)

  - ✏️ Modifica (apre modal modifica - solo ruolo, flag in read-only)
  - 🗑️ Elimina (con confirm)

**Scenario 4: Sezione Utenti Aziendali**

5. Il sistema mostra la pagina "Utenti Aziendali" con tabella:

   | Nome  | Cognome | Email             | Ruolo            | Permessi                      | Stato Invito      | Ultimo Accesso   | Azioni   |
   | ----- | ------- | ----------------- | ---------------- | ----------------------------- | ----------------- | ---------------- | -------- |
   | Mario | Rossi   | mario@example.com | Admin-Cliente    | Crea Fornitori, Compila Audit | ✅ Attivo         | 08/12/2025 15:30 | ✏️ 🗑️    |
   | Laura | Bianchi | laura@example.com | Cliente semplice | -                             | ⏳ Invito Pending | -                | ✏️ 🗑️ 📧 |

6. Pulsante "Aggiungi Utente" in alto a destra della card
7. Colonna "Permessi": Mostra badge per ogni flag attivo (es: "Crea Fornitori" se true)
8. Colonna "Stato Invito":
   - ✅ Attivo (verde): utente ha impostato password e fatto almeno un accesso
   - ⏳ Invito Pending (giallo): email inviata ma utente non ha ancora impostato password
   - ❌ Disabilitato (rosso): utente disabilitato manualmente
9. Icone azioni:
   - ✏️ Modifica (apre modal modifica - solo ruolo, flag in read-only)
   - 🗑️ Elimina (con confirm)
   - 📧 Re-invia Invito (visibile solo se stato = "Invito Pending")

**Scenario 5: Sezione Riepilogo Audit**

1. Il sistema mostra la pagina "Audit" con tabella degli audit:

   | Codice Audit | Framework       | Data Creazione | Stato      | Azioni |
   | ------------ | --------------- | -------------- | ---------- | ------ |
   | AUD-2025-001 | NIS2            | 01/12/2025     | Completato | 👁️     |
   | AUD-2025-002 | CIS Controls v8 | 15/11/2025     | In Corso   | 👁️     |

2. Se nessun audit presente → messaggio "Nessun audit creato. Crea il primo audit per iniziare la valutazione."

### Edge Cases

**EC1: Azienda senza sedi (impossibile per validazione)**

- Scenario non possibile: validazione in creazione richiede almeno 1 sede

**EC2: Azienda senza utenti (impossibile per validazione)**

- Scenario non possibile: validazione in creazione richiede almeno 1 utente

**EC3: Stato conformità N/A**

- Se nessun audit è stato mai completato per l'azienda
- Sistema: Badge "N/A" grigio con tooltip "Nessun audit completato"

**EC4: Utente non autorizzato tenta accesso diretto**

- Se un Consulente B tenta di accedere via URL al dettaglio di un'azienda assegnata a Consulente A
- Sistema: Errore 403 "Non hai accesso a questa risorsa"

**EC5: Admin-Consulente visualizza azienda di altro consulente della stessa azienda di consulenza**

- Admin-Consulente può visualizzare e modificare tutte le aziende clienti della propria azienda di consulenza

**EC7: Utente con account condiviso (multi-consulente)**

- Se l'utente "mario@example.com" è associato a più aziende clienti
- Nella tabella utenti, il Consulente vede **solo l'associazione relativa alla propria azienda cliente**
- Non vede né ha accesso alle altre associazioni di Mario

---

## US-ANA-015: Modificare Dati Azienda Cliente

**Come** Admin di piattaforma/Admin Consulente/Consulente
**Voglio** modificare i dati anagrafici di un'azienda cliente
**In modo che** possa mantenere aggiornate le informazioni

### Criteri di Accettazione

**Scenario 1: Accesso alla modifica**

1. Il Consulente visualizza il dettaglio di un'azienda cliente
2. Il Consulente clicca sul pulsante "Modifica"
3. Il sistema mostra un form di modifica con i campi **pre-compilati**

**Scenario 2: Modifica campi**

1. Il Consulente modifica uno o più campi (es: cambia "Telefono")
2. I campi sono validati in tempo reale (blur validation):

   - Email Generale → formato email valido
   - Codice Fiscale → 16 caratteri alfanumerici uppercase

3. Il Consulente clicca "Salva Modifiche"
4. Il sistema valida tutti i campi obbligatori
5. Se validazione OK → sistema:
   - Salva le modifiche in database
   - Aggiorna campo "Ultima Modifica" con timestamp corrente
   - Mostra toast success "Dati azienda aggiornati con successo"
   - Redirect a dettaglio azienda con dati aggiornati

**Scenario 3: Partita IVA non modificabile**

1. Il campo "Partita IVA" è mostrato come **read-only** (grigio, disabled)
2. Tooltip: "La Partita IVA non può essere modificata dopo la creazione. In caso di errore, contatta l'amministratore."

### Field Specifications

### Edge Cases

**EC1: Modifica concorrente**

- Se Consulente A e Admin-Consulente B modificano la stessa azienda simultaneamente
- Sistema: Last write wins (ultima modifica sovrascrive)

**EC2: Validazione Codice Fiscale modificato**

- Se Consulente modifica Codice Fiscale inserendo formato non valido
- Sistema: Errore inline "Codice Fiscale deve essere composto da 16 caratteri alfanumerici"

**EC3: Consulente non autorizzato**

- Se Consulente B tenta di modificare azienda assegnata a Consulente A (accesso diretto via URL)
- Sistema: Errore 403 "Non hai i permessi per modificare questa azienda"

**EC4: Campo Email Generale duplicato**

- Non c'è vincolo di unicità su Email Generale (può essere condivisa tra aziende)
- Sistema: Permette salvataggio anche se email già usata da altra azienda

---

## US-ANA-016: Cambiare Consulente Assegnato

**Come** Admin-Consulente
**Voglio** cambiare il consulente assegnato a un'azienda cliente
**In modo che** possa redistribuire i carichi di lavoro tra i consulenti del mio team

### Criteri di Accettazione

**Scenario 1: Admin-Consulente accede alla modifica consulente**

1. L'Admin-Consulente visualizza il dettaglio di un'azienda cliente della propria azienda di consulenza
2. L'Admin-Consulente clicca sul pulsante "Modifica"
3. Il sistema mostra un form di modifica con i campi **pre-compilati** e:
   - Campo **Consulente Assegnato** (dropdown) pre-selezionato con consulente corrente
   - Lista consulenti della stessa azienda di consulenza
   - Warning banner: "⚠️ Attenzione: Puoi cambiare il consulente solo se non ci sono audit attivi per questa azienda."
   - Pulsanti: "Salva" | "Annulla"

**Scenario 2: Controllo audit attivi prima del cambio**

1. L'Admin-Consulente seleziona un nuovo consulente dal dropdown
2. L'Admin-Consulente clicca "Salva"
3. Il sistema valida:
   - Cerca se esistono audit con stato "In Corso" o "In Bozza" per l'azienda cliente
   - Se **esistono audit attivi**:
     - Mostra errore: "❌ Impossibile cambiare il consulente. Ci sono audit attivi per questa azienda. Completa o elimina gli audit prima di procedere."
     - Lista audit attivi: "[Codice Audit] - [Framework] - [Stato]"
     - Pulsante "Annulla" per chiudere
   - Se **non ci sono audit attivi**:
     - Procede con il cambio (vedi Scenario 3)

**Scenario 3: Cambio consulente eseguito**

1. Il sistema:

   - Aggiorna il campo `consulente_id` dell'azienda cliente
   - Mostra toast success "Consulente assegnato cambiato con successo"
   - Aggiorna dettaglio azienda con nuovo consulente

2. Il **nuovo consulente** ora vede l'azienda cliente nella propria lista
3. Il **vecchio consulente** non vede più l'azienda cliente nella propria lista (ma Admin-Consulente sì)

**Scenario 4: Admin di piattaforma di piattaforma cambia consulente tra aziende di consulenza diverse**

1. L'Admin di piattaforma visualizza dettaglio azienda cliente
2. L'Admin clicca "Modifica"
3. Il sistema mostra dropdown con **tutti i consulenti** di **tutte le aziende di consulenza**
4. Formato dropdown: "[Nome Consulente] ([Azienda di Consulenza])"
5. Resto del flusso identico a Scenario 2-3

**Scenario 5: Cambio consulente con account utenti condivisi**

1. Se l'azienda cliente ha utenti aziendali con account condivisi (multi-consulente)
2. Il cambio di consulente **NON impatta** gli utenti aziendali
3. Gli utenti aziendali continuano ad avere accesso con gli stessi ruoli e permessi
4. Il nuovo consulente **eredita** la gestione degli utenti aziendali esistenti
   |

### Edge Cases

**EC1: Audit completati non bloccano il cambio**

- Se ci sono audit con stato "Completato" o "Archiviato"
- Sistema: **Permette** il cambio di consulente (solo audit attivi lo bloccano)

**EC2: Consulente auto-assegnazione**

- Se Admin-Consulente cambia consulente assegnando sé stesso
- Sistema: Permette l'operazione (nessun vincolo)

---

## US-ANA-017: Gestire Utenti Aziendali

**Come** Admin di piattaforma/Admin Consulente/Consulente
**Voglio** aggiungere, modificare ed eliminare utenti aziendali per un'azienda cliente
**In modo che** possa gestire gli accessi e i permessi degli utenti finali

### Criteri di Accettazione

**Scenario 1: Aggiungere nuovo utente aziendale**

1. Il Consulente visualizza il dettaglio azienda cliente (sezione "Utenti Aziendali")
2. Il Consulente clicca "Aggiungi Utente"
3. Il sistema mostra pagina "Aggiungi Utente Aziendale" con form
4. Il Consulente compila:
   - Nome, Cognome, Email, Telefono
   - Ruolo (Admin-Cliente / Cliente semplice)
   - Flag permessi: "Può creare fornitori", "Può compilare Audit" (default false, **modificabili solo ora**)
5. Il Consulente clicca "Salva Utente"
6. Il sistema valida:
   - Email non duplicata **nella stessa azienda cliente**
   - Campi required compilati
7. Se validazione OK → sistema:

   - Crea utente aziendale
   - Se email **non esiste** globalmente → crea account + invia email invito
   - Se email **già esiste** globalmente → aggiorna account aggiungendo link ad azienda cliente + invia email notifica
   - Aggiorna tabella utenti con nuovo utente
   - Mostra toast "Utente aggiunto con successo. Email di invito inviata."

**Scenario 2: Modificare utente aziendale esistente**

1. Il Consulente clicca icona ✏️ "Modifica" su un utente nella tabella
2. Il sistema mostra pagina "Modifica Utente Aziendale" con form **parzialmente pre-compilato**:

   **Campi in READ-ONLY (grigio, disabled)**:

   - Nome
   - Cognome
   - Email
   - Telefono
   - Flag "Può creare fornitori"
   - Flag "Può compilare Audit"

   **Campi MODIFICABILI**:

   - Ruolo (dropdown: Admin-Cliente / Cliente semplice)

3. Il Consulente modifica il ruolo (es: da "Cliente semplice" a "Admin-Cliente")
4. Il Consulente clicca "Salva Modifiche"
5. Il sistema:

   - Aggiorna solo il campo `ruolo` dell'utente aziendale
   - Aggiorna tabella utenti
   - Mostra toast "Ruolo utente aggiornato con successo"

**Scenario 3: Eliminare utente aziendale**

1. Il Consulente clicca icona 🗑️ "Elimina" su un utente nella tabella
2. Il sistema mostra confirm dialog:
   - Titolo: "⚠️ Conferma Eliminazione"
   - Messaggio: "Sei sicuro di voler eliminare l'utente [Nome] [Cognome] ([Email])? L'utente non avrà più accesso a questa azienda cliente."
   - Pulsanti: "Elimina" (danger) | "Annulla"
3. Il Consulente clicca "Elimina"
4. Il sistema valida:
   - Controlla che **non sia l'ultimo utente aziendale** dell'azienda cliente
   - Se è l'ultimo → errore "❌ Impossibile eliminare l'ultimo utente aziendale. Ogni azienda deve avere almeno un utente."
5. Se validazione OK → sistema:
   - **Elimina il record Utente Aziendale** (link tra account e azienda cliente)
   - Se l'account utente è associato **solo a questa azienda** → **disabilita account** (soft delete)
   - Se l'account utente è associato **a più aziende (multi-consulente)** → **mantiene account attivo** (rimuove solo link ad azienda cliente)
   - Chiude dialog
   - Rimuove riga dalla tabella
   - Mostra toast "Utente eliminato con successo"

**Scenario 6: Gestione utente con account condiviso (multi-consulente)**

1. Se Consulente A visualizza utente "mario@example.com" che è anche associato ad Azienda Cliente #2 (Consulente B)
2. Consulente A vede **solo l'associazione relativa alla propria azienda cliente**
3. Consulente A può:
   - Modificare il **ruolo** di Mario relativamente alla propria azienda (es: Admin-Cliente in Azienda #1, Cliente semplice in Azienda #2)
   - Eliminare il link di Mario alla propria azienda (ma account Mario rimane attivo per Azienda #2)
4. Consulente A **NON può**:
   - Vedere che Mario è associato ad altre aziende
   - Modificare dati personali (nome, cognome, email, telefono) → sono read-only perché account condiviso
   - Disabilitare globalmente l'account Mario

### Edge Cases

**EC1: Email duplicata nello stesso contesto**

- Se Consulente tenta di aggiungere utente con email già usata nella stessa azienda cliente
- Sistema: Errore "Email già utilizzata per un altro utente di questa azienda"

**EC2: Email duplicata in contesto diverso (multi-consulente)**

- Se Consulente A aggiunge "mario@example.com" e Consulente B aggiunge lo stesso "mario@example.com"
- Sistema: Gestione identica a US-ANA-011 (account condiviso, nessun warning al front)

**EC3: Eliminazione ultimo utente**

- Se azienda ha 1 solo utente e Consulente tenta di eliminarlo
- Sistema: Errore "Impossibile eliminare l'ultimo utente aziendale. Ogni azienda deve avere almeno un utente."

**EC4: Eliminazione utente con account multi-azienda**

- Se Mario è associato a 3 aziende e Consulente A elimina il link ad Azienda #1
- Sistema: Rimuove solo associazione ad Azienda #1, account Mario rimane attivo per Azienda #2 e #3

**EC6: Modifica ruolo da Admin-Cliente a Cliente semplice**

- Se utente era Admin-Cliente e viene cambiato a Cliente semplice
- Sistema: L'utente **perde** la capacità di gestire utenti aziendali
- Flag permessi rimangono invariati (sono indipendenti dal ruolo)

---

## US-ANA-023: Gestire Sedi Aziendali

**Come** Admin di Piattaforma/Admin Consulente/Consulente
**Voglio** aggiungere, modificare ed eliminare sedi aziendali per un'azienda cliente
**In modo che** possa mantenere aggiornata la mappatura delle location dell'azienda

### Criteri di Accettazione

**Scenario 1: Aggiungere nuova sede aziendale**

1. Il Consulente visualizza il dettaglio azienda cliente (sezione "Sedi Aziendali")
2. Il Consulente clicca "Aggiungi Sede"
3. Il sistema mostra form "Aggiungi Sede"
4. Il Consulente compila tutti i campi required
5. Il Consulente clicca "Salva Sede"
6. Il sistema valida e salva la sede
7. Il sistema:
   - Aggiorna tabella sedi con nuova riga
   - Mostra toast "Sede aggiunta con successo"

**Scenario 2: Modificare sede aziendale esistente**

1. Il Consulente clicca icona ✏️ "Modifica" su una sede nella tabella
2. Il sistema mostra modal "Modifica Sede" con form pre-compilato
3. **Tutti i campi sono modificabili**:
4. Il Consulente modifica uno o più campi
5. Il Consulente clicca "Salva Modifiche"
6. Il sistema valida e aggiorna la sede
7. Il sistema:
   - Aggiorna riga nella tabella
   - Mostra toast "Sede aggiornata con successo"

**Scenario 3: Visualizzare dettagli sede**

1. Il Consulente clicca icona 👁️ "Visualizza" su una sede nella tabella
2. Il sistema va alla pagina dettaglio con form completo in **read-only**:

**Scenario 4: Eliminare sede aziendale**

1. Il Consulente clicca icona 🗑️ "Elimina" su una sede nella tabella
2. Il sistema mostra confirm dialog:
   - Titolo: "⚠️ Conferma Eliminazione"
   - Messaggio: "Sei sicuro di voler eliminare la sede [Tipo Sede] - [Indirizzo] [Città]?"
   - Pulsanti: "Elimina" (danger) | "Annulla"
3. Il Consulente clicca "Elimina"
4. Il sistema valida:
   - Controlla che **non sia l'ultima sede** dell'azienda cliente
   - Se è l'ultima → errore "❌ Impossibile eliminare l'ultima sede. Ogni azienda deve avere almeno una sede."
5. Se validazione OK → sistema:
   - Elimina la sede (soft delete)
   - Chiude dialog
   - Rimuove riga dalla tabella
   - Mostra toast "Sede eliminata con successo"

### Edge Cases

**EC1: Eliminazione ultima sede**

- Se azienda ha 1 sola sede e Consulente tenta di eliminarla
- Sistema: Errore "Impossibile eliminare l'ultima sede. Ogni azienda deve avere almeno una sede."

**EC2: Duplicazione sede (stesso indirizzo)**

- Sistema **non impedisce** l'inserimento di sedi duplicate
- Motivazione: Un'azienda può avere più uffici nello stesso edificio (es: piani diversi)

**EC3: Validazione CAP/Provincia per nazioni diverse**

- Se Nazione ≠ Italia → CAP e Provincia non hanno validazione formato specifica (free text)

**EC4: Modifica Tipo Sede da Legale ad altro**

- Se l'unica sede con tipo "Sede Legale" viene cambiata a "Operativa"
- Sistema: **Permette** la modifica (nessun vincolo che impone almeno una sede legale)

**EC5: Sede referenziata in audit/fornitori**

- Se una sede è referenziata in audit o fornitori
- Sistema: **Permette eliminazione** (o implementa soft delete mantenendo referenze storiche)

---

## US-ANA-024: Eliminare Azienda Cliente

**Come** Admin di Piattaforma/Admin Consuelente/Consulente
**Voglio** eliminare un'azienda cliente che non gestisco più
**In modo che** possa mantenere pulita la mia lista di clienti

### Criteri di Accettazione

**Scenario 1: Tentativo di eliminazione con audit attivi**

1. Il Consulente visualizza dettaglio azienda cliente
2. Il Consulente clicca pulsante "Elimina" (icona 🗑️ in header)
3. Il sistema mostra confirm dialog:
   - Titolo: "⚠️ Conferma Eliminazione"
   - Messaggio: "Sei sicuro di voler eliminare l'azienda [Ragione Sociale]? Questa azione è irreversibile."
   - Warning: "Verranno eliminati anche: X sedi, Y utenti aziendali, Z audit, W fornitori"
   - Pulsanti: "Elimina" (danger) | "Annulla"
4. Il Consulente clicca "Elimina"
5. Il sistema valida:
   - Controlla se esistono audit con stato "In Corso" o "In Bozza"
   - Se **esistono audit attivi**:
     - Mostra errore: "❌ Impossibile eliminare l'azienda. Ci sono audit attivi. Completa o elimina gli audit prima di procedere."
     - Lista audit attivi: "[Codice Audit] - [Framework] - [Stato]"
     - Pulsante "Annulla" per chiudere
   - Se **non ci sono audit attivi**:
     - Procede con eliminazione (vedi Scenario 2)

**Scenario 2: Eliminazione con successo**

1. Il sistema esegue **eliminazione a cascata** (transazione atomica):

   a. **Elimina record Azienda Cliente**

   b. **Elimina Sedi Aziendali** associate (tutte)

   c. **Gestisce Utenti Aziendali**:

   - Per ogni utente aziendale:
     - Elimina record "Utente Aziendale" (link tra account e azienda)
     - Se account utente è associato **solo a questa azienda** → **disabilita account**
     - Se account utente è associato **a più aziende (multi-consulente)** → **mantiene account attivo** (rimuove solo link)

   d. **Elimina Audit** associati (inclusi dettagli risposte, azioni correttive, ecc.)

   e. **Elimina Fornitori e Qualifiche** associate

2. Se eliminazione OK → sistema:

   - Chiude dialog
   - Mostra toast "Azienda cliente eliminata con successo"
   - Redirect a lista "Aziende Clienti"

3. Se errore durante eliminazione → sistema:
   - Rollback transazione completa
   - Mostra errore "Errore durante l'eliminazione. Riprova o contatta il supporto."

**Scenario 3: Admin-Consulente elimina azienda di altro consulente**

1. Admin-Consulente può eliminare qualsiasi azienda della propria azienda di consulenza
2. Flusso identico a Scenario 1-2

**Scenario 4: Impatto su utenti aziendali multi-contesto**

1. Se l'azienda ha utente "mario@example.com" associato anche ad Azienda Cliente #2 (Consulente B)
2. Eliminazione Azienda Cliente #1:
   - Rimuove link di Mario ad Azienda #1
   - Account Mario rimane attivo per Azienda #2
   - Mario al prossimo login vede solo Azienda #2 nel context switcher

### Edge Cases

**EC1: Eliminazione concorrente**

- Se due utenti (es: Consulente e Admin-Consulente) tentano di eliminare la stessa azienda simultaneamente
- Sistema: First-come-first-served. Il secondo riceve errore "Azienda non trovata"

**EC2: Audit completati non bloccano eliminazione**

- Solo audit con stato "In Corso" o "In Bozza" bloccano eliminazione
- Audit "Completato" o "Archiviato" vengono eliminati insieme all'azienda

**EC3: Eliminazione con fornitori referenziati**

- Se l'azienda ha fornitori che sono anche fornitori di altre aziende (scenario improbabile in multi-tenancy)
- Sistema: Elimina solo le associazioni fornitore-azienda, non il fornitore globale (se applicabile)

**EC4: Eliminazione azienda con documenti caricati**

- Se esistono file/documenti caricati (es: allegati audit, documenti fornitori)
- Sistema: Elimina anche i file fisici dal storage (S3/file system)

---

## US-ANA-025: Ricercare e Filtrare Aziende Clienti

**Come** Consulente
**Voglio** cercare e filtrare le aziende clienti per trovare rapidamente quella che mi interessa
**In modo che** possa accedere velocemente alle informazioni di cui ho bisogno

### Criteri di Accettazione

**Scenario 1: Ricerca testuale globale**

1. Il Consulente accede alla lista "Aziende Clienti"
2. Il sistema mostra un campo di ricerca prominente sopra la tabella:
   - Placeholder: "Cerca per Ragione Sociale, Partita IVA o Codice Fiscale..."
   - Icona 🔍
3. Il Consulente digita "Acme" nel campo di ricerca
4. Il sistema filtra la tabella in tempo reale (debounce 300ms) mostrando solo aziende che contengono "Acme" in:
   - Ragione Sociale
   - Partita IVA
   - Codice Fiscale
5. Se nessun risultato → messaggio "Nessuna azienda trovata per la ricerca 'Acme'"

**Nota informativa**:
"Il debounce di 300ms ottimizza le performance evitando troppe richieste al server durante la digitazione. L'aggiornamento avviene automaticamente dopo 300ms dall'ultimo carattere digitato."

**Scenario 2: Filtri avanzati**

1. Il Consulente clicca pulsante "Filtri Avanzati" (icona ⚙️ accanto al campo di ricerca)
2. Il sistema mostra un pannello collapsible con filtri aggiuntivi:

   **Filtri disponibili**:

   - **Settore di Attività** (dropdown multi-select) → valori da tabella codifiche
   - **Dimensione Aziendale** (dropdown multi-select) → Micro/Piccola/Media/Grande
   - **Stato Conformità** (dropdown multi-select) → Conforme/Non Conforme/In Valutazione/N/A
   - **Consulente Assegnato** (dropdown) → visibile solo per Admin di piattaforma-Consulente/Admin
   - **Data Creazione** (date range picker) → "Da [data] A [data]"
   - **Sedi Presenti** (checkbox) → "Solo aziende con più di 1 sede"

3. Il Consulente seleziona filtri (es: Settore = "Sanità", Dimensione = "Grande")
4. Il Consulente clicca "Applica Filtri"
5. Il sistema filtra la tabella mostrando solo aziende che matchano **tutti i filtri** (AND logic)
6. Il sistema mostra un badge "X filtri attivi" sopra la tabella
7. Il Consulente può cliccare "Rimuovi Filtri" per resettare

**Scenario 3: Combinazione ricerca + filtri**

1. Il Consulente digita "S.p.A." nel campo di ricerca
2. Il Consulente applica filtro "Stato Conformità = Non Conforme"
3. Il sistema mostra solo aziende con:
   - Ragione Sociale contenente "S.p.A." **E**
   - Stato Conformità = "Non Conforme"

**Scenario 4: Ordinamento colonne**

1. Il Consulente clicca su header colonna "Data Creazione"
2. Il sistema ordina la tabella per Data Creazione DESC (più recenti prima)
3. Icona freccia ↓ appare accanto a "Data Creazione"
4. Il Consulente clicca nuovamente → ordina ASC (più vecchie prima)
5. Icona freccia ↑
6. Ordinamento persiste anche con ricerca/filtri attivi

**Scenario 5: Salvataggio preferenze ricerca**

1. Il sistema salva in session storage:
   - Ultimo valore del campo di ricerca
   - Filtri applicati
   - Ordinamento colonna
2. Se il Consulente naviga via e ritorna alla lista → trova ricerca/filtri già applicati
3. Pulsante "Reset" per azzerare tutto

### Field Specifications

**Campo Ricerca Globale**:

| Campo        | Label          | Tipo | Placeholder                                                  | Note                             |
| ------------ | -------------- | ---- | ------------------------------------------------------------ | -------------------------------- |
| search_query | (nessun label) | Text | "Cerca per Ragione Sociale, Partita IVA o Codice Fiscale..." | Debounce 300ms                   |
| search_icon  | 🔍             | Icon | -                                                            | Posizione: inside left del campo |

**Pannello Filtri Avanzati**:

| Filtro               | Tipo                   | Valori                                   | Comportamento                   |
| -------------------- | ---------------------- | ---------------------------------------- | ------------------------------- |
| Settore di Attività  | Dropdown multi-select  | Da tabella codifiche                     | OR logic se multi-selezione     |
| Dimensione Aziendale | Dropdown multi-select  | Micro/Piccola/Media/Grande               | OR logic                        |
| Stato Conformità     | Dropdown multi-select  | Conforme/Non Conforme/In Valutazione/N/A | OR logic                        |
| Consulente Assegnato | Dropdown single-select | Lista consulenti (filtrata per ruolo)    | -                               |
| Data Creazione       | Date range picker      | Date picker "Da" e "A"                   | Filtra range inclusivo          |
| Sedi Presenti        | Checkbox               | Boolean                                  | Mostra solo aziende con >1 sede |

**Badge Filtri Attivi**:

| Campo                 | Tipo   | Visibilità                         | Note                                      |
| --------------------- | ------ | ---------------------------------- | ----------------------------------------- |
| badge_filtri_attivi   | Badge  | Condizionale (se filtri applicati) | Formato: "3 filtri attivi", colore blu    |
| button_rimuovi_filtri | Button | Accanto al badge                   | Testo "Rimuovi Filtri", colore secondario |

### Edge Cases

**EC1: Ricerca senza risultati**

- Sistema mostra messaggio "Nessuna azienda trovata per la ricerca '[query]'. Prova a modificare i criteri."

**EC2: Filtri senza risultati**

- Sistema mostra messaggio "Nessuna azienda corrisponde ai filtri applicati. Rimuovi alcuni filtri per vedere risultati."

**EC3: Performance con molte aziende (>1000)**

- Ricerca testuale: query al backend con indice full-text
- Filtri: query al backend con WHERE clauses ottimizzate
- Paginazione: client-side dopo fetch filtrato

**EC4: Filtro Consulente Assegnato per Admin di piattaforma**

- Admin di piattaforma di piattaforma vede dropdown con **tutti i consulenti** (formato: "[Nome] ([Azienda Consulenza])")
- Admin-Consulente vede dropdown con **solo consulenti della propria azienda di consulenza**

**EC5: Persistenza tra sessioni**

- Ricerca/filtri salvati in **session storage** (non persistono dopo logout)
- Motivazione: evitare confusione con filtri obsoleti

**EC6: URL con query string**

- Sistema supporta deep linking: `/aziende-clienti?search=Acme&stato=non_conforme`
- Utile per condividere link filtrati tra team

**EC7: Export risultati filtrati**

- Pulsante "Esporta CSV" esporta **solo le aziende visibili** dopo ricerca/filtri
- CSV include tutte le colonne della tabella

### Dependencies

- **PRE**: US-ANA-010 (Visualizzare lista aziende)
- **PRE**: Tabella codifiche `Settore_Attività` popolata
- **PRE**: Sistema calcolo conformità attivo
- **POST**: Export CSV (feature separata)

---

## Riepilogo User Stories - Gestione Aziende Clienti

| ID         | Titolo                                 | Priorità    | Complessità | Dipendenze             |
| ---------- | -------------------------------------- | ----------- | ----------- | ---------------------- |
| US-ANA-010 | Visualizzare Lista Aziende Clienti     | Must-have   | Bassa       | -                      |
| US-ANA-011 | Creare Nuova Azienda Cliente           | Must-have   | Alta        | US-ANA-010             |
| US-ANA-012 | Gestire Scenario Multi-Consulente      | Must-have   | Alta        | US-ANA-011             |
| US-ANA-013 | Utilizzare Context Switcher            | Must-have   | Media       | US-ANA-012             |
| US-ANA-014 | Visualizzare Dettaglio Azienda Cliente | Must-have   | Media       | US-ANA-011             |
| US-ANA-015 | Modificare Dati Azienda Cliente        | Must-have   | Bassa       | US-ANA-014             |
| US-ANA-016 | Cambiare Consulente Assegnato          | Should-have | Media       | US-ANA-014             |
| US-ANA-017 | Gestire Utenti Aziendali               | Must-have   | Alta        | US-ANA-014, US-ANA-012 |
| US-ANA-023 | Gestire Sedi Aziendali                 | Must-have   | Bassa       | US-ANA-014             |
| US-ANA-024 | Eliminare Azienda Cliente              | Should-have | Media       | US-ANA-014             |
| US-ANA-025 | Ricercare e Filtrare Aziende Clienti   | Should-have | Media       | US-ANA-010             |

---

## Note Tecniche per Sviluppatori

### Struttura Dati - Tabelle Coinvolte

**Tabella: `aziende_clienti`**

- `id` (PK)
- `ragione_sociale`
- `partita_iva` (unique per tenant - nota: può essere duplicata cross-tenant)
- `codice_fiscale`
- `settore_attivita_id` (FK a `settori_attivita`)
- `dimensione_aziendale` (enum)
- `sito_web`
- `telefono`
- `email_generale`
- `consulente_id` (FK a `utenti` dove ruolo = 'Consulente')
- `created_at`
- `updated_at`

**Tabella: `sedi_aziendali`**

- `id` (PK)
- `azienda_cliente_id` (FK a `aziende_clienti`)
- `tipo_sede` (enum)
- `indirizzo`
- `civico`
- `cap`
- `citta`
- `provincia`
- `nazione`
- `created_at`

**Tabella: `utenti_aziendali`** (junction table tra `utenti` e `aziende_clienti`)

- `id` (PK)
- `utente_id` (FK a `utenti`)
- `azienda_cliente_id` (FK a `aziende_clienti`)
- `ruolo` (enum: 'Admin-Cliente', 'Cliente')
- `flag_puo_creare_fornitori` (boolean)
- `flag_puo_compilare_audit` (boolean)
- `created_at`
- **Unique constraint**: (`utente_id`, `azienda_cliente_id`) → un utente può essere associato a una azienda una sola volta

**Tabella: `utenti`** (globale, account unici)

- `id` (PK)
- `email` (unique globalmente)
- `password_hash`
- `nome`
- `cognome`
- `telefono`
- `stato_invito` (enum: 'Pending', 'Attivo', 'Disabilitato')
- `ultimo_accesso`
- `created_at`

### Logica Multi-Tenancy

**Segregazione Dati**:

- Ogni query deve filtrare per `consulente_id` (o azienda di consulenza per Admin di piattaforma-Consulente)
- Middleware di autenticazione aggiunge automaticamente clausola WHERE al context

**Context Switcher**:

- Frontend: Store Redux/Vuex con `selectedAziendaClienteId`
- Backend: API richiede header `X-Context-Azienda-Cliente-Id` per utenti con ruolo "Azienda"
- Validazione: Backend verifica che l'utente abbia effettivamente accesso all'azienda cliente specificata

### API Endpoints Suggeriti

```
GET    /api/aziende-clienti                    → Lista aziende (filtrate per tenant)
POST   /api/aziende-clienti                    → Crea azienda
GET    /api/aziende-clienti/:id                → Dettaglio azienda
PUT    /api/aziende-clienti/:id                → Modifica azienda
DELETE /api/aziende-clienti/:id                → Elimina azienda
PUT    /api/aziende-clienti/:id/consulente     → Cambia consulente assegnato

GET    /api/aziende-clienti/:id/sedi           → Lista sedi
POST   /api/aziende-clienti/:id/sedi           → Crea sede
PUT    /api/sedi/:id                           → Modifica sede
DELETE /api/sedi/:id                           → Elimina sede

GET    /api/aziende-clienti/:id/utenti         → Lista utenti aziendali
POST   /api/aziende-clienti/:id/utenti         → Crea utente aziendale
PUT    /api/utenti-aziendali/:id               → Modifica ruolo utente
DELETE /api/utenti-aziendali/:id               → Elimina utente aziendale
POST   /api/utenti-aziendali/:id/resend-invite → Re-invia email invito
```

### Validazioni Backend Critiche

1. **Creazione Azienda**: Transazione atomica per azienda + sedi + utenti
2. **Email Duplicata**: Rilevamento account esistente e merge intelligente
3. **Eliminazione**: Cascade delete con controllo audit attivi
4. **Cambio Consulente**: Verifica assenza audit attivi
5. **Multi-tenancy**: Ogni endpoint valida accesso basato su ruolo e tenant

---

**Fine User Stories - Gestione Aziende Clienti**
