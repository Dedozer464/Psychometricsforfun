from enum import Enum
from dataclasses import dataclass
from typing import List, Dict
import math


class PsychopathyFactor(Enum):
    """Psychopathy factors based on PCL-R"""
    FACTOR_1 = "Interpersonal/Affective (Emotional Deficiency)"
    FACTOR_2 = "Social Deviance (Behavioral Problems)"


class PCLRItem:
    """PCL-R Item with score (0-2 scale)"""
    
    def __init__(self, item_number: int, description: str, category: str):
        self.item_number = item_number
        self.description = description
        self.category = category  # Factor 1 or Factor 2
        self.score = 0  # 0 = Not present, 1 = Possibly present, 2 = Definitely present
    
    def set_score(self, score: int):
        """Set score with validation"""
        if 0 <= score <= 2:
            self.score = score
        else:
            raise ValueError("Score must be 0, 1, or 2")
    
    def __str__(self):
        score_label = ["Not present", "Possibly present", "Definitely present"]
        return f"Item {self.item_number}: {self.description} - {score_label[self.score]} ({self.score})"


class PsychopathyProfile:
    """Comprehensive psychopathy profile"""
    
    def __init__(self, name: str):
        self.name = name
        self.items: List[PCLRItem] = []
        self.total_score = 0
        self.factor_1_score = 0
        self.factor_2_score = 0
        self._initialize_pcl_r()
    
    def _initialize_pcl_r(self):
        """Initialize all PCL-R items"""
        # Factor 1 - Interpersonal/Affective (Emotional Deficiency)
        self.items.append(PCLRItem(1, "Glibness/Superficial charm", "Factor 1"))
        self.items.append(PCLRItem(2, "Grandiose sense of self-worth", "Factor 1"))
        self.items.append(PCLRItem(3, "Need for stimulation/Proneness to boredom", "Factor 1"))
        self.items.append(PCLRItem(4, "Pathological lying", "Factor 1"))
        self.items.append(PCLRItem(5, "Cunning/Manipulative", "Factor 1"))
        self.items.append(PCLRItem(6, "Lack of remorse or guilt", "Factor 1"))
        self.items.append(PCLRItem(7, "Shallow affect", "Factor 1"))
        self.items.append(PCLRItem(8, "Callousness/Lack of empathy", "Factor 1"))
        self.items.append(PCLRItem(9, "Parasitic lifestyle", "Factor 1"))
        
        # Factor 2 - Social Deviance (Behavioral Problems)
        self.items.append(PCLRItem(10, "Poor behavioral controls", "Factor 2"))
        self.items.append(PCLRItem(11, "Promiscuous sexual behavior", "Factor 2"))
        self.items.append(PCLRItem(12, "Early behavior problems", "Factor 2"))
        self.items.append(PCLRItem(13, "Lack of realistic long-term goals", "Factor 2"))
        self.items.append(PCLRItem(14, "Impulsivity", "Factor 2"))
        self.items.append(PCLRItem(15, "Irresponsibility", "Factor 2"))
        self.items.append(PCLRItem(16, "Failure to accept responsibility", "Factor 2"))
        self.items.append(PCLRItem(17, "Many short-term marital relationships", "Factor 2"))
        self.items.append(PCLRItem(18, "Juvenile delinquency", "Factor 2"))
        self.items.append(PCLRItem(19, "Revocation of conditional release", "Factor 2"))
        self.items.append(PCLRItem(20, "Criminal versatility", "Factor 2"))
    
    def set_item_score(self, item_number: int, score: int):
        """Set score for a specific item"""
        if 1 <= item_number <= 20:
            self.items[item_number - 1].set_score(score)
        else:
            raise ValueError("Item number must be between 1 and 20")
    
    def calculate_scores(self):
        """Calculate total and factor scores"""
        self.total_score = sum(item.score for item in self.items)
        
        factor_1_items = [item for item in self.items if item.category == "Factor 1"]
        factor_2_items = [item for item in self.items if item.category == "Factor 2"]
        
        self.factor_1_score = sum(item.score for item in factor_1_items)
        self.factor_2_score = sum(item.score for item in factor_2_items)
    
    def get_psychopathy_level(self) -> str:
        """Classify psychopathy level based on PCL-R total score"""
        if self.total_score >= 30:
            return "HIGH PSYCHOPATHY (Criminal psychopath range)"
        elif self.total_score >= 25:
            return "MODERATE-HIGH PSYCHOPATHY"
        elif self.total_score >= 20:
            return "MODERATE PSYCHOPATHY"
        elif self.total_score >= 15:
            return "LOW-MODERATE PSYCHOPATHY"
        elif self.total_score >= 10:
            return "LOW PSYCHOPATHY"
        else:
            return "MINIMAL PSYCHOPATHY (Normal range)"
    
    def get_risk_assessment(self) -> str:
        """Risk assessment based on scores"""
        if self.total_score >= 30:
            return "HIGH RISK - Likely to engage in violent/criminal behavior"
        elif self.total_score >= 25:
            return "MODERATE-HIGH RISK - Prone to manipulation and exploitation"
        elif self.total_score >= 20:
            return "MODERATE RISK - Capable of harmful behavior, limited empathy"
        elif self.total_score >= 15:
            return "LOW-MODERATE RISK - Some concerning traits, generally manageable"
        elif self.total_score >= 10:
            return "LOW RISK - Minimal psychopathic traits"
        else:
            return "MINIMAL RISK - Normal personality range"
    
    def get_factor_profile(self) -> str:
        """Describe the factor profile"""
        f1_pct = (self.factor_1_score / 18) * 100
        f2_pct = (self.factor_2_score / 22) * 100
        
        profile = f"Factor 1 (Emotional): {self.factor_1_score}/18 ({f1_pct:.0f}%) - "
        profile += "High emotional deficiency\n" if f1_pct >= 50 else "Moderate emotional deficiency\n" if f1_pct >= 30 else "Low emotional deficiency\n"
        
        profile += f"Factor 2 (Behavioral): {self.factor_2_score}/22 ({f2_pct:.0f}%) - "
        profile += "High behavioral problems\n" if f2_pct >= 50 else "Moderate behavioral problems\n" if f2_pct >= 30 else "Low behavioral problems"
        
        return profile
    
    def display_profile(self):
        """Display full psychopathy profile"""
        self.calculate_scores()
        
        print(f"\n{'='*80}")
        print(f"PSYCHOPATHY CHECKLIST - REVISED (PCL-R) PROFILE: {self.name}")
        print(f"{'='*80}")
        
        print(f"\nTotal PCL-R Score: {self.total_score}/40")
        print(f"Psychopathy Level: {self.get_psychopathy_level()}")
        print(f"Risk Assessment: {self.get_risk_assessment()}")
        
        print(f"\n{self.get_factor_profile()}")
        
        print(f"\n{'─'*80}")
        print("FACTOR 1 - INTERPERSONAL/AFFECTIVE (Emotional Deficiency) Items:")
        print(f"{'─'*80}")
        for item in self.items:
            if item.category == "Factor 1":
                bar = "█" * item.score + "░" * (2 - item.score)
                print(f"  Item {item.item_number:2d}: {item.description:40s} [{bar}] {item.score}")
        
        print(f"\n{'─'*80}")
        print("FACTOR 2 - SOCIAL DEVIANCE (Behavioral Problems) Items:")
        print(f"{'─'*80}")
        for item in self.items:
            if item.category == "Factor 2":
                bar = "█" * item.score + "░" * (2 - item.score)
                print(f"  Item {item.item_number:2d}: {item.description:40s} [{bar}] {item.score}")
        
        print(f"\n{'='*80}\n")


class AlicePsychopathy(PsychopathyProfile):
    """
    Alice: Empathetic Leader
    Expected: Very low psychopathy (genuine empathy, high conscience)
    """
    
    def __init__(self):
        super().__init__("Alice (Empathetic Leader)")
        self._set_alice_scores()
    
    def _set_alice_scores(self):
        """Set psychopathy scores based on profile"""
        # Factor 1 - Very low (genuine empathy, authentic)
        self.set_item_score(1, 0)   # Glibness - No, genuine
        self.set_item_score(2, 1)   # Grandiosity - Slight (confident, not grandiose)
        self.set_item_score(3, 0)   # Need for stimulation - No, stable
        self.set_item_score(4, 0)   # Pathological lying - No
        self.set_item_score(5, 0)   # Manipulative - No
        self.set_item_score(6, 0)   # Lack of remorse - No, has conscience
        self.set_item_score(7, 0)   # Shallow affect - No, deep emotions
        self.set_item_score(8, 0)   # Lack of empathy - No, highly empathetic
        self.set_item_score(9, 0)   # Parasitic - No, self-reliant
        
        # Factor 2 - Low (well-controlled, responsible)
        self.set_item_score(10, 0)  # Poor behavioral controls - No
        self.set_item_score(11, 0)  # Promiscuous - No
        self.set_item_score(12, 0)  # Early behavior problems - No
        self.set_item_score(13, 0)  # Lack of goals - No, goal-oriented
        self.set_item_score(14, 0)  # Impulsivity - No
        self.set_item_score(15, 0)  # Irresponsibility - No, very responsible
        self.set_item_score(16, 0)  # Failure to accept responsibility - No
        self.set_item_score(17, 0)  # Many short-term relationships - No
        self.set_item_score(18, 0)  # Juvenile delinquency - No
        self.set_item_score(19, 0)  # Revocation of conditional release - N/A
        self.set_item_score(20, 0)  # Criminal versatility - No


class BobPsychopathy(PsychopathyProfile):
    """
    Bob: Chaotic Jester
    Expected: Moderate psychopathy (impulsive, callous humor, lacks planning)
    """
    
    def __init__(self):
        super().__init__("Bob (Chaotic Jester)")
        self._set_bob_scores()
    
    def _set_bob_scores(self):
        """Set psychopathy scores based on profile"""
        # Factor 1 - Moderate (some callousness, shallow affect in humor)
        self.set_item_score(1, 1)   # Glibness - Moderately (comedic charm)
        self.set_item_score(2, 1)   # Grandiosity - Some (thinks he's funny)
        self.set_item_score(3, 2)   # Need for stimulation - Yes (seeks chaos)
        self.set_item_score(4, 1)   # Pathological lying - Some (embellishes)
        self.set_item_score(5, 1)   # Manipulative - Some (uses humor to avoid)
        self.set_item_score(6, 1)   # Lack of remorse - Moderately (doesn't care much)
        self.set_item_score(7, 1)   # Shallow affect - Moderately (surface humor)
        self.set_item_score(8, 1)   # Lack of empathy - Moderate (insensitive jokes)
        self.set_item_score(9, 0)   # Parasitic - No, but irresponsible
        
        # Factor 2 - High (poor controls, impulsive, behavioral issues)
        self.set_item_score(10, 2)  # Poor behavioral controls - Yes, very impulsive
        self.set_item_score(11, 1)  # Promiscuous - Possibly (careless)
        self.set_item_score(12, 2)  # Early behavior problems - Likely
        self.set_item_score(13, 2)  # Lack of goals - Yes, no direction
        self.set_item_score(14, 2)  # Impulsivity - Very high
        self.set_item_score(15, 2)  # Irresponsibility - High
        self.set_item_score(16, 2)  # Failure to accept responsibility - Yes
        self.set_item_score(17, 1)  # Many short-term relationships - Possibly
        self.set_item_score(18, 1)  # Juvenile delinquency - Possibly
        self.set_item_score(19, 0)  # Revocation of conditional release - N/A
        self.set_item_score(20, 1)  # Criminal versatility - Some


class CharliePsychopathy(PsychopathyProfile):
    """
    Charlie: People Pleaser with Narcissistic/Manipulative Traits
    Expected: HIGH psychopathy (manipulative, lacks genuine empathy, exploits others)
    """
    
    def __init__(self):
        super().__init__("Charlie (People Pleaser)")
        self._set_charlie_scores()
    
    def _set_charlie_scores(self):
        """Set psychopathy scores based on profile"""
        # Factor 1 - HIGH (master manipulator, shallow emotions, lacks true empathy)
        self.set_item_score(1, 2)   # Glibness - Yes, expert charm
        self.set_item_score(2, 2)   # Grandiosity - High (entitlement, superiority)
        self.set_item_score(3, 1)   # Need for stimulation - Some (needs validation)
        self.set_item_score(4, 2)   # Pathological lying - Yes (lies about contributions)
        self.set_item_score(5, 2)   # Manipulative - Highly manipulative
        self.set_item_score(6, 2)   # Lack of remorse - Yes, no guilt
        self.set_item_score(7, 1)   # Shallow affect - Moderately (fakes emotions)
        self.set_item_score(8, 2)   # Lack of empathy - Yes, no genuine empathy
        self.set_item_score(9, 1)   # Parasitic - Some (leeches off others' work)
        
        # Factor 2 - Moderate (controlled behavior, subtle deviance)
        self.set_item_score(10, 1)  # Poor behavioral controls - Controlled but passive-aggressive
        self.set_item_score(11, 0)  # Promiscuous - No
        self.set_item_score(12, 0)  # Early behavior problems - No (well-hidden)
        self.set_item_score(13, 1)  # Lack of goals - Some (validation-focused)
        self.set_item_score(14, 1)  # Impulsivity - Low impulsivity (calculated)
        self.set_item_score(15, 1)  # Irresponsibility - Appears responsible, isn't really
        self.set_item_score(16, 2)  # Failure to accept responsibility - Yes, blames others
        self.set_item_score(17, 0)  # Many short-term relationships - No
        self.set_item_score(18, 0)  # Juvenile delinquency - No (hidden)
        self.set_item_score(19, 0)  # Revocation of conditional release - N/A
        self.set_item_score(20, 1)  # Criminal versatility - Some (gossip, passive-aggressive)


class PsychopathyComparator:
    """Compare psychopathy profiles"""
    
    def __init__(self):
        self.profiles: List[PsychopathyProfile] = []
    
    def add_profile(self, profile: PsychopathyProfile):
        """Add a psychopathy profile"""
        self.profiles.append(profile)
    
    def compare_all(self):
        """Display comparison of all profiles"""
        print("\n" + "="*80)
        print("PSYCHOPATHY COMPARISON - PCL-R TOTAL SCORES")
        print("="*80)
        
        for profile in sorted(self.profiles, key=lambda p: p.total_score, reverse=True):
            profile.calculate_scores()
            bar_length = int(profile.total_score / 2)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            print(f"{profile.name:30} [{bar}] {profile.total_score:2d}/40 - {profile.get_psychopathy_level()}")
        
        print("="*80 + "\n")
    
    def compare_factors(self):
        """Compare Factor 1 and Factor 2 scores"""
        print("\n" + "="*80)
        print("PSYCHOPATHY FACTOR COMPARISON")
        print("="*80)
        
        for profile in self.profiles:
            profile.calculate_scores()
            print(f"\n{profile.name}:")
            print(f"  Factor 1 (Emotional/Interpersonal): {profile.factor_1_score:2d}/18 ({(profile.factor_1_score/18)*100:.0f}%)")
            print(f"  Factor 2 (Behavioral/Social Deviance): {profile.factor_2_score:2d}/22 ({(profile.factor_2_score/22)*100:.0f}%)")
            print(f"  Total: {profile.total_score:2d}/40")
        
        print("\n" + "="*80 + "\n")
    
    def behavioral_predictions(self):
        """Predict behaviors based on psychopathy scores"""
        print("\n" + "="*80)
        print("BEHAVIORAL PREDICTIONS BASED ON PSYCHOPATHY PROFILE")
        print("="*80)
        
        behaviors = {
            "Alice": {
                "score": 2,
                "prediction": """
Alice (Total: 2/40 - MINIMAL PSYCHOPATHY)
├─ Interpersonal: Genuine, authentic relationships
├─ Emotional: Deep emotional connections, genuine remorse
├─ Behavior: Responsible, planned, long-term focused
├─ Relationships: Stable, committed relationships
├─ Work: Ethical behavior, considers others' wellbeing
└─ Risk: Very low risk for harm, high trustworthiness
"""
            },
            "Bob": {
                "score": 20,
                "prediction": """
Bob (Total: 20/40 - MODERATE PSYCHOPATHY)
├─ Interpersonal: Superficial charm, shallow connections
├─ Emotional: Limited empathy, humor masks callousness
├─ Behavior: Impulsive, poor planning, chaotic
├─ Relationships: Short-lived, unstable connections
├─ Work: Unreliable, avoids responsibility, blames others
└─ Risk: Moderate risk - causes harm through negligence & insensitivity
"""
            },
            "Charlie": {
                "score": 27,
                "prediction": """
Charlie (Total: 27/40 - MODERATE-HIGH PSYCHOPATHY)
├─ Interpersonal: Expert manipulator, calculated relationships
├─ Emotional: Shallow affect, fakes emotions for control
├─ Behavior: Controlled, planned exploitation strategies
├─ Relationships: Exploitative, uses people instrumentally
├─ Work: Undermines competitors, takes credit, passive-aggressive
└─ Risk: Moderate-high risk - causes harm through manipulation & exploitation
"""
            }
        }
        
        for profile in sorted(self.profiles, key=lambda p: p.total_score):
            profile.calculate_scores()
            key = [k for k in behaviors.keys() if k.lower() in profile.name.lower()][0]
            print(behaviors[key]["prediction"])
        
        print("="*80 + "\n")
    
    def clinical_insights(self):
        """Provide clinical insights"""
        print("\n" + "="*80)
        print("CLINICAL INSIGHTS & RECOMMENDATIONS")
        print("="*80)
        
        for profile in sorted(self.profiles, key=lambda p: p.total_score):
            profile.calculate_scores()
            print(f"\n{profile.name} (PCL-R: {profile.total_score}/40)")
            print("─" * 80)
            
            if profile.total_score < 10:
                insight = "PROFILE: Non-psychopathic individual\nCHARACTERISTICS:\n  • Genuine emotional capacity and empathy\n  • Stable relationships and long-term commitment\n  • Accepts responsibility and feels remorse\n  • Guided by conscience and moral principles\nMANAGEMENT: Standard social interaction, trustworthy for leadership"
                print(insight)
            
            elif profile.total_score < 20:
                insight = "PROFILE: Low-moderate psychopathic traits\nCHARACTERISTICS:\n  • Some impulse control issues but generally functional\n  • Limited empathy but capable of appearing to care\n  • Inconsistent follow-through and responsibility\n  • Unreliable in interpersonal commitments\nMANAGEMENT: Set clear boundaries, avoid giving unsupervised responsibility, use concrete consequences"
                print(insight)
            
            elif profile.total_score < 30:
                insight = "PROFILE: Moderate to high psychopathic traits\nCHARACTERISTICS:\n  • Expert at manipulation and deception\n  • Superficial charm masks predatory nature\n  • Exploits others while appearing helpful\n  • High risk for emotional/social harm to others\n  • May use intimidation, gossip, or sabotage\nMANAGEMENT: Do not place in positions of authority or trust, avoid intimate relationships, establish firm accountability systems, legal safeguards if needed"
                print(insight)
            
            else:
                insight = "PROFILE: High psychopathic traits (Criminal range)\nCHARACTERISTICS:\n  • Likely to cause serious harm without remorse\n  • Sophisticated manipulation and deception\n  • No emotional bonds, purely predatory\n  • High risk for violence, theft, or exploitation\nMANAGEMENT: Requires professional intervention, may need legal restriction, high supervision and formal oversight necessary"
                print(insight)
        
        print("\n" + "="*80 + "\n")


def main():
    """Main execution"""
    print("\n" + "#"*80)
    print("# PSYCHOPATHY CHECKLIST - REVISED (PCL-R)")
    print("# Clinical Assessment of Three Personality Types")
    print("#"*80)
    
    # Create psychopathy profiles
    alice = AlicePsychopathy()
    bob = BobPsychopathy()
    charlie = CharliePsychopathy()
    
    # Display individual profiles
    alice.display_profile()
    bob.display_profile()
    charlie.display_profile()
    
    # Create comparator
    comparator = PsychopathyComparator()
    comparator.add_profile(alice)
    comparator.add_profile(bob)
    comparator.add_profile(charlie)
    
    # Comparisons
    comparator.compare_all()
    comparator.compare_factors()
    comparator.behavioral_predictions()
    comparator.clinical_insights()
    
    # Final summary
    print("\n" + "="*80)
    print("PCL-R SCORE INTERPRETATION GUIDE")
    print("="*80)
    print("""
0-10:    MINIMAL PSYCHOPATHY (Normal range)
         Non-psychopathic individuals with intact empathy and conscience

11-15:   LOW PSYCHOPATHY
         Some concerning traits but generally prosocial behavior

16-20:   LOW-MODERATE PSYCHOPATHY
         Noticeable lack of empathy, some impulsive/irresponsible behavior

21-24:   MODERATE PSYCHOPATHY
         Significant psychopathic traits, risk of manipulation/harm

25-29:   MODERATE-HIGH PSYCHOPATHY
         Strong psychopathic features, high risk for exploitation

30+:     HIGH PSYCHOPATHY (Criminal range)
         Likely to cause serious harm, predatory behavior, no remorse

IMPORTANT NOTES:
• PCL-R is a clinical assessment tool, not a diagnosis
• Psychopathy is distinct from criminality
• Not all psychopaths are criminals; not all criminals are psychopaths
• High psychopathy + low opportunity ≠ high criminality
• Early intervention may reduce harm in moderate cases
• Psychopathy is relatively stable across lifespan
""")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
