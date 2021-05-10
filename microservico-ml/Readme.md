# Divisão do processo de treino e inferência de um modelo em diferentes arquivos

## Esse modelo tem como objetivo predizer o MPG de um carro, por meio de suas características

* O Modelo desenvolvido no Jupyter está em: https://github.com/ai2-education-fiep-turma-2/15-DeepLearning/blob/master/Aula3/Keras-PyTorch-Exemplos.ipynb


* Arquivo original : Auto2.csv

* Script para tratamento de dados : prepararDados.py

Gera como saída o arquivo auto_final.csv

* Script para treino do modelo : treinarModelo.py

Gera como saída o modelo treinado autoModel.h5 e o scaler.pkl

* Script para avaliar o modelo treinado: evaluateModel.py

* Script para fazer predições no modelo treinado: predicao.py

## Servindo modelo com microserviços

### A partir do modelo treinado os scripts abaixo mostram como criar um servidor que recebe pedidos por inferências e um exemplo de cliente que poderia ser implementado em alguma aplicação

* Script que implementa um microserviço para servir predições no modelo treinado: predict-server.py

* Script que realiza chamado ao microserviço de predição: predict-client.py

## servindo modelo com tensorflow_model_server

* Linha de comando para colocar servidor de predições no ar
  tensorflow_model_server --rest_api_port=5001 --model_name=auto_model --model_base_path=/home/silvio/serving/

O valor do parâmetro --model_base_path tem que ser igual ao diretório no qual o modelo treinao foi salvo usando o seguinte fragmento de código python:

```
version='1'

export_path='/home/silvio/serving/'+version

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)
```

* script que faz chamadas para o servidor de predições: client_tf_server.py

