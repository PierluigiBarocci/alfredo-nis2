# Product Requirements Document (PRD)

# Piattaforma di Conformità

**Versione**: 1.1
**Data**: 2025-12-15
**Stato**: Draft
**Progetto**: Piattaforma di Conformità
**Tipo**: Piattaforma SaaS Multi-Tenant

---

## Indice

1. [Executive Summary](#1-executive-summary)
2. [Panoramica Prodotto](#2-panoramica-prodotto)
3. [Obiettivi di Business](#3-obiettivi-di-business)
4. [Utenti e Personas](#4-utenti-e-personas)
5. [Requisiti Funzionali](#5-requisiti-funzionali)
   - [5.1 Anagrafiche](#51-anagrafiche)
   - [5.2 Autenticazione (TBD)](#52-autenticazione-tbd)
   - [5.3 Framework Normativi (TBD)](#53-framework-normativi-tbd)
   - [5.4 Audit e Compliance (TBD)](#54-audit-e-compliance-tbd)
   - [5.5 Gestione Fornitori (TBD)](#55-gestione-fornitori-tbd)
   - [5.6 Azioni Correttive (TBD)](#56-azioni-correttive-tbd)
   - [5.7 Reporting (TBD)](#57-reporting-tbd)
6. [Requisiti Non Funzionali](#6-requisiti-non-funzionali)
7. [Vincoli e Assunzioni](#7-vincoli)
8. [Appendici](#8-appendici)

---

## 1. Executive Summary

### 1.1 Descrizione del Prodotto

La **Piattaforma di Conformità** è una soluzione SaaS multi-tenant progettata per gestire audit di conformità normativa (NIS2, CIS Controls) con funzionalità di qualifica fornitori, azioni correttive e reportistica automatizzata.

Il prodotto trasforma la gestione manuale della conformità (attualmente su database Access) in un sistema cloud strutturato, scalabile e multi-cliente per consulenti di compliance e aziende.

### 1.2 Problema da Risolvere

**Pain point attuali**:

- Gestione manuale su database Access non scalabile
- Nessuna segregazione dati tra clienti
- Processi di audit frammentati e non standardizzati
- Nessun sistema di notifiche automatiche per scadenze azioni correttive

### 1.3 Proposta di Valore

**Benefici chiave**:

- **Multi-tenancy rigoroso**: Segregazione completa dati per consulente con visibilità basata su ruolo
- **Tracciabilità completa**: Storicizzazione audit, azioni e valutazioni con audit trail immutabile
- **Automazione**: Generazione automatica report PDF, notifiche email scadenze, calcolo compliance
- **Scalabilità**: Gestione centinaia di aziende clienti e migliaia di utenti con performance garantite
- **Compliance by design**: Conformità GDPR, soft delete, MFA obbligatorio

### 1.4 Scope MVP

**In scope (Release 1.0 - MVP)**:

- Gestione completa anagrafiche (utenti, aziende, sedi) con multi-tenancy
- Autenticazione email+password con MFA obbligatorio
- Gestione framework normativi NIS2/CIS (struttura gerarchica Ambito → Tematica → Categoria → Requisito)
- Audit di conformità con valutazioni requisiti e calcolo compliance
- Processo qualifica fornitori con link temporaneo (7gg validità)
- Piano azioni correttive con scadenze e notifiche
- 4 report PDF standard (Report Audit, Compliance per Framework, Piano Azioni, Qualifica Fornitori)

**Out of scope (Release future)**:

- Analytics avanzati e dashboard predittivi
- Mobile app nativa (iOS/Android)
- Integrazione con sistemi esterni (OverRisk, SIEM)
- Multi-lingua (solo italiano in MVP)
- SSO/SAML federato
- Machine Learning per suggerimenti azioni

---

## 2. Panoramica Prodotto

### 2.1 Visione

(TBD)

### 2.2 Posizionamento

(TBD)

---

## 3. Obiettivi di Business

### 3.1 Obiettivi Primari (Must-Achieve)

1. **Parità funzionale con Access**: Replicare TUTTE le funzionalità del DB Access attuale + miglioramenti UX
2. **Multi-tenancy funzionante**: Segregazione dati verificata con test multi-utente (Consulente A non vede dati Consulente B)
3. **4 report PDF generati correttamente**: Template statici con intestazione, dati dinamici, export lato client
4. **CRUD completo**: Tutte le anagrafiche (utenti, aziende, framework, audit) gestibili via UI

### 3.2 Obiettivi Secondari (Nice-to-Have)

- Dashboard con KPI in tempo reale (contatori filtrati per tenant)
- Export CSV liste per analisi offline

---

## 4. Utenti e Personas

### 4.1 Ruoli Utente

La piattaforma supporta 4 ruoli distinti con permessi e visibilità diversi:

#### 4.1.1 Admin Piattaforma

**Descrizione**: Amministratore con accesso completo alla piattaforma, gestisce aziende di consulenza e configurazioni globali.

**Permessi**:

- CRUD completo su TUTTE le entità (aziende consulenza, aziende clienti, utenti, framework, audit)
- Visibilità globale senza filtri tenant
- Configurazione limiti per aziende consulenza
- Gestione utenti Admin (con vincoli: no auto-eliminazione, no eliminazione ultimo Admin)

**Responsabilità**:

- Onboarding nuove aziende di consulenza
- Configurazione framework normativi
- Supporto di secondo livello

#### 4.1.2 Consulente (Admin-Consulente e Consulente semplice)

**Descrizione**: Professionista di compliance che gestisce audit per aziende clienti.

**Sottotipi**:

- **Admin-Consulente**: Gestisce consulenti della propria azienda, vede TUTTE le aziende clienti dell'azienda di consulenza
- **Consulente semplice**: Vede SOLO aziende clienti a cui è esplicitamente assegnato

**Permessi**:

- CRUD aziende clienti assegnate (con sedi e utenti aziendali)
- Creazione e gestione audit
- Gestione azioni correttive
- Visibilità filtrata per tenant (multi-tenancy rigoroso)

**Responsabilità**:

- Pianificazione ed esecuzione audit conformità
- Valutazione requisiti
- Monitoraggio piano azioni

#### 4.1.3 Utente Aziendale (Admin Cliente e Cliente semplice)

**Descrizione**: Referente aziendale che consulta lo stato conformità della propria azienda.

**Sottotipi**:

- **Admin Cliente**: Gestisce utenti aziendali della propria azienda
- **Cliente semplice**: Accesso viewer

**Permessi**:

- Visualizzazione audit della propria azienda (read-only)
- Visualizzazione report di conformità
- Visualizzazione piano azioni assegnate
- Opzionale: compilazione audit (se flag attivo), creazione fornitori (se flag attivo)

**Responsabilità**:

- Consultazione stato conformità
- Supporto al consulente durante audit
- Implementazione azioni correttive

#### 4.1.4 Fornitore (Accesso Temporaneo)

**Descrizione**: Fornitore esterno che compila questionario di qualifica tramite link temporaneo.

**Permessi**:

- Accesso tramite token univoco (validità 7 giorni)
- Compilazione form qualifica fornitore (no login/password)
- Caricamento documenti (max 10MB per file)

**Responsabilità**:

- Compilazione questionario di qualifica entro scadenza
- Caricamento certificazioni richieste

---

## 5. Requisiti Funzionali

### 5.1 Anagrafiche

#### 5.1.1 Obiettivo

Implementare la gestione completa delle anagrafiche per utenti (Admin Piattaforma, Consulenti, Utenti Aziendali), Aziende di Consulenza e Aziende Clienti (con Sedi), con supporto multi-tenancy rigoroso e segregazione dati per consulente.

#### 5.1.2 Scope Funzionale

Questa sezione copre:

**Gestione Utenti**:

- Admin Piattaforma (CRUD con validazione vincoli: no auto-eliminazione, no ultimo Admin)
- Consulenti (Admin-Consulente e Consulente semplice) collegati ad Aziende Consulenza
- Utenti Aziendali (Admin Cliente e Cliente semplice) collegati ad Aziende Clienti
- Lista unificata utenti con azioni contestuali intelligenti (redirect automatico al contesto appropriato)
- Modal selezione tipo utente per creazione (3 flussi: Admin inline, Consulente → redirect Aziende Consulenza, Utente Aziendale → redirect Aziende Clienti)
- Filtri e ricerca globale (nome, cognome, email, telefono)

**Gestione Aziende di Consulenza**:

- CRUD completo Aziende Consulenza (Admin)
- Validazione P.IVA univoca (11 cifre numeriche)
- Validazione Codice Fiscale univoco (11 o 16 caratteri alfanumerici)
- Gestione consulenti collegati (CRUD completo in sezione dedicata)
- Gestione limiti (max aziende clienti, max utenti aziende) configurabili
- Visualizzazione aziende clienti associate (widget nel dettaglio)
- Validazione vincoli eliminazione (blocco se esistono aziende clienti attive o audit attivi)
- Filtri e ricerca (nome azienda, P.IVA, referente)

**Gestione Aziende Clienti**:

- CRUD completo Aziende Clienti (Consulente e Admin)
- Validazione P.IVA o CF obbligatori (almeno uno dei due, univoci)
- Assegnazione singolo consulente (scenario base) + multi-consulente (scenario avanzato)
- Multi-tenancy logico: Consulente vede SOLO le proprie aziende clienti, Admin vede TUTTE
- Gestione Sedi Aziendali (CRUD completo, almeno 1 sede obbligatoria)
- Gestione Utenti Aziendali (CRUD completo, assegnati a sede specifica)
- Validazione vincoli eliminazione (blocco se ci sono audit attivi, sedi, utenti)
- Filtri e ricerca (ragione sociale, P.IVA, consulente assegnato)

**Dashboard & KPI**:

- Contatori dashboard filtrati per tenant (Admin vede globale, Consulente vede solo propri dati)
- Widget: Aziende registrate, Consulenti, Azioni attive (con trend vs anno precedente)

**Sistema**:

- Soft delete per tutte le entità (preservazione audit trail con flag `deleted_at`)
- Validazione email univoca globale (cross-tenant)
- Invio email benvenuto con credenziali temporanee (12 caratteri alfanumerici)
- Blocco creazione al raggiungimento soglie massime configurate
- Paginazione server-side su tutte le liste (10/25/50 rows per page)

#### 5.1.3 Mapping Entità Anagrafiche

Di seguito la struttura dettagliata delle entità anagrafiche con campi, tipi di dato, relazioni e vincoli.

##### 5.1.3.1 Entità: Admin Piattaforma

**Descrizione**: Utente amministratore con accesso completo alla piattaforma.

**Tabella database**: `utenti` (con `ruolo = 'Admin Piattaforma'`)

**Campi**:

| Campo      | Tipo      | Lunghezza | Required | Unique       | Default  | Vincoli                                 | Descrizione                              |
| ---------- | --------- | --------- | -------- | ------------ | -------- | --------------------------------------- | ---------------------------------------- |
| id         | UUID      | -         | Sì       | Sì           | auto     | PK                                      | Identificatore univoco                   |
| nome       | VARCHAR   | 100       | Sì       | No           | -        | Solo alfabetici, spazi, apostrofi       | Nome amministratore                      |
| cognome    | VARCHAR   | 100       | Sì       | No           | -        | Solo alfabetici, spazi, apostrofi       | Cognome amministratore                   |
| email      | VARCHAR   | 255       | Sì       | Sì (globale) | -        | Formato email valido, lowercase         | Email per login (univoca cross-tenant)   |
| telefono   | VARCHAR   | 20        | No       | No           | null     | Formato internazionale (+XX XXX XXXXXX) | Telefono di contatto                     |
| ruolo      | ENUM      | -         | Sì       | No           | -        | 'Admin Piattaforma'                     | Tipo utente fisso                        |
| stato      | ENUM      | -         | Sì       | No           | 'Attivo' | 'Attivo', 'Disattivato'                 | Stato account                            |
| created_at | TIMESTAMP | -         | Sì       | No           | now()    | -                                       | Data creazione                           |
| updated_at | TIMESTAMP | -         | Sì       | No           | now()    | -                                       | Data ultima modifica                     |
| deleted_at | TIMESTAMP | -         | No       | No           | null     | Soft delete                             | Data eliminazione (null = non eliminato) |
| deleted_by | UUID      | -         | No       | No           | null     | FK → utenti.id                          | Admin che ha eliminato questo record     |

**Regole di business**:

- **Vincolo eliminazione 1**: Non è possibile eliminare se stesso (auto-eliminazione bloccata)
- **Vincolo eliminazione 2**: Non è possibile eliminare l'ultimo Admin attivo della piattaforma (deve esistere almeno 1 Admin)
- **Vincolo modifica**: Email NON modificabile dopo creazione (campo read-only in form modifica)
- **Soft delete**: Eliminazione logica con flag `deleted_at` (preservazione audit trail)

**Validazioni**:

- Email: regex `^[^\s@]+@[^\s@]+\.[^\s@]+$`, case-insensitive
- Telefono: regex `^\+\d{1,3}\s\d{2,4}\s\d{6,10}$` (se compilato)
- Nome/Cognome: regex `^[a-zA-ZÀ-ÿ\s']{1,100}$`
- Password temporanea: 12 caratteri alfanumerici (maiuscole, minuscole, numeri, simboli), validità 7 giorni

---

##### 5.1.3.2 Entità: Azienda di Consulenza

**Descrizione**: Studio o società di consulenza che gestisce audit per aziende clienti.

**Tabella database**: `aziende_consulenza`

**Campi**:

| Campo               | Tipo      | Lunghezza | Required | Unique       | Default | Vincoli                                  | Descrizione                                    |
| ------------------- | --------- | --------- | -------- | ------------ | ------- | ---------------------------------------- | ---------------------------------------------- |
| id                  | UUID      | -         | Sì       | Sì           | auto    | PK                                       | Identificatore univoco                         |
| nome_azienda        | VARCHAR   | 255       | Sì       | No           | -       | Max 255 char                             | Ragione sociale                                |
| indirizzo           | VARCHAR   | 255       | Sì       | No           | -       | Max 255 char                             | Indirizzo completo (via, civico, città, CAP)   |
| p_iva               | VARCHAR   | 11        | Sì       | Sì (globale) | -       | Esattamente 11 cifre numeriche           | Partita IVA (univoca)                          |
| codice_fiscale      | VARCHAR   | 16        | Sì       | Sì (globale) | -       | 11 o 16 caratteri alfanumerici uppercase | Codice fiscale (univoco)                       |
| email               | VARCHAR   | 255       | Sì       | No           | -       | Formato email valido                     | Email generale azienda                         |
| telefono            | VARCHAR   | 20        | Sì       | No           | -       | Formato internazionale                   | Telefono azienda                               |
| note                | TEXT      | -         | No       | No           | null    | Max 1000 char                            | Note libere                                    |
| max_aziende_clienti | INTEGER   | -         | Sì       | No           | -       | > 0                                      | Limite massimo aziende clienti creabili        |
| max_utenti_aziende  | INTEGER   | -         | Sì       | No           | -       | > 0                                      | Limite massimo utenti aziende clienti creabili |
| created_at          | TIMESTAMP | -         | Sì       | No           | now()   | -                                        | Data creazione                                 |
| created_by          | UUID      | -         | Sì       | No           | -       | FK → utenti.id                           | Admin che ha creato l'azienda                  |
| updated_at          | TIMESTAMP | -         | Sì       | No           | now()   | -                                        | Data ultima modifica                           |
| deleted_at          | TIMESTAMP | -         | No       | No           | null    | Soft delete                              | Data eliminazione                              |

**Relazioni**:

- **1 Azienda Consulenza → N Consulenti** (1:N via `utenti.azienda_consulenza_id`)
- **1 Azienda Consulenza → N Aziende Clienti** (1:N via `aziende_clienti.azienda_consulenza_id`)

**Regole di business**:

- **Primo Admin-Consulente obbligatorio**: Al momento della creazione, deve essere creato almeno 1 Admin-Consulente collegato
- **Vincolo eliminazione**: Bloccare eliminazione se esistono aziende clienti attive o audit attivi
- **Modifica limiti**: Se si modificano `max_aziende_clienti` o `max_utenti_aziende`, il nuovo valore deve essere >= al numero già creato (no riduzione sotto soglia attuale)
- **Soft delete**: Eliminazione logica con `deleted_at`, disattivazione di tutti i consulenti collegati

**Validazioni**:

- P.IVA: esattamente 11 cifre numeriche, univoca globalmente
- Codice Fiscale: 11 o 16 caratteri alfanumerici uppercase, univoco globalmente
- max_aziende_clienti: integer > 0
- max_utenti_aziende: integer > 0

---

##### 5.1.3.3 Entità: Consulente

**Descrizione**: Professionista di compliance collegato a un'Azienda di Consulenza.

**Tabella database**: `utenti` (con `ruolo IN ('Admin Consulente', 'Consulente')`)

**Campi**:

| Campo                 | Tipo      | Lunghezza | Required | Unique       | Default  | Vincoli                          | Descrizione                           |
| --------------------- | --------- | --------- | -------- | ------------ | -------- | -------------------------------- | ------------------------------------- |
| id                    | UUID      | -         | Sì       | Sì           | auto     | PK                               | Identificatore univoco                |
| azienda_consulenza_id | UUID      | -         | Sì       | No           | -        | FK → aziende_consulenza.id       | Azienda di consulenza di appartenenza |
| nome                  | VARCHAR   | 100       | Sì       | No           | -        | Solo alfabetici, spazi           | Nome consulente                       |
| cognome               | VARCHAR   | 100       | Sì       | No           | -        | Solo alfabetici, spazi           | Cognome consulente                    |
| email                 | VARCHAR   | 255       | Sì       | Sì (globale) | -        | Formato email valido, lowercase  | Email per login                       |
| telefono              | VARCHAR   | 20        | Sì       | No           | -        | Formato internazionale           | Telefono consulente                   |
| ruolo                 | ENUM      | -         | Sì       | No           | -        | 'Admin Consulente', 'Consulente' | Tipo consulente                       |
| is_admin              | BOOLEAN   | -         | Sì       | No           | false    | Derivato da ruolo                | True se Admin Consulente              |
| stato                 | ENUM      | -         | Sì       | No           | 'Attivo' | 'Attivo', 'Disattivato'          | Stato account                         |
| created_at            | TIMESTAMP | -         | Sì       | No           | now()    | -                                | Data creazione                        |
| updated_at            | TIMESTAMP | -         | Sì       | No           | now()    | -                                | Data ultima modifica                  |
| deleted_at            | TIMESTAMP | -         | No       | No           | null     | Soft delete                      | Data eliminazione                     |

**Relazioni**:

- **N Consulenti → 1 Azienda Consulenza** (N:1 via `azienda_consulenza_id`)
- **N Consulenti → M Aziende Clienti** (N:M via tabella junction `consulenti_aziende_clienti`)

**Regole di business**:

- **Admin-Consulente**: Vede TUTTE le aziende clienti dell'azienda consulenza, indipendentemente dalle assegnazioni esplicite
- **Consulente semplice**: Vede SOLO aziende clienti a cui è esplicitamente assegnato (multi-tenancy rigoroso)
- **Vincolo eliminazione**: Non è possibile eliminare l'unico Admin-Consulente dell'azienda (deve esistere almeno 1)
- **Assegnazione aziende**: Gestita in tabella `consulenti_aziende_clienti` (solo per consulenti semplici, Admin-Consulente accede a tutte)

**Validazioni**:

- Email: univoca globalmente
- Telefono: formato internazionale obbligatorio

---

##### 5.1.3.4 Entità: Azienda Cliente

**Descrizione**: Azienda soggetta a normativa NIS2 che viene auditata dai consulenti.

**Tabella database**: `aziende_clienti`

**Campi**:

| Campo                 | Tipo      | Lunghezza | Required | Unique           | Default | Vincoli                             | Descrizione                                    |
| --------------------- | --------- | --------- | -------- | ---------------- | ------- | ----------------------------------- | ---------------------------------------------- |
| id                    | UUID      | -         | Sì       | Sì               | auto    | PK                                  | Identificatore univoco                         |
| azienda_consulenza_id | UUID      | -         | Sì       | No               | -       | FK → aziende_consulenza.id          | Azienda consulenza che gestisce questo cliente |
| ragione_sociale       | VARCHAR   | 255       | Sì       | No               | -       | Max 255 char                        | Ragione sociale azienda                        |
| indirizzo             | VARCHAR   | 255       | Sì       | No               | -       | Max 255 char                        | Indirizzo sede legale                          |
| partita_iva           | VARCHAR   | 11        | No       | Sì (se presente) | null    | 11 cifre numeriche                  | Partita IVA (univoca se presente)              |
| codice_fiscale        | VARCHAR   | 16        | No       | Sì (se presente) | null    | 16 caratteri alfanumerici uppercase | Codice fiscale (univoco se presente)           |
| telefono              | VARCHAR   | 20        | Sì       | No               | -       | Formato internazionale              | Telefono azienda                               |
| PEC                   | VARCHAR   | 255       | Sì       | No               | -       | Formato email valido                | Email generale azienda                         |
| note                  | TEXT      | -         | No       | No               | null    | Max 1000 char                       | Note libere                                    |
| created_at            | TIMESTAMP | -         | Sì       | No               | now()   | -                                   | Data creazione                                 |
| created_by            | UUID      | -         | Sì       | No               | -       | FK → utenti.id                      | Consulente che ha creato l'azienda             |
| updated_at            | TIMESTAMP | -         | Sì       | No               | now()   | -                                   | Data ultima modifica                           |
| deleted_at            | TIMESTAMP | -         | No       | No               | null    | Soft delete                         | Data eliminazione                              |

**Relazioni**:

- **1 Azienda Cliente → 1 Azienda Consulenza** (N:1 via `azienda_consulenza_id`)
- **1 Azienda Cliente → N Sedi Aziendali** (1:N via `sedi_aziendali.azienda_cliente_id`)
- **1 Azienda Cliente → N Utenti Aziendali** (1:N via junction `utenti_aziendali`)
- **1 Azienda Cliente → N Audit** (1:N via `audit.azienda_cliente_id`)
- **M Aziende Clienti ← N Consulenti** (N:M via `consulenti_aziende_clienti`)

**Regole di business**:

- **Vincolo P.IVA/CF**: Almeno uno dei due deve essere compilato (OR required)
- **Almeno 1 sede obbligatoria**: Al momento della creazione, deve essere creata almeno 1 sede aziendale
- **Almeno 1 utente aziendale obbligatorio**: Al momento della creazione, deve essere creato almeno 1 utente aziendale
- **Vincolo eliminazione**: Bloccare eliminazione se esistono audit con stato "In Corso" o "In Bozza"
- **Multi-tenancy**: Consulente vede SOLO aziende clienti a cui è assegnato (filtro automatico su `consulenti_aziende_clienti`)

**Validazioni**:

- Partita IVA: 11 cifre numeriche (se compilata)
- Codice Fiscale: 16 caratteri alfanumerici uppercase (se compilato)
- Almeno uno tra P.IVA e CF obbligatorio

---

##### 5.1.3.5 Entità: Sede Aziendale

**Descrizione**: Sede fisica di un'azienda cliente (legale, operativa, filiale, etc.).

**Tabella database**: `sedi_aziendali`

**Campi**:

| Campo              | Tipo      | Lunghezza | Required | Unique | Default  | Vincoli                                                                | Descrizione                     |
| ------------------ | --------- | --------- | -------- | ------ | -------- | ---------------------------------------------------------------------- | ------------------------------- |
| id                 | UUID      | -         | Sì       | Sì     | auto     | PK                                                                     | Identificatore univoco          |
| azienda_cliente_id | UUID      | -         | Sì       | No     | -        | FK → aziende_clienti.id                                                | Azienda cliente di appartenenza |
| tipo_sede          | ENUM      | -         | Sì       | No     | -        | 'Sede Legale', 'Sede Operativa', 'Filiale', 'Magazzino', 'Centro Dati' | Tipo sede                       |
| indirizzo          | VARCHAR   | 255       | Sì       | No     | -        | Max 255 char                                                           | Via/piazza                      |
| civico             | VARCHAR   | 10        | Sì       | No     | -        | Max 10 char                                                            | Numero civico (es: 123/A)       |
| cap                | VARCHAR   | 10        | Sì       | No     | -        | 5 cifre se nazione=Italia                                              | Codice avviamento postale       |
| citta              | VARCHAR   | 100       | Sì       | No     | -        | Max 100 char                                                           | Città                           |
| provincia          | VARCHAR   | 2         | Sì       | No     | -        | 2 caratteri uppercase se nazione=Italia                                | Sigla provincia (es: MI, RM)    |
| nazione            | VARCHAR   | 100       | Sì       | No     | 'Italia' | -                                                                      | Nazione (default Italia)        |
| created_at         | TIMESTAMP | -         | Sì       | No     | now()    | -                                                                      | Data creazione                  |
| deleted_at         | TIMESTAMP | -         | No       | No     | null     | Soft delete                                                            | Data eliminazione               |

**Relazioni**:

- **N Sedi → 1 Azienda Cliente** (N:1 via `azienda_cliente_id`)
- **1 Sede → N Utenti Aziendali** (1:N via `utenti_aziendali.sede_id`)

**Regole di business**:

- **Almeno 1 sede obbligatoria**: Ogni azienda cliente deve avere almeno 1 sede (validazione in eliminazione)
- **Vincolo eliminazione**: Non è possibile eliminare l'ultima sede dell'azienda
- **Soft delete**: Eliminazione logica con `deleted_at`

**Validazioni**:

- CAP: 5 cifre numeriche se nazione=Italia (altrimenti free text)
- Provincia: 2 caratteri uppercase se nazione=Italia (altrimenti opzionale)
- Tipo sede: enum vincolato ai valori specificati

---

##### 5.1.3.6 Entità: Utente Aziendale

**Descrizione**: Referente dell'azienda cliente che accede alla piattaforma per consultare audit.

**Tabella database**: `utenti` (con `ruolo IN ('Admin Cliente', 'Cliente')`) + junction table `utenti_aziendali`

**Campi tabella `utenti`**:

| Campo          | Tipo      | Lunghezza | Required | Unique       | Default   | Vincoli                             | Descrizione                            |
| -------------- | --------- | --------- | -------- | ------------ | --------- | ----------------------------------- | -------------------------------------- |
| id             | UUID      | -         | Sì       | Sì           | auto      | PK                                  | Identificatore univoco                 |
| nome           | VARCHAR   | 100       | Sì       | No           | -         | Solo alfabetici, spazi              | Nome utente                            |
| cognome        | VARCHAR   | 100       | Sì       | No           | -         | Solo alfabetici, spazi              | Cognome utente                         |
| email          | VARCHAR   | 255       | Sì       | Sì (globale) | -         | Formato email valido, lowercase     | Email per login (univoca cross-tenant) |
| telefono       | VARCHAR   | 20        | No       | No           | null      | Formato internazionale              | Telefono utente                        |
| stato_invito   | ENUM      | -         | Sì       | No           | 'Pending' | 'Pending', 'Attivo', 'Disabilitato' | Stato invito                           |
| ultimo_accesso | TIMESTAMP | -         | No       | No           | null      | -                                   | Data ultimo login                      |
| created_at     | TIMESTAMP | -         | Sì       | No           | now()     | -                                   | Data creazione                         |
| deleted_at     | TIMESTAMP | -         | No       | No           | null      | Soft delete                         | Data eliminazione                      |

**Campi tabella junction `utenti_aziendali`** (link tra utente e azienda cliente):

| Campo                     | Tipo      | Lunghezza | Required | Unique | Vincoli                    | Descrizione                                             |
| ------------------------- | --------- | --------- | -------- | ------ | -------------------------- | ------------------------------------------------------- |
| id                        | UUID      | -         | Sì       | Sì     | PK                         | Identificatore univoco associazione                     |
| utente_id                 | UUID      | -         | Sì       | No     | FK → utenti.id             | Utente                                                  |
| azienda_cliente_id        | UUID      | -         | Sì       | No     | FK → aziende_clienti.id    | Azienda cliente                                         |
| sede_id                   | UUID      | -         | Sì       | No     | FK → sedi_aziendali.id     | Sede di assegnazione                                    |
| ruolo                     | ENUM      | -         | Sì       | No     | 'Admin Cliente', 'Cliente' | Ruolo specifico per questa azienda                      |
| flag_puo_creare_fornitori | BOOLEAN   | -         | Sì       | No     | false                      | Permesso creazione fornitori (read-only dopo creazione) |
| flag_puo_compilare_audit  | BOOLEAN   | -         | Sì       | No     | false                      | Permesso compilazione audit (read-only dopo creazione)  |
| created_at                | TIMESTAMP | -         | Sì       | No     | now()                      | Data associazione                                       |

**Unique constraint**: (`utente_id`, `azienda_cliente_id`) → un utente può essere associato a una azienda UNA sola volta

**Relazioni**:

- **1 Utente → M Aziende Clienti** (1:M via `utenti_aziendali`, account condiviso multi-consulente)
- **1 Associazione → 1 Sede** (N:1 via `sede_id`)

**Regole di business**:

- **Account condiviso multi-consulente**: Se un utente con email esistente viene creato per altra azienda cliente (consulente diverso), si aggiorna l'account esistente aggiungendo link ad azienda cliente (no creazione duplicato)
- **Ruolo indipendente per azienda**: Utente può essere Admin-Cliente in Azienda #1 e Cliente semplice in Azienda #2 (ruolo nella junction table)
- **Flag permessi read-only**: I flag `puo_creare_fornitori` e `puo_compilare_audit` sono modificabili SOLO in creazione, poi diventano read-only
- **Almeno 1 utente aziendale**: Ogni azienda cliente deve avere almeno 1 utente (validazione in eliminazione)
- **Vincolo eliminazione**: Eliminare associazione `utenti_aziendali` (non account utente se condiviso)
- **Soft delete account**: Se utente associato a 1 sola azienda → disabilita account; se associato a più aziende → mantiene account attivo

**Validazioni**:

- Email: univoca globalmente (cross-tenant)
- Email duplicata in creazione: gestione automatica account condiviso (no warning front-end per privacy)
- Sede: deve appartenere alla stessa azienda cliente

---

##### 5.1.3.7 Tabella Junction: Consulenti ↔ Aziende Clienti

**Descrizione**: Tabella many-to-many per gestire assegnazione consulenti ad aziende clienti (scenario multi-consulente).

**Tabella database**: `consulenti_aziende_clienti`

**Campi**:

| Campo              | Tipo      | Required | Unique | Vincoli                           | Descrizione                                     |
| ------------------ | --------- | -------- | ------ | --------------------------------- | ----------------------------------------------- |
| id                 | UUID      | Sì       | Sì     | PK                                | Identificatore univoco                          |
| consulente_id      | UUID      | Sì       | No     | FK → utenti.id (ruolo=Consulente) | Consulente assegnato                            |
| azienda_cliente_id | UUID      | Sì       | No     | FK → aziende_clienti.id           | Azienda cliente                                 |
| is_principale      | BOOLEAN   | Sì       | No     | Default false                     | True se consulente principale (primo assegnato) |
| created_at         | TIMESTAMP | Sì       | No     | -                                 | Data assegnazione                               |

**Unique constraint**: (`consulente_id`, `azienda_cliente_id`) → un consulente può essere assegnato a un'azienda UNA sola volta

**Relazioni**:

- **N Consulenti ↔ M Aziende Clienti** (many-to-many)

**Regole di business**:

- **Almeno 1 consulente assegnato**: Ogni azienda cliente deve avere almeno 1 consulente (validazione in rimozione)
- **Consulente principale**: Il primo consulente assegnato ha flag `is_principale = true`
- **Multi-tenancy**: Consulente vede azienda cliente in lista SOLO se presente in questa tabella (Admin-Consulente bypassa controllo)
- **Cambio consulente**: Possibile SOLO se non ci sono audit attivi (stato "In Corso" o "In Bozza")

---

##### 5.1.3.8 Diagramma ER Semplificato

```
┌─────────────────────┐
│  Admin Piattaforma  │
│ (tabella: utenti)   │
└─────────────────────┘
         │ created_by
         ▼
┌─────────────────────────────┐
│  Azienda di Consulenza      │
│  - id                       │
│  - nome_azienda             │
│  - p_iva (unique)           │
│  - codice_fiscale (unique)  │
│  - max_aziende_clienti      │
│  - max_utenti_aziende       │
└─────────────────────────────┘
         │ 1
         │
         │ azienda_consulenza_id
         ▼ N
┌─────────────────────┐              ┌──────────────────────────┐
│    Consulente       │◄──── N:M ────┤ consulenti_aziende_     │
│ (tabella: utenti)   │              │ clienti (junction)       │
│  - ruolo: Admin     │              └──────────────────────────┘
│    Consulente /     │                        │ N
│    Consulente       │                        │
└─────────────────────┘                        │ azienda_cliente_id
         │ created_by                          ▼ 1
         ▼                              ┌─────────────────────┐
┌─────────────────────────────┐        │  Azienda Cliente    │
│      Azienda Cliente         │        │  - id               │
│  - id                        │        │  - ragione_sociale  │
│  - ragione_sociale           │        │  - partita_iva      │
│  - partita_iva (unique)      │        │  - codice_fiscale   │
│  - codice_fiscale (unique)   │        └─────────────────────┘
│  - azienda_consulenza_id (FK)│                 │ 1
└─────────────────────────────┘                 │
         │ 1                                    │ azienda_cliente_id
         │                                      ▼ N
         │ azienda_cliente_id           ┌─────────────────────┐
         ▼ N                            │  Sede Aziendale     │
┌─────────────────────┐                 │  - id               │
│  Sede Aziendale     │                 │  - tipo_sede        │
│  - id               │                 │  - indirizzo        │
│  - tipo_sede        │                 │  - citta            │
│  - indirizzo        │                 └─────────────────────┘
│  - citta            │                          │ 1
└─────────────────────┘                          │ sede_id
         │ 1                                     ▼ N
         │ sede_id                    ┌──────────────────────────┐
         ▼ N                           │  utenti_aziendali        │
┌──────────────────────────┐           │  (junction)              │
│  utenti_aziendali        │           │  - utente_id (FK)        │
│  (junction)              │           │  - azienda_cliente_id    │
│  - utente_id (FK)        │           │  - sede_id (FK)          │
│  - azienda_cliente_id    │           │  - ruolo                 │
│  - sede_id (FK)          │           │  - flag_puo_creare_...   │
│  - ruolo                 │           └──────────────────────────┘
│  - flag_puo_creare_...   │                    │ N
└──────────────────────────┘                    │ utente_id
         │ N                                    ▼ 1
         │ utente_id                    ┌─────────────────────┐
         ▼ 1                            │  Utente Aziendale   │
┌─────────────────────┐                 │  (tabella: utenti)  │
│  Utente Aziendale   │                 │  - id               │
│  (tabella: utenti)  │                 │  - nome             │
│  - id               │                 │  - cognome          │
│  - nome             │                 │  - email (unique)   │
│  - cognome          │                 │  - stato_invito     │
│  - email (unique)   │                 └─────────────────────┘
│  - stato_invito     │
└─────────────────────┘
```

**Legenda relazioni**:

- **1:N**: Una entità padre ha molte entità figlie (es: 1 Azienda Cliente → N Sedi)
- **N:M**: Relazione many-to-many tramite junction table (es: N Consulenti ↔ M Aziende Clienti)
- **FK**: Foreign key che punta alla primary key di altra tabella

---

#### 5.1.4 User Stories e Acceptance Criteria

**Totale**: 24 user stories con acceptance criteria dettagliati, edge cases, field specifications e dipendenze.

#### 5.1.5 Ordine di Implementazione

L'ordine ottimale di implementazione è suddiviso in 4 sprint:

**Sprint 1: Foundation - Admin & Aziende Consulenza Base (Stories 1-7)**

- Durata stimata: 8-10 giorni
- Obiettivo: Creare fondamenta del sistema con gestione utenti Admin e CRUD base Aziende di Consulenza
- Stories: US-ANA-001 → US-ANA-007
- Complessità: Bassa-Media | Rischio: Basso

**Sprint 2: Multi-Tenancy Core - Aziende Clienti & Sedi (Stories 8-15)**

- Durata stimata: 12-14 giorni
- Obiettivo: Implementare gestione Aziende Clienti con segregazione multi-tenant, Sedi e Utenti Aziendali
- Stories: US-ANA-008 → US-ANA-015
- Complessità: Media-Alta | Rischio: Medio

**Sprint 3: Advanced Multi-Consulente & Context Switcher (Stories 16-21)**

- Durata stimata: 10-12 giorni
- Obiettivo: Abilitare scenari complessi multi-consulente, context switcher, gestione avanzata Aziende Consulenza
- Stories: US-ANA-016 → US-ANA-021
- Complessità: Alta | Rischio: Alto

**Sprint 4: Enhancement & Polish - Filtri, Ricerche, Gestione Utenti (Stories 22-24)**

- Durata stimata: 2-3 giorni
- Obiettivo: Completare funzionalità di gestione centralizzata utenti
- Stories: US-ANA-022 → US-ANA-024
- Complessità: Bassa-Media | Rischio: Basso

#### 5.1.6 Wireframe e Mockup

https://www.figma.com/design/w7tK8k6e58KlzmFgxIVpNu/UI-%7C-NIS2--Condiviso-?node-id=11532-768&t=qqtGoFYRItbZmhGl-1

#### 5.1.7 Dipendenze

**Dipendenze in ingresso** (epic che devono essere completate/parallele prima):

- **Epic E1 - Autenticazione** (parziale, parallelo):
  - Necessaria per login utenti e gestione sessioni
  - Creazione utenti può procedere in parallelo (epic Anagrafiche crea record utenti, epic Autenticazione gestisce login/MFA)
  - MFA obbligatorio configurato al primo accesso (implementato in epic Autenticazione)

**Dipendenze in uscita** (epic che dipendono da questa - bloccate fino al completamento):

- **Epic E3 - Framework Normativi**: Framework NIS2/CIS associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- **Epic E4 - Audit**: Audit creati per Aziende Clienti da Consulenti (richiede Aziende Clienti + Consulenti + Utenti Aziendali)
- **Epic E5 - Fornitori**: Fornitori associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- **Epic E6 - Azioni Correttive**: Azioni assegnate a Utenti Aziendali (richiede Utenti Aziendali esistenti)
- **Epic E7 - Reporting**: Report generati per Aziende Clienti con dati anagrafici (richiede tutte le anagrafiche)

#### 5.1.8 Priorità

**MUST-HAVE (Release blocker)** - Le anagrafiche sono la **fondazione del sistema**. Senza utenti e aziende configurati, nessun'altra funzionalità (audit, framework, fornitori, report) può essere utilizzata. Questa epic **blocca tutte le epic successive**. Multi-tenancy implementato qui è critico per segregazione dati rigorosa richiesta da GDPR e conformità.

---

### 5.2 Autenticazione (TBD)

_Sezione da completare con requisiti funzionali per autenticazione email+password, MFA obbligatorio, password reset, gestione sessioni._

---

### 5.3 Framework Normativi

#### 5.3.1 Obiettivo

Implementare la gestione completa dei framework normativi (NIS2, CIS Controls) con struttura gerarchica articolata e sistema di template riutilizzabili per Template Audit. La gestione include anagrafiche di requisiti e criteri di valutazione, creazione di framework template con righe strutturate (Ambito → Tematica → Categoria → Misura → Requisito), associazione di criteri di valutazione, e gestione stati con workflow di pubblicazione.

#### 5.3.2 Scope Funzionale

Questa sezione copre:

**Gestione Requisiti (Anagrafica)**:

- CRUD completo requisiti (Admin)
- Validazione univocita nome requisito
- Tracciamento utilizzo in framework
- Gestione eliminazione con warning se requisito utilizzato in framework esistenti
- Filtri e ricerca (nome, descrizione)

**Gestione Criteri di Valutazione (Anagrafica)**:

- CRUD completo criteri di valutazione (Admin)
- Due tipologie: Campo Libero (input testuale con max lunghezza configurabile) e Scala (valori numerici predefiniti con label)
- Gestione dinamica coppie Valore-Label per criteri tipo Scala (minimo 2 coppie)
- Tipo criterio NON modificabile dopo creazione
- Validazione univocita nome criterio e valori numerici nella scala
- Tracciamento utilizzo in framework
- Filtri e ricerca (nome, tipo)

**Gestione Template Framework**:

- CRUD completo framework template (Admin)
- Associazione criteri di valutazione a livello framework (multi-select)
- Gestione righe framework con 5 livelli gerarchici: Ambito, Tematica, Categoria, Misura, Requisito
- Campi Ambito/Tematica/Categoria/Misura con Freesolo Autocomplete (suggerimenti da valori esistenti + possibilita digitare nuovi)
- Campo Requisito con dropdown da anagrafica requisiti
- Gestione freesolo con eliminazione suggerimenti tramite icona X (con warning se utilizzati)
- Tabella anteprima righe con CRUD in-page (Aggiungi/Modifica/Elimina)
- Workflow stati: Bozza → Pubblicato → Archiviato
- Pubblicazione framework (da Bozza a Pubblicato) con validazione minimo 1 riga
- Archiviazione framework (da Pubblicato ad Archiviato) con blocco modifica
- Eliminazione con vincoli (hard delete per Bozza, blocco se utilizzato in Template Audit per Pubblicato, warning per Archiviato)

**Dashboard & KPI**:

- Contatori framework per stato (Bozza, Pubblicato, Archiviato)
- Contatori requisiti e criteri di valutazione disponibili

**Sistema**:

- Soft delete per requisiti e criteri di valutazione (preservazione audit trail)
- Hard delete per framework (con validazione vincoli utilizzo)
- Anagrafica suggerimenti per campi freesolo (Ambito, Tematica, Categoria, Misura)
- Cascade delete per coppie Scala al delete criterio
- Paginazione server-side su tutte le liste (10/25/50 rows per page per anagrafiche, 8/16/24 per framework template, 5 per tabella anteprima righe)

#### 5.3.3 Mapping Entita Framework

Di seguito la struttura dettagliata delle entita framework con campi, tipi di dato, relazioni e vincoli.

##### 5.3.3.1 Entita: Requisito

**Descrizione**: Elemento atomico valutabile in un audit (es: "Implementare autenticazione multi-fattore").

**Tabella database**: `requisiti`

**Campi**:

| Campo          | Tipo      | Lunghezza | Required | Unique | Default | Vincoli                 | Descrizione                        |
| -------------- | --------- | --------- | -------- | ------ | ------- | ----------------------- | ---------------------------------- |
| id             | UUID      | -         | Si       | Si     | auto    | PK                      | Identificatore univoco             |
| nome_requisito | VARCHAR   | 255       | Si       | Si     | -       | Max 255 char, univoco   | Nome requisito (identificativo)    |
| requisito      | TEXT      | 1000      | Si       | No     | -       | Max 1000 char           | Descrizione dettagliata requisito  |
| descrizione    | VARCHAR   | 255       | No       | No     | null    | Max 255 char            | Descrizione interna (uso admin)    |
| created_at     | TIMESTAMP | -         | Si       | No     | now()   | -                       | Data creazione                     |
| updated_at     | TIMESTAMP | -         | Si       | No     | now()   | -                       | Data ultima modifica               |
| deleted_at     | TIMESTAMP | -         | No       | No     | null    | Soft delete             | Data eliminazione (soft delete)    |

**Relazioni**:

- **1 Requisito → N Righe Framework** (1:N via `righe_framework.requisito_id`)

**Regole di business**:

- **Vincolo eliminazione**: Warning se requisito utilizzato in framework esistenti (non blocco hard)
- **Eliminazione con cascade**: Eliminando requisito, eliminare anche righe framework associate
- **Soft delete**: Eliminazione logica con flag `deleted_at`

**Validazioni**:

- Nome requisito: univoco, case-insensitive
- Requisito: max 1000 caratteri

---

##### 5.3.3.2 Entita: Criterio di Valutazione

**Descrizione**: Criterio utilizzato per valutare i requisiti negli audit. Puo essere Campo Libero (input testuale) o Scala (valori predefiniti).

**Tabella database**: `elementi_valutazione`

**Campi**:

| Campo         | Tipo      | Lunghezza | Required | Unique | Default | Vincoli                           | Descrizione                            |
| ------------- | --------- | --------- | -------- | ------ | ------- | --------------------------------- | -------------------------------------- |
| id            | UUID      | -         | Si       | Si     | auto    | PK                                | Identificatore univoco                 |
| nome_elemento | VARCHAR   | 255       | Si       | Si     | -       | Max 255 char, univoco             | Nome criterio                          |
| descrizione   | TEXT      | 1000      | No       | No     | null    | Max 1000 char                     | Descrizione estesa (uso interno)       |
| tipo_elemento | ENUM      | -         | Si       | No     | -       | 'Campo Libero', 'Scala'           | Tipo criterio (NON modificabile)       |
| max_lunghezza | INTEGER   | -         | No       | No     | null    | > 0 (solo se tipo=Campo Libero)   | Lunghezza massima campo libero         |
| created_at    | TIMESTAMP | -         | Si       | No     | now()   | -                                 | Data creazione                         |
| updated_at    | TIMESTAMP | -         | Si       | No     | now()   | -                                 | Data ultima modifica                   |
| deleted_at    | TIMESTAMP | -         | No       | No     | null    | Soft delete                       | Data eliminazione (soft delete)        |

**Relazioni**:

- **1 Criterio → N Coppie Scala** (1:N via `valori_scala.elemento_valutazione_id`, solo se tipo=Scala)
- **M Criteri ↔ N Framework** (M:N via tabella junction `framework_elementi_valutazione`)

**Regole di business**:

- **Tipo NON modificabile**: Una volta creato, il tipo (Campo Libero / Scala) non puo essere cambiato
- **Se tipo=Scala**: Minimo 2 coppie Valore-Label obbligatorie
- **Vincolo eliminazione**: Warning se criterio utilizzato in framework esistenti (non blocco hard)
- **Cascade delete**: Se tipo=Scala, eliminare tutte le coppie Valore-Label associate
- **Soft delete**: Eliminazione logica con flag `deleted_at`

**Validazioni**:

- Nome criterio: univoco, case-insensitive
- Tipo: enum fisso ('Campo Libero', 'Scala')
- max_lunghezza: integer > 0 (se tipo=Campo Libero)

---

##### 5.3.3.3 Entita: Coppie Scala (per Criteri tipo Scala)

**Descrizione**: Coppie Valore Numerico - Label associate a un criterio di valutazione tipo Scala.

**Tabella database**: `valori_scala`

**Campi**:

| Campo                    | Tipo      | Lunghezza | Required | Unique                           | Default | Vincoli                           | Descrizione                                  |
| ------------------------ | --------- | --------- | -------- | -------------------------------- | ------- | --------------------------------- | -------------------------------------------- |
| id                       | UUID      | -         | Si       | Si                               | auto    | PK                                | Identificatore univoco                       |
| elemento_valutazione_id  | UUID      | -         | Si       | No                               | -       | FK → elementi_valutazione.id      | Criterio di appartenenza                     |
| valore_numerico          | DECIMAL   | (10,2)    | Si       | Si (per elemento_valutazione_id) | -       | 2 decimali, univoco nella scala   | Valore numerico (es: 0.0, 0.5, 1.0)          |
| label_associata          | VARCHAR   | 100       | Si       | No                               | -       | Max 100 char                      | Label descrittiva (es: "Non conforme")       |
| created_at               | TIMESTAMP | -         | Si       | No                               | now()   | -                                 | Data creazione                               |

**Unique constraint**: (`elemento_valutazione_id`, `valore_numerico`) → un valore numerico univoco per ciascun criterio Scala

**Relazioni**:

- **N Coppie → 1 Criterio Scala** (N:1 via `elemento_valutazione_id`)

**Regole di business**:

- **Minimo 2 coppie**: Ogni criterio Scala deve avere almeno 2 coppie
- **Ordinamento**: Visualizzazione ordinata per valore numerico crescente
- **Cascade delete**: Eliminando criterio Scala, eliminare tutte le coppie associate

**Validazioni**:

- valore_numerico: decimal 2 decimali, univoco per criterio
- label_associata: max 100 caratteri

---

##### 5.3.3.4 Entita: Framework Template

**Descrizione**: Template di framework normativo (es: NIS2, CIS Controls v8) con stato e righe associate.

**Tabella database**: `framework_template`

**Campi**:

| Campo                   | Tipo      | Lunghezza | Required | Unique | Default | Vincoli                                  | Descrizione                                  |
| ----------------------- | --------- | --------- | -------- | ------ | ------- | ---------------------------------------- | -------------------------------------------- |
| id                      | UUID      | -         | Si       | Si     | auto    | PK                                       | Identificatore univoco                       |
| nome_framework          | VARCHAR   | 255       | Si       | Si     | -       | Max 255 char, univoco                    | Nome framework (es: NIS2, CIS v8)            |
| descrizione_framework   | TEXT      | 1000      | No       | No     | null    | Max 1000 char                            | Descrizione framework                        |
| stato_framework         | ENUM      | -         | Si       | No     | 'Bozza' | 'Bozza', 'Pubblicato', 'Archiviato'      | Stato framework                              |
| n_righe                 | INTEGER   | -         | Si       | No     | 0       | >= 0                                     | Contatore righe framework (denormalizzato)   |
| created_at              | TIMESTAMP | -         | Si       | No     | now()   | -                                        | Data creazione                               |
| created_by              | UUID      | -         | Si       | No     | -       | FK → utenti.id                           | Admin che ha creato il framework             |
| updated_at              | TIMESTAMP | -         | Si       | No     | now()   | -                                        | Data ultima modifica                         |
| pubblicato_il           | TIMESTAMP | -         | No       | No     | null    | -                                        | Data pubblicazione (se stato=Pubblicato)     |
| archiviato_il           | TIMESTAMP | -         | No       | No     | null    | -                                        | Data archiviazione (se stato=Archiviato)     |
| deleted_at              | TIMESTAMP | -         | No       | No     | null    | Hard delete (non soft delete)            | Data eliminazione (null = non eliminato)     |

**Relazioni**:

- **1 Framework → N Righe Framework** (1:N via `righe_framework.framework_template_id`)
- **M Framework ↔ N Criteri Valutazione** (M:N via `framework_elementi_valutazione`)

**Regole di business**:

- **Stato default**: Bozza alla creazione
- **Pubblicazione**: Richiede almeno 1 riga framework (n_righe >= 1)
- **Framework con 0 righe**: Consentito in stato Bozza, NON pubblicabile
- **Modifica**: Consentita in stato Bozza e Pubblicato, bloccata in stato Archiviato
- **Eliminazione Bozza**: Hard delete libero
- **Eliminazione Pubblicato**: Blocco hard se utilizzato in Template Audit, altrimenti solo archiviazione
- **Eliminazione Archiviato**: Hard delete con warning

**Validazioni**:

- Nome framework: univoco, case-insensitive
- Stato: enum fisso ('Bozza', 'Pubblicato', 'Archiviato')

---

##### 5.3.3.5 Entita: Riga Framework

**Descrizione**: Riga di un framework template con struttura gerarchica (Ambito → Tematica → Categoria → Misura → Requisito).

**Tabella database**: `righe_framework`

**Campi**:

| Campo                 | Tipo      | Lunghezza | Required | Unique | Default | Vincoli                         | Descrizione                        |
| --------------------- | --------- | --------- | -------- | ------ | ------- | ------------------------------- | ---------------------------------- |
| id                    | UUID      | -         | Si       | Si     | auto    | PK                              | Identificatore univoco             |
| framework_template_id | UUID      | -         | Si       | No     | -       | FK → framework_template.id      | Framework di appartenenza          |
| ambito                | VARCHAR   | 100       | Si       | No     | -       | Max 100 char, freesolo          | Ambito (1° livello gerarchia)      |
| tematica              | VARCHAR   | 100       | Si       | No     | -       | Max 100 char, freesolo          | Tematica (2° livello gerarchia)    |
| categoria             | VARCHAR   | 100       | Si       | No     | -       | Max 100 char, freesolo          | Categoria (3° livello gerarchia)   |
| misura                | VARCHAR   | 100       | Si       | No     | -       | Max 100 char, freesolo          | Misura (4° livello gerarchia)      |
| requisito_id          | UUID      | -         | Si       | No     | -       | FK → requisiti.id               | Requisito (5° livello gerarchia)   |
| created_at            | TIMESTAMP | -         | Si       | No     | now()   | -                               | Data creazione                     |

**Relazioni**:

- **N Righe → 1 Framework** (N:1 via `framework_template_id`)
- **N Righe → 1 Requisito** (N:1 via `requisito_id`)

**Regole di business**:

- **Tutti i campi obbligatori**: Tutti i 5 livelli gerarchici sono required
- **Freesolo**: Ambito, Tematica, Categoria, Misura sono campi freesolo (suggerimenti da valori esistenti + possibilita digitare nuovi)
- **Requisito**: Dropdown da anagrafica requisiti
- **NO validazione univocita**: Duplicate righe consentite (stesso Ambito-Tematica-Categoria-Misura-Requisito puo apparire piu volte)
- **Cascade delete**: Eliminando framework, eliminare tutte le righe associate

**Validazioni**:

- Tutti i campi required (no null)
- Ambito/Tematica/Categoria/Misura: max 100 caratteri
- Requisito: deve esistere in anagrafica requisiti

---

##### 5.3.3.6 Entita: Anagrafica Suggerimenti Freesolo

**Descrizione**: Anagrafica valori suggeriti per campi freesolo (Ambito, Tematica, Categoria, Misura).

**Tabella database**: `suggerimenti_freesolo`

**Campi**:

| Campo       | Tipo      | Lunghezza | Required | Unique | Default | Vincoli                                       | Descrizione                                |
| ----------- | --------- | --------- | -------- | ------ | ------- | --------------------------------------------- | ------------------------------------------ |
| id          | UUID      | -         | Si       | Si     | auto    | PK                                            | Identificatore univoco                     |
| campo       | ENUM      | -         | Si       | No     | -       | 'Ambito', 'Tematica', 'Categoria', 'Misura'   | Tipo campo freesolo                        |
| valore      | VARCHAR   | 100       | Si       | No     | -       | Max 100 char                                  | Valore suggerimento                        |
| created_at  | TIMESTAMP | -         | Si       | No     | now()   | -                                             | Data creazione                             |

**Unique constraint**: (`campo`, `valore`) → un valore univoco per tipo campo (case-insensitive)

**Relazioni**:

- Nessuna relazione diretta (anagrafica indipendente)

**Regole di business**:

- **Salvataggio automatico**: Nuovi valori digitati in campi freesolo vengono salvati al salvataggio framework
- **Eliminazione con icona X**: Admin puo eliminare suggerimenti dall'autocomplete
- **Warning se utilizzato**: Se suggerimento utilizzato in framework esistenti, mostrare dialog warning (non blocco)
- **Case-insensitive**: Validazione univocita case-insensitive

**Validazioni**:

- Campo: enum fisso ('Ambito', 'Tematica', 'Categoria', 'Misura')
- Valore: max 100 caratteri, univoco per tipo campo

---

##### 5.3.3.7 Tabella Junction: Framework ↔ Criteri di Valutazione

**Descrizione**: Tabella many-to-many per associare criteri di valutazione a framework template.

**Tabella database**: `framework_elementi_valutazione`

**Campi**:

| Campo                    | Tipo      | Required | Unique | Vincoli                       | Descrizione                            |
| ------------------------ | --------- | -------- | ------ | ----------------------------- | -------------------------------------- |
| id                       | UUID      | Si       | Si     | PK                            | Identificatore univoco                 |
| framework_template_id    | UUID      | Si       | No     | FK → framework_template.id    | Framework                              |
| elemento_valutazione_id  | UUID      | Si       | No     | FK → elementi_valutazione.id  | Criterio di valutazione                |
| created_at               | TIMESTAMP | Si       | No     | -                             | Data associazione                      |

**Unique constraint**: (`framework_template_id`, `elemento_valutazione_id`) → un criterio associato a un framework UNA sola volta

**Relazioni**:

- **M Framework ↔ N Criteri Valutazione** (many-to-many)

**Regole di business**:

- **Associazione opzionale**: Framework puo avere 0 o piu criteri associati
- **Eliminazione**: Eliminando framework o criterio, eliminare anche record junction

---

##### 5.3.3.8 Diagramma ER Semplificato

```
┌─────────────────────────────┐
│  Admin Piattaforma          │
│  (tabella: utenti)          │
└─────────────────────────────┘
         │ created_by
         ▼
┌─────────────────────────────┐
│  Framework Template         │
│  - id                       │
│  - nome_framework (unique)  │
│  - stato_framework          │
│  - n_righe                  │
└─────────────────────────────┘
         │ 1
         │
         │ framework_template_id
         ▼ N
┌─────────────────────────────┐              ┌──────────────────────────────┐
│  Riga Framework             │              │ framework_elementi_          │
│  - id                       │◄──── N:M ────│ valutazione (junction)       │
│  - ambito (freesolo)        │              └──────────────────────────────┘
│  - tematica (freesolo)      │                        │ N
│  - categoria (freesolo)     │                        │
│  - misura (freesolo)        │                        ▼ 1
│  - requisito_id (FK)        │              ┌─────────────────────────────┐
└─────────────────────────────┘              │  Criterio di Valutazione    │
         │ N                                 │  - id                       │
         │ requisito_id                      │  - nome_elemento (unique)   │
         ▼ 1                                 │  - tipo_elemento            │
┌─────────────────────────────┐              │  - max_lunghezza            │
│  Requisito                  │              └─────────────────────────────┘
│  - id                       │                        │ 1
│  - nome_requisito (unique)  │                        │ elemento_valutazione_id
│  - requisito                │                        ▼ N
│  - descrizione              │              ┌─────────────────────────────┐
└─────────────────────────────┘              │  Coppie Scala               │
                                             │  (solo se tipo=Scala)       │
┌─────────────────────────────┐              │  - id                       │
│  Anagrafica Suggerimenti    │              │  - valore_numerico (unique) │
│  (freesolo)                 │              │  - label_associata          │
│  - id                       │              └─────────────────────────────┘
│  - campo (enum)             │
│  - valore (unique per campo)│
└─────────────────────────────┘
```

**Legenda relazioni**:

- **1:N**: Una entita padre ha molte entita figlie (es: 1 Framework → N Righe)
- **N:M**: Relazione many-to-many tramite junction table (es: N Framework ↔ M Criteri)
- **FK**: Foreign key che punta alla primary key di altra tabella

---

#### 5.3.4 User Stories e Acceptance Criteria

**Totale**: 18 user stories suddivise in 3 macro-aree:

- **US-FWK-001 a US-FWK-005**: Gestione Requisiti (5 stories)
- **US-FWK-006 a US-FWK-010**: Gestione Criteri di Valutazione (5 stories)
- **US-FWK-011 a US-FWK-018**: Gestione Template Framework (8 stories)

Tutte le user stories includono acceptance criteria dettagliati, edge cases, field specifications e dipendenze. Consultare i documenti dettagliati:

- **Gestione Requisiti**: `deliveries/epica-framework/US-FWK-001-005-gestione-requisiti.md`
- **Gestione Criteri di Valutazione**: `deliveries/epica-framework/US-FWK-006-010-gestione-elementi-valutazione.md`
- **Gestione Template Framework**: `deliveries/epica-framework/US-FWK-011-018-gestione-framework.md`

#### 5.3.5 Ordine di Implementazione

L'ordine ottimale di implementazione e suddiviso in 3 sprint:

**Sprint 1: Anagrafiche Foundation - Requisiti e Criteri (Stories 1-10)**

- Durata stimata: 10-12 giorni
- Obiettivo: Creare anagrafiche di base (Requisiti e Criteri di Valutazione) con CRUD completo
- Stories: US-FWK-001 → US-FWK-010
- Complessita: Bassa-Media | Rischio: Basso

**Sprint 2: Framework Core - Creazione e Gestione Righe (Stories 11-14)**

- Durata stimata: 12-15 giorni
- Obiettivo: Implementare creazione framework con gestione righe, freesolo autocomplete, tabella anteprima
- Stories: US-FWK-011 → US-FWK-014
- Complessita: Alta | Rischio: Alto

**Sprint 3: Framework Advanced - Stati e Workflow (Stories 15-18)**

- Durata stimata: 8-10 giorni
- Obiettivo: Completare workflow stati (Bozza/Pubblicato/Archiviato), eliminazione con vincoli
- Stories: US-FWK-015 → US-FWK-018
- Complessita: Media-Alta | Rischio: Medio

#### 5.3.6 Wireframe e Mockup

https://www.figma.com/design/w7tK8k6e58KlzmFgxIVpNu/UI-%7C-NIS2--Condiviso-?node-id=11532-768&t=qqtGoFYRItbZmhGl-1

#### 5.3.7 Dipendenze

**Dipendenze in ingresso** (epic che devono essere completate/parallele prima):

- **Epic E2 - Anagrafiche** (completata):
  - Necessaria per gestione utenti Admin che creano framework
  - Admin Piattaforma e il ruolo che gestisce CRUD framework
  - `created_by` nelle tabelle framework punta a `utenti.id`

**Dipendenze in uscita** (epic che dipendono da questa - bloccate fino al completamento):

- **Epic E4 - Template Audit**: Template Audit utilizzano Framework Template come blueprint (richiede framework pubblicati)
- **Epic E5 - Audit**: Audit associati a Template Audit che referenziano framework (richiede framework pubblicati)
- **Epic E7 - Reporting**: Report includono dati framework e conformita calcolata (richiede framework completi)

#### 5.3.8 Priorita

**MUST-HAVE (Release blocker)** - I framework normativi sono la **spina dorsale della conformita**. Senza framework strutturati (NIS2, CIS), non e possibile creare Template Audit, eseguire valutazioni requisiti, calcolare compliance o generare report. Questa epic **blocca tutte le epic di audit e reporting**. La struttura gerarchica (Ambito → Tematica → Categoria → Misura → Requisito) replica fedelmente il DB Access esistente ed e critica per migrazione dati.

---

---

### 5.4 Audit e Compliance (TBD)

_Sezione da completare con requisiti funzionali per creazione audit, valutazione requisiti, calcolo compliance, tracciabilità storica._

---

### 5.5 Gestione Fornitori (TBD)

_Sezione da completare con requisiti funzionali per processo qualifica fornitori con link temporaneo (7gg validità), questionario, caricamento documenti._

---

### 5.6 Azioni Correttive (TBD)

_Sezione da completare con requisiti funzionali per piano azioni, scadenze, assegnazione utenti aziendali, notifiche automatiche._

---

### 5.7 Reporting (TBD)

_Sezione da completare con requisiti funzionali per generazione 4 report PDF standard (Report Audit, Compliance per Framework, Piano Azioni, Qualifica Fornitori)._

---

## 6. Requisiti Non Funzionali

### 6.1 Performance

| Requisito                              | Target                 | Misurazione                           |
| -------------------------------------- | ---------------------- | ------------------------------------- |
| Tempo caricamento pagina               | < 2 secondi            | Lighthouse Performance Score > 90     |
| Tempo caricamento liste (>1000 record) | < 2 secondi            | Test performance con dataset popolato |
| Tempo generazione report PDF           | < 5 secondi            | Analytics tempo medio generazione     |
| Paginazione server-side                | 10/25/50 rows per page | Implementato su tutte le liste        |
| Debounce filtri testuali               | 300ms                  | Ottimizzazione query database         |

### 6.2 Scalabilità

| Requisito                                   | Target                      |
| ------------------------------------------- | --------------------------- |
| Numero aziende di consulenza                | > 100                       |
| Numero consulenti per azienda               | > 50                        |
| Numero aziende clienti per consulente       | > 100                       |
| Numero utenti aziendali per azienda cliente | > 50                        |
| Numero audit per azienda cliente            | > 500 (storico pluriennale) |
| Concurrent users                            | > 500 utenti simultanei     |

### 6.3 Sicurezza

| Requisito           | Implementazione                                              |
| ------------------- | ------------------------------------------------------------ |
| Autenticazione      | Email+password con hash bcrypt                               |
| MFA obbligatorio    | TOTP (Google Authenticator) per tutti i ruoli                |
| Segregazione dati   | Multi-tenancy logico con filtri automatici tenant            |
| Password temporanea | 12 caratteri alfanumerici, validità 7 giorni                 |
| Soft delete         | Flag`deleted_at` per preservazione audit trail               |
| SQL Injection       | Prepared statements, input sanitization                      |
| XSS                 | Output encoding, Content Security Policy                     |
| CSRF                | Token CSRF su tutte le form POST/PUT/DELETE                  |
| Rate limiting       | Max 5 tentativi login falliti in 15min → blocco 30min        |
| Audit trail         | Log immutabile di TUTTE le operazioni CRUD su utenti/aziende |

### 6.4 Disponibilità

| Requisito         | Target                                                   |
| ----------------- | -------------------------------------------------------- |
| Uptime            | > 99.5% (max 3.6 ore downtime/mese)                      |
| Backup            | Backup automatico database ogni 24h, retention 30 giorni |
| Disaster Recovery | RTO < 4 ore, RPO < 1 ora                                 |
| Monitoraggio      | AWS CloudWatch con alert automatici su errori critici    |

### 6.5 Usabilità

| Requisito           | Target                                                                      |
| ------------------- | --------------------------------------------------------------------------- |
| Responsive design   | Supporto desktop (Chrome, Firefox, Edge), tablet (iPad), mobile (view-only) |
| Accessibilità       | WCAG 2.1 Level A (minimum)                                                  |
| Browser supportati  | Chrome >= 90, Firefox >= 88, Edge >= 90, Safari >= 14                       |
| Tempo apprendimento | < 1 ora per consulente esperto (con demo guidata)                           |
| Lingua              | Solo italiano in MVP                                                        |

### 6.6 Manutenibilità

| Requisito          | Implementazione                                                     |
| ------------------ | ------------------------------------------------------------------- |
| Code coverage      | > 80% per backend, > 70% per frontend                               |
| Documentazione API | OpenAPI/Swagger con esempi                                          |
| Logging            | Structured logging (JSON) con livelli (DEBUG, INFO, WARNING, ERROR) |
| Error handling     | Messaggi errore user-friendly, codici errore standardizzati         |
| Versionamento      | Semantic versioning (major.minor.patch)                             |

---

## 7. Vincoli

### 7.1 Vincoli Tecnici

**Obbligatori (non negoziabili)**:

- **Database relazionale**: PostgreSQL (no NoSQL, no MongoDB)
- **Hosting**: AWS obbligatorio (EC2, RDS, S3)
- **Multi-tenancy logico**: Tabelle relazionali con FK `azienda_consulenza_id` (no database separati per tenant)
- **Generazione PDF**: Lato client con libreria jsPDF (no server-side rendering)
- **Email**: SMTP configurato (AWS SES consigliato)
- **Gestione documentale**: S3 con versioning abilitato (storico file audit)
- **Link temporanei fornitori**: Token univoco, validità 7 giorni, no autenticazione

**Raccomandati**:

- Framework frontend: React o Vue.js
- Framework backend: Nest o Node.js (Express) o Python (FastAPI)

### 7.2 Vincoli di Business

**Priorità MVP**:

- **MUST-HAVE**: Anagrafiche, Autenticazione, Framework NIS2/CIS, Audit base, Fornitori, 4 report PDF
- **SHOULD-HAVE**: Dashboard KPI, Filtri avanzati, Export CSV
- **NICE-TO-HAVE**: Analytics avanzati, Context switcher multi-azienda

**Esclusioni esplicite**:

- No integrazione OverRisk (versioni future)
- No SSO/SAML (solo email+password in MVP)
- No multi-lingua (solo italiano)
- No mobile app nativa (responsive web solo)
- No analytics ML/predittivi

---

## 8. Appendici

### 8.1 Glossario

| Termine                   | Definizione                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Admin Piattaforma**     | Amministratore con accesso completo alla piattaforma, gestisce aziende di consulenza e aziende clienti      |
| **Admin-Consulente**      | Consulente con ruolo admin in un'Azienda di Consulenza, gestisce consulenti e vede tutte le aziende clienti |
| **Consulente**            | Professionista che gestisce audit per aziende clienti assegnate                                             |
| **Azienda di Consulenza** | Studio o società di consulenza che gestisce audit per aziende clienti                                       |
| **Azienda Cliente**       | Azienda che viene auditata dai consulenti                                                                   |
| **Utente Aziendale**      | Referente aziendale che consulta stato conformità (Admin Cliente o Cliente semplice)                        |
| **Multi-tenancy**         | Segregazione dati per consulente/azienda consulenza (Consulente A non vede dati Consulente B)               |
| **Context Switcher**      | UI per Admin Cliente/Cliente semplice multi-azienda per switchare tra contesti aziende                      |
| **Soft Delete**           | Eliminazione logica con flag`deleted_at` (preservazione audit trail, no delete fisico)                      |
| **Link Temporaneo**       | Token univoco con validità 7 giorni per accesso fornitori (no login/password)                               |
| **Audit di Conformità**   | Valutazione strutturata conformità aziendale a framework NIS2/CIS                                           |
| **Framework Normativo**   | Struttura gerarchica Ambito → Tematica → Categoria → Requisito (NIS2, CIS Controls)                         |
| **Requisito**             | Elemento atomico valutabile in un audit (es: "Implementare autenticazione multi-fattore")                   |
| **Azione Correttiva**     | Intervento da implementare per risolvere non conformità rilevata in audit                                   |
| **Report PDF**            | Documento generato automaticamente (lato client) con template statico e dati dinamici                       |

### 8.2 Acronimi

| Acronimo  | Significato                                                           |
| --------- | --------------------------------------------------------------------- |
| **NIS2**  | Network and Information Security Directive 2 (Direttiva UE 2022/2555) |
| **CIS**   | Center for Internet Security                                          |
| **GDPR**  | General Data Protection Regulation (Regolamento UE 2016/679)          |
| **MFA**   | Multi-Factor Authentication                                           |
| **CRUD**  | Create, Read, Update, Delete                                          |
| **SaaS**  | Software as a Service                                                 |
| **MVP**   | Minimum Viable Product                                                |
| **KPI**   | Key Performance Indicator                                             |
| **UI/UX** | User Interface / User Experience                                      |
| **API**   | Application Programming Interface                                     |
| **JWT**   | JSON Web Token                                                        |
| **SMTP**  | Simple Mail Transfer Protocol                                         |
| **AWS**   | Amazon Web Services                                                   |
| **RTO**   | Recovery Time Objective                                               |
| **RPO**   | Recovery Point Objective                                              |
| **NPS**   | Net Promoter Score                                                    |

### 8.3 Riferimenti

**Normative di riferimento**:

- Direttiva NIS2: [EUR-Lex 32022L2555](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32022L2555)
- CIS Controls v8: [CIS Official Website](https://www.cisecurity.org/controls/v8)
- GDPR: [EUR-Lex 32016R0679](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32016R0679)

**Standard tecnici**:

- WCAG 2.1: [W3C Web Accessibility](https://www.w3.org/WAI/WCAG21/quickref/)
- OpenAPI 3.0: [OpenAPI Specification](https://swagger.io/specification/)
- Semantic Versioning: [SemVer 2.0](https://semver.org/)

### 8.4 Storia delle Revisioni

| Versione | Data       | Autore           | Modifiche                                                                                                                                                                          |
| -------- | ---------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1      | 2025-12-15 | Delivery Manager | Integrazione sezione 5.3 Framework Normativi completa: mapping entità (Requisiti, Criteri di Valutazione, Framework Template, Righe, Suggerimenti Freesolo), 18 user stories, workflow stati |
| 1.0      | 2025-12-12 | Delivery Manager | Creazione PRD iniziale con sezione Anagrafiche completa (mapping entità, relazioni, vincoli). Altre sezioni TBD.                                                                   |

---

**Fine del Documento PRD v1.1**

**Status**: Draft - Sezioni Anagrafiche (5.1) e Framework Normativi (5.3) complete, altre sezioni da integrare nelle prossime iterazioni.

**Prossimi step**:

1. Review e approvazione sezioni Anagrafiche e Framework Normativi da stakeholder
2. Integrazione sezione Autenticazione (epic E1)
3. Integrazione sezione Template Audit (epic E4)
4. Integrazione sezione Audit (epic E5)
5. Integrazione sezione Fornitori, Azioni, Reporting (epic E6, E7, E8)
6. Creazione matrice tracciabilità completa
7. Finalizzazione e approvazione PRD completo
