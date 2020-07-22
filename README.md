# Steps to run and deploy the application on to Kubernetes Services

## Prerequisites

- Python2.X or Python 3.X
- Docker

## Testing Locally

### Step - 1: Run the flask app locally

```
source venv/bin/activate
```
```
pip intall -r requirements.txt
```
```
python app.py
```

### Step - 2: Build the Docker image

```
docker build -t flask-web-app:latest .
```

### Step - 3: Build a container from the docker images and run the app

```
docker run -p -d 5000:5000 flask-web-app
```

# Kubernetes

## installation
Docker install with docker-compose:
```
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get -y install docker-ce
sudo usermod -aG docker ${USER}
sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

Kuberentes install and create cluster:
```
sudo systemctl enable docker
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt-get install kubeadm kubelet kubectl -y
sudo hostnamectl set-hostname kmaster
ifconfig
sudo nano /etc/hosts
sudo swapoff -a
sudo nano /etc/fstab
```
Reboot to apply changes

Then create cluster:
```
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Create Network install for pods:
```
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```
Give Permission to access network and access:
```
kubectl taint nodes kmaster node-role.kubernetes.io/master-
```

## Secrets

Create the necessary secrets:

```
kubectl create secret generic mysql-pass --from-literal=password=<your_password>
kubectl create secret generic secret-key-base --from-literal=secret-key-base=50dae16d7d1403e175ceb2461605b527cf87a5b18479740508395cb3f1947b12b63bad049d7d1545af4dcafa17a329be4d29c18bd63b421515e37b43ea43df64
```

## mysql

Create the volumes:

```
kubectl create -f ./kube/mysql/
```

Create the Service and Deployment

```
kubectl run -it --rm --image=mysql:5.6 --restart=Never mysql-client -- mysql -h k8s-sample-app-mysql -p<your_password>
```

# you can then run normal MySQL commands like:
mysql> show databases;


## Dependiences

Create the Service

```
kubectl create -f ./kube/depend/
```

## ElasticSearch

You will have to build and push the Rails image. Make sure you update the ```lib/tasks/docker.rake``` with your own username.

First run the setup Kube job to create the database and run migrations
Create the Rails Service

```
kubectl create -f ./kube/elastic/
```


## Rails

You will have to build and push the Rails image. Make sure you update the ```lib/tasks/docker.rake``` with your own username.

First run the setup Kube job to create the database and run migrations
Create the Rails Service

```
kubectl create -f ./kube/deploy/
```


## Check

Finally check that pods:

```
kubectl get pods
```

## Results
 Finally we can access that URL here

Then access it at ```http://localhost:4000/admin```.





