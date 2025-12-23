from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Tuple
import math


class MaturityLevel(Enum):
    """Maturity classification levels"""
    HIGHLY_MATURE = "Highly Mature (90-100)"
    MATURE = "Mature (75-89)"
    MODERATELY_MATURE = "Moderately Mature (60-74)"
    IMMATURE = "Immature (40-59)"
    HIGHLY_IMMATURE = "Highly Immature (0-39)"


class WorkReadiness(Enum):
    """Work readiness classification"""
    HIGHLY_READY = "Highly Work Ready (90-100)"
    READY = "Work Ready (75-89)"
    MODERATELY_READY = "Moderately Work Ready (60-74)"
    NEEDS_DEVELOPMENT = "Needs Development (40-59)"
    NOT_READY = "Not Work Ready (0-39)"


@dataclass
class MaturityDimension:
    """A specific dimension of maturity"""
    name: str
    score: float  # 0-100 scale
    description: str
    
    def __str__(self):
        return f"{self.name}: {self.score:.0f}/100 - {self.description}"


class MaturityAssessment:
    """Comprehensive maturity and work readiness assessment"""
    
    def __init__(self, name: str):
        self.name = name
        self.maturity_dimensions: List[MaturityDimension] = []
        self.work_readiness_dimensions: List[MaturityDimension] = []
        self.total_maturity_score = 0
        self.total_work_readiness_score = 0
        self._initialize_dimensions()
    
    def _initialize_dimensions(self):
        """Initialize maturity and work readiness dimensions"""
        pass
    
    def add_maturity_dimension(self, dimension: MaturityDimension):
        """Add a maturity dimension"""
        self.maturity_dimensions.append(dimension)
    
    def add_work_readiness_dimension(self, dimension: MaturityDimension):
        """Add a work readiness dimension"""
        self.work_readiness_dimensions.append(dimension)
    
    def calculate_scores(self):
        """Calculate overall maturity and work readiness scores"""
        if self.maturity_dimensions:
            self.total_maturity_score = sum(d.score for d in self.maturity_dimensions) / len(self.maturity_dimensions)
        
        if self.work_readiness_dimensions:
            self.total_work_readiness_score = sum(d.score for d in self.work_readiness_dimensions) / len(self.work_readiness_dimensions)
    
    def get_maturity_level(self) -> MaturityLevel:
        """Classify maturity level"""
        score = self.total_maturity_score
        if score >= 90:
            return MaturityLevel.HIGHLY_MATURE
        elif score >= 75:
            return MaturityLevel.MATURE
        elif score >= 60:
            return MaturityLevel.MODERATELY_MATURE
        elif score >= 40:
            return MaturityLevel.IMMATURE
        else:
            return MaturityLevel.HIGHLY_IMMATURE
    
    def get_work_readiness_level(self) -> WorkReadiness:
        """Classify work readiness level"""
        score = self.total_work_readiness_score
        if score >= 90:
            return WorkReadiness.HIGHLY_READY
        elif score >= 75:
            return WorkReadiness.READY
        elif score >= 60:
            return WorkReadiness.MODERATELY_READY
        elif score >= 40:
            return WorkReadiness.NEEDS_DEVELOPMENT
        else:
            return WorkReadiness.NOT_READY
    
    def get_strengths(self) -> List[str]:
        """Get top strengths based on dimensions"""
        all_dims = self.maturity_dimensions + self.work_readiness_dimensions
        sorted_dims = sorted(all_dims, key=lambda d: d.score, reverse=True)
        return [d.name for d in sorted_dims[:3]]
    
    def get_weaknesses(self) -> List[str]:
        """Get top weaknesses based on dimensions"""
        all_dims = self.maturity_dimensions + self.work_readiness_dimensions
        sorted_dims = sorted(all_dims, key=lambda d: d.score)
        return [d.name for d in sorted_dims[:3]]
    
    def display_profile(self):
        """Display full assessment profile"""
        self.calculate_scores()
        
        print(f"\n{'='*90}")
        print(f"MATURITY & WORK READINESS ASSESSMENT: {self.name}")
        print(f"{'='*90}")
        
        print(f"\nOVERALL SCORES:")
        print(f"  Maturity Score: {self.total_maturity_score:.1f}/100 - {self.get_maturity_level().value}")
        print(f"  Work Readiness Score: {self.total_work_readiness_score:.1f}/100 - {self.get_work_readiness_level().value}")
        
        # Maturity dimensions
        print(f"\n{'─'*90}")
        print("MATURITY DIMENSIONS:")
        print(f"{'─'*90}")
        for dim in sorted(self.maturity_dimensions, key=lambda d: d.score, reverse=True):
            bar_length = int(dim.score / 10)
            bar = "█" * bar_length + "░" * (10 - bar_length)
            print(f"  {dim.name:35} [{bar}] {dim.score:5.1f}/100")
            print(f"    └─ {dim.description}")
        
        # Work readiness dimensions
        print(f"\n{'─'*90}")
        print("WORK READINESS DIMENSIONS:")
        print(f"{'─'*90}")
        for dim in sorted(self.work_readiness_dimensions, key=lambda d: d.score, reverse=True):
            bar_length = int(dim.score / 10)
            bar = "█" * bar_length + "░" * (10 - bar_length)
            print(f"  {dim.name:35} [{bar}] {dim.score:5.1f}/100")
            print(f"    └─ {dim.description}")
        
        # Strengths and weaknesses
        print(f"\n{'─'*90}")
        print("TOP STRENGTHS:")
        for i, strength in enumerate(self.get_strengths(), 1):
            print(f"  {i}. {strength}")
        
        print(f"\nTOP AREAS FOR DEVELOPMENT:")
        for i, weakness in enumerate(self.get_weaknesses(), 1):
            print(f"  {i}. {weakness}")
        
        print(f"\n{'='*90}\n")


class AliceMaturity(MaturityAssessment):
    """
    Alice: Empathetic Leader
    Expected: Highly mature and work-ready
    """
    
    def __init__(self):
        super().__init__("Alice (Empathetic Leader)")
        self._initialize_dimensions()
    
    def _initialize_dimensions(self):
        """Initialize Alice's dimensions"""
        # Maturity dimensions
        self.add_maturity_dimension(MaturityDimension(
            "Emotional Regulation",
            92,
            "Excellent control over emotions, responds thoughtfully to stress"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Self-Awareness",
            95,
            "Deep understanding of strengths, weaknesses, and impact on others"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Accountability",
            93,
            "Takes responsibility for mistakes, learns from failures"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Perspective Taking",
            96,
            "Can see situations from multiple viewpoints with empathy"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Delayed Gratification",
            90,
            "Willing to invest effort for long-term goals"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Independence",
            88,
            "Self-reliant but also values collaboration and input"
        ))
        
        # Work readiness dimensions
        self.add_work_readiness_dimension(MaturityDimension(
            "Time Management",
            92,
            "Excellent planning and organizational skills"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Reliability",
            95,
            "Consistently delivers on commitments and deadlines"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Communication",
            94,
            "Clear, respectful, and effective in all communication"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Problem-Solving",
            93,
            "Analyzes issues thoroughly and generates quality solutions"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Teamwork & Collaboration",
            96,
            "Excellent at motivating and coordinating team efforts"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Leadership Potential",
            94,
            "Natural leader who inspires and develops others"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Adaptability",
            90,
            "Flexible and handles change constructively"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Ethics",
            97,
            "Strong moral compass, acts with integrity"
        ))


class BobMaturity(MaturityAssessment):
    """
    Bob: Chaotic Jester
    Expected: Highly immature and not work-ready
    """
    
    def __init__(self):
        super().__init__("Bob (Chaotic Jester)")
        self._initialize_dimensions()
    
    def _initialize_dimensions(self):
        """Initialize Bob's dimensions"""
        # Maturity dimensions
        self.add_maturity_dimension(MaturityDimension(
            "Emotional Regulation",
            28,
            "Poor impulse control, reacts emotionally rather than thoughtfully"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Self-Awareness",
            35,
            "Limited insight into impact on others, blames external factors"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Accountability",
            25,
            "Avoids responsibility, makes excuses, doesn't learn from mistakes"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Perspective Taking",
            30,
            "Struggles to understand others' viewpoints, self-centered"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Delayed Gratification",
            22,
            "Seeks immediate rewards, avoids effort or planning"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Independence",
            38,
            "Lacks direction and discipline, dependent on external structure"
        ))
        
        # Work readiness dimensions
        self.add_work_readiness_dimension(MaturityDimension(
            "Time Management",
            25,
            "Disorganized, missed deadlines, poor planning"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Reliability",
            20,
            "Cannot be counted on, frequently absent or unprepared"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Communication",
            32,
            "Inappropriate jokes, doesn't listen, talks too much"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Problem-Solving",
            28,
            "Jumps to solutions without analysis, misses details"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Teamwork & Collaboration",
            24,
            "Disrupts team dynamics, poor cooperation with colleagues"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Leadership Potential",
            18,
            "No demonstrated leadership qualities, lacks credibility"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Adaptability",
            30,
            "Resistant to feedback, poor at adjusting approach"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Ethics",
            35,
            "Questionable integrity, doesn't respect professional norms"
        ))


class CharlieMaturity(MaturityAssessment):
    """
    Charlie: People Pleaser with Narcissistic Traits
    Expected: Moderate-high work readiness but low true maturity
    """
    
    def __init__(self):
        super().__init__("Charlie (People Pleaser)")
        self._initialize_dimensions()
    
    def _initialize_dimensions(self):
        """Initialize Charlie's dimensions"""
        # Maturity dimensions
        self.add_maturity_dimension(MaturityDimension(
            "Emotional Regulation",
            48,
            "Appears controlled but passive-aggressive, holds grudges"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Self-Awareness",
            35,
            "Limited genuine self-reflection, defensive about criticism"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Accountability",
            42,
            "Blames others indirectly, avoids admitting mistakes"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Perspective Taking",
            38,
            "Can appear empathetic but is actually self-focused and calculating"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Delayed Gratification",
            55,
            "Will work toward goals but for selfish validation reasons"
        ))
        
        self.add_maturity_dimension(MaturityDimension(
            "Independence",
            62,
            "Appears independent but depends heavily on others' validation"
        ))
        
        # Work readiness dimensions
        self.add_work_readiness_dimension(MaturityDimension(
            "Time Management",
            78,
            "Good organization but uses it to control and manage impressions"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Reliability",
            75,
            "Delivers projects on time but may cut corners or take credit"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Communication",
            72,
            "Articulate and polished but manipulative, gossips behind scenes"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Problem-Solving",
            76,
            "Competent problem-solver but decisions biased toward personal gain"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Teamwork & Collaboration",
            58,
            "Appears collaborative but undermine teammates when beneficial"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Leadership Potential",
            68,
            "May appear leader-like but lacks integrity and genuine concern for others"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Adaptability",
            65,
            "Adapts well for personal advantage but resists real feedback"
        ))
        
        self.add_work_readiness_dimension(MaturityDimension(
            "Professional Ethics",
            45,
            "Makes ethical compromises when beneficial, lacks true integrity"
        ))


class MaturityComparator:
    """Compare maturity and work readiness across individuals"""
    
    def __init__(self):
        self.assessments: List[MaturityAssessment] = []
    
    def add_assessment(self, assessment: MaturityAssessment):
        """Add an assessment"""
        self.assessments.append(assessment)
    
    def compare_all_scores(self):
        """Compare all scores"""
        print("\n" + "="*90)
        print("OVERALL MATURITY & WORK READINESS COMPARISON")
        print("="*90)
        
        for assessment in sorted(self.assessments, key=lambda a: a.total_maturity_score, reverse=True):
            assessment.calculate_scores()
            
            mat_bar = "█" * int(assessment.total_maturity_score / 10) + "░" * (10 - int(assessment.total_maturity_score / 10))
            work_bar = "█" * int(assessment.total_work_readiness_score / 10) + "░" * (10 - int(assessment.total_work_readiness_score / 10))
            
            print(f"\n{assessment.name}")
            print(f"  Maturity:        [{mat_bar}] {assessment.total_maturity_score:5.1f}/100 ({assessment.get_maturity_level().value})")
            print(f"  Work Readiness:  [{work_bar}] {assessment.total_work_readiness_score:5.1f}/100 ({assessment.get_work_readiness_level().value})")
        
        print("\n" + "="*90 + "\n")
    
    def work_readiness_ranking(self):
        """Rank by work readiness"""
        print("\n" + "="*90)
        print("WORK READINESS RANKING")
        print("="*90)
        
        ranked = sorted(self.assessments, key=lambda a: a.total_work_readiness_score, reverse=True)
        
        for rank, assessment in enumerate(ranked, 1):
            assessment.calculate_scores()
            status = "✓ HIRE" if assessment.total_work_readiness_score >= 75 else "⚠ CONDITIONAL" if assessment.total_work_readiness_score >= 60 else "✗ NOT READY"
            
            print(f"\n{rank}. {assessment.name}")
            print(f"   Work Readiness: {assessment.total_work_readiness_score:.1f}/100")
            print(f"   Maturity: {assessment.total_maturity_score:.1f}/100")
            print(f"   Status: {status}")
        
        print("\n" + "="*90 + "\n")
    
    def job_fit_analysis(self):
        """Analyze job fit for different roles"""
        print("\n" + "="*90)
        print("JOB FIT ANALYSIS - RECOMMENDED POSITIONS")
        print("="*90)
        
        job_recommendations = {
            "Alice": {
                "ideal_roles": [
                    "Executive/Senior Leadership",
                    "Project Manager",
                    "Team Lead",
                    "HR Manager",
                    "Strategic Advisor",
                    "Executive Coach"
                ],
                "suitability": "EXCELLENT - Highly suitable for any role requiring leadership, judgment, or interpersonal skills"
            },
            "Bob": {
                "ideal_roles": [
                    "Entry-level positions",
                    "Individual contributor roles with supervision",
                    "Structured/routine tasks"
                ],
                "suitability": "POOR - Requires extensive supervision and structure; not suitable for decision-making roles"
            },
            "Charlie": {
                "ideal_roles": [
                    "Project Coordinator (with oversight)",
                    "Administrative role",
                    "Mid-level contributor (not leadership)"
                ],
                "suitability": "CAUTION - Can perform technical tasks well but should NOT have authority over others or access to sensitive information"
            }
        }
        
        for assessment in sorted(self.assessments, key=lambda a: a.total_work_readiness_score, reverse=True):
            key = [k for k in job_recommendations.keys() if k.lower() in assessment.name.lower()][0]
            rec = job_recommendations[key]
            
            print(f"\n{assessment.name}")
            print(f"  Suitability: {rec['suitability']}")
            print(f"  Ideal Roles:")
            for role in rec['ideal_roles']:
                print(f"    • {role}")
        
        print("\n" + "="*90 + "\n")
    
    def maturity_insights(self):
        """Provide detailed maturity insights"""
        print("\n" + "="*90)
        print("MATURITY INSIGHTS & DEVELOPMENT")
        print("="*90)
        
        insights = {
            "Alice": {
                "level": "HIGHLY MATURE",
                "profile": """
CHARACTERISTICS:
• Takes responsibility for own actions and outcomes
• Demonstrates genuine empathy and concern for others
• Thoughtful decision-making with long-term perspective
• Accepts feedback constructively and grows from experiences
• Models integrity and ethical behavior consistently
• Manages emotions effectively even under pressure

EMOTIONAL MATURITY: Exceptionally high
PROFESSIONAL MATURITY: Exceptionally high
INTERPERSONAL MATURITY: Exceptionally high

DEVELOPMENT AREAS: Minimal (continues to develop naturally through experience)
POTENTIAL PITFALLS: May become over-critical of less mature individuals"""
            },
            "Bob": {
                "level": "HIGHLY IMMATURE",
                "profile": """
CHARACTERISTICS:
• Blames others for failures and setbacks
• Acts without thinking about consequences
• Takes things personally and reacts emotionally
• Avoids responsibility for mistakes
• Focused on immediate gratification
• Disregards others' feelings and needs

EMOTIONAL MATURITY: Very low (impulse-driven)
PROFESSIONAL MATURITY: Very low (lacks discipline)
INTERPERSONAL MATURITY: Very low (self-centered)

CRITICAL CONCERNS:
• May damage team dynamics and morale
• Creates conflicts and disrupts workflows
• Unreliable in critical situations
• Requires constant supervision

INTERVENTION NEEDED: Significant behavioral coaching or not suitable for employment"""
            },
            "Charlie": {
                "level": "MODERATELY IMMATURE (with competent facade)",
                "profile": """
CHARACTERISTICS:
• Appears mature but lacks genuine self-awareness
• Uses competence as a mask for emotional immaturity
• Manipulates situations for personal advantage
• Holds grudges and seeks subtle revenge
• Struggles to genuinely care about others' wellbeing
• Reactive to perceived slights (though hides it)

EMOTIONAL MATURITY: Low (controlled but unhealthy)
PROFESSIONAL MATURITY: Moderate (functional but self-serving)
INTERPERSONAL MATURITY: Low (manipulative, not authentic)

RED FLAGS:
• Passive-aggressive behavior patterns
• Gossiping and creating office divisions
• Credit-taking and blame-shifting
• Undermining colleagues

INTERVENTION NEEDED: Psychological counseling, clear behavioral expectations, 
or transfer to role with less influence over others"""
            }
        }
        
        for assessment in sorted(self.assessments, key=lambda a: a.total_maturity_score, reverse=True):
            key = [k for k in insights.keys() if k.lower() in assessment.name.lower()][0]
            insight = insights[key]
            
            print(f"\n{assessment.name}")
            print(f"MATURITY LEVEL: {insight['level']}")
            print(insight['profile'])
        
        print("\n" + "="*90 + "\n")
    
    def hiring_recommendation_summary(self):
        """Final hiring recommendations"""
        print("\n" + "="*90)
        print("HIRING RECOMMENDATIONS SUMMARY")
        print("="*90)
        
        for assessment in sorted(self.assessments, key=lambda a: a.total_work_readiness_score, reverse=True):
            assessment.calculate_scores()
            
            print(f"\n{assessment.name}")
            print("─" * 90)
            
            work_score = assessment.total_work_readiness_score
            mat_score = assessment.total_maturity_score
            
            if work_score >= 90 and mat_score >= 90:
                rec = """
RECOMMENDATION: ★★★★★ HIRE IMMEDIATELY
This person is an exceptional candidate who would be valuable in virtually any role.
They combine strong technical/operational capabilities with genuine maturity and
integrity. They would elevate team performance and culture.

SALARY LEVEL: Top-tier
ROLE SUITABILITY: Leadership, management, strategic roles
RISK LEVEL: Minimal
SUPERVISION NEEDED: Minimal (can be trusted with autonomy)"""
            
            elif work_score >= 75 and mat_score >= 75:
                rec = """
RECOMMENDATION: ★★★★ HIRE (Strong candidate)
Reliable and competent professional suitable for most roles. Shows good judgment
and professional behavior. Would be a solid contributor to the team.

SALARY LEVEL: Above-average
ROLE SUITABILITY: Specialist, coordinator, mid-level roles
RISK LEVEL: Low
SUPERVISION NEEDED: Standard"""
            
            elif work_score >= 60 and mat_score >= 60:
                rec = """
RECOMMENDATION: ★★ CONDITIONAL HIRE (with caution)
May be suitable for entry-level or highly structured roles with close supervision.
Be aware of potential issues in judgment or interpersonal dynamics.

SALARY LEVEL: Entry to mid-level
ROLE SUITABILITY: Individual contributor roles with clear structure
RISK LEVEL: Moderate
SUPERVISION NEEDED: Close and ongoing"""
            
            elif work_score >= 40:
                rec = """
RECOMMENDATION: ★ RISKY (Not recommended without significant reservations)
Candidate shows concerning patterns in maturity or reliability. Only consider for
very specific, closely-supervised positions. Be prepared for performance issues.

SALARY LEVEL: Entry-level only
ROLE SUITABILITY: Routine tasks only, supervised roles
RISK LEVEL: High
SUPERVISION NEEDED: Intensive"""
            
            else:
                rec = """
RECOMMENDATION: ✗ DO NOT HIRE
Candidate demonstrates inadequate maturity or work readiness for employment.
Hiring would pose significant risk to team dynamics and outcomes.
Recommend decline or significant intervention/development first.

RISK LEVEL: Very high
SUPERVISION NEEDED: Would require more resources than output would provide"""
            
            print(rec)
        
        print("\n" + "="*90 + "\n")


def main():
    """Main execution"""
    print("\n" + "#"*90)
    print("# MATURITY & WORK READINESS ASSESSMENT")
    print("# Comprehensive evaluation of three personality types")
    print("#"*90)
    
    # Create assessments
    alice = AliceMaturity()
    bob = BobMaturity()
    charlie = CharlieMaturity()
    
    # Display individual profiles
    alice.display_profile()
    bob.display_profile()
    charlie.display_profile()
    
    # Create comparator
    comparator = MaturityComparator()
    comparator.add_assessment(alice)
    comparator.add_assessment(bob)
    comparator.add_assessment(charlie)
    
    # Comprehensive analysis
    comparator.compare_all_scores()
    comparator.work_readiness_ranking()
    comparator.job_fit_analysis()
    comparator.maturity_insights()
    comparator.hiring_recommendation_summary()
    
    # Educational summary
    print("\n" + "="*90)
    print("MATURITY FRAMEWORK - KEY DEFINITIONS")
    print("="*90)
    print("""
EMOTIONAL MATURITY:
The ability to understand, manage, and express emotions appropriately. 
Includes emotional regulation, self-awareness, and impulse control.

PROFESSIONAL MATURITY:
Demonstrating reliability, accountability, and professional standards.
Includes time management, meeting commitments, and ethical behavior.

INTERPERSONAL MATURITY:
The capacity for genuine relationships, empathy, and consideration for others.
Includes perspective-taking, authentic communication, and collaborative behavior.

WORK READINESS:
The overall preparedness and suitability for employment, encompassing skills,
behavior, judgment, and reliability needed for workplace success.

KEY DISTINCTION:
⚠️  A person can appear work-ready but be emotionally immature
    (High work performance, low genuine maturity = Red flag for leadership roles)

✓  True work readiness combines capability with genuine maturity
    (Consistent high performance + authentic growth mindset = Reliable leader)
""")
    print("="*90 + "\n")


if __name__ == "__main__":
    main()
