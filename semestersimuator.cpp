#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

class Character {
public:
    string name;
    string major;
    string academicGoals;
    int health;
    int stress;
    int socialLife;
    int academicPerformance;

    Character(string n, string m, string a) : name(n), major(m), academicGoals(a), health(100), stress(0), socialLife(50), academicPerformance(50) {}

    void displayStatus() {
        cout << "Name: " << name << endl;
        cout << "Major: " << major << endl;
        cout << "Academic Goals: " << academicGoals << endl;
        cout << "Health: " << health << endl;
        cout << "Stress: " << stress << endl;
        cout << "Social Life: " << socialLife << endl;
        cout << "Academic Performance: " << academicPerformance << endl;
    }
};

class Game {
public:
    Character* character;
    int week;

    Game(Character* c) : character(c), week(1) {}

    void start() {
        cout << "Welcome to Semester Simulator!" << endl;
        while (week <= 16) {
            cout << "Week " << week << endl;
            character->displayStatus();
            performActivities();
            week++;
        }
        endGame();
    }

    void performActivities() {
        int choice;
        cout << "Choose an activity for this week:" << endl;
        cout << "1. Study" << endl;
        cout << "2. Socialize" << endl;
        cout << "3. Work Part-Time" << endl;
        cout << "4. Exercise" << endl;
        cout << "5. Rest" << endl;
        cin >> choice;

        switch (choice) {
        case 1:
            study();
            break;
        case 2:
            socialize();
            break;
        case 3:
            workPartTime();
            break;
        case 4:
            exercise();
            break;
        case 5:
            rest();
            break;
        default:
            cout << "Invalid choice. Please try again." << endl;
            performActivities();
            break;
        }
    }

    void study() {
        character->academicPerformance += 10;
        character->stress += 5;
        cout << "You studied hard this week." << endl;
    }

    void socialize() {
        character->socialLife += 10;
        character->stress -= 5;
        cout << "You spent time with friends this week." << endl;
    }

    void workPartTime() {
        character->academicPerformance -= 5;
        character->stress += 10;
        cout << "You worked part-time this week." << endl;
    }

    void exercise() {
        character->health += 10;
        character->stress -= 5;
        cout << "You exercised this week." << endl;
    }

    void rest() {
        character->health += 5;
        character->stress -= 10;
        cout << "You rested this week." << endl;
    }

    void endGame() {
        cout << "The semester has ended!" << endl;
        character->displayStatus();
        cout << "Thank you for playing Semester Simulator!" << endl;
    }
};

int main() {
    string name, major, academicGoals;
    cout << "Enter your character's name: ";
    getline(cin, name);
    cout << "Enter your character's major: ";
    getline(cin, major);
    cout << "Enter your character's academic goals: ";
    getline(cin, academicGoals);

    Character* character = new Character(name, major, academicGoals);
    Game game(character);
    game.start();

    delete character;
    return 0;
}