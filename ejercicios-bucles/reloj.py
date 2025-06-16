import time
from datetime import datetime
 
try:
    while True:
        ahora = datetime.now().strftime(
            "%H:%M:%S")
        print("\nHora actual: {}".format(ahora),
            end="")
        time.sleep(1)
 
 
except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")