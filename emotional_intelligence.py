from enum import Enum
from dataclasses import dataclass
from typing import List


class PersonalityType(Enum):
    EMPATHETIC_LEADER = 1
    CHAOTIC_JESTER = 2
    PEOPLE_PLEASER_WITH_ISSUES = 3


@dataclass
class TraitScore:
    """Represents a personality trait with its intensity (0-10)"""
    trait: str
    score: int

    def __str__(self):
        return f"{self.trait}: {self.score}/10"


class Person:
    """Base class representing a person with emotional intelligence traits"""
    
    def __init__(self, name: str, personality_type: PersonalityType):
        self.name = name
        self.personality_type = personality_type
        self.traits: List[TraitScore] = []
        self._initialize_traits()
    
    def _initialize_traits(self):
        """Initialize traits based on personality type"""
        pass
    
    def get_emotional_intelligence_profile(self) -> dict:
        """Return a dictionary of the person's EI profile"""
        return {
            "name": self.name,
            "type": self.personality_type.name,
            "traits": [{"trait": t.trait, "score": t.score} for t in self.traits],
            "average_ei_score": self.calculate_average_ei()
        }
    
    def calculate_average_ei(self) -> float:
        """Calculate average emotional intelligence score"""
        if not self.traits:
            return 0
        return round(sum(t.score for t in self.traits) / len(self.traits), 2)
    
    def display_profile(self):
        """Display person's personality profile"""
        print(f"\n{'='*50}")
        print(f"Name: {self.name}")
        print(f"Type: {self.personality_type.name}")
        print(f"{'='*50}")
        for trait in self.traits:
            self._display_trait_bar(trait)
        print(f"Average EI Score: {self.calculate_average_ei()}/10")
        print(f"{'='*50}\n")
    
    @staticmethod
    def _display_trait_bar(trait: TraitScore):
        """Display a visual bar for trait score"""
        bar_length = trait.score
        bar = "█" * bar_length + "░" * (10 - bar_length)
        print(f"{trait.trait:25} [{bar}] {trait.score}/10")
    
    def interact(self, other_person: 'Person', scenario: str) -> str:
        """Simulate interaction between two people"""
        pass


class EmphatheticLeader(Person):
    """
    Personality Type 1: Caring, Nurturing, Socially Aware, Smart
    Positive traits: Caring, Nurturing, Socially Aware, Smart, Loveable, Respectful
    Growth areas: Brags
    """
    
    def __init__(self, name: str = "Empathetic Leader"):
        super().__init__(name, PersonalityType.EMPATHETIC_LEADER)
    
    def _initialize_traits(self):
        self.traits = [
            TraitScore("Caring", 9),
            TraitScore("Nurturing", 8),
            TraitScore("Social Awareness", 9),
            TraitScore("Intelligence", 8),
            TraitScore("Likability", 8),
            TraitScore("Respectfulness", 9),
            TraitScore("Humility", 6),  # Lower due to bragging tendency
        ]
    
    def interact(self, other_person: 'Person', scenario: str) -> str:
        responses = {
            "conflict": f"{self.name} listens carefully to {other_person.name}'s perspective and tries to find a solution that respects both parties.",
            "success": f"{self.name} celebrates {other_person.name}'s success, though might mention their own achievements.",
            "struggle": f"{self.name} offers genuine support and guidance to {other_person.name}.",
            "group": f"{self.name} naturally takes charge, making sure everyone feels heard and valued."
        }
        return responses.get(scenario, "Handles situation with grace and empathy.")


class ChaoticJester(Person):
    """
    Personality Type 2: Chaotic, Careless, Funny, Antisocial
    Positive traits: Funny
    Growth areas: Chaotic, Careless, Antisocial, Not Charming
    Strengths: Respectful (surprisingly!)
    """
    
    def __init__(self, name: str = "Chaotic Jester"):
        super().__init__(name, PersonalityType.CHAOTIC_JESTER)
    
    def _initialize_traits(self):
        self.traits = [
            TraitScore("Humor", 9),
            TraitScore("Chaotic Energy", 8),
            TraitScore("Carelessness", 7),
            TraitScore("Social Engagement", 3),
            TraitScore("Charm", 4),
            TraitScore("Respectfulness", 7),
            TraitScore("Responsibility", 3),
        ]
    
    def interact(self, other_person: 'Person', scenario: str) -> str:
        responses = {
            "conflict": f"{self.name} makes a joke to diffuse tension, but may not fully address the serious issue.",
            "success": f"{self.name} laughs it off and moves on to the next thing without dwelling on it.",
            "struggle": f"{self.name} doesn't know how to offer emotional support, but provides comic relief.",
            "group": f"{self.name} entertains everyone but often unintentionally upsets people with insensitive humor."
        }
        return responses.get(scenario, "Does their own thing without much regard for others.")


class PeoplePleaser(Person):
    """
    Personality Type 3: Gossips, Passive Aggressive, Takes Care of Things
    Positive traits: Takes care of things
    Growth areas: Gossips, Passive Aggressive, Wants applause, Looks down on people, Feels entitled
    Complex traits: People pleaser (can be positive or negative)
    """
    
    def __init__(self, name: str = "People Pleaser"):
        super().__init__(name, PersonalityType.PEOPLE_PLEASER_WITH_ISSUES)
    
    def _initialize_traits(self):
        self.traits = [
            TraitScore("Gossip Tendency", 8),
            TraitScore("Passive Aggressiveness", 7),
            TraitScore("Responsibility", 8),
            TraitScore("Need for Validation", 8),
            TraitScore("Condescension", 6),
            TraitScore("Entitlement", 7),
            TraitScore("People Pleasing", 8),
        ]
    
    def interact(self, other_person: 'Person', scenario: str) -> str:
        responses = {
            "conflict": f"{self.name} agrees on the surface but privately complains to others about {other_person.name}.",
            "success": f"{self.name} helps {other_person.name} succeed but expects recognition and praise.",
            "struggle": f"{self.name} 'helps' while subtly reminding them of their own superiority.",
            "group": f"{self.name} organizes things meticulously but keeps score of who appreciates their efforts."
        }
        return responses.get(scenario, "Takes charge but expects significant acknowledgment.")


class EmotionalIntelligenceAnalyzer:
    """Analyzer for comparing emotional intelligence profiles"""
    
    def __init__(self):
        self.people: List[Person] = []
    
    def add_person(self, person: Person):
        """Add a person to the analyzer"""
        self.people.append(person)
    
    def compare_profiles(self):
        """Compare all people's profiles"""
        print("\n" + "="*60)
        print("EMOTIONAL INTELLIGENCE COMPARISON")
        print("="*60)
        
        names = [p.name for p in self.people]
        scores = [p.calculate_average_ei() for p in self.people]
        
        for name, score in zip(names, scores):
            bar = "█" * int(score) + "░" * (10 - int(score))
            print(f"{name:30} [{bar}] {score}/10")
        
        print("="*60 + "\n")
    
    def show_interaction(self, person1_idx: int, person2_idx: int, scenario: str):
        """Show how two people would interact"""
        if 0 <= person1_idx < len(self.people) and 0 <= person2_idx < len(self.people):
            p1 = self.people[person1_idx]
            p2 = self.people[person2_idx]
            print(f"\nScenario: {scenario}")
            print(f"Interaction between {p1.name} and {p2.name}:")
            print(f"  {p1.interact(p2, scenario)}")
            print()


def main():
    """Main execution"""
    # Create three people with different emotional intelligence profiles
    person1 = EmphatheticLeader("Alice (Empathetic Leader)")
    person2 = ChaoticJester("Bob (Chaotic Jester)")
    person3 = PeoplePleaser("Charlie (People Pleaser)")
    
    # Display individual profiles
    person1.display_profile()
    person2.display_profile()
    person3.display_profile()
    
    # Compare profiles
    analyzer = EmotionalIntelligenceAnalyzer()
    analyzer.add_person(person1)
    analyzer.add_person(person2)
    analyzer.add_person(person3)
    
    analyzer.compare_profiles()
    
    # Show interactions
    scenarios = ["conflict", "success", "struggle", "group"]
    
    print("INTERACTION SIMULATIONS:")
    print("="*60)
    for scenario in scenarios:
        analyzer.show_interaction(0, 1, scenario)
        analyzer.show_interaction(0, 2, scenario)
        analyzer.show_interaction(1, 2, scenario)


if __name__ == "__main__":
    main()
