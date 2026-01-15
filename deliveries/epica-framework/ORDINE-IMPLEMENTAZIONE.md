# Ordine di Implementazione - Epica Framework

**Versione**: 1.0
**Data**: 2025-12-11
**Totale User Stories**: 18
**Nomenclatura**: US-FWK-001 → US-FWK-018

---

## Executive Summary

Questo documento definisce l'ordine ottimale di implementazione delle 18 user stories dell'Epica Framework, raggruppate in 3 sprint logici. L'ordine tiene conto di:

- **Dipendenze tecniche**: Anagrafiche base prima, framework complesso poi
- **Valore di business**: Funzionalita core che sbloccano altre feature
- **Complessita crescente**: Partire da CRUD semplici, crescere verso gestione stati e freesolo
- **Testing incrementale**: Possibilita di testare ogni layer prima del successivo
- **Rischio**: Affrontare parti critiche (freesolo, stati framework, tabella anteprima) in modo controllato

### Rationale Generale dell'Ordine

1. **Sprint 1 - Anagrafiche Base**: CRUD Requisiti + CRUD Elementi di Valutazione (con Campo Libero/Scala)
2. **Sprint 2 - Framework Core**: CRUD Framework base + gestione righe + freesolo
3. **Sprint 3 - Stati e Pubblicazione**: Gestione stati (Bozza/Pubblicato/Archiviato) + eliminazione con vincoli

---

## Sprint 1: Anagrafiche Base - Requisiti ed Elementi di Valutazione (Stories 1-10)

**Obiettivo Sprint**: Creare le due anagrafiche fondamentali (Requisiti e Elementi di Valutazione) necessarie per costruire i Framework

**Durata stimata**: 10-12 giorni

---

### 1. US-FWK-001 - Visualizzare lista requisiti (Admin)

**Rationale**:
- Prima story in assoluto dell'epica. Fondazione per gestione Requisiti.
- Lista vuota inizialmente, ma necessaria per testare UI e navigazione.
- Entry point per tutte le operazioni su Requisiti.

**Dipendenze**: Nessuna (foundation)

**Complessita**: Bassa (lista semplice con paginazione + filtro ricerca)

**Testing**: Testabile immediatamente (Admin → accede a "Requisiti" → vede lista vuota)

---

### 2. US-FWK-002 - Creare nuovo requisito (Admin)

**Rationale**:
- Creazione primo requisito necessario per popolare anagrafica.
- Form semplice (2 campi: Nome + Descrizione).
- Validazione univocita nome.

**Dipendenze**:
- US-FWK-001 (lista dove appare requisito creato)

**Complessita**: Bassa (form 2 campi + validazione univocita)

**Testing**: Testabile end-to-end (Admin crea requisito → verifica in lista)

---

### 3. US-FWK-003 - Visualizzare dettaglio requisito (Admin)

**Rationale**:
- Pagina dettaglio read-only necessaria per consultazione e accesso a modifica.
- Mostra sezione "Utilizzo" (contatore framework che usano il requisito).

**Dipendenze**:
- US-FWK-002 (serve almeno 1 requisito esistente)

**Complessita**: Bassa (pagina dettaglio read-only + contatore utilizzo)

**Testing**: Testabile dopo creazione (Admin crea requisito → click nome → vede dettaglio)

---

### 4. US-FWK-004 - Modificare requisito (Admin)

**Rationale**:
- Completamento CRUD Requisiti (dopo Create e Read).
- Permette correzione errori nei dati.

**Dipendenze**:
- US-FWK-003 (modal modifica accessibile da dettaglio)

**Complessita**: Bassa (form modifica, validazione univocita nome escludendo se stesso)

**Testing**: Testabile in sequenza (crea requisito → modifica dati → verifica cambiamenti)

---

### 5. US-FWK-005 - Eliminare requisito con validazione vincoli (Admin)

**Rationale**:
- Completamento CRUD Requisiti (Delete).
- Implementa warning (NON blocco) se requisito utilizzato in righe framework.
- Hard delete con graceful degradation.

**Dipendenze**:
- US-FWK-004 (testare prima modifica, poi eliminazione)

**Complessita**: Media (warning utilizzo + hard delete)

**Testing**: Testabile con scenari (requisito non usato → eliminazione OK, requisito usato → warning)

---

### 6. US-FWK-006 - Visualizzare lista elementi di valutazione (Admin)

**Rationale**:
- Fondazione per gestione Elementi di Valutazione.
- Lista con badge tipo (Campo Libero / Scala).
- Entry point per creazione elementi.

**Dipendenze**: Nessuna (foundation)

**Complessita**: Bassa (lista con badge colorati + filtro ricerca)

**Testing**: Testabile immediatamente (Admin → accede a "Elementi di valutazione" → vede lista vuota)

---

### 7. US-FWK-007 - Creare nuovo elemento di valutazione - Campo Libero o Scala (Admin)

**Rationale**:
- Story piu complessa di Sprint 1 (radio button + campi condizionali).
- Implementa tipo "Campo Libero" (2 campi) e tipo "Scala" (coppie dinamiche Valore-Label).
- Validazione: almeno 2 coppie per Scala, valori numerici univoci.

**Dipendenze**:
- US-FWK-006 (lista dove appare elemento creato)

**Complessita**: Alta (radio button + campi condizionali + blocchi ripetibili + validazioni complesse)

**Testing**: Testabile end-to-end (Admin crea Campo Libero → verifica, Admin crea Scala con 3 coppie → verifica)

---

### 8. US-FWK-008 - Visualizzare dettaglio elemento di valutazione (Admin)

**Rationale**:
- Pagina dettaglio read-only con layout diverso per tipo (Campo Libero vs Scala).
- Se tipo=Scala: mostrare tabella coppie Valore-Label ordinata.

**Dipendenze**:
- US-FWK-007 (serve almeno 1 elemento esistente)

**Complessita**: Media (layout condizionale + tabella coppie se Scala)

**Testing**: Testabile dopo creazione (Admin crea elemento → click nome → vede dettaglio corretto)

---

### 9. US-FWK-009 - Modificare elemento di valutazione (Admin)

**Rationale**:
- Completamento CRUD Elementi (dopo Create e Read).
- **Tipo NON modificabile** (vincolo importante).
- Se tipo=Scala: modifica coppie (aggiungi/rimuovi/modifica, minimo 2).

**Dipendenze**:
- US-FWK-008 (modal modifica accessibile da dettaglio)

**Complessita**: Alta (gestione coppie Scala modificabili + vincolo tipo immutabile)

**Testing**: Testabile con scenari (modifica Campo Libero, modifica Scala aggiungendo coppia, tentativo eliminazione sotto minimo)

---

### 10. US-FWK-010 - Eliminare elemento di valutazione con validazione vincoli (Admin)

**Rationale**:
- Completamento CRUD Elementi (Delete).
- Warning (NON blocco) se elemento utilizzato in framework.
- Cascade delete per coppie Scala.

**Dipendenze**:
- US-FWK-009 (testare prima modifica, poi eliminazione)

**Complessita**: Media (warning utilizzo + cascade delete coppie)

**Testing**: Testabile con scenari (elemento non usato → eliminazione OK, elemento usato → warning)

---

## Sprint 2: Framework Core - CRUD Base + Gestione Righe + Freesolo (Stories 11-14, 15-16)

**Obiettivo Sprint**: Implementare CRUD Framework con gestione righe dinamiche, freesolo autocomplete, e dettaglio/modifica

**Durata stimata**: 14-16 giorni

---

### 11. US-FWK-011 - Visualizzare lista template framework (Admin)

**Rationale**:
- Entry point per gestione Framework.
- Lista con badge stati (Bozza/Pubblicato/Archiviato).
- Menu azioni condizionali per stato.

**Dipendenze**:
- US-FWK-001 a US-FWK-010 (anagrafiche Requisiti ed Elementi devono esistere)

**Complessita**: Media (lista con badge stati + menu azioni condizionali)

**Testing**: Testabile immediatamente (Admin → accede a "Template framework" → vede lista vuota)

---

### 12. US-FWK-012 - Creare nuovo framework con righe e elementi di valutazione (Admin)

**Rationale**:
- Story piu complessa dell'epica. Implementa:
  - Form 3 sezioni (info base, multi-select elementi, gestione righe)
  - Freesolo autocomplete per 4 campi (Ambito, Tematica, Categoria, Misura)
  - Tabella anteprima righe con menu azioni (Modifica/Elimina)
  - Salvataggio con 0 righe consentito (stato Bozza)
- Salvataggio anagrafica suggerimenti freesolo.

**Dipendenze**:
- US-FWK-011 (lista dove appare framework creato)
- US-FWK-002 (select Requisito deve avere almeno 1 requisito)
- US-FWK-007 (multi-select Elementi deve avere almeno 1 elemento)

**Complessita**: Altissima (form complesso + freesolo + tabella anteprima + gestione righe in memoria)

**Testing**: Testabile end-to-end (Admin crea framework vuoto → salva Bozza, Admin crea framework con 3 righe → salva Bozza)

---

### 13. US-FWK-013 - Gestire righe framework - Aggiungi/Modifica/Elimina in tabella anteprima (Admin)

**Rationale**:
- Story dedicata alla gestione CRUD righe nella tabella anteprima (prima del salvataggio finale).
- Implementa:
  - Aggiunta riga: validazione 5 campi → aggiungi a tabella
  - Modifica riga: popolamento form + modalita edit + pulsante "Aggiorna riga"
  - Eliminazione riga: rimozione immediata (no dialog)
- Gestione in memoria (no persistenza fino a "Salva" finale).

**Dipendenze**:
- US-FWK-012 (tabella anteprima presente in creazione framework)

**Complessita**: Alta (gestione stato form + tabella + modalita edit)

**Testing**: Testabile in US-FWK-012 (aggiungi 3 righe, modifica riga 2, elimina riga 1, salva framework)

---

### 14. US-FWK-014 - Gestire freesolo con eliminazione suggerimenti tramite icona X (Admin)

**Rationale**:
- Feature critica per pulizia anagrafica suggerimenti freesolo.
- Implementa:
  - Icona X accanto ad ogni suggerimento nel dropdown
  - Controllo utilizzo suggerimento in framework esistenti
  - Warning se utilizzato (NON blocco)
  - Eliminazione da anagrafica suggerimenti
- Migliora UX evitando accumulo suggerimenti errati.

**Dipendenze**:
- US-FWK-012 (freesolo autocomplete implementato)

**Complessita**: Media (UI icona X + dialog warning + eliminazione da anagrafica)

**Testing**: Testabile end-to-end (Admin crea framework con "Ambito: Prova", poi in nuovo framework apre dropdown Ambito, click X su "Prova" → warning → conferma → suggerimento rimosso)

---

### 15. US-FWK-015 - Visualizzare dettaglio framework in modalita sola lettura (Admin)

**Rationale**:
- Pagina dettaglio read-only necessaria per consultazione framework.
- Mostra:
  - Info base (nome, descrizione, stato, elementi valutazione)
  - Tabella righe read-only (sortable, paginata)
  - Sezione "Utilizzo" (contatore template audit)
- Pulsante "Modifica" disabilitato se stato=Archiviato.

**Dipendenze**:
- US-FWK-012 (serve almeno 1 framework esistente)

**Complessita**: Media (pagina dettaglio con tabella righe + badge stato + contatore utilizzo)

**Testing**: Testabile dopo creazione (Admin crea framework → click nome → vede dettaglio)

---

### 16. US-FWK-016 - Modificare framework esistente (Admin)

**Rationale**:
- Completamento CRUD Framework (dopo Create e Read).
- Riutilizza stessa UI di creazione (US-FWK-012) pre-popolata.
- Tabella righe pre-popolata con righe esistenti.
- Vincolo: framework Pubblicato NON puo salvare con 0 righe.

**Dipendenze**:
- US-FWK-015 (modal modifica accessibile da dettaglio)
- US-FWK-013 (gestione righe riutilizzata)

**Complessita**: Alta (form pre-popolato + gestione righe esistenti + validazione stato)

**Testing**: Testabile in sequenza (crea framework con 2 righe → modifica: aggiungi 1 riga, rimuovi 1 riga → salva → verifica 2 righe totali)

---

## Sprint 3: Stati e Pubblicazione - Gestione Lifecycle Framework (Stories 17-18)

**Obiettivo Sprint**: Implementare gestione stati framework (Bozza → Pubblicato → Archiviato) ed eliminazione con vincoli complessi

**Durata stimata**: 8-10 giorni

---

### 17. US-FWK-017 - Pubblicare framework - cambio stato Bozza → Pubblicato (Admin)

**Rationale**:
- Azione critica che rende framework disponibile ai Consulenti per Template Audit.
- Implementa:
  - Validazione prerequisiti: almeno 1 riga (blocco se 0 righe)
  - Dialog conferma con recap caratteristiche framework
  - Cambio stato Bozza → Pubblicato
  - Timestamp `pubblicato_il`
  - Aggiornamento menu azioni (rimuove "Pubblica", aggiunge "Archivia")

**Dipendenze**:
- US-FWK-012 (creazione framework in Bozza)
- US-FWK-016 (modifica framework per aggiungere righe se necessario)

**Complessita**: Media (validazione righe + dialog conferma + cambio stato + aggiornamento UI)

**Testing**: Testabile con scenari (framework con 0 righe → blocco, framework con 3 righe → pubblicazione OK → badge verde)

---

### 18. US-FWK-018 - Eliminare/Archiviare framework con validazione vincoli (Admin)

**Rationale**:
- Story piu complessa di Sprint 3. Implementa 4 casi d'uso distinti:
  - **CASO 1**: Eliminazione Bozza → dialog conferma standard → hard delete
  - **CASO 2**: Archiviazione Pubblicato NON utilizzato → dialog conferma → cambio stato Archiviato
  - **CASO 3**: Eliminazione Pubblicato utilizzato → BLOCCO + dialog warning → suggerimento archiviazione
  - **CASO 4**: Eliminazione Archiviato → dialog warning forte → hard delete
- Menu azioni condizionali per stato.
- Controllo utilizzo in Template Audit (epica futura).

**Dipendenze**:
- US-FWK-017 (serve framework Pubblicato per testare CASO 2 e 3)
- US-FWK-012 (serve framework Bozza per testare CASO 1)

**Complessita**: Altissima (4 flussi diversi + validazione utilizzo + dialog multipli + cascade delete)

**Testing**: Testabile con scenari multipli:
- CASO 1: Admin crea framework Bozza → elimina → conferma → hard delete
- CASO 2: Admin pubblica framework (0 template audit) → archivia → conferma → stato Archiviato
- CASO 3: Admin tenta eliminare framework Pubblicato con template audit → blocco → dialog warning
- CASO 4: Admin elimina framework Archiviato → warning → conferma → hard delete

---

## Riepilogo Dipendenze Critiche

### Dipendenze Blocking (Story A → Story B)

| Story Prerequisito | Story Dipendente | Motivo |
|-------------------|------------------|--------|
| US-FWK-001 | US-FWK-002 | Lista dove appare requisito creato |
| US-FWK-002 | US-FWK-003 | Serve almeno 1 requisito esistente per visualizzare dettaglio |
| US-FWK-003 | US-FWK-004 | Modal modifica accessibile da dettaglio |
| US-FWK-004 | US-FWK-005 | Testare modifica prima di eliminazione |
| US-FWK-006 | US-FWK-007 | Lista dove appare elemento creato |
| US-FWK-007 | US-FWK-008 | Serve almeno 1 elemento esistente per visualizzare dettaglio |
| US-FWK-008 | US-FWK-009 | Modal modifica accessibile da dettaglio |
| US-FWK-009 | US-FWK-010 | Testare modifica prima di eliminazione |
| US-FWK-001 a US-FWK-010 | US-FWK-011 | Anagrafiche Requisiti ed Elementi devono esistere prima di Framework |
| US-FWK-011 | US-FWK-012 | Lista dove appare framework creato |
| US-FWK-002 | US-FWK-012 | Select Requisito deve avere almeno 1 requisito disponibile |
| US-FWK-007 | US-FWK-012 | Multi-select Elementi deve avere almeno 1 elemento disponibile |
| US-FWK-012 | US-FWK-013 | Tabella anteprima presente in creazione framework |
| US-FWK-012 | US-FWK-014 | Freesolo autocomplete implementato |
| US-FWK-012 | US-FWK-015 | Serve almeno 1 framework esistente per visualizzare dettaglio |
| US-FWK-015 | US-FWK-016 | Modal modifica accessibile da dettaglio |
| US-FWK-013 | US-FWK-016 | Gestione righe riutilizzata in modifica |
| US-FWK-012 | US-FWK-017 | Serve framework in Bozza per pubblicare |
| US-FWK-016 | US-FWK-017 | Modifica framework per aggiungere righe se necessario |
| US-FWK-017 | US-FWK-018 (CASO 2,3) | Serve framework Pubblicato per testare archiviazione/eliminazione |
| US-FWK-012 | US-FWK-018 (CASO 1) | Serve framework Bozza per testare eliminazione |

### Dipendenze Logiche (Suggerite ma non bloccanti)

| Story | Dipendenza Logica | Motivo |
|-------|------------------|--------|
| US-FWK-013 | US-FWK-012 | Gestione righe e parte integrante della creazione, ma testabile separatamente |
| US-FWK-014 | US-FWK-012 | Eliminazione suggerimenti ha senso dopo avere suggerimenti salvati, ma implementabile da subito |

---

## Matrice Sprint vs Complessita

| Sprint | Stories | Story Points Totali (stimati) | Complessita Media | Rischio |
|--------|---------|------------------------------|-------------------|---------|
| Sprint 1 | 10 | 32 | Media | Basso |
| Sprint 2 | 6 | 42 | Alta | Alto |
| Sprint 3 | 2 | 21 | Alta | Medio |
| **TOTALE** | **18** | **95** | **Media-Alta** | **Medio** |

**Legenda Story Points**:
- Bassa: 2 SP
- Media: 3-5 SP
- Alta: 8 SP
- Altissima: 13 SP

**Distribuzione Complessita**:
- Sprint 1: 3 Bassa + 6 Media + 1 Alta = focus su foundation
- Sprint 2: 1 Media + 3 Alta + 2 Altissima = focus su features complesse
- Sprint 3: 1 Media + 1 Altissima = focus su gestione stati

---

## Note Implementative per Sprint

### Sprint 1: Focus su Solidita Anagrafiche

**Obiettivo**: Creare anagrafiche robuste con CRUD completo e validazioni

**Testing**: Unit test + E2E per ogni story

**Priorita**:
- Validazioni univocita (nome requisito, nome elemento)
- Hard delete con warning utilizzo
- Gestione tipo elemento (Campo Libero vs Scala) con campi condizionali
- Blocchi ripetibili per coppie Scala (minimo 2)

**Deliverable**: Admin puo gestire completamente Requisiti ed Elementi di Valutazione

**Rischi**:
- **Rischio 1**: Validazione coppie Scala complessa
  - **Mitigazione**: Test approfonditi su validazione univocita valori numerici + eliminazione sotto minimo 2 coppie

---

### Sprint 2: Focus su Framework Complesso

**Obiettivo**: Implementare creazione/modifica framework con freesolo e gestione righe dinamiche

**Testing**: Test freesolo (suggerimenti + eliminazione X) + test gestione righe (aggiungi/modifica/elimina)

**Priorita**:
- Freesolo autocomplete con anagrafica suggerimenti
- Tabella anteprima righe con operazioni CRUD in memoria
- Modalita edit riga (popolamento form + pulsante "Aggiorna riga")
- Salvataggio atomico (framework + righe + associazioni elementi)

**Deliverable**: Admin puo creare framework completi con righe e associare elementi di valutazione

**Rischi**:
- **Rischio 1**: Gestione stato form riga (creazione vs edit) complessa
  - **Mitigazione**: State machine chiaro per modalita form + reset corretto dopo operazioni
- **Rischio 2**: Freesolo con eliminazione X puo causare confusione UX
  - **Mitigazione**: Dialog conferma + warning utilizzo + test UX con utenti reali
- **Rischio 3**: Tabella anteprima con operazioni in memoria puo avere bugs (perdita dati)
  - **Mitigazione**: Test approfonditi su operazioni multiple (aggiungi 5, modifica 2, elimina 1, salva → verifica 6 righe)

---

### Sprint 3: Focus su Stati e Lifecycle

**Obiettivo**: Implementare gestione completa stati framework e vincoli eliminazione

**Testing**: Test cambio stati + test 4 casi eliminazione/archiviazione

**Priorita**:
- Validazione prerequisiti pubblicazione (almeno 1 riga)
- Cambio stato con timestamp dedicati (pubblicato_il, archiviato_il)
- Menu azioni condizionali per stato
- 4 flussi eliminazione/archiviazione distinti

**Deliverable**: Framework con lifecycle completo (Bozza → Pubblicato → Archiviato → Eliminato)

**Rischi**:
- **Rischio 1**: 4 flussi eliminazione complessi da testare
  - **Mitigazione**: Test matrix con tutti gli scenari (Bozza eliminazione, Pubblicato archiviazione, Pubblicato eliminazione con utilizzo, Archiviato eliminazione)
- **Rischio 2**: Controllo utilizzo in Template Audit (epica futura) puo non essere implementato
  - **Mitigazione**: Mock controllo utilizzo per test + documentazione per epica Audit

---

## Rischi e Mitigazioni Generali

### Rischio 1: Freesolo Autocomplete Complessita (Sprint 2)

**Descrizione**: Freesolo con suggerimenti + eliminazione X + salvataggio nuovi valori e feature complessa

**Mitigazione**:
- Implementare anagrafica suggerimenti separata (tabella dedicata per Ambito, Tematica, Categoria, Misura)
- Test approfonditi su:
  - Suggerimenti case-insensitive
  - Eliminazione con X (warning se utilizzato)
  - Salvataggio automatico nuovi valori al save framework
- Validazione univocita suggerimenti

### Rischio 2: Gestione Righe Framework in Memoria (Sprint 2)

**Descrizione**: Operazioni CRUD righe in tabella anteprima (prima del salvataggio finale) possono avere bugs di stato

**Mitigazione**:
- State management robusto (Redux/Context per gestione righe in memoria)
- Test scenario complessi:
  - Aggiungi 5 righe → modifica riga 2 → elimina riga 4 → annulla modifica → salva → verifica 4 righe corrette
  - Crea framework con 3 righe → modifica framework → aggiungi 2 righe, modifica 1 esistente, elimina 1 esistente → salva → verifica 4 righe totali
- Validazione salvataggio atomico (rollback se errore)

### Rischio 3: Tipo Elemento Non Modificabile (Sprint 1)

**Descrizione**: Vincolo "tipo elemento non modificabile" puo causare frustrazione utente se sceglie tipo sbagliato

**Mitigazione**:
- Dialog warning chiaro quando cambio tipo in creazione (prima del salvataggio): "Cambiando tipo perderai i dati inseriti. Continuare?"
- Nota informativa evidente in pagina modifica: "Il tipo di elemento non puo essere modificato dopo la creazione."
- Documentazione utente con esempio: "Se hai creato Campo Libero per errore, elimina l'elemento e ricrealo come Scala."

### Rischio 4: Stati Framework Confusione (Sprint 3)

**Descrizione**: 3 stati (Bozza/Pubblicato/Archiviato) + 4 flussi eliminazione possono confondere utenti

**Mitigazione**:
- Badge colorati chiari (grigio Bozza, verde Pubblicato, arancione Archiviato)
- Dialog esplicativi per ogni azione:
  - Pubblica: "Sara visibile ai Consulenti"
  - Archivia: "Non sara piu visibile per nuovi template"
  - Elimina: 4 dialog diversi per ogni caso
- Documentazione dettagliata con diagramma stati

### Rischio 5: Performance con Molte Righe Framework (Sprint 2)

**Descrizione**: Framework con 100+ righe puo avere performance degradata in tabella anteprima

**Mitigazione**:
- Paginazione tabella anteprima (5 righe per pagina in creazione, 10 in dettaglio)
- Lazy loading righe in modifica
- Validazione max righe (es: 500 righe) con warning a 400

---

## Definition of Done per Story

Ogni story e considerata COMPLETA quando:

1. **Codice**:
   - Implementazione completa secondo criteri accettazione
   - Code review completata e approvata
   - Nessun warning/error critico

2. **Testing**:
   - Unit test scritti e passanti (coverage >80%)
   - E2E test per flussi principali
   - Test edge cases documentati
   - Test validazioni (univocita, required, formati)

3. **Documentazione**:
   - API endpoints documentati (se nuovi)
   - Commenti codice per logica complessa
   - README aggiornato (se nuove dipendenze)

4. **UI/UX**:
   - Mockup/wireframe rispettati (page_38-42.png)
   - Responsive design testato (mobile, tablet, desktop)
   - Accessibilita base rispettata (WCAG 2.1 Level A)

5. **Validazioni**:
   - Validazioni frontend + backend implementate
   - Messaggi errore user-friendly
   - Edge cases gestiti

6. **Performance**:
   - Query ottimizzate (no N+1)
   - Lazy loading implementato (se liste lunghe)
   - Debounce su ricerche testuali (300ms)

7. **Security**:
   - Input sanitizzati (SQL injection, XSS)
   - Autenticazione/Autorizzazione verificate
   - Solo Admin accede a CRUD anagrafiche

8. **Deploy**:
   - Branch mergiato su main
   - Deploy su staging completato
   - Smoke test su staging passanti

---

## Sequenza di Testing Ottimale

### Dopo Sprint 1 (Anagrafiche)

**Test E2E Critici**:
1. Admin crea 5 requisiti → verifica lista → modifica requisito 2 → elimina requisito 4 → verifica 4 rimanenti
2. Admin crea elemento tipo "Campo Libero" → verifica dettaglio → modifica nome → verifica
3. Admin crea elemento tipo "Scala" con 4 coppie → verifica dettaglio → modifica: aggiungi coppia, modifica valore coppia 2 → verifica 5 coppie
4. Admin tenta eliminare coppia Scala fino a 1 coppia → sistema blocca con errore "Minimo 2 coppie"
5. Admin crea requisito "Req1", lo usa in framework (Sprint 2), tenta eliminare "Req1" → warning ma eliminazione consentita

### Dopo Sprint 2 (Framework Core)

**Test E2E Critici**:
1. Admin crea framework "NIS2" con 0 righe → salva Bozza → verifica stato Bozza + 0 righe
2. Admin crea framework "CIS Controls" con 5 righe (usa freesolo per Ambito/Tematica/Categoria/Misura + select Requisito) → salva Bozza → verifica 5 righe + suggerimenti salvati
3. Admin modifica framework "CIS Controls": aggiungi 2 righe, modifica riga 3 (cambia Ambito), elimina riga 1 → salva → verifica 6 righe totali con modifiche corrette
4. Admin apre dropdown Ambito in nuovo framework → vede suggerimento "Ambito1" → click X → warning (usato in framework "CIS Controls") → conferma → suggerimento rimosso
5. Admin crea framework con riga duplicata (stessi 5 campi) → sistema permette (no validazione univocita riga)

### Dopo Sprint 3 (Stati e Pubblicazione)

**Test E2E Critici**:
1. Admin crea framework Bozza con 0 righe → tenta pubblicare → blocco "Aggiungi almeno 1 riga"
2. Admin crea framework Bozza con 3 righe → pubblica → verifica stato Pubblicato + badge verde + timestamp pubblicato_il
3. Admin pubblica framework "FW1" (NON usato in template audit) → archivia → verifica stato Archiviato + badge arancione + pulsante Modifica disabilitato
4. Admin tenta eliminare framework Pubblicato "FW2" (usato in 2 template audit) → blocco con dialog "Utilizzato in 2 template" + pulsante "Archivia framework"
5. Admin elimina framework Archiviato "FW3" → warning forte → conferma → hard delete → verifica rimosso da lista

---

## Checklist Pre-Implementazione

Prima di iniziare ogni sprint, verificare:

- [ ] Tutte le dipendenze bloccanti completate (vedi matrice dipendenze)
- [ ] Mockup/wireframe disponibili (page_38-42.png)
- [ ] Database schema aggiornato (tabelle: requisiti, elementi_valutazione, framework, righe_framework, suggerimenti_freesolo)
- [ ] API endpoints pianificati (REST CRUD per ogni entita)
- [ ] Environment di staging pronto
- [ ] Admin user creato per test (da epica Anagrafiche)
- [ ] Definition of Done condivisa e compresa
- [ ] Test data preparati (es: 10 requisiti, 5 elementi valutazione per testare framework)

---

## Metriche di Successo per Epica

Al completamento dei 3 sprint, il sistema deve:

1. **Gestione Requisiti**:
   - [x] CRUD completo Requisiti (lista, crea, dettaglio, modifica, elimina)
   - [x] Validazione univocita nome
   - [x] Warning utilizzo in framework (ma eliminazione consentita)
   - [x] Hard delete con graceful degradation

2. **Gestione Elementi di Valutazione**:
   - [x] CRUD completo Elementi (lista, crea, dettaglio, modifica, elimina)
   - [x] Tipo "Campo Libero" con 2 campi (nome campo, max lunghezza)
   - [x] Tipo "Scala" con coppie dinamiche (minimo 2, valore numerico + label)
   - [x] Tipo non modificabile dopo creazione
   - [x] Warning utilizzo in framework (ma eliminazione consentita)
   - [x] Cascade delete coppie Scala

3. **Gestione Framework**:
   - [x] CRUD completo Framework (lista, crea, dettaglio, modifica, elimina/archivia)
   - [x] Multi-select elementi di valutazione
   - [x] Gestione righe con 5 campi (4 freesolo + 1 select requisito)
   - [x] Freesolo autocomplete con suggerimenti + icona X eliminazione
   - [x] Tabella anteprima righe con operazioni CRUD in memoria
   - [x] Modalita edit riga (popolamento form + pulsante "Aggiorna riga")
   - [x] Salvataggio con 0 righe consentito (stato Bozza)

4. **Gestione Stati Framework**:
   - [x] 3 stati: Bozza, Pubblicato, Archiviato
   - [x] Pubblicazione con validazione (almeno 1 riga)
   - [x] Archiviazione framework Pubblicato
   - [x] Eliminazione Bozza (hard delete)
   - [x] Eliminazione Pubblicato bloccata se utilizzato (solo archiviazione)
   - [x] Eliminazione Archiviato con warning (hard delete)

5. **Validazioni**:
   - [x] Nome requisito univoco
   - [x] Nome elemento univoco
   - [x] Nome framework univoco
   - [x] Coppie Scala: minimo 2, valori numerici univoci
   - [x] Framework Pubblicato: minimo 1 riga
   - [x] Suggerimenti freesolo univoci (case-insensitive)

6. **UX**:
   - [x] Freesolo autocomplete con suggerimenti
   - [x] Icona X per eliminazione suggerimenti
   - [x] Tabella anteprima righe con menu azioni
   - [x] Badge colorati per stati framework
   - [x] Dialog conferma/warning per azioni critiche
   - [x] Notifiche toast per feedback utente

7. **Performance**:
   - [x] Paginazione su tutte le liste (8/16/24 rows)
   - [x] Debounce su filtri ricerca (300ms)
   - [x] Lazy loading righe framework (se >100 righe)

---

## Conclusione

L'ordine di implementazione proposto permette di:

1. **Costruire anagrafiche solide** (Sprint 1) prima di framework complesso
2. **Testare freesolo e gestione righe** (Sprint 2) in modo incrementale
3. **Gestire stati e lifecycle** (Sprint 3) solo dopo validare base funzionante

**Durata totale stimata**: 32-38 giorni (circa 7-8 settimane con team 6/7 persone)

**Raccomandazione**: Eseguire **Sprint Review** e **Retrospettiva** alla fine di ogni sprint per validare completezza e adattare planning successivo se necessario.

**Note Epica Futura (Audit)**:
- Framework Pubblicati saranno visibili ai Consulenti per creare Template Audit
- Template Audit useranno Framework come blueprint (read-only)
- Eliminazione Framework Pubblicato bloccata se utilizzato in Template Audit attivi

---

_Documento creato da: Delivery Manager Agent_
_Ultima revisione: 2025-12-11_
_Versione: 1.0_
