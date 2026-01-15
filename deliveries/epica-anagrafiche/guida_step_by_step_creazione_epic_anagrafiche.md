# Guida Step-by-Step: Creazione Epic Anagrafiche in Jira

**Versione**: 2.0
**Data**: 2025-12-11
**Caso d'uso**: Creazione Epic "Gestione Anagrafiche" - Piattaforma Conformità NIS2/CIS
**Progetto**: alfredo-nis2

---

## Introduzione

Questa guida ti accompagna nella creazione dell'Epic "Gestione Anagrafiche" in Jira **dall'inizio alla fine senza sorprese**.

A differenza di guide generiche, questa:

- **Prevede TUTTO in anticipo**: niente "ah, serve anche questo" a metà strada
- **Non ti fa buttare lavoro**: prima prepari tutto, poi crei l'epic
- **È sequenziale**: ogni step dipende dal precedente, niente salti
- **Ha checkbox**: spunta ogni voce per tracciare progresso
- **È specifica per il tuo progetto**: tutti gli esempi sono basati sul vostro sistema NIS2 reale

---

## Struttura della Guida

La guida è divisa in **6 FASI**:

1. **FASE 0: Checklist Pre-Volo** - Verifica che hai tutto prima di iniziare
2. **FASE 1: Preparazione Ambiente** - Crea/verifica components, labels, fix versions
3. **FASE 2: Preparazione Contenuti** - Prepara description, links, metadata
4. **FASE 3: Creazione Epic** - Crea l'epic vera e propria
5. **FASE 4: Collegamento User Stories** - Collega le story all'epic
6. **FASE 5: Verifica Finale** - Checklist che tutto sia completo

---

## FASE 0: Checklist Pre-Volo

**Obiettivo**: Verificare che hai accesso e permessi necessari PRIMA di iniziare.

### Verifica Accessi

- [ ] **Accesso a Jira**: Hai account Jira attivo e puoi fare login
- [ ] **Progetto Jira esistente**: Esiste un progetto configurato (es: "CONF - Piattaforma Conformità NIS2/CIS")
- [ ] **Permessi di creazione**: Puoi creare Issue tipo "Epic" nel progetto
- [ ] **Permessi di configurazione**: Puoi creare/modificare Components, Labels, Fix Versions (o hai contatto admin che può farlo)

**Come verificare permessi**:

1. Vai al tuo progetto Jira
2. Click su **"Create"** (pulsante blu in alto)
3. Nel campo **"Issue Type"**, verifica che esista opzione **"Epic"**
4. Se vedi "Epic", hai i permessi. Chiudi il dialog senza salvare.

**Se NON hai permessi**: Contatta l'admin Jira e richiedi permessi "Create Issue" e "Project Administrator" (o almeno "Manage Components/Versions")

---

### Verifica Documentazione Disponibile

Prima di creare l'epic, devi avere questi documenti pronti (o sapere dove trovarli):

- [ ] **PRD o Documento Requisiti**: Documento che descrive funzionalità dell'epic
- [ ] **User Stories**: Lista user stories da collegare all'epic
- [ ] **Ordine Implementazione**: Documento che definisce priorità e dipendenze
- [ ] **Wireframe/Mockup** (opzionale): Link Figma/Sketch/PDF con mockup UI
- [ ] **Flow Diagram** (opzionale): Link Miro/Lucidchart con diagrammi flusso

**Documentazione per Epic Anagrafiche NIS2**:

- **PRD Location**: `C:\Users\pierl\Documents\Work\alfredo-nis2\deliveries\epica-anagrafiche\`
- **User Stories**: 27 file totali
  - `US-001-gestione-aziende-consulenza.md` (10 stories)
  - `US-002-gestione-aziende-clienti.md` (story da definire)
  - `US-003-gestione-utenti-admin.md` (6 stories)
- **Ordine Implementazione**: `ORDINE-IMPLEMENTAZIONE.md` (4 sprint, 27 stories: US-ANA-001 → US-ANA-027)
- **Wireframe**: (Da aggiungere quando disponibile)
- **Flow Diagram Multi-Tenancy**: (Da aggiungere quando disponibile)

**Se manca documentazione**: FERMATI. Non creare epic senza requisiti chiari. Scrivi prima PRD/User Stories, poi torna qui.

---

## FASE 1: Preparazione Ambiente Jira

**Obiettivo**: Creare/verificare che Components, Labels, Fix Versions esistano PRIMA di creare l'epic.

### Step 1.1: Verifica/Crea Components

**Cosa sono i Components**: Categorie funzionali del progetto (es: "Anagrafiche", "Autenticazione", "Audit", etc.)

**Perché servono prima**: Quando crei l'epic, dovrai selezionare un Component dal dropdown. Se non esiste, dovrai abbandonare la creazione dell'epic per crearlo.

#### Come Verificare Components Esistenti

1. Vai al tuo progetto Jira
2. Click su **Settings** (icona ingranaggio in basso a sinistra) → **"Components"**
3. Verifica se esiste il component per la tua epic

**Per Epic Anagrafiche NIS2**: Verifica se esiste component **"Anagrafiche"**

#### Come Creare Nuovo Component

Se il component NON esiste:

1. Nella pagina "Components", click **"Create Component"**
2. Compila il form:
   - **Name**: `Anagrafiche` (nome component)
   - **Description**: `Gestione anagrafiche: Aziende Consulenza, Aziende Clienti, Utenti (Admin, Consulenti, Utenti Aziendali), Sedi Aziendali con multi-tenancy`
   - **Component Lead**: Lascia vuoto o seleziona te stesso
   - **Default Assignee**: Seleziona "Component Lead" o "Project Default"
3. Click **"Save"**

**Checklist Components per Progetto NIS2 Completo** (crea quelli che ti servono):

- [ ] **Anagrafiche** - Gestione utenti, aziende consulenza, aziende clienti, sedi
- [ ] **Autenticazione & Sicurezza** - Login email+password, MFA obbligatorio, password reset
- [ ] **Framework Normativi** - Gestione framework NIS2/CIS (Ambito → Tematica → Categoria → Requisito)
- [ ] **Audit & Compliance** - Gestione audit conformità, valutazioni requisiti, calcolo compliance
- [ ] **Fornitori** - Processo qualifica fornitori con link temporaneo (7gg validità)
- [ ] **Azioni Correttive** - Gestione piano azioni, scadenze, notifiche
- [ ] **Reporting** - Generazione 4 report PDF (Report Audit, Compliance Framework, Piano Azioni, Qualifica Fornitori)
- [ ] **Dashboard** - Dashboard e KPI con filtri tenant
- [ ] **Sistema** - Notifiche email, configurazioni, logging, soft delete

---

### Step 1.2: Verifica/Crea Fix Versions

**Cosa sono le Fix Versions**: Milestone o release del progetto (es: "Release 1.0", "Release 2.0", "MVP")

**Perché servono prima**: Quando crei l'epic, dovrai selezionare una Fix Version dal dropdown.

#### Come Verificare Fix Versions Esistenti

1. Vai al tuo progetto Jira
2. Click su **Settings** (icona ingranaggio) → **"Releases"** (o "Versions")
3. Verifica se esiste la release per la tua epic

**Per Epic Anagrafiche NIS2**: Verifica se esiste release **"Release 1.0"** o **"MVP"**

#### Come Creare Nuova Fix Version

Se la release NON esiste:

1. Nella pagina "Releases", click **"Create Version"**
2. Compila il form:
   - **Name**: `Release 1.0 - MVP` (nome release)
   - **Start Date**: Data inizio sviluppo (es: 2025-12-11)
   - **Release Date**: Data rilascio prevista (es: 2026-03-15)
   - **Description**: `MVP con funzionalità core: Anagrafiche, Autenticazione, Framework NIS2/CIS, Audit base, Fornitori, 4 report PDF`
3. Click **"Save"**

**Checklist Fix Versions Suggerite per Piattaforma NIS2**:

- [ ] **Release 1.0 - MVP** - Funzionalità core: Anagrafiche + Autenticazione + Framework + Audit + Fornitori + Report base
- [ ] **Release 2.0 - Enhancement** - Azioni correttive avanzate, Report avanzati, Dashboard analytics, Performance optimization
- [ ] **Release 3.0 - Evoluzioni** - Multi-lingua, Mobile app, API pubbliche, Integrazioni esterne (OverRisk escluso da MVP)

---

### Step 1.3: Prepara Lista Labels

**Cosa sono i Labels**: Tag liberi per categorizzare issue (es: "must-have", "priority-high", "security")

**Perché prepararli prima**: I labels si possono creare al volo, MA è meglio avere una lista standard per consistenza.

**Labels Standard Consigliati per Progetto NIS2** (copia questa lista, la userai dopo):

```
must-have, should-have, nice-to-have, priority-high, priority-medium, priority-low, security, authentication, audit, reporting, compliance, frontend, backend, database, foundation, enhancement, bug, technical-debt, multi-tenancy, crud, regtech
```

**Per Epic Anagrafiche NIS2**: Userai questi labels:

```
must-have, priority-high, foundation, multi-tenancy, crud, database
```

**Rationale labels Epic Anagrafiche**:
- `must-have`: Epic bloccante - senza anagrafiche nessun'altra feature funziona
- `priority-high`: Massima priorità implementativa
- `foundation`: Fondamenta del sistema (tutte le epic successive dipendono da questa)
- `multi-tenancy`: Implementa segregazione dati rigorosa (Consulente A non vede dati Consulente B)
- `crud`: CRUD completo per Aziende Consulenza, Aziende Clienti, Utenti, Sedi
- `database`: Struttura database relazionale core con codifiche

**Nota**: I labels NON vanno creati in anticipo in Jira (si creano quando li usi la prima volta). Questa lista è solo per avere naming consistente.

- [ ] **Copiato lista labels standard** in un file testo temporaneo

---

### Step 1.4: Configura Board (Opzionale ma Consigliato)

**Obiettivo**: Configurare la Board Kanban/Scrum per visualizzare epic come swimlanes.

#### Come Configurare Swimlanes per Epic

1. Vai alla Board del progetto (es: "CONF Board")
2. Click su **"Board"** → **"Board Settings"** (menu in alto a destra)
3. Nella sidebar sinistra, click **"Swimlanes"**
4. Seleziona **"Epics"** come strategia swimlane
5. Click **"Save"**

**Risultato**: Le user stories saranno raggruppate per epic nella board, facilitando visualizzazione.

- [ ] **Board configurata con swimlanes per epic**

---

## FASE 2: Preparazione Contenuti Epic

**Obiettivo**: Scrivere description, preparare links e metadata PRIMA di aprire il form di creazione epic.

### Step 2.1: Scrivi Description Epic

**Perché scrivere prima**: La description è lunga (200-500 righe). Scriverla nel form Jira è scomodo. Meglio prepararla in un editor esterno (VSCode, Notepad++) e poi fare copy-paste.

#### Template Description Epic

Copia questo template in un file testo (es: `epic-anagrafiche-description.md`):

```markdown
## Obiettivo

[Descrizione breve obiettivo epic - 1-2 frasi]

## Scope Funzionale

Questa epic copre:

- [Feature 1]
- [Feature 2]
- [Feature 3]
- ...

**Escluso da questa epic:**

- [Feature esclusa 1]
- [Feature esclusa 2]

## Ruoli Coinvolti

- **Admin**: [Cosa può fare]
- **Consulente**: [Cosa può fare]
- **Azienda**: [Cosa può fare]
- **Fornitore**: [Cosa può fare o se escluso]

## Vincoli Tecnici

- [Vincolo 1]
- [Vincolo 2]
- [Vincolo 3]

## Deliverable Attesi

- [ ] PRD sezione [Nome]
- [ ] User stories dettagliate con acceptance criteria (27 stories)
- [ ] Ordine implementazione e roadmap sprint
- [ ] Wireframe pagine CRUD [Entità]
- [ ] Matrice tracciabilità requisiti

## Priorità

**[MUST-HAVE / SHOULD-HAVE / NICE-TO-HAVE]** - [Motivazione]

## Dipendenze

- **Dipendenze in ingresso**: [Epic che devono essere completate prima di questa]
- **Dipendenze in uscita**: [Epic che dipendono da questa]

## Note

[Note rilevanti per implementazione, coordinamento team, rischi, etc.]

---

**Epic collegata a:**

- Milestone: Release 1.0
- Componente: [Nome Component]
- Label: [label1], [label2], [label3]
```

#### Esempio Compilato per Epic Anagrafiche NIS2

Salva questo in `epic-anagrafiche-description.md`:

```markdown
## Obiettivo

Implementare la gestione completa delle anagrafiche per utenti (Admin Piattaforma, Consulenti, Utenti Aziendali), Aziende di Consulenza e Aziende Clienti (con Sedi), con supporto multi-tenancy rigoroso e segregazione dati per consulente.

## Scope Funzionale

Questa epic copre:

- **Gestione Utenti**:
  - Admin Piattaforma (CRUD con validazione vincoli: no auto-eliminazione, no ultimo Admin)
  - Consulenti (Admin-Consulente e Consulente semplice) collegati ad Aziende Consulenza
  - Utenti Aziendali (Admin Cliente e Cliente semplice) collegati ad Aziende Clienti
  - Lista unificata utenti con azioni contestuali intelligenti (redirect automatico al contesto appropriato)
  - Modal selezione tipo utente per creazione (3 flussi: Admin inline, Consulente → redirect Aziende Consulenza, Utente Aziendale → redirect Aziende Clienti)
  - Filtri e ricerca globale (nome, cognome, email, telefono) con debounce 300ms

- **Gestione Aziende di Consulenza**:
  - CRUD completo Aziende Consulenza (Admin)
  - Validazione P.IVA univoca (11 cifre numeriche)
  - Validazione Codice Fiscale univoco (11 o 16 caratteri alfanumerici)
  - Gestione consulenti collegati (CRUD completo in modal)
  - Gestione limiti licenza (max aziende clienti, max utenti aziende) configurabili
  - Visualizzazione aziende clienti associate (widget nel dettaglio)
  - Validazione vincoli eliminazione (blocco se esistono aziende clienti attive o audit attivi)
  - Filtri e ricerca (nome azienda, P.IVA, referente) con debounce 300ms

- **Gestione Aziende Clienti**:
  - CRUD completo Aziende Clienti (Consulente e Admin)
  - Validazione P.IVA o CF obbligatori (almeno uno dei due, univoci)
  - Assegnazione singolo consulente (scenario base) + multi-consulente (scenario avanzato)
  - Multi-tenancy logico: Consulente vede SOLO le proprie aziende clienti, Admin vede TUTTE
  - Gestione Sedi Aziendali (CRUD completo in modal, almeno 1 sede principale obbligatoria)
  - Gestione Utenti Aziendali (CRUD completo in modal, assegnati a sede specifica)
  - Context Switcher per Admin-Consulente che gestisce più Aziende di Consulenza
  - Validazione vincoli eliminazione (blocco se ci sono audit attivi, sedi, utenti)
  - Filtri e ricerca (ragione sociale, P.IVA, consulente assegnato) con debounce 300ms
  - Export liste (CSV e PDF con template)

- **Dashboard & KPI**:
  - Contatori dashboard filtrati per tenant (Admin vede globale, Consulente vede solo propri dati)
  - Widget: Aziende registrate, Consulenti, Azioni attive (con trend vs anno precedente)

- **Sistema**:
  - Soft delete per tutte le entità (preservazione audit trail con flag `deleted_at`)
  - Validazione email univoca globale (cross-tenant)
  - Invio email benvenuto con credenziali temporanee (12 caratteri alfanumerici)
  - Blocco creazione al raggiungimento soglie massime configurate (licenze)
  - Paginazione server-side su tutte le liste (8/16/24 rows per page)
  - Debounce 300ms su filtri testuali (performance con >1000 record)

**Escluso da questa epic:**

- Autenticazione e login (epic separata: E1 - Autenticazione)
- Gestione framework normativi NIS2/CIS (epic separata: E3 - Framework Normativi)
- Gestione audit e compliance (epic separata: E4 - Audit)
- Processo qualifica fornitori con link temporaneo (epic separata: E5 - Fornitori)
- Azioni correttive e piano azioni (epic separata: E6 - Azioni)
- Generazione report PDF (epic separata: E7 - Reporting)

## Ruoli Coinvolti

- **Admin Piattaforma**:
  - Accesso completo a TUTTE le anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti)
  - Può creare/modificare/eliminare qualsiasi entità (con validazione vincoli)
  - Vede dati globali senza filtri tenant
  - Gestisce limiti licenza per Aziende Consulenza

- **Consulente**:
  - Accesso filtrato alle PROPRIE aziende clienti (quelle a cui è stato esplicitamente assegnato)
  - Può gestire CRUD aziende clienti assegnate (sedi, utenti aziendali)
  - Vede SOLO dati del proprio tenant (multi-tenancy rigoroso)
  - NON vede aziende clienti di altri consulenti
  - Contatori dashboard filtrati per tenant

- **Admin-Consulente**:
  - Consulente con ruolo admin in un'Azienda di Consulenza
  - Può gestire consulenti della propria Azienda Consulenza
  - Vede TUTTE le aziende clienti della propria Azienda Consulenza (indipendentemente dalle assegnazioni esplicite)
  - Se associato a PIÙ Aziende di Consulenza: usa Context Switcher per cambiare contesto

- **Utente Aziendale (Admin Cliente / Cliente)**:
  - Accesso viewer ai dati della propria azienda cliente
  - NON gestisce anagrafiche (funzionalità esclusa per questo ruolo in questa epic)
  - Utilizzerà anagrafiche per consultare audit e conformità (epic future)

- **Fornitore**:
  - ESCLUSO da questa epic (accesso tramite link temporaneo gestito in epic separata E5)

## Vincoli Tecnici

- **Database relazionale**: Struttura tabelle relazionali con codifiche gestite in tabelle dedicate (no NoSQL)
- **Multi-tenancy logico**: Tabelle relazionali con foreign key `azienda_consulenza_id` (NON database separati per tenant)
- **P.IVA Aziende Consulenza**: Obbligatoria, univoca globalmente, 11 cifre numeriche
- **P.IVA/CF Aziende Clienti**: Almeno uno dei due obbligatorio, entrambi univoci se presenti
- **Email utenti**: Univoca globalmente (cross-tenant), formato valido, case-insensitive
- **Soft delete**: Tutte le entità eliminabili con flag `deleted_at` (NO delete fisico, preservazione audit trail)
- **Validazione vincoli eliminazione**:
  - Azienda Consulenza: blocco se esistono aziende clienti attive o audit attivi
  - Azienda Cliente: blocco se esistono audit attivi
  - Sede: blocco se è l'unica sede principale
  - Admin: blocco auto-eliminazione e blocco eliminazione ultimo Admin
  - Consulente: blocco eliminazione ultimo Admin-Consulente dell'azienda
- **Limiti licenza**: Configurabili per Azienda Consulenza (`max_aziende_clienti`, `max_utenti_aziende`), validati server-side
- **Almeno 1 sede principale**: Ogni Azienda Cliente deve avere almeno 1 sede con flag `is_principale = true`
- **Almeno 1 Admin**: Deve esistere sempre almeno 1 Admin Piattaforma attivo
- **Paginazione**: Server-side su tutte le liste (performance con >1000 record)
- **Debounce**: 300ms su filtri testuali (ottimizzazione query database)
- **Password temporanea**: 12 caratteri alfanumerici, hashed con bcrypt, validità 7 giorni
- **Email invito**: SMTP configurato, template HTML con credenziali, gestione errore invio (non bloccare creazione utente)

## Deliverable Attesi

- [ ] PRD sezione Anagrafiche completo (già disponibile in `deliveries/epica-anagrafiche/`)
- [ ] User stories dettagliate con acceptance criteria (27 stories: US-ANA-001 → US-ANA-027)
  - [ ] US-001-gestione-aziende-consulenza.md (10 stories: US-ANA-004 → US-ANA-008, US-ANA-018 → US-ANA-022)
  - [ ] US-002-gestione-aziende-clienti.md (stories da definire)
  - [ ] US-003-gestione-utenti-admin.md (6 stories: US-ANA-001 → US-ANA-003, US-ANA-009, US-ANA-026 → US-ANA-027)
- [ ] Ordine implementazione e roadmap 4 sprint (già disponibile in `ORDINE-IMPLEMENTAZIONE.md`)
  - [ ] Sprint 1: Foundation - Admin & Aziende Consulenza Base (7 stories, 8-10 giorni)
  - [ ] Sprint 2: Multi-Tenancy Core - Aziende Clienti & Sedi (8 stories, 12-14 giorni)
  - [ ] Sprint 3: Advanced Multi-Consulente & Context Switcher (6 stories, 10-12 giorni)
  - [ ] Sprint 4: Enhancement & Polish - Filtri, Ricerche, Gestione Utenti (6 stories, 8-10 giorni)
- [ ] Wireframe pagine CRUD:
  - [ ] Wireframe Lista/Dettaglio/Form Aziende Consulenza
  - [ ] Wireframe Lista/Dettaglio/Form Aziende Clienti
  - [ ] Wireframe Lista Unificata Utenti con modal selezione tipo
  - [ ] Wireframe Modal gestione Sedi Aziendali
  - [ ] Wireframe Modal gestione Consulenti
  - [ ] Wireframe Modal gestione Utenti Aziendali
  - [ ] Wireframe Context Switcher (dropdown tenant per Admin-Consulente multi-azienda)
- [ ] Flow diagram Multi-Tenancy:
  - [ ] Diagramma segregazione dati (Consulente A vs Consulente B)
  - [ ] Diagramma Context Switcher (Admin-Consulente di 2 Aziende Consulenza)
  - [ ] Diagramma Multi-Consulente (Azienda Cliente assegnata a 3 consulenti)
- [ ] Matrice tracciabilità requisiti (vincoli di progetto → user stories)

## Priorità

**MUST-HAVE (Release blocker)** - Le anagrafiche sono la **fondazione del sistema**. Senza utenti e aziende configurati, nessun'altra funzionalità (audit, framework, fornitori, report) può essere utilizzata. Questa epic **blocca tutte le epic successive**. Multi-tenancy implementato qui è critico per segregazione dati rigorosa richiesta da GDPR e conformità.

## Dipendenze

### Dipendenze in ingresso (epic che devono essere completate prima)

- **Epic E1 - Autenticazione** (parziale, parallelo):
  - Necessaria per login utenti e gestione sessioni
  - Creazione utenti può procedere in parallelo (epic Anagrafiche crea record utenti, epic Autenticazione gestisce login/MFA)
  - MFA obbligatorio configurato al primo accesso (implementato in epic Autenticazione)

### Dipendenze in uscita (epic che dipendono da questa - bloccate fino al completamento)

- **Epic E3 - Framework Normativi**: Framework NIS2/CIS associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- **Epic E4 - Audit**: Audit creati per Aziende Clienti da Consulenti (richiede Aziende Clienti + Consulenti + Utenti Aziendali)
- **Epic E5 - Fornitori**: Fornitori associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- **Epic E6 - Azioni Correttive**: Azioni assegnate a Utenti Aziendali (richiede Utenti Aziendali esistenti)
- **Epic E7 - Reporting**: Report generati per Aziende Clienti con dati anagrafici (richiede tutte le anagrafiche)

## Note

### Sprint Planning & Roadmap

- **Durata totale stimata**: 38-46 giorni (circa 8-10 settimane) con team 6/7 persone
- **Story Points totali**: 99 SP
- **Velocità media target**: 24 SP/sprint
- **Sprint 1 (Foundation)**: Rischio BASSO - creazione fondamenta stabili, testing completo prima di passare a Sprint 2
- **Sprint 2 (Multi-Tenancy)**: Rischio MEDIO - implementazione segregazione dati, test multi-tenancy CRITICI (Consulente A non deve vedere dati Consulente B)
- **Sprint 3 (Multi-Consulente)**: Rischio ALTO - Context Switcher complesso, validazioni vincoli eliminazione avanzate
- **Sprint 4 (Enhancement)**: Rischio BASSO - UX polish, filtri e ricerche

### Testing Critico

- **Multi-tenancy**: Testare RIGOROSAMENTE con multi-utenti (Consulente A crea azienda → Consulente B NON vede azienda in lista)
- **Context Switcher**: Testare Admin-Consulente associato a 2 Aziende Consulenza (switch contesto → refresh dati completo)
- **Validazioni vincoli**: Testare scenari blocco eliminazione (Azienda con audit attivi, ultimo Admin, auto-eliminazione)
- **Performance**: Testare con dataset popolato (>1000 record) → verificare paginazione server-side e debounce funzionanti
- **Soft delete**: Verificare preservazione audit trail (utente eliminato → `created_by` ancora referenziato)

### Coordinamento Team

- **Backend**: Schema database relazionale con tabelle anagrafiche, foreign key, indici su campi filtrabili
- **Frontend**: UI CRUD con form validazioni client-side + server-side, modal/dialog pattern consistente
- **UX Designer**: Wireframe per 6 entità (Aziende Consulenza, Aziende Clienti, Utenti, Sedi, Consulenti, Utenti Aziendali)
- **QA**: Test plan multi-tenancy, scenari edge case (eliminazioni, limiti licenza, validazioni univocità)

### Rischi Identificati

1. **Multi-tenancy bugs** (Sprint 2): Segregazione dati non corretta → Data leak tra tenant
   - **Mitigazione**: Code review su TUTTE le query con filtro tenant, security audit endpoint API
2. **Context Switcher complessità** (Sprint 3): Refresh dati incompleto → stato inconsistente
   - **Mitigazione**: Test approfonditi cambio contesto, persistenza sessione
3. **Performance con molti dati** (Sprint 4): Filtri lenti con >1000 record
   - **Mitigazione**: Paginazione server-side da subito, debounce 300ms, indici database
4. **Validazioni vincoli eliminazione** (Sprint 3): Eliminazione accidentale con dati collegati
   - **Mitigazione**: Dialog conferma dettagliato con lista impatti, soft delete con possibilità ripristino (feature futura)

---

**Epic collegata a:**

- **Milestone**: Release 1.0 - MVP
- **Componente**: Anagrafiche
- **Labels**: must-have, priority-high, foundation, multi-tenancy, crud, database
- **Story Points**: 99 SP
- **Sprint**: 4 sprint (Foundation → Multi-Tenancy Core → Advanced Multi-Consulente → Enhancement & Polish)
```

- [ ] **Description epic scritta e salvata** in file testo

---

### Step 2.2: Prepara Lista Links Esterni

**Obiettivo**: Preparare URL a documentazione esterna (PRD, user stories, wireframe, flow diagram) da collegare all'epic.

Crea una lista di link in un file testo (es: `epic-anagrafiche-links.txt`):

```
LINKS DA AGGIUNGERE ALL'EPIC ANAGRAFICHE NIS2

1. PRD Anagrafiche (Folder)
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/
   Title: PRD - Epic Gestione Anagrafiche

2. User Stories - Gestione Aziende Consulenza
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/US-001-gestione-aziende-consulenza.md
   Title: User Stories Aziende Consulenza (US-ANA-004 → US-ANA-008, US-ANA-018 → US-ANA-022)

3. User Stories - Gestione Aziende Clienti
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/US-002-gestione-aziende-clienti.md
   Title: User Stories Aziende Clienti (da definire)

4. User Stories - Gestione Utenti Admin
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/US-003-gestione-utenti-admin.md
   Title: User Stories Utenti Admin (US-ANA-001 → US-ANA-003, US-ANA-009, US-ANA-026 → US-ANA-027)

5. Ordine Implementazione - Roadmap 4 Sprint
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/ORDINE-IMPLEMENTAZIONE.md
   Title: Ordine Implementazione - 4 Sprint (27 stories, 99 SP, 38-46 giorni)

6. Wireframe Anagrafiche (PLACEHOLDER - aggiornare quando disponibile)
   URL: https://figma.com/file/[id]/wireframe-anagrafiche-nis2
   Title: Wireframe Anagrafiche (Liste, Dettagli, Form CRUD, Modal Sedi/Consulenti/Utenti, Context Switcher)

7. Flow Diagram Multi-Tenancy (PLACEHOLDER - aggiornare quando disponibile)
   URL: https://miro.com/board/[id]/flow-multi-tenancy-nis2
   Title: Flow Diagram Multi-Tenancy & Context Switcher

8. Documento Vincoli di Progetto NIS2
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/research/documento_vincolo_di_progetto_piattaforma_conformità_ni2.md
   Title: Vincoli di Progetto - Piattaforma Conformità NIS2/CIS

9. Database Access Legacy (Riferimento)
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/research/old_piattaforma_conformità_nis2.accdb
   Title: Database Access Legacy (Struttura Dati Riferimento)

10. Script Lettura Access
    URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/research/read_access.py
    Title: Script Python per Analisi Database Access
```

**Nota per Link File System**:
- I link `file://` funzionano solo se Jira è in locale o su rete condivisa.
- **Per team remoti**, usa link a repository Git (GitHub/GitLab) o documenti condivisi (Google Docs, Confluence).

**Alternativa Link Git** (se progetto su GitHub/GitLab):

```
1. PRD Anagrafiche
   URL: https://github.com/[org]/alfredo-nis2/tree/main/deliveries/epica-anagrafiche
   Title: PRD - Epic Gestione Anagrafiche

5. Ordine Implementazione
   URL: https://github.com/[org]/alfredo-nis2/blob/main/deliveries/epica-anagrafiche/ORDINE-IMPLEMENTAZIONE.md
   Title: Ordine Implementazione - 4 Sprint
```

- [ ] **Lista links preparata** in file testo

---

### Step 2.3: Prepara Metadata Epic

**Obiettivo**: Decidere valori per campi Epic Name, Summary, Priority, Labels, Component, Fix Version.

Compila questa tabella (salva in file testo `epic-anagrafiche-metadata.txt`):

```
METADATA EPIC ANAGRAFICHE NIS2

Epic Name (breve, max 255 char):
Gestione Anagrafiche

Summary (titolo completo con codice epic):
E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy

Priority:
Highest

Labels (separati da virgola, no spazi dopo virgola):
must-have,priority-high,foundation,multi-tenancy,crud,database

Component:
Anagrafiche

Fix Version:
Release 1.0 - MVP

Assignee:
[Il tuo nome o "Product Owner" o "Nautes"]

Reporter:
[Il tuo nome - auto-compilato da Jira]

Story Points (stimati):
99

Original Estimate (tempo):
38-46 giorni (8-10 settimane con team 6/7 persone)
```

**Convenzione Naming Epic per Progetto NIS2**:

- **Epic Name**: Breve (2-4 parole) - es: "Gestione Anagrafiche"
- **Summary**: `E[N] - [Titolo Descrittivo completo]` - es: "E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy"

**Codici Epic Piattaforma NIS2**:
  - `E1` = Autenticazione & Sicurezza (Login, MFA, Password Reset)
  - `E2` = **Anagrafiche** (Aziende Consulenza, Aziende Clienti, Utenti, Sedi)
  - `E3` = Framework Normativi (NIS2/CIS - Ambito → Tematica → Categoria → Requisito)
  - `E4` = Audit & Compliance (Gestione audit, valutazioni requisiti, calcolo compliance)
  - `E5` = Fornitori (Qualifica fornitori con link temporaneo 7gg)
  - `E6` = Azioni Correttive (Piano azioni, scadenze, notifiche)
  - `E7` = Reporting (4 report PDF: Audit, Compliance Framework, Piano Azioni, Qualifica Fornitori)
  - `E8` = Dashboard & Analytics (KPI, contatori, grafici)
  - `E9` = Sistema (Notifiche email, configurazioni, logging, audit trail)

- [ ] **Metadata epic preparata** in file testo

---

## FASE 3: Creazione Epic in Jira

**Obiettivo**: Creare l'epic in Jira compilando il form con i contenuti preparati in FASE 2.

**IMPORTANTE**: Ora che hai preparato TUTTO, la creazione dell'epic sarà veloce (5-10 minuti). Tieni aperti i file con description, links e metadata.

---

### Step 3.1: Aprire Form Creazione Epic

1. Vai al tuo progetto Jira (es: "CONF - Piattaforma Conformità NIS2/CIS")
2. Click su **"Create"** (pulsante blu in alto a destra)
3. Nel campo **"Issue Type"**, seleziona **"Epic"**

- [ ] **Form creazione epic aperto**

---

### Step 3.2: Compilare Campi Obbligatori

#### Campo: Epic Name

Copia da `epic-anagrafiche-metadata.txt` il valore **Epic Name**:

```
Gestione Anagrafiche
```

Incolla nel campo **"Epic Name"** del form Jira.

- [ ] **Epic Name compilato**

---

#### Campo: Summary

Copia da `epic-anagrafiche-metadata.txt` il valore **Summary**:

```
E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy
```

Incolla nel campo **"Summary"** del form Jira.

- [ ] **Summary compilato**

---

#### Campo: Description

Apri il file `epic-anagrafiche-description.md` che hai preparato in Step 2.1.

1. Seleziona TUTTO il contenuto (Ctrl+A)
2. Copia (Ctrl+C)
3. Torna al form Jira
4. Clicca nel campo **"Description"**
5. Incolla (Ctrl+V)

**Verifica**: La description dovrebbe apparire formattata con titoli, liste, checkbox.

- [ ] **Description compilata**

---

### Step 3.3: Compilare Campi Aggiuntivi

#### Campo: Priority

Copia da `epic-anagrafiche-metadata.txt` il valore **Priority**:

```
Highest
```

Nel form Jira, nel campo **"Priority"**, seleziona dal dropdown **"Highest"** (o equivalente nel tuo schema Jira: "Critical", "P0", "Blocker", etc.)

**Rationale Priority Highest**:
- Epic **bloccante** per Release 1.0 - senza anagrafiche nessun'altra feature funziona
- Foundation del sistema - tutte le epic successive (E3, E4, E5, E6, E7) dipendono da questa
- Multi-tenancy implementato qui è **critico** per conformità GDPR

- [ ] **Priority impostata su Highest**

---

#### Campo: Labels

Copia da `epic-anagrafiche-metadata.txt` il valore **Labels**:

```
must-have,priority-high,foundation,multi-tenancy,crud,database
```

Nel form Jira, nel campo **"Labels"**:

1. Clicca nel campo
2. Digita il primo label: `must-have`
3. Premi **Enter** (il label viene aggiunto)
4. Digita il secondo label: `priority-high`
5. Premi **Enter**
6. Continua per tutti i label: `foundation`, `multi-tenancy`, `crud`, `database`

**Nota**: Se il label non esiste, Jira ti proporrà di crearlo. Click su "Create label must-have".

- [ ] **Tutti i labels aggiunti** (must-have, priority-high, foundation, multi-tenancy, crud, database)

---

#### Campo: Component

Copia da `epic-anagrafiche-metadata.txt` il valore **Component**:

```
Anagrafiche
```

Nel form Jira, nel campo **"Component"**, seleziona dal dropdown **"Anagrafiche"**.

**Se il component NON appare nel dropdown**: Significa che non hai completato Step 1.1. FERMA qui.

1. Click **"Cancel"** per chiudere il form (salva description in un file prima!)
2. Torna a Step 1.1 e crea il component
3. Poi ritorna qui e riapri il form

- [ ] **Component selezionato**

---

#### Campo: Fix Version

Copia da `epic-anagrafiche-metadata.txt` il valore **Fix Version**:

```
Release 1.0 - MVP
```

Nel form Jira, nel campo **"Fix Version"** (o "Release"), seleziona dal dropdown **"Release 1.0 - MVP"**.

**Se la release NON appare nel dropdown**: Significa che non hai completato Step 1.2. FERMA qui.

1. Click **"Cancel"** per chiudere il form (salva description prima!)
2. Torna a Step 1.2 e crea la release
3. Poi ritorna qui e riapri il form

- [ ] **Fix Version selezionata**

---

#### Campo: Assignee

Copia da `epic-anagrafiche-metadata.txt` il valore **Assignee** (o seleziona te stesso).

Nel form Jira, nel campo **"Assignee"**, digita il nome dell'utente e seleziona dal dropdown.

**Consiglio**: Assegna a **Product Owner** (Nautes) o **Delivery Manager** (chi gestisce il backlog).

- [ ] **Assignee impostato**

---

#### Campo: Story Points (se campo custom configurato)

Copia da `epic-anagrafiche-metadata.txt` il valore **Story Points**:

```
99
```

Nel form Jira, nel campo **"Story Points"** (se presente), inserisci `99`.

**Nota**: Story Points epic = somma story points di tutte le user stories collegate (27 stories).

**Se campo Story Points NON presente**: Salta questo step (aggiungerai story points dopo collegando le user stories).

- [ ] **Story Points inseriti** (se campo presente)

---

#### Campo: Sprint

**IMPORTANTE**: Le epic NON si assegnano a sprint. Solo le user stories derivate vanno negli sprint.

Lascia il campo **"Sprint"** vuoto.

- [ ] **Sprint lasciato vuoto**

---

### Step 3.4: Salvare Epic

1. Verifica che tutti i campi obbligatori siano compilati (vedrai indicatore rosso se manca qualcosa)
2. Click su **"Create"** in fondo al form

**Risultato**: Jira creerà l'epic e ti mostrerà un messaggio di successo con l'**Epic Key** (es: `CONF-10`).

3. **ANNOTA L'EPIC KEY** in un file testo (es: `epic-anagrafiche-key.txt`):

```
EPIC KEY: CONF-10
EPIC URL: https://your-jira-domain.atlassian.net/browse/CONF-10
```

Questo key ti servirà per collegare le user stories (FASE 4).

- [ ] **Epic creata con successo**
- [ ] **Epic Key annotato**

---

## FASE 4: Collegamento Links e User Stories

**Obiettivo**: Aggiungere links esterni all'epic e collegare le 27 user stories.

### Step 4.1: Aprire Epic Appena Creata

1. Nel messaggio di successo, click sul link dell'epic (es: `CONF-10`)
2. Si apre la pagina dettaglio dell'epic

- [ ] **Pagina dettaglio epic aperta**

---

### Step 4.2: Aggiungere Links Esterni

#### Come Aggiungere Web Link

1. Nella pagina dettaglio epic, cerca la sezione **"Links"** (di solito nel pannello destro)
2. Click su **"Link"** → **"Web Link"**
3. Compila il form:
   - **URL**: Incolla URL da `epic-anagrafiche-links.txt`
   - **Title**: Incolla Title
4. Click **"Link"**

Ripeti per tutti i link preparati in Step 2.2:

- [ ] **Link 1: PRD Anagrafiche (Folder)** aggiunto
- [ ] **Link 2: User Stories Aziende Consulenza** aggiunto
- [ ] **Link 3: User Stories Aziende Clienti** aggiunto
- [ ] **Link 4: User Stories Utenti Admin** aggiunto
- [ ] **Link 5: Ordine Implementazione** aggiunto
- [ ] **Link 6: Wireframe Anagrafiche** aggiunto (se disponibile, altrimenti segna come TODO)
- [ ] **Link 7: Flow Diagram Multi-Tenancy** aggiunto (se disponibile, altrimenti segna come TODO)
- [ ] **Link 8: Documento Vincoli di Progetto** aggiunto
- [ ] **Link 9: Database Access Legacy** aggiunto (se rilevante)
- [ ] **Link 10: Script Lettura Access** aggiunto (se rilevante)

**Nota**: Se wireframe/flow non sono ancora pronti, aggiungi link placeholder e aggiornali dopo.

---

### Step 4.3: Collegare User Stories all'Epic

**Scenario**: Hai già creato le 27 user stories come Issue tipo "Story" in Jira, e ora vuoi collegarle all'epic.

**Se NON hai ancora creato le user stories**: Salta questo step per ora. Creerai le story dopo e le collegherai all'epic in quel momento (vedi Step 4.4).

#### Come Collegare Story Esistente all'Epic

**Metodo 1: Da Pagina Story**

1. Apri una user story in Jira (es: `CONF-20` = `US-ANA-001: Creare Admin Piattaforma`)
2. Cerca il campo **"Epic Link"** (di solito nel pannello destro)
3. Click nel campo **"Epic Link"**
4. Digita l'epic key (es: `CONF-10`) o il nome epic (`Gestione Anagrafiche`)
5. Seleziona l'epic dal dropdown
6. Jira salva automaticamente

**Metodo 2: Da Pagina Epic (Bulk Add)**

1. Nella pagina dettaglio epic (`CONF-10`), cerca sezione **"Child Issues"** o **"Issues in Epic"**
2. Click su **"Add"** o **"+"**
3. Nel dialog, cerca le story per key o summary (es: `US-ANA-001`)
4. Seleziona le story da collegare (multi-select con Ctrl+Click)
5. Click **"Add"**

**Per Epic Anagrafiche NIS2**: Collega le **27 user stories** `US-ANA-001` → `US-ANA-027`.

**Lista User Stories da Collegare**:

**Sprint 1 - Foundation (7 stories)**:
- US-ANA-001: Creare Admin Piattaforma
- US-ANA-002: Modificare Admin Piattaforma
- US-ANA-003: Eliminare Admin Piattaforma con validazione vincoli
- US-ANA-004: Visualizzare lista aziende di consulenza
- US-ANA-005: Creare nuova azienda di consulenza con primo admin-consulente
- US-ANA-006: Visualizzare dettaglio azienda di consulenza
- US-ANA-007: Modificare dati azienda di consulenza

**Sprint 2 - Multi-Tenancy Core (8 stories)**:
- US-ANA-008: Gestire consulenti collegati all'azienda di consulenza
- US-ANA-009: Visualizzare Lista Aziende Clienti
- US-ANA-010: Creare Azienda Cliente (assegnazione single-consulente)
- US-ANA-011: Visualizzare Dettaglio Azienda Cliente
- US-ANA-012: Gestire Sedi Aziendali
- US-ANA-013: Gestire Utenti Aziendali
- US-ANA-014: Modificare Azienda Cliente
- US-ANA-015: Eliminare Azienda Cliente

**Sprint 3 - Advanced Multi-Consulente (6 stories)**:
- US-ANA-016: Assegnare Multipli Consulenti (Multi-Consulente)
- US-ANA-017: Implementare Context Switcher per Multi-Consulente
- US-ANA-018: Gestire aziende clienti associate all'azienda di consulenza
- US-ANA-019: Eliminare azienda di consulenza con validazione vincoli
- US-ANA-020: Visualizzare contatori dashboard filtrati per tenant
- US-ANA-021: Bloccare creazione aziende/utenti al raggiungimento soglia massima

**Sprint 4 - Enhancement & Polish (6 stories)**:
- US-ANA-022: Ricercare e filtrare aziende di consulenza
- US-ANA-023: Ricercare e Filtrare Aziende Clienti
- US-ANA-024: Esportare Lista Aziende Clienti (CSV/PDF)
- US-ANA-025: Visualizzare lista unificata utenti
- US-ANA-026: Modal selezione tipo utente per creazione
- US-ANA-027: Filtrare e ricercare utenti

**Consiglio**: Se hai molte story, usa bulk add (Metodo 2) per risparmiare tempo.

- [ ] **User stories collegate all'epic** (tutte le 27 stories)

---

### Step 4.4: Creare User Stories Nuove Collegate all'Epic

**Scenario**: Non hai ancora creato le user stories, vuoi crearle ora e collegarle direttamente all'epic.

#### Come Creare Story Collegata all'Epic

1. Click su **"Create"** in Jira
2. Nel campo **"Issue Type"**, seleziona **"Story"**
3. Nel campo **"Epic Link"**, seleziona `CONF-10 - Gestione Anagrafiche` (l'epic che hai appena creato)
4. Compila il campo **"Summary"** con il nome della story (es: `US-ANA-001: Creare Admin Piattaforma`)
5. Compila il campo **"Description"** con il contenuto della user story:
   - Template: "Come [ruolo] Voglio [azione] In modo che [beneficio]"
   - Acceptance Criteria (copiati dai file US-*.md)
   - Dipendenze
   - Edge Cases
6. Compila campi aggiuntivi:
   - **Priority**: es: `High`
   - **Labels**: es: `must-have,admin,crud,foundation`
   - **Component**: `Anagrafiche` (stesso component dell'epic)
   - **Fix Version**: `Release 1.0 - MVP` (stesso fix version dell'epic)
   - **Story Points**: es: `3` (basato su complessità)
7. Click **"Create"**

Ripeti per tutte le 27 user stories dell'epic.

**Fonte User Stories**:
- `US-001-gestione-aziende-consulenza.md` (10 stories)
- `US-002-gestione-aziende-clienti.md` (stories da definire)
- `US-003-gestione-utenti-admin.md` (6 stories)

**Consiglio**: Crea prima le **7 story di Sprint 1** per iniziare sviluppo, poi continua con le altre man mano.

- [ ] **User stories create e collegate all'epic**

---

### Step 4.5: Ordinare User Stories per Priorità

**Obiettivo**: Le story nell'epic devono essere ordinate per priorità implementazione (quelle da fare prima in alto).

#### Come Riordinare Story nell'Epic

**Metodo 1: Drag & Drop nella Board**

1. Vai alla Board Kanban/Scrum del progetto
2. Se hai configurato swimlanes per epic (Step 1.4), vedrai le story raggruppate sotto l'epic
3. Drag & Drop le story per riordinarle (prima story = priorità più alta)

**Metodo 2: Riordino da Backlog**

1. Vai al **"Backlog"** del progetto
2. Filtra per epic: seleziona `CONF-10 - Gestione Anagrafiche`
3. Drag & Drop le story nell'ordine desiderato

**Per Epic Anagrafiche NIS2**: Ordina le 27 story secondo `ORDINE-IMPLEMENTAZIONE.md`:

**Sprint 1** (7 stories, ordine sequenziale):
1. US-ANA-001: Creare Admin Piattaforma
2. US-ANA-002: Modificare Admin Piattaforma
3. US-ANA-003: Eliminare Admin Piattaforma con validazione vincoli
4. US-ANA-004: Visualizzare lista aziende di consulenza
5. US-ANA-005: Creare nuova azienda di consulenza con primo admin-consulente
6. US-ANA-006: Visualizzare dettaglio azienda di consulenza
7. US-ANA-007: Modificare dati azienda di consulenza

**Sprint 2** (8 stories):
8. US-ANA-008: Gestire consulenti collegati
9. US-ANA-009: Visualizzare Lista Aziende Clienti
10. US-ANA-010: Creare Azienda Cliente
11. US-ANA-011: Visualizzare Dettaglio Azienda Cliente
12. US-ANA-012: Gestire Sedi Aziendali
13. US-ANA-013: Gestire Utenti Aziendali
14. US-ANA-014: Modificare Azienda Cliente
15. US-ANA-015: Eliminare Azienda Cliente

**Sprint 3** (6 stories):
16. US-ANA-016: Assegnare Multipli Consulenti
17. US-ANA-017: Implementare Context Switcher
18. US-ANA-018: Gestire aziende clienti associate
19. US-ANA-019: Eliminare azienda di consulenza
20. US-ANA-020: Visualizzare contatori dashboard
21. US-ANA-021: Bloccare creazione al limite

**Sprint 4** (6 stories):
22. US-ANA-022: Ricercare e filtrare aziende di consulenza
23. US-ANA-023: Ricercare e Filtrare Aziende Clienti
24. US-ANA-024: Esportare Lista Aziende Clienti
25. US-ANA-025: Visualizzare lista unificata utenti
26. US-ANA-026: Modal selezione tipo utente
27. US-ANA-027: Filtrare e ricercare utenti

- [ ] **User stories ordinate per priorità** (sequenza Sprint 1 → Sprint 2 → Sprint 3 → Sprint 4)

---

### Step 4.6: Creare Relazioni tra Epic (se applicabile)

**Obiettivo**: Se la tua epic dipende da altre epic o blocca altre epic, crea link espliciti.

#### Come Creare Link tra Epic

1. Nella pagina dettaglio epic (`CONF-10`), cerca sezione **"Links"**
2. Click su **"Link"** → **"Jira Issue"**
3. Seleziona tipo relazione:
   - **"is blocked by"**: Questa epic è bloccata da altra epic
   - **"blocks"**: Questa epic blocca altra epic
   - **"relates to"**: Epic collegate ma non bloccanti
4. Nel campo **"Issue"**, digita l'epic key o nome
5. Click **"Link"**

**Per Epic Anagrafiche NIS2 (E2)**:

**Dipendenze IN ingresso** (questa epic è bloccata da):
- `E1` - Epic Autenticazione & Sicurezza (parziale, parallelo)
  - Tipo relazione: **"relates to"** (non bloccante completo - creazione utenti può procedere in parallelo)
  - Note: MFA obbligatorio configurato al primo accesso (implementato in E1)

**Dipendenze IN uscita** (questa epic blocca):
- `E3` - Epic Framework Normativi
  - Tipo relazione: **"blocks"**
  - Motivo: Framework associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- `E4` - Epic Audit & Compliance
  - Tipo relazione: **"blocks"**
  - Motivo: Audit creati per Aziende Clienti da Consulenti (richiede Aziende + Consulenti + Utenti)
- `E5` - Epic Fornitori
  - Tipo relazione: **"blocks"**
  - Motivo: Fornitori associati ad Aziende Clienti (richiede Aziende Clienti esistenti)
- `E6` - Epic Azioni Correttive
  - Tipo relazione: **"blocks"**
  - Motivo: Azioni assegnate a Utenti Aziendali (richiede Utenti Aziendali esistenti)
- `E7` - Epic Reporting
  - Tipo relazione: **"blocks"**
  - Motivo: Report generati con dati anagrafici (richiede tutte le anagrafiche)

**Nota**: Se le altre epic non esistono ancora, salta questo step e aggiungi i link dopo quando le creerai.

- [ ] **Relazione "relates to" con E1 (Autenticazione)** creata (se epic esiste)
- [ ] **Relazione "blocks" con E3 (Framework)** creata (se epic esiste)
- [ ] **Relazione "blocks" con E4 (Audit)** creata (se epic esiste)
- [ ] **Relazione "blocks" con E5 (Fornitori)** creata (se epic esiste)
- [ ] **Relazione "blocks" con E6 (Azioni)** creata (se epic esiste)
- [ ] **Relazione "blocks" con E7 (Reporting)** creata (se epic esiste)

---

## FASE 5: Verifica Finale e Post-Creazione

**Obiettivo**: Verificare che l'epic sia completa e configurare filtri/dashboard.

### Step 5.1: Checklist Completezza Epic

Apri la pagina dettaglio dell'epic e verifica:

- [ ] **Epic Name** breve e chiaro (es: "Gestione Anagrafiche")
- [ ] **Summary** con convenzione `E[N] - [Titolo]` (es: "E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy")
- [ ] **Description** completa con:
  - [ ] Obiettivo
  - [ ] Scope Funzionale (incluso + escluso)
  - [ ] Ruoli Coinvolti (Admin, Consulente, Admin-Consulente, Utente Aziendale, Fornitore)
  - [ ] Vincoli Tecnici (multi-tenancy, P.IVA, soft delete, validazioni, limiti licenza)
  - [ ] Deliverable Attesi (con checkbox per PRD, user stories, roadmap, wireframe, flow diagram)
  - [ ] Priorità MUST-HAVE + motivazione (epic bloccante, foundation)
  - [ ] Dipendenze (in ingresso: E1 parziale; in uscita: E3, E4, E5, E6, E7)
  - [ ] Note (sprint planning, testing critico multi-tenancy, coordinamento team, rischi)
- [ ] **Priority** impostata su `Highest`
- [ ] **Labels** configurati (must-have, priority-high, foundation, multi-tenancy, crud, database)
- [ ] **Component** assegnato (`Anagrafiche`)
- [ ] **Fix Version** = `Release 1.0 - MVP`
- [ ] **Assignee** impostato (Product Owner o Delivery Manager)
- [ ] **Story Points** = `99` (se campo configurato)
- [ ] **Sprint** lasciato vuoto (corretto - epic non vanno in sprint)
- [ ] **Links esterni** aggiunti:
  - [ ] Link PRD Anagrafiche (Folder)
  - [ ] Link User Stories Aziende Consulenza
  - [ ] Link User Stories Aziende Clienti
  - [ ] Link User Stories Utenti Admin
  - [ ] Link Ordine Implementazione
  - [ ] Link Wireframe (o placeholder)
  - [ ] Link Flow Diagram Multi-Tenancy (o placeholder)
  - [ ] Link Documento Vincoli di Progetto
- [ ] **Relazioni con altre epic** create (E1 relates to, E3-E7 blocks - se epic esistono)
- [ ] **User Stories collegate** all'epic (27 stories: US-ANA-001 → US-ANA-027)
- [ ] **User Stories ordinate** per priorità implementazione (sequenza Sprint 1 → 2 → 3 → 4)

---

### Step 5.2: Creare Filtri Jira per Epic

**Obiettivo**: Creare filtri salvati per visualizzare velocemente story dell'epic o epic della release.

#### Filtro 1: Tutte le Story dell'Epic Anagrafiche

1. Vai a **"Filters"** → **"Advanced Search"**
2. Scrivi query JQL:

```jql
project = "CONF" AND "Epic Link" = CONF-10 ORDER BY priority DESC, created ASC
```

(Sostituisci `CONF-10` con l'epic key della tua epic)

3. Click **"Save As"** (icona floppy disk in alto a destra)
4. Nome filtro: `Epic Anagrafiche - All Stories (27)`
5. Descrizione: `Tutte le 27 user stories dell'epic E2 - Gestione Anagrafiche (US-ANA-001 → US-ANA-027)`
6. Check **"Add to favorites"** (opzionale)
7. Click **"Submit"**

- [ ] **Filtro "Epic Anagrafiche - All Stories" creato**

---

#### Filtro 2: Story Epic Anagrafiche - Sprint 1 (Foundation)

1. Query JQL:

```jql
project = "CONF" AND "Epic Link" = CONF-10 AND labels = "sprint-1" ORDER BY priority DESC
```

(Presuppone che tu abbia aggiunto label `sprint-1` alle story del primo sprint. Se non l'hai fatto, usa alternative query sotto)

**Query alternativa** (basata su sprint effettivo):

```jql
project = "CONF" AND "Epic Link" = CONF-10 AND Sprint = "Sprint 1 - Foundation" ORDER BY priority DESC
```

2. Salva come: `Epic Anagrafiche - Sprint 1 Foundation (7 stories)`

**Per tutti i 4 sprint**:
- Filtro Sprint 1: 7 stories (US-ANA-001 → US-ANA-007)
- Filtro Sprint 2: 8 stories (US-ANA-008 → US-ANA-015)
- Filtro Sprint 3: 6 stories (US-ANA-016 → US-ANA-021)
- Filtro Sprint 4: 6 stories (US-ANA-022 → US-ANA-027)

- [ ] **Filtro "Epic Anagrafiche - Sprint 1" creato** (opzionale)
- [ ] **Filtro "Epic Anagrafiche - Sprint 2" creato** (opzionale)
- [ ] **Filtro "Epic Anagrafiche - Sprint 3" creato** (opzionale)
- [ ] **Filtro "Epic Anagrafiche - Sprint 4" creato** (opzionale)

---

#### Filtro 3: Tutte le Epic Release 1.0 - MVP

1. Query JQL:

```jql
project = "CONF" AND issuetype = Epic AND fixVersion = "Release 1.0 - MVP" ORDER BY priority DESC, created ASC
```

2. Salva come: `Epic Release 1.0 - MVP - All`
3. Descrizione: `Tutte le epic della Release 1.0 MVP (E1, E2, E3, E4, E5, E6, E7, E8, E9)`

- [ ] **Filtro "Epic Release 1.0 - All" creato**

---

#### Filtro 4: Epic Must-Have (Bloccanti Release)

1. Query JQL:

```jql
project = "CONF" AND issuetype = Epic AND labels = "must-have" ORDER BY priority DESC
```

2. Salva come: `Epic Must-Have (Release Blockers)`
3. Descrizione: `Epic bloccanti per Release 1.0 - senza queste la release non può uscire`

- [ ] **Filtro "Epic Must-Have" creato**

---

### Step 5.3: Aggiungere Epic a Dashboard (Opzionale)

**Obiettivo**: Creare gadget dashboard per monitorare progresso epic.

#### Come Creare Dashboard per Epic

1. Vai a **"Dashboards"** → **"Create Dashboard"**
2. Nome: `Epic Anagrafiche - Progress Tracker`
3. Click **"Create"**
4. Click **"Add Gadget"**

**Gadget 1: Epic Burndown**

1. Cerca gadget **"Epic Burndown"**
2. Seleziona epic: `CONF-10 - Gestione Anagrafiche`
3. Click **"Save"**

**Gadget 2: Epic Progress (Pie Chart)**

1. Cerca gadget **"Pie Chart"**
2. Filtro: Seleziona filtro `Epic Anagrafiche - All Stories` (creato in Step 5.2)
3. Statistic Type: **"Issue Status"**
4. Click **"Save"**

**Gadget 3: Epic Story List**

1. Cerca gadget **"Filter Results"**
2. Filtro: Seleziona filtro `Epic Anagrafiche - All Stories`
3. Numero di risultati: `50`
4. Click **"Save"**

**Gadget 4: Sprint Progress (per Sprint 1)**

1. Cerca gadget **"Sprint Burndown"**
2. Seleziona Sprint: `Sprint 1 - Foundation`
3. Click **"Save"**

- [ ] **Dashboard epic creata con 4 gadget** (opzionale)

---

### Step 5.4: Aggiornare Documentazione Esterna

**Obiettivo**: Aggiornare PRD e file README con link all'epic Jira.

#### Aggiungere Link Jira al PRD

Apri il file README nella cartella PRD (es: `deliveries/epica-anagrafiche/README.md`) e aggiungi sezione:

```markdown
## Tracciabilità Jira

### Epic Jira

- **Epic Key**: CONF-10
- **Epic Name**: E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy
- **Epic URL**: [CONF-10 - E2 Gestione Anagrafiche](https://your-jira-domain.atlassian.net/browse/CONF-10)
- **Priority**: Highest (MUST-HAVE, Release Blocker)
- **Fix Version**: Release 1.0 - MVP
- **Story Points**: 99 SP
- **Sprint**: 4 sprint (Foundation → Multi-Tenancy Core → Advanced Multi-Consulente → Enhancement & Polish)
- **Durata Stimata**: 38-46 giorni (8-10 settimane con team 6/7 persone)

### User Stories Jira

**Sprint 1 - Foundation (7 stories, 21 SP)**:
- [CONF-20] US-ANA-001: Creare Admin Piattaforma
- [CONF-21] US-ANA-002: Modificare Admin Piattaforma
- [CONF-22] US-ANA-003: Eliminare Admin Piattaforma con validazione vincoli
- [CONF-23] US-ANA-004: Visualizzare lista aziende di consulenza
- [CONF-24] US-ANA-005: Creare nuova azienda di consulenza con primo admin-consulente
- [CONF-25] US-ANA-006: Visualizzare dettaglio azienda di consulenza
- [CONF-26] US-ANA-007: Modificare dati azienda di consulenza

**Sprint 2 - Multi-Tenancy Core (8 stories, 34 SP)**:
- [CONF-27] US-ANA-008: Gestire consulenti collegati all'azienda di consulenza
- [CONF-28] US-ANA-009: Visualizzare Lista Aziende Clienti
- [CONF-29] US-ANA-010: Creare Azienda Cliente (assegnazione single-consulente)
- [CONF-30] US-ANA-011: Visualizzare Dettaglio Azienda Cliente
- [CONF-31] US-ANA-012: Gestire Sedi Aziendali
- [CONF-32] US-ANA-013: Gestire Utenti Aziendali
- [CONF-33] US-ANA-014: Modificare Azienda Cliente
- [CONF-34] US-ANA-015: Eliminare Azienda Cliente

**Sprint 3 - Advanced Multi-Consulente (6 stories, 26 SP)**:
- [CONF-35] US-ANA-016: Assegnare Multipli Consulenti (Multi-Consulente)
- [CONF-36] US-ANA-017: Implementare Context Switcher per Multi-Consulente
- [CONF-37] US-ANA-018: Gestire aziende clienti associate all'azienda di consulenza
- [CONF-38] US-ANA-019: Eliminare azienda di consulenza con validazione vincoli
- [CONF-39] US-ANA-020: Visualizzare contatori dashboard filtrati per tenant
- [CONF-40] US-ANA-021: Bloccare creazione aziende/utenti al raggiungimento soglia massima

**Sprint 4 - Enhancement & Polish (6 stories, 18 SP)**:
- [CONF-41] US-ANA-022: Ricercare e filtrare aziende di consulenza
- [CONF-42] US-ANA-023: Ricercare e Filtrare Aziende Clienti
- [CONF-43] US-ANA-024: Esportare Lista Aziende Clienti (CSV/PDF)
- [CONF-44] US-ANA-025: Visualizzare lista unificata utenti
- [CONF-45] US-ANA-026: Modal selezione tipo utente per creazione
- [CONF-46] US-ANA-027: Filtrare e ricercare utenti

### Filtri Jira

- [Epic Anagrafiche - All Stories (27)](https://your-jira-domain.atlassian.net/issues/?filter=12345)
- [Epic Anagrafiche - Sprint 1 Foundation](https://your-jira-domain.atlassian.net/issues/?filter=12346)
- [Epic Release 1.0 - MVP - All](https://your-jira-domain.atlassian.net/issues/?filter=12347)
- [Epic Must-Have (Release Blockers)](https://your-jira-domain.atlassian.net/issues/?filter=12348)

### Dashboard

- [Epic Anagrafiche - Progress Tracker](https://your-jira-domain.atlassian.net/dashboards/12345)
```

**Nota**: Sostituisci `your-jira-domain.atlassian.net` con l'URL del tuo Jira aziendale e aggiorna i numeri CONF-XX con i key reali assegnati da Jira.

- [ ] **PRD aggiornato con link Jira**

---

### Step 5.5: Notificare Team

**Obiettivo**: Comunicare al team che l'epic è stata creata e è pronta per planning.

#### Email/Messaggio al Team

Copia questo template e invia al team (email, Slack, Teams):

```
Oggetto: Epic "Gestione Anagrafiche" (E2) creata in Jira - Pronta per Sprint Planning

Ciao team,

Ho creato l'epic "Gestione Anagrafiche" (E2) in Jira per la Piattaforma Conformità NIS2/CIS:

📌 Epic Key: CONF-10
📌 Epic Name: E2 - Gestione Anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti, Sedi) - Multi-Tenancy
📌 Epic URL: https://your-jira-domain.atlassian.net/browse/CONF-10

## Dettagli Epic

- **Priorità**: HIGHEST (MUST-HAVE, Release Blocker)
- **Fix Version**: Release 1.0 - MVP
- **Component**: Anagrafiche
- **Story Points**: 99 SP
- **User Stories**: 27 stories collegate (US-ANA-001 → US-ANA-027)
- **Durata Stimata**: 38-46 giorni (8-10 settimane con team 6/7 persone)

## Roadmap Implementazione (4 Sprint)

- **Sprint 1 - Foundation** (7 stories, 21 SP, 8-10 giorni):
  - Admin Piattaforma CRUD
  - Aziende Consulenza CRUD base
  - Rischio: BASSO

- **Sprint 2 - Multi-Tenancy Core** (8 stories, 34 SP, 12-14 giorni):
  - Aziende Clienti CRUD con multi-tenancy
  - Sedi Aziendali + Utenti Aziendali
  - Rischio: MEDIO (testing multi-tenancy CRITICO)

- **Sprint 3 - Advanced Multi-Consulente** (6 stories, 26 SP, 10-12 giorni):
  - Multi-consulente + Context Switcher
  - Validazioni vincoli eliminazione avanzate
  - Rischio: ALTO (Context Switcher complesso)

- **Sprint 4 - Enhancement & Polish** (6 stories, 18 SP, 8-10 giorni):
  - Filtri, ricerche, export CSV/PDF
  - Lista unificata utenti
  - Rischio: BASSO

## Documentazione Disponibile

- **PRD**: C:\Users\pierl\Documents\Work\alfredo-nis2\deliveries\epica-anagrafiche\
- **User Stories**:
  - US-001-gestione-aziende-consulenza.md (10 stories)
  - US-002-gestione-aziende-clienti.md (stories da definire)
  - US-003-gestione-utenti-admin.md (6 stories)
- **Ordine Implementazione**: ORDINE-IMPLEMENTAZIONE.md (roadmap dettagliata 4 sprint)
- **Wireframe**: (TODO - da creare)
- **Flow Diagram Multi-Tenancy**: (TODO - da creare)

## Prossimi Passi

1. **Review epic description e user stories** (deadline: [data])
2. **Sprint Planning Sprint 1** (7 stories da stimare, kickoff: [data])
3. **Creazione wireframe** (Aziende Consulenza, Aziende Clienti, Utenti, Sedi, Context Switcher)
4. **Setup environment sviluppo** (database, SMTP, AWS staging)
5. **Kick-off sviluppo Sprint 1** (data inizio: [data])

## Note Importanti

- ⚠️ **Epic BLOCCANTE**: Senza anagrafiche nessun'altra epic (E3 Framework, E4 Audit, E5 Fornitori, E6 Azioni, E7 Reporting) può funzionare
- ⚠️ **Multi-tenancy CRITICO**: Testing rigoroso segregazione dati (Consulente A NON deve vedere dati Consulente B)
- ⚠️ **Context Switcher complesso**: Feature ad alto rischio (Sprint 3), pianificare tempo extra testing

## Domande?

Rispondete a questa email o scrivetemi su Slack/Teams.

Grazie!
[Il tuo nome]
Product Owner / Delivery Manager
Piattaforma Conformità NIS2/CIS
```

**Nota**: Aggiorna i placeholder `[data]`, `[Il tuo nome]`, `your-jira-domain.atlassian.net` con valori reali.

- [ ] **Team notificato** via email/Slack/Teams

---

## FASE 6: Manutenzione Epic (Durante Sviluppo)

**Obiettivo**: Mantenere l'epic aggiornata durante lo sviluppo.

### Durante lo Sviluppo

**Ogni settimana** (o dopo ogni sprint):

1. **Aggiorna checklist Deliverable** nella description epic:

   - Spunta `[x]` i deliverable completati
   - Esempio: `[x] User stories dettagliate (27 stories completate)`

2. **Aggiungi commento status update** nell'epic:

```markdown
## Status Update - Week 50/2025 - Sprint 1 Completato

**Progress Sprint 1 - Foundation**:

- ✅ Completate: US-ANA-001, US-ANA-002, US-ANA-003, US-ANA-004, US-ANA-005, US-ANA-006, US-ANA-007 (7/7 stories)
- 🚧 In corso: Nessuna (Sprint 1 chiuso)
- 📋 In backlog: US-ANA-008 → US-ANA-027 (20 stories)

**Testing Sprint 1**:

- ✅ Unit test: 85% coverage
- ✅ E2E test: Admin CRUD, Aziende Consulenza CRUD, Email invito (tutti passanti)
- ✅ Validazioni vincoli: Auto-eliminazione Admin, ultimo Admin (bloccati correttamente)

**Blocchi**:

- Nessuno

**Prossimi Passi**:

- Sprint 2 kick-off: lunedì 2025-12-18
- Iniziare US-ANA-008 (Gestire consulenti collegati)
- Testing multi-tenancy CRITICO in Sprint 2

**Rischi**:

- Nessuno identificato in Sprint 1
- Sprint 2: Rischio MEDIO per implementazione multi-tenancy (pianificare testing rigoroso)

**Story Points**:

- Consumati Sprint 1: 21/99 SP (21%)
- Remaining: 78 SP
- Velocità Sprint 1: 21 SP/sprint
- Stima completamento: 4 sprint (~ 8 settimane) - confermato

**Metriche Sprint 1**:

- Durata effettiva: 9 giorni (stimato: 8-10 giorni) ✅
- Bug trovati in QA: 3 (tutti fixati)
- Code review: 7 PR approvate
- Tech debt: 0 (nessun shortcut preso)
```

3. **Aggiorna links** se cambiano URL (es: wireframe finalmente pronti):
   - Sostituisci placeholder link Figma con URL reale
   - Aggiungi commento: "Wireframe disponibili: [URL]"

4. **Traccia blocchi** con link a issue bloccanti:
   - Es: "US-ANA-008 bloccata da bug CONF-50 (SMTP non configurato)"
   - Crea dependency link in Jira: US-ANA-008 "is blocked by" CONF-50

5. **Aggiorna Epic Status** (se campo custom configurato):
   - Sprint 1: Status = "In Progress"
   - Dopo Sprint 1: Status = "27% Complete"
   - Dopo Sprint 2: Status = "58% Complete"
   - Dopo Sprint 3: Status = "84% Complete"
   - Dopo Sprint 4: Status = "Done"

- [ ] **Epic aggiornata settimanalmente** durante sviluppo

---

### Quando Completare Epic

L'epic si considera **COMPLETA** quando:

1. **Tutte le 27 user stories** collegate sono in stato "Done"
2. **Tutti i deliverable** nella checklist sono spuntati `[x]`
3. **Test E2E superati** per tutti i flussi principali:
   - Admin CRUD (creazione, modifica, eliminazione con vincoli)
   - Aziende Consulenza CRUD (creazione, modifica, gestione consulenti, eliminazione con vincoli)
   - Aziende Clienti CRUD (creazione single-consulente, multi-consulente, sedi, utenti aziendali, eliminazione con vincoli)
   - Multi-tenancy (Consulente A non vede dati Consulente B)
   - Context Switcher (Admin-Consulente di 2 aziende consulenza, switch contesto, refresh dati)
   - Dashboard contatori (Admin vede globale, Consulente vede filtrato)
   - Filtri e ricerche (debounce, paginazione, reset filtri)
   - Export CSV/PDF (template corretti, dati completi)
4. **Deploy su staging** completato e smoke test passanti
5. **Documentazione aggiornata**:
   - API docs (endpoint anagrafiche)
   - README (setup database, configurazione SMTP)
   - Changelog (features aggiunte in Release 1.0)
6. **Performance verificata**:
   - Testato con >1000 record
   - Paginazione server-side funzionante
   - Debounce 300ms attivo su filtri testuali
   - Query < 2 secondi per liste lunghe

**Come chiudere epic**:

1. Apri epic in Jira
2. Click **"Workflow"** → **"Done"** (o equivalente)
3. Aggiungi commento finale:

```markdown
## Epic Completata - 2025-02-28

✅ Tutte le 27 user stories completate con successo.

### Deliverable Completati

- [x] PRD sezione Anagrafiche completo
- [x] User stories dettagliate (27 stories: US-ANA-001 → US-ANA-027)
- [x] Ordine implementazione e roadmap 4 sprint
- [x] Wireframe CRUD Aziende Consulenza, Aziende Clienti, Utenti, Sedi, Context Switcher
- [x] Flow diagram multi-tenancy e context switcher
- [x] Matrice tracciabilità requisiti

### Testing Completato

- [x] Unit test: coverage 87% (target: >80%) ✅
- [x] E2E test: tutti passanti (54 scenari testati)
- [x] Multi-tenancy: testato rigorosamente (Consulente A non vede dati Consulente B) ✅
- [x] Context Switcher: testato con Admin-Consulente di 2 aziende ✅
- [x] Performance: testato con 1500 record (paginazione server-side OK, debounce OK) ✅
- [x] Validazioni vincoli: auto-eliminazione, ultimo Admin, aziende con audit attivi (tutti bloccati correttamente) ✅

### Deploy & Staging

- [x] Staging deploy completato (2025-02-28 15:30)
- [x] Smoke test passanti (27/27 scenari OK)
- [x] Database migrazione applicata (schema anagrafiche v1.0)
- [x] SMTP configurato e testato (email invito funzionanti)
- [x] Pronto per release produzione

### Metriche Epic

- **Story Points**: 99 SP (completati)
- **Sprint**: 4 sprint (Foundation → Multi-Tenancy → Multi-Consulente → Enhancement)
- **Durata**: 44 giorni (stimato: 38-46 giorni) ✅
- **Velocità media**: 24.75 SP/sprint (target: 24 SP/sprint) ✅
- **Bug trovati in QA**: 18 (tutti fixati prima di release)
- **Tech debt**: 2 items identificati (schedulati per Sprint 5)

### Lessons Learned

**Cosa è andato bene**:
- Multi-tenancy implementato correttamente al primo colpo (testing rigoroso ha pagato)
- Context Switcher: dopo refactoring iniziale (3 giorni extra) funziona perfettamente
- Validazioni P.IVA/CF: nessun bug trovato (validazioni server-side + client-side robuste)
- Performance: paginazione server-side da subito ha evitato problemi con dataset grandi

**Cosa migliorare**:
- Context Switcher più complesso del previsto (+3 giorni rispetto a stima)
- Multi-tenancy testing: serve più tempo dedicato (pianificare +2 giorni in Sprint 2)
- Validazioni P.IVA/CF: richiesto refactoring dopo primo tentativo (+2 giorni)
- Wireframe: ritardo di 1 settimana (pianificare creazione wireframe PRIMA di Sprint 1)

**Rischi Materializzati**:
- ⚠️ Context Switcher complessità (Sprint 3): CONFERMATO - richiesto refactoring (+3 giorni)
- ⚠️ Performance con molti dati (Sprint 4): NESSUN PROBLEMA - paginazione server-side da subito ha funzionato

**Tech Debt Identificato** (da schedulare in Sprint 5):
1. Refactoring validazioni email (codice duplicato in 3 file)
2. Ottimizzazione query dashboard contatori (cache backend 5 minuti)

### Next Steps

- ✅ Epic E2 (Anagrafiche) COMPLETA
- 📋 Iniziare Epic E3 (Framework Normativi) - dipende da E2 ✅
- 📋 Iniziare Epic E4 (Audit & Compliance) - dipende da E2 ✅
- 📋 Monitorare metriche post-release (performance, bug produzione)
- 📋 Raccogliere feedback utenti (Admin + Consulenti early adopters)
- 📋 Planning Sprint 5 (Tech debt + Epic E3 kick-off)

### Team Appreciation

Grazie al team per l'eccellente lavoro! 🎉

- Backend team: Schema database solido, multi-tenancy impeccabile
- Frontend team: UX polished, context switcher intuitivo
- QA team: Testing rigoroso ha trovato tutti i bug prima di staging
- UX Designer: Wireframe chiari, feedback loop efficace

Release 1.0 MVP: ON TRACK ✅
```

4. Cambia stato epic a **"Done"**
5. Salva e chiudi epic

- [ ] **Epic completata e chiusa** quando tutto è fatto

---

## Template Riutilizzabile per Epic Successive

Quando crei le prossime epic del progetto NIS2 (es: E3 Framework Normativi, E4 Audit, E5 Fornitori), usa questo workflow:

1. **Copia cartella deliveries**:
   ```bash
   cp -r deliveries/epica-anagrafiche deliveries/epica-framework-normativi
   ```

2. **Duplica file metadata**:
   - Salva `epic-framework-metadata.txt`
   - Salva `epic-framework-description.md`
   - Salva `epic-framework-links.txt`

3. **Adatta contenuti per nuova epic**:
   - Modifica description (Obiettivo, Scope, Ruoli, Vincoli, Deliverable)
   - Modifica metadata (Epic Name, Summary, Labels, Story Points)
   - Modifica links (user stories, ordine implementazione)

4. **Segui questa guida**: Esegui FASE 0 → FASE 5 step-by-step

### Differenze per Epic Successive

**Epic E3 - Framework Normativi**:
- **Component**: `Framework Normativi` (nuovo component)
- **Labels**: `must-have, priority-high, framework, compliance, nis2, cis`
- **Dipendenze in ingresso**: E2 (Anagrafiche) COMPLETO - framework associati ad Aziende Clienti
- **Dipendenze in uscita**: E4 (Audit) - audit valutano requisiti framework
- **Priorità**: MUST-HAVE (Release Blocker)
- **Story Points**: (da definire dopo breakdown user stories)

**Epic E4 - Audit & Compliance**:
- **Component**: `Audit & Compliance` (nuovo component)
- **Labels**: `must-have, priority-high, audit, compliance, valutazioni`
- **Dipendenze in ingresso**: E2 (Anagrafiche) + E3 (Framework) COMPLETI
- **Dipendenze in uscita**: E6 (Azioni), E7 (Reporting)
- **Priorità**: MUST-HAVE (Release Blocker)

**Epic E5 - Fornitori**:
- **Component**: `Fornitori` (nuovo component)
- **Labels**: `must-have, priority-high, fornitori, link-temporaneo, email`
- **Dipendenze in ingresso**: E2 (Anagrafiche) COMPLETO
- **Dipendenze in uscita**: E7 (Reporting - Report Qualifica Fornitori)
- **Priorità**: MUST-HAVE (Release Blocker)

**Epic E7 - Reporting**:
- **Component**: `Reporting` (nuovo component)
- **Labels**: `must-have, priority-high, reporting, pdf, csv, template`
- **Dipendenze in ingresso**: E2 (Anagrafiche) + E3 (Framework) + E4 (Audit) + E5 (Fornitori) COMPLETI
- **Dipendenze in uscita**: Nessuna (ultima epic MVP)
- **Priorità**: MUST-HAVE (Release Blocker)

---

## Domande Frequenti (FAQ) - Specifiche per Progetto NIS2

### Q1: Quante story dovrebbe contenere un'epic per progetto NIS2?

**R**: Per progetto NIS2, le epic sono **grandi e complesse** (foundation di sistema RegTech). Epic Anagrafiche ha **27 stories (99 SP)** perché copre 3 entità principali (Aziende Consulenza, Aziende Clienti, Utenti) con multi-tenancy. Epic successive saranno più piccole (10-15 stories). Se superi 30, considera split (es: "Audit - Parte 1: Creazione Audit" e "Audit - Parte 2: Valutazioni Requisiti").

---

### Q2: Come gestisco le dipendenze bloccanti tra epic NIS2?

**R**: Epic Anagrafiche (E2) è **fondazione** - blocca TUTTE le epic successive (E3, E4, E5, E6, E7). Usa link Jira "blocks":
- E2 blocks E3 (Framework dipende da Aziende Clienti)
- E2 blocks E4 (Audit dipende da Aziende + Consulenti + Utenti)
- E2 blocks E5 (Fornitori dipende da Aziende Clienti)
- E3 + E4 block E7 (Reporting dipende da Framework + Audit completati)

**Planning**: NON iniziare E3 finché E2 non è almeno al 80% (Sprint 3 completato). Testing multi-tenancy di E2 è CRITICO prima di procedere.

---

### Q3: Come gestisco story che toccano più epic (es: Dashboard in E2 e E8)?

**R**: Assegna la story all'**epic principale** (dove sta la maggior parte del lavoro) e usa link **"relates to"** per epic secondarie.

Esempio:
- Story `US-ANA-020: Dashboard Contatori` appartiene a **E2 (Anagrafiche)** (implementa contatori anagrafiche filtrati tenant)
- Ma "relates to" **E8 (Dashboard & Analytics)** (usa pattern dashboard widget replicabile per altre epic)

---

### Q4: Come gestisco multi-tenancy testing per Epic Anagrafiche?

**R**: Multi-tenancy è **CRITICO** per progetto NIS2 (conformità GDPR). Testing RIGOROSO:

**Sprint 2 (quando implementi multi-tenancy)**:
1. Test scenario: Consulente A crea Azienda Cliente X → Consulente B fa login → verifica che NON vede Azienda X in lista
2. Test scenario: Admin vede Azienda X + Y (di Consulente A e B) → verifica colonna "Consulente Assegnato" corretta
3. Test scenario: Consulente A tenta accedere a Azienda Cliente Y (di Consulente B) con URL diretto → verifica errore 403 Forbidden
4. Code review OBBLIGATORIA: Verificare TUTTE le query hanno filtro `WHERE azienda_consulenza_id = :tenant_id`

**Sprint 3 (Context Switcher)**:
1. Test scenario: Admin-Consulente di Azienda Consulenza 1 + 2 → switch contesto → verifica cambio completo dati (liste, contatori, dashboard)

---

### Q5: Context Switcher (Sprint 3) è davvero necessario o posso rimandare?

**R**: **Necessario per MVP** se hai Admin-Consulente che gestiscono **più Aziende di Consulenza** (scenario reale per consulenti freelance o piccole società). Se il tuo modello business è "1 Consulente = 1 Azienda di Consulenza", puoi rimandare a Release 2.0. Ma Epic Anagrafiche ha stimato Context Switcher in Sprint 3 perché è scenario **comune** in piattaforme multi-tenant RegTech.

**Alternativa semplificata** (se vuoi rimandare): Consulente può fare **logout + login con altro account** per cambiare azienda consulenza (UX peggiore ma funziona).

---

### Q6: Soft delete è obbligatorio per TUTTE le entità o solo alcune?

**R**: **Soft delete OBBLIGATORIO per TUTTE le entità anagrafiche** (Admin, Consulenti, Utenti Aziendali, Aziende Consulenza, Aziende Clienti, Sedi) per:
1. **Audit trail**: Preservare `created_by`, `modified_by` (altrimenti foreign key rotte)
2. **Conformità GDPR**: Tracciabilità completa operazioni (chi ha eliminato cosa e quando)
3. **Possibilità ripristino** (feature futura - non in MVP ma schema DB pronto)

**Implementazione**: Flag `deleted_at` (timestamp nullable) + `deleted_by` (foreign key a `users.id`). Query default: `WHERE deleted_at IS NULL`.

---

### Q7: Validazioni P.IVA/CF sono critiche o posso usare validazione base?

**R**: **CRITICHE per progetto NIS2** (piattaforma compliance deve essere conforme!). Implementa validazioni **server-side + client-side**:

- **P.IVA Aziende Consulenza**: 11 cifre numeriche, univoca globalmente, regex `/^\d{11}$/`
- **P.IVA/CF Aziende Clienti**: Almeno uno dei due obbligatorio, entrambi univoci se presenti
  - P.IVA: 11 cifre numeriche `/^\d{11}$/`
  - CF: 11 o 16 caratteri alfanumerici `/^[A-Z0-9]{11,16}$/`
- **Email**: Univoca globalmente (cross-tenant), case-insensitive, regex standard email

**Nota**: Per MVP, validazione **sintattica** (regex) è sufficiente. Validazione **semantica** (controllo con Agenzia Entrate API) può essere aggiunta in Release 2.0.

---

### Q8: Limiti licenza (soglie massime) sono feature must-have o nice-to-have?

**R**: **MUST-HAVE per MVP** se modello business è **licensing per numero aziende/utenti** (tipico per SaaS multi-tenant). Epic Anagrafiche ha US-ANA-021 (Sprint 3) per implementare blocco creazione al raggiungimento soglia.

**Implementazione**:
- Campi in tabella `aziende_consulenza`: `max_aziende_clienti`, `max_utenti_aziende` (integer)
- Validazione server-side: Prima di creare Azienda Cliente, verificare `COUNT(aziende_clienti WHERE azienda_consulenza_id = :id) < max_aziende_clienti`
- Messaggio errore user-friendly: "Limite aziende clienti raggiunto (50/50). Contatta l'amministratore per aumentare il limite."

Se modello business è **flat fee** (no limiti), puoi impostare `max_aziende_clienti = 9999` (infinito) o rimuovere feature.

---

### Q9: Export CSV/PDF (Sprint 4) è bloccante per Release 1.0 o posso rimandare?

**R**: **SHOULD-HAVE per MVP** (non bloccante assoluto ma importante per UX). Consulenti useranno export per:
- Report clienti (es: lista aziende clienti con dati conformità)
- Backup dati (CSV)
- Presentazioni (PDF formattato)

Se tempo stringe, **rimanda a Release 1.1** e concentrati su CRUD completo (Sprint 1-3). Ma US-ANA-024 è in Sprint 4 proprio perché è enhancement non bloccante.

---

### Q10: Devo creare TUTTE le 27 user stories in Jira prima di iniziare Sprint 1?

**R**: **NO**. Approccio consigliato per progetto grande (27 stories):

**Prima di Sprint 1**:
- Crea epic in Jira (CONF-10)
- Crea **7 stories di Sprint 1** (US-ANA-001 → US-ANA-007) con acceptance criteria completi
- Stima story points Sprint 1 (target: 21 SP)
- Assegna stories a Sprint 1 in Jira

**Durante Sprint 1** (ultimi 2 giorni):
- Crea **8 stories di Sprint 2** (US-ANA-008 → US-ANA-015)
- Stima story points Sprint 2 (target: 34 SP)

**Durante Sprint 2**:
- Crea **6 stories di Sprint 3** (US-ANA-016 → US-ANA-021)

**Durante Sprint 3**:
- Crea **6 stories di Sprint 4** (US-ANA-022 → US-ANA-027)

**Rationale**: Evitare lavoro inutile se requisiti cambiano. Just-in-time story creation riduce waste.

---

## Checklist Finale Recap

Usa questa checklist rapida per verificare di aver completato tutto:

### FASE 0: Pre-Volo

- [ ] Accesso Jira verificato
- [ ] Permessi creazione epic verificati
- [ ] Documentazione (PRD, User Stories, Ordine Implementazione) pronta
- [ ] 27 user stories disponibili (3 file: US-001, US-002, US-003)

### FASE 1: Preparazione Ambiente

- [ ] Component "Anagrafiche" creato/verificato
- [ ] Fix Version "Release 1.0 - MVP" creata/verificata
- [ ] Labels list preparata (must-have, priority-high, foundation, multi-tenancy, crud, database)
- [ ] Board configurata con swimlanes epic (opzionale)

### FASE 2: Preparazione Contenuti

- [ ] Description epic scritta e salvata (Obiettivo, Scope, Ruoli, Vincoli, Deliverable, Priorità, Dipendenze, Note)
- [ ] Lista 10 links esterni preparata (PRD, user stories, ordine implementazione, wireframe, flow diagram, vincoli progetto, DB Access)
- [ ] Metadata epic preparata (Epic Name, Summary, Priority Highest, Labels, Component, Fix Version, Assignee, 99 SP)

### FASE 3: Creazione Epic

- [ ] Form creazione epic compilato con tutti i campi
- [ ] Epic creata con successo (Epic Key annotato: CONF-10)

### FASE 4: Collegamento Links e Stories

- [ ] 10 links esterni aggiunti all'epic (8 obbligatori + 2 placeholder wireframe/flow)
- [ ] 27 user stories collegate all'epic (US-ANA-001 → US-ANA-027)
- [ ] User stories ordinate per priorità (sequenza Sprint 1 → 2 → 3 → 4)
- [ ] Relazioni tra epic create: E2 relates to E1, E2 blocks E3/E4/E5/E6/E7 (se epic esistono)

### FASE 5: Verifica Finale

- [ ] Checklist completezza epic verificata (16 items)
- [ ] 4 Filtri Jira creati (All Stories, Sprint 1-4, Release 1.0, Must-Have)
- [ ] Dashboard epic creata con 4 gadget (opzionale)
- [ ] PRD aggiornato con sezione Tracciabilità Jira
- [ ] Team notificato via email/Slack/Teams

### FASE 6: Manutenzione (Durante Sviluppo)

- [ ] Epic aggiornata settimanalmente con status update
- [ ] Deliverable checklist aggiornata dopo ogni milestone
- [ ] Epic chiusa quando tutte le 27 stories completate + testing passato + deploy staging OK

---

## Risorse Aggiuntive

### Documentazione Jira

- **Jira Epic Documentation**: [https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/](https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/)
- **JQL Reference**: [https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- **Epic Planning Best Practices**: [https://www.atlassian.com/agile/project-management/epics](https://www.atlassian.com/agile/project-management/epics)

### Documentazione Progetto NIS2

- **Documento Vincoli di Progetto**: `research/documento_vincolo_di_progetto_piattaforma_conformità_ni2.md`
- **CLAUDE.md** (Context file): `CLAUDE.md` (contiene overview progetto, design principles, constraints)
- **Database Access Legacy**: `research/old_piattaforma_conformità_nis2.accdb`
- **Script Lettura Access**: `research/read_access.py`

---

## Conclusione

Hai completato la guida step-by-step per creare l'Epic "Gestione Anagrafiche" (E2) in Jira per la Piattaforma Conformità NIS2/CIS!

### Vantaggi di questo approccio

- **Zero interruzioni**: Tutto preparato in anticipo (description, links, metadata), creazione epic veloce (5-10 min)
- **Tracciabilità completa**: 10 links a documenti, dipendenze chiare tra epic (E2 blocks E3/E4/E5/E6/E7), metadata strutturati
- **Ripetibile**: Template riutilizzabile per epic successive (E3 Framework, E4 Audit, E5 Fornitori, E6 Azioni, E7 Reporting)
- **Specifico per NIS2**: Tutti gli esempi basati sul vostro progetto reale (27 stories, multi-tenancy, context switcher, limiti licenza)
- **Collaborativo**: Team ha visibilità completa su scope (Aziende Consulenza + Aziende Clienti + Utenti + Sedi), priorità (MUST-HAVE Highest), dipendenze (blocca 5 epic successive), roadmap (4 sprint, 99 SP, 38-46 giorni)

### Prossimi passi

1. **Crea Epic Anagrafiche (E2)** seguendo questa guida (tempo stimato: 45-60 minuti con preparazione completa)
2. **Crea 7 user stories Sprint 1** (US-ANA-001 → US-ANA-007) in Jira con acceptance criteria completi
3. **Sprint Planning Sprint 1**: Stima story points (target: 21 SP), assegna stories a sprint, kickoff sviluppo
4. **Crea wireframe** (Aziende Consulenza, Aziende Clienti, Utenti, Sedi, Context Switcher) - pianifica 1 settimana con UX Designer
5. **Crea epic successive** usando questa guida come template:
   - E1 (Autenticazione) - parallelo a E2
   - E3 (Framework Normativi) - dopo E2 Sprint 3 completato (80%)
   - E4 (Audit) - dopo E2 + E3 completati
   - E5 (Fornitori) - dopo E2 completato
   - E6 (Azioni) - dopo E2 + E4 completati
   - E7 (Reporting) - ultima epic MVP (dopo E2/E3/E4/E5 completati)

### Metriche Successo Epic Anagrafiche

Al completamento dei 4 sprint (38-46 giorni), il sistema deve:

✅ **Gestione Utenti**: 3 tipi creabili (Admin, Consulenti, Utenti Aziendali), lista unificata, soft delete
✅ **Gestione Aziende Consulenza**: CRUD completo, gestione consulenti, validazione vincoli eliminazione, filtri/ricerche
✅ **Gestione Aziende Clienti**: CRUD completo, sedi (≥1 principale), utenti aziendali, multi-consulente, context switcher, export CSV/PDF
✅ **Multi-Tenancy**: Segregazione dati rigorosa (Consulente vede SOLO propri dati), Admin vede tutto
✅ **Validazioni**: P.IVA univoca, CF univoco, Email univoca, vincoli eliminazione (no dati collegati)
✅ **UX**: Filtri avanzati, paginazione (8/16/24), debounce 300ms, modal/dialog consistenti, notifiche toast
✅ **Performance**: Paginazione server-side, debounce, lazy loading (>1000 record), query <2s

Buon lavoro con la Piattaforma Conformità NIS2/CIS! 🚀

---

_Guida creata per: Progetto alfredo-nis2 - Piattaforma Conformità NIS2/CIS_
_Epic: E2 - Gestione Anagrafiche_
_Team: 6/7 persone_
_Product Owner: Nautes_
_Versione: 2.0 (Specifica per progetto NIS2)_
_Data: 2025-12-11_
_Ultima revisione: 2025-12-11_
