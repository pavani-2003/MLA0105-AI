class VacuumCleaner:
    def __init__(self):
        self.location = 0  # 0 represents location A, 1 represents location B
        self.cleaned = {0: False, 1: False}

    def move_to_location(self, new_location):
        self.location = new_location

    def clean_location(self):
        self.cleaned[self.location] = True
        print(f"Location {chr(ord('A') + self.location)} cleaned.")

    def is_location_clean(self):
        return self.cleaned[self.location]

def clean_environment(vacuum_cleaner, locations):
    for location in locations:
        if not vacuum_cleaner.is_location_clean():
            vacuum_cleaner.clean_location()
        if location != vacuum_cleaner.location:
            vacuum_cleaner.move_to_location(location)
            print(f"Moved to location {chr(ord('A') + location)}.")

if __name__ == "__main__":
    vacuum_cleaner = VacuumCleaner()

    # Locations to be cleaned
    locations_to_clean = [0, 1]

    # Clean the environment
    clean_environment(vacuum_cleaner, locations_to_clean)
