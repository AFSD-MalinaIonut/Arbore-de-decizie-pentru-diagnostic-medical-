import random
import pandas
import os


def genereaza_pacienti_fictivi(numar_total_pacienti):
    lista_cu_toti_pacientii = []
    lista_boli_posibile = ["Raceala", "Gripa", "COVID-19", "Alergie"]

    for numar_curent in range(numar_total_pacienti):
        boala_pacientului = random.choice(lista_boli_posibile)

        are_febra = 0
        are_tuse = 0
        are_oboseala = 0
        are_durere_in_gat = 0
        are_pierdere_gust_miros = 0
        are_stranut = 0
        are_dificultati_respiratorii = 0

        if boala_pacientului == "Raceala":
            if random.random() < 0.20: are_febra = 1
            if random.random() < 0.80: are_tuse = 1
            if random.random() < 0.50: are_oboseala = 1
            if random.random() < 0.90: are_durere_in_gat = 1
            if random.random() < 0.90: are_stranut = 1

        elif boala_pacientului == "Gripa":
            if random.random() < 0.90: are_febra = 1
            if random.random() < 0.80: are_tuse = 1
            if random.random() < 0.90: are_oboseala = 1
            if random.random() < 0.60: are_durere_in_gat = 1
            if random.random() < 0.10: are_stranut = 1

        elif boala_pacientului == "COVID-19":
            if random.random() < 0.80: are_febra = 1
            if random.random() < 0.80: are_tuse = 1
            if random.random() < 0.90: are_oboseala = 1
            if random.random() < 0.70: are_pierdere_gust_miros = 1
            if random.random() < 0.50: are_dificultati_respiratorii = 1

        elif boala_pacientului == "Alergie":
            if random.random() < 0.40: are_tuse = 1
            if random.random() < 0.30: are_oboseala = 1
            if random.random() < 0.95: are_stranut = 1
            if random.random() < 0.20: are_dificultati_respiratorii = 1

        fisa_medicala_pacient = {
            "Febra": are_febra,
            "Tuse": are_tuse,
            "Oboseala": are_oboseala,
            "Durere_in_gat": are_durere_in_gat,
            "Pierdere_gust_miros": are_pierdere_gust_miros,
            "Stranut": are_stranut,
            "Dificultati_respiratorii": are_dificultati_respiratorii,
            "Diagnostic": boala_pacientului
        }

        lista_cu_toti_pacientii.append(fisa_medicala_pacient)

    return lista_cu_toti_pacientii


if __name__ == "__main__":
    print("Începem generarea celor 200 de pacienți...")
    date_generate = genereaza_pacienti_fictivi(200)
    tabel_final = pandas.DataFrame(date_generate)


    adresa_scriptului_curent = os.path.dirname(os.path.abspath(__file__))
    adresa_completa_fisier = os.path.join(adresa_scriptului_curent, 'data', 'dataset_simptome.csv')

    print(f" [DEBUG GENERATOR] Salvez noile date la adresa: {adresa_completa_fisier}")


    os.makedirs(os.path.join(adresa_scriptului_curent, 'data'), exist_ok=True)


    tabel_final.to_csv(adresa_completa_fisier, index=False)

    print("Succes! Datele au fost suprascrise. Acum poți rula main.py!")