# Estudis Clínics COVID (Web Scraping)
## Descripció de l'objectiu
L'objectiu del projecte és extreure un conjunt de proves clíniques realitzades per la COVID arreu del món amb la finalitat de realitzar estudis estadístics i Data Mining .
La web [ClinicalTrials.gov](https://clinicaltrials.gov) és una base de dades d’estudis clínics finançats amb fons privats i públics realitzats a tot el món.

Alhora d'obtenir les dades realitzem un rastreig de la web. Anem recorrent els diferents elements del resultat de cerca i es desacarrega aquesta informació en un document CSV.

## Membres de l'equip
Aquesta pràctica ha estat realitzada integrament per l'alumne de la UOC Jordi Puig
## Descripció del DataSet
El Dataset descarregat conté informació de cada una de les proves clíniques realitzades per COVID i emmagatzemades en la web [ClinicalTrials.gov](https://clinicaltrials.gov)
Cada un d'aquests registres està composat per aquests camps:

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

## Representació gràfica
## Inspiració
## Codi font
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
