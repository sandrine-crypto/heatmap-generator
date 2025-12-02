# 🔥 Générateur de Heatmaps

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://votre-app.streamlit.app)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Application web pour créer rapidement des **heatmaps professionnelles** à partir de fichiers Excel et les exporter en PowerPoint.

![Demo](demo.gif)

---

## ✨ Fonctionnalités

- 🎨 **8 palettes de couleurs** (incluant palettes scientifiques colorblind-friendly)
- 📊 **Détection automatique** des marqueurs, groupes et réplicats
- 📤 **Upload Excel simple** (drag & drop)
- 📥 **Export PowerPoint** haute qualité
- ⚡ **Interface intuitive** (aucune ligne de code nécessaire)
- 🔬 **Conçu pour la recherche scientifique**

---

## 🚀 Démarrage Rapide

### Option 1 : Utiliser l'application en ligne (RECOMMANDÉ)

**Aucune installation nécessaire !**

👉 **[Accéder à l'application](https://votre-app.streamlit.app)** 👈

### Option 2 : Lancer localement

```bash
# Cloner le repository
git clone https://github.com/votre-username/heatmap-generator.git
cd heatmap-generator

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run streamlit_app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`

---

## 📋 Format Excel Requis

### Structure

```
Colonne A : Variable (Temps, Dose, Concentration, etc.)
Colonnes B+ : Marqueur_Groupe_Réplicat
```

### Exemple

| Temps | IL6_Control_1 | IL6_Control_2 | IL6_Treated_1 | IL6_Treated_2 |
|-------|---------------|---------------|---------------|---------------|
| 0h    | 1.2           | 1.4           | 1.3           | 1.5           |
| 2h    | 2.5           | 2.8           | 45.2          | 48.9          |
| 6h    | 3.1           | 3.4           | 89.5          | 92.1          |

### Règles de nommage

✅ **Format correct :**
```
Marqueur_Groupe_Réplicat

Exemples :
- IL6_Control_1
- TNF_Treated_2
- ProtA-WT-3      (tirets acceptés)
- Gene1.KO.1      (points acceptés)
```

❌ **Format incorrect :**
```
- IL6 Control 1   (espaces interdits)
- IL6(Control)1   (parenthèses interdites)
- IL6_Control     (manque numéro réplicat)
```

---

## 🎨 Palettes Disponibles

| Palette | Usage | Colorblind-safe |
|---------|-------|-----------------|
| `viridis` ⭐ | Publications scientifiques | ✅ |
| `cividis` | Alternative scientifique | ✅ |
| `plasma` | Présentations haute visibilité | ✅ |
| `rouge` | Classique, chaleur | ❌ |
| `bleu` | Professionnel, corporate | ❌ |
| `vert` | Nature, croissance | ❌ |
| `inferno` | Contraste élevé | ✅ |
| `magma` | Moderne | ✅ |

---

## 📖 Guide d'Utilisation

### 1. Préparer votre fichier Excel

Suivez le format décrit ci-dessus. Des fichiers d'exemple sont disponibles dans `/exemples/`.

### 2. Upload et configuration

1. **Uploadez** votre fichier Excel
2. **Configurez** les options dans la barre latérale :
   - Palette de couleurs
   - Affichage des valeurs
   - Échelle logarithmique
3. **Vérifiez** la prévisualisation automatique

### 3. Génération

1. Cliquez sur **"GÉNÉRER LES HEATMAPS"**
2. Attendez quelques secondes
3. **Téléchargez** votre PowerPoint !

---

## 📁 Structure du Projet

```
heatmap-generator/
├── streamlit_app.py              # Application Streamlit (interface web)
├── heatmap_generator_generic_v2.py  # Moteur de génération
├── requirements.txt              # Dépendances Python
├── README.md                     # Documentation
├── .streamlit/
│   └── config.toml              # Configuration Streamlit
├── exemples/
│   ├── Exemple_Temps.xlsx       # Exemple données temporelles
│   ├── Exemple_Concentration.xlsx  # Exemple dose-réponse
│   └── Exemple_Dose.xlsx        # Exemple doses traitement
└── docs/
    ├── GUIDE_INSTALLATION.md
    ├── GUIDE_FORMAT_COLONNES.md
    └── FAQ.md
```

---

## 🚀 Déploiement sur Streamlit Cloud

### Étapes (100% gratuit)

1. **Fork ce repository** sur votre compte GitHub

2. **Créez un compte** sur [Streamlit Cloud](https://streamlit.io/cloud) (gratuit)

3. **Déployez l'application :**
   - Cliquez sur "New app"
   - Sélectionnez votre repository GitHub
   - Branch : `main`
   - Main file path : `streamlit_app.py`
   - Cliquez "Deploy"

4. **Votre app est en ligne !** 🎉
   - URL : `https://votre-username-heatmap-generator.streamlit.app`
   - Partagez le lien avec vos collègues

**Temps total : 5 minutes** ⏱️

---

## 🛠️ Installation Locale (Développeurs)

### Prérequis

- Python 3.12+
- pip

### Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/heatmap-generator.git
cd heatmap-generator

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run streamlit_app.py
```

---

## 📊 Exemples

### Fichiers Excel exemples

Téléchargez les exemples dans `/exemples/` :

- **Exemple_Temps.xlsx** : Données temporelles (cytokines)
- **Exemple_Concentration.xlsx** : Courbe dose-réponse (protéines)
- **Exemple_Dose.xlsx** : Doses de traitement (gènes)

### Résultats PowerPoint

Voir `/exemples/resultats/` pour des exemples de sorties générées.

---

## ❓ FAQ

<details>
<summary><b>Pourquoi mes heatmaps ne se génèrent pas ?</b></summary>

Vérifiez que :
- Vos colonnes suivent le format `Marqueur_Groupe_Réplicat`
- Pas d'espaces ou parenthèses dans les noms
- La première colonne contient bien votre variable (Temps, Dose, etc.)
</details>

<details>
<summary><b>Puis-je utiliser d'autres séparateurs que _ ?</b></summary>

Oui ! Les séparateurs acceptés sont :
- `_` (underscore) - Recommandé
- `-` (tiret)
- `.` (point)

Exemple : `IL6-Control-1` ou `IL6.Control.1` fonctionnent aussi.
</details>

<details>
<summary><b>Quelle palette choisir pour une publication ?</b></summary>

**Recommandé : viridis** ⭐

C'est la palette la plus utilisée en science car :
- Perceptuellement uniforme
- Colorblind-friendly
- Imprimable en noir & blanc
- Acceptée par les revues scientifiques
</details>

<details>
<summary><b>Puis-je traiter plusieurs marqueurs en même temps ?</b></summary>

Oui ! Le générateur détecte automatiquement tous les marqueurs uniques dans vos colonnes et crée une heatmap pour chacun.
</details>

<details>
<summary><b>Combien de temps prend la génération ?</b></summary>

Généralement moins de 10 secondes, selon :
- Nombre de marqueurs
- Nombre de points de données
- Taille du fichier Excel
</details>

---

## 🤝 Contribution

Les contributions sont les bienvenues !

### Comment contribuer

1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

---

## 📝 Changelog

### v2.0 (Décembre 2024)
- ✨ Interface web Streamlit
- ✨ Déploiement sur Streamlit Cloud
- ✨ Upload drag & drop
- ✨ Prévisualisation automatique
- ✨ 8 palettes de couleurs
- 🐛 Correction détection format colonnes

### v1.0 (Novembre 2024)
- 🎉 Version initiale
- ⚡ Générateur Python CLI
- 📊 Support Excel et CSV
- 🎨 5 palettes de base

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Assistant IA**

- GitHub: [@votre-username](https://github.com/votre-username)
- Email: votre.email@example.com

---

## 🙏 Remerciements

- [Streamlit](https://streamlit.io/) pour le framework
- [Matplotlib](https://matplotlib.org/) pour les visualisations
- [python-pptx](https://python-pptx.readthedocs.io/) pour l'export PowerPoint
- La communauté scientifique pour les retours

---

## 📚 Documentation Complète

- [Guide d'installation détaillé](docs/GUIDE_INSTALLATION.md)
- [Format des colonnes](docs/GUIDE_FORMAT_COLONNES.md)
- [FAQ complète](docs/FAQ.md)
- [API Documentation](docs/API.md)

---

## 💡 Cas d'Usage

Ce générateur est utilisé par des chercheurs en :
- 🧬 Biologie moléculaire
- 💊 Pharmacologie
- 🔬 Immunologie
- 🧪 Biochimie
- 🌱 Biologie végétale
- 🦠 Microbiologie

---

## 🌟 Support

Si cette application vous est utile, n'oubliez pas de :
- ⭐ Mettre une étoile sur GitHub
- 📢 Partager avec vos collègues
- 💬 Donner votre feedback

---

<p align="center">
  <b>Fait avec ❤️ pour la communauté scientifique</b>
</p>
