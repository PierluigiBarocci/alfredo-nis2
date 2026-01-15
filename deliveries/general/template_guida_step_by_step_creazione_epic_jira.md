# Guida Step-by-Step: Creazione Epic in Jira (Zero Sorprese)

**Versione**: 1.0
**Data**: 2025-12-11
**Caso d'uso**: Creazione Epic "Anagrafiche" (primo esempio pratico)

---

## Introduzione

Questa guida ti accompagna nella creazione di un'Epic in Jira **dall'inizio alla fine senza sorprese**.

A differenza di guide generiche, questa:
- **Prevede TUTTO in anticipo**: niente "ah, serve anche questo" a meta strada
- **Non ti fa buttare lavoro**: prima prepari tutto, poi crei l'epic
- **E' sequenziale**: ogni step dipende dal precedente, niente salti
- **Ha checkbox**: spunta ogni voce per tracciare progresso

---

## Struttura della Guida

La guida e divisa in **5 FASI**:

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
- [ ] **Progetto Jira esistente**: Esiste un progetto configurato (es: "CONF - Piattaforma conformita NIS2/CIS")
- [ ] **Permessi di creazione**: Puoi creare Issue tipo "Epic" nel progetto
- [ ] **Permessi di configurazione**: Puoi creare/modificare Components, Labels, Fix Versions (o hai contatto admin che puo farlo)

**Come verificare permessi**:
1. Vai al tuo progetto Jira
2. Click su **"Create"** (pulsante blu in alto)
3. Nel campo **"Issue Type"**, verifica che esista opzione **"Epic"**
4. Se vedi "Epic", hai i permessi. Chiudi il dialog senza salvare.

**Se NON hai permessi**: Contatta l'admin Jira e richiedi permessi "Create Issue" e "Project Administrator" (o almeno "Manage Components/Versions")

---

### Verifica Documentazione Disponibile

Prima di creare l'epic, devi avere questi documenti pronti (o sapere dove trovarli):

- [ ] **PRD o Documento Requisiti**: Documento che descrive funzionalita dell'epic (es: `deliveries/epica-anagrafiche/`)
- [ ] **User Stories**: Lista user stories da collegare all'epic (es: `US-ANA-001.md`, `US-ANA-002.md`, etc.)
- [ ] **Ordine Implementazione**: Documento che definisce priorita e dipendenze (es: `ORDINE-IMPLEMENTAZIONE.md`)
- [ ] **Wireframe/Mockup** (opzionale): Link Figma/Sketch/PDF con mockup UI
- [ ] **Flow Diagram** (opzionale): Link Miro/Lucidchart con diagrammi flusso

**Esempio per Epic Anagrafiche**:
- PRD: `C:\Users\pierl\Documents\Work\alfredo-nis2\deliveries\epica-anagrafiche\`
- User Stories: 27 file `US-ANA-001.md` → `US-ANA-027.md`
- Ordine: `ORDINE-IMPLEMENTAZIONE.md`

**Se manca documentazione**: FERMATI. Non creare epic senza requisiti chiari. Scrivi prima PRD/User Stories, poi torna qui.

---

## FASE 1: Preparazione Ambiente Jira

**Obiettivo**: Creare/verificare che Components, Labels, Fix Versions esistano PRIMA di creare l'epic.

### Step 1.1: Verifica/Crea Components

**Cosa sono i Components**: Categorie funzionali del progetto (es: "Anagrafiche", "Autenticazione", "Audit", etc.)

**Perche servono prima**: Quando crei l'epic, dovrai selezionare un Component dal dropdown. Se non esiste, dovrai abbandonare la creazione dell'epic per crearlo.

#### Come Verificare Components Esistenti

1. Vai al tuo progetto Jira
2. Click su **Settings** (icona ingranaggio in basso a sinistra) → **"Components"**
3. Verifica se esiste il component per la tua epic

**Per Epic Anagrafiche**: Verifica se esiste component **"Anagrafiche"**

#### Come Creare Nuovo Component

Se il component NON esiste:

1. Nella pagina "Components", click **"Create Component"**
2. Compila il form:
   - **Name**: `Anagrafiche` (nome component)
   - **Description**: `Gestione anagrafiche utenti, aziende consulenza e aziende clienti`
   - **Component Lead**: Lascia vuoto o seleziona te stesso
   - **Default Assignee**: Seleziona "Component Lead" o "Project Default"
3. Click **"Save"**

**Checklist Components per Progetto Completo** (crea quelli che ti servono):

- [ ] **Anagrafiche** - Gestione utenti e aziende
- [ ] **Autenticazione & Sicurezza** - Login, password reset, sessioni
- [ ] **Framework Normativi** - Gestione framework NIS2/CIS
- [ ] **Audit & Compliance** - Gestione audit e valutazioni conformita
- [ ] **Fornitori** - Processo qualifica fornitori
- [ ] **Reporting** - Generazione report PDF/CSV
- [ ] **Dashboard** - Dashboard e KPI
- [ ] **Sistema** - Notifiche, configurazioni, logging

---

### Step 1.2: Verifica/Crea Fix Versions

**Cosa sono le Fix Versions**: Milestone o release del progetto (es: "Release 1.0", "Release 2.0", "MVP")

**Perche servono prima**: Quando crei l'epic, dovrai selezionare una Fix Version dal dropdown.

#### Come Verificare Fix Versions Esistenti

1. Vai al tuo progetto Jira
2. Click su **Settings** (icona ingranaggio) → **"Releases"** (o "Versions")
3. Verifica se esiste la release per la tua epic

**Per Epic Anagrafiche**: Verifica se esiste release **"Release 1.0"** o **"MVP"**

#### Come Creare Nuova Fix Version

Se la release NON esiste:

1. Nella pagina "Releases", click **"Create Version"**
2. Compila il form:
   - **Name**: `Release 1.0` (nome release)
   - **Start Date**: Data inizio sviluppo (es: 2025-12-11)
   - **Release Date**: Data rilascio prevista (es: 2026-02-15)
   - **Description**: `Prima release MVP con funzionalita core`
3. Click **"Save"**

**Checklist Fix Versions Suggerite**:

- [ ] **Release 1.0** - MVP con funzionalita core (Anagrafiche, Autenticazione, Framework, Audit base)
- [ ] **Release 2.0** - Enhancement (Fornitori, Report avanzati, Dashboard avanzate)
- [ ] **Release 3.0** - Evoluzioni future (Multi-lingua, Mobile, Integrazioni)

---

### Step 1.3: Prepara Lista Labels

**Cosa sono i Labels**: Tag liberi per categorizzare issue (es: "must-have", "priority-high", "security")

**Perche prepararli prima**: I labels si possono creare al volo, MA e meglio avere una lista standard per consistenza.

**Labels Standard Consigliati** (copia questa lista, la userai dopo):

```
must-have, should-have, nice-to-have, priority-high, priority-medium, priority-low, security, authentication, audit, reporting, compliance, frontend, backend, database, foundation, enhancement, bug, technical-debt
```

**Per Epic Anagrafiche**: Userai questi labels:
```
must-have, priority-high, foundation, database, multi-tenancy, crud
```

**Nota**: I labels NON vanno creati in anticipo in Jira (si creano quando li usi la prima volta). Questa lista e solo per avere naming consistente.

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

**Perche scrivere prima**: La description e lunga (200-500 righe). Scriverla nel form Jira e scomodo. Meglio prepararla in un editor esterno (VSCode, Notepad++) e poi fare copy-paste.

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

- **Admin**: [Cosa puo fare]
- **Consulente**: [Cosa puo fare]
- **Azienda**: [Cosa puo fare]
- **Fornitore**: [Cosa puo fare o se escluso]

## Vincoli Tecnici

- [Vincolo 1]
- [Vincolo 2]
- [Vincolo 3]

## Deliverable Attesi

- [ ] PRD sezione [Nome]
- [ ] User stories dettagliate con acceptance criteria (27 stories)
- [ ] Ordine implementazione e roadmap sprint
- [ ] Wireframe pagine CRUD [Entita]
- [ ] Matrice tracciabilita requisiti

## Priorita

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

#### Esempio Compilato per Epic Anagrafiche

Salva questo in `epic-anagrafiche-description.md`:

```markdown
## Obiettivo

Implementare la gestione completa delle anagrafiche per utenti (Admin, Consulenti, Utenti Aziendali), aziende di consulenza e aziende clienti, con supporto multi-tenancy e segregazione dati rigorosa.

## Scope Funzionale

Questa epic copre:
- Gestione utenti piattaforma (Admin, Consulenti, Utenti Aziendali)
- Gestione aziende di consulenza con consulenti collegati
- Gestione aziende clienti con sedi aziendali e utenti aziendali
- Multi-tenancy logico con segregazione dati per consulente
- Scenario multi-consulente (azienda cliente assegnata a piu consulenti)
- Context switcher per Admin-Consulente che gestisce piu aziende di consulenza
- CRUD completo per tutte le entita anagrafiche
- Validazioni P.IVA/CF univoche
- Soft delete con preservazione audit trail
- Filtri e ricerche avanzate
- Export liste (CSV/PDF)
- Contatori dashboard filtrati per tenant
- Gestione soglie massime entita (limite creazioni)

**Escluso da questa epic:**
- Autenticazione e login (epic separata)
- Gestione framework normativi (epic separata)
- Gestione audit e compliance (epic separata)
- Processo qualifica fornitori (epic separata)

## Ruoli Coinvolti

- **Admin**: Accesso completo a tutte le anagrafiche (Aziende Consulenza, Aziende Clienti, Utenti). Puo creare/modificare/eliminare qualsiasi entita. Vede dati globali senza filtri tenant.
- **Consulente**: Accesso filtrato alle proprie aziende clienti e relativi utenti aziendali. Puo gestire CRUD aziende clienti assegnate. Vede solo dati del proprio tenant.
- **Admin-Consulente**: Consulente con ruolo admin in un'azienda di consulenza. Puo gestire consulenti della propria azienda. Se associato a piu aziende di consulenza, usa context switcher.
- **Azienda (Admin Cliente)**: Accesso viewer ai dati della propria azienda cliente. NON gestisce anagrafiche (funzionalita esclusa per questo ruolo in questa epic).
- **Fornitore**: ESCLUSO da questa epic (accesso tramite link temporaneo gestito in epic separata)

## Vincoli Tecnici

- Multi-tenancy logico con tabelle relazionali (non database separati)
- P.IVA obbligatoria e univoca per Aziende Consulenza
- P.IVA o CF obbligatorio per Aziende Clienti (almeno uno dei due, univoci)
- Email univoca per tutti gli utenti (across all tenant)
- Soft delete per tutte le entita (nessuna eliminazione fisica)
- Almeno 1 sede principale obbligatoria per Azienda Cliente
- Validazione vincoli eliminazione (blocco se ci sono dati collegati)
- Almeno 1 Admin piattaforma sempre presente (no eliminazione ultimo Admin)
- Soglie massime configurabili per numero entita (Aziende, Utenti)

## Deliverable Attesi

- [ ] PRD sezione Anagrafiche completa
- [ ] User stories dettagliate con acceptance criteria (27 stories: US-ANA-001 → US-ANA-027)
- [ ] Ordine implementazione e roadmap 4 sprint
- [ ] Wireframe pagine CRUD Aziende Consulenza, Aziende Clienti, Utenti
- [ ] Wireframe modal gestione Sedi, Consulenti, Utenti Aziendali
- [ ] Flow diagram multi-tenancy e context switcher
- [ ] Matrice tracciabilita requisiti (vincoli → stories)

## Priorita

**MUST-HAVE (Release blocker)** - Le anagrafiche sono la fondazione del sistema. Senza utenti e aziende configurati, nessun'altra funzionalita (audit, framework, fornitori) puo essere utilizzata. Questa epic blocca tutte le epic successive.

## Dipendenze

- **Dipendenze in ingresso**:
  - Epic Autenticazione (E1) - necessaria per login utenti e gestione sessioni
- **Dipendenze in uscita**:
  - Epic Framework Normativi (E3) - i framework sono associati ad Aziende Clienti
  - Epic Audit (E4) - gli audit sono creati per Aziende Clienti da Consulenti
  - Epic Fornitori (E5) - i fornitori sono associati ad Aziende Clienti

## Note

- **Sprint Planning**: Epic suddivisa in 4 sprint logici (Foundation, Multi-Tenancy Core, Advanced Multi-Consulente, Enhancement & Polish)
- **Testing critico**: Multi-tenancy deve essere testata rigorosamente (Consulente A non deve vedere dati Consulente B)
- **Context Switcher**: Feature complessa, implementare in story separata (US-ANA-017) con testing approfondito
- **Performance**: Con >1000 record, implementare paginazione server-side e debounce su ricerche
- **Coordinamento**: Questa epic richiede coordinamento con team UX per wireframe e team backend per schema database

---

**Epic collegata a:**
- Milestone: Release 1.0
- Componente: Anagrafiche
- Label: must-have, priority-high, foundation, multi-tenancy, crud, database
```

- [ ] **Description epic scritta e salvata** in file testo

---

### Step 2.2: Prepara Lista Links Esterni

**Obiettivo**: Preparare URL a documentazione esterna (PRD, wireframe, flow diagram) da collegare all'epic.

Crea una lista di link in un file testo (es: `epic-anagrafiche-links.txt`):

```
LINKS DA AGGIUNGERE ALL'EPIC

1. PRD Anagrafiche
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/
   Title: PRD - Gestione Anagrafiche

2. User Stories
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/
   Title: User Stories Anagrafiche (US-ANA-001 → US-ANA-027)

3. Ordine Implementazione
   URL: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/ORDINE-IMPLEMENTAZIONE.md
   Title: Roadmap 4 Sprint - Ordine Implementazione

4. Wireframe (PLACEHOLDER - aggiornare quando disponibile)
   URL: https://figma.com/link-to-wireframe
   Title: Wireframe Anagrafiche

5. Flow Diagram (PLACEHOLDER - aggiornare quando disponibile)
   URL: https://miro.com/link-to-flow
   Title: Flow Diagram Multi-Tenancy & Context Switcher
```

**Nota**: I link `file://` funzionano solo se Jira e in locale o su rete condivisa. Per team remoti, usa link a repository Git (es: GitHub/GitLab) o documenti condivisi (Google Docs, Confluence).

**Alternativa link Git** (se il progetto e su GitHub):

```
1. PRD Anagrafiche
   URL: https://github.com/your-org/alfredo-nis2/tree/main/deliveries/epica-anagrafiche
   Title: PRD - Gestione Anagrafiche
```

- [ ] **Lista links preparata** in file testo

---

### Step 2.3: Prepara Metadata Epic

**Obiettivo**: Decidere valori per campi Epic Name, Summary, Priority, Labels, Component, Fix Version.

Compila questa tabella (salva in file testo `epic-anagrafiche-metadata.txt`):

```
METADATA EPIC ANAGRAFICHE

Epic Name (breve):
Gestione Anagrafiche

Summary (titolo completo):
E2 - Gestione Anagrafiche (Utenti, Aziende Consulenza, Aziende Clienti)

Priority:
Highest

Labels (separati da virgola):
must-have, priority-high, foundation, multi-tenancy, crud, database

Component:
Anagrafiche

Fix Version:
Release 1.0

Assignee:
[Il tuo nome o "Product Owner"]

Reporter:
[Il tuo nome - auto-compilato da Jira]
```

**Convenzione Naming Epic**:
- **Epic Name**: Breve (2-4 parole) - es: "Gestione Anagrafiche"
- **Summary**: `E[N] - [Titolo Descrittivo]` - es: "E2 - Gestione Anagrafiche (Utenti, Aziende Consulenza, Aziende Clienti)"
  - `E1` = Autenticazione
  - `E2` = Anagrafiche
  - `E3` = Framework Normativi
  - `E4` = Audit
  - `E5` = Fornitori

- [ ] **Metadata epic preparata** in file testo

---

## FASE 3: Creazione Epic in Jira

**Obiettivo**: Creare l'epic in Jira compilando il form con i contenuti preparati in FASE 2.

**IMPORTANTE**: Ora che hai preparato TUTTO, la creazione dell'epic sara veloce (5-10 minuti). Tieni aperti i file con description, links e metadata.

---

### Step 3.1: Aprire Form Creazione Epic

1. Vai al tuo progetto Jira
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
E2 - Gestione Anagrafiche (Utenti, Aziende Consulenza, Aziende Clienti)
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

Nel form Jira, nel campo **"Priority"**, seleziona dal dropdown **"Highest"** (o equivalente nel tuo schema Jira: "Critical", "P0", etc.)

- [ ] **Priority impostata su Highest**

---

#### Campo: Labels

Copia da `epic-anagrafiche-metadata.txt` il valore **Labels**:

```
must-have, priority-high, foundation, multi-tenancy, crud, database
```

Nel form Jira, nel campo **"Labels"**:

1. Clicca nel campo
2. Digita il primo label: `must-have`
3. Premi **Enter** (il label viene aggiunto)
4. Digita il secondo label: `priority-high`
5. Premi **Enter**
6. Continua per tutti i label

**Nota**: Se il label non esiste, Jira ti proporra di crearlo. Click su "Create label must-have".

- [ ] **Tutti i labels aggiunti**

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
Release 1.0
```

Nel form Jira, nel campo **"Fix Version"** (o "Release"), seleziona dal dropdown **"Release 1.0"**.

**Se la release NON appare nel dropdown**: Significa che non hai completato Step 1.2. FERMA qui.

1. Click **"Cancel"** per chiudere il form (salva description prima!)
2. Torna a Step 1.2 e crea la release
3. Poi ritorna qui e riapri il form

- [ ] **Fix Version selezionata**

---

#### Campo: Assignee

Copia da `epic-anagrafiche-metadata.txt` il valore **Assignee** (o seleziona te stesso).

Nel form Jira, nel campo **"Assignee"**, digita il nome dell'utente e seleziona dal dropdown.

**Consiglio**: Assegna a Product Owner o Delivery Manager (chi gestisce il backlog).

- [ ] **Assignee impostato**

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
```

Questo key ti servira per collegare le user stories (FASE 4).

- [ ] **Epic creata con successo**
- [ ] **Epic Key annotato**

---

## FASE 4: Collegamento Links e User Stories

**Obiettivo**: Aggiungere links esterni all'epic e collegare le user stories.

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
   - **URL**: Incolla URL da `epic-anagrafiche-links.txt` (es: `file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/`)
   - **Title**: Incolla Title (es: `PRD - Gestione Anagrafiche`)
4. Click **"Link"**

Ripeti per tutti i link preparati in Step 2.2:

- [ ] **Link 1: PRD Anagrafiche** aggiunto
- [ ] **Link 2: User Stories** aggiunto
- [ ] **Link 3: Ordine Implementazione** aggiunto
- [ ] **Link 4: Wireframe** aggiunto (se disponibile, altrimenti segna come TODO)
- [ ] **Link 5: Flow Diagram** aggiunto (se disponibile, altrimenti segna come TODO)

**Nota**: Se wireframe/flow non sono ancora pronti, aggiungi link placeholder e aggiornali dopo.

---

### Step 4.3: Collegare User Stories all'Epic

**Scenario**: Hai gia creato le user stories come Issue tipo "Story" in Jira, e ora vuoi collegarle all'epic.

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

**Per Epic Anagrafiche**: Collega le 27 user stories `US-ANA-001` → `US-ANA-027`.

**Consiglio**: Se hai molte story, usa bulk add (Metodo 2) per risparmiare tempo.

- [ ] **User stories collegate all'epic** (tutte le 27 stories per Epic Anagrafiche)

---

### Step 4.4: Creare User Stories Nuove Collegate all'Epic

**Scenario**: Non hai ancora creato le user stories, vuoi crearle ora e collegarle direttamente all'epic.

#### Come Creare Story Collegata all'Epic

1. Click su **"Create"** in Jira
2. Nel campo **"Issue Type"**, seleziona **"Story"**
3. Nel campo **"Epic Link"**, seleziona `CONF-10 - Gestione Anagrafiche` (l'epic che hai appena creato)
4. Compila il campo **"Summary"** con il nome della story (es: `US-ANA-001: Creare Admin Piattaforma`)
5. Compila il campo **"Description"** con il contenuto della user story (template: "Come [ruolo] Voglio [azione] In modo che [beneficio]" + Acceptance Criteria)
6. Compila campi aggiuntivi:
   - **Priority**: es: `High`
   - **Labels**: es: `must-have, admin, crud, foundation`
   - **Component**: es: `Anagrafiche` (stesso component dell'epic)
   - **Fix Version**: es: `Release 1.0` (stesso fix version dell'epic)
7. Click **"Create"**

Ripeti per tutte le user stories dell'epic.

**Per Epic Anagrafiche**: Crea 27 user stories (vedi file `US-ANA-001.md` → `US-ANA-027.md` per contenuti).

**Consiglio**: Crea prima 2-3 story per sprint 1, poi continua con le altre man mano.

- [ ] **User stories create e collegate all'epic**

---

### Step 4.5: Ordinare User Stories per Priorita

**Obiettivo**: Le story nell'epic devono essere ordinate per priorita implementazione (quelle da fare prima in alto).

#### Come Riordinare Story nell'Epic

**Metodo 1: Drag & Drop nella Board**

1. Vai alla Board Kanban/Scrum del progetto
2. Se hai configurato swimlanes per epic (Step 1.4), vedrai le story raggruppate sotto l'epic
3. Drag & Drop le story per riordinarle (prima story = priorita piu alta)

**Metodo 2: Riordino da Backlog**

1. Vai al **"Backlog"** del progetto
2. Filtra per epic: seleziona `CONF-10 - Gestione Anagrafiche`
3. Drag & Drop le story nell'ordine desiderato

**Per Epic Anagrafiche**: Ordina le 27 story secondo `ORDINE-IMPLEMENTAZIONE.md`:

1. US-ANA-001 (Creare Admin)
2. US-ANA-002 (Modificare Admin)
3. US-ANA-003 (Eliminare Admin)
4. US-ANA-004 (Lista Aziende Consulenza)
5. ... (continua secondo ordine implementazione)

- [ ] **User stories ordinate per priorita**

---

### Step 4.6: Creare Relazioni tra Epic (se applicabile)

**Obiettivo**: Se la tua epic dipende da altre epic o blocca altre epic, crea link espliciti.

#### Come Creare Link tra Epic

1. Nella pagina dettaglio epic (`CONF-10`), cerca sezione **"Links"**
2. Click su **"Link"** → **"Jira Issue"**
3. Seleziona tipo relazione:
   - **"is blocked by"**: Questa epic e bloccata da altra epic (es: Epic Anagrafiche e bloccata da Epic Autenticazione)
   - **"blocks"**: Questa epic blocca altra epic (es: Epic Anagrafiche blocca Epic Audit)
   - **"relates to"**: Epic collegate ma non bloccanti (es: Epic Anagrafiche relates to Epic Framework)
4. Nel campo **"Issue"**, digita l'epic key o nome (es: `CONF-5` = Epic Autenticazione)
5. Click **"Link"**

**Per Epic Anagrafiche**:

- **Dipendenze IN ingresso** (questa epic e bloccata da):
  - `CONF-5` Epic Autenticazione (E1) - necessaria per login utenti

- **Dipendenze IN uscita** (questa epic blocca):
  - `CONF-15` Epic Framework Normativi (E3)
  - `CONF-20` Epic Audit (E4)
  - `CONF-25` Epic Fornitori (E5)

**Nota**: Se le altre epic non esistono ancora, salta questo step e aggiungi i link dopo quando le creerai.

- [ ] **Relazioni tra epic create** (se epic dipendenti esistono)

---

## FASE 5: Verifica Finale e Post-Creazione

**Obiettivo**: Verificare che l'epic sia completa e configurare filtri/dashboard.

### Step 5.1: Checklist Completezza Epic

Apri la pagina dettaglio dell'epic e verifica:

- [ ] **Epic Name** breve e chiaro (es: "Gestione Anagrafiche")
- [ ] **Summary** con convenzione `E[N] - [Titolo]` (es: "E2 - Gestione Anagrafiche (Utenti, Aziende Consulenza, Aziende Clienti)")
- [ ] **Description** completa con:
  - [ ] Obiettivo
  - [ ] Scope Funzionale (incluso + escluso)
  - [ ] Ruoli Coinvolti
  - [ ] Vincoli Tecnici
  - [ ] Deliverable Attesi (con checkbox)
  - [ ] Priorita + motivazione
  - [ ] Dipendenze (in ingresso + uscita)
  - [ ] Note
- [ ] **Priority** impostata (es: Highest)
- [ ] **Labels** configurati (es: must-have, priority-high, foundation, multi-tenancy, crud, database)
- [ ] **Component** assegnato (es: Anagrafiche)
- [ ] **Fix Version** = "Release 1.0" (o release appropriata)
- [ ] **Assignee** impostato (Product Owner o Delivery Manager)
- [ ] **Sprint** lasciato vuoto (corretto - epic non vanno in sprint)
- [ ] **Links esterni** aggiunti:
  - [ ] Link PRD
  - [ ] Link User Stories
  - [ ] Link Ordine Implementazione
  - [ ] Link Wireframe (o placeholder)
  - [ ] Link Flow Diagram (o placeholder)
- [ ] **Relazioni con altre epic** create (se esistono epic dipendenti)
- [ ] **User Stories collegate** all'epic (27 stories per Epic Anagrafiche)
- [ ] **User Stories ordinate** per priorita implementazione

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
4. Nome filtro: `Epic Anagrafiche - All Stories`
5. Descrizione: `Tutte le user stories dell'epic Gestione Anagrafiche`
6. Check **"Add to favorites"** (opzionale)
7. Click **"Submit"**

- [ ] **Filtro "Epic Anagrafiche - All Stories" creato**

---

#### Filtro 2: Story Epic Anagrafiche - Sprint 1

1. Query JQL:

```jql
project = "CONF" AND "Epic Link" = CONF-10 AND labels = "sprint-1" ORDER BY priority DESC
```

(Presuppone che tu abbia aggiunto label `sprint-1` alle story del primo sprint. Se non l'hai fatto, salta questo filtro.)

2. Salva come: `Epic Anagrafiche - Sprint 1`

- [ ] **Filtro "Epic Anagrafiche - Sprint 1" creato** (opzionale)

---

#### Filtro 3: Tutte le Epic Release 1.0

1. Query JQL:

```jql
project = "CONF" AND issuetype = Epic AND fixVersion = "Release 1.0" ORDER BY priority DESC, created ASC
```

2. Salva come: `Epic Release 1.0 - All`

- [ ] **Filtro "Epic Release 1.0 - All" creato**

---

#### Filtro 4: Epic Must-Have

1. Query JQL:

```jql
project = "CONF" AND issuetype = Epic AND labels = "must-have" ORDER BY priority DESC
```

2. Salva come: `Epic Must-Have`

- [ ] **Filtro "Epic Must-Have" creato**

---

### Step 5.3: Aggiungere Epic a Dashboard (Opzionale)

**Obiettivo**: Creare gadget dashboard per monitorare progresso epic.

#### Come Creare Dashboard per Epic

1. Vai a **"Dashboards"** → **"Create Dashboard"**
2. Nome: `Epic Anagrafiche - Progress`
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

- [ ] **Dashboard epic creata con gadget** (opzionale)

---

### Step 5.4: Aggiornare Documentazione Esterna

**Obiettivo**: Aggiornare PRD e file README con link all'epic Jira.

#### Aggiungere Link Jira al PRD

Apri il file PRD (es: `deliveries/epica-anagrafiche/README.md`) e aggiungi sezione:

```markdown
## Tracciabilita Jira

- **Epic Jira**: [CONF-10 - E2 Gestione Anagrafiche](https://your-jira.atlassian.net/browse/CONF-10)
- **User Stories**:
  - [CONF-20] US-ANA-001: Creare Admin Piattaforma
  - [CONF-21] US-ANA-002: Modificare Admin Piattaforma
  - [CONF-22] US-ANA-003: Eliminare Admin Piattaforma con validazione vincoli
  - [CONF-23] US-ANA-004: Visualizzare lista aziende di consulenza (Admin)
  - ... (continua per tutte le 27 stories)
```

**Nota**: Sostituisci `your-jira.atlassian.net` con l'URL del tuo Jira aziendale.

- [ ] **PRD aggiornato con link Jira**

---

### Step 5.5: Notificare Team

**Obiettivo**: Comunicare al team che l'epic e stata creata e e pronta per planning.

#### Email/Messaggio al Team

Copia questo template e invia al team:

```
Oggetto: Epic "Gestione Anagrafiche" creata in Jira - Pronta per Planning

Ciao team,

Ho creato l'epic "Gestione Anagrafiche" in Jira:

Epic Key: CONF-10
Epic Name: E2 - Gestione Anagrafiche (Utenti, Aziende Consulenza, Aziende Clienti)
Epic URL: https://your-jira.atlassian.net/browse/CONF-10

Dettagli:
- 27 user stories collegate (US-ANA-001 → US-ANA-027)
- Priorita: MUST-HAVE (Release blocker)
- Fix Version: Release 1.0
- Component: Anagrafiche

Roadmap implementazione:
- Sprint 1: Foundation (7 stories) - Admin & Aziende Consulenza Base
- Sprint 2: Multi-Tenancy Core (8 stories) - Aziende Clienti & Sedi
- Sprint 3: Advanced Multi-Consulente (6 stories) - Context Switcher
- Sprint 4: Enhancement & Polish (6 stories) - Filtri, Ricerche, Export

Documentazione:
- PRD: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/
- Ordine Implementazione: file://C:/Users/pierl/Documents/Work/alfredo-nis2/deliveries/epica-anagrafiche/ORDINE-IMPLEMENTAZIONE.md

Prossimi passi:
1. Review epic description e user stories
2. Sprint Planning per Sprint 1 (7 stories da stimare)
3. Kick-off sviluppo settimana prossima

Domande? Rispondete a questa email o scrivetemi su Slack.

Grazie!
[Il tuo nome]
```

- [ ] **Team notificato** via email/Slack/Teams

---

## FASE 6: Manutenzione Epic (Durante Sviluppo)

**Obiettivo**: Mantenere l'epic aggiornata durante lo sviluppo.

### Durante lo Sviluppo

**Ogni settimana** (o dopo ogni sprint):

1. **Aggiorna checklist Deliverable** nella description epic:
   - Spunta `[x]` i deliverable completati
   - Esempio: `[x] PRD sezione Anagrafiche completa`

2. **Aggiungi commento status update** nell'epic:

```markdown
## Status Update - Week 50/2025 - Sprint 1 Complete

**Progress**:
- Completate: US-ANA-001, US-ANA-002, US-ANA-003, US-ANA-004, US-ANA-005, US-ANA-006, US-ANA-007
- In corso: Nessuna
- In backlog: US-ANA-008 → US-ANA-027 (20 stories)

**Blocchi**:
- Nessuno

**Prossimi Passi**:
- Sprint 2 kick-off lunedi 2025-12-18
- Iniziare US-ANA-008 (Gestire consulenti)

**Rischi**:
- Nessuno

**Story Points**:
- Consumati: 21/99
- Remaining: 78
- Velocita: 21 SP/sprint
- Stima completamento: 4 sprint (~8 settimane)
```

3. **Aggiorna links** se cambiano URL (es: wireframe finalmente pronti)

4. **Traccia blocchi** con link a issue bloccanti (es: "US-ANA-008 bloccata da bug CONF-50")

- [ ] **Epic aggiornata settimanalmente** durante sviluppo

---

### Quando Completare Epic

L'epic si considera **COMPLETA** quando:

1. **Tutte le user stories** collegate sono in stato "Done"
2. **Tutti i deliverable** nella checklist sono spuntati `[x]`
3. **Test E2E** superati per tutti i flussi principali
4. **Deploy su staging** completato e smoke test passanti
5. **Documentazione** aggiornata (API docs, README, changelog)

**Come chiudere epic**:

1. Apri epic in Jira
2. Click **"Workflow"** → **"Done"** (o equivalente)
3. Aggiungi commento finale:

```markdown
## Epic Completata - 2025-01-31

Tutte le 27 user stories completate con successo.

**Deliverable**:
- [x] PRD sezione Anagrafiche completa
- [x] User stories dettagliate (27 stories)
- [x] Ordine implementazione e roadmap
- [x] Wireframe CRUD Aziende Consulenza, Aziende Clienti, Utenti
- [x] Flow diagram multi-tenancy
- [x] Matrice tracciabilita requisiti

**Testing**:
- [x] Unit test (coverage 85%)
- [x] E2E test (tutti passanti)
- [x] Multi-tenancy testato e verificato
- [x] Performance testata con 1000+ record

**Deploy**:
- [x] Staging deploy completato
- [x] Smoke test passanti
- [x] Pronto per release produzione

**Metriche**:
- Story Points: 99 SP
- Sprint: 4 sprint (8 settimane)
- Velocita media: 24 SP/sprint
- Bug trovati in QA: 12 (tutti fixati)

**Lessons Learned**:
- Context switcher piu complesso del previsto (+3 giorni)
- Multi-tenancy testing fondamentale (trovati 4 bug critici)
- Validazioni P.IVA/CF hanno richiesto refactoring (+ 2 giorni)

**Next Steps**:
- Monitorare metriche post-release
- Raccogliere feedback utenti
- Iniziare Epic Framework Normativi (E3)
```

4. Salva e chiudi epic

- [ ] **Epic completata e chiusa** quando tutto e fatto

---

## Template Riutilizzabile per Epic Successive

Quando crei le prossime epic (es: Framework Normativi, Audit, Fornitori), usa questo workflow:

1. **Copia cartella deliveries**: `cp -r epica-anagrafiche epica-framework`
2. **Duplica file metadata**: Salva `epic-[nome]-metadata.txt`, `epic-[nome]-description.md`, `epic-[nome]-links.txt`
3. **Adatta contenuti**: Modifica description, metadata, links per nuova epic
4. **Segui questa guida**: Esegui FASE 0 → FASE 5 step-by-step

**Differenze per epic successive**:

- **Component**: Cambia component (es: "Framework Normativi" invece di "Anagrafiche")
- **Labels**: Adatta labels funzionali (es: `framework, compliance` invece di `crud, multi-tenancy`)
- **Dipendenze**: Aggiorna dipendenze in ingresso/uscita (es: Epic Framework dipende da Epic Anagrafiche)
- **Priorita**: Potrebbe essere diversa (es: Should-Have invece di Must-Have)

---

## Domande Frequenti (FAQ)

### Q1: Quante story dovrebbe contenere un'epic?

**R**: Non c'e limite fisso, ma **5-15 story** e un range gestibile. Se superi 20, considera split in piu epic (es: "Anagrafiche - Parte 1: Utenti" e "Anagrafiche - Parte 2: Aziende").

---

### Q2: Posso cambiare lo scope dell'epic dopo creazione?

**R**: Si, ma **documenta i cambi nei commenti**. Se lo scope cresce troppo (+30%), meglio creare una nuova epic per le funzionalita aggiunte.

---

### Q3: Come gestisco story che toccano piu epic?

**R**: Assegna la story all'**epic principale** (dove sta la maggior parte del lavoro) e usa link **"relates to"** per epic secondarie.

Esempio:
- Story `US-ANA-020: Dashboard Contatori` appartiene a Epic Anagrafiche
- Ma "relates to" Epic Dashboard (perche tocca anche UI dashboard)

---

### Q4: Le epic devono essere completate in un solo sprint?

**R**: **No**. Le epic possono durare **piu sprint** (tipicamente 2-5 sprint). Solo le **user stories** devono stare in un solo sprint (story troppo grandi vanno splittate).

---

### Q5: Come gestisco le funzionalita condivise tra piu ruoli?

**R**: Usa **una story unica** e specifica le **differenze per ruolo** nella sezione "Acceptance Criteria".

Esempio story `US-ANA-009: Visualizzare Lista Aziende Clienti`:
- **AC-01**: Admin vede tutte le aziende clienti (nessun filtro tenant)
- **AC-02**: Consulente vede solo aziende assegnate a lui (filtro tenant attivo)

---

### Q6: Devo creare tutte le 27 user stories subito?

**R**: **No**. Puoi creare prima le story dello **Sprint 1** (7 stories) e poi continuare con gli altri sprint man mano. Ma assicurati di avere almeno **le prime 5-7 story** create prima di iniziare sviluppo.

---

### Q7: Cosa faccio se trovo un bug durante sviluppo?

**R**: Crea una **issue tipo "Bug"** (NON story) e collegala all'epic con link **"relates to"**. Il bug NON conta come story nell'epic, ma e tracciato.

---

### Q8: Come gestisco task tecnici (es: "Setup database schema")?

**R**: Se e task infrastrutturale NON legato a una story specifica, crea **issue tipo "Task"** e collegala all'epic. Se e parte di una story (es: "Creare tabella utenti" per US-ANA-001), crea **subtask** della story.

---

### Q9: Posso usare questa guida per progetti non-NIS2?

**R**: **Si**. La guida e generica. Basta adattare:
- Nomi component (es: "Payments" invece di "Anagrafiche")
- Labels (es: `payments, stripe, checkout`)
- Description template (cambia Obiettivo, Scope, Ruoli, Vincoli)

---

### Q10: Ho creato l'epic ma poi ho scoperto che serve altro. Devo ricrearla?

**R**: **No**. Puoi modificare l'epic dopo creazione:
1. Apri epic in Jira
2. Click **"Edit"** (icona matita in alto a destra)
3. Modifica description, labels, component, etc.
4. Salva

**IMPORTANTE**: Se cambi scope significativamente, aggiungi commento per tracciare il cambio.

---

## Checklist Finale Recap

Usa questa checklist rapida per verificare di aver completato tutto:

### FASE 0: Pre-Volo
- [ ] Accesso Jira verificato
- [ ] Permessi creazione epic verificati
- [ ] Documentazione (PRD, User Stories) pronta

### FASE 1: Preparazione Ambiente
- [ ] Component creato/verificato
- [ ] Fix Version creata/verificata
- [ ] Labels list preparata
- [ ] Board configurata con swimlanes epic

### FASE 2: Preparazione Contenuti
- [ ] Description epic scritta e salvata
- [ ] Lista links esterni preparata
- [ ] Metadata epic preparata (Name, Summary, Priority, Labels, Component, Fix Version)

### FASE 3: Creazione Epic
- [ ] Form creazione epic compilato
- [ ] Epic creata con successo
- [ ] Epic Key annotato

### FASE 4: Collegamento Links e Stories
- [ ] Links esterni aggiunti all'epic
- [ ] User stories collegate all'epic
- [ ] User stories ordinate per priorita
- [ ] Relazioni tra epic create (se applicabile)

### FASE 5: Verifica Finale
- [ ] Checklist completezza epic verificata
- [ ] Filtri Jira creati
- [ ] Dashboard epic creata (opzionale)
- [ ] PRD aggiornato con link Jira
- [ ] Team notificato

### FASE 6: Manutenzione (Durante Sviluppo)
- [ ] Epic aggiornata settimanalmente
- [ ] Deliverable checklist aggiornata
- [ ] Epic chiusa quando completata

---

## Risorse Aggiuntive

- **Jira Documentation**: [https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/](https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/)
- **JQL Reference**: [https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- **Epic Planning**: [https://www.atlassian.com/agile/project-management/epics](https://www.atlassian.com/agile/project-management/epics)

---

## Conclusione

Hai completato la guida step-by-step per creare un'Epic in Jira senza sorprese!

**Vantaggi di questo approccio**:
- **Zero interruzioni**: Tutto preparato in anticipo, niente "ah, serve anche questo"
- **Tracciabilita completa**: Links a documenti, dipendenze chiare, metadata strutturati
- **Ripetibile**: Template riutilizzabile per tutte le epic future
- **Collaborativo**: Team ha visibilita completa su scope, priorita, dipendenze

**Prossimi passi**:
1. **Crea Epic Anagrafiche** seguendo questa guida (tempo stimato: 30-45 minuti)
2. **Crea Epic successive** (Autenticazione, Framework, Audit, Fornitori) riutilizzando template
3. **Sprint Planning**: Stima story points per prime story e inizia Sprint 1

Buon lavoro!

---

_Guida creata da: Delivery Manager Agent_
_Versione: 1.0_
_Data: 2025-12-11_
_Caso d'uso: Epic Anagrafiche (E2) - Piattaforma conformita NIS2/CIS_
