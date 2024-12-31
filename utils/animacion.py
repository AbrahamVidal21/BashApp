from rich.progress import Progress
import time

def animacion_proceso(tiempo_espera):
    """
    Muestra una barra de progreso durante el tiempo de espera.
    """
    with Progress() as progress:
        task = progress.add_task("[cyan]Procesando...", total=tiempo_espera)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(1)  # Espera de 1 segundo por avance