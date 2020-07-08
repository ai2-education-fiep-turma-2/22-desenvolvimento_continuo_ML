# Usando TFX serving

* Instalando o tensorflow_model_server para servir modelos como microserviços
```
echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
apt update
```

* Iniciando Microserviço que publica o modelo de predição:
```
tensorflow_model_server --rest_api_port=8501 --model_name=fashion_model --model_base_path=/tmp
```

* Realizando predicoes a partir de imagens
  * O modelo recebe imagens com as seguintes dimensoes 28 x 28 
  * antes de realizar a predicao é feito a adequacao da imagem
  
```
python clientMnist.py
```
