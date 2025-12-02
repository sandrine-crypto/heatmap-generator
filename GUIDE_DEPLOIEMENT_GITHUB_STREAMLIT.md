# 🚀 GUIDE COMPLET - DÉPLOIEMENT SUR GITHUB ET STREAMLIT CLOUD

## 🎯 Objectif

Déployer votre application Heatmaps sur **GitHub** et la rendre accessible via **Streamlit Cloud** (gratuit) pour que n'importe qui puisse l'utiliser avec un simple lien.

**Résultat final :** Une URL du type `https://votre-nom-heatmaps.streamlit.app` accessible à tous ! 🌐

---

## ⏱️ Temps Requis

- **Première fois :** 15-20 minutes
- **Mises à jour suivantes :** 2 minutes

---

## 📋 Prérequis

### Comptes nécessaires (100% gratuits)

1. **Compte GitHub** → [Créer un compte](https://github.com/signup)
2. **Compte Streamlit Cloud** → [Créer un compte](https://streamlit.io/cloud) (utilise votre compte GitHub)

### Fichiers nécessaires

✅ Tous les fichiers sont déjà créés pour vous ! Vous devez avoir :

```
📁 Votre dossier
   ├── streamlit_app.py                     ✅
   ├── heatmap_generator_generic_v2.py      ✅
   ├── requirements.txt                     ✅
   ├── README.md                            ✅
   └── .streamlit/
       └── config.toml                      ✅
```

---

## 🔥 MÉTHODE 1 : DÉPLOIEMENT COMPLET (Étape par étape)

### 🌐 PARTIE 1 : Créer le Repository GitHub

#### Étape 1.1 : Créer un nouveau repository

1. **Connectez-vous** à [GitHub](https://github.com)

2. **Cliquez** sur le **+** en haut à droite → **"New repository"**

3. **Configurez** le repository :
   ```
   Repository name  : heatmap-generator (ou le nom de votre choix)
   Description      : 🔥 Application web pour créer des heatmaps à partir d'Excel
   Public/Private   : Public (pour Streamlit Cloud gratuit)
   ✅ Add a README file : NON (on a déjà le nôtre)
   Add .gitignore   : Python
   Choose a license : MIT License
   ```

4. **Cliquez** sur **"Create repository"**

#### Étape 1.2 : Upload vos fichiers sur GitHub

**Option A : Via l'interface web (SIMPLE)**

1. Dans votre nouveau repository, cliquez sur **"Add file" → "Upload files"**

2. **Glissez-déposez** tous vos fichiers :
   - `streamlit_app.py`
   - `heatmap_generator_generic_v2.py`
   - `requirements.txt`
   - `README.md`
   - Créez un dossier `.streamlit` et uploadez `config.toml` dedans

3. **Commit message** : "Initial commit - Heatmap Generator v2.0"

4. **Cliquez** sur **"Commit changes"**

**Option B : Via Git (AVANCÉ)**

```bash
# Dans votre dossier de travail
git init
git add .
git commit -m "Initial commit - Heatmap Generator v2.0"
git branch -M main
git remote add origin https://github.com/VOTRE-USERNAME/heatmap-generator.git
git push -u origin main
```

✅ **Vos fichiers sont maintenant sur GitHub !**

---

### ☁️ PARTIE 2 : Déployer sur Streamlit Cloud

#### Étape 2.1 : Connecter Streamlit Cloud à GitHub

1. **Allez sur** [Streamlit Cloud](https://streamlit.io/cloud)

2. **Connectez-vous** avec votre compte GitHub (cliquez "Sign in with GitHub")

3. **Autorisez** Streamlit à accéder à vos repositories

#### Étape 2.2 : Créer une nouvelle application

1. **Cliquez** sur **"New app"** (bouton en haut à droite)

2. **Configurez** l'application :
   ```
   Repository    : votre-username/heatmap-generator
   Branch        : main
   Main file path: streamlit_app.py
   App URL       : votre-nom-heatmaps (personnalisez)
   ```

3. **Advanced settings** (optionnel) :
   - Python version : 3.12
   - Secrets : (laissez vide pour l'instant)

4. **Cliquez** sur **"Deploy!"**

#### Étape 2.3 : Attendre le déploiement

- ⏳ **Première fois : 2-5 minutes**
- 📊 Vous verrez les logs de déploiement en temps réel
- ✅ Quand c'est prêt : "Your app is live!" 🎉

#### Étape 2.4 : Récupérer votre URL

Votre application est maintenant accessible à :
```
https://votre-nom-heatmaps.streamlit.app
```

**🎉 FÉLICITATIONS ! Votre application est EN LIGNE !**

---

## 🔄 MÉTHODE 2 : MISES À JOUR FUTURES

### Quand vous modifiez votre code

1. **Modifiez** vos fichiers localement

2. **Uploadez** sur GitHub :
   - Via interface web : "Add file" → "Upload files"
   - Via Git : `git add . && git commit -m "Update" && git push`

3. **Streamlit Cloud** redéploie automatiquement (30 secondes) ⚡

**C'est tout !** Aucune manipulation sur Streamlit Cloud nécessaire.

---

## 📁 STRUCTURE COMPLÈTE DU REPOSITORY GITHUB

Votre repository devrait ressembler à ça :

```
heatmap-generator/
├── .streamlit/
│   └── config.toml              # Configuration Streamlit
├── exemples/                    # (Optionnel) Fichiers exemples
│   ├── Exemple_Temps.xlsx
│   ├── Exemple_Concentration.xlsx
│   └── Exemple_Dose.xlsx
├── docs/                        # (Optionnel) Documentation supplémentaire
│   ├── GUIDE_INSTALLATION.md
│   └── GUIDE_FORMAT_COLONNES.md
├── .gitignore                   # Fichiers à ignorer
├── LICENSE                      # Licence MIT
├── README.md                    # Documentation principale
├── requirements.txt             # Dépendances Python
├── streamlit_app.py            # Application Streamlit (INTERFACE)
└── heatmap_generator_generic_v2.py  # Moteur de génération
```

---

## 🎨 PERSONNALISATION

### Changer le nom de l'application

Dans `streamlit_app.py`, ligne 15 :
```python
st.set_page_config(
    page_title="Votre Titre Ici",  # ← Modifiez ici
    page_icon="🔥",
    ...
)
```

### Changer les couleurs

Dans `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#FF6B6B"      # Couleur principale (boutons)
backgroundColor = "#FFFFFF"    # Fond
secondaryBackgroundColor = "#F0F2F6"  # Fond secondaire
textColor = "#262730"         # Texte
```

**Couleurs recommandées :**
- **Rouge** : `#FF6B6B` (actuel)
- **Bleu** : `#4A90E2`
- **Vert** : `#28a745`
- **Violet** : `#9B59B6`

### Ajouter votre logo

Ajoutez un fichier `logo.png` et dans `streamlit_app.py` :
```python
st.image("logo.png", width=200)
```

---

## 🔐 SECRETS ET VARIABLES D'ENVIRONNEMENT

Si vous avez besoin de clés API ou variables secrètes :

### Dans Streamlit Cloud

1. Allez dans votre app sur Streamlit Cloud
2. Cliquez sur **"⚙️ Settings"**
3. Section **"Secrets"**
4. Ajoutez vos secrets au format TOML :
   ```toml
   API_KEY = "votre-clé-secrète"
   DATABASE_URL = "votre-url"
   ```

### Dans votre code

```python
import streamlit as st

# Accéder aux secrets
api_key = st.secrets["API_KEY"]
```

**⚠️ Important :** Ne committez JAMAIS de secrets dans Git !

---

## 🐛 DÉPANNAGE

### Erreur : "ModuleNotFoundError"

**Problème :** Une bibliothèque manque dans `requirements.txt`

**Solution :**
1. Ajoutez la bibliothèque dans `requirements.txt`
2. Commit & push
3. Streamlit redéploiera automatiquement

### Erreur : "File not found"

**Problème :** Le chemin du fichier est incorrect

**Solution :**
- Vérifiez que tous les fichiers sont bien dans le repository
- Chemins dans le code : utilisez chemins relatifs (`./fichier.py`)

### App trop lente

**Problème :** Fichier Excel trop volumineux ou calculs longs

**Solutions :**
- Ajoutez `@st.cache_data` devant les fonctions lourdes
- Limitez la taille d'upload dans `config.toml` : `maxUploadSize = 50`

### App plantée / erreur 500

**Problème :** Erreur Python dans le code

**Solution :**
1. Consultez les logs dans Streamlit Cloud : "Manage app" → "Logs"
2. Reproduisez localement : `streamlit run streamlit_app.py`
3. Corrigez l'erreur
4. Commit & push

---

## 📊 STATISTIQUES ET MONITORING

### Voir les stats d'utilisation

Dans Streamlit Cloud :
- **Analytics** : Nombre de visiteurs, sessions, pays
- **Logs** : Erreurs et activité en temps réel

### Limitations version gratuite

- **Ressources :** 1 GB RAM, 1 CPU
- **Apps :** 1 app publique
- **Uptime :** Apps inactives >7 jours sont mises en veille

**💡 Astuce :** Pour apps privées ou plus de ressources, voir Streamlit Cloud Pro (payant)

---

## 🌟 OPTIMISATIONS

### Performance

```python
# Ajouter du caching pour fonctions lourdes
@st.cache_data
def charger_donnees(fichier):
    # ... code ...
    return data

@st.cache_resource
def creer_generateur():
    # ... code ...
    return generator
```

### SEO (si app publique)

Dans `README.md`, ajoutez :
- Keywords
- Description détaillée
- Images/GIFs de démo
- Badges (Python version, license, etc.)

---

## 🔄 WORKFLOW DE DÉVELOPPEMENT

### Développement local

```bash
# 1. Créer une branche
git checkout -b feature/nouvelle-fonctionnalite

# 2. Développer et tester localement
streamlit run streamlit_app.py

# 3. Commit les changements
git add .
git commit -m "Ajouter nouvelle fonctionnalité"

# 4. Push vers GitHub
git push origin feature/nouvelle-fonctionnalite

# 5. Créer une Pull Request sur GitHub

# 6. Merger dans main
# → Streamlit Cloud redéploie automatiquement !
```

---

## 📚 RESSOURCES UTILES

### Documentation

- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Docs](https://docs.github.com/)

### Communauté

- [Forum Streamlit](https://discuss.streamlit.io/)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)
- [Discord Streamlit](https://discord.gg/streamlit)

### Tutoriels vidéo

- [Déployer sur Streamlit Cloud](https://www.youtube.com/watch?v=HKoOBiAaHGg)
- [Streamlit in 5 minutes](https://www.youtube.com/watch?v=0ESc1bh3eIg)

---

## ✅ CHECKLIST DÉPLOIEMENT

**Avant de déployer :**

- [ ] Tous les fichiers sont créés
- [ ] `requirements.txt` contient toutes les dépendances
- [ ] Code fonctionne localement (`streamlit run streamlit_app.py`)
- [ ] README.md est complet
- [ ] Pas de secrets dans le code (utiliser Streamlit secrets)

**Sur GitHub :**

- [ ] Repository créé
- [ ] Tous les fichiers uploadés
- [ ] Repository est Public

**Sur Streamlit Cloud :**

- [ ] Compte créé et connecté à GitHub
- [ ] App déployée
- [ ] URL testée et fonctionnelle
- [ ] Analytics activés (optionnel)

---

## 🎉 RÉSUMÉ

**3 étapes simples :**

1. **GitHub** : Créer repository + Upload fichiers (5 min)
2. **Streamlit Cloud** : Connecter + Déployer (5 min)
3. **Partager** : Récupérer URL et partager ! (1 min)

**Temps total : 15 minutes** ⏱️

**Résultat : Application web accessible à tous via un lien !** 🌐

---

## 💡 PROCHAINES ÉTAPES

Une fois déployé, vous pouvez :

- 📢 **Partager** le lien avec vos collègues
- 📊 **Monitorer** l'utilisation dans Streamlit Analytics
- 🔧 **Améliorer** l'app (commits auto-déploient)
- 🌟 **Promouvoir** sur réseaux sociaux / publications
- 📝 **Documenter** vos cas d'usage

---

**Besoin d'aide ?** Consultez la [documentation Streamlit](https://docs.streamlit.io/) ou posez votre question sur le [forum](https://discuss.streamlit.io/) ! 😊

---

**Bon déploiement ! 🚀**
