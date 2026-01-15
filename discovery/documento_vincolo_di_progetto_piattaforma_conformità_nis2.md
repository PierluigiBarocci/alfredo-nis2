Documento dei Vincoli di Progetto
Titolo: Piattaforma di Conformità (NIS2 / CIS) Versione: 2.0 Data: 28/10/2025 Redatto da: Nautes

1. Scopo del Documento
   Il presente documento definisce i vincoli, l’ambito, i requisiti funzionali e tecnici del progetto “Piattaforma di Conformità”, avente l’obiettivo di realizzare una soluzione software modulare per la gestione della conformità normativa con particolare riferimento alla Direttiva NIS2 e al framework CIS, con possibilità di estensione futura ad altre normative.
   Il documento costituisce riferimento vincolante per:
   •
   delimitare il perimetro funzionale del progetto;
   •
   identificare gli elementi tecnici, organizzativi e operativi che rientrano nel rilascio dell’MVP e delle successive evoluzioni;
   •
   stabilire i criteri di accettazione del lavoro da parte del committente.
2. Ambito del Progetto
   2.1 Funzionalità incluse
   La piattaforma comprenderà, in forma minima ma completa, i seguenti moduli e funzioni:
   •
   Gestione utenti e ruoli: Accesso tramite autenticazione email + password e MFA con Multi-tenant logico cioè di segregazione del dato: ogni azienda vede solo le informazioni di propria competenza. Ruoli previsti:
   o
   Admin: gestione completa dei dati della piattaforma;
   o
   Consulente: esecuzione audit, aggiornamento e lettura dei propri dati.
   o
   Azienda: legge le informazioni importate dal proprio consulente.
   o
   Fornitore: accesso su pagina web dedicata con credenziale temporanea.
   NON è prevista la gestione dei permessi ma ogni ruolo ha le sue funzionalità.
   Anagrafiche:
   •
   Anagrafiche Clienti e Sedi: Funzionalità CRUD per la gestione di aziende e sedi con campi anagrafici di base e relazioni tra sedi e clienti (max 10 campi).
   •
   Anagrafiche consulenti:
   Creati dagli Admin di piattaforma, questi accedono e inseriscono le aziende loro clienti.
   •
   Anagrafica Fornitori:
   Ogni azienda può creare l’anagrafica dei propri fornitori per inviargli l’audit dedicato.
   •
   Catalogo Framework e Codifiche: Struttura gerarchica: Tematica → Categoria/Misura → Requisito, con Ambito trasversale (es. NIS2). Verrà costruito un CRUD dedicato alla gestione delle varie sezioni della normativa (CRUD tematica, categorie, Misura e Requisiti) di fatto L’admin dovrà ricostruire l’impianto normativo in oggetto per renderlo poi disponibile agli utenti di piattaforma.
   La struttura delle informazioni ripercorrerà la struttura del DB Access attualmente in uso.
   In questa struttura sarà possibile mappare più framework (afferenti comunque a strutture di 4 livelli) tramite interfaccia CRUD. Tutti i valori e le codifiche saranno strutturati a livello di database.
   •
   Gestione Audit: Creazione e storicizzazione di audit con i seguenti attributi:
   o
   titolo;
   o
   cliente/sede associata;
   o
   Selezione set requisiti con associazione valori (compliance/rischio) inseriti dal consulente;
   o
   Possibilità di creare azioni legate ad ogni requisito, con possibilità di aggiornarle
   o
   data inizio/fine;
   o
   esecutore.
   Le valutazioni per requisito utilizzano scale codificate (es. da 0 a 1.0). Gli audit sono consultabili in modalità storica e producono report PDF standard.
   •
   Indicatori e Calcoli: Indicatori dichiarati (inseriti dall’operatore) o calcolati automaticamente. Le formule di calcolo saranno riferite solo al calcolo della compliance e della copertura e saranno bloccate lato backend (no editor formule).
   •
   Obiettivi e Azioni: Per ogni requisito (e per ogni cliente) è possibile impostare delle azioni. Le azioni create saranno “anagraficizzate” e potranno essere selezionabili dall’utente ed associate anche ad altri requisiti. Ogni azione include: scadenza, stato, attore responsabile (interno, consulente o fornitore).
   •
   Qualifica Fornitori: Gestione anagrafica fornitori (nome, indirizzo, P.IVA) con storico delle valutazioni e documenti. È previsto l’invio di link temporanei (valido 7 gg) via email per la compilazione di form da parte dei fornitori, senza creazione di utenze permanenti. Il link è eventualmente reinviabile. Le risposte vengono memorizzate e associate agli audit di riferimento.
   •
   Reportistica Standard (PDF): Template di base con intestazione per i seguenti report:
   o
   Report Audit;
   o
   Stato di Compliance per Framework;
   o
   Piano Azioni;
   o
   Qualifica Fornitori.
   •
   Dashboard Base e Export: Due viste principali:
   o
   Cliente (per il consulente): KPI essenziali (es. % compliance, n° azioni aperte, scadenze fornitori);
   o
   Cliente Viewer: stato di conformità e report scaricabili. Export dei dati in formato PDF e CSV.
   •
   Notifiche e Scadenze: Invio automatico di promemoria email su scadenze di azioni e fornitori.
   2.2 Funzionalità escluse o differite
   Sono esclusi dal presente perimetro:
   •
   Integrazione diretta o automatica con la piattaforma OverRisk (potrà essere oggetto di sviluppo successivo).
   •
   Analisi e moduli di analytics avanzati e machine learning (previsti in una fase evolutiva).
   •
   Meccanismi di autenticazione SSO o federata.
   •
   Multi-lingua e localizzazione.
   •
   App mobile o accesso offline.
3. Vincoli Tecnici
   •
   Architettura dati: Database relazionale con codifiche gestite in tabelle dedicate (CRUD). Tutte le regole di calcolo devono risiedere lato backend e non modificabili via interfaccia.
   •
   Sicurezza e autenticazione: Login via email+password e MFA con gestione ruoli. Nessun accesso anonimo o federato. I link temporanei per i fornitori devono avere durata limitata e token univoco.
   •
   Gestione documentale: File caricati (es. documenti fornitori) associati a record specifici, con versioning e storico.
   •
   Reportistica: Generazione PDF lato server, template base statico con intestazione.
   •
   Hosting e ambiente di esecuzione: Cloud AWS
   •
   Interoperabilità: Le esportazioni saranno disponibili in PDF e CSV.
4. Vincoli Organizzativi
   •
   Ogni cliente opera in un ambiente logico separato.
   •
   Gli utenti (consulenti, fornitori e aziende) vedono esclusivamente i propri dati (del proprio tenant).
   •
   Il progetto prevede un MVP iniziale con successivi ampliamenti modulari.
5. Prerequisiti e Dipendenze
   •
   Disponibilità del database di obiettivi già esistente per la codifica iniziale.
   •
   Accesso ai modelli di report.
   •
   Configurazione SMTP o servizio email per notifiche automatiche.
   •
   Definizione dell’anagrafica utenti e ruoli iniziali da parte del committente.
