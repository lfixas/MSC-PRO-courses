# T-NSA-501 Network Configuration Project


## Description
Ce projet implique la configuration de quatre machines virtuelles pour créer une infrastructure réseau sécurisée et efficace. Il comprend une passerelle OpenBSD, un serveur web FreeBSD, et des machines clients pour les employés et les administrateurs.

## Table des Matières
- [Installation](#installation)
  - [VM 1 - Passerelle](#vm-1---passerelle)
  - [VM 2 - Serveur Web](#vm-2---serveur-web)
  - [VM 3 & VM 4 - Clients](#vm-3--vm-4---clients)
- [Utilisation](#utilisation)
  - [Passerelle](#passerelle)
  - [Serveur Web](#serveur-web)
  - [Clients](#clients)
- [Graphiques et Tableaux](#graphiques-et-tableaux)
- [Support](#support)
- [Contributeurs](#contributeurs)

## Installation

### VM 1 - Passerelle
Objectif : Configurer la VM 1 comme une passerelle pour gérer le trafic entre les réseaux internes et Internet.

- **Système d'exploitation :** OpenBSD 7.4
- **Configuration :** 4 cartes réseau, bridge/NAT, DHCP pour 3 LANs privés.
- **Instructions détaillées :** [OpenBSD](https://www.openbsd.org/)

  Étapes :

    - Installation d'OpenBSD 7.4.
    - Configuration des 4 cartes réseau.
    - Mise en place d'un pont ou NAT pour connecter les réseaux privés à Internet.
    - Configuration du serveur DHCP pour attribuer des adresses IP aux machines sur les réseaux privés.
    - Définition des adresses IP statiques pour les cartes réseau internes.
    - Création de 3 LANs avec les configurations spécifiées (Administration, Serveur, Employé).


### VM 2 - Serveur Web
Objectif : Mettre en place un serveur web NGINX avec PHP 7.4 et une base de données MySQL.

- **Système d'exploitation :** FreeBSD 13
- **Services :** NGINX, PHP 7.4, MySQL 80-server.
- **Configuration :** Adresse IP statique via DHCP.
- **Instructions détaillées :** [FreeBSD](https://www.freebsd.org/where/)

  Étapes :

    - Installation de FreeBSD 13.
    - Installation et configuration de NGINX.
    - Installation de [PHP 7.4](https://setupexample.com/install-php74-on-freebsd) et des modules requis.
    - Configuration du serveur pour obtenir une adresse IP statique via DHCP (192.168.42.70).
    - Installation de MySQL 80-server et configuration de la base de données nsa501.
    - Création d'un utilisateur 'backend' avec tous les droits sur la table nsa501.


### VM 3 & VM 4 - Clients
Objectif : Préparer les machines clients pour les employés et les administrateurs.

- **Système d'exploitation :** Au choix avec GUI
- **Configuration :** Récupération automatique des paramètres réseau via DHCP.

  Étapes :
    - Installation d'un système d'exploitation avec interface graphique.
    - Configuration pour récupérer automatiquement les paramètres réseau via DHCP.

---

# Utilisation

## Passerelle

### Gestion du Trafic Réseau

La VM 1, configurée comme passerelle, joue un rôle crucial dans la gestion du trafic entre les différents LANs et Internet.

#### Routage et NAT (Network Address Translation)
- **Fonctionnement du NAT :**
  - Permet aux machines sur les LANs privés d'accéder à Internet.
  - Modifie les adresses IP des paquets sortants pour qu'ils apparaissent comme provenant de l'adresse IP publique de la passerelle.
  - Redirige le trafic entrant vers les adresses IP internes appropriées.

#### Gestion des Interfaces Réseau
- **Configuration des Cartes Réseau :**
  - Quatre cartes réseau, chacune connectée à un LAN différent ou à Internet.
  - Gère le trafic entrant et sortant pour la communication entre les réseaux internes et l'extérieur.

#### DHCP (Dynamic Host Configuration Protocol)
- **Fonctionnement du DHCP :**
  - Attribue automatiquement des adresses IP, des masques de sous-réseau, des passerelles par défaut et des informations DNS.

### Sécurité et Filtrage de Paquets

Des règles de filtrage de paquets sont utilisées pour contrôler le trafic et assurer la sécurité.

#### LAN d'Administration
- **Accès et Restrictions :**
  - Accès complet aux services sur le LAN Serveur.
  - Connexions sortantes autorisées vers le LAN Serveur.
  - Connexions entrantes limitées aux réponses aux requêtes initiées par le LAN.

#### LAN Serveur
- **Gestion du Trafic :**
  - Accès restreint selon les besoins des services hébergés.
  - Règles basées sur les services (ex. : trafic HTTP/HTTPS pour un serveur web).

#### LAN Employé
- **Restrictions :**
  - Accès limité au serveur web via HTTP et HTTPS uniquement.
  - Blocage des autres formes de trafic vers le LAN Serveur.

#### Accès Internet
- **Contrôle du Trafic :**
  - Tous les LANs peuvent accéder à Internet.
  - Restrictions sur certains ports ou protocoles pour prévenir les activités non autorisées.

#### Interconnexion des LANs
- **Règles de Communication :**
  - Règles spécifiques pour la communication entre les LANs.
  - Filtrage basé sur les adresses IP, les ports et les protocoles.

---

## Serveur Web

### Gestion du Serveur Web NGINX

La VM 2 est configurée comme un serveur web sous FreeBSD 13, utilisant NGINX. Voici les étapes pour gérer ce serveur :

#### Démarrage et Arrêt de NGINX
- **Pour démarrer NGINX :**
  ```bash
  service nginx start
  ```
- **Pour arrêter NGINX :**
  ```bash
  service nginx stop
  ```
- **Pour redémarrer NGINX (après des modifications de configuration) :**
  ```bash
  service nginx restart
  ```

#### Configuration de NGINX
- Le fichier de configuration principal se trouve à `/usr/local/etc/nginx/nginx.conf`.
- Pour gérer les sites web :
  - Éditez les fichiers dans `/usr/local/etc/nginx/sites-available/`.
  - Créez un lien symbolique dans `/usr/local/etc/nginx/sites-enabled/`.
  - Redémarrez NGINX pour appliquer les changements.

#### Déploiement de Pages Web
- Placez les fichiers web (HTML, CSS, JavaScript) dans `/usr/local/www/nginx/`.
- Assurez-vous que les permissions des fichiers permettent à NGINX de les lire.

#### Gestion des Logs
- Les logs d'accès et d'erreur se trouvent dans `/var/log/nginx/`.
- Utilisez ces fichiers pour le débogage et la surveillance.

### Gestion de la Base de Données MySQL

La VM 2 inclut MySQL pour le stockage des données.

#### Démarrage et Arrêt de MySQL
- **Pour démarrer MySQL :**
  ```bash
  service mysql-server start
  ```
- **Pour arrêter MySQL :**
  ```bash
  service mysql-server stop
  ```

#### Accès à MySQL
- Accédez à MySQL via :
  ```bash
  mysql -u root -p
  ```
- Entrez le mot de passe à l'invite.

#### Création et Gestion de l'Utilisateur 'backend'
- **Créer un utilisateur :**
  ```sql
  CREATE USER 'backend'@'localhost' IDENTIFIED BY 'password';
  ```
- **Accorder des droits sur la table nsa501 :**
  ```sql
  GRANT ALL PRIVILEGES ON nsa501.* TO 'backend'@'localhost';
  FLUSH PRIVILEGES;
  ```

#### Gestion des Données
- **Exporter des données :**
  ```bash
  mysqldump -u backend -p nsa501 > backup.sql
  ```
- **Importer des données :**
  ```bash
  mysql -u backend -p nsa501 < backup.sql
  ```

#### Sécurité et Maintenance
- Changez régulièrement les mots de passe.
- Surveillez les logs d'accès.
- Effectuez des sauvegardes régulières.

---

## Clients

Les VM 3 et VM 4 sont configurées comme des machines clients dans notre infrastructure réseau, destinées respectivement aux employés et aux administrateurs.

### Accès Réseau

#### Connexion au Réseau
- **Configuration DHCP :**
  - Les clients obtiennent automatiquement leurs paramètres réseau via DHCP, incluant l'adresse IP, le masque de sous-réseau, la passerelle par défaut et les informations DNS.
  - Ils peuvent communiquer avec d'autres machines sur le même LAN et avec des ressources sur d'autres LANs via la passerelle.

#### Accès au Serveur Web
- **Navigation Web :**
  - Utilisez un navigateur pour accéder au serveur web hébergé sur la VM 2.
  - Entrez l'adresse IP du serveur web (ex. `http://192.168.42.70`) pour charger le site.
  - Assurez-vous que les règles de pare-feu et de filtrage de paquets autorisent ce trafic.

### Protocoles de Communication

#### HTTP et HTTPS
- **Utilisation des Protocoles :**
  - Les clients peuvent utiliser HTTP et HTTPS pour accéder aux ressources web.
  - HTTP est moins sécurisé ; HTTPS est recommandé pour la confidentialité et l'intégrité des données.

#### Restrictions de Protocole
- **Conformité aux Règles de Sécurité :**
  - Certaines restrictions peuvent être appliquées selon les règles de la passerelle.
  - Par exemple, le LAN des employés peut être limité à l'accès HTTP/HTTPS uniquement.
  - Vérifiez les règles de filtrage de paquets pour comprendre les restrictions applicables.

---

## Graphiques et Tableaux
- **Schéma de l'infrastructure :**

![App Screenshot](https://i.ibb.co/tDJL8Xj/Virtual-Network-Infrastructure-Diagram.png)

- **Tableaux de configuration :**

**VM 1 - Passerelle (Gateway)**
| Interface | Adresse IP | Subnet Mask | DHCP Range | Accès |
|-----------|------------|-------------|------------|-------|
| LAN-1     | 192.168.42.1/26 | 255.255.255.192 | 192.168.42.40 - 192.168.42.60 | Tous ports vers LAN-2 |
| LAN-2     | 192.168.42.65/26 | 255.255.255.192 | 192.168.42.70 - 192.168.42.110 | Limité selon services |
| LAN-3     | 192.168.42.129/26 | 255.255.255.192 | 192.168.42.140 - 192.168.42.180 | HTTP/HTTPS vers LAN-2 |

**VM 2 - Serveur Web**
| Paramètre | Valeur |
|-----------|--------|
| Système d'exploitation | FreeBSD 13 |
| Adresse IP (DHCP) | 192.168.42.70 |
| Services | NGINX, PHP 7.4, MySQL |

**VM 3 & VM 4 - Clients**
| VM | Système d'exploitation | Configuration Réseau |
|----|-----------------------|----------------------|
| VM 3 (Employé) | Au choix avec GUI | DHCP |
| VM 4 (Admin) | Au choix avec GUI | DHCP |

## Support
Pour toute question ou support, veuillez ouvrir un issue dans ce dépôt GitHub.

## Contributeurs
- [Colette OSWALD](https://github.com/Leily67)
- [Lucas FIXARI](https://github.com/lfixas)