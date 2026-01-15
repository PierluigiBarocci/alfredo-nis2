# Connection string for Access database
import os
import sys

import pyodbc

db_file = os.path.join(os.getcwd(), "old_piattaforma_conformità_nis2.accdb")
print(f"Tentativo di apertura: {db_file}")
print(f"File esiste: {os.path.exists(db_file)}\n")
conn_str = f"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_file};"

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Get all table names
    tables = cursor.tables(tableType="TABLE")
    table_names = [
        row.table_name for row in tables if not row.table_name.startswith("MSys")
    ]

    print("=== TABELLE NEL DATABASE ===\n")
    for table_name in table_names:
        print(f"\n{'=' * 60}")
        print(f"TABELLA: {table_name}")
        print("=" * 60)

        # Get column information
        columns = cursor.columns(table=table_name)
        print("\nColonne:")
        for col in columns:
            print(f"  - {col.column_name} ({col.type_name})")

        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
        count = cursor.fetchone()[0]
        print(f"\nNumero di record: {count}")

        # Show sample data (first 3 rows)
        if count > 0:
            cursor.execute(f"SELECT TOP 3 * FROM [{table_name}]")
            rows = cursor.fetchall()
            if rows:
                print("\nEsempio dati (prime 3 righe):")
                for i, row in enumerate(rows, 1):
                    print(f"  Riga {i}: {row}")

    conn.close()
    print("\n" + "=" * 60)
    print("Analisi completata!")

except pyodbc.Error as e:
    print(f"Errore: {e}")
    sys.exit(1)
