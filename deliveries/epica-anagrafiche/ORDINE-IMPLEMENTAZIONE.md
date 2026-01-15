# Ordine di Implementazione - Epica Anagrafiche

**Versione**: 2.0
**Data**: 2025-12-11
**Totale User Stories**: 27
**Nomenclatura**: US-ANA-001 → US-ANA-027 (unificata)

---

## Executive Summary

Questo documento definisce l'ordine ottimale di implementazione delle 27 user stories dell'Epica Anagrafiche, raggruppate in 4 sprint logici. L'ordine tiene conto di:

- **Dipendenze tecniche**: Fondamenta prima, funzionalità avanzate poi
- **Valore di business**: Funzionalità core che sbloccano altre feature
- **Complessità crescente**: Partire da base semplice, crescere gradualmente
- **Testing incrementale**: Possibilità di testare ogni layer prima del successivo
- **Rischio**: Affrontare parti critiche (multi-tenancy, multi-consulente) in modo controllato

### Rationale Generale dell'Ordine

1. **Sprint 1 - Foundation**: Creare utenti Admin e CRUD base Aziende Consulenza (senza multi-tenancy)
2. **Sprint 2 - Multi-Tenancy Core**: Implementare Aziende Clienti con segregazione dati e gestione Sedi
3. **Sprint 3 - Advanced Multi-Consulente**: Abilitare scenari complessi (multi-consulente, context switcher)
4. **Sprint 4 - Enhancement & Polish**: Filtri avanzati, ricerche, contatori, soglie

---

## Sprint 1: Foundation - Admin & Aziende Consulenza Base (Stories 1-7)

**Obiettivo Sprint**: Creare fondamenta del sistema con gestione utenti Admin e CRUD base Aziende di Consulenza (senza scenari multi-tenancy complessi)

**Durata stimata**: 8-10 giorni

---

### 1. US-ANA-001 - Creare Admin Piattaforma

**Rationale**:

- Prima story in assoluto. Serve per creare gli Admin iniziali che gestiranno tutto il resto.
- Nessuna dipendenza da altre entità.
- Necessaria per avere utenti loggati che possano testare le feature successive.

**Dipendenze**: Nessuna (foundation)

**Complessità**: Bassa (form 4 campi + email invito)

**Testing**: Testabile immediatamente (creazione Admin → login → verifica accesso)

---

### 2. US-ANA-002 - Modificare Admin Piattaforma

**Rationale**:

- Completamento CRUD Admin (dopo Create).
- Permette di correggere errori nei dati Admin creati.
- Logica semplice (form modifica, email read-only).

**Dipendenze**:

- US-ANA-001 (serve almeno 1 Admin esistente da modificare)

**Complessità**: Bassa (form modifica, no vincoli complessi)

**Testing**: Testabile in sequenza (crea Admin → modifica Admin → verifica cambiamenti)

---

### 3. US-ANA-003 - Eliminare Admin Piattaforma con validazione vincoli

**Rationale**:

- Completamento CRUD Admin (dopo Create e Update).
- Implementa vincoli critici di sicurezza (no auto-eliminazione, no ultimo Admin).
- Necessaria per gestire ciclo vita Admin completo.

**Dipendenze**:

- US-ANA-001 (serve almeno 2 Admin per testare vincolo "ultimo Admin")

**Complessità**: Media (logica vincoli + soft delete + invalidazione sessioni)

**Testing**: Testabile dopo creazione multipli Admin (scenari: auto-delete, ultimo Admin, eliminazione valida)

---

### 4. US-ANA-004 - Visualizzare lista aziende di consulenza (Admin)

**Rationale**:

- Fondazione gestione Aziende Consulenza.
- Lista vuota inizialmente, ma necessaria per testare UI e navigazione.
- Entry point per tutte le operazioni su Aziende Consulenza.

**Dipendenze**:

- US-ANA-001 (serve Admin loggato per accedere alla lista)

**Complessità**: Bassa (lista semplice con paginazione)

**Testing**: Testabile immediatamente (Admin → accede a "Aziende di consulenza" → vede lista vuota)

---

### 5. US-ANA-005 - Creare nuova azienda di consulenza con primo admin-consulente (Admin)

**Rationale**:

- Prima creazione di entità multi-tenant (Azienda Consulenza + Admin-Consulente).
- Implementa validazione P.IVA (univoca).
- Crea il primo tenant logico del sistema.
- Necessaria per tutte le funzionalità successive legate ai Consulenti.

**Dipendenze**:

- US-ANA-004 (lista dove appare azienda creata)
- US-ANA-001 (Admin che crea l'azienda)

**Complessità**: Media (form 2 sezioni, validazione P.IVA, creazione 2 entità atomica, email invito)

**Testing**: Testabile end-to-end (Admin crea azienda → verifica in lista → Admin-Consulente riceve email → login)

---

### 6. US-ANA-006 - Visualizzare dettaglio azienda di consulenza (Admin)

**Rationale**:

- Pagina dettaglio necessaria per accedere a funzionalità avanzate (gestione consulenti, modifica, eliminazione).
- Implementa widgets contatori (base per dashboard).
- Entry point per modifiche e gestione consulenti.

**Dipendenze**:

- US-ANA-005 (serve almeno 1 azienda esistente da visualizzare)

**Complessità**: Media (pagina dettaglio con 6 widgets, calcolo contatori)

**Testing**: Testabile dopo creazione azienda (Admin crea azienda → click su nome → vede dettaglio)

---

### 7. US-ANA-007 - Modificare dati azienda di consulenza (Admin)

**Rationale**:

- Completamento CRUD Aziende Consulenza (dopo Create e Read).
- Permette correzione dati errati.
- Validazione P.IVA modificata (univoca, escludendo se stessa).

**Dipendenze**:

- US-ANA-006 (modal modifica accessibile da dettaglio)

**Complessità**: Bassa (form modifica, P.IVA non modificabile)

**Testing**: Testabile in sequenza (crea azienda → modifica dati → verifica cambiamenti in dettaglio)

---

## Sprint 2: Multi-Tenancy Core - Aziende Clienti & Sedi (Stories 8-15)

**Obiettivo Sprint**: Implementare gestione Aziende Clienti con segregazione multi-tenant, Sedi Aziendali e Utenti Aziendali (scenario single-consulente)

**Durata stimata**: 12-14 giorni

---

### 8. US-ANA-008 - Gestire consulenti collegati all'azienda di consulenza (Admin)

**Rationale**:

- Necessaria prima di Aziende Clienti (i Consulenti gestiranno le aziende clienti).
- Implementa creazione/modifica/eliminazione consulenti (non Admin-Consulente).
- Widget "Elenco consulenti" nel dettaglio azienda.

**Dipendenze**:

- US-ANA-006 (widget accessibile da dettaglio azienda)

**Complessità**: Alta (CRUD completo consulenti + vincoli eliminazione + lista widget)

**Testing**: Testabile end-to-end (Admin → dettaglio azienda → aggiungi consulente → verifica email → consulente login)

---

### 9. US-ANA-009 - Visualizzare Lista Aziende Clienti

**Rationale**:

- Entry point per gestione Aziende Clienti.
- Implementa filtri multi-tenancy (Consulente vede solo sue aziende, Admin vede tutto).
- Prima feature che testa segregazione dati.

**Dipendenze**:

- US-ANA-008 (serve almeno 1 Consulente loggato per testare filtro tenant)
- US-ANA-005 (serve Azienda Consulenza esistente)

**Complessità**: Media (lista con filtri tenant + colonne dinamiche per ruolo)

**Testing**: Testabile con multi-utenti (Admin vede tutte, Consulente vede solo sue)

---

### 10. US-ANA-010 - Creare Azienda Cliente (assegnazione single-consulente)

**Rationale**:

- Prima creazione di entità Azienda Cliente.
- Implementa validazione P.IVA/CF (univoche).
- Assegnazione a singolo consulente (scenario base).
- Necessaria per tutte le feature successive (Sedi, Utenti Aziendali).

**Dipendenze**:

- US-ANA-009 (lista dove appare azienda creata)
- US-ANA-008 (dropdown consulenti deve contenere almeno 1 consulente)

**Complessità**: Media (form 2 sezioni, validazioni P.IVA/CF, relazione Azienda-Consulente)

**Testing**: Testabile end-to-end (Consulente crea azienda → assegna a sé stesso → verifica in lista)

---

### 11. US-ANA-011 - Visualizzare Dettaglio Azienda Cliente

**Rationale**:

- Pagina dettaglio necessaria per accedere a Sedi e Utenti Aziendali.
- Implementa widget contatori (Sedi, Utenti, Audit).
- Entry point per modifiche e gestione sottosezioni.

**Dipendenze**:

- US-ANA-010 (serve almeno 1 azienda cliente esistente)

**Complessità**: Media (pagina dettaglio con tabs, widgets contatori)

**Testing**: Testabile dopo creazione azienda (Consulente crea azienda → click su nome → vede dettaglio)

---

### 12. US-ANA-012 - Gestire Sedi Aziendali

**Rationale**:

- Gestione Sedi necessaria prima di Utenti Aziendali (utenti assegnati a sedi).
- CRUD completo sedi in modal.
- Validazione vincoli (almeno 1 sede principale).

**Dipendenze**:

- US-ANA-011 (tab "Sedi" accessibile da dettaglio azienda)

**Complessità**: Alta (CRUD completo + validazione "almeno 1 sede principale" + lista widget)

**Testing**: Testabile end-to-end (Consulente → dettaglio azienda → tab Sedi → crea/modifica/elimina sedi)

---

### 13. US-ANA-013 - Gestire Utenti Aziendali

**Rationale**:

- Creazione utenti che accederanno alla piattaforma per consultare audit.
- Validazione email univoca + assegnazione sede.
- Implementa ruoli Azienda (Admin Cliente vs Cliente semplice).

**Dipendenze**:

- US-ANA-012 (dropdown sedi deve contenere almeno 1 sede)
- US-ANA-011 (tab "Utenti" accessibile da dettaglio azienda)

**Complessità**: Alta (CRUD utenti + ruoli + validazioni + email invito)

**Testing**: Testabile end-to-end (Consulente → crea utente aziendale → utente riceve email → login come Admin Cliente)

---

### 14. US-ANA-014 - Modificare Azienda Cliente

**Rationale**:

- Completamento CRUD Aziende Clienti (dopo Create e Read).
- Permette correzione dati + cambio consulente assegnato (single-consulente).

**Dipendenze**:

- US-ANA-011 (form modifica accessibile da dettaglio)

**Complessità**: Bassa (form modifica, P.IVA/CF non modificabili)

**Testing**: Testabile in sequenza (crea azienda → modifica dati → verifica cambiamenti)

---

### 15. US-ANA-015 - Eliminare Azienda Cliente

**Rationale**:

- Completamento CRUD Aziende Clienti (Delete).
- Implementa validazione vincoli (blocco se ci sono audit attivi).
- Soft delete con preservazione audit trail.

**Dipendenze**:

- US-ANA-014 (testare prima modifica, poi eliminazione)

**Complessità**: Media (validazione vincoli + soft delete + cascade sedi/utenti)

**Testing**: Testabile con scenari (azienda senza audit → eliminazione OK, azienda con audit → blocco)

---

## Sprint 3: Advanced Multi-Consulente & Context Switcher (Stories 16-21)

**Obiettivo Sprint**: Abilitare scenari complessi multi-consulente, context switcher, gestione avanzata Aziende Consulenza

**Durata stimata**: 10-12 giorni

---

### 16. US-ANA-016 - Assegnare Multipli Consulenti (Multi-Consulente)

**Rationale**:

- Feature avanzata che permette collaborazione tra consulenti.
- Modifica logica multi-tenancy (azienda visibile a più consulenti).
- Necessaria prima di Context Switcher (che dipende da scenari multi-tenant complessi).

**Dipendenze**:

- US-ANA-010 (serve azienda con single-consulente già assegnato)
- US-ANA-008 (serve lista consulenti disponibili)

**Complessità**: Alta (logica multi-assegnazione + validazione "almeno 1 consulente" + tabella many-to-many)

**Testing**: Testabile con multi-utenti (Consulente A crea azienda → Admin assegna anche Consulente B → entrambi vedono azienda)

---

### 17. US-ANA-017 - Implementare Context Switcher per Multi-Consulente

**Rationale**:

- Feature UX critica per Admin-Consulente che gestisce più aziende di consulenza.
- Permette cambio contesto senza logout.
- Necessaria per testare segregazione multi-tenant avanzata.

**Dipendenze**:

- US-ANA-016 (scenario multi-consulente deve essere già implementato)
- US-ANA-005 (serve almeno 2 aziende di consulenza per testare switch)

**Complessità**: Alta (context switcher UI + logica cambio tenant + refresh dati + persistenza sessione)

**Testing**: Testabile con Admin-Consulente di 2 aziende (login → vede aziende clienti Azienda A → switch a Azienda B → vede aziende clienti Azienda B)

---

### 18. US-ANA-018 - Gestire aziende clienti associate all'azienda di consulenza (Admin)

**Rationale**:

- Widget nel dettaglio Azienda Consulenza che mostra aziende clienti associate.
- Permette riassegnazione consulenti da questa vista.
- Complementare a US-ANA-009 (vista da Aziende Clienti) e US-ANA-016 (riassegnazione).

**Dipendenze**:

- US-ANA-006 (widget accessibile da dettaglio azienda consulenza)
- US-ANA-010 (serve almeno 1 azienda cliente esistente)
- US-ANA-016 (feature multi-consulente deve essere implementata)

**Complessità**: Media (widget lista + azioni riassegnazione consulente)

**Testing**: Testabile end-to-end (Admin → dettaglio Azienda Consulenza → vede lista aziende clienti → riassegna consulente)

---

### 19. US-ANA-019 - Eliminare azienda di consulenza con validazione vincoli (Admin)

**Rationale**:

- Completamento CRUD Aziende Consulenza (Delete).
- Implementa vincoli complessi (blocco se ci sono aziende clienti attive o audit attivi).
- Feature critica per integrità dati (no eliminazione accidentale con dati collegati).

**Dipendenze**:

- US-ANA-018 (necessario vedere aziende clienti associate prima di validare vincolo eliminazione)
- US-ANA-010 (necessario avere aziende clienti collegate per testare blocco)

**Complessità**: Alta (validazione vincoli multipli + soft delete + cascade consulenti + dialog dettagliato impatti)

**Testing**: Testabile con scenari (azienda senza clienti → eliminazione OK, azienda con clienti → blocco + messaggio dettagliato)

---

### 20. US-ANA-020 - Visualizzare contatori dashboard filtrati per tenant (Admin e Consulente)

**Rationale**:

- Dashboard con KPI critici (aziende clienti, audit attivi, azioni aperte).
- Implementa filtri tenant (Admin vede tutto, Consulente vede solo sue aziende).
- Necessaria per monitoraggio operativo.

**Dipendenze**:

- US-ANA-010 (serve aziende clienti esistenti per calcolare contatori)
- US-ANA-008 (serve consulenti esistenti per filtrare per tenant)
- US-ANA-016 (scenario multi-consulente per testare filtri complessi)

**Complessità**: Media (widget contatori + query aggregate + filtri tenant)

**Testing**: Testabile con multi-utenti (Admin vede contatori globali, Consulente vede solo suoi dati)

---

### 21. US-ANA-021 - Bloccare creazione aziende/utenti al raggiungimento soglia massima (Sistema)

**Rationale**:

- Feature di sicurezza/licensing (evitare creazione illimitata).
- Validazione server-side su tutte le creazioni (Aziende Consulenza, Aziende Clienti, Utenti).
- Necessaria per controllo crescita piattaforma.

**Dipendenze**:

- US-ANA-005 (creazione Aziende Consulenza)
- US-ANA-010 (creazione Aziende Clienti)
- US-ANA-001 (creazione Admin)
- US-ANA-008 (creazione Consulenti)

**Complessità**: Media (validazione soglie + messaggi errore dettagliati + configurazione soglie)

**Testing**: Testabile creando entità fino a soglia (es: crea 50 aziende → 51a bloccata con messaggio "Limite raggiunto")

---

## Sprint 4: Enhancement & Polish - Filtri, Ricerche, Gestione Utenti (Stories 22-27)

**Obiettivo Sprint**: Completare funzionalità di ricerca avanzata, filtri e gestione centralizzata utenti

**Durata stimata**: 8-10 giorni

---

### 22. US-ANA-022 - Ricercare e filtrare aziende di consulenza (Admin)

**Rationale**:

- Feature UX importante per Admin con molte aziende.
- Filtri: nome azienda, P.IVA, città, range date creazione.
- Ricerca globale con debounce.

**Dipendenze**:

- US-ANA-004 (lista dove applicare filtri)

**Complessità**: Media (filtri multipli + ricerca globale + debounce + reset filtri)

**Testing**: Testabile con dataset popolato (crea 20+ aziende → applica filtri → verifica risultati)

---

### 23. US-ANA-023 - Ricercare e Filtrare Aziende Clienti

**Rationale**:

- Feature UX importante per Consulenti con molte aziende clienti.
- Filtri: ragione sociale, P.IVA, consulente assegnato, stato conformità.
- Ricerca globale con debounce.

**Dipendenze**:

- US-ANA-009 (lista dove applicare filtri)

**Complessità**: Media (filtri multipli + ricerca globale + debounce + reset filtri)

**Testing**: Testabile con dataset popolato (crea 20+ aziende clienti → applica filtri → verifica risultati)

---

### 24. US-ANA-024 - Esportare Lista Aziende Clienti (CSV/PDF)

**Rationale**:

- Feature di reporting per Consulenti.
- Export CSV (tutti campi) e PDF (template formattato).
- Rispetta filtri applicati alla lista.

**Dipendenze**:

- US-ANA-009 (lista da esportare)
- US-ANA-023 (export deve rispettare filtri)

**Complessità**: Bassa (generazione CSV server-side + PDF client-side con template)

**Testing**: Testabile end-to-end (applica filtri → click Export CSV → verifica file → click Export PDF → verifica template)

---

### 25. US-ANA-025 - Visualizzare lista unificata utenti (Admin)

**Rationale**:

- Lista centralizzata di TUTTI gli utenti (Admin, Consulenti, Utenti Aziendali).
- Entry point per gestione utenti da vista unificata.
- Azioni intelligenti (redirect a contesto appropriato per modifica/eliminazione).

**Dipendenze**:

- US-ANA-001 (serve almeno 1 Admin)
- US-ANA-008 (serve almeno 1 Consulente)
- US-ANA-013 (serve almeno 1 Utente Aziendale)

**Complessità**: Alta (lista multi-entità + badge tipo utente + azioni contestuali con redirect intelligenti)

**Testing**: Testabile con utenti misti (Admin crea 1 Admin, 2 Consulenti, 3 Utenti Aziendali → vede lista unificata → test azioni)

---

### 26. US-ANA-026 - Modal selezione tipo utente per creazione (Admin)

**Rationale**:

- UX pattern per creazione utenti da lista unificata.
- Modal con 3 opzioni: Consulente → redirect ad Aziende Consulenza, Utente Aziendale → redirect ad Aziende Clienti, Admin → form inline.

**Dipendenze**:

- US-ANA-025 (pulsante "Crea Nuovo Utente" che apre modal)
- US-ANA-001 (opzione "Admin" → form inline)

**Complessità**: Media (modal con 3 flussi diversi + redirect condizionali)

**Testing**: Testabile end-to-end (Admin → click Crea Nuovo Utente → seleziona tipo → verifica flusso corretto)

---

### 27. US-ANA-027 - Filtrare e ricercare utenti (Admin)

**Rationale**:

- Feature UX per Admin con molti utenti.
- Filtri: tipo utente (Consulente/Cliente/Admin), ricerca globale (nome/cognome/email/telefono).
- Debounce 300ms su ricerca testuale.

**Dipendenze**:

- US-ANA-025 (lista dove applicare filtri)

**Complessità**: Media (filtri multipli + ricerca globale + debounce + badge "Filtri attivi")

**Testing**: Testabile con dataset popolato (crea 30+ utenti misti → applica filtri → verifica risultati)

---

## Riepilogo Dipendenze Critiche

### Dipendenze Blocking (Story A → Story B)

| Story Prerequisito                 | Story Dipendente                   | Motivo                                                             |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| US-ANA-001                         | US-ANA-002, US-ANA-003             | Serve almeno 1 Admin esistente per modificare/eliminare            |
| US-ANA-001                         | US-ANA-004                         | Serve Admin loggato per accedere alle liste                        |
| US-ANA-004                         | US-ANA-005                         | Lista dove appare azienda creata                                   |
| US-ANA-005                         | US-ANA-006                         | Serve almeno 1 azienda esistente per visualizzare dettaglio        |
| US-ANA-006                         | US-ANA-007, US-ANA-008, US-ANA-018 | Dettaglio è entry point per modifiche e gestione sottosezioni      |
| US-ANA-008                         | US-ANA-009                         | Serve almeno 1 Consulente per testare filtri multi-tenancy         |
| US-ANA-009                         | US-ANA-010                         | Lista dove appare azienda cliente creata                           |
| US-ANA-010                         | US-ANA-011                         | Serve almeno 1 azienda cliente per visualizzare dettaglio          |
| US-ANA-011                         | US-ANA-012, US-ANA-013, US-ANA-014 | Dettaglio è entry point per Sedi, Utenti, Modifiche                |
| US-ANA-012                         | US-ANA-013                         | Utenti Aziendali assegnati a Sedi (dropdown deve contenere sedi)   |
| US-ANA-010                         | US-ANA-016                         | Serve azienda con single-consulente prima di assegnare multipli    |
| US-ANA-016                         | US-ANA-017                         | Context switcher richiede scenario multi-consulente implementato   |
| US-ANA-016                         | US-ANA-018                         | Widget aziende clienti richiede feature multi-consulente           |
| US-ANA-018                         | US-ANA-019                         | Validazione eliminazione richiede vedere aziende clienti associate |
| US-ANA-001, US-ANA-008, US-ANA-013 | US-ANA-025                         | Lista unificata utenti richiede tutti i tipi di utenti esistenti   |
| US-ANA-025                         | US-ANA-026                         | Modal creazione utente accessibile da lista unificata              |
| US-ANA-009                         | US-ANA-023                         | Filtri si applicano alla lista aziende clienti                     |
| US-ANA-023                         | US-ANA-024                         | Export deve rispettare filtri applicati                            |

### Dipendenze Logiche (Suggerite ma non bloccanti)

| Story      | Dipendenza Logica      | Motivo                                                                                  |
| ---------- | ---------------------- | --------------------------------------------------------------------------------------- |
| US-ANA-022 | US-ANA-004             | Filtri hanno più senso dopo avere molte aziende, ma implementabili subito               |
| US-ANA-021 | US-ANA-005, US-ANA-010 | Soglie hanno senso dopo implementare creazioni, ma validabili da subito                 |
| US-ANA-020 | US-ANA-010             | Contatori dashboard più significativi con dati popolati, ma widget implementabile prima |
| US-ANA-027 | US-ANA-025             | Filtri utenti hanno senso dopo lista popolata, ma implementabili insieme                |

---

## Matrice Sprint vs Complessità

| Sprint     | Stories | Story Points Totali (stimati) | Complessità Media | Rischio   |
| ---------- | ------- | ----------------------------- | ----------------- | --------- |
| Sprint 1   | 7       | 21                            | Bassa-Media       | Basso     |
| Sprint 2   | 8       | 34                            | Media-Alta        | Medio     |
| Sprint 3   | 6       | 26                            | Alta              | Alto      |
| Sprint 4   | 6       | 18                            | Bassa-Media       | Basso     |
| **TOTALE** | **27**  | **99**                        | **Media**         | **Medio** |

**Legenda Story Points**:

- Bassa: 2 SP
- Media: 3-5 SP
- Alta: 8 SP

---

## Note Implementative per Sprint

### Sprint 1: Focus su Stabilità

- **Obiettivo**: Creare fondamenta solide con test completi
- **Testing**: Unit test + E2E per ogni story
- **Priorità**: Autenticazione, validazioni, soft delete
- **Deliverable**: Admin possono creare/modificare/eliminare Admin e Aziende Consulenza

### Sprint 2: Focus su Multi-Tenancy

- **Obiettivo**: Implementare segregazione dati corretta
- **Testing**: Test multi-tenancy (Consulente A non vede dati Consulente B)
- **Priorità**: Filtri tenant, validazioni P.IVA/CF, relazioni Azienda-Consulente
- **Deliverable**: Consulenti possono gestire Aziende Clienti con Sedi e Utenti Aziendali

### Sprint 3: Focus su Scenari Complessi

- **Obiettivo**: Abilitare multi-consulente e context switcher
- **Testing**: Test scenari complessi (azienda con 3 consulenti, Admin-Consulente di 2 aziende consulenza)
- **Priorità**: Context switcher, validazioni vincoli eliminazione
- **Deliverable**: Sistema supporta collaborazione multi-consulente e gestione avanzata

### Sprint 4: Focus su UX & Performance

- **Obiettivo**: Migliorare usabilità con filtri e ricerche
- **Testing**: Test performance con dataset grandi (>1000 record)
- **Priorità**: Debounce, lazy loading, export ottimizzati
- **Deliverable**: Piattaforma completa con UX polished e funzionalità di ricerca avanzata

---

## Rischi e Mitigazioni

### Rischio 1: Multi-Tenancy Bugs (Sprint 2)

**Descrizione**: Segregazione dati non corretta → Consulente A vede dati Consulente B

**Mitigazione**:

- Test E2E con multi-utenti PRIMA di passare a Sprint 3
- Code review approfondita su query filtri tenant
- Security audit su endpoint API

### Rischio 2: Context Switcher Complessità (Sprint 3)

**Descrizione**: Context switcher complesso → refresh dati incompleto o stato inconsistente

**Mitigazione**:

- Implementare context switcher in story separata (US-ANA-017)
- Test approfonditi su cambio contesto (verifica refresh completo)
- Persistenza sessione per evitare perdita stato

### Rischio 3: Performance con Molti Dati (Sprint 4)

**Descrizione**: Filtri e ricerche lenti con >1000 record

**Mitigazione**:

- Implementare paginazione server-side da subito
- Debounce 300ms su ricerche testuali
- Indici database su campi filtrabili (email, P.IVA, nome)

### Rischio 4: Validazioni Vincoli Eliminazione (Sprint 3)

**Descrizione**: Eliminazione accidentale di Azienda Consulenza con dati collegati

**Mitigazione**:

- Implementare validazione vincoli robusta (US-ANA-019, US-ANA-015)
- Dialog conferma dettagliato con lista impatti
- Soft delete con possibilità ripristino (feature futura)

---

## Definition of Done per Story

Ogni story è considerata COMPLETA quando:

1. **Codice**:

   - Implementazione completa secondo criteri accettazione
   - Code review completata e approvata
   - Nessun warning/error critico

2. **Testing**:

   - Unit test scritti e passanti (coverage >80%)
   - E2E test per flussi principali
   - Test edge cases documentati
   - Test multi-tenancy (se applicabile)

3. **Documentazione**:

   - API endpoints documentati (se nuovi)
   - Commenti codice per logica complessa
   - README aggiornato (se nuove dipendenze)

4. **UI/UX**:

   - Mockup/wireframe approvati (se nuova UI)
   - Responsive design testato (mobile, tablet, desktop)
   - Accessibilità base rispettata (WCAG 2.1 Level A)

5. **Validazioni**:

   - Validazioni frontend + backend implementate
   - Messaggi errore user-friendly
   - Edge cases gestiti

6. **Performance**:

   - Query ottimizzate (no N+1)
   - Lazy loading implementato (se liste lunghe)
   - Debounce su ricerche testuali

7. **Security**:

   - Input sanitizzati (SQL injection, XSS)
   - Autenticazione/Autorizzazione verificate
   - Multi-tenancy testata (se applicabile)

8. **Deploy**:
   - Branch mergiato su main
   - Deploy su staging completato
   - Smoke test su staging passanti

---

## Sequenza di Testing Ottimale

### Dopo Sprint 1 (Foundation)

**Test E2E Critici**:

1. Admin crea Admin Piattaforma → riceve email → fa login → accede a dashboard
2. Admin crea Azienda Consulenza + Admin-Consulente → Admin-Consulente fa login → vede dashboard filtrato
3. Admin modifica dati Azienda Consulenza → verifica modifiche persistite
4. Admin tenta eliminare ultimo Admin → sistema blocca con messaggio
5. Admin tenta eliminare se stesso → sistema blocca con messaggio

### Dopo Sprint 2 (Multi-Tenancy)

**Test E2E Critici**:

1. Consulente A crea Azienda Cliente X → Consulente B non vede Azienda X in lista
2. Admin vede tutte le Aziende Clienti (A + B) → verifica colonna "Consulente Assegnato"
3. Consulente crea Sede principale → tenta eliminare → sistema blocca
4. Consulente crea Utente Aziendale → Utente fa login → vede solo propria azienda
5. Consulente tenta eliminare Azienda Cliente con Utenti Aziendali → sistema blocca (se vincolo attivo)

### Dopo Sprint 3 (Multi-Consulente)

**Test E2E Critici**:

1. Admin assegna Azienda Cliente X a Consulente A + B → entrambi vedono Azienda X
2. Admin-Consulente di Azienda Consulenza 1 + 2 → fa login → usa context switcher → verifica cambio dati
3. Admin tenta eliminare Azienda Consulenza con Aziende Clienti attive → sistema blocca con dialog dettagliato
4. Consulente A rimuove Consulente B da Azienda Cliente X → Consulente B non vede più Azienda X
5. Dashboard contatori: Admin vede tutti, Consulente vede solo propri dati

### Dopo Sprint 4 (Enhancement)

**Test E2E Critici**:

1. Admin applica filtri su lista Aziende Consulenza → verifica risultati corretti
2. Consulente esporta lista Aziende Clienti (CSV + PDF) → verifica contenuto export
3. Admin usa lista unificata utenti → click Modifica su Consulente → redirect corretto ad Aziende Consulenza
4. Admin filtra utenti per "Tipo Utente = Consulente" + ricerca "mario" → verifica risultati
5. Admin crea 50 Aziende Consulenza (se soglia = 50) → 51a creazione bloccata con messaggio

---

## Checklist Pre-Implementazione

Prima di iniziare ogni sprint, verificare:

- [ ] Tutte le dipendenze bloccanti completate (vedi matrice dipendenze)
- [ ] Mockup/wireframe approvati per nuove UI
- [ ] Database schema aggiornato (se nuove tabelle/colonne)
- [ ] API endpoints pianificati (se nuovi)
- [ ] Environment di staging pronto
- [ ] Team ha accesso a tool necessari (SMTP per email, storage per documenti)
- [ ] Definition of Done condivisa e compresa

---

## Metriche di Successo per Epica

Al completamento dei 4 sprint, il sistema deve:

1. **Gestione Utenti**:

   - [x] 3 tipi di utenti creabili (Admin, Consulenti, Utenti Aziendali)
   - [x] Lista unificata utenti con azioni contestuali
   - [x] Soft delete con preservazione audit trail

2. **Gestione Aziende Consulenza**:

   - [x] CRUD completo Aziende Consulenza
   - [x] Gestione consulenti collegati
   - [x] Validazione vincoli eliminazione
   - [x] Filtri e ricerche

3. **Gestione Aziende Clienti**:

   - [x] CRUD completo Aziende Clienti
   - [x] Gestione Sedi Aziendali (almeno 1 principale)
   - [x] Gestione Utenti Aziendali con ruoli
   - [x] Multi-consulente con context switcher
   - [x] Export CSV/PDF

4. **Multi-Tenancy**:

   - [x] Segregazione dati corretta (Consulente vede solo propri dati)
   - [x] Admin vede tutti i dati
   - [x] Context switcher per Admin-Consulente multi-azienda

5. **Validazioni**:

   - [x] P.IVA univoca (Aziende Consulenza e Clienti)
   - [x] CF univoco (Aziende Clienti)
   - [x] Email univoca (Utenti)
   - [x] Vincoli eliminazione (no eliminazione con dati collegati)

6. **UX**:

   - [x] Filtri e ricerche avanzate
   - [x] Paginazione su tutte le liste
   - [x] Modal e dialog user-friendly
   - [x] Notifiche toast per feedback utente

7. **Performance**:
   - [x] Paginazione server-side
   - [x] Debounce su ricerche testuali
   - [x] Lazy loading (se >1000 record)

---

## Conclusione

L'ordine di implementazione proposto permette di:

1. **Costruire fondamenta solide** (Sprint 1) prima di affrontare multi-tenancy
2. **Testare segregazione dati** (Sprint 2) in modo incrementale
3. **Abilitare scenari complessi** (Sprint 3) solo dopo validare base funzionante
4. **Migliorare UX** (Sprint 4) come enhancement finale

**Durata totale stimata**: 38-46 giorni (circa 8-10 settimane con team 6/7 persone)

**Raccomandazione**: Eseguire **Sprint Review** e **Retrospettiva** alla fine di ogni sprint per validare completezza e adattare planning successivo se necessario.

---

_Documento creato da: Delivery Manager Agent_
_Ultima revisione: 2025-12-09_
_Versione: 2.0 (nomenclatura unificata US-ANA-001 → US-ANA-027)_
