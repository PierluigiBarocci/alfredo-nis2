# Guida Strutturale - Organizzazione Backlog e Documentazione

**Progetto**: Piattaforma Conformità NIS2/CIS
**Versione**: 1.0
**Data**: 2025-11-24
**Scopo**: Definire la struttura organizzativa di Epic, Feature, User Stories, PRD e Jira per il progetto MVP

---

## 1. Panoramica

Questo documento definisce l'**impalcatura organizzativa** del progetto, stabilendo come strutturare il backlog, scrivere le user stories, organizzare il PRD e configurare Jira. NON contiene il contenuto effettivo delle stories o del PRD, ma descrive **come** organizziamo il lavoro.

### Principi Guida

1. **Epic = Aree Funzionali** (non ruoli): Le Epic rappresentano domini funzionali del sistema, non chi li usa
2. **Functionality-First**: Le funzionalità condivise Admin-Consulente vanno organizzate per area funzionale
3. **RBAC in Acceptance Criteria**: Le differenze di permessi tra ruoli sono gestite nei criteri di accettazione
4. **Single Source of Truth**: Una story per funzionalità, con varianti di ruolo documentate inline

---

## 2. Struttura Epic

Il backlog MVP è organizzato in **5 Epic funzionali**:

### E1: Flussi Autenticazione e Profilo
**Scope**: Tutto ciò che riguarda accesso, sicurezza, gestione profilo utente
**Include**:
- Login/Logout/MFA
- Recupero password
- Gestione profilo personale
- Dashboard iniziali (segmentate per ruolo)

**Ruoli coinvolti**: Admin, Consulente, Azienda, Fornitore
**Caratteristica**: Epic trasversale - ogni ruolo ha flussi specifici

---

### E2: Gestione Anagrafiche
**Scope**: CRUD di entità core (Aziende, Utenti, Fornitori base)
**Include**:
- Gestione Aziende Cliente (CRUD)
- Gestione Utenti (CRUD con assegnazione ruoli)
- Gestione Fornitori (anagrafica base, no questionari)
- Gestione Inventario Asset

**Ruoli coinvolti**: Admin, Consulente
**Caratteristica**: Funzionalità amministrative/di configurazione

**Nota**: I fornitori come *soggetti anagrafici* stanno qui. I fornitori come *processo di qualifica* stanno in E5.

---

### E3: Gestione Framework Normativi
**Scope**: Configurazione e gestione della struttura gerarchica dei framework
**Include**:
- CRUD Framework (NIS2, CIS, custom)
- Gestione gerarchia: Ambito → Tematica → Categoria/Misura → Requisito
- Import/export strutture framework

**Ruoli coinvolti**: Admin
**Caratteristica**: Configurazione avanzata, fondazione per gli audit

---

### E4: Gestione Audit
**Scope**: Creazione, esecuzione, valutazione e reportistica audit
**Include**:
- Creazione audit (testata + requisiti da framework)
- Compilazione e valutazione
- Gestione azioni correttive
- Generazione report PDF (Report Audit, Compliance, Piano Azioni)

**Ruoli coinvolti**: Admin, Consulente (operazioni), Azienda (visualizzazione)
**Caratteristica**: Core business della piattaforma

---

### E5: Gestione Fornitori (Processo Qualifica)
**Scope**: Workflow completo di qualifica fornitori con questionari e link temporanei
**Include**:
- Creazione questionari di qualifica
- Generazione link temporanei (7gg validità)
- Compilazione da parte fornitore (accesso guest)
- Valutazione risposte e reportistica

**Ruoli coinvolti**: Admin, Consulente (creazione), Fornitore (compilazione guest)
**Caratteristica**: Workflow separato con logica di accesso temporaneo

**Perché Epic separata**: Logica di business unica (link temporanei, accesso guest, workflow non-CRUD)

---

## 3. Approccio Organizzativo

### 3.1 Features sotto Epic

Ogni Epic contiene **Features** che raggruppano user stories correlate:

**Esempio (E2 - Anagrafiche)**:
- Feature: Gestione Aziende Cliente
  - Story: CRUD Aziende (Admin-Consulente)
  - Story: Visualizzazione Azienda (Consulente-Azienda)
- Feature: Gestione Utenti
  - Story: CRUD Utenti (Admin)
  - Story: Assegnazione Ruoli (Admin)

### 3.2 Funzionalità Condivise

**Principio**: Funzionalità condivise Admin-Consulente = **1 story** con RBAC in acceptance criteria

**NON fare**:
- ❌ Story separata "Admin: Crea Azienda"
- ❌ Story separata "Consulente: Crea Azienda"

**Fare**:
- ✅ Story unica "Gestione Aziende Cliente (CRUD)" con sezione "Differenze per Ruolo" nei criteri

**Quando splittare**:
- UI/flusso completamente diversi tra ruoli
- Logica di business radicalmente diversa
- Necessità di deploy separato

### 3.3 Gestione RBAC

Le differenze di permessi/visibilità vanno nei **Criteri di Accettazione**:

```markdown
## Criteri di Accettazione

### AC-01: Creazione Azienda
DATO che sono loggato come [Admin/Consulente]
QUANDO clicco su "Nuova Azienda"
ALLORA si apre il form di creazione

**Differenze per Ruolo**:
- Admin: Vede tutte le aziende di tutti i clienti
- Consulente: Vede solo le aziende dei propri clienti assegnati
```

---

## 4. Struttura PRD

Il Product Requirements Document segue **11 sezioni standardizzate**:

### Indice PRD

1. **Panoramica Prodotto**
   - Obiettivi, scope MVP, out-of-scope

2. **Utenti e Ruoli**
   - 4 ruoli (Admin, Consulente, Azienda, Fornitore)
   - Matrice permessi generale

3. **Requisiti Funzionali**
   - **Organizzati per Epic** (5 sezioni: E1, E2, E3, E4, E5)
   - Ogni Epic con Features e funzionalità dettagliate
   - Business Rules referenziate

4. **Modello Dati (High-Level)**
   - Entità principali e relazioni
   - NO schema DB tecnico (gestito da architects)

5. **Specifiche UI/UX**
   - Navigazione principale
   - Layout pattern
   - Riferimenti a wireframe

6. **Regole di Business**
   - ID formato `BR-[EPIC]-[nnn]`
   - Es: `BR-AUD-001`, `BR-FOR-012`
   - Elencate per Epic con descrizione

7. **Integrazioni**
   - Email (SMTP)
   - Storage (AWS S3)
   - NO integrazioni esterne in MVP

8. **Requisiti Non-Funzionali**
   - Performance, sicurezza, scalabilità
   - Multi-tenancy, MFA obbligatorio

9. **Piano di Rilascio**
   - Priorità features
   - MVP vs future enhancements

10. **Rischi e Dipendenze**
    - Blocchi tecnici
    - Dipendenze tra Epic/Features

11. **Appendice**
    - Glossario
    - Riferimenti normativi (NIS2, CIS)

### Business Rules - Sistema di ID

**Formato**: `BR-[EPIC_CODE]-[nnn]`

**Epic Codes**:
- `AUTH` = E1 (Autenticazione)
- `ANA` = E2 (Anagrafiche)
- `FWK` = E3 (Framework)
- `AUD` = E4 (Audit)
- `FOR` = E5 (Fornitori)

**Esempio**:
```
BR-FOR-001: I link temporanei hanno validità di 7 giorni dalla generazione
BR-AUD-005: Il calcolo della percentuale di compliance è eseguito backend-only
BR-ANA-003: Un fornitore può essere assegnato a più aziende cliente
```

### Traceability

**Matrice di tracciabilità** in Appendice:

| Requisito Vincolo | Sezione PRD | User Story ID | Stato |
|-------------------|-------------|---------------|-------|
| Multi-tenant logico | 8.2 | AUTH-001, ANA-002 | Draft |
| Link temporanei 7gg | 3.5, 6 (BR-FOR-001) | FOR-003 | Draft |

---

## 5. Scrittura User Stories

### 5.1 Convenzione Naming

**Formato**: `[EPIC_CODE]-[nnn]: [Titolo Funzionale]`

**Esempi**:
- `AUTH-001: Login con Email e Password`
- `ANA-005: CRUD Aziende Cliente`
- `AUD-012: Generazione Report Audit PDF`
- `FOR-003: Generazione Link Temporaneo Fornitore`

### 5.2 Template Story

```markdown
# [EPIC_CODE]-[nnn]: [Titolo]

## Descrizione
Come [ruolo/i coinvolti]
Voglio [azione]
In modo che [beneficio business]

## Criteri di Accettazione

### AC-01: [Nome Criterio]
DATO che [precondizione]
QUANDO [azione utente]
ALLORA [risultato atteso]

**Differenze per Ruolo** (se applicabile):
- Admin: [comportamento specifico]
- Consulente: [comportamento specifico]

### AC-02: [Validazioni]
- Campo X: obbligatorio, max 100 caratteri
- Campo Y: formato email valido

### AC-03: [Regole di Business]
- Riferimento: BR-XXX-nnn
- Comportamento: [descrizione]

## Edge Cases
- Scenario: [descrizione errore]
- Comportamento: [gestione errore]

## Dipendenze
- Richiede: [Story ID prerequisita]
- Blocca: [Story ID dipendente]

## Note Tecniche (opzionale)
[Hint implementativi se necessari]
```

### 5.3 Quando Splittare vs Merge

**Merge in 1 story** quando:
- Stessa UI, stessa logica, solo permessi diversi
- CRUD standard condiviso tra Admin-Consulente
- Differenze minime esprimibili in AC

**Split in N stories** quando:
- UI completamente diverse
- Workflow diversi (es: Fornitore guest vs Admin backoffice)
- Deploy indipendenti necessari
- Team diversi lavorano in parallelo

---

## 6. Organizzazione Jira

### 6.1 Gerarchia

```
Epic (5 totali)
  └─ Feature (raggruppamenti funzionali)
       └─ User Story (task implementativi)
            └─ Sub-task (opzionale, per breakdown tecnico)
```

### 6.2 Epic in Jira

| Epic ID | Nome | Epic Link |
|---------|------|-----------|
| E1 | Flussi Autenticazione e Profilo | `epic-auth` |
| E2 | Gestione Anagrafiche | `epic-anagrafiche` |
| E3 | Gestione Framework Normativi | `epic-framework` |
| E4 | Gestione Audit | `epic-audit` |
| E5 | Gestione Fornitori (Processo Qualifica) | `epic-fornitori` |

### 6.3 Components

Usare **Components** per indicare **chi usa** la funzionalità (non dove sta):

- `Admin` - Funzionalità amministrative
- `Aziende Consulenza` - Funzionalità consulenti
- `Aziende Clienti` - Funzionalità viewer clienti
- `Fornitori` - Funzionalità guest fornitori
- `Shared` - Funzionalità multi-ruolo

**Esempio**: Story "CRUD Aziende" ha Components: `[Admin, Aziende Consulenza, Shared]`

### 6.4 Labels

Usare **Labels** per metadati cross-cutting:

**Role-based**:
- `role:admin`
- `role:consulente`
- `role:azienda`
- `role:fornitore`
- `shared:admin-consulente`

**Technical**:
- `multi-tenant`
- `rbac`
- `pdf-generation`
- `email-notification`
- `temp-link`

**Priority**:
- `mvp-critical`
- `mvp-should-have`
- `post-mvp`

**Esempio**: Story "Generazione Link Temporaneo" ha:
- Epic: `E5`
- Components: `[Admin, Aziende Consulenza, Fornitori]`
- Labels: `[role:admin, role:consulente, role:fornitore, temp-link, email-notification, mvp-critical]`

### 6.5 Story Naming in Jira

**Summary (titolo)**: `[EPIC_CODE]-[nnn]: [Titolo Funzionale]`
**Issue Key**: Generato automaticamente (es: `PLAT-123`)

Nel backlog apparirà:
```
PLAT-123: ANA-005: CRUD Aziende Cliente
```

---

## 7. Decisioni Chiave

### 7.1 Perché Fornitori è Epic Separata?

**Motivazione**:
- Logica di business unica (link temporanei, token univoci, scadenza 7gg)
- Workflow non-CRUD (generazione → email → compilazione guest → valutazione)
- Accesso guest senza autenticazione permanente
- Reportistica specifica (Qualifica Fornitori PDF)

**NON** è un'anagrafica CRUD standard come Aziende/Utenti.

### 7.2 Perché Non Epic per Ruolo?

**Alternativa scartata**:
- Epic "Admin Features"
- Epic "Consulente Features"
- Epic "Cliente Features"

**Problema**:
- Funzionalità condivise (es: CRUD Aziende) andrebbero duplicate
- Navigazione backlog per "cosa fa il sistema" (non "chi lo usa")
- Team organizzati per dominio funzionale, non per ruolo

**Soluzione adottata**:
- Epic = domini funzionali
- Components + Labels = identificano i ruoli

### 7.3 Perché Shared Functionality in Epic Funzionali?

**Esempio**: "CRUD Aziende" usato da Admin e Consulente

**Dove va?**
→ Epic E2 (Anagrafiche) perché è *gestione anagrafica*

**NON**:
- ❌ Epic separata "Shared Features"
- ❌ Duplicata in "Admin Epic" + "Consulente Epic"

**Rationale**:
- Organizzazione per **dominio**, non per utente
- Single source of truth
- RBAC gestito in AC, non in struttura backlog

### 7.4 Livello di Dettaglio: PRD vs Jira Stories

**PRD (Product Requirements Document)**:
- **Cosa**: Requisiti funzionali completi
- **Livello**: Alto livello, orientato al business
- **Dettaglio**: Business rules, entità dati, flow generali
- **Audience**: Stakeholder, Product Team, Client

**Jira Stories**:
- **Cosa**: Task implementativi
- **Livello**: Dettaglio operativo, orientato allo sviluppo
- **Dettaglio**: Acceptance criteria step-by-step, edge cases, field specs
- **Audience**: Dev Team, QA, Scrum Master

**Relazione**:
- 1 sezione PRD (es: "3.2 Gestione Anagrafiche") → N Jira Stories (ANA-001, ANA-002, ANA-003...)
- PRD = "Cosa serve e perché"
- Stories = "Come implementare e verificare"

---

## 8. Workflow di Lavoro

### Step 1: Analisi Vincoli
- Leggere documento vincoli cliente
- Identificare requisiti funzionali, non-funzionali, constraint tecnici
- Fare domande di chiarimento

### Step 2: Strutturare PRD
- Seguire template 11 sezioni
- Sezione 3 (Requisiti Funzionali) = struttura per 5 Epic
- Definire Business Rules con ID
- Creare matrice di tracciabilità

### Step 3: Scrivere User Stories
- Per ogni Feature in PRD, creare N stories in Jira
- Seguire naming convention `[EPIC_CODE]-[nnn]`
- Template completo con AC, edge cases, dipendenze
- Assegnare Epic, Components, Labels

### Step 4: Organizzare Backlog
- Raggruppare per Epic
- Prioritizzare: MVP-critical → Should-have → Post-MVP
- Mappare dipendenze tra stories
- Validare copertura completa dei vincoli

### Step 5: Validazione
- Ogni vincolo cliente → almeno 1 story
- Ogni story → tracciabile a sezione PRD
- Nessuna ambiguità nei criteri di accettazione
- Nessuna sovrapposizione tra stories

---

## 9. Esempi Pratici

### Esempio 1: Funzionalità Condivisa

**Requisito**: Admin e Consulente possono creare/modificare Aziende Cliente

**Approccio**:
- Epic: E2 (Anagrafiche)
- Feature: Gestione Aziende Cliente
- Story: `ANA-005: CRUD Aziende Cliente`
- Components: `[Admin, Aziende Consulenza, Shared]`
- Labels: `[role:admin, role:consulente, shared:admin-consulente, multi-tenant, mvp-critical]`

**AC con RBAC**:
```markdown
### AC-02: Visualizzazione Lista Aziende
DATO che sono loggato come [Admin/Consulente]
QUANDO accedo alla sezione "Aziende"
ALLORA vedo la lista delle aziende

**Differenze per Ruolo**:
- Admin: Vede TUTTE le aziende di TUTTI i clienti
- Consulente: Vede SOLO le aziende dei clienti a cui è assegnato
```

---

### Esempio 2: Funzionalità Ruolo-Specifica

**Requisito**: Solo Admin può creare/modificare Framework

**Approccio**:
- Epic: E3 (Framework)
- Feature: Configurazione Framework
- Story: `FWK-001: CRUD Framework Normativi`
- Components: `[Admin]`
- Labels: `[role:admin, mvp-critical]`

**Nessuna sezione "Differenze per Ruolo"** perché solo Admin ha accesso.

---

### Esempio 3: Workflow Multi-Ruolo

**Requisito**: Processo qualifica fornitori (Admin/Consulente creano, Fornitore compila, Admin/Consulente valutano)

**Approccio**:
- Epic: E5 (Fornitori)
- Feature: Qualifica Fornitori
- Stories:
  - `FOR-001: Creazione Questionario Qualifica` (Admin/Consulente)
  - `FOR-002: Generazione Link Temporaneo` (Admin/Consulente)
  - `FOR-003: Compilazione Questionario da Fornitore` (Fornitore guest)
  - `FOR-004: Valutazione Risposte Fornitore` (Admin/Consulente)
  - `FOR-005: Generazione Report Qualifica PDF` (Admin/Consulente)

**Rationale**: Workflow complesso → split in stories per fase, non per ruolo

---

## 10. Checklist Validazione

### PRD Completato
- [ ] Tutte le 11 sezioni compilate
- [ ] Sezione 3 strutturata per 5 Epic
- [ ] Business Rules con ID univoci
- [ ] Matrice di tracciabilità vincoli → PRD
- [ ] Glossario termini tecnici

### Backlog Jira Completo
- [ ] 5 Epic create con descrizioni
- [ ] Features raggruppate sotto Epic corrette
- [ ] Tutte le stories con ID format `[EPIC_CODE]-[nnn]`
- [ ] Components assegnati correttamente
- [ ] Labels multi-dimensionali applicati
- [ ] Dipendenze mappate tra stories
- [ ] Priorità MVP assegnate

### User Stories Complete
- [ ] Template standard seguito
- [ ] Criteri di Accettazione step-by-step
- [ ] Sezione "Differenze per Ruolo" dove necessaria
- [ ] Edge cases documentati
- [ ] Business Rules referenziate
- [ ] Dipendenze identificate

### Traceability
- [ ] Ogni vincolo cliente → almeno 1 story
- [ ] Ogni story → sezione PRD identificata
- [ ] Nessuna sovrapposizione funzionale
- [ ] Nessuna ambiguità in AC

---

## 11. Riferimenti

### Documenti di Progetto
- **Vincoli Cliente**: `./research/documento_vincolo_di_progetto_piattaforma_conformità_ni2.md`
- **CLAUDE.md**: `./CLAUDE.md` (context file generale)
- **Database Legacy**: `./research/old_piattaforma_conformità_nis2.accdb`

### Template
- **Template PRD**: Da creare seguendo struttura sezione 4
- **Template User Story**: Sezione 5.2 di questo documento

### Tools
- **Jira**: Per gestione backlog e sprint
- **Confluence/Docs**: Per hosting PRD finale
- **Access Reader**: `./research/read_access.py` per analisi DB legacy

---

## Changelog

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | 2025-11-24 | Delivery Manager | Creazione iniziale - struttura organizzativa completa |

---

**Fine del Documento**

_Questo documento è un blueprint organizzativo. Il contenuto effettivo (PRD compilato, user stories dettagliate) verrà sviluppato seguendo questa struttura._
