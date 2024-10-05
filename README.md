__________________________ ITALIAN VERSION __________________________
# Csv To Pdf

Questo programma Python permette di elaborare file CSV, offrendo all'utente la possibilità di selezionare le colonne di interesse e di aggregare i dati in base a specifici criteri. L'obiettivo è fornire uno strumento flessibile e personalizzabile per la manipolazione di dataset strutturati, senza la necessità di scrivere codice complesso.

Funzionalità principali:
 - Selezione colonne: L'utente può scegliere quali colonne del file CSV mantenere nell'output, filtrando solo le informazioni rilevanti.
 - Aggregazione dati: È possibile raggruppare i dati in base ai valori di una colonna specifica, facilitando l'analisi e la gestione dei dataset.
 - Semplice da usare.
Questo strumento è ideale per chi deve lavorare con grandi quantità di dati CSV e vuole poterli manipolare in modo efficiente e personalizzato.

## Requisiti e Input

Per utilizzare questo programma, assicurati di avere i seguenti file nella cartella `resources` all'interno della directory del progetto:

1. **logo.png**: Questo file deve contenere il logo che verrà inserito nella parte superiore del documento PDF generato.
2. **document.csv**: Questo è il file CSV che verrà elaborato per generare il documento PDF (controllare che il separatore sia ; altrimenti modificare il codice indicando come separatore , o qualsiasi altro separatore sia stato usato ).
3. **collapse.txt**: Questo file deve contenere una sola parola, che è il nome della colonna secondo cui i dati verranno raggruppati (collassati).
4. **columns.txt**: Questo file deve contenere l'elenco delle colonne che si desidera mantenere nel file CSV, vanno elencate una sotto l'altra come nell'esempio.

## Utilizzo

### Prerequisiti
Prima di usare il programma, assicurati di avere **Python 3** installato sul tuo sistema. Ecco come installare Python 3 su macOS e Windows:

#### Installare Python 3 su macOS:
1. Apri il Terminale.
2. Controlla se Python 3 è già installato digitando:
   ```bash
   python3 --version
   ```
Se Python 3 è installato, dovresti vedere il numero di versione. 3. Se Python 3 non è installato, installalo usando Homebrew (se non hai Homebrew, puoi installarlo da https://brew.sh/):
   ```bash
   brew install python
   ```
Dopo l'installazione, verifica digitando:
   ```bash
   python3 --version
   ```
#### Installare Python 3 su Windows:

Vai sul sito ufficiale di Python: https://www.python.org/downloads/
1. Scarica l'ultima versione di Python 3 per Windows.
2. Esegui il programma di installazione e assicurati di selezionare la casella "Add Python to PATH" durante l'installazione.
3. Dopo l'installazione, apri il Prompt dei comandi (o PowerShell) e verifica l'installazione digitando:
   ```bash
   python3 --version
   ```
#### Eseguire il Programma
Una volta installato Python 3, segui questi passaggi per eseguire il programma:

1. Sposta la cartella del progetto (es. CsvToPdf) sul desktop.
2. Apri il terminale (o il Prompt dei comandi/PowerShell su Windows).
3. Esegui il programma digitando il seguente comando:
   ```bash
   python3 ~/Desktop/CsvToPdf/csvToPdf.py
   ```
Questo comando presuppone che la cartella del progetto si trovi sul desktop. Se la cartella si trova in un'altra posizione, modifica il percorso di conseguenza.

Marco lizza 2024 ©

__________________________ ENGLISH VERSION __________________________

This Python program allows you to process CSV files, giving the user the ability to select which columns to keep and to aggregate data based on specific criteria. The goal is to provide a flexible and customizable tool for handling structured datasets without the need to write complex code.

Key Features:
 - Column Selection: Users can choose which columns from the CSV file to retain in the output, filtering only the relevant information.
 - Data Aggregation: It is possible to group data based on the values of a specific column, making dataset analysis and management easier.
 - User-friendly.
This tool is ideal for those working with large amounts of CSV data who want to manipulate it efficiently and in a customized way.

## Requirements and Input

To use this program, ensure you have the following files in the `resources` folder within the project directory:

1. **logo.png**: This file should contain the logo that will be placed at the top of the generated PDF document.
2. **document.csv**: This is the CSV file that will be processed to generate the PDF document (ensure that the separator is ;; otherwise, modify the code to indicate , or any other separator that has been used).
3. **collapse.txt**: This file should contain a single word, which is the name of the column by which the data will be grouped (collapsed).
4. **columns.txt**: This file should contain the list of columns that you want to keep from the CSV file, listed one under the other as shown in the example.

## Usage

### Prerequisites
Before using the program, make sure you have **Python 3** installed on your system. Here's how to install Python 3 on macOS and Windows:

#### Installing Python 3 on macOS:
1. Open Terminal.
2. Check if Python 3 is already installed by typing:
   ```bash
   python3 --version
   ```
If Python 3 is installed, you should see the version number. 3. If Python 3 is not installed, install it using Homebrew (if you don't have Homebrew installed, visit https://brew.sh/):
   ```bash
   brew install python
   ```
After installation, verify it by running:
    ```bash
    python3 --version
    ```
#### Installing Python 3 on Windows:

Go to the official Python website: https://www.python.org/downloads/
1. Download the latest Python 3 version for Windows.
2. Run the installer and make sure to check the box "Add Python to PATH" during installation.
3. After installation, open Command Prompt (or PowerShell) and verify the installation by typing:
   ```bash
    python --version
   ```
or
   ```bash
   python3 --version
   ```
#### Running the Program
Once you have Python 3 installed, follow these steps to run the program:

1. Move the project folder (e.g., CsvToPdf) to your desktop.
2. Open the terminal (or Command Prompt/PowerShell on Windows).
3. Run the program by typing the following command:
   ```bash
   python3 ~/Desktop/CsvToPdf/csvToPdf.py 
   ```
This command assumes the project folder is located on your desktop. If the folder is in a different location, adjust the path accordingly.

Marco lizza 2024 ©
