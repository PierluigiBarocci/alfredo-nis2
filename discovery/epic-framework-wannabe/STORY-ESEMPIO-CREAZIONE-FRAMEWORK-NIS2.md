# 📖 Storia: Alfredo Crea il Framework NIS2

**Documento**: Esempio Narrativo Completo
**Data**: 10 Dicembre 2025
**Versione**: 2.0
**Scopo**: Validare il flusso di creazione Framework attraverso un caso d'uso reale

---

## 🎭 I Protagonisti

- **Alfredo**: Admin di Piattaforma presso NetcoADV
- **Laura Bianchi**: Consulente Senior
- **Azienda Cliente**: "TechCorp S.p.A." (settore manifatturiero)

---

## 📅 Giorno 1: Alfredo Riceve l'Incarico

È lunedì mattina, 10 dicembre 2025. Alfredo, Admin di piattaforma presso NetcoADV, riceve una email dal CEO:

> "Ciao Alfredo,
>
> Abbiamo appena firmato un contratto con 5 nuove aziende che devono conformarsi alla Direttiva NIS2. Ho bisogno che tu carichi il framework NIS2 in piattaforma entro questa settimana, così i nostri consulenti possono iniziare gli audit.
>
> Ti allego il documento ufficiale della Direttiva UE 2022/2555 e il nostro template Excel con la struttura che abbiamo usato finora in Access.
>
> Grazie!"

Alfredo apre l'Excel allegato e vede **71 righe** con questa struttura:

**Colonne**: Ambito | Tematica | Categoria | Misura | Codice Requisito

**Esempio righe**:

- a) Gestione del rischio | Monitoraggio cyber security | GV.RM | GV.RM-03 | Inventario asset aggiornato
- a) Gestione del rischio | Monitoraggio cyber security | GV.RM | GV.RM-04 | Piano gestione rischi documentato

Alfredo pensa: "Perfetto, con la nuova piattaforma posso digitalizzare tutto questo e renderlo riutilizzabile per tutti i consulenti!"

---

## 🚀 Giorno 1 - Ore 10:00: Alfredo Inizia la Creazione

### Passo 1: Login e Navigazione

Alfredo apre il browser e va su `https://piattaforma.netcoadv.it`

1. Inserisce le sue credenziali:
   - Email: alfredo@netcoadv.it
   - Password: (password nascosta)
2. Clicca su "Accedi"
3. Il sistema lo riconosce come Admin di Piattaforma e mostra la dashboard

Nella sidebar sinistra, Alfredo vede diverse voci di menu:

- Aziende Consulenza
- Aziende Clienti
- **Framework** (clicca qui)
- Template Audit
- Audit
- Report

---

### Passo 2: Visualizzazione Lista Framework

Il sistema apre la pagina "Framework".

Alfredo vede:

- Un pulsante arancione "+ Nuovo Framework" in alto a destra
- Una lista con 2 framework esistenti:
  - Badge verde [PUBBLICATO] ISO 27001:2013 (creato 3 mesi fa da un altro admin)
  - Badge blu [BOZZA] GDPR Assessment (creato ieri da Alfredo, ancora incompleto)

Alfredo pensa: "Ok, devo crearne uno nuovo per NIS2"

---

### Passo 3: Avvio Creazione Framework

Alfredo clicca su "+ Nuovo Framework"

Il sistema apre una nuova pagina con titolo "Crea Nuovo Framework". In alto c'è il breadcrumb: Framework > Nuovo

Viene mostrata la **SEZIONE 1: INFORMAZIONI BASE** con due campi:

**Campo Nome Framework** (obbligatorio):

- Placeholder: "Es: Framework Nazionale Cybersecurity 2025"
- Alfredo compila: Framework NIS2 - Direttiva UE 2022/2555

**Campo Descrizione** (opzionale, area testo multiriga):

- Placeholder: "Descrivi lo scopo e l'ambito di applicazione del framework"
- Alfredo compila: Framework per la valutazione della conformità alla Direttiva NIS2 (Network and Information Security 2). Applicabile a soggetti essenziali e importanti nei settori energia, trasporti, bancario, sanitario, infrastrutture digitali e manifatturiero.

In fondo ci sono due pulsanti: [Annulla] e [Avanti →]

Alfredo clicca su "Avanti →"

---

### Passo 4: Costruzione Struttura Framework

Il sistema mostra la **SEZIONE 2: STRUTTURA FRAMEWORK**

In alto viene mostrato il recap:

- Segno di spunta verde "SEZIONE 1: INFORMAZIONI BASE (completata)"
- "Nome: Framework NIS2 - Direttiva UE 2022/2555"
- Pulsante [Modifica] per tornare indietro

Alfredo vede:

- Un testo esplicativo: "Aggiungi le righe del framework compilando la tabella qui sotto. Ogni riga rappresenta un requisito valutabile durante l'audit."
- Due pulsanti: "+ Aggiungi Riga" e "Importa da CSV"
- Una tabella vuota con intestazioni: # | Ambito | Tematica | Categoria | Misura | Requisito
- Un messaggio: "Clicca '+ Aggiungi Riga' per iniziare"

Alfredo pensa: "Ho 71 righe da inserire... vediamo se posso importare l'Excel!"

---

#### Tentativo 1: Import CSV

Alfredo clicca "Importa da CSV"

Il sistema apre un dialog che mostra:

- Titolo: "IMPORTA STRUTTURA DA CSV"
- Testo: "Carica un file CSV con questa struttura:"
- Lista colonne richieste (in ordine):
  1. Ambito
  2. Tematica
  3. Categoria
  4. Misura
  5. Codice Requisito
- Pulsante "Scarica Template CSV"
- Area per trascinare il file o cliccare per sfogliare
- Pulsanti: [Annulla] [Importa]

Alfredo:

1. Clicca "Scarica Template CSV" e scarica il file template_framework.csv
2. Apre il suo Excel con le 71 righe
3. Copia i dati nel template CSV (rimuovendo eventuali colonne non necessarie)
4. Salva come nis2_struttura.csv
5. Trascina il file nell'area del dialog
6. Clicca "Importa"

Il sistema elabora il file...

**Errore!** Il sistema mostra un dialog:

- Titolo: "ERRORE IMPORTAZIONE"
- Messaggio: "Trovati 15 requisiti non presenti nell'anagrafica globale:"
- Lista: GV.RM-03 (riga 1), GV.RM-04 (riga 2), GV.RM-05 (riga 3), ... (altri 12)
- Spiegazione: "Devi prima creare questi requisiti nell'anagrafica globale, oppure aggiungere le righe manualmente."
- Pulsanti: [OK] [Vai ad Anagrafica]

Alfredo pensa: "Ah giusto, devo prima creare i requisiti! Vediamo se posso farlo al volo..."

---

#### Tentativo 2: Aggiunta Manuale Prima Riga

Alfredo clicca "OK" e poi clicca "+ Aggiungi Riga"

Il sistema apre un modal (popup) con titolo "Aggiungi Riga Framework" e un testo esplicativo: "Compila i 5 livelli gerarchici. I campi sono opzionali tranne Requisito."

Il modal mostra 5 campi:

1. **Campo Ambito** (autocomplete freesolo)

   - Placeholder: "Es: a) Gestione del rischio"
   - Suggerimenti: (nessuno, è il primo framework)

2. **Campo Tematica** (autocomplete freesolo)

   - Placeholder: "Es: Monitoraggio cyber security"
   - Suggerimenti: (nessuno)

3. **Campo Categoria** (autocomplete freesolo)

   - Placeholder: "Es: GV.RM - Gestione del Rischio"
   - Suggerimenti: (nessuno)

4. **Campo Misura** (autocomplete freesolo)

   - Placeholder: "Es: GV.RM-03"
   - Suggerimenti: (nessuno)

5. **Campo Requisito** (select da anagrafica, obbligatorio)
   - Placeholder: "Cerca requisito..."
   - Campo con ricerca
   - Messaggio: "Nessun requisito trovato. Crea il primo requisito."
   - Pulsante "+ Crea Nuovo Requisito"

In fondo: [Annulla] [Salva Riga]

Alfredo compila la prima riga guardando l'Excel:

**Ambito**: Digita `a) Gestione del rischio` e preme Invio

**Tematica**: Digita `Monitoraggio cyber security` e preme Invio

**Categoria**: Digita `GV.RM - Gestione del Rischio` e preme Invio

**Misura**: Digita `GV.RM-03` e preme Invio

**Requisito**: Clicca sul campo e vede che il dropdown è vuoto. Clicca sul pulsante "+ Crea Nuovo Requisito"

---

#### Creazione Requisito al Volo

Il sistema apre un secondo modal (annidato) con titolo "Crea Nuovo Requisito"

Il modal mostra 4 campi:

1. **Codice** (obbligatorio, univoco)

   - Placeholder: "Univoco, es: GV.RM-03"
   - Alfredo digita: GV.RM-03

2. **Nome** (obbligatorio)

   - Placeholder: "Es: Inventario asset informatici"
   - Alfredo digita: Inventario asset informatici aggiornato

3. **Descrizione** (opzionale, area testo)

   - Alfredo digita: L'organizzazione deve mantenere un inventario completo e aggiornato di tutti gli asset informatici (hardware, software, dati) con classificazione per criticità e responsabile.

4. **Livello Assessment** (radio button)
   - Opzioni: Essenziale (E), Importante (I), Fuori ambito (F)
   - Alfredo seleziona: Importante (I)

In fondo: [Annulla] [Salva Requisito]

Alfredo clicca "Salva Requisito"

Il sistema:

1. Salva il requisito nell'Anagrafica Requisiti Globali
2. Chiude il modal "Crea Nuovo Requisito"
3. Pre-seleziona automaticamente il requisito appena creato nel campo "Requisito" del modal "Aggiungi Riga"

Alfredo vede che il campo "Requisito" ora mostra: "GV.RM-03: Inventario asset informatici aggiornato"

Alfredo clicca "Salva Riga"

Il sistema chiude il modal e mostra la tabella con la prima riga aggiunta:

**Tabella Righe Framework**:

- Riga 1: a) Gestione rischio | Monitoraggio cyber security | GV.RM | GV.RM-03 | Inventario asset...
- Pulsanti per la riga: [Modifica] [Elimina] [↑] [↓]
- Sotto la tabella: "Totale righe: 1"

Alfredo pensa: "Ok, funziona! Ma ho ancora 70 righe da inserire... devo trovare un modo più veloce!"

---

### Passo 5: Alfredo Crea i Requisiti Mancanti in Batch

Alfredo decide di creare prima tutti i requisiti nell'anagrafica globale, poi importare il CSV.

1. Clicca sul logo NetcoADV (torna alla home)
2. Nella sidebar clicca su "Requisiti" (nuova voce menu per l'anagrafica)
3. Il sistema apre la pagina "Requisiti Globali"

Alfredo vede:

- Titolo: "REQUISITI GLOBALI"
- Pulsante "+ Nuovo Requisito"
- Lista con 1 requisito già presente: "GV.RM-03: Inventario asset informatici aggiornato"

Alfredo passa i prossimi **20 minuti** a creare i requisiti uno per uno cliccando "+ Nuovo Requisito" e compilando il form per ognuno:

- GV.RM-04: Piano gestione rischi documentato
- GV.RM-05: Valutazione rischi supply chain
- GV.RR-01: Ruoli e responsabilità definiti
- ... (continua per tutti i 145 requisiti univoci)

Alle 10:45, Alfredo ha finito di creare tutti i requisiti necessari.

---

### Passo 6: Ritorno alla Creazione Framework e Import CSV

Alfredo:

1. Clicca su "Framework" nella sidebar
2. Vede che il framework "Framework NIS2 - Direttiva UE 2022/2555" è presente nella lista con badge blu [BOZZA]
3. Nota sotto il nome: "Ultima modifica: 10/12/2025 10:30" (il sistema ha fatto auto-save)
4. Clicca su [Modifica]

Il sistema riapre la pagina di creazione, già alla SEZIONE 2 con la riga 1 già presente nella tabella.

Alfredo clicca "Importa da CSV" e ricarica il file nis2_struttura.csv

Questa volta il sistema elabora con successo!

Il sistema mostra un dialog di conferma:

- Titolo: "IMPORTAZIONE COMPLETATA"
- Messaggio con checkmark verdi:
  - 71 righe importate con successo
  - 145 requisiti univoci associati
  - 16 ambiti univoci rilevati
- Pulsante: [OK]

Alfredo clicca "OK"

La tabella ora mostra tutte le 71 righe! Alfredo scorre per verificare:

- Riga 1: a) Gestione rischio | Monitoraggio cyber... | GV.RM | GV.RM-03 | Inventario...
- Riga 2: a) Gestione rischio | Monitoraggio cyber... | GV.RM | GV.RM-04 | Piano...
- ...
- Riga 71: p) Gestione crisi | Incident response | GV.IR | GV.IR-05 | Piano...

Sotto la tabella: "Totale righe: 71 | Ambiti univoci: 16 (a-p) | Requisiti univoci: 145"

Sono presenti anche i pulsanti: [Espandi Tutto] [Comprimi Tutto] per vedere la vista ad albero

Alfredo pensa: "Perfetto! Ora passo alle scale di valutazione"

In fondo alla pagina clicca "Avanti →"

---

### Passo 7: Associazione Scale di Valutazione

Il sistema mostra la **SEZIONE 3: SCALE DI VALUTAZIONE E CALCOLI**

In alto viene mostrato il recap:

- Segno di spunta verde "SEZIONE 1: INFORMAZIONI BASE (completata)"
- Segno di spunta verde "SEZIONE 2: STRUTTURA FRAMEWORK (71 righe aggiunte)"

La sezione 3 è divisa in due sottosezioni.

#### Sottosezione 3.1: SCALE DI VALUTAZIONE

Testo esplicativo: "Seleziona le scale che i Consulenti useranno per valutare i requisiti durante gli audit."

Alfredo vede una lista di checkbox con le scale pre-configurate:

**Scala 1**: Grado Copertura NIS2 (0.0-1.0)

- Descrizione breve: "6 livelli: Nullo, Insufficiente, Iniziale, Incompleto, Avanzato, Completo"
- Pulsante [Anteprima]

**Scala 2**: Grado Compliance NIS2 (0-3)

- Descrizione breve: "4 livelli: Compliant, Parziale, Minimale, Assente"
- Pulsante [Anteprima]

**Scala 3**: Probabilità Rischio (1-4)

- Descrizione breve: "4 livelli: Bassa, Media, Alta, Molto alta"
- Pulsante [Anteprima]

**Scala 4**: Danno (1-4)

- Descrizione breve: "4 livelli: Lieve, Modesto, Grave, Gravissimo"
- Pulsante [Anteprima]

**Scala 5**: ISO 27001 Maturità (1-5)

- Descrizione breve: "5 livelli: Non implementato, Pianificato, Parziale, Implementato, Ottimizzato"
- Pulsante [Anteprima]

In fondo: Pulsante "+ Crea Nuova Scala"

Alfredo pensa: "Per NIS2 usiamo le prime 4 scale"

Alfredo seleziona (spunta le checkbox):

- Grado Copertura NIS2 (0.0-1.0)
- Grado Compliance NIS2 (0-3)
- Probabilità Rischio (1-4)
- Danno (1-4)

Alfredo clicca [Anteprima] sulla scala "Grado Copertura NIS2" per verificare.

Il sistema apre un modal che mostra:

- Titolo: "ANTEPRIMA SCALA: Grado Copertura NIS2"
- Range: 0.0 - 1.0
- Lista livelli:
  - 0,0 - Nullo: Il controllo non è implementato in alcuna sua parte
  - 0,2 - Insufficiente: Implementazione iniziale di alcuni aspetti fondamentali
  - 0,4 - Iniziale: Il controllo risulta parzialmente implementato
  - 0,6 - Incompleto: Implementazione significativa ma incompleta
  - 0,8 - Avanzato: Controllo ampiamente implementato con lacune minori
  - 1,0 - Completo: Controllo completamente implementato
- Pulsante: [Chiudi]

Alfredo pensa: "Perfetto, è quella giusta!" e clicca "Chiudi"

---

#### Sottosezione 3.2: CALCOLI AUTOMATICI (Opzionale)

Alfredo scorre in basso e vede la sottosezione "CALCOLI AUTOMATICI"

Testo esplicativo: "Definisci calcoli automatici per aggregare i valori delle scale e generare indicatori."

Alfredo vede una lista di checkbox con i calcoli predefiniti:

**Calcolo 1**: Indice Rischio

- Formula: Probabilità × Danno
- Range: 1-16
- Richiede: Scale "Probabilità Rischio" + "Danno"
- Pulsante [Configura Soglie]

**Calcolo 2**: % Conformità

- Formula: (Requisiti conformi / Totali) × 100
- Range: 0-100%
- Richiede: Scala "Grado Compliance"
- Pulsante [Configura Soglie]

**Calcolo 3**: Media Copertura

- Formula: AVG(Grado Copertura)
- Range: 0.0-1.0
- Richiede: Scala "Grado Copertura"
- Pulsante [Configura Soglie]

In fondo: Pulsante "+ Crea Calcolo Custom" (disabilitato, con nota "Post-MVP")

Alfredo pensa: "Ottimo! Proprio quello che ci serve per i report. Attiviamo Indice Rischio e % Conformità"

Alfredo seleziona:

- Indice Rischio (checkbox)
- % Conformità (checkbox)

---

### Passo 8: Configurazione Soglie Indice Rischio

Alfredo clicca [Configura Soglie] sul calcolo "Indice Rischio"

Il sistema apre un modal:

- Titolo: "CONFIGURA SOGLIE: Indice Rischio"
- Formula: Probabilità × Danno
- Range valori: 1-16
- Testo: "Definisci le soglie per classificare i risultati del calcolo in livelli di severità."

Alfredo vede una sezione "SOGLIE DI CLASSIFICAZIONE" con due livelli precompilati:

**Livello 1**:

- Nome: Basso
- Range: Da 1 A 3
- Colore: Verde (dropdown)
- Pulsante [Rimuovi]

**Livello 2**:

- Nome: Medio
- Range: Da 4 A 6
- Colore: Giallo (dropdown)
- Pulsante [Rimuovi]

In fondo: Pulsante "+ Aggiungi Livello"

Sotto la lista livelli, un warning: "Valori non coperti: 7-16"

Alfredo pensa: "Ci sono dei buchi. Aggiungo i livelli Alto e Grave..."

Alfredo clicca "+ Aggiungi Livello" due volte e compila:

**Livello 3**:

- Nome: Alto
- Range: Da 8 A 9
- Colore: Arancione

**Livello 4**:

- Nome: Grave
- Range: Da 12 A 16
- Colore: Rosso

Il warning ora dice: "Valori non coperti: 7, 10, 11"

Alfredo pensa: "Mmm, ci sono ancora dei buchi. Sistemiamo..."

Alfredo modifica:

- Livello 2: Range Da 4 A 7 (invece di 6)
- Livello 3: Range Da 8 A 11 (invece di 9)

Il warning scompare!

In fondo al modal: [Annulla] [Salva Soglie]

Alfredo clicca "Salva Soglie"

Il sistema chiude il modal e mostra accanto al calcolo "Indice Rischio" un badge verde con checkmark: "Configurato"

Riepilogo visibile:

- Indice Rischio (Configurato)
  - Basso (1-3): Verde
  - Medio (4-7): Giallo
  - Alto (8-11): Arancione
  - Grave (12-16): Rosso

---

### Passo 9: Configurazione Soglie % Conformità

Alfredo clicca [Configura Soglie] sul calcolo "% Conformità"

Il sistema apre un modal simile. Alfredo configura:

**Livello 1**:

- Nome: Non Conforme
- Range: Da 0 A 59
- Colore: Rosso

**Livello 2**:

- Nome: Parzialmente Conforme
- Range: Da 60 A 79
- Colore: Giallo

**Livello 3**:

- Nome: Conforme
- Range: Da 80 A 100
- Colore: Verde

Nessun warning (tutti i valori 0-100 sono coperti)

Alfredo clicca "Salva Soglie"

Il calcolo "% Conformità" ora mostra il badge "Configurato"

In fondo alla pagina: [← Indietro] [Salva Bozza] [Avanti → Review]

Alfredo clicca "Avanti → Review"

---

### Passo 10: Review Finale

Il sistema mostra la pagina con breadcrumb: Framework > Nuovo > Review

Viene mostrata una sezione "RIEPILOGO FRAMEWORK" con tutto quello che Alfredo ha configurato:

**Informazioni Base**:

- Nome: Framework NIS2 - Direttiva UE 2022/2555
- Descrizione: (testo completo)
- Pulsante [Modifica] per tornare alla SEZIONE 1

**Struttura**:

- Totale righe: 71
- Ambiti univoci: 16 (a-p)
- Requisiti univoci: 145
- Pulsante [Modifica] per tornare alla SEZIONE 2

**Scale di Valutazione**:

- Grado Copertura NIS2 (0.0-1.0)
- Grado Compliance NIS2 (0-3)
- Probabilità Rischio (1-4)
- Danno (1-4)
- Pulsante [Modifica] per tornare alla SEZIONE 3

**Calcoli Automatici**:

- Indice Rischio (Probabilità × Danno)
  - Basso (1-3): Verde
  - Medio (4-7): Giallo
  - Alto (8-11): Arancione
  - Grave (12-16): Rosso
- % Conformità (Requisiti conformi / Totali)
  - Non Conforme (<60%): Rosso
  - Parziale (60-79%): Giallo
  - Conforme (≥80%): Verde
- Pulsante [Modifica] per tornare alla SEZIONE 3

In fondo:

- "Stato: Bozza"
- Nota: "Potrai pubblicarlo dopo il salvataggio"

Pulsanti finali: [← Indietro] [Salva come Bozza] [Salva e Pubblica]

Alfredo controlla tutto attentamente. Tutto sembra corretto!

Alfredo pensa: "Meglio salvare come Bozza per ora, così posso far verificare tutto al CEO prima di pubblicare"

Alfredo clicca "Salva come Bozza"

---

### Passo 11: Framework Salvato

Il sistema mostra una notifica verde in alto: "Framework salvato come Bozza"

Il sistema reindirizza alla pagina **Dettaglio Framework**:

In alto:

- Titolo: "FRAMEWORK: Framework NIS2 - Direttiva UE 2022/2555"
- Breadcrumb: Framework > Dettaglio
- Badge blu [BOZZA]
- Pulsanti disponibili: [Modifica] [Pubblica] [Clona] [Elimina]

**Sezione INFORMAZIONI BASE**:

- Nome: Framework NIS2 - Direttiva UE 2022/2555
- Descrizione: (testo completo)
- Stato: Bozza
- Creato il: 10/12/2025 11:15
- Creato da: Alfredo Rossi (Admin)

**Sezione STRUTTURA FRAMEWORK (71 righe)**:

Vista ad albero gerarchico (collassata di default):

- Freccia espandibile ▼ a) Gestione del rischio (15 requisiti)

  - ▼ Monitoraggio cyber security
    - ▼ GV.RM - Gestione del Rischio
      - ▼ GV.RM-03
        - Pallino • Requisito: Inventario asset aggiornato
      - ▼ GV.RM-04
        - Pallino • Requisito: Piano gestione rischi documentato

- Freccia espandibile ▼ b) Ruoli e responsabilità (8 requisiti)
  - ...

Pulsanti: [Espandi Tutto] [Comprimi Tutto]

**Sezione SCALE DI VALUTAZIONE ASSOCIATE**:

- Grado Copertura NIS2 (0.0-1.0) [Anteprima]
- Grado Compliance NIS2 (0-3) [Anteprima]
- Probabilità Rischio (1-4) [Anteprima]
- Danno (1-4) [Anteprima]

**Sezione CALCOLI AUTOMATICI**:

- Indice Rischio (Probabilità × Danno)
  - Range: 1-16
  - Soglie: Basso (1-3) Verde, Medio (4-7) Giallo, Alto (8-11) Arancione, Grave (12-16) Rosso
- % Conformità (Requisiti conformi / Totali)
  - Range: 0-100%
  - Soglie: Non Conforme (<60%) Rosso, Parziale (60-79%) Giallo, Conforme (≥80%) Verde

Alfredo è soddisfatto! Ore 11:15 - ha impiegato **1 ora e 15 minuti** per creare il framework completo.

---

## 📧 Giorno 1 - Ore 11:30: Alfredo Invia Email al CEO

Alfredo scrive:

> "Ciao,
>
> Ho caricato il Framework NIS2 in piattaforma. È in stato 'Bozza' per permetterti di verificarlo.
>
> Link: https://piattaforma.netcoadv.it/framework/nis2-2025
>
> Una volta approvato, lo pubblico e diventa disponibile per tutti i consulenti.
>
> Alfredo"

---

## 📅 Giorno 2 - Ore 9:00: CEO Approva e Alfredo Pubblica

Il CEO risponde:

> "Perfetto Alfredo! Ho verificato, tutto ok. Puoi pubblicare."

Alfredo:

1. Apre il Dettaglio Framework NIS2
2. Clicca su "Pubblica"

Il sistema mostra un dialog di conferma:

- Titolo: "CONFERMA PUBBLICAZIONE"
- Messaggio: "Stai per pubblicare il framework: Framework NIS2 - Direttiva UE 2022/2555"
- Elenco conseguenze con checkmark e X:
  - Checkmark "Il framework sarà visibile ai Consulenti"
  - Checkmark "I Consulenti potranno clonarlo in Template"
  - X "NON potrai più modificarlo"
  - X "Per modifiche dovrai creare una nuova versione tramite 'Clona'"
- Domanda: "Sei sicuro di voler procedere?"
- Pulsanti: [Annulla] [Conferma Pubblica]

Alfredo clicca "Conferma Pubblica"

Il sistema:

- Cambia stato da "Bozza" a "Pubblicato"
- Registra timestamp: 11/12/2025 09:05
- Disabilita pulsante "Modifica"
- Abilita pulsante "Clona per Modificare"
- Mostra notifica verde: "Framework pubblicato con successo"

Il badge cambia da [BOZZA] blu a [PUBBLICATO] verde.

Ora i pulsanti disponibili sono: [Clona] [Archivia] (Modifica è disabilitato e grigio)

---

## 👥 Giorno 2 - Ore 10:00: Laura (Consulente) Vede il Nuovo Framework

Laura Bianchi, Consulente Senior, si logga in piattaforma.

Nella sidebar clicca su "Template Audit" poi "+ Nuovo Template"

Il sistema mostra lo step 1: "Seleziona Framework Base"

Laura vede una lista di framework pubblicati:

- ISO 27001:2013
- **Framework NIS2 - Direttiva UE 2022/2555** (con badge verde [NUOVO!])
- GDPR Assessment

Laura seleziona "Framework NIS2" e clicca "Avanti"

Il sistema clona il framework in un nuovo Template Audit personalizzabile per il cliente "TechCorp S.p.A."

Laura pensa: "Perfetto! Ora posso personalizzare questo template per TechCorp e iniziare l'audit!"

---

## 📅 Giorno 30 - Alfredo Scopre un Errore

Un mese dopo, Laura chiama Alfredo:

> "Ciao Alfredo, ho notato che nel Framework NIS2 manca un requisito importante sulla gestione dei backup. Puoi aggiungerlo?"

Alfredo:

1. Apre il Dettaglio Framework NIS2
2. Vede che il pulsante "Modifica" è disabilitato (framework pubblicato)
3. Clicca su "Clona"

Il sistema mostra un dialog:

- Titolo: "CLONA FRAMEWORK"
- Messaggio: "Stai per creare una copia modificabile di: Framework NIS2 - Direttiva UE 2022/2555"
- Campo: "Nuovo Nome Framework:" con valore precompilato "Framework NIS2 - Direttiva UE 2022/2555 v2"
- Elenco con checkmark di cosa viene copiato:
  - "Tutta la struttura gerarchica (71 righe)"
  - "Tutti i requisiti associati (145)"
  - "Tutte le scale di valutazione (4)"
  - "Tutti i calcoli e soglie configurate"
- Nota: "La copia sarà in stato 'Bozza' e potrai modificarla liberamente."
- Pulsanti: [Annulla] [Conferma Clona]

Alfredo modifica il nome in: `Framework NIS2 - Direttiva UE 2022/2555 (Rev. Gennaio 2026)`

Alfredo clicca "Conferma Clona"

Il sistema:

- Crea nuovo framework con ID diverso
- Stato: "Bozza"
- Struttura identica all'originale
- Apre la pagina Modifica del clone

Notifica verde: "Framework clonato con successo. Ora puoi modificarlo."

Alfredo:

1. È già nella modalità Modifica, SEZIONE 2: Struttura
2. Clicca "+ Aggiungi Riga"
3. Aggiunge il requisito mancante sui backup
4. Clicca "Salva"
5. Va alla review finale e clicca "Salva e Pubblica"

Ora ci sono **2 versioni** del Framework NIS2 nella lista:

- **Framework NIS2 - Direttiva UE 2022/2555** [PUBBLICATO] - Usato in: 12 Template
- **Framework NIS2 - Direttiva UE 2022/2555 (Rev. Gennaio 2026)** [PUBBLICATO] - Usato in: 0 Template

I consulenti possono ora scegliere quale versione usare per i nuovi Template!

Alfredo può anche cliccare su "Archivia" sulla vecchia versione per nasconderla dalla vista dei consulenti (ma i Template esistenti continueranno a funzionare).

---

## 🎯 Fine della Storia

### Cosa Abbiamo Visto

1. Creazione Framework completo (71 righe, 145 requisiti, 4 scale, 2 calcoli)
2. Import CSV per velocizzare inserimento
3. Creazione Requisiti al volo durante compilazione
4. Configurazione Scale e Calcoli con soglie personalizzate
5. Salvataggio Bozza per review
6. Pubblicazione con conferma e immutabilità
7. Clonazione per creare nuove versioni
8. Utilizzo da parte Consulenti per creare Template Audit

### Tempo Totale Impiegato

- **Creazione Framework**: 1h 15min
- **Review CEO**: 5min
- **Pubblicazione**: 2min
- **Clonazione e modifica**: 10min

**Totale**: circa 1h 30min per digitalizzare un framework completo!

### Modifiche Versione 2.0

**Modifiche strutturali**:

- Rimosso il livello "Nome" dalla gerarchia (ora sono 5 livelli: Ambito, Tematica, Categoria, Misura, Requisito)
- Aggiornata la struttura CSV di import (5 colonne invece di 6)
- Aggiornati tutti i riferimenti ai campi del modal "Aggiungi Riga"

**Modifiche stilistiche**:

- Eliminato completamente tutte le grafiche ASCII
- Trasformato in stile narrativo puro
- Focus su "cosa vede Alfredo" e "cosa fa Alfredo"
- Descrizioni discorsive invece di rappresentazioni visive

---

**Fine del Documento**

**Documento redatto il**: 10 Dicembre 2025
**Autore**: AI Assistant + Pier Luigi (Product Owner)
**Versione**: 2.0 (Aggiornato con feedback cliente)
