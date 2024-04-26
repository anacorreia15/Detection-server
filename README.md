# Detection-server
Este repositório tem código python para conseguir correr num Servidor para que faça a deteção e classificação de tigelas em imagens.

No âmbito do projeto final de licenciatura em Engenharia Informática onde o objetivo principal é mensurar o desperdicio alimentar em cantinas institucionais. Este é um primerio passo, sendo o proposto quantificar a sopa que é desperdiçada, através de extração de caracteristicas. Posteriormente pode vir a ser adaptado a outros pratos.

---------------------------------------------------------------------------------------------------------------------

(O venv com os packages instalados não pode estar no github, por isso para conseguir usar este código é necessário instalar primeiros todos os packages necessários.)
Os modelos treinados (ficheiros .pth) também não estão aqui, porque são ficheiros muito pesados.

Como correr automatization.py:
$ cd /home/server/Desktop/Projeto/resnet-fasterrcnn_1
(criar o venv caso não esteja criado -> python3 -m venv venv)
$ source venv/bin/activate
(instalar os packages caso necessário)
$ python3 automatization.py

### Packages necessários instalar no venv: (instalar o pip em primeiro lugar, caso não esteja instalado)

pip install watchdog
pip install numpy
pip install opencv-python
pip install torch torchvision
pip install pyyaml
pip install matplotlib
pip install vision_transformers
pip install albumentations
pip install pandas
pip install wandb
pip install tensorboard

sudo apt install libgtk2.0-dev pkg-config



