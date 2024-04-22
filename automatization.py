import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#from detection import detection_function, parse_opt
from detection_cut import detection_function, parse_opt

args = parse_opt()
#done_folder = './images/Done'

def detection(image_path, directory, filename):
    # Classificar e detetar tigela na imagem
    detection_function(args, image_path)

    #Eliminar as imagens classificadas
    os.remove(image_path)


# Função para processar todas as imagens no diretório
def process_existing_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(directory, filename)

            detection(image_path, directory, filename)

# Diretório que você quer monitorar
directory_to_watch = os.path.abspath("./images")

# Processar imagens existentes antes de iniciar a observação do Watchdog
process_existing_images(directory_to_watch)

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith((".jpg", ".jpeg", ".png")):
            print(f"Detected new image: {event.src_path}")
            filename = os.path.basename(event.src_path)

            detection(event.src_path, directory_to_watch, filename)

# Crie um observador para monitorar o diretório
observer = Observer()
observer.schedule(ImageHandler(), directory_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(5)  # Espera por 5 segundos antes de verificar novamente
except KeyboardInterrupt:
    observer.stop()

observer.join()
