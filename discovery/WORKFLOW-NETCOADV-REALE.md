# WORKFLOW NETCOADV - Come Lavorano Oggi

**Data**: 2025-12-10
**Versione**: 1.0
**Fonte**: Relazione IT Assessment "Luce sul Mare" (cliente NetcoADV)

---

## 🎯 COSA FA NETCOADV

NetcoADV è una **società di consulenza cybersecurity** che:

1. Va dai clienti aziendali (es: "Luce sul Mare srl")
2. Fa un **IT Assessment** (valutazione sicurezza informatica)
3. Produce una **relazione completa** con:
   - Valutazione rischi
   - GAP Analysis vs NIS2
   - Piano azioni correttive
4. Consegna la relazione al cliente

---

## 📋 IL PROCESSO ATTUALE

### FASE 1: Preparazione Assessment

NetcoADV prepara l'audit usando un **Framework** predefinito:

**Framework Nazionale Cybersecurity 2025** che combina:

- **NIST Cybersecurity Framework** (6 funzioni, 23 categorie, 71 codici/misure)
- **Direttiva NIS2** (16 ambiti politiche, requisiti normativi)

```
FRAMEWORK NAZIONALE 2025
├─ NIST CSF (Valutazione Rischi)
│  ├─ 6 Funzioni: GV, ID, PR, DE, RS, RC
│  ├─ 23 Categorie: GV.OC, GV.RM, ID.RA, ...
│  └─ 71 Codici/Misure: GV.OC-04, GV.RM-03, ...
│
└─ NIS2 (Compliance Normativa)
   ├─ 16 Ambiti Politiche: a-p (art.21)
   │  a) Gestione del rischio
   │  b) Ruoli e responsabilità
   │  c) Affidabilità risorse umane
   │  ...
   └─ Requisiti specifici per ogni Codice/Misura
```

---

### FASE 2: Esecuzione Assessment presso Cliente

Il consulente NetcoADV va dal cliente e compila **DUE TIPI di questionari**:

#### A) QUESTIONARIO DI PERIMETRO

**Scopo**: Inventario asset informatici
**Contenuto**:

- Nr dispositivi aziendali
- Nr server fisici/virtuali
- Nr firewall, router, switch
- Esistenza backup, protezione antivirus
- Gestione rete (VLAN, WiFi)

**Output**: Allegato "Questionario di Perimetro" (screenshot pagina 7 relazione)

---

#### B) QUESTIONARIO PER FUNZIONI

**Scopo**: Valutazione implementazione misure tecniche/organizzative

**Struttura**:

```
Per ogni CODICE/MISURA del framework:
├─ Titolo Tematica (es: "Gestione del rischio informatico")
├─ Tematica (descrizione lunga del controllo)
├─ Situazione riscontrata (valutazione consulente)
├─ Grado copertura (scala 0.0-1.0)
│  0.0 = Nullo
│  0.2 = Insufficiente
│  0.4 = Iniziale
│  0.6 = Incompleto
│  0.8 = Avanzato
│  1.0 = Completo
├─ Probabilità rischio (1-4: Bassa, Media, Alta, Molto alta)
├─ Danno (1-4: Lieve, Modesto, Grave, Molto grave)
└─ Indice rischio (P × D = 1-16)
```

**Calcolo Probabilità "P"**:

- P è influenzata dal **Grado di copertura** del controllo:
  - Grado 1.0 → Probabilità 1 (Bassa)
  - Grado 0.8 → Probabilità 2 (Media)
  - Grado 0.4-0.6 → Probabilità 3 (Alta)
  - Grado 0.0-0.2 → Probabilità 4 (Molto alta)

**Esempio concreto**:

```
Codice: GV.OC-04
Titolo: Consapevolezza del Sistema Informativo aziendale
Situazione: "L'azienda ha un sistema di scansione automatico della rete
             ed una reportistica continuamente aggiornata."
Grado copertura: 1,0 - Completo
Probabilità: 1 - Bassa
Danno: 3 - Grave
Indice rischio: 3 - Basso (verde)
```

**Output**: Allegato "01-Questionario per Funzioni" (quello che hai negli screenshots)

---

### FASE 3: GAP Analysis NIS2

Dopo il questionario, il consulente fa la **GAP Analysis** per valutare la **conformità normativa**.

**Struttura**:

```
Per ogni AMBITO POLITICHE NIS2:
  Per ogni CODICE/MISURA:
    Per ogni REQUISITO:
      ├─ Requisito (testo normativo)
      ├─ Stato attuale (valutazione consulente)
      ├─ Grado compliance (scala 0-3)
      │  0 = Compliant (conforme)
      │  1 = Parziale (parzialmente conforme)
      │  2 = Minimale (conforme in modo limitato)
      │  3 = Assente (non conforme)
      │
      └─ Azioni/Mitigazioni (SE compliance > 0):
         ├─ Priorità (Obbligatoria, Prioritaria, Fortemente consigliata, Consigliata, Facoltativa)
         ├─ Descrizione azione (cosa fare)
         ├─ Assegnatario (chi esegue)
         ├─ Responsabile (chi supervisiona)
         ├─ Referente aziendale
         ├─ Da informare
         ├─ Stato avanzamento
         ├─ Scadenza
         └─ Concluso il
```

**Esempio concreto**:

```
Ambito politiche: a) Gestione del rischio
Funzione: (GV) GOVERNO
Categoria: (GV.RM) Strategia di gestione del rischio
Codice/Misura: GV.RM-03

  Requisito 1:
  "Nell'ambito dei processi di gestione del rischio del soggetto NIS
   e nel rispetto delle politiche di cui alla misura GV.PO-01, è definito,
   attuato, aggiornato e documentato un piano di gestione dei rischi..."

  Stato attuale: "Sì è definito un DPIA, da implementare nell'ottica NIS"

  Grado compliance: 1 - Parziale

  Azioni/Mitigazioni:
    [Priorità: Obbligatoria]
    Descrizione: "Redigere, adottare e documentare un insieme completo
                  di politiche di sicurezza informatica che coprano tutti
                  gli ambiti indicati, in linea con l'art. 21 della
                  direttiva NIS2..."
    Assegnatario: [da compilare]
    Responsabile: [da compilare]
    Scadenza: [da compilare]

    [Priorità: Fortemente consigliata]
    Descrizione: "Stilare procedure sotto la supervisione di Consulenti
                  specializzati in ambito NIS2"
```

**Output**: Allegati GAP Analysis (05-09: per Ambito, per Azioni, per Codice, per Incaricato)

---

### FASE 4: Generazione Relazione Finale

Il consulente produce una **Relazione completa** (21 pagine) con:

1. **Sezione IT Assessment**:

   - Introduzione metodologia
   - Questionario di perimetro
   - Questionario per funzioni
   - Tabella sintesi codici/misure
   - Legenda grado copertura (0.0-1.0)
   - Calcolo indice rischio (P×D)

2. **Sezione GAP Analysis**:

   - Sintesi requisiti NON compliance
   - Sintesi requisiti e numero azioni
   - GAP Analysis per Ambito NIS2
   - GAP Analysis per Azioni
   - GAP Analysis per Codice
   - GAP Analysis per Incaricato
   - Elenco azioni per Requisito e Sede

3. **Sezione Panorama Sicurezza**:
   - Raccomandazioni per area:
     - Governance e Politiche
     - Gestione Rischio
     - Formazione Personale
     - Asset Management
     - Vulnerability Management
     - Continuità Operativa
     - Backup
     - Incident Response

**Output**: Relazione PDF completa consegnata al cliente

---

## 🗄️ STRUMENTI ATTUALI

### Database Access

NetcoADV usa un **database Microsoft Access** per gestire:

**Tabelle Anagrafica Framework**:

- `db_anagrafica_codici_NIS2` (71 codici/misure)
- `db_anagrafica_requisiti_NIS2` (145 requisiti)
- `db_servizio_grado_copertura_NIS2` (scala 0.0-1.0)
- `db_servizio_grado_compliance_NIS2` (scala 0-3)

**Tabelle Valutazioni Audit**:

- `db_sedi_codici_mtom_NIS2` (valutazioni Grado copertura per Codice)
- `db_sedi_requisiti_mtom_NIS2` (valutazioni Grado compliance per Requisito)

**Tabelle Azioni Correttive**:

- `db_anagrafica_azioni_NIS2` (catalogo azioni riutilizzabili)
- `db_requisiti_azioni_mtom_NIS2` (assignment azioni a requisiti)

**Generazione Report**:

- Query Access + export PDF/Excel
- Template PDF predefiniti

---

## 🎯 COSA VUOLE NETCOADV DALLA NUOVA PIATTAFORMA

### Problema Attuale

1. **Framework rigido**: Access ha hardcoded il Framework Nazionale 2025
2. **Non riutilizzabile**: Se domani serve ISO 27001 o GDPR, devono rifare tutto il database
3. **Non scalabile**: Ogni nuovo standard = nuovo database Access
4. **Non collaborativo**: 1 consulente alla volta può lavorare sul database

### Richiesta Cliente

> **"Voglio una piattaforma dove io (Admin) possa CREARE FRAMEWORK configurabili,
> che poi i miei consulenti possono usare come base per gli audit"**

Nello specifico:

#### Come ADMIN (responsabile tecnico NetcoADV):

1. **Creo Framework base** (es: "Framework NIS2 2025", "ISO 27001:2022", "GDPR Compliance")
2. **Definisco la struttura gerarchica**:
   - Ambiti / Funzioni / Categorie / Codici / Requisiti
   - Scale valutazione (es: 0.0-1.0 per NIS2, 1-5 per ISO)
   - Formule calcolo rischio
3. **Pubblico il Framework** → diventa disponibile per i consulenti

#### Come CONSULENTE (chi va dai clienti):

1. **Vedo lista Framework pubblicati** dall'Admin
2. **Clono un Framework in "Template Audit"** personalizzato
3. **Modifico il Template** se necessario:
   - Rimuovo requisiti non applicabili al cliente
   - Aggiungo note/commenti
   - Cambio ordine per seguire il flusso intervista
4. **Creo Audit dal Template** per una specifica Azienda/Sede
5. **Compilo valutazioni** durante l'audit presso cliente
6. **Genero report automatici** (Questionario, GAP Analysis, Piano Azioni)

---

## 🔑 ELEMENTI CHIAVE DA MODELLARE

### 1. FRAMEWORK (creato da Admin)

```
Framework
├─ Nome: "Framework Nazionale Cybersecurity 2025"
├─ Descrizione: "Combinazione NIST CSF + NIS2"
├─ Stato: Bozza / Pubblicato / Archiviato
└─ Struttura gerarchica:
   ├─ Ambiti (es: "a) Gestione del rischio")
   ├─ Funzioni (es: "GV - GOVERNO")
   ├─ Categorie (es: "GV.RM - Strategia gestione rischio")
   ├─ Codici/Misure (es: "GV.RM-03: Le attività e gli esiti...")
   └─ Requisiti (es: "Requisito 1: Nell'ambito dei processi...")
```

### 2. SCALE VALUTAZIONE

```
Scala "Grado Copertura NIS2" (0.0-1.0)
├─ 0,0 - Nullo: "Il controllo non è implementato..."
├─ 0,2 - Insufficiente: "Implementazione iniziale..."
├─ 0,4 - Iniziale: "Parzialmente implementato..."
├─ 0,6 - Incompleto: "Implementazione significativa..."
├─ 0,8 - Avanzato: "Ampiamente implementato..."
└─ 1,0 - Completo: "Completamente implementato"

Scala "Grado Compliance NIS2" (0-3)
├─ 0 - Compliant: "Requisito pienamente soddisfatto"
├─ 1 - Parziale: "Requisito soddisfatto in parte"
├─ 2 - Minimale: "Soddisfatto in modo limitato"
└─ 3 - Assente: "Requisito non soddisfatto"
```

### 3. TEMPLATE AUDIT (snapshot Framework modificabile da Consulente)

```
Template Audit
├─ Nome: "NIS2 PMI Settore Turistico"
├─ Framework origine: "Framework Nazionale 2025"
├─ Modificabile: true/false
├─ Creato da: Consulente X
└─ Righe (subset/modifica del Framework):
   ├─ GV.OC-04 → Requisito 1 [INCLUSO]
   ├─ GV.RM-03 → Requisito 1 [INCLUSO]
   ├─ ID.RA-05 → Requisito 1 [INCLUSO]
   ├─ ID.RA-05 → Requisito 2 [INCLUSO]
   ├─ ID.RA-05 → Requisito 3 [ESCLUSO - non applicabile]
   └─ ID.RA-05 → Requisito 4 [INCLUSO]
```

### 4. AUDIT (esecuzione Template presso Azienda Cliente)

```
Audit
├─ Template: "NIS2 PMI Settore Turistico"
├─ Azienda Cliente: "Luce sul Mare srl"
├─ Sede: "Igea Marina"
├─ Livello assessment: Importante
├─ Consulente: Umberto Borla
├─ Data: 29/10/2025
└─ Valutazioni (per ogni riga Template):
   ├─ Codice GV.OC-04:
   │  ├─ Situazione riscontrata: "L'azienda ha un sistema..."
   │  ├─ Grado copertura: 1,0
   │  ├─ Probabilità: 1
   │  ├─ Danno: 3
   │  └─ Indice rischio: 3
   ├─ Requisito GV.RM-03-1:
   │  ├─ Stato attuale: "Sì è definito un DPIA..."
   │  ├─ Grado compliance: 1 - Parziale
   │  └─ Azioni:
   │     ├─ Azione 1: [Priorità Obbligatoria] "Redigere politiche..."
   │     └─ Azione 2: [Priorità Fortemente consigliata] "Stilare procedure..."
```

### 5. AZIONI CORRETTIVE

```
Azione Correttiva
├─ Descrizione: "Redigere, adottare e documentare un insieme completo..."
├─ Priorità: Obbligatoria
├─ Requisito riferimento: GV.RM-03 - Requisito 1
├─ Assegnatario: [da definire]
├─ Responsabile: [da definire]
├─ Referente aziendale: [da definire]
├─ Da informare: [da definire]
├─ Stato avanzamento: [vuoto]
├─ Scadenza: [vuoto]
└─ Concluso il: [vuoto]
```

---

## 📊 REPORT DA GENERARE

La piattaforma deve produrre questi report (attualmente fatti in Access):

### 1. Questionario di Perimetro

- Asset inventory
- Protezioni software
- Backup
- Gestione rete

### 2. Questionario per Funzioni

- Raggruppato per Funzione NIST (GV, ID, PR, DE, RS, RC)
- Lista Codici/Misure con:
  - Tematica
  - Situazione riscontrata
  - Grado copertura
  - Probabilità, Danno, Indice rischio
- Evidenzia codici con rischio Medio/Alto/Grave

### 3. Sintesi Codici/Misure

- Tabella aggregata per Tematica
- Stato attuale requisito
- Grado copertura
- Indice rischio

### 4. Sintesi Requisiti non Compliance

- Lista requisiti con Grado compliance > 0
- Evidenzia GAP da colmare

### 5. Sintesi Requisiti e Numero Azioni

- Per ogni requisito non compliant
- Nr azioni associate
- Priorità azioni

### 6. GAP Analysis per Ambito NIS2

- Raggruppato per Ambito politiche (a-p)
- Per ogni Codice/Misura:
  - Requisiti
  - Grado compliance
  - Azioni correttive

### 7. GAP Analysis per Azioni

- Raggruppato per Priorità
- Descrizione azione
- Responsabilità
- Scadenze

### 8. GAP Analysis per Codice

- Raggruppato per Codice/Misura
- Tutti i requisiti del codice
- Azioni associate

### 9. GAP Analysis per Incaricato

- Raggruppato per Assegnatario
- Lista azioni da eseguire
- Scadenze

### 10. Elenco Azioni per Requisito e Sede

- Vista completa azioni
- Filtri per Sede/Requisito

---

## 🎯 CONCLUSIONE

NetcoADV vuole passare da:

- ❌ Framework hardcoded in Access
- ❌ 1 database per ogni standard
- ❌ Lavoro isolato locale

A:

- ✅ Framework configurabili da Admin
- ✅ Riutilizzo framework per qualsiasi standard (NIS2, ISO, GDPR, ...)
- ✅ Collaborazione cloud tra consulenti
- ✅ Template personalizzabili per settore/dimensione cliente
- ✅ Report automatici e consistenti

---

**Fine Workflow**
