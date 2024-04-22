# Detection-server
Este repositório tem código python para conseguir usar num Servidor para fazer a deteção e classificação de tigelas em imagens.

No âmbito do projeto final de licenciatura em Engenharia Informática onde o objetivo principal é mensurar o desperdicio alimentar em cantinas institucionais. Este é um primerio passo, sendo o proposto quantificar a sopa que é desperdiçada, através de extração de caracteristicas. Posteriormente pode vir a ser adaptado a outros pratos.

---------------------------------------------------------------------------------------------------------------------

O venv com os packages instalados não pode estar no github, por isso para conseguir usar este código é necessário instalar primeiros todos os packages necessários.

Os modelos treinados (ficheiros .pth) também não estão aqui, porque são ficheiros muito pesados.

### Packages necessários instalar no venv (run automatization.py): -> python3 automatization.py

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



