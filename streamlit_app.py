"""
🔥 GÉNÉRATEUR DE HEATMAPS - Interface Web
Application Streamlit pour créer des heatmaps à partir de fichiers Excel

Auteur: Assistant IA
Version: 2.0
"""

import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
import sys

# Configuration de la page
st.set_page_config(
    page_title="Générateur de Heatmaps",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF5252;
    }
</style>
""", unsafe_allow_html=True)

# Importer le générateur de heatmaps
try:
    from heatmap_generator_generic_v2 import HeatmapGenerator
except ImportError:
    st.error("⚠️ Erreur : Le module heatmap_generator_generic_v2.py est introuvable. Assurez-vous qu'il est dans le même dossier.")
    st.stop()

# Titre principal
st.markdown('<div class="main-header">🔥 Générateur de Heatmaps</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transformez vos données Excel en heatmaps PowerPoint professionnelles</div>', unsafe_allow_html=True)

# Barre latérale - Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Palette de couleurs
    st.subheader("🎨 Palette de couleurs")
    palette = st.selectbox(
        "Choisissez une palette :",
        options=['rouge', 'bleu', 'vert', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'],
        index=0,
        help="Viridis et cividis sont recommandés pour les publications scientifiques (colorblind-friendly)"
    )
    
    # Aperçu palette
    palette_colors = {
        'rouge': '🔴🟠🟡',
        'bleu': '🔵💙🔷',
        'vert': '🟢💚🌲',
        'viridis': '🟣🔵🟢🟡',
        'plasma': '🔷🟣🩷🟠🟡',
        'inferno': '⚫🟣🟠🟡',
        'magma': '⚫🟣🟠⚪',
        'cividis': '🔵⚫🟡'
    }
    st.caption(f"Aperçu : {palette_colors.get(palette, '🎨')}")
    
    st.divider()
    
    # Options d'affichage
    st.subheader("📊 Options d'affichage")
    afficher_valeurs = st.checkbox("Afficher les valeurs dans les cellules", value=True)
    echelle_log = st.checkbox("Utiliser échelle logarithmique", value=True, 
                              help="Recommandé pour des données avec large plage de valeurs")
    
    st.divider()
    
    # Configuration avancée
    with st.expander("🔧 Configuration avancée"):
        colonne_x = st.text_input("Nom colonne X (laisser vide = auto)", value="", 
                                  help="Laissez vide pour détection automatique")
        label_axe_x = st.text_input("Label axe X personnalisé", value="",
                                    help="Ex: 'Temps (heures)' ou 'Concentration (ng/mL)'")
        max_heatmaps = st.slider("Heatmaps max par slide", min_value=1, max_value=9, value=6)
        titre_pres = st.text_input("Titre présentation", value="Analyse des résultats expérimentaux")
    
    st.divider()
    
    # Info
    st.info("💡 **Astuce** : Utilisez la palette 'viridis' pour les publications scientifiques !")

# Zone principale
tab1, tab2, tab3 = st.tabs(["📤 Upload & Génération", "📖 Guide d'utilisation", "ℹ️ À propos"])

with tab1:
    st.header("📤 Étape 1 : Uploadez votre fichier Excel")
    
    # Upload fichier
    uploaded_file = st.file_uploader(
        "Glissez-déposez votre fichier Excel ici ou cliquez pour parcourir",
        type=['xlsx', 'xls'],
        help="Format requis : Colonne A = variable (Temps, Dose, etc.), Colonnes B+ = Marqueur_Groupe_Réplicat"
    )
    
    if uploaded_file is not None:
        # Sauvegarder temporairement le fichier
        temp_file_path = f"temp_{uploaded_file.name}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ Fichier uploadé : {uploaded_file.name}")
        
        # Prévisualisation des données
        st.header("🔍 Étape 2 : Prévisualisation")
        
        try:
            # Lire le fichier
            try:
                df = pd.read_excel(temp_file_path, sheet_name='Données')
            except:
                df = pd.read_excel(temp_file_path, sheet_name=0)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Nombre de lignes", df.shape[0])
                st.metric("Nombre de colonnes", df.shape[1])
            
            with col2:
                # Détecter marqueurs
                colonnes_donnees = [col for col in df.columns if col != df.columns[0]]
                marqueurs = set()
                for col in colonnes_donnees:
                    for sep in ['_', '-', '.']:
                        if sep in col:
                            marqueurs.add(col.split(sep)[0])
                            break
                
                st.metric("Marqueurs détectés", len(marqueurs))
                if marqueurs:
                    st.caption(f"Marqueurs : {', '.join(sorted(marqueurs))}")
            
            # Afficher aperçu
            with st.expander("👁️ Voir les premières lignes"):
                st.dataframe(df.head(10), use_container_width=True)
            
            # Vérification du format
            st.subheader("✅ Vérification du format")
            
            format_ok = True
            messages = []
            
            # Vérifier séparateurs
            has_separator = False
            for col in colonnes_donnees[:5]:  # Vérifier les 5 premières
                if '_' in col or '-' in col or '.' in col:
                    has_separator = True
                    break
            
            if has_separator:
                st.success("✅ Format détecté : Colonnes avec séparateurs (_/-/.)")
            else:
                st.warning("⚠️ Attention : Aucun séparateur détecté dans les noms de colonnes")
                st.caption("Format attendu : Marqueur_Groupe_Réplicat")
                format_ok = False
            
            # Vérifier espaces et parenthèses
            problematic_cols = []
            for col in colonnes_donnees:
                if ' ' in col or '(' in col or ')' in col:
                    problematic_cols.append(col)
            
            if problematic_cols:
                st.warning(f"⚠️ {len(problematic_cols)} colonnes avec espaces/parenthèses détectées")
                with st.expander("Voir les colonnes problématiques"):
                    for col in problematic_cols[:10]:
                        st.text(f"• {col}")
                    if len(problematic_cols) > 10:
                        st.caption(f"... et {len(problematic_cols) - 10} autres")
                format_ok = False
            
            if format_ok:
                st.markdown('<div class="success-box">✅ <b>Format correct !</b> Prêt à générer les heatmaps.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="warning-box">⚠️ <b>Format à corriger.</b> Consultez le guide ci-dessous.</div>', unsafe_allow_html=True)
            
            # Bouton de génération
            st.header("🚀 Étape 3 : Génération")
            
            if st.button("🔥 GÉNÉRER LES HEATMAPS", type="primary"):
                with st.spinner("🔄 Génération en cours... Veuillez patienter."):
                    try:
                        # Configuration
                        config = {
                            'colonne_x': colonne_x if colonne_x else None,
                            'label_axe_x': label_axe_x if label_axe_x else None,
                            'echelle_log': echelle_log,
                            'max_heatmaps_par_slide': max_heatmaps,
                            'titre_presentation': titre_pres
                        }
                        
                        # Créer générateur
                        generator = HeatmapGenerator(temp_file_path, config)
                        
                        # Afficher progression
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Charger données
                        status_text.text("📊 Chargement des données...")
                        progress_bar.progress(20)
                        generator.charger_donnees()
                        
                        # Calculer matrices
                        status_text.text("🧮 Calcul des matrices...")
                        progress_bar.progress(50)
                        generator.calculer_matrices()
                        
                        # Créer présentation
                        status_text.text("🎨 Création des heatmaps...")
                        progress_bar.progress(75)
                        output_file = "Heatmaps_Generated.pptx"
                        generator.creer_presentation(output_file, 
                                                    afficher_valeurs=afficher_valeurs,
                                                    palette=palette)
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Terminé !")
                        
                        # Succès
                        st.balloons()
                        st.success("🎉 **PowerPoint créé avec succès !**")
                        
                        # Statistiques
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Marqueurs", len(generator.marqueurs))
                        with col2:
                            st.metric("Groupes", len(generator.groupes))
                        with col3:
                            st.metric("Points mesurés", len(generator.valeurs_x))
                        
                        # Bouton de téléchargement
                        with open(output_file, "rb") as file:
                            st.download_button(
                                label="📥 TÉLÉCHARGER LE POWERPOINT",
                                data=file,
                                file_name=f"Heatmaps_{uploaded_file.name.split('.')[0]}.pptx",
                                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                            )
                        
                        st.info("💡 Le fichier PowerPoint contient toutes vos heatmaps. Ouvrez-le dans PowerPoint ou Google Slides !")
                        
                    except Exception as e:
                        st.error(f"❌ Erreur lors de la génération : {str(e)}")
                        st.exception(e)
        
        except Exception as e:
            st.error(f"❌ Erreur lors de la lecture du fichier : {str(e)}")
            st.exception(e)
    
    else:
        # Instructions si pas de fichier
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **📋 Format Excel requis :**
        
        - **Colonne A** : Variable (Temps, Dose, Concentration, etc.)
        - **Colonnes B+** : Format `Marqueur_Groupe_Réplicat`
        
        **Exemple :**
        ```
        Temps | IL6_Control_1 | IL6_Control_2 | IL6_Treated_1 | IL6_Treated_2
        ──────┼───────────────┼───────────────┼───────────────┼───────────────
        0h    |     1.2       |     1.4       |     1.3       |     1.5
        2h    |     2.5       |     2.8       |    45.2       |    48.9
        ```
        
        **Séparateurs acceptés :** `_` (underscore), `-` (tiret), `.` (point)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.header("📖 Guide d'utilisation")
    
    st.subheader("🎯 En 3 étapes simples")
    
    st.markdown("""
    ### 1️⃣ Préparez votre fichier Excel
    
    **Format requis :**
    - **Première colonne** : Variable mesurée (Temps, Dose, Concentration, Passage, etc.)
    - **Autres colonnes** : Format `Marqueur_Groupe_Réplicat`
    
    **✅ Exemples valides :**
    ```
    IL6_Control_1       ← Marqueur: IL6, Groupe: Control, Réplicat: 1
    TNF_Treated_2       ← Marqueur: TNF, Groupe: Treated, Réplicat: 2
    ProtA-WT-3          ← Tirets acceptés aussi
    Gene1.KO.1          ← Points acceptés aussi
    ```
    
    **❌ Exemples invalides :**
    ```
    IL6 Control 1       ← Espaces interdits
    IL6(Control)1       ← Parenthèses interdites
    IL6_Control         ← Manque numéro réplicat
    ```
    
    ---
    
    ### 2️⃣ Configurez les options
    
    Dans la barre latérale :
    - **Palette** : Choisissez la couleur (viridis recommandé pour publications)
    - **Valeurs** : Cochez pour afficher les nombres dans les cellules
    - **Échelle log** : Recommandé si large plage de valeurs
    
    ---
    
    ### 3️⃣ Générez et téléchargez
    
    - Cliquez sur **"GÉNÉRER LES HEATMAPS"**
    - Attendez quelques secondes
    - Téléchargez votre PowerPoint !
    """)
    
    st.divider()
    
    st.subheader("🔧 Format des colonnes en détail")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Structure :**
        ```
        Marqueur_Groupe_Réplicat
        ```
        
        **Où :**
        - `Marqueur` = Ce que vous mesurez
        - `Groupe` = Condition expérimentale
        - `Réplicat` = Numéro (1, 2, 3...)
        """)
    
    with col2:
        st.markdown("""
        **Exemples concrets :**
        - Cytokines : `IL6_Control_1`
        - Protéines : `ProtA_WT_2`
        - Gènes : `Gene1_KO_3`
        - Doses : `Marker_Dose50_1`
        """)
    
    st.divider()
    
    st.subheader("❓ Problèmes fréquents")
    
    with st.expander("❌ Erreur : Colonnes avec espaces/parenthèses"):
        st.markdown("""
        **Problème :** Votre fichier contient des noms comme `"IL6 Control 1"` ou `"Treatment (10mg) 2"`
        
        **Solution :** Renommez en format correct :
        - `"IL6 Control 1"` → `"IL6_Control_1"`
        - `"Treatment (10mg) 2"` → `"Treatment10_2"`
        
        **Astuce Excel :** Utilisez Trouver/Remplacer
        - Remplacez ` ` (espace) par `_`
        - Supprimez `(` et `)`
        """)
    
    with st.expander("❌ Erreur : Aucun marqueur détecté"):
        st.markdown("""
        **Problème :** Les colonnes n'ont pas de séparateur ou format incorrect
        
        **Solution :** Vérifiez que toutes les colonnes (sauf la première) suivent le format :
        - `Marqueur_Groupe_Réplicat`
        - Avec un séparateur : `_` ou `-` ou `.`
        """)
    
    with st.expander("💡 Comment choisir la palette ?"):
        st.markdown("""
        **Pour publications scientifiques :**
        - `viridis` ⭐ (meilleur choix, colorblind-friendly)
        - `cividis` (alternative colorblind-friendly)
        
        **Pour présentations :**
        - `plasma` (contraste élevé)
        - `rouge` (classique)
        
        **Pour rapports internes :**
        - `bleu` (professionnel)
        - `vert` (neutre)
        """)

with tab3:
    st.header("ℹ️ À propos")
    
    st.markdown("""
    ### 🔥 Générateur de Heatmaps v2.0
    
    Application web pour créer rapidement des heatmaps professionnelles à partir de données Excel.
    
    **Fonctionnalités :**
    - ✅ Upload Excel simple (drag & drop)
    - ✅ Détection automatique des marqueurs et groupes
    - ✅ 8 palettes de couleurs
    - ✅ Export PowerPoint haute qualité
    - ✅ Interface intuitive
    - ✅ 100% gratuit et open-source
    
    **Technologies :**
    - Python 3.12+
    - Streamlit
    - Pandas, NumPy, Matplotlib
    - python-pptx
    
    **Auteur :** Assistant IA  
    **Version :** 2.0  
    **Licence :** MIT
    
    ---
    
    ### 📚 Ressources
    
    - [Documentation complète](https://github.com)
    - [Exemples de fichiers](https://github.com)
    - [Signaler un bug](https://github.com/issues)
    
    ---
    
    ### 💡 Besoin d'aide ?
    
    Si vous rencontrez un problème :
    1. Consultez le **Guide d'utilisation**
    2. Vérifiez le **format de vos colonnes**
    3. Téléchargez un **fichier d'exemple**
    """)
    
    st.divider()
    
    st.info("🌟 Si cette application vous est utile, partagez-la avec vos collègues !")

# Footer
st.divider()
st.caption("© 2024 Générateur de Heatmaps | Fait avec ❤️ et Streamlit")
