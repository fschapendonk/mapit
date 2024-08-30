import argparse
import sys
import webbrowser

def is_float(value):
    """Controleer of een waarde kan worden geconverteerd naar een float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_lat_lon(input_data):
    """Controleer of de input bestaat uit geldige lat/lon coördinaten."""
    if len(input_data) == 2 and all(is_float(coord) for coord in input_data):
        lat, lon = map(float, input_data)
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return True, lat, lon
    return False, None, None

def validate_address(address):
    """
    Controleer of het adres correct is: 'straat huisnummer, plaats'.
    Het adres wordt opgesplitst en gecontroleerd op straat/huisnummer en plaats.
    """
    parts = address.split(',')
    if len(parts) != 2:
        return False, None, None
    
    street_part = parts[0].strip()
    place_part = parts[1].strip()
    
    # Simpele validatie van straat/huisnummer en plaatsnaam
    if street_part and place_part and any(char.isdigit() for char in street_part):
        return True, street_part, place_part
    return False, None, None

def open_in_browser(location):
    """Open een locatie in Google Maps in de browser."""
    base_url = "https://www.google.com/maps/search/?api=1&query="
    webbrowser.open(base_url + location)

def main():
    # Definieer de argument parser
    parser = argparse.ArgumentParser(description="Verwerk locatiegegevens.")
    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        help="Voer locatiegegevens in: lat, lon of 'straat huisnummer, plaats'.",
    )

    # Argumenten parsen
    args = parser.parse_args()

    # Controleer of er iets is ingevuld
    if not args.input:
        print(
            "Fout: Er zijn geen locatiegegevens opgegeven.\n"
            "Gebruik de volgende formaten:\n"
            "- Voor coördinaten: lat, lon (bijv. 52.3676, 4.9041)\n"
            "- Voor adres: 'Straat huisnummer, Plaats' (bijv. 'Damrak 1, Amsterdam')"
        )
        sys.exit(1)

    # Splits input op komma's om te controleren of het om lat/lon of een adres gaat
    input_data = [x.strip() for x in args.input.split(",")]

    # Controleer op lat/lon
    valid_lat_lon, lat, lon = validate_lat_lon(input_data)
    if valid_lat_lon:
        print(f"Validatie geslaagd: coördinaten ingevoerd - Latitude: {lat}, Longitude: {lon}")
        open_in_browser(f"{lat},{lon}")
        sys.exit(0)

    # Controleer op adres
    valid_address, street, place = validate_address(args.input)
    if valid_address:
        print(f"Validatie geslaagd: adres ingevoerd - {street}, {place}")
        open_in_browser(f"{street}, {place}")
        sys.exit(0)

    # Als input niet voldoet aan criteria, gebruik als zoekquery
    print(
        f"De ingevoerde gegevens zijn niet direct herkend als geldige coördinaten of adres.\n"
        f"De zoekterm '{args.input}' wordt nu als zoekopdracht gebruikt op Google Maps."
    )
    open_in_browser(args.input)
    sys.exit(0)

if __name__ == "__main__":
    main()
