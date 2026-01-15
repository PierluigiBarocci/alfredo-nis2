# EPICA: Gestione Framework Dinamici

**Versione**: 2.0
**Data**: 2025-12-10
**Autore**: Design Thinking Session
**Stato**: ✅ Aggiornato

---

## 🎯 Obiettivo dell'Epica

Permettere all'**Admin di Piattaforma** di creare, gestire e pubblicare **Framework configurabili** (es: NIS2, ISO 27001, GDPR, CIS Controls, o framework custom) che i **Consulenti** potranno poi clonare e utilizzare come base per gli audit presso i clienti.

---

## 🧭 Contesto di Business

### Problema Attuale

NetcoADV (cliente) oggi usa un database Access con framework **hardcoded** (NIST CSF + NIS2). Ogni nuovo standard richiede un nuovo database. Non è scalabile né riutilizzabile.

### Soluzione Richiesta

Una piattaforma dove:

- **Admin** crea framework configurabili con struttura gerarchica personalizzabile
- **Admin** definisce scale di valutazione custom per ogni framework
- **Admin** pubblica framework e diventa disponibile per i Consulenti
- **Consulenti** clonano framework in "Template Audit" e li personalizzano
- **Consulenti** usano template per creare audit presso clienti

### Benefici

- Riutilizzo framework per qualsiasi standard (NIS2, ISO, GDPR, ...)
- Admin può creare framework 1:1 con standard esistenti o completamente custom
- Flessibilità totale: valori gerarchici liberi (pattern "freesolo")
- Scale valutazione personalizzabili per ogni framework
- Versioning implicito: clone per modifiche post-pubblicazione

---

## 📐 Struttura Framework

### Come Funziona la Gerarchia

Ogni Framework è organizzato in una struttura gerarchica a **5 livelli più requisiti**. Immagina di costruire un albero: partiamo dal tronco (Framework) e scendiamo fino alle foglie (Requisiti).

**Esempio concreto - Framework NIS2**:

Il Framework si chiama "NIS2 Direttiva UE 2022/2555". Dentro questo framework troviamo:

- Un **Ambito** chiamato "a) Gestione del rischio"
- Dentro questo Ambito c'è una **Tematica** chiamata "Monitoraggio cyber security"
- La Tematica contiene una **Categoria** chiamata "GV.RM - Gestione del Rischio"
- Dentro la Categoria c'è una **Misura** specifica chiamata "GV.RM-03"
- Infine, la Misura è associata a un **Requisito** preso dall'anagrafica globale: "Inventario asset informatici aggiornato"

**I 5 livelli gerarchici sono**:

1. **Ambito** - Il macro-tema normativo (es. "a) Gestione del rischio", "b) Ruoli e responsabilità")
2. **Tematica** - L'area specifica dentro l'ambito (es. "Monitoraggio cyber security", "Incident response")
3. **Categoria** - Il raggruppamento di controlli (es. "GV.RM - Gestione del Rischio")
4. **Misura** - Il codice specifico del controllo (es. "GV.RM-03")
5. **Requisito** - La descrizione dettagliata selezionata dall'anagrafica globale

**Come funziona in pratica**:

- I primi 4 livelli (Ambito, Tematica, Categoria, Misura) sono **campi liberi**: l'Admin può digitare qualsiasi valore
- Il sistema suggerisce valori già usati in altri framework (autocomplete), ma l'Admin può sempre inserire valori nuovi
- Il **Requisito** invece deve essere **selezionato** dall'anagrafica globale (non può essere digitato liberamente)
- Tutti i livelli sono opzionali tranne il Requisito che è obbligatorio

---

## 🎨 Pattern Freesolo

### Cos'è?

Un campo di input intelligente che:

1. Mostra suggerimenti da valori già usati in precedenza (autocomplete)
2. Permette di digitare un valore completamente nuovo
3. Salva il nuovo valore per suggerirlo in futuro

### Esempio Pratico

Quando l'Admin compila il campo "Ambito":

- **Prima volta**: Digita "a) Gestione del rischio" e il sistema salva questo valore
- **Seconda volta** (in un altro framework): Inizia a digitare "a) Ges..." e il sistema gli suggerisce "a) Gestione del rischio"
- **Terza volta**: Digita "b) Ruoli e responsabilità" e il sistema salva anche questo nuovo valore

### Perché è utile?

- **Flessibilità totale**: L'Admin può inventare qualsiasi struttura senza vincoli
- **Consistenza**: Il sistema suggerisce valori già usati per evitare duplicati accidentali come "Governance" vs "GOVERNANCE"
- **Velocità**: L'autocomplete riduce la digitazione ripetitiva

---

## ⚖️ Scale Valutazione

### Cosa Sono?

Le scale valutazione sono strumenti numerici o qualitativi che i Consulenti useranno per valutare i requisiti durante gli audit. Ogni scala ha diversi livelli, ognuno con un valore e una descrizione.

### Esempi di Scale

**Scala NIS2 - Grado Copertura (valori da 0.0 a 1.0)**:

- 0,0 = Nullo (il controllo non è implementato)
- 0,2 = Insufficiente (implementazione iniziale)
- 0,4 = Iniziale (parzialmente implementato)
- 0,6 = Incompleto (implementazione significativa ma non completa)
- 0,8 = Avanzato (implementato con lacune minori)
- 1,0 = Completo (completamente implementato)

**Scala NIS2 - Grado Compliance (valori da 0 a 3)**:

- 0 = Compliant (conforme)
- 1 = Parziale (parzialmente conforme)
- 2 = Minimale (conformità minimale)
- 3 = Assente (non conforme)

**Scala ISO 27001 Maturità (valori da 1 a 5)**:

- 1 = Non implementato
- 2 = Pianificato
- 3 = Parzialmente implementato
- 4 = Implementato
- 5 = Implementato e ottimizzato

### Come si Associano ai Framework

Un framework può usare **una o più scale** contemporaneamente. Ad esempio, il Framework NIS2 usa:

- Scala "Grado Copertura 0.0-1.0" per valutare l'implementazione tecnica delle misure
- Scala "Grado Compliance 0-3" per valutare la conformità normativa
- Scala "Probabilità Rischio 1-4" per valutare la probabilità di un rischio
- Scala "Danno 1-4" per valutare l'impatto potenziale di un rischio

### Valutazioni Durante l'Audit: CODICI vs REQUISITI

**IMPORTANTE**: Durante l'audit, il Consulente effettua DUE tipi di valutazioni separate:

**1. Valutazioni sui CODICI (Categoria/Misura)**:

- Applicate ai livelli gerarchici (Categoria e Misura)
- Usano la scala "Grado Copertura 0.0-1.0"
- Servono per valutare l'implementazione complessiva di un'area di controllo
- Esempio: La Categoria "GV.RM - Gestione del Rischio" ha copertura 0.6 (Incompleto)

**2. Valutazioni sui REQUISITI**:

- Applicate a ogni singolo requisito
- Usano la scala "Grado Compliance 0-3"
- Servono per valutare la conformità specifica di ogni requisito
- Esempio: Il Requisito "Inventario asset aggiornato" ha compliance 1 (Parziale)

**3. Campo "Situazione Riscontrata"**:

- È un campo testo libero che il Consulente compila durante l'audit
- Descrive la situazione reale trovata presso il cliente
- Esempio: "L'inventario asset esiste ma viene aggiornato solo trimestralmente invece che in tempo reale"
- Aiuta a documentare il contesto e giustificare la valutazione assegnata

**Perché questa divisione?**

La divisione tra valutazioni di CODICI e REQUISITI permette di avere una visione a due livelli:

- **Macro-livello** (CODICI): "Quanto è coperta quest'area di controllo nel complesso?"
- **Micro-livello** (REQUISITI): "Ogni singolo requisito è conforme alla normativa?"

Nei report, questo consente di mostrare sia la copertura complessiva per area sia il dettaglio di conformità per ogni requisito specifico.

---

## 🗂️ Anagrafica Requisiti Globali

### Cos'è?

Un catalogo centrale di **requisiti riutilizzabili** condiviso tra tutti i framework della piattaforma.

### Esempio Pratico

Supponiamo di avere il Requisito Globale con codice "GV.RM-03":

- **Codice**: GV.RM-03
- **Nome**: "Inventario asset aggiornato"
- **Descrizione**: "L'organizzazione deve mantenere un inventario aggiornato di tutti gli asset informatici (hardware, software, dati) con classificazione per criticità."
- **Livello Assessment**: Importante (può essere Essenziale, Importante, o Fuori ambito)

Questo stesso requisito può essere usato in framework diversi:

- Framework NIS2, nella Misura "GV.RM-03"
- Framework ISO 27001, nel Controllo "A.8.1.1"
- Framework CIS Controls, nel Control "1.1"

### Perché è Utile?

- **Evita duplicazione**: Il requisito viene scritto una sola volta, non 3 volte in framework diversi
- **Garantisce consistenza**: Il testo è identico in tutti i framework che lo usano
- **Facilita la manutenzione**: Se serve aggiornare la descrizione, si modifica in un punto solo

### Campo "Livello Assessment" (E/I/F)

Ogni requisito ha un campo "Livello Assessment" con tre possibili valori:

- **E (Essenziale)**: Requisito critico per la conformità
- **I (Importante)**: Requisito rilevante ma non bloccante
- **F (Fuori ambito)**: Requisito non applicabile in determinati contesti

**IMPORTANTE**: Questo campo è **puramente informativo**. Durante l'audit, tutti i requisiti vengono sempre mostrati al Consulente, indipendentemente dal loro livello. Il campo serve solo come indicazione della priorità, ma non filtra né nasconde requisiti.

---

## 📊 Stati Framework

Un Framework può trovarsi in tre stati durante il suo ciclo di vita:

### Stato: BOZZA

**Descrizione**: Framework in fase di creazione o modifica, visibile solo agli Admin di piattaforma.

**Caratteristiche**:

- Modificabile liberamente (l'Admin può cambiare qualsiasi cosa)
- Non visibile ai Consulenti
- Non può essere usato per creare Template Audit
- Può essere salvato anche se incompleto

### Stato: PUBBLICATO

**Descrizione**: Framework completato e approvato, reso disponibile ai Consulenti.

**Caratteristiche**:

- **Completamente immutabile** (non può più essere modificato)
- Visibile a tutti i Consulenti
- Può essere clonato dai Consulenti per creare Template Audit
- Per modificarlo, l'Admin deve creare una nuova versione tramite "Clona"

### Stato: ARCHIVIATO

**Descrizione**: Framework obsoleto o deprecato, non più utilizzabile per nuovi audit.

**Caratteristiche**:

- Non modificabile
- Non visibile ai Consulenti
- Non può essere usato per creare nuovi Template Audit
- Gli audit già esistenti basati su questo framework continuano a funzionare
- Visibile solo agli Admin (per consultazione storica)

### Come Cambiare Stato

**Da Bozza a Pubblicato**:

- L'Admin clicca sul pulsante "Pubblica"
- Il sistema mostra un dialog di conferma che spiega che il framework diventerà immutabile
- Dopo la conferma, il framework diventa Pubblicato e visibile ai Consulenti

**Da Pubblicato ad Archiviato**:

- L'Admin clicca sul pulsante "Archivia"
- Il sistema mostra un dialog di conferma
- Dopo la conferma, il framework viene nascosto ai Consulenti ma rimane disponibile per audit già esistenti

**Non è possibile**:

- Tornare da Pubblicato a Bozza (bisogna clonare il framework)
- Tornare da Archiviato a Pubblicato (bisogna clonare il framework)

### Regola dell'Immutabilità

Quando un framework viene pubblicato, diventa **immutabile** per un motivo importante: garantire che i Template Audit e gli Audit già creati rimangano consistenti. Se l'Admin potesse modificare un framework pubblicato, tutti i Template e Audit basati su quel framework si troverebbero con una struttura cambiata, causando inconsistenze nei dati.

Se l'Admin scopre un errore in un framework pubblicato, deve usare la funzione "Clona" per creare una nuova versione in stato Bozza, modificarla, e poi pubblicarla come versione aggiornata.

---

## 🔄 Versioning Framework (Clonazione)

### Il Problema

L'Admin ha pubblicato il framework "NIS2 2025". Dopo un mese, scopre che manca un requisito importante sui backup. Come fa ad aggiungerlo se il framework pubblicato è immutabile?

### La Soluzione: Clonazione

L'Admin usa la funzione **"Clona"** per creare una copia completa del framework in stato Bozza. Ecco come funziona:

1. L'Admin apre il framework "NIS2 2025" (stato: Pubblicato)
2. Clicca sul pulsante "Clona"
3. Il sistema mostra un dialog che chiede il nome per la nuova versione
4. Il sistema suggerisce automaticamente "NIS2 2025 v2" (ma l'Admin può cambiarlo)
5. L'Admin conferma
6. Il sistema crea un nuovo framework identico all'originale, ma in stato Bozza
7. L'Admin può ora modificare liberamente la nuova versione
8. Quando è pronto, l'Admin pubblica la nuova versione

### Cosa Viene Clonato

Quando si clona un framework, il sistema copia:

- Nome framework (con suffisso "v2", "v3", ecc.)
- Descrizione
- Tutta la struttura gerarchica (tutte le righe con Ambito, Tematica, Categoria, Misura, Requisiti)
- Tutte le scale di valutazione associate
- Tutti i calcoli automatici con le soglie configurate

### Cosa NON Viene Clonato

- L'ID univoco del framework (il clone avrà un ID nuovo)
- Lo stato (il clone parte sempre come Bozza)
- Il timestamp di creazione (il clone avrà la data/ora di quando è stato creato)
- L'autore (il clone viene assegnato all'Admin che lo ha clonato)

### Versioning Implicito

Il sistema non gestisce un campo "versione" esplicito (tipo "v1.0", "v2.0"). Il versioning è **implicito** e basato sul nome del framework. È responsabilità dell'Admin dare nomi significativi che rendano chiaro quale versione sia quale.

Esempi di naming convention consigliate:

- "NIS2 2025", "NIS2 2025 v2", "NIS2 2025 v3"
- "NIS2 Gennaio 2026", "NIS2 Giugno 2026"
- "ISO 27001:2013", "ISO 27001:2022"

### Framework Originale vs Clone

Importante: il framework originale rimane pubblicato e funzionante. I Consulenti che hanno già creato Template Audit basati sull'originale non vengono impattati. Quando la nuova versione viene pubblicata, i Consulenti potranno scegliere quale versione usare per i nuovi Template.

---

## 🎭 Ruoli e Permessi

### Admin Piattaforma

Può fare tutto:

- Creare framework
- Modificare framework in Bozza
- Pubblicare framework
- Archiviare framework
- Clonare framework
- Eliminare framework in Bozza
- Vedere tutti i framework (Bozza, Pubblicati, Archiviati)

### Consulente e Admin-Consulente

Hanno permessi limitati:

- NON possono creare framework
- NON possono modificare framework
- NON possono pubblicare framework
- Possono vedere solo framework Pubblicati
- Possono clonare framework Pubblicati per creare Template Audit personalizzati per i loro clienti

### Utente Aziendale

Non ha accesso ai framework:

- Non può vedere i framework
- Non può fare nulla con i framework
- Vede solo i report degli audit già completati sul proprio cliente

---

## 🎬 FLUSSO COMPLETO: Creazione Framework

Vediamo ora nel dettaglio cosa vede e cosa fa l'Admin per creare un framework completo, passo dopo passo.

### FASE 1: Avvio Creazione Framework

**Scenario**: L'Admin è nella pagina "Framework" che mostra la lista di tutti i framework esistenti.

**Azione**: L'Admin clicca sul pulsante arancione **"+ Nuovo Framework"** in alto a destra.

**Cosa succede**: Il sistema apre una nuova pagina dedicata (non un popup) con il titolo "Crea Nuovo Framework". In alto c'è il breadcrumb "Framework > Nuovo" per aiutare l'Admin a capire dove si trova.

**Cosa vede l'Admin**:

La pagina mostra la **SEZIONE 1: INFORMAZIONI BASE** con due campi:

**Campo "Nome Framework"**:

- È obbligatorio (marcato con asterisco)
- Lunghezza massima 255 caratteri
- Deve essere univoco (non possono esistere due framework con lo stesso nome)
- Placeholder: "Es: Framework Nazionale Cybersecurity 2025"

**Campo "Descrizione"**:

- È opzionale
- Area di testo multiriga
- Lunghezza massima 1000 caratteri
- Placeholder: "Descrivi lo scopo e l'ambito di applicazione del framework"

**Pulsanti disponibili**:

- **Annulla** (in basso a sinistra): Se l'Admin clicca qui, il sistema mostra un dialog di conferma "Sei sicuro di voler annullare? I dati inseriti andranno persi". Se conferma, torna alla lista Framework.
- **Avanti →** (in basso a destra): Valida i campi. Se il nome è vuoto o duplicato, mostra errore. Se tutto OK, passa alla FASE 2.

---

### FASE 2: Costruzione Struttura Framework

**Cosa succede**: Dopo aver cliccato "Avanti", la stessa pagina si aggiorna mostrando la SEZIONE 1 come "completata" (con segno di spunta verde) e apre la **SEZIONE 2: STRUTTURA FRAMEWORK**.

**Cosa vede l'Admin**:

In alto c'è un recap della sezione 1:

- "✓ SEZIONE 1: INFORMAZIONI BASE (completata)"
- "Nome: Framework Nazionale Cybersecurity 2025"
- Pulsante [Modifica] per tornare indietro a modificare nome/descrizione

Poi appare la sezione 2 con:

- Un testo esplicativo: "Aggiungi le righe del framework compilando la tabella qui sotto. Ogni riga rappresenta un requisito valutabile durante l'audit."
- Due pulsanti: **"+ Aggiungi Riga"** e **"Importa da CSV"**
- Una tabella vuota con intestazioni: # | Ambito | Tematica | Categoria | Misura | Requisito
- Un messaggio: "Clicca '+ Aggiungi Riga' per iniziare"

#### Come Aggiungere una Riga

**L'Admin clicca "+ Aggiungi Riga"**

Il sistema apre un modal (popup) con il titolo "Aggiungi Riga Framework" e un testo esplicativo: "Compila i 5 livelli gerarchici. I campi sono opzionali tranne Requisito."

**Campi nel modal**:

1. **Ambito** (campo freesolo con autocomplete)

   - Placeholder: "Es: a) Gestione del rischio"
   - Suggerimenti: Se l'Admin inizia a digitare, il sistema mostra valori già usati in altri framework
   - L'Admin può selezionare un suggerimento oppure digitare un valore completamente nuovo

2. **Tematica** (campo freesolo con autocomplete)

   - Placeholder: "Es: Monitoraggio cyber security"
   - Funziona come Ambito

3. **Categoria** (campo freesolo con autocomplete)

   - Placeholder: "Es: GV.RM - Gestione del Rischio"
   - Funziona come Ambito

4. **Misura** (campo freesolo con autocomplete)

   - Placeholder: "Es: GV.RM-03"
   - Funziona come Ambito

5. **Requisito** (select da anagrafica, obbligatorio)
   - Campo con ricerca
   - Placeholder: "Cerca requisito..."
   - Quando l'Admin inizia a digitare, il sistema filtra i requisiti esistenti
   - L'Admin deve selezionarne uno dalla lista
   - In fondo alla lista c'è il pulsante "+ Crea Nuovo Requisito" per creare un requisito al volo

**Validazioni quando si salva la riga**:

- Almeno uno dei campi tra Ambito/Tematica/Categoria/Misura deve essere compilato
- Il campo Requisito è obbligatorio
- Se la riga è identica a una già esistente, il sistema mostra un warning "Riga duplicata, vuoi procedere comunque?"

**Pulsanti nel modal**:

- **Annulla**: Chiude il modal senza salvare
- **Salva Riga**: Valida e, se OK, aggiunge la riga alla tabella e chiude il modal

#### Creare un Requisito al Volo

Se l'Admin clicca "+ Crea Nuovo Requisito" mentre sta compilando una riga, il sistema apre un secondo modal (annidato) con il titolo "Crea Nuovo Requisito".

**Campi nel modal requisito**:

1. **Codice** (obbligatorio, univoco)

   - Es: "GV.RM-06"
   - Se il codice esiste già, mostra errore

2. **Nome** (obbligatorio, max 255 caratteri)

   - Es: "Gestione incidenti cybersecurity"

3. **Descrizione** (opzionale, area testo)

   - Max 2000 caratteri

4. **Livello Assessment** (radio button, obbligatorio)
   - Opzioni: Essenziale (E), Importante (I), Fuori ambito (F)
   - Default: Importante

**Quando l'Admin salva il requisito**:

- Il sistema lo salva nell'Anagrafica Requisiti Globali
- Chiude il modal "Crea Nuovo Requisito"
- Preseleziona automaticamente il requisito appena creato nel campo "Requisito" del modal "Aggiungi Riga"
- L'Admin può completare gli altri campi e salvare la riga

#### Visualizzare le Righe Aggiunte

Dopo aver aggiunto la prima riga, la tabella si popola e mostra:

- Numero progressivo riga
- Valori di Ambito, Tematica, Categoria, Misura
- Nome del Requisito (troncato se troppo lungo)
- Pulsanti per ogni riga: [Modifica] [Elimina] [↑] [↓]

**Funzioni sui pulsanti**:

- **Modifica**: Riapre il modal con i dati precompilati
- **Elimina**: Chiede conferma ("Sei sicuro?") e rimuove la riga
- **↑ ↓**: Sposta la riga su o giù per riordinare

Sotto la tabella viene mostrato il totale: "Totale righe: X"

#### Importare da CSV

Se l'Admin clicca "Importa da CSV", il sistema apre un dialog che spiega la struttura del file CSV richiesto:

- Colonne richieste (in ordine): Ambito, Tematica, Categoria, Misura, Codice Requisito
- C'è un pulsante "Scarica Template CSV" per scaricare un file esempio
- L'Admin può trascinare il suo file CSV o cliccare per selezionarlo
- Il sistema valida il file:
  - Se tutti i requisiti esistono nell'anagrafica globale: importa le righe con successo
  - Se mancano requisiti: mostra errore con lista requisiti mancanti e suggerisce di crearli prima

**Pulsanti in fondo alla pagina**:

- **← Indietro**: Torna alla SEZIONE 1 per modificare nome/descrizione
- **Salva Bozza**: Salva il framework in stato Bozza (anche senza righe o con righe incomplete) e reindirizza al Dettaglio Framework
- **Avanti →**: Valida che ci sia almeno 1 riga, e se OK passa alla FASE 3

---

### FASE 3: Associazione Scale Valutazione e Calcoli

**Cosa succede**: Dopo aver cliccato "Avanti" dalla FASE 2, la pagina si aggiorna mostrando la **SEZIONE 3: SCALE DI VALUTAZIONE E CALCOLI**.

In alto viene mostrato il recap delle sezioni precedenti:

- "✓ SEZIONE 1: INFORMAZIONI BASE (completata)"
- "✓ SEZIONE 2: STRUTTURA FRAMEWORK (71 righe aggiunte)"

La sezione 3 è divisa in due sottosezioni:

#### Sottosezione 3.1: SCALE DI VALUTAZIONE

**Testo esplicativo**: "Seleziona le scale che i Consulenti useranno per valutare i requisiti durante gli audit."

**Cosa vede l'Admin**: Una lista di checkbox con le scale pre-configurate disponibili:

**Scala: Grado Copertura NIS2 (0.0-1.0)**

- Descrizione breve: "6 livelli: Nullo, Insufficiente, Iniziale, Incompleto, Avanzato, Completo"
- Pulsante [Anteprima] per vedere i dettagli completi

**Scala: Grado Compliance NIS2 (0-3)**

- Descrizione breve: "4 livelli: Compliant, Parziale, Minimale, Assente"
- Pulsante [Anteprima]

**Scala: Probabilità Rischio (1-4)**

- Descrizione breve: "4 livelli: Bassa, Media, Alta, Molto alta"
- Pulsante [Anteprima]

**Scala: Danno (1-4)**

- Descrizione breve: "4 livelli: Lieve, Modesto, Grave, Gravissimo"
- Pulsante [Anteprima]

In fondo alla lista c'è il pulsante **"+ Crea Nuova Scala"** per creare scale custom.

**Quando l'Admin clicca su [Anteprima]**: Si apre un modal che mostra tutti i dettagli della scala:

- Nome scala
- Range (es: 0.0 - 1.0)
- Lista completa dei livelli con valore, label e descrizione
- Pulsante [Chiudi]

**Quando l'Admin clicca su "+ Crea Nuova Scala"**: Si apre un modal per creare una scala personalizzata con:

- Nome scala (obbligatorio)
- Descrizione (opzionale)
- Tipo valori: numerici interi o decimali
- Sezione per definire i livelli (minimo 2):
  - Per ogni livello: Valore, Label, Descrizione
  - Pulsante "+ Aggiungi Livello" per aggiungere altri livelli
  - Pulsante [Rimuovi] per ogni livello
- Pulsanti: [Annulla] [Salva Scala]

Quando la scala viene salvata, il sistema la salva nell'Anagrafica Scale Valutazione e la preseleziona automaticamente nella lista.

#### Sottosezione 3.2: CALCOLI AUTOMATICI (Opzionale)

**Testo esplicativo**: "Definisci calcoli automatici per aggregare i valori delle scale e generare indicatori."

**Cosa vede l'Admin**: Una lista di checkbox con i calcoli predefiniti disponibili:

**Calcolo: Indice Rischio**

- Formula: Probabilità × Danno
- Range: 1-16
- Richiede: Scale "Probabilità Rischio" + "Danno"
- Pulsante [Configura Soglie]
- Se le scale richieste non sono selezionate, mostra warning: "⚠️ Seleziona prima le scale 'Probabilità Rischio' e 'Danno' per abilitare questo calcolo"

**Calcolo: % Conformità**

- Formula: (Requisiti conformi / Totali) × 100
- Range: 0-100%
- Richiede: Scala "Grado Compliance"
- Pulsante [Configura Soglie]

**Calcolo: Media Copertura**

- Formula: AVG(Grado Copertura)
- Range: 0.0-1.0
- Richiede: Scala "Grado Copertura"
- Pulsante [Configura Soglie]

**Quando l'Admin clicca [Configura Soglie]**: Si apre un modal specifico per quel calcolo.

**Esempio: Configurazione Soglie Indice Rischio**

Il modal mostra:

- Titolo: "Configura Soglie: Indice Rischio"
- Formula: Probabilità × Danno
- Range valori: 1-16
- Testo esplicativo: "Definisci le soglie per classificare i risultati del calcolo in livelli di severità."

Sezione per definire le soglie:

- Per ogni livello di soglia:
  - Nome (es: "Basso", "Medio", "Alto", "Grave")
  - Range (Da X A Y)
  - Colore (dropdown: Verde, Giallo, Arancione, Rosso, Blu, Grigio)
  - Pulsante [Rimuovi]
- Pulsante "+ Aggiungi Livello"

**Validazione in tempo reale**:

- Il sistema controlla che i range non si sovrappongano
- Il sistema segnala se ci sono "buchi" nei range: "⚠️ Valori non coperti: 7, 10, 11"
- Il sistema segnala sovrapposizioni: "❌ Range 4-6 si sovrappone con 5-8"

Pulsanti: [Annulla] [Salva Soglie]

Quando le soglie vengono salvate, il calcolo viene marcato con badge "✓ Configurato".

**Come funziona nei report**:
Quando durante l'audit il Consulente valuta un requisito con Probabilità=3 e Danno=4, il sistema:

1. Calcola automaticamente: Indice Rischio = 3 × 4 = 12
2. Classifica secondo le soglie: 12 cade nel range "Grave" (12-16)
3. Nel report mostra: "Indice rischio: 12 - Grave" con sfondo rosso

**Validazioni per procedere alla fase successiva**:

- Almeno 1 scala deve essere selezionata (altrimenti errore: "Seleziona almeno una scala di valutazione")
- I calcoli sono opzionali, ma se selezionati devono avere le scale richieste già selezionate

**Pulsanti in fondo alla pagina**:

- **← Indietro**: Torna alla SEZIONE 2 (Struttura Framework)
- **Salva Bozza**: Salva il framework in stato Bozza e reindirizza al Dettaglio Framework
- **Avanti → Review**: Valida e passa alla FASE 4 (Review finale)

---

### FASE 4: Review Finale e Salvataggio

**Cosa succede**: Dopo aver cliccato "Avanti → Review", la pagina mostra un riepilogo completo di tutto quello che l'Admin ha configurato.

**Cosa vede l'Admin**:

Il breadcrumb diventa: "Framework > Nuovo > Review"

Viene mostrata una sezione "RIEPILOGO FRAMEWORK" con:

**Informazioni Base**:

- Nome: Framework Nazionale Cybersecurity 2025
- Descrizione: (il testo completo)
- Pulsante [Modifica] per tornare alla SEZIONE 1

**Struttura**:

- Totale righe: 71
- Ambiti univoci: 16 (a-p)
- Requisiti univoci: 145
- Pulsante [Modifica] per tornare alla SEZIONE 2

**Scale di Valutazione**:

- Lista delle scale selezionate (es: Grado Copertura NIS2, Grado Compliance NIS2, Probabilità Rischio, Danno)
- Pulsante [Modifica] per tornare alla SEZIONE 3

**Calcoli Automatici** (se configurati):

- Per ogni calcolo attivo mostra:
  - Nome e formula
  - Lista soglie con range e colore
- Pulsante [Modifica] per tornare alla SEZIONE 3

In fondo:

- "Stato: Bozza"
- Nota: "Potrai pubblicarlo dopo il salvataggio"

**Pulsanti finali**:

- **← Indietro**: Torna alla SEZIONE 3
- **Salva come Bozza**: Salva e vai al Dettaglio Framework
- **Salva e Pubblica**: Salva e pubblica immediatamente

#### Salvare come Bozza

Se l'Admin clicca "Salva come Bozza":

1. Sistema salva il framework con stato "Bozza"
2. Mostra notifica verde: "Framework salvato come Bozza"
3. Reindirizza alla pagina Dettaglio Framework

#### Salvare e Pubblicare

Se l'Admin clicca "Salva e Pubblica":

1. Sistema mostra un dialog di conferma che spiega:

   - "Stai per pubblicare il framework: [nome]"
   - "Una volta pubblicato:"
   - "• Il framework sarà visibile ai Consulenti"
   - "• I Consulenti potranno clonarlo in Template"
   - "• NON potrai più modificarlo"
   - "• Per modifiche dovrai creare una nuova versione (clone)"
   - "Sei sicuro di voler procedere?"
   - Pulsanti: [Annulla] [Conferma Pubblica]

2. Se l'Admin conferma:
   - Sistema salva il framework con stato "Pubblicato"
   - Registra timestamp di pubblicazione
   - Mostra notifica verde: "Framework pubblicato con successo"
   - Reindirizza alla pagina Dettaglio Framework

---

### FASE 5: Dopo il Salvataggio - Pagina Dettaglio Framework

Sia che l'Admin abbia salvato come Bozza o pubblicato direttamente, viene portato alla pagina **Dettaglio Framework**.

**Cosa vede l'Admin**:

In alto:

- Titolo: "FRAMEWORK: Framework Nazionale Cybersecurity 2025"
- Breadcrumb: "Framework > Dettaglio"
- Badge colorato con lo stato: [BOZZA] in blu oppure [PUBBLICATO] in verde

Pulsanti azione (variano in base allo stato):

- Se Bozza: [Modifica] [Pubblica] [Clona] [Elimina]
- Se Pubblicato: [Clona] [Archivia] (Modifica è disabilitato)
- Se Archiviato: [Clona] [Elimina] (se non usato in nessun Template)

**Sezione: INFORMAZIONI BASE**

- Nome framework
- Descrizione
- Stato
- Creato il: data/ora
- Creato da: nome Admin

**Sezione: STRUTTURA FRAMEWORK**

Mostra una **vista ad albero gerarchico** espandibile/collassabile:

- Livello 1: ▼ a) Gestione del rischio (15 requisiti)

  - Livello 2: ▼ Monitoraggio cyber security
    - Livello 3: ▼ GV.RM - Gestione del Rischio
      - Livello 4: ▼ GV.RM-03
        - Requisito: • Inventario asset aggiornato
      - Livello 4: ▼ GV.RM-04
        - Requisito: • Piano gestione rischi documentato

- Livello 1: ▼ b) Ruoli e responsabilità (8 requisiti)
  - ...

Pulsanti: [Espandi Tutto] [Comprimi Tutto]

**Sezione: SCALE DI VALUTAZIONE ASSOCIATE**

Lista delle scale con:

- Nome scala
- Pulsante [Anteprima] per vedere i dettagli

**Sezione: CALCOLI AUTOMATICI**

Per ogni calcolo configurato mostra:

- Nome e formula
- Range valori
- Soglie configurate con nome, range e indicatore colore

---

## ✏️ MODIFICA FRAMEWORK (Solo se Bozza)

**Scenario**: L'Admin è nella pagina Dettaglio di un Framework in stato Bozza e vuole modificarlo.

**Azione**: L'Admin clicca sul pulsante **"Modifica"**.

**Cosa succede**: Il sistema riapre la stessa pagina di creazione framework, ma in modalità "Edit". Tutti i campi sono precompilati con i dati esistenti. L'Admin può:

- Modificare nome e descrizione
- Aggiungere, modificare, eliminare righe della struttura
- Riordinare le righe
- Aggiungere o rimuovere scale
- Aggiungere, rimuovere o riconfigurare calcoli

**Validazioni**:

- Non può eliminare tutte le righe (minimo 1 richiesta)
- Non può deselezionare tutte le scale (minimo 1 richiesta)
- Se rimuove una scala usata da un calcolo, il sistema mostra warning: "Rimuovendo questa scala, il calcolo 'Indice Rischio' verrà disabilitato"

**Salvataggio**: Quando l'Admin clicca "Salva", il sistema aggiorna il framework mantenendo lo stesso ID, mostra notifica "Framework aggiornato con successo" e reindirizza al Dettaglio Framework.

**Note importanti**:

- Il pulsante "Modifica" è disabilitato se il framework è Pubblicato o Archiviato
- Se un framework è Pubblicato e l'Admin vuole modificarlo, deve prima clonarlo

---

## 🗑️ ELIMINAZIONE FRAMEWORK

**Scenario**: L'Admin vuole eliminare un Framework.

**Azione**: L'Admin clicca sul pulsante **"Elimina"** (disponibile nella lista framework o nel dettaglio).

**Cosa succede**: Il sistema esegue delle validazioni prima di permettere l'eliminazione.

### Validazione 1: Stato Framework

**Framework in Bozza**: Può sempre essere eliminato liberamente (non è in uso).

**Framework Pubblicato**: Non può MAI essere eliminato. Il sistema mostra un dialog di errore: "Il framework non può essere eliminato perché è in stato Pubblicato. I framework pubblicati non possono essere eliminati per garantire l'integrità dei Template e Audit che li utilizzano. Se vuoi rimuoverlo dalla vista dei Consulenti, usa il pulsante 'Archivia'."

**Framework Archiviato**: Può essere eliminato solo se non è usato in nessun Template esistente.

### Validazione 2: Utilizzo in Template

Il sistema controlla quanti Template utilizzano questo framework. Se il conteggio è maggiore di zero, l'eliminazione non è permessa.

**Caso 1: Framework Eliminabile (Bozza, non usato)**

Il sistema mostra un dialog di conferma: "Stai per eliminare il framework: [nome]. Stato: Bozza. Creato il: [data]. ⚠️ Questa azione è IRREVERSIBILE. Sei sicuro di voler procedere?"

Pulsanti: [Annulla] [Elimina]

Se l'Admin conferma, il sistema esegue un soft delete, mostra notifica "Framework eliminato con successo" e reindirizza alla lista Framework.

**Caso 2: Framework NON Eliminabile (Archiviato ma usato in Template)**

Il sistema mostra un dialog di errore: "Il framework non può essere eliminato perché è usato in 5 Template esistenti: [lista template]. Per eliminarlo, devi prima eliminare tutti i Template che lo utilizzano."

Pulsanti: [OK] [Vedi Template]

Se l'Admin clicca "Vedi Template", viene reindirizzato alla lista Template con filtro automatico sul framework.

---

## 📋 VISUALIZZAZIONE LISTA FRAMEWORK (Admin)

**Scenario**: L'Admin clicca sulla voce menu "Framework" nella sidebar.

**Cosa vede l'Admin**:

In alto:

- Titolo: "FRAMEWORK"
- Breadcrumb: "Framework"
- Pulsante arancione: **"+ Nuovo Framework"**

**Sezione Filtri e Ricerca**:

Campo di ricerca full-text:

- Placeholder: "Cerca framework..."
- Cerca in: Nome framework, Descrizione, Nome requisiti
- Risultati filtrati in tempo reale (dopo 300ms dalla fine della digitazione)

Filtro per Stato:

- Dropdown con opzioni: Tutti / Bozza / Pubblicato / Archiviato
- Chips cliccabili per selezione rapida

Filtro per Autore:

- Dropdown con lista degli Admin
- Mostra chi ha creato quale framework

Pulsante [Pulisci Filtri] per reset

**Sezione Risultati**:

Intestazione: "FRAMEWORK (23 risultati)"

Ogni framework viene mostrato come una card con:

**Badge stato** (colorato):

- [BOZZA] in blu
- [PUBBLICATO] in verde
- [ARCHIVIATO] in grigio

**Informazioni principali**:

- Nome framework (grande, in grassetto)
- "Creato il [data] da [nome admin]"
- Statistiche: "71 righe • 145 requisiti • 4 scale"
- Se usato: "Usato in: 12 Template"

**Pulsanti azione** (variano per stato):

Framework Bozza:

- [Visualizza] [Modifica] [Pubblica] [Elimina]

Framework Pubblicato:

- [Visualizza] [Clona] [Archivia]

Framework Archiviato:

- [Visualizza] [Clona] [Elimina] (se non usato)

In fondo: Pulsante [Carica Altri...] per paginazione infinita (carica 20 risultati alla volta)

**Ordinamento**:

- Default: Data creazione discendente (più recenti prima)
- Altre opzioni: Nome A-Z, Nome Z-A, Data creazione ascendente

---

## 📦 GESTIONE REQUISITI GLOBALI - Pagina Dedicata

L'Admin può accedere alla pagina **"Requisiti"** dal menu principale per gestire l'anagrafica centrale.

**Cosa vede l'Admin**:

In alto:

- Titolo: "REQUISITI GLOBALI"
- Breadcrumb: "Requisiti"
- Pulsante: **"+ Nuovo Requisito"**

**Sezione Filtri e Ricerca**:

- Campo ricerca full-text su Codice, Nome, Descrizione
- Filtro per Tag (dropdown multi-selezione)
- Pulsante [Pulisci Filtri]

**Sezione Risultati**:

Ogni requisito viene mostrato come una card con:

- Codice e Nome (es: "GV.RM-03: Inventario asset aggiornato")
- Descrizione troncata
- Tag come chips colorate
- "Usato in: 3 Framework"
- Pulsanti: [Visualizza] [Modifica] [Elimina]

**Quando l'Admin clicca "+ Nuovo Requisito"**: Si apre un modal identico a quello della creazione al volo, con i campi:

- Codice (obbligatorio, univoco)
- Nome (obbligatorio)
- Descrizione (opzionale)
- Livello Assessment (E/I/F)
- Tag (opzionali, per facilitare ricerca)

**Quando l'Admin clicca [Modifica]**: Il requisito può essere modificato solo se non è usato in nessun Framework Pubblicato. Se è usato, il sistema mostra un dialog di avviso: "Il requisito è usato in [N] Framework. Le modifiche impatteranno i framework in Bozza che lo utilizzano."

**Quando l'Admin clicca [Elimina]**: Il sistema controlla se il requisito è usato in qualche framework. Se sì, mostra errore: "Il requisito non può essere eliminato perché è usato in [lista framework]. Per eliminarlo, rimuovilo prima da tutti i Framework che lo utilizzano."

---

## 🎯 Come si Collegano le Parti

Per aiutare a capire meglio come tutti questi pezzi si incastrano tra loro, ecco una spiegazione discorsiva delle relazioni:

### Framework e Requisiti

Un Framework è come un contenitore che raggruppa molti Requisiti. Però i Requisiti non appartengono a un singolo Framework: sono condivisi e riutilizzabili. Immagina una biblioteca di libri (Requisiti) che possono essere usati in diverse collezioni tematiche (Framework).

Quando l'Admin crea una riga nel Framework, non sta creando un nuovo requisito da zero: sta scegliendo un requisito esistente dalla biblioteca globale e lo sta associando a quella posizione gerarchica specifica (Ambito → Tematica → Categoria → Misura).

### Framework e Scale

Un Framework può usare più Scale di valutazione contemporaneamente. È come dire: "Per questo framework, i Consulenti useranno questi strumenti di misura specifici". Ogni scala è uno strumento diverso per misurare aspetti diversi (copertura, conformità, rischio, ecc.).

### Scale e Calcoli

I Calcoli Automatici usano i valori delle Scale come input. Ad esempio, il calcolo "Indice Rischio" prende il valore della scala "Probabilità Rischio" e lo moltiplica per il valore della scala "Danno". Per questo motivo, un calcolo può essere attivato solo se le scale che usa sono state selezionate nel framework.

### Framework e Template Audit

Quando un Consulente vuole fare un audit per un cliente, non parte da zero: sceglie un Framework Pubblicato e lo clona per creare un Template Audit personalizzato. Il Template è una copia del Framework che il Consulente può adattare alle esigenze specifiche del cliente (ad esempio, può escludere alcuni requisiti non applicabili).

### Stati e Ciclo di Vita

Il ciclo di vita tipico di un framework è:

1. L'Admin crea il framework (stato Bozza)
2. Lo compila e lo salva (rimane Bozza)
3. Quando è pronto, lo pubblica (diventa Pubblicato)
4. I Consulenti lo vedono e lo usano per creare Template
5. Se serve aggiornarlo, l'Admin lo clona (crea una Bozza v2)
6. La v2 viene modificata e pubblicata
7. Il framework originale può essere archiviato (diventa Archiviato)

---

## 📝 Indice User Stories (Da Implementare)

Le user stories dettagliate verranno create in documenti separati. Qui l'elenco completo:

### Gestione Framework Base

- US-FW-001: Visualizzare lista Framework (Admin)
- US-FW-002: Creare nuovo Framework (Admin)
- US-FW-003: Visualizzare dettaglio Framework (Admin)
- US-FW-004: Modificare Framework in Bozza (Admin)
- US-FW-005: Pubblicare Framework (Admin)
- US-FW-006: Archiviare Framework (Admin)
- US-FW-007: Clonare Framework per nuova versione (Admin)
- US-FW-008: Eliminare Framework (Admin)

### Gestione Requisiti Globali

- US-FW-009: Visualizzare Anagrafica Requisiti Globali (Admin)
- US-FW-010: Creare Requisito Globale (Admin)
- US-FW-011: Modificare Requisito Globale (Admin)
- US-FW-012: Eliminare Requisito Globale (Admin)

### Gestione Scale Valutazione

- US-FW-013: Visualizzare Scale Valutazione (Admin)
- US-FW-014: Creare Scala Valutazione Custom (Admin)
- US-FW-015: Modificare Scala Valutazione (Admin)
- US-FW-016: Eliminare Scala Valutazione (Admin)

### Ricerca e Filtri

- US-FW-017: Ricercare e Filtrare Framework (Admin)
- US-FW-018: Ricercare e Filtrare Requisiti Globali (Admin)

### Visualizzazione per Consulenti

- US-FW-019: Visualizzare Framework Pubblicati (Consulente)

---

## ✅ Riepilogo Modifiche Versione 2.0

**Modifiche strutturali**:

- Rimosso il livello "Nome" dalla gerarchia (ora: Ambito → Tematica → Categoria → Misura → Requisito)
- Aggiunto campo "Livello Assessment" (E/I/F) sui requisiti, specificato come informativo
- Aggiunto campo "Situazione Riscontrata" compilato durante l'audit
- Chiarita la separazione tra valutazioni CODICI (Grado Copertura su Categoria/Misura) e REQUISITI (Grado Compliance)
- Spiegato il perché della doppia valutazione

**Modifiche stilistiche**:

- Eliminato completamente tutte le grafiche ASCII
- Trasformato tutto in stile discorsivo e narrativo
- Focus su "cosa vede l'Admin" invece di strutture tecniche
- Rimossi tecnicismi da developer
- Aggiunte spiegazioni esplicite di come le parti si collegano

---

**Documento redatto il**: 10 Dicembre 2025
**Autore**: AI Assistant + Pier Luigi (Product Owner)
**Versione**: 2.0 (Aggiornato con feedback cliente)
