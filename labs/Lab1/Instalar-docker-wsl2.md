## Activar wsl2 

En powershell realizar lo siguiente.

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-default-version 2
```

## Instalar and Configurar Ubuntu

Para instalar seguir los siguientes pasos.

```powershell
# instala ubuntu desde la store
# abre la app ubuntu
# configura username y password
# en powershell configura la distribución
wsl --set-version Ubuntu 2
```


## Instalar Docker & Docker-compose en Ubuntu

Abrir la distribucion de linux Ubuntu en WSL 

```bash
#actualiza e instala paquetes
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common libssl-dev libffi-dev git wget nano

#añade usuario y grupo
sudo groupadd docker
sudo usermod -aG docker ${USER}

#añade docker key y repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

#Instala docker y docker-compose
sudo apt-get install -y docker-ce containerd.io docker-compose

#Instala docker-compose (si el comando anterior fallo)
sudo curl -sSL https://github.com/docker/compose/releases/download/v`curl -s https://github.com/docker/compose/tags | grep "compose/releases/tag" | sed -r 's|.*([0-9]+\.[0-9]+\.[0-9]+).*|\1|p' | head -n 1`/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
```

## Correr docker al inicio

correr el siguiente bash

```bash
cat <<EOF >> ~/.profile
if ! service docker status > /dev/null; then
  echo "docker service not running, starting..."
  sudo service docker start
fi
EOF

source ~/.profile
```

## Consideraciones

```powershell
#Para reiniciar wsl (use en caso de que lo anterior no funciones)
wsl --shutdown

# Para comunicar contenedores no uses localhost, apunta a: [terminal de ubuntu] - la primera IP que aparece usando:.
ip addr | grep eth0 | grep inet

# Para asegurar que el servicio de Docker se ejecute al iniciar y así evitar tener que usar sudo, realice lo siguiente:
wsl.exe -u root service docker status || wsl.exe -u root service docker start
```
