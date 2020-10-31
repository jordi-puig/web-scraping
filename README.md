# Estudis Clínics COVID (Web Scraping)
## Descripció de l'objectiu
L'objectiu del projecte és extreure un conjunt de proves clíniques realitzades per la COVID arreu del món amb la finalitat de realitzar estudis estadístics i Data Mining .
La web [ClinicalTrials.gov](https://clinicaltrials.gov) és una base de dades d’estudis clínics finançats amb fons privats i públics realitzats a tot el món.

Alhora d'obtenir les dades realitzem un rastreig de la web. Anem recorrent els diferents elements del resultat de cerca i es desacarrega aquesta informació en un document CSV.

## Membres de l'equip
Aquesta pràctica ha estat realitzada integrament per l'alumne de la UOC Jordi Puig
## Descripció del DataSet
El Dataset descarregat conté informació de cada una de les proves clíniques realitzades per COVID i emmagatzemades a la web [ClinicalTrials.gov](https://clinicaltrials.gov).

Cada un d'aquests registres està composat per aquests camps:

### Dades de l'estudi
- Id: Identificador del registre (string)
- Brief Title: Títol (string)
- Official Title: Títol oficial (string)
- Brief Summary: Descripció curta (string)
- Detailed Description: Descripció detallada (string)
- Study Type: Tipus d'estudi a realitzar (p.ex. COVID) (string)
- Study Phase: Fase en la que es troba l'estudi (string)
- Study Design: Disseny de l'estudi (string)
- Condition/Disease: Malaltia o condició a tractar (string)
- Intervention/Treatment: Intervencions realitzades o tractaments (string)
- Study Arms: Grups d'estudi (string)
- Start Date: Data d'inici (date)
- Completion Date: Data de finalització (date)
### Dades dels participants en l'estudi
- Estimated Enrollment: Nombre de participants (enter) 
- Eligibility Criteria: Criteri per incloure els participants a l'estudi (string)
- Sex/Gender: Sexes dels particioants (string)
- Ages: Edats del participants (string)
- Study Population: Població a estudiar (string)
- Study Groups/Cohorts: Grups d'estudi (string)
- Listed Location Countries: Països dels participants en l'estudi (string)
### Responsables / Sponsors
- Responsible Party: Responsables del projecte (string)
- Study Sponsor: Sponsors que paricipen (string)
- Collaborators: Col·laboradors de l'estudi (string)
- Investigators: Grup d'investigadors (string)
## Representació gràfica
## Inspiració
## Codi font
El codi font està format per els següents fitxers cada un amb una responsabilitat específica [SRP](https://en.wikipedia.org/wiki/Single-responsibility_principle) i amb orientació a objectes:
- main.py: és la classe principal que rep la petició i arrenca tot el procés
- scraper.py: és la classe que s'encarrega de realitzar el procés d'scraping i emmagatzemar el fitxer csv..
- browser.py: fa la navegació. Embolcalla un objecte de Selenium i realitza la navegació per les págines.
- navigator.py: a partir de la página del navegador permet anar a la següent pàgina o l'anterior.
- study_scraper.py: fa scraping d'una pàgina d'estudi.
- study.py: és l'entitat study
- data2csv.py: guarda els registes generats de l'scraping realitzat a un fitxer csv 
## Implementació
## Configuració previa:
- pip install selenium
- pip install webdriver-manager
- pip install fake-useragent
## Executar
Per executar fem el següent:
```
python main.py
```
## Extensió de la pràctica
La práctica está orientada a obtenir les dades dels estudis científics per COVID però he fet una ampliació per a recuperar qualsevol estudi científic amb un criterir de cerca.

Per a obtenir aquests registres realitzem l'execució que hem comentat en el punt previ però de la forma següent:

Per executar fem el següent:
```
python main.py cancer
```
I ens descarregarà els estudis que tenen com a keyword la paraula cancer.

Per defecte la keyword és COVID.
## Recursos
## Llicencia utilitzada
## Agraïments
