from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import quote
from datetime import datetime

# ==============================
# Initialisation de l'application
# ==============================

app = FastAPI(
    title="LinkedIn Jobs Finder API",
    version="2.0",
    description="API REST pour scraper ou simuler des offres d'emploi depuis LinkedIn"
)

# Autoriser les appels depuis ton frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# Classe du scraper
# ==============================

class LinkedInJobScraper:
    def __init__(self):
        self.base_url = "https://www.linkedin.com/jobs/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
        }

    def build_search_url(self, keywords, location="", remote=False, experience_level="", start=0):
        params = {
            'keywords': keywords,
            'location': location,
            'start': start
        }

        if remote:
            params['f_WT'] = '2'

        if experience_level:
            params['f_E'] = experience_level

        url = f"{self.base_url}?" + "&".join([f"{k}={quote(str(v))}" for k, v in params.items()])
        return url

    def scrape_job_listings(self, url, max_jobs=25):
        jobs = []
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            job_cards = soup.find_all("div", class_="base-card")

            for card in job_cards[:max_jobs]:
                job = self.extract_job_info(card)
                if job:
                    jobs.append(job)

            print(f"✅ {len(jobs)} offres récupérées")
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur requête: {e}")
        return jobs

    def extract_job_info(self, card):
        job = {}
        title_elem = card.find("h3", class_="base-search-card__title")
        company_elem = card.find("h4", class_="base-search-card__subtitle")
        location_elem = card.find("span", class_="job-search-card__location")
        date_elem = card.find("time")
        link_elem = card.find("a", class_="base-card__full-link")

        job["titre"] = title_elem.text.strip() if title_elem else "N/A"
        job["entreprise"] = company_elem.text.strip() if company_elem else "N/A"
        job["localisation"] = location_elem.text.strip() if location_elem else "N/A"
        job["date_publication"] = date_elem.get("datetime", datetime.now().isoformat()) if date_elem else datetime.now().isoformat()
        job["lien"] = link_elem.get("href", "#") if link_elem else "#"
        job["type"] = "Temps plein"
        job["experience"] = "Non spécifié"
        job["description"] = f"Poste de {job['titre']} chez {job['entreprise']}"

        return job

scraper = LinkedInJobScraper()

# ==============================
# Modèle de données d'entrée
# ==============================

class JobSearchParams(BaseModel):
    keywords: str = ""
    location: str = "Morocco"
    experience: str = ""
    jobType: str = ""
    remote: bool = False
    maxJobs: int = 25

# ==============================
# Routes principales
# ==============================

@app.get("/")
def home():
    return {
        "message": "Bienvenue sur l'API LinkedIn Jobs Finder (FastAPI)",
        "version": "2.0",
        "endpoints": {
            "POST /api/search": "Scraper de vraies offres LinkedIn",
            "POST /api/mock-search": "Retourne des données simulées",
            "GET /api/health": "Vérifie l'état de l'API"
        }
    }

@app.get("/api/health")
def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.post("/api/search")
def search_jobs(params: JobSearchParams):
    url = scraper.build_search_url(
        keywords=params.keywords,
        location=params.location,
        remote=params.remote,
        experience_level=params.experience
    )
    jobs = scraper.scrape_job_listings(url, params.maxJobs)
    return {
        "success": True,
        "count": len(jobs),
        "jobs": jobs,
        "search_params": params.dict()
    }

@app.post("/api/mock-search")
def mock_search(params: JobSearchParams):
    mock_jobs = [
        {
            "titre": "Data Scientist Senior",
            "entreprise": "DXC Technology",
            "localisation": "Casablanca, Maroc",
            "date_publication": "2025-10-15T10:00:00",
            "type": "Temps plein",
            "experience": "Confirmé",
            "description": "Expert Python, Machine Learning, SQL.",
            "lien": "https://www.linkedin.com/jobs/view/123456"
        },
        {
            "titre": "Stagiaire PFE DATA / IA / BI",
            "entreprise": "Deloitte",
            "localisation": "Casablanca, Maroc (Hybride)",
            "date_publication": "2025-10-14T14:30:00",
            "type": "Stage",
            "experience": "Débutant",
            "description": "Stage en Data Science, BI et IA.",
            "lien": "https://www.linkedin.com/jobs/view/123457"
        }
    ]

    filtered = [
        job for job in mock_jobs
        if params.keywords.lower() in job["titre"].lower() or params.keywords.lower() in job["entreprise"].lower()
    ]

    time.sleep(0.5)
    return {
        "success": True,
        "count": len(filtered),
        "jobs": filtered,
        "search_params": params.dict(),
        "note": "Ceci est une version mock avec des données d'exemple."
    }

# ==============================
# Lancement du serveur
# ==============================

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("🚀 API LinkedIn Jobs Finder (FastAPI)")
    print("📍 URL: http://localhost:8000")
    print("📚 Documentation: http://localhost:8000/docs")
    print("=" * 60)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
