# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Club:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

class FootballLeague:
    def __init__(self):
        self.clubs = []
        self.matches = []

    def add_club(self, name, city):
        for club in self.clubs:
            if club.name == name or club.city == city:
                print("Club with the same name or city already exists.")
                return

        new_club = Club(name, city)
        self.clubs.append(new_club)
        print(f"Club {name} from {city} added successfully.")

    def display_clubs(self):
        if not self.clubs:
            print("No clubs available.")
            return

        print("\nList of Clubs:")
        for idx, club in enumerate(self.clubs, start=1):
            print(f"{idx}. {club.name} ({club.city})")

    def add_match(self, match_data):
        for match in self.matches:
            if match[:2] == match_data[:2] or match[2:] == match_data[2:]:
                print("Match with the same teams already exists.")
                return

        self.matches.append(match_data)
        print("Match added successfully.")

    def input_single_match(self):
        self.display_clubs()
        club1_idx = int(input("Enter the index of the first club: ")) - 1
        club2_idx = int(input("Enter the index of the second club: ")) - 1
        score1 = int(input("Enter the score of the first club: "))
        score2 = int(input("Enter the score of the second club: "))

        self.update_stats(club1_idx, club2_idx, score1, score2)

    def input_multiple_matches(self):
        while True:
            self.display_clubs()
            club1_idx = int(input("Enter the index of the first club: ")) - 1
            club2_idx = int(input("Enter the index of the second club: ")) - 1
            score1 = int(input("Enter the score of the first club: "))
            score2 = int(input("Enter the score of the second club: "))
            self.matches.append((club1_idx, club2_idx, score1, score2))

            add_more = input("Do you want to add another match? (yes/no): ").lower()
            if add_more != 'yes':
                break

        for match_data in self.matches:
            self.update_stats(*match_data)

    def update_stats(self, club1_idx, club2_idx, score1, score2):
        club1 = self.clubs[club1_idx]
        club2 = self.clubs[club2_idx]

        club1.matches += 1
        club2.matches += 1

        if score1 > score2:
            club1.wins += 1
            club1.points += 3
            club2.losses += 1
        elif score1 < score2:
            club2.wins += 1
            club2.points += 3
            club1.losses += 1
        else:
            club1.draws += 1
            club2.draws += 1
            club1.points += 1
            club2.points += 1

        club1.goals_for += score1
        club1.goals_against += score2
        club2.goals_for += score2
        club2.goals_against += score1

    def display_standings(self):
        if not self.clubs:
            print("No clubs available.")
            return

        print("\nLeague Standings:")
        print(f"{'No':<5}{'Club':<15}{'Ma':<5}{'Me':<5}{'S':<5}{'K':<5}{'GM':<5}{'GK':<5}{'Point':<5}")
        for idx, club in enumerate(self.clubs, start=1):
            print(f"{idx:<5}{club.name:<15}{club.matches:<5}{club.wins:<5}{club.draws:<5}{club.losses:<5}"
                  f"{club.goals_for:<5}{club.goals_against:<5}{club.points:<5}")

def main():
    league = FootballLeague()

    while True:
        print("\nMenu:")
        print("1. Input Data Klub")
        print("2. Input Skor Pertandingan (Single Match)")
        print("3. Input Skor Pertandingan (Multiple Matches)")
        print("4. Tampilan Klasemen")
        print("5. Keluar")

        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == '1':
            name = input("Nama Klub: ")
            city = input("Kota Klub: ")
            league.add_club(name, city)

        elif choice == '2':
            league.input_single_match()

        elif choice == '3':
            league.input_multiple_matches()

        elif choice == '4':
            league.display_standings()

        elif choice == '5':
            print("Terima kasih, keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

