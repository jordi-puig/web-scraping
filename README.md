# Practica 1 - Web scraping
## Descripció de l'objectiu
L'objectiu d'el projecte és extreure un conjunt de proves clíniques realitzades arreu del món amb la finalitat de realitzar estudis estadístics i Data Mining .
La web [ClinicalTrials.gov](https://clinicaltrials.gov/ct2/about-site/crawling) és una base de dades d’estudis clínics finançats amb fons privats i públics realitzats a tot el món.

Alhora d'obtenir les dades realitzem un rastreig de la web. Anem recorrent els diferents elements del resultat de cerca i es desacarrega aquesta informació en un document CSV.

Es realitza un control sobre els elements ja descarregats per a no repetir registres.

També realitzem un control del espaiat entre les diferents peticions que es realitan per tal de no saturar el servidor remot.

## Membres de l'equip
## Camps del DataSet
El Dataset descarregat conté els següents camps per a cada registre:
- Id: Identificador del registre (string)
- Title: Títol (string)
- Official Title: Títol oficial (string)
- Brief_Summary: Descripció curta (string)
- Detailed_Description: Descripció detallada (string) 
- Start Date: Data d'inici (date)
- Completion Date: Data de finalització (date)
- Condition/Disease: Malaltia o condició a tractar (string)
- Intervention/Treatment: Intervencions realitzades o tractaments (string)
- Study Type: Tipus d'estudi (categorical)
- Study Population: Població a estudiar (string)
- Study Groups: Grups d'estudi (string)
- Phase: Fase en la que es trova (categorical)
- Ages: Edats del participants (string)
- Sexes: Sexes dels particioants (string)
- Participants: Nombre de participants (enter) 
- Eligibility Criteria: Criteri per incloure els participants a l'estudi (string)
 

## Fitxers del codi font
## Configuració previa:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py
- pip install selenium
- pip install webdriver-manager
## Recursos
## Llicencia utilitzada
## Agraïments
