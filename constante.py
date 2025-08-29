LAYER_ROUTE = "troncon_de_route"

TITRE_INTERFACE = "Contribution directe BDUni (ROUTE)"
VERSION = "v1.1.1"
PLUGIN_ESPACE_CO = "ign_espace_collaboratif"

# champs
IDENTIFIANT = "id"
NATURE = "nature"
IMPORTANCE = "importance"
SENS = "sens_de_circulation"
NB_VOIES = "nombre_de_voies"
LARGEUR = "largeur_de_chaussee"
ITI_VERT = "itineraire_vert"
ACCES = "acces_vehicule_leger"

# attributs
SANS_OBJET = "Sans objet"
DOUBLE_SENS = "Double sens"
SENS_DIRECT = "Sens direct"
SENS_INVERSE = "Sens inverse"
SENS_UNIQUE = "Sens unique"


ACCES_LIBRE = "Libre"
ACCES_IMPOSSIBLE = "Physiquement impossible"
ACCES_RESTREINT = "Restreint aux ayants droit"
RTE_2_CHAUSSEES = "Route à 2 chaussées"
RTE_1_CHAUSSEE = "Route à 1 chaussée"
RTE_EMPIERREE = "Route empierrée"
ROND_POINT = "Rond-point"
CHEMIN = "Chemin"
SENTIER = "Sentier"


CLEABS = "cleabs"

FOND_DIAL = "background-color:#d3ddff"

# 0 : bouton clické → fond rose
# 1 : valeur de l'objet → fond vert
# 2 : valeur par defaut → pas de fond
# 3 : couleur fond label → fond bleu clair
# 4 : couleur fond bouton validation (orange)
# 5 : aspect pour le line edit largeur (fond rose)
# 6 : valeur interdite
CUSTOM_WIDGETS = ("background-color: #ff8080 ;font-weight: bold",
                  "background-color: #2ab51a ;font-weight: bold",
                  "background-color: None ;font-weight: bold",
                  "background-color: #cccccc",
                  "background-color: #df920d",
                  "background-color: #ff8080 ;font-weight: bold",
                  "background-color: None ;font-weight: bold"
                  )

# TEST
# 0 : pas de fond
# 1 : cliqué --> fond rose
CUSTOM_RADIOBOX = (
    """
            QRadioButton {background-color: #4CAF50;color: black;font-weight: bold}
            QRadioButton::indicator {width: 0px;height: 0px;}
            QRadioButton:checked {background-color: #ff8080;}
            }
        """,

    """ QRadioButton  {border: 2px solid #4CAF50;  
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                text-align: center;}
            QRadioButton ::indicator {width: 0px;height: 0px;}
            QRadioButton :checked {background-color: blue;}"""
)
