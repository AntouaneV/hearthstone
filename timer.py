import signal
import time

def fonction_timer(signum, frame):
    print("Temps écoulé !")

# Pour attendre 5 secondes avant de lancer le timer
signal.alarm(5)
signal.signal(signal.SIGALRM, fonction_timer)

# Pour désactiver le timer
signal.alarm(0)
