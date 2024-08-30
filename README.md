# MatIt

`MapIt` is een eenvoudig Python-script dat locatiegegevens verwerkt en deze automatisch opent in Google Maps. Het kan zowel coördinaten (latitude/longitude) als adressen herkennen en gebruiken. Wanneer de invoer niet voldoet aan de standaardcriteria, wordt de invoer gebruikt als een zoekquery op Google Maps.

## Installatie

Om `MapIt` te installeren, kun je de volgende stappen volgen:

1. Clone de repository of download de bestanden.

   ```bash
   git clone <repository-url>
   cd mapit

2. Installeer het pakket met pip:
    ```bash
    pip install .

## Gebruik
Nadat de installatie is voltooid, kun je het script gebruiken via de command line. Voer het commando mijn_script gevolgd door de locatiegegevens in.

### Voorbeelden van Gebruik
1. Coördinaten invoeren (Latitude, Longitude)

    Voer coördinaten in het volgende formaat in:

    ```bash
    mijn_script "52.3676, 4.9041"
    ```
    Dit opent automatisch de locatie op Google Maps.

2. Adres invoeren (Straat Huisnummer, Plaats)

    Voer een adres in het volgende formaat in:

    ```bash
    mijn_script "Vriesdonk 12, Biezenmortel"
    Dit opent automatisch het ingevoerde adres op Google Maps.

3. Onbekende of Afwijkende Invoer

    Wanneer de invoer niet herkend wordt als coördinaten of adres, wordt deze als zoekquery gebruikt op Google Maps:

    ```bash
    mijn_script "Onbekende locatie"

## Functionaliteiten
**Valideer coördinaten**: Herkent geldige latitude/longitude paren en opent deze op Google Maps.

**Valideer adressen**: Herkent adressen in het formaat "Straat huisnummer, Plaats" en opent deze op Google Maps.

**Gebruik als zoekquery**: Bij niet-herkende invoer wordt de input gebruikt als zoekterm op Google Maps.

## Foutmeldingen
Indien de invoer niet voldoet aan de verwachte formaten, wordt een foutmelding weergegeven met de volgende instructies:

    Fout: Er zijn geen locatiegegevens opgegeven.
    Gebruik de volgende formaten:
    - Voor coördinaten: lat, lon (bijv. 52.3676, 4.9041)
    - Voor adres: 'Straat huisnummer, Plaats' (bijv. 'Damrak 1, Amsterdam')

## Vereisten
- Python 3.6 of hoger
- 'webbrowser' module (standaard inbegrepen in Python)

## Bijdragen
Voel je vrij om bij te dragen aan dit project door een pull request in te dienen of een issue aan te maken.

## Licentie
Dit project is gelicentieerd onder de MIT-licentie. Zie het LICENSE bestand voor meer informatie.

### Toelichting
- **Installatie-instructies**: Beschrijft hoe je het pakket installeert.
- **Gebruik**: Laat met voorbeelden zien hoe je het script kunt gebruiken met verschillende soorten invoer.
- **Functionaliteiten**: Omschrijft wat het script kan doen.
- **Foutmeldingen**: Biedt inzicht in wat er gebeurt bij onjuiste invoer.
- **Vereisten**: Vermeldt dat Python 3.6+ nodig is, en dat de `webbrowser` module gebruikt wordt.
- **Bijdragen en Licentie**: Nodigt uit tot bijdragen en vermeldt de licentie.





