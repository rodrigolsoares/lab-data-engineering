# Lab data engineering



## Create user airflow
```bash
sudo docker exec -it [nome do container] /bin/bash

airflow users create --role Admin \
--username admin \
--password admin \
--email email@email.com \
--firstname teste \
--lastname teste

FLASK_APP=airflow.www.app flask fab create-admin
```

## Home screen Airflow 
![Alt text](docs/home-screen-airflow.PNG?raw=true "Arquitetura")
