import streamlit
import pandas
import os
from sklearn.tree import DecisionTreeClassifier



def antreneaza_model_pentru_web():
    adresa_scriptului_curent = os.path.dirname(os.path.abspath(__file__))
    adresa_completa_fisier = os.path.join(adresa_scriptului_curent, 'data', 'dataset_simptome.csv')

    tabel_date_medicale = pandas.read_csv(adresa_completa_fisier)

    simptome_pacienti = tabel_date_medicale.drop('Diagnostic', axis=1)
    diagnostice_tinta = tabel_date_medicale['Diagnostic']

    model_arbore_decizie = DecisionTreeClassifier(random_state=42)
    model_arbore_decizie.fit(simptome_pacienti, diagnostice_tinta)

    return model_arbore_decizie



modelul_nostru_inteligent = antreneaza_model_pentru_web()


streamlit.title("🩺 Sistem de Diagnostic Medical AI")
streamlit.write("Bifează simptomele pe care le ai în acest moment pentru a primi un diagnostic estimativ.")

streamlit.markdown("---")


are_febra = streamlit.checkbox("Am febră")
are_tuse = streamlit.checkbox("Am tuse")
are_oboseala = streamlit.checkbox("Mă simt obosit(ă)")
are_durere_in_gat = streamlit.checkbox("Mă doare în gât")
are_pierdere_gust = streamlit.checkbox("Mi-am pierdut gustul sau mirosul")
are_stranut = streamlit.checkbox("Strănut des")
are_dificultati_respiratorii = streamlit.checkbox("Am dificultăți de respirație")

streamlit.markdown("---")


if streamlit.button("Află Diagnosticul"):

    date_pacient_nou = pandas.DataFrame([{
        "Febra": int(are_febra),
        "Tuse": int(are_tuse),
        "Oboseala": int(are_oboseala),
        "Durere_in_gat": int(are_durere_in_gat),
        "Pierdere_gust_miros": int(are_pierdere_gust),
        "Stranut": int(are_stranut),
        "Dificultati_respiratorii": int(are_dificultati_respiratorii)
    }])


    diagnostic_estimat = modelul_nostru_inteligent.predict(date_pacient_nou)


    streamlit.success(f"Diagnosticul estimat de Inteligența Artificială este: **{diagnostic_estimat[0].upper()}**")