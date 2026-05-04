import pandas
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import os


def antreneaza_model():
    print("1. Se încarcă datele...")
    adresa_scriptului_curent = os.path.dirname(os.path.abspath(__file__))
    adresa_completa_fisier = os.path.join(adresa_scriptului_curent, 'data', 'dataset_simptome.csv')

    tabel_date_medicale = pandas.read_csv(adresa_completa_fisier)

    print("2. Se pregătesc datele (Data Preprocessing)...")
    simptome_pacienti = tabel_date_medicale.drop('Diagnostic', axis=1)
    diagnostice_tinta = tabel_date_medicale['Diagnostic']

    print("3. Se împart datele (80% antrenare, 20% testare)...")
    (simptome_pentru_antrenare,
     simptome_pentru_testare,
     diagnostice_pentru_antrenare,
     diagnostice_pentru_testare) = train_test_split(
        simptome_pacienti, diagnostice_tinta, test_size=0.2, random_state=42)

    print("4. Se antrenează Arborele de Decizie...")
    model_arbore_decizie = DecisionTreeClassifier(random_state=42)
    model_arbore_decizie.fit(simptome_pentru_antrenare, diagnostice_pentru_antrenare)

    print("5. Se evaluează modelul...")
    diagnostice_prezise = model_arbore_decizie.predict(simptome_pentru_testare)
    acuratete_calculata = accuracy_score(diagnostice_pentru_testare, diagnostice_prezise)

    print("-" * 30)
    print(f"Antrenare completă! Acuratețe: {acuratete_calculata * 100:.2f}%")
    print("-" * 30)


    return model_arbore_decizie


def testare_interactiva_pacient(model_antrenat):
    print("\n" + "=" * 40)
    print(" 🩺 SISTEM DE DIAGNOSTIC MEDICAL 🩺 ")
    print("=" * 40)
    print("Răspunde cu 1 (DA) sau 0 (NU) la următoarele întrebări:\n")


    are_febra = int(input("Ai febră? (1 sau 0): "))
    are_tuse = int(input("Ai tuse? (1 sau 0): "))
    are_oboseala = int(input("Te simți obosit? (1 sau 0): "))
    are_durere_in_gat = int(input("Te doare în gât? (1 sau 0): "))
    are_pierdere_gust = int(input("Ți-ai pierdut gustul sau mirosul? (1 sau 0): "))
    are_stranut = int(input("Strănuți des? (1 sau 0): "))
    are_dificultati_respiratorii = int(input("Ai dificultăți de respirație? (1 sau 0): "))


    date_pacient_nou = pandas.DataFrame([{
        "Febra": are_febra,
        "Tuse": are_tuse,
        "Oboseala": are_oboseala,
        "Durere_in_gat": are_durere_in_gat,
        "Pierdere_gust_miros": are_pierdere_gust,
        "Stranut": are_stranut,
        "Dificultati_respiratorii": are_dificultati_respiratorii
    }])


    diagnostic_estimat = model_antrenat.predict(date_pacient_nou)

    print("\n" + "-" * 40)

    print(f"🤖 Diagnosticul calculat de AI este: >> {diagnostic_estimat[0].upper()} <<")
    print("-" * 40 + "\n")


if __name__ == "__main__":

    modelul_nostru_inteligent = antreneaza_model()


    testare_interactiva_pacient(modelul_nostru_inteligent)