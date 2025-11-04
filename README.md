# LinkedIn Jobs Finder 💼

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.12-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Application web de recherche d'emplois LinkedIn avec scraping en temps réel et interface moderne.

## 📋 Table des Matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [API Documentation](#api-documentation)
- [Déploiement](#déploiement)
- [Structure du Projet](#structure-du-projet)
- [Technologies](#technologies)
- [Limitations](#limitations)
- [Améliorations Futures](#améliorations-futures)
- [Contribuer](#contribuer)

## 🎯 Aperçu

**LinkedIn Jobs Finder** est une application full-stack qui permet de rechercher des offres d'emploi sur LinkedIn en temps réel. Elle combine un backend Python FastAPI avec scraping web et une interface HTML/CSS/JavaScript moderne et responsive.

### Cas d'usage

- 🔍 Recherche d'emplois par mots-clés (ex: "Data Scientist", "Python Developer")
- 🌍 Filtrage par pays (Maroc, France, Canada, USA, etc.)
- 💼 Filtrage par niveau d'expérience et type d'emploi
- 🏠 Recherche d'emplois à distance
- 📊 Affichage des résultats avec détails complets

## ✨ Fonctionnalités

### Backend API (FastAPI)
- ✅ Scraping en temps réel des offres LinkedIn
- ✅ API RESTful avec endpoints `/api/search` et `/api/mock-search`
- ✅ Support CORS pour intégration frontend
- ✅ Gestion des erreurs robuste
- ✅ Mode mock avec données d'exemple

### Frontend (HTML/CSS/JS)
- ✅ Interface moderne type réseau social
- ✅ Design responsive (mobile-friendly)
- ✅ Filtres avancés (pays, expérience, type d'emploi)
- ✅ Affichage en temps réel des résultats
- ✅ Dates relatives (Il y a X jours)
- ✅ Liens directs vers les offres LinkedIn

### Scraping
- ✅ Extraction de titres, entreprises, localisations
- ✅ Dates de publication
- ✅ Liens vers les offres originales
- ✅ User-Agent personnalisé pour éviter les blocages

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                              │
│                  user_interface.html                             │
│         HTML5 + CSS3 + Vanilla JavaScript                        │
└─────────────────────┬───────────────────────────────────────────┘
                      │ HTTP REST API
                      │ (POST /api/search)
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                   BACKEND API (FastAPI)                          │
│                        main.py                                   │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐   │
│  │         FastAPI Application                            │   │
│  │  • CORS Middleware                                     │   │
│  │  • POST /api/search                                    │   │
│  │  • POST /api/mock-search                               │   │
│  │  • GET /api/health                                     │   │
│  └────────────────────┬───────────────────────────────────┘   │
│                       │                                          │
│  ┌────────────────────▼───────────────────────────────────┐   │
│  │      LinkedInJobScraper Class                          │   │
│  │  • build_search_url()                                  │   │
│  │  • scrape_job_listings()                               │   │
│  │  • extract_job_info()                                  │   │
│  └────────────────────┬───────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────┘
                        │ HTTP GET Requests
                        │ (BeautifulSoup + Requests)
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LinkedIn Jobs Search                           │
│              https://www.linkedin.com/jobs/search                │
└─────────────────────────────────────────────────────────────────┘
```

### Flux de Données

1. **Utilisateur** → Saisit critères de recherche dans l'interface
2. **Frontend** → Envoie requête POST à `/api/search`
3. **Backend** → Construit l'URL LinkedIn avec paramètres
4. **Scraper** → Envoie requête HTTP à LinkedIn
5. **Parser** → Extrait données avec BeautifulSoup
6. **API** → Retourne JSON au frontend
7. **Frontend** → Affiche les offres d'emploi

## 📦 Prérequis

### Logiciels Requis

```bash
Python 3.8 ou supérieur
pip (gestionnaire de packages Python)
```

### Navigateur Web
- Chrome, Firefox, Safari, ou Edge (version récente)

## 🔧 Installation

### 1. Cloner le Repository

```bash
git clone https://github.com/ahmed-elmahdaoui/linkedin-jobs-finder.git
cd linkedin-jobs-finder
```

### 2. Créer un Environnement Virtuel (Recommandé)

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les Dépendances

```bash
pip install -r requirements.txt
```

**Contenu de `requirements.txt`** :
```
fastapi
uvicorn
pydantic
beautifulsoup4
requests
```

### 4. Vérifier l'Installation

```bash
python main.py
```

Vous devriez voir :
```
============================================================
🚀 API LinkedIn Jobs Finder (FastAPI)
📍 URL: http://localhost:8000
📚 Documentation: http://localhost:8000/docs
============================================================
INFO:     Started server process [12345]
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## ⚙️ Configuration

### Variables d'Environnement

Le serveur utilise le port `8000` par défaut. Pour changer :

```bash
export PORT=5000  # Linux/Mac
set PORT=5000     # Windows
```

Ou modifiez directement dans `main.py` :

```python
if __name__ == "__main__":
    port = 8000  # Changez cette valeur
    uvicorn.run("main:app", host="0.0.0.0", port=port)
```

### Configuration CORS

Pour autoriser d'autres domaines, modifiez dans `main.py` :

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://votre-domaine.com"],  # Spécifiez vos domaines
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Configuration du Scraper

Personnalisez les headers HTTP dans la classe `LinkedInJobScraper` :

```python
self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml',
}
```

## 🚀 Utilisation

### Démarrer le Backend

```bash
python main.py
```

Le serveur démarre sur `http://localhost:8000`

### Ouvrir le Frontend

#### Option 1 : Fichier local (Simple)
```bash
# Ouvrez directement dans le navigateur
open user_interface.html  # Mac
xdg-open user_interface.html  # Linux
start user_interface.html  # Windows
```

#### Option 2 : Serveur HTTP local (Recommandé)
```bash
# Python 3
python -m http.server 3000

# Ou avec un serveur Node.js
npx http-server -p 3000
```

Accédez à `http://localhost:3000/user_interface.html`

### Effectuer une Recherche

1. **Saisir des mots-clés** : Ex: "Data Scientist", "Python Developer"
2. **Cliquer sur le bouton Filtres** (optionnel)
3. **Sélectionner les critères** :
   - Pays : Maroc, France, Canada, etc.
   - Niveau d'expérience : Débutant, Confirmé, etc.
   - Type d'emploi : Temps plein, Stage, etc.
   - Emploi à distance : Cocher si souhaité
4. **Cliquer sur "Rechercher"**
5. **Consulter les résultats**

### Exemples de Recherche

```javascript
// Recherche simple
Mots-clés: "Data Scientist"
Pays: Morocco
→ Résultats: Offres Data Scientist au Maroc

// Recherche avancée
Mots-clés: "Python Developer"
Pays: France
Niveau: Confirmé
Type: Temps plein
Remote: ✓
→ Résultats: Postes Python Senior à distance en France
```

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```http
GET /api/health
```

**Réponse** :
```json
{
  "status": "ok",
  "timestamp": "2025-11-03T10:30:00"
}
```

#### 2. Search Jobs (Réel)
```http
POST /api/search
Content-Type: application/json
```

**Body** :
```json
{
  "keywords": "Data Scientist",
  "location": "Morocco",
  "experience": "2",
  "jobType": "full-time",
  "remote": false,
  "maxJobs": 25
}
```

**Paramètres** :
- `keywords` (string) : Mots-clés de recherche
- `location` (string) : Pays ou ville
- `experience` (string) : Niveau ("1"=Débutant, "2"=Intermédiaire, "3"=Confirmé, "4"=Directeur, "5"=Exécutif)
- `jobType` (string) : Type d'emploi ("full-time", "part-time", "contract", "internship")
- `remote` (boolean) : Emplois à distance uniquement
- `maxJobs` (int) : Nombre maximum de résultats (défaut: 25)

**Réponse** :
```json
{
  "success": true,
  "count": 5,
  "jobs": [
    {
      "titre": "Data Scientist Senior",
      "entreprise": "DXC Technology",
      "localisation": "Casablanca, Maroc",
      "date_publication": "2025-10-15T10:00:00",
      "type": "Temps plein",
      "experience": "Confirmé",
      "description": "Poste de Data Scientist Senior chez DXC Technology",
      "lien": "https://www.linkedin.com/jobs/view/123456"
    }
  ],
  "search_params": {
    "keywords": "Data Scientist",
    "location": "Morocco",
    ...
  }
}
```

#### 3. Mock Search (Données test)
```http
POST /api/mock-search
Content-Type: application/json
```

**Body** : Identique à `/api/search`

**Réponse** : Retourne des données d'exemple pré-définies

### Exemples avec cURL

```bash
# Health check
curl http://localhost:8000/api/health

# Recherche réelle
curl -X POST http://localhost:8000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "keywords": "Python Developer",
    "location": "France",
    "remote": true,
    "maxJobs": 10
  }'

# Recherche mock
curl -X POST http://localhost:8000/api/mock-search \
  -H "Content-Type: application/json" \
  -d '{"keywords": "Data Scientist", "location": "Morocco"}'
```

### Documentation Interactive

FastAPI génère automatiquement une documentation interactive :

```
http://localhost:8000/docs      # Swagger UI
http://localhost:8000/redoc     # ReDoc
```

## 🌐 Déploiement

### Déploiement sur Render

#### ⚠️ ERREUR CRITIQUE DANS `render.yaml`

**Problème** : Typo dans la commande de démarrage
```yaml
startCommand: "ptyhon main.py"  # ❌ ERREUR : "ptyhon" au lieu de "python"
```

**Solution** :
```yaml
startCommand: "python main.py"  # ✅ CORRECT
```

#### Configuration Render

**Fichier `render.yaml` corrigé** :
```yaml
services:
  - type: web
    name: jobs-finder-api
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python main.py"
    autoDeploy: true
```

#### Étapes de Déploiement

1. **Créer un compte sur [Render](https://render.com/)**

2. **Connecter votre Repository GitHub**

3. **Créer un nouveau Web Service**
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

4. **Variables d'Environnement (Optionnel)**
   ```
   PORT=10000
   PYTHON_VERSION=3.11.0
   ```

5. **Déployer**
   - Render détecte automatiquement `render.yaml`
   - Build et déploiement automatiques

6. **Obtenir l'URL de production**
   ```
   https://jobs-finder-api.onrender.com
   ```

7. **Mettre à jour le Frontend**
   
   Dans `user_interface.html`, changez l'URL de l'API :
   ```javascript
   // Développement
   const API_URL = 'http://localhost:8000';
   
   // Production
   const API_URL = 'https://jobs-finder-api.onrender.com';
   
   // Fonction de recherche
   async function searchJobs() {
       const response = await fetch(`${API_URL}/api/search`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify(params)
       });
   }
   ```

### Déploiement sur Heroku

```bash
# Installer Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Créer app
heroku create linkedin-jobs-finder

# Ajouter Procfile
echo "web: python main.py" > Procfile

# Push et déployer
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Ouvrir l'app
heroku open
```

### Déploiement Docker (Optionnel)

**Dockerfile** :
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

**Commandes** :
```bash
# Build
docker build -t linkedin-jobs-finder .

# Run
docker run -p 8000:8000 linkedin-jobs-finder
```

## 📁 Structure du Projet

```
linkedin-jobs-finder/
├── main.py                    # Backend FastAPI avec scraper
├── user_interface.html        # Frontend (Single Page App)
├── requirements.txt           # Dépendances Python
├── render.yaml                # Configuration Render (⚠️ corrigez la typo!)
├── Procfile                   # Configuration Heroku (optionnel)
├── Dockerfile                 # Configuration Docker (optionnel)
├── .gitignore                 # Fichiers à ignorer
└── README.md                  # Documentation
```

### Détails des Fichiers

#### `main.py`
```python
# Composants principaux
- FastAPI app avec CORS
- LinkedInJobScraper class
  ├── build_search_url()
  ├── scrape_job_listings()
  └── extract_job_info()
- Routes:
  ├── GET /
  ├── GET /api/health
  ├── POST /api/search
  └── POST /api/mock-search
```

#### `user_interface.html`
```html
<!-- Structure -->
- Header (Logo + Titre + Barre de recherche)
- Filtres (Pays, Expérience, Type, Remote)
- Zone de résultats (Job cards dynamiques)
- Footer
- JavaScript:
  ├── searchJobs()
  ├── displayJobs()
  ├── formatDate()
  └── toggleFilters()
```

## 🛠️ Technologies

### Backend
- **Python 3.8+** : Langage de programmation
- **FastAPI** : Framework web moderne et rapide
- **Uvicorn** : Serveur ASGI
- **Pydantic** : Validation de données
- **BeautifulSoup4** : Parsing HTML
- **Requests** : Client HTTP

### Frontend
- **HTML5** : Structure
- **CSS3** : Styles modernes (gradients, shadows, animations)
- **JavaScript (Vanilla)** : Logique client
- **Lucide Icons** : Bibliothèque d'icônes SVG

### Outils
- **Render / Heroku** : Hébergement cloud
- **Docker** : Containerisation (optionnel)
- **Git** : Contrôle de version

## ⚠️ Limitations

### Scraping LinkedIn
1. **Rate Limiting** : LinkedIn peut bloquer les requêtes excessives
2. **Captcha** : Risque de déclenchement avec trop de requêtes
3. **Structure HTML changeante** : Les sélecteurs CSS peuvent devenir obsolètes
4. **Données incomplètes** : Certaines informations peuvent manquer

### Solutions
- Implémenter un cache pour réduire les requêtes
- Ajouter des délais entre les requêtes
- Utiliser un système de rotation de User-Agents
- Envisager l'API officielle LinkedIn (payante)

### Restrictions Techniques
- Pas d'authentification LinkedIn (accès limité aux offres publiques)
- Pas de sauvegarde des résultats (pas de base de données)
- Scraping bloqué si IP bannie

## 🔒 Considérations Légales

⚠️ **Important** : Le scraping de LinkedIn peut violer leurs conditions d'utilisation. Ce projet est à des fins éducatives uniquement.

**Alternatives légales** :
1. **LinkedIn API officielle** : https://www.linkedin.com/developers/
2. **Adzuna API** : https://www.adzuna.com/
3. **Indeed API** : https://www.indeed.com/publisher
4. **GitHub Jobs API** : https://jobs.github.com/api

## 🚀 Améliorations Futures

### Fonctionnalités
- [ ] Authentification utilisateur (comptes)
- [ ] Sauvegarde des recherches favorites
- [ ] Notifications par email pour nouvelles offres
- [ ] Export des résultats (CSV, PDF)
- [ ] Graphiques de tendances d'emploi
- [ ] Suggestions intelligentes de mots-clés
- [ ] Mode sombre (dark mode)

### Technique
- [ ] Cache Redis pour performances
- [ ] Base de données PostgreSQL pour historique
- [ ] Tests unitaires et d'intégration
- [ ] CI/CD avec GitHub Actions
- [ ] Rate limiting côté serveur
- [ ] Système de pagination
- [ ] WebSockets pour mises à jour en temps réel
- [ ] Compression GZIP des réponses

### UX/UI
- [ ] Animations de chargement sophistiquées
- [ ] Filtres sauvegardés dans localStorage
- [ ] Raccourcis clavier
- [ ] Mode comparaison d'offres
- [ ] Partage d'offres sur réseaux sociaux

## 🐛 Problèmes Connus

### 1. Typo dans `render.yaml`

**Erreur** :
```yaml
startCommand: "ptyhon main.py"  # ❌ Typo
```

**Solution** :
```yaml
startCommand: "python main.py"  # ✅ Corrigé
```

### 2. CORS en Production

Si le frontend est hébergé sur un autre domaine, ajoutez-le :

```python
allow_origins=["https://votre-frontend.com"]
```

### 3. Port Dynamique (Render/Heroku)

Assurez-vous que le code lit la variable `PORT` :

```python
port = int(os.environ.get("PORT", 8000))
```

### 4. LinkedIn Peut Bloquer

Si vous obtenez des erreurs 429 (Too Many Requests) :
- Réduisez le nombre de requêtes
- Ajoutez des délais (`time.sleep()`)
- Utilisez un proxy ou VPN

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment participer :

### 1. Fork le Projet
```bash
git clone https://github.com/votre-username/linkedin-jobs-finder.git
```

### 2. Créer une Branche
```bash
git checkout -b feature/SuperFeature
```

### 3. Commit vos Changements
```bash
git commit -m 'Add SuperFeature'
```

### 4. Push vers la Branche
```bash
git push origin feature/SuperFeature
```

### 5. Ouvrir une Pull Request

### Guidelines
- Suivez les conventions Python (PEP 8)
- Ajoutez des docstrings aux fonctions
- Testez vos modifications
- Mettez à jour la documentation

## 📄 License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2025 [Votre Nom]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

## 👥 Auteurs

**Ahmed EL MAHDAOUI**
- GitHub: https://github.com/ahmed-elmahdaoui.
- LinkedIn: https://www.linkedin.com/in/ahmed-el-mahdaoui-00bab9282
- Email: ahmed.elmahdawi@usmba.ac.ma

## 🙏 Remerciements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [LinkedIn](https://www.linkedin.com/) pour la plateforme d'emplois
- [Render](https://render.com/) pour l'hébergement gratuit
- La communauté Python open source

## 📚 Ressources Utiles

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Web Scraping with Python](https://realpython.com/beautiful-soup-web-scraper-python/)
- [REST API Best Practices](https://restfulapi.net/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Python Requests Documentation](https://requests.readthedocs.io/)

## 📞 Support

Si vous rencontrez des problèmes :

1. Consultez la [section Problèmes Connus](#problèmes-connus)
2. Ouvrez une [Issue](https://github.com/votre-username/linkedin-jobs-finder/issues)
3. Rejoignez notre [Discord](https://discord.gg/votre-serveur) (optionnel)

---

⭐ **Si ce projet vous aide dans votre recherche d'emploi, n'hésitez pas à lui donner une étoile !**

💼 **Bonne chance dans votre recherche d'opportunités professionnelles !**

Made with ❤️ and 🐍 by [Ahmed EL MAHDAOUI]
