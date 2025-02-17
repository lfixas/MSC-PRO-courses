# 0 - Prelude to Kubernetes in YAML major, Op. 42

## A little quiz to start with 

### Where is Kubernetes ?

Kubernetes est une plateforme de gestion de conteneurs qui peut être déployée de plusieurs manières : 

- Sur site (On-Premise) : Kubernetes peut être installé et gérer sur des serveurs physiques ou machines virtuelles ; 
- Cloud public : Plusieurs fournisseurs de cloud offrent des services Kubernetes managés - Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Services (EKS), Azure Kubernetes Service (AKS) ; 
- Cloud privé : Kubernetes peut aussi être installé sur des clouds privés, comme OpenStack. 

### What is Kubernetes ?

Kubernetes est une plateforme open source, portable et extensible pour gérer des "charges de travail" (workloads) et des services containerisés, ce qui facilite à la fois la configuration et l'automatisation. 

### Why is Kubernetes ? 

Kubernetes est utilisé pour plusieurs raisons clés qui répondent à des besoins de gestion des applications et des services déployés sous forme de conteneurs. 

- **Automatisation de la gestion des conteneurs :** Kubernetes permet d'automatiser le déploiement, la gestion et la mise à l'échelle d'applications conteneurisées. 

- **Evolutivité et haute disponibilité :** Kubernetes assure la haute disponibilité des applications en surveillant constamment l'état des conteneurs et en les redémarrant si nécessaire. 

- **Portabilité :** Kubernetes est indépendant des fournisseurs de cloud, donc il offre une grande portabilité. 

- **Gestion simplifiée de la configuration et des secrets :** Kubernetes fournit des mécanismes intégrés pour gérer les configurations et les secrets de manière sécurisée et centralisée, ce qui simplifie la gestion des informations sensibles et des paramètres de configuration. 

- **Récupération automatique :** Kubernetes surveille l'état des noeuds et des conteneurs, et il peut automatiquement redémarrer les conteneurs défaillants, remplacer et redémarrer les noeuds, et même tuer les conteneurs qui ne répondent pas aux contrôles de santé définis. 

- **Gestion efficace des ressources** : Kubernetes optimise l'utilisation des ressources matérielles en répartissant les charges de travail de manière efficace à traver les noeufs du cluster, permettant ainsi une utilisation optimale des ressources disponibles. 

### What is a cluster ? 

Un cluster est un ensemble de machines sur lesquelles Kubernetes est installé. Ces machines travaillent ensemble pour exécuter et gérer les applications conteneurisées. Un cluster Kubernetes est composé de deux types principaux composants.  

#### Cluster - Plan de contrôle (control plane)

Le plan de contrôle gère l'état global du cluster, prenant les décisions pour ce qui est du déploiement et de la gestion des applications. Il comprend plusieurs composants principaux. 

- API Server ; 
- Etcd : base de données clé-valeur hautement disponible qui stocke l'état de tout le cluster de Kubernetes ; 
- Controller Manager ; 
- Scheduler.

#### Cluster - Noeuds de travail (worker nodes)

Les noeuds de travail sont les machines sur lesquelles les conteneurs des applications sont réellement exécutés. Chaque noeud de travail contient plusieurs composants : 

- **Kubelet** : un agent qui s'éxécute sur chaque noeuf de travail et assure que les conteneurs sont exécutés dans des pods. Il communique avec le control plane via l'API Server ; 

- **Kube-proxy** : un réseau proxy qui maintient les règles de réseau sur les noeuds, permettant la communication entre les services et les pods du cluster ; 

- **Container Runtine** : Logiciel responsable de l'exécution des conteneurs, par exemple docker. 

### What is a node ?

Un noeud dans Kubernetes est une machine sur laquelle Kubernetes exécute des applications conteneurisées. Les noeuds constituent les unités de base de l'infrastructure d'exécution des applications dans un cluster Kubernetes. 

- **Noeuds de travail (worker nodes)** : les noeuds de travail sont des machines sur lequelles les conteneurs des applications sont déployées et exécutés. Chaque noeud de travail contient plusieurs composants qui sont essentiels pour la gestion des contenrus et la communication avec le controle plane. 

- **Noeuds du plan de contrôle (control plane nodes)** : les noeuds du plan de contrôle sont responsables de la gestion globale du cluster, de la planification des pods, de la maintenance de l'état du cluster, etc... Ces noeuds exécutent les composants principaux du plan de contrôle tels que l'API Server, etcd, le Scheduler et le Controller Manager. 

### What is a pod ? 

Un pod est la plus petite unité déployable et gérable dans l'architecture Kubernetes. Il représente une instance d'une application ou d'un composant d'application. Un pod encapsule un ou plusieurs conteneurs (généralement un seul), des ressources de stockage, une adresse IP réseau unique, ainsi que des options sur la manière de s'éxécuter. 

### In what way(s) are Kubernetes and Docker related ? 

Kubernetes et Docker sont deux technologies complémentaires qui peuvent être utilisées ensemble pour gérer des applications conteneurisées. 