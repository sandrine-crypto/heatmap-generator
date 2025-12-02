# 🚀 DÉMARRAGE RAPIDE - Interface Web Streamlit

## 🎯 VOUS AVEZ 3 OPTIONS

---

## ⭐ OPTION 1 : STREAMLIT CLOUD (Recommandé)

### C'est quoi ?
**Application web accessible via URL** - Aucune installation pour les utilisateurs !

### Avantages
✅ **Gratuit** (Streamlit Community Cloud)  
✅ **Accessible partout** (juste un navigateur)  
✅ **Partageable** (envoyez le lien à vos collègues)  
✅ **Auto-déploiement** (push Git → mise à jour automatique)  

### Comment faire ? (15 minutes)

**1. Téléchargez tous les fichiers du dossier `github-streamlit/`**

**2. Suivez le guide :**
👉 [GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md](computer:///mnt/user-data/outputs/github-streamlit/GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md)

**3. Résultat :**
Votre app sera accessible à : `https://votre-nom-heatmaps.streamlit.app` 🎉

---

## 💻 OPTION 2 : LOCAL (Test rapide)

### C'est quoi ?
Application web qui tourne sur **votre ordinateur** (localhost)

### Avantages
✅ **Rapide** à tester  
✅ **Hors ligne**  
✅ **Aucune limite** de ressources  

### Comment faire ? (2 minutes)

```bash
# 1. Téléchargez tous les fichiers du dossier github-streamlit/

# 2. Installez les dépendances (une fois)
pip install -r requirements.txt

# 3. Lancez l'application
streamlit run streamlit_app.py
```

**Résultat :** L'app s'ouvre automatiquement dans votre navigateur à `http://localhost:8501` 🎉

---

## 🌐 OPTION 3 : GOOGLE COLAB (Alternative)

### C'est quoi ?
**Python dans le navigateur** - Version notebook

### Avantages
✅ **Aucune installation**  
✅ **Gratuit**  

### Comment faire ?

👉 [Test_Heatmaps_Google_Colab.ipynb](computer:///mnt/user-data/outputs/Test_Heatmaps_Google_Colab.ipynb)

---

## 📊 QUELLE OPTION CHOISIR ?

| Critère | Streamlit Cloud | Local | Colab |
|---------|-----------------|-------|-------|
| **Installation** | ❌ | ✅ pip | ❌ |
| **Accessible** | 🌐 URL publique | 💻 Localhost | 🌐 Google |
| **Partage** | ✅ Lien | ❌ | ⚠️ Notebook |
| **Interface** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Temps setup** | 15 min | 2 min | 5 min |

**Recommandation :**
- **Vous seul** → Local (rapide)
- **Équipe** → Streamlit Cloud (partage facile)
- **Pas de Python** → Colab (pas d'installation)

---

## 📁 FICHIERS NÉCESSAIRES

**Tous les fichiers sont dans :** `/mnt/user-data/outputs/github-streamlit/`

**Structure :**
```
github-streamlit/
├── streamlit_app.py                    ⭐ Application web (interface)
├── heatmap_generator_generic_v2.py     ⭐ Moteur de génération
├── requirements.txt                    ⭐ Dépendances Python
├── README.md                           📖 Documentation GitHub
├── .streamlit/
│   └── config.toml                    ⚙️ Configuration
├── .gitignore                          🔧 Fichiers à ignorer
├── LICENSE                             📄 Licence MIT
└── GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md  📚 Guide déploiement
```

**Fichiers essentiels (minimum) :**
- `streamlit_app.py`
- `heatmap_generator_generic_v2.py`
- `requirements.txt`

---

## 🚀 LANCEMENT RAPIDE LOCAL

### Windows

```cmd
REM Ouvrir CMD dans le dossier github-streamlit/
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Mac / Linux

```bash
# Ouvrir Terminal dans le dossier github-streamlit/
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Anaconda

```bash
# Ouvrir Anaconda Prompt
conda activate base  # ou votre environnement
pip install -r requirements.txt
streamlit run streamlit_app.py
```

**L'application s'ouvre automatiquement dans votre navigateur !** 🎉

---

## 📖 GUIDES COMPLETS

### Pour tester localement
1. Téléchargez le dossier `github-streamlit/`
2. Installez : `pip install -r requirements.txt`
3. Lancez : `streamlit run streamlit_app.py`

### Pour déployer sur Streamlit Cloud
👉 [GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md](computer:///mnt/user-data/outputs/github-streamlit/GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md)

### Pour comprendre l'interface
👉 [GUIDE_INTERFACE_STREAMLIT.md](computer:///mnt/user-data/outputs/GUIDE_INTERFACE_STREAMLIT.md)

---

## 🎨 APERÇU DE L'INTERFACE

```
╔════════════════════════════════════════════════╗
║ 🔥 Générateur de Heatmaps                     ║
╠════════════════════════════════════════════════╣
║ Barre latérale         │  Zone principale     ║
║ ─────────────────      │  ──────────────────  ║
║ ⚙️ Configuration       │  📤 Upload Excel     ║
║ 🎨 Palette: rouge      │  [Drag & Drop]       ║
║ ☑ Valeurs affichées    │                      ║
║ ☑ Échelle log          │  🔍 Prévisualisation ║
║                        │  ✅ Format correct   ║
║ 💡 Astuce: viridis     │                      ║
║    pour publications   │  🚀 Génération       ║
║                        │  [GÉNÉRER]           ║
║                        │                      ║
║                        │  📥 Téléchargement   ║
╚════════════════════════════════════════════════╝
```

---

## ✨ FONCTIONNALITÉS

### Interface Web
- ✅ **Upload drag & drop** Excel
- ✅ **8 palettes** de couleurs
- ✅ **Prévisualisation** automatique
- ✅ **Vérification** format colonnes
- ✅ **Téléchargement** PowerPoint en 1 clic

### Configuration
- ✅ Palette personnalisable
- ✅ Valeurs dans cellules (on/off)
- ✅ Échelle log ou linéaire
- ✅ Labels personnalisés
- ✅ Titre présentation

### Détection Automatique
- ✅ Marqueurs
- ✅ Groupes
- ✅ Réplicats
- ✅ Variable X (Temps, Dose, etc.)

---

## 🆘 PROBLÈMES ?

### L'app ne démarre pas
```bash
# Vérifiez les dépendances
pip install -r requirements.txt

# Vérifiez Streamlit
streamlit --version
```

### Port déjà utilisé
```bash
# Utilisez un autre port
streamlit run streamlit_app.py --server.port 8502
```

### Erreur "module not found"
```bash
# Vérifiez que vous êtes dans le bon dossier
ls  # Doit afficher streamlit_app.py

# Vérifiez heatmap_generator_generic_v2.py
ls heatmap_generator_generic_v2.py
```

---

## 💡 CONSEILS

### Pour tester rapidement
👉 Utilisez **Option 2 (Local)** - 2 minutes !

### Pour partager avec équipe
👉 Utilisez **Option 1 (Streamlit Cloud)** - 15 minutes setup, puis juste un lien !

### Pour démo/présentation
👉 Les deux fonctionnent, mais Streamlit Cloud est plus impressionnant (URL publique)

---

## 🎯 PROCHAINES ÉTAPES

### Maintenant
1. ✅ Choisissez votre option (Local ou Cloud)
2. ✅ Testez avec un fichier exemple
3. ✅ Partagez avec vos collègues !

### Plus tard
- 📊 Ajoutez vos propres palettes
- 🎨 Personnalisez l'interface
- 🚀 Ajoutez des fonctionnalités
- 📚 Améliorez la documentation

---

## 📞 BESOIN D'AIDE ?

### Documentation complète
- [README.md](computer:///mnt/user-data/outputs/github-streamlit/README.md) - Tout savoir sur l'app
- [GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md](computer:///mnt/user-data/outputs/github-streamlit/GUIDE_DEPLOIEMENT_GITHUB_STREAMLIT.md) - Déploiement détaillé
- [GUIDE_INTERFACE_STREAMLIT.md](computer:///mnt/user-data/outputs/GUIDE_INTERFACE_STREAMLIT.md) - Comprendre l'interface

### Ressources externes
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Forum](https://discuss.streamlit.io/)
- [GitHub Guides](https://guides.github.com/)

---

## 🎉 C'EST PARTI !

**Choix rapide :**
- 💻 **Test local** → `streamlit run streamlit_app.py`
- 🌐 **Déploiement Cloud** → Suivez le guide déploiement

**Temps total : 2-15 minutes selon option** ⏱️

---

<p align="center">
  <b>Bonne création de heatmaps ! 🔥</b>
</p>
