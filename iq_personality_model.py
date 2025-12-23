from enum import Enum
from dataclasses import dataclass
from typing import List, Dict
import math


class IQCategory(Enum):
    GENIUS = "Genius (140+)"
    VERY_SUPERIOR = "Very Superior (130-139)"
    SUPERIOR = "Superior (120-129)"
    HIGH_AVERAGE = "High Average (110-119)"
    AVERAGE = "Average (90-109)"
    LOW_AVERAGE = "Low Average (80-89)"
    BORDERLINE = "Borderline (70-79)"


@dataclass
class CognitiveSkill:
    """Represents a specific cognitive skill"""
    name: str
    score: float  # 0-100 scale
    
    def __str__(self):
        return f"{self.name}: {self.score:.1f}"


class IQProfile:
    """Detailed IQ profile for a person"""
    
    def __init__(self, name: str, iq_score: int):
        self.name = name
        self.iq_score = iq_score
        self.category = self._categorize_iq(iq_score)
        self.percentile = self._calculate_percentile(iq_score)
        self.cognitive_skills: List[CognitiveSkill] = []
        self.strengths: List[str] = []
        self.weaknesses: List[str] = []
    
    @staticmethod
    def _categorize_iq(iq: int) -> IQCategory:
        """Categorize IQ score"""
        if iq >= 140:
            return IQCategory.GENIUS
        elif iq >= 130:
            return IQCategory.VERY_SUPERIOR
        elif iq >= 120:
            return IQCategory.SUPERIOR
        elif iq >= 110:
            return IQCategory.HIGH_AVERAGE
        elif iq >= 90:
            return IQCategory.AVERAGE
        elif iq >= 80:
            return IQCategory.LOW_AVERAGE
        else:
            return IQCategory.BORDERLINE
    
    @staticmethod
    def _calculate_percentile(iq: int) -> float:
        """Calculate percentile rank (approximate)"""
        # Using standard normal distribution
        z_score = (iq - 100) / 15
        percentile = (1 + math.erf(z_score / math.sqrt(2))) / 2
        return round(percentile * 100, 2)
    
    def add_cognitive_skill(self, skill: CognitiveSkill):
        """Add a cognitive skill"""
        self.cognitive_skills.append(skill)
    
    def add_strength(self, strength: str):
        """Add a cognitive strength"""
        self.strengths.append(strength)
    
    def add_weakness(self, weakness: str):
        """Add a cognitive weakness"""
        self.weaknesses.append(weakness)
    
    def display_profile(self):
        """Display IQ profile"""
        print(f"\n{'='*60}")
        print(f"IQ PROFILE: {self.name}")
        print(f"{'='*60}")
        print(f"IQ Score: {self.iq_score}")
        print(f"Category: {self.category.value}")
        print(f"Percentile Rank: {self.percentile}%")
        print(f"{'='*60}")
        
        print("\nCognitive Skills:")
        for skill in self.cognitive_skills:
            self._display_skill_bar(skill)
        
        print("\nStrengths:")
        for strength in self.strengths:
            print(f"  ✓ {strength}")
        
        print("\nWeaknesses:")
        for weakness in self.weaknesses:
            print(f"  ✗ {weakness}")
        
        print(f"{'='*60}\n")
    
    @staticmethod
    def _display_skill_bar(skill: CognitiveSkill):
        """Display a skill bar"""
        score = int(skill.score / 10)
        bar = "█" * score + "░" * (10 - score)
        print(f"  {skill.name:25} [{bar}] {skill.score:.1f}/100")


class AliceEmpathetic(IQProfile):
    """
    Alice: Empathetic Leader
    IQ: 135 (Very Superior)
    High in emotional intelligence and logical reasoning
    """
    
    def __init__(self):
        super().__init__("Alice (Empathetic Leader)", 135)
        self._initialize_profile()
    
    def _initialize_profile(self):
        """Initialize Alice's cognitive profile"""
        # Cognitive skills
        self.add_cognitive_skill(CognitiveSkill("Verbal Reasoning", 92))
        self.add_cognitive_skill(CognitiveSkill("Logical Reasoning", 90))
        self.add_cognitive_skill(CognitiveSkill("Spatial Reasoning", 78))
        self.add_cognitive_skill(CognitiveSkill("Mathematical Ability", 85))
        self.add_cognitive_skill(CognitiveSkill("Processing Speed", 88))
        self.add_cognitive_skill(CognitiveSkill("Memory Retention", 91))
        self.add_cognitive_skill(CognitiveSkill("Emotional Understanding", 95))
        self.add_cognitive_skill(CognitiveSkill("Social Cognition", 93))
        
        # Strengths
        self.add_strength("Excellent communication and articulation")
        self.add_strength("Strong emotional intelligence and empathy")
        self.add_strength("Superior leadership and interpersonal skills")
        self.add_strength("Ability to see complex social dynamics")
        self.add_strength("Strategic thinking in people management")
        self.add_strength("Can understand and predict human behavior")
        
        # Weaknesses
        self.add_weakness("Slightly weaker in pure abstract/spatial thinking")
        self.add_weakness("May over-analyze social situations")
        self.add_weakness("Can be influenced by emotions in decision-making")
        self.add_weakness("Tendency to be self-congratulatory")
    
    def solve_problem(self, problem: str) -> str:
        """How Alice would solve different problems"""
        solutions = {
            "conflict": "Alice would analyze the emotional and logical components of the conflict, find the underlying needs, and propose a solution that satisfies all parties rationally and emotionally.",
            "project": "Alice would break down the project into components, assign them strategically based on team strengths, and create a comprehensive plan with built-in emotional buy-in.",
            "learning": "Alice would quickly grasp new concepts, understand their application, and teach them to others with clarity and patience.",
            "innovation": "Alice would generate creative solutions by combining logical analysis with empathetic understanding of user needs."
        }
        return solutions.get(problem, "Alice applies her superior intellect and emotional awareness to find optimal solutions.")
    
    def make_decision(self, scenario: str) -> str:
        """How Alice makes decisions"""
        decisions = {
            "promotion": "After careful analysis of qualifications, merit, and team dynamics, Alice would choose the best candidate while considering team morale.",
            "investment": "Alice would conduct thorough research, analyze risk factors, and make a calculated decision with emotional detachment.",
            "conflict_resolution": "Alice would mediate by understanding all perspectives and facilitating a rational, mutually beneficial resolution.",
            "strategy": "Alice would develop long-term strategies that balance business logic with human factors."
        }
        return decisions.get(scenario, "Alice makes well-reasoned, emotionally intelligent decisions.")


class BobChaotic(IQProfile):
    """
    Bob: Chaotic Jester
    IQ: 105 (Average)
    Average intelligence but with poor judgment and impulse control
    """
    
    def __init__(self):
        super().__init__("Bob (Chaotic Jester)", 105)
        self._initialize_profile()
    
    def _initialize_profile(self):
        """Initialize Bob's cognitive profile"""
        # Cognitive skills
        self.add_cognitive_skill(CognitiveSkill("Verbal Reasoning", 72))
        self.add_cognitive_skill(CognitiveSkill("Logical Reasoning", 68))
        self.add_cognitive_skill(CognitiveSkill("Spatial Reasoning", 80))
        self.add_cognitive_skill(CognitiveSkill("Mathematical Ability", 65))
        self.add_cognitive_skill(CognitiveSkill("Processing Speed", 78))
        self.add_cognitive_skill(CognitiveSkill("Memory Retention", 70))
        self.add_cognitive_skill(CognitiveSkill("Creative Thinking", 87))
        self.add_cognitive_skill(CognitiveSkill("Practical Problem Solving", 75))
        
        # Strengths
        self.add_strength("Quick, creative thinking")
        self.add_strength("Good spatial awareness and visualization")
        self.add_strength("Natural humor and comedic timing")
        self.add_strength("Can think outside the box")
        self.add_strength("Good at improvisation")
        
        # Weaknesses
        self.add_weakness("Weak logical reasoning and analysis")
        self.add_weakness("Poor planning and foresight")
        self.add_weakness("Low verbal articulation")
        self.add_weakness("Difficulty with complex math and calculations")
        self.add_weakness("Poor impulse control")
        self.add_weakness("Struggles with abstract concepts")
        self.add_weakness("Limited working memory")
    
    def solve_problem(self, problem: str) -> str:
        """How Bob would solve different problems"""
        solutions = {
            "conflict": "Bob would try to make a joke to lighten the mood, but might not understand the deeper issues or provide a real solution.",
            "project": "Bob would jump into action without much planning, make changes on the fly, and often miss important details.",
            "learning": "Bob would struggle with abstract concepts but learn best through hands-on, practical experience.",
            "innovation": "Bob would have spontaneous ideas but struggle to develop them into actual implementations or think through consequences."
        }
        return solutions.get(problem, "Bob approaches problems impulsively with creative but often poorly thought-out solutions.")
    
    def make_decision(self, scenario: str) -> str:
        """How Bob makes decisions"""
        decisions = {
            "promotion": "Bob might choose whoever is the most fun to hang out with, not necessarily the most qualified.",
            "investment": "Bob would make a snap decision without analyzing risks, possibly losing money.",
            "conflict_resolution": "Bob would avoid the real issue and try to distract everyone with humor.",
            "strategy": "Bob wouldn't think beyond the immediate future and would make inconsistent decisions."
        }
        return decisions.get(scenario, "Bob makes impulsive, poorly thought-out decisions.")


class CharlieCharlatan(IQProfile):
    """
    Charlie: People Pleaser with Narcissistic Traits
    IQ: 118 (High Average)
    Above average intelligence used to manipulate and gain validation
    """
    
    def __init__(self):
        super().__init__("Charlie (People Pleaser)", 118)
        self._initialize_profile()
    
    def _initialize_profile(self):
        """Initialize Charlie's cognitive profile"""
        # Cognitive skills
        self.add_cognitive_skill(CognitiveSkill("Verbal Reasoning", 88))
        self.add_cognitive_skill(CognitiveSkill("Logical Reasoning", 80))
        self.add_cognitive_skill(CognitiveSkill("Spatial Reasoning", 82))
        self.add_cognitive_skill(CognitiveSkill("Mathematical Ability", 81))
        self.add_cognitive_skill(CognitiveSkill("Processing Speed", 85))
        self.add_cognitive_skill(CognitiveSkill("Memory Retention", 89))
        self.add_cognitive_skill(CognitiveSkill("Manipulation Skills", 92))
        self.add_cognitive_skill(CognitiveSkill("Social Strategy", 90))
        
        # Strengths
        self.add_strength("Good verbal skills and persuasion")
        self.add_strength("Excellent at reading social cues (for manipulation)")
        self.add_strength("Organized and detail-oriented")
        self.add_strength("Can appear competent and reliable")
        self.add_strength("Good at managing impressions")
        self.add_strength("Strategic thinking for personal gain")
        
        # Weaknesses
        self.add_weakness("Uses intelligence for manipulation, not constructive purposes")
        self.add_weakness("Passive-aggressive communication")
        self.add_weakness("Can't genuinely empathize")
        self.add_weakness("Holds grudges and keeps score")
        self.add_weakness("Lacks genuine humility despite intelligence")
        self.add_weakness("May underestimate others while appearing supportive")
    
    def solve_problem(self, problem: str) -> str:
        """How Charlie would solve different problems"""
        solutions = {
            "conflict": "Charlie would appear to help resolve the conflict but would subtly ensure they get credit and others feel they owe them.",
            "project": "Charlie would take charge, manage all details, and constantly remind everyone how critical their contributions were.",
            "learning": "Charlie would learn quickly to appear knowledgeable and use that knowledge to position themselves as superior.",
            "innovation": "Charlie would take others' ideas, develop them competently, and claim primary credit while appearing humble."
        }
        return solutions.get(problem, "Charlie uses intelligent problem-solving primarily to advance their own standing.")
    
    def make_decision(self, scenario: str) -> str:
        """How Charlie makes decisions"""
        decisions = {
            "promotion": "Charlie would consider factors that ensure they look good, might subtly undermine competitors.",
            "investment": "Charlie would calculate risks well but might make decisions based on personal prestige rather than pure logic.",
            "conflict_resolution": "Charlie would mediate in a way that makes them look like the hero and puts others in their debt.",
            "strategy": "Charlie would develop strategies that advance their position while appearing to serve the group."
        }
        return decisions.get(scenario, "Charlie makes calculated decisions that benefit their status and validation.")


class IQComparator:
    """Compare IQ profiles and behaviors"""
    
    def __init__(self):
        self.profiles: List[IQProfile] = []
    
    def add_profile(self, profile: IQProfile):
        """Add an IQ profile"""
        self.profiles.append(profile)
    
    def compare_all(self):
        """Display comparison of all profiles"""
        print("\n" + "="*80)
        print("IQ SCORE COMPARISON")
        print("="*80)
        
        for profile in sorted(self.profiles, key=lambda p: p.iq_score, reverse=True):
            bar_length = int(profile.iq_score / 10)
            bar = "█" * bar_length + "░" * (15 - bar_length)
            print(f"{profile.name:30} [{bar}] {profile.iq_score} | {profile.category.value}")
        
        print("="*80 + "\n")
    
    def problem_solving_comparison(self, problem: str):
        """Compare how each person solves a problem"""
        print("\n" + "="*80)
        print(f"PROBLEM-SOLVING APPROACH: {problem.upper()}")
        print("="*80)
        
        for profile in self.profiles:
            print(f"\n{profile.name} (IQ: {profile.iq_score}):")
            print(f"  {profile.solve_problem(problem)}")
        
        print("\n" + "="*80 + "\n")
    
    def decision_making_comparison(self, scenario: str):
        """Compare how each person makes decisions"""
        print("\n" + "="*80)
        print(f"DECISION-MAKING SCENARIO: {scenario.upper()}")
        print("="*80)
        
        for profile in self.profiles:
            print(f"\n{profile.name} (IQ: {profile.iq_score}):")
            print(f"  {profile.make_decision(scenario)}")
        
        print("\n" + "="*80 + "\n")
    
    def cognitive_strength_comparison(self):
        """Compare cognitive strengths across all profiles"""
        print("\n" + "="*80)
        print("COGNITIVE STRENGTHS COMPARISON")
        print("="*80)
        
        for profile in self.profiles:
            print(f"\n{profile.name}:")
            skill_names = [skill.name for skill in profile.cognitive_skills]
            max_skill = max(profile.cognitive_skills, key=lambda s: s.score)
            min_skill = min(profile.cognitive_skills, key=lambda s: s.score)
            
            print(f"  Highest Skill: {max_skill.name} ({max_skill.score:.1f}/100)")
            print(f"  Lowest Skill: {min_skill.name} ({min_skill.score:.1f}/100)")
            print(f"  Average Score: {sum(s.score for s in profile.cognitive_skills) / len(profile.cognitive_skills):.1f}/100")
        
        print("\n" + "="*80 + "\n")


def main():
    """Main execution"""
    print("\n" + "#"*80)
    print("# INTELLIGENT QUOTIENT (IQ) ANALYSIS OF THREE PERSONALITY TYPES")
    print("#"*80)
    
    # Create IQ profiles
    alice = AliceEmpathetic()
    bob = BobChaotic()
    charlie = CharlieCharlatan()
    
    # Display individual profiles
    alice.display_profile()
    bob.display_profile()
    charlie.display_profile()
    
    # Create comparator
    comparator = IQComparator()
    comparator.add_profile(alice)
    comparator.add_profile(bob)
    comparator.add_profile(charlie)
    
    # Comparisons
    comparator.compare_all()
    comparator.cognitive_strength_comparison()
    
    # Problem-solving scenarios
    problems = ["conflict", "project", "learning", "innovation"]
    for problem in problems:
        comparator.problem_solving_comparison(problem)
    
    # Decision-making scenarios
    scenarios = ["promotion", "investment", "conflict_resolution", "strategy"]
    for scenario in scenarios:
        comparator.decision_making_comparison(scenario)
    
    # Summary analysis
    print("\n" + "="*80)
    print("SUMMARY ANALYSIS")
    print("="*80)
    
    print("\nAlice (IQ: 135 - Very Superior):")
    print("  • Superior overall intelligence with exceptional emotional understanding")
    print("  • Best equipped to lead, teach, and solve complex human-centered problems")
    print("  • Tends to think strategically and consider long-term consequences")
    print("  • Weakness: May be self-congratulatory and over-analytical")
    
    print("\nBob (IQ: 105 - Average):")
    print("  • Average intelligence with creative but impulsive thinking patterns")
    print("  • Good at humor and practical tasks, weak in abstract reasoning")
    print("  • Likely to act first, think later - prone to poor decisions")
    print("  • Strength: Natural creativity and improvisation")
    
    print("\nCharlie (IQ: 118 - High Average):")
    print("  • Above-average intelligence used primarily for personal advancement")
    print("  • Strong in manipulation and impression management")
    print("  • Competent but motivated by validation and status")
    print("  • Weakness: Lacks genuine empathy despite high social cognition")
    
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()
