from body import CelestialBody, SolarSystem

if __name__ == "__main__":
    solar_system = SolarSystem(width=1400, height=900)
    sun = CelestialBody(
        solar_system,
        mass=10_000,
        velocity=(0, 0),
        color="yellow",
    )

    planet_a = CelestialBody(
        solar_system,
        mass=1,
        position=(-350, 0),
        velocity=(0, 5),
        color="red",
    )

    planet_b = CelestialBody(
        solar_system,
        mass=1,
        position=(-500, 0),
        velocity=(0, 5),
        color="green",
    )
    while True:
        solar_system.calculate_all_body_interactions()
        solar_system.update_all()
