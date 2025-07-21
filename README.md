# Product Scraper

Ce projet Python permet de récupérer automatiquement le **nom d’un produit** et son **image** à partir de son code EAN/UPC en utilisant le site [BarcodeLookup](https://www.barcodelookup.com).

>  Utilise `Selenium`, `ChromeDriver` et `BeautifulSoup` pour automatiser la récupération des données.

---

## 🚀 Fonctionnalités

- Scraping du **nom du produit**
- Scraping de l’**URL de l’image** du produit
- Mode **headless** (sans ouvrir de fenêtre de navigateur)
- Compatible avec les codes **EAN** ou **UPC**

---

## 📁 Structure du projet

```
.
├── scraper.py        # Script principal de scraping
├── requirements.txt  # Dépendances Python
└── README.md         # Documentation
```

---

## 🛠️ Prérequis

- Python 3.7+
- Google Chrome installé sur la machine

---

##  Installation

1. **Cloner le dépôt GitHub** :
   ```bash
   git clone https://github.com/ton-nom-utilisateur/barcode-scraper.git
   cd barcode-scraper
   ```

2. **Créer un environnement virtuel (optionnel mais recommandé)** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

---

##  Utilisation

1. Exécute le script en ligne de commande avec un code EAN ou UPC :

   ```bash
   python scraper.py 3017620425035
   ```

2. Résultat attendu (exemple) :
   ```json
   {
     "title": "Nutella Hazelnut Spread with Cocoa",
     "image_url": "https://images.barcodelookup.com/123456789.jpg"
   }
   ```

---

## 💡 Remarques

- L’utilisation excessive de scraping peut entraîner un blocage temporaire par le site.
- Le scraping de données doit respecter les [conditions d'utilisation du site](https://www.barcodelookup.com/terms).

---

## 🔧 Dépannage

- Si ChromeDriver échoue :
  - Vérifie que Google Chrome est bien installé.
  - Assure-toi que `webdriver-manager` est à jour :
    ```bash
    pip install -U webdriver-manager
    ```

- Pour voir les erreurs en détail, lance le script sans l’option `--headless` en modifiant cette ligne :
  ```python
  options.add_argument("--headless=new")  # <-- supprimer ou commenter
  ```

---

## 📜 Licence

Ce projet est open-source sous licence MIT. Voir [LICENSE](LICENSE) pour plus d'informations.

---

##  Contribuer

Les contributions sont les bienvenues ! Tu peux :

- Créer une issue pour signaler un bug
- Faire une pull request avec des améliorations
