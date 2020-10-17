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
- Id: identificador del registre (string)
- Title: titol de l'estudi (string)
- Official Title: (string)
- Description: descripció de l'estudi (string)
- Detail: descripció detallada (string) 
- Start Date: data d'inici de l'estudi (date)
- Completion Date: data d'inici de l'estudi (date)
- Condition/Disease: malaltia o condició a tractar en l'estudi (string)
- Study Type: tipus d'estudi (categorical)
- Study Population: població d'estudi (string)
- Phase: fase en la que es trova l'estudi (categorical)
- Intervention/Treatment: intervencions realitzades o tractaments (string)
- Ages: edats del participants (string)
- Sexes: sexes dels particioants (string)
- Participants: nombre de participants (enter) 
- Eligibility Criteria: criteri per incloure els participants a l'estudi (string)
 
## Configuració previa:
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- python get-pip.py
## Fitxers de el codi font
## Recursos
## Llicencia utilitzada
## Agraïments
