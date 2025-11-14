import sqlite3
import os

DB_FILE = "products.db"

def clear_database():
    """Supprime toutes les tables existantes dans la base SQLite."""
    if not os.path.exists(DB_FILE):
        print(f"Aucune base de données '{DB_FILE}' trouvée.")
        return

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Récupère toutes les tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if not tables:
            print("Aucune table à supprimer.")
        else:
            for table in tables:
                name = table[0]
                cursor.execute(f"DROP TABLE IF EXISTS {name};")
                print(f"Table supprimée : {name}")

            conn.commit()
            print("✅ Toutes les tables ont été supprimées avec succès.")

        conn.close()
    except Exception as e:
        print(f"❌ Erreur : {e}")

def delete_database_file():
    """Supprime complètement le fichier de base de données."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"✅ Fichier '{DB_FILE}' supprimé.")
    else:
        print(f"Aucun fichier '{DB_FILE}' trouvé.")

if __name__ == "__main__":
    print("=== Suppression de toutes les tables de la base ===")
    clear_database()

    # Si tu veux aussi supprimer le fichier entier, décommente la ligne ci-dessous :
    delete_database_file()
