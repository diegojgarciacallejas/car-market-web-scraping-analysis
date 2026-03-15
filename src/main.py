import csv
import os
from typing import Dict, List

from scrapers import (
    Autoscout24_francia,
    clicars,
    Autoscout24_holanda,
    Flexicar,
    cochesmobile,
    Ocasion_plus_final,
    autocasion,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")


def escrbir_csv(nombre_archivo: str, listado: List[Dict]) -> None:
    output_path = os.path.join(RAW_DATA_DIR, nombre_archivo + ".csv")
    with open(output_path, "w", newline="\n", encoding="utf-8") as csvfile:
        if listado:
            campos = listado[0].keys()
            csvtool = csv.DictWriter(csvfile, fieldnames=campos)
            csvtool.writeheader()
            for elem in listado:
                csvtool.writerow(elem)


if __name__ == "__main__":
    # coches_cliclars = clicars.funcion_clicars()
    # escrbir_csv("clicars", coches_cliclars)

    # coches_cochesmobile = cochesmobile.funcion_cochesmobile()
    # escrbir_csv("cochesmobile", coches_cochesmobile)

    # coches_autoscout24_francia = Autoscout24_francia.funcion_AutoScout24()
    # escrbir_csv("autoscout24_france", coches_autoscout24_francia)

    # coches_flexicar = Flexicar.flexicar()
    # escrbir_csv("flexicar", coches_flexicar)

    coches_autocasion = autocasion.funcion_autocar()
    escrbir_csv("autocasion", coches_autocasion)

    # coches_ocasioplus = Ocasion_plus_final.funcion_ocasionplus()
    # escrbir_csv("ocasionplus", coches_ocasioplus)

    coches_autoscout24_holanda = Autoscout24_holanda.funcion_autoscout_holada()
    escrbir_csv("autoscout24_netherlands", coches_autoscout24_holanda)