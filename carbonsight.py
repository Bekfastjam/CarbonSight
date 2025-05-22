
# carbonsight.py

# Emission factors (kg CO2 per unit)
EMISSION_FACTORS = {
    'car_km': 0.221,         # average passenger vehicle per km
    'electricity_kwh': 0.512, # world avg, adjust as needed
    'short_flight': 255,     # short-haul flight per flight (~1 hour)
}

def main():
    print("\n=== CarbonSight – Real-Time CO₂ Emissions Tracker ===\n")
    try:
        km = float(input("Enter kilometers driven today: ") or 0)
        kwh = float(input("Enter electricity used (kWh): ") or 0)
        flights = int(input("Enter number of short flights: ") or 0)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    car_emissions = km * EMISSION_FACTORS['car_km']
    elec_emissions = kwh * EMISSION_FACTORS['electricity_kwh']
    flight_emissions = flights * EMISSION_FACTORS['short_flight']
    total = car_emissions + elec_emissions + flight_emissions

    print("\nYour estimated CO₂ emissions today: {:.1f} kg".format(total))
    print("- Car: {:.1f} kg".format(car_emissions))
    print("- Electricity: {:.1f} kg".format(elec_emissions))
    print("- Flights: {:.1f} kg".format(flight_emissions))
    print("\nThank you for using CarbonSight!\n")

if __name__ == "__main__":
    main()
