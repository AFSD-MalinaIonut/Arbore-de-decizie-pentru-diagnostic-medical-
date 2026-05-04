import pandas
import os
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


def genereaza_imagine_arbore():
    print("1. Se încarcă datele pentru desenare...")
    adresa_scriptului_curent = os.path.dirname(os.path.abspath(__file__))
    adresa_completa_fisier = os.path.join(adresa_scriptului_curent, 'data', 'dataset_simptome.csv')

    tabel_date_medicale = pandas.read_csv(adresa_completa_fisier)

    simptome_pacienti = tabel_date_medicale.drop('Diagnostic', axis=1)
    diagnostice_tinta = tabel_date_medicale['Diagnostic']

    print("2. Se antrenează un model special pentru desenare...")

    model_arbore_vizual = DecisionTreeClassifier(random_state=42, max_depth=4)
    model_arbore_vizual.fit(simptome_pacienti, diagnostice_tinta)

    print("3. Se desenează schema logică...")

    plt.figure(figsize=(16, 10))

    plot_tree(
        model_arbore_vizual,
        feature_names=simptome_pacienti.columns,
        class_names=model_arbore_vizual.classes_,
        filled=True,
        rounded=True,
        fontsize=10
    )


    plt.title("Arbore de Decizie - Diagnostic Medical", fontsize=16)


    adresa_salvare_imagine = os.path.join(adresa_scriptului_curent, 'schema_arbore_decizie.png')
    plt.savefig(adresa_salvare_imagine)

    print(f"Succes! Imaginea a fost salvată aici: {adresa_salvare_imagine}")


    plt.show()


if __name__ == "__main__":
    genereaza_imagine_arbore()