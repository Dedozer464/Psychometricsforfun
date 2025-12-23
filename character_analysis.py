#!/usr/bin/env python3
"""
Character Personality Analysis & Longevity Prediction System
This script analyzes character traits and predicts life expectancy based on personality and lifestyle factors.
"""

import pandas as pd
from dataclasses import dataclass
from typing import List, Dict, Tuple
import statistics

# ============================================================================
# CHARACTER CLASS AND STRUCTURE
# ============================================================================

@dataclass
class Character:
    """Class to represent a character with traits and lifestyle factors"""
    name: str
    age: int
    traits: List[str]
    lifestyle_factors: List[str]
    
    def __post_init__(self):
        """Normalize all strings to lowercase for comparison"""
        self.traits = [trait.lower().replace(" ", "_") for trait in self.traits]
        self.lifestyle_factors = [factor.lower().replace(" ", "_") for factor in self.lifestyle_factors]


# ============================================================================
# SCORING AND ASSESSMENT FUNCTIONS
# ============================================================================

def score_maturity(traits: List[str]) -> float:
    """
    Score character maturity on a 0-100 scale
    
    Args:
        traits: List of character traits
        
    Returns:
        Maturity score (0-100)
    """
    maturity_score = 50  # Base score
    
    # Positive maturity indicators
    positive_traits = {
        "caring": 15,
        "nurturing": 15,
        "analytical": 12,
        "sympathetic": 14,
        "helpful": 12,
        "observant": 10,
        "emotionally_intelligent": 18,
        "loves_everybody": 16,
        "curious": 10
    }
    
    # Negative maturity indicators
    negative_traits = {
        "gossips_a_lot": -20,
        "gossips": -20,
        "passive_aggressive": -25,
        "obsessive": -15,
        "obsessive_about_people": -15,
        "narcissistic": -30,
        "judgmental": -18,
        "looks_down_on_people": -20,
        "substance_abuse": -30,
        "smokes_marijuana": -12,
        "hates_men": -18,
        "not_so_observant": -10,
        "dismissive": -15
    }
    
    # Check for positive traits
    for trait in traits:
        if trait in positive_traits:
            maturity_score += positive_traits[trait]
    
    # Check for negative traits
    for trait in traits:
        if trait in negative_traits:
            maturity_score += negative_traits[trait]
    
    # Clamp score between 0 and 100
    maturity_score = max(0, min(100, maturity_score))
    return maturity_score


def assess_personality(traits: List[str]) -> List[str]:
    """
    Assess personality types based on traits
    
    Args:
        traits: List of character traits
        
    Returns:
        List of personality type classifications
    """
    personality_types = []
    
    if any(t in traits for t in ["caring", "nurturing", "helpful", "loves_everybody"]):
        personality_types.append("Caregiver")
    
    if any(t in traits for t in ["analytical", "curious", "observant"]):
        personality_types.append("Analyst")
    
    if any(t in traits for t in ["funny", "talkative"]):
        personality_types.append("Entertainer")
    
    if any(t in traits for t in ["emotional", "sympathetic", "nervous"]):
        personality_types.append("Sensitive")
    
    if any(t in traits for t in ["passive_aggressive", "gossips", "gossips_a_lot", "judgmental", "looks_down_on_people"]):
        personality_types.append("Critic")
    
    if any(t in traits for t in ["loves_everybody", "nurturing"]):
        personality_types.append("Altruist")
    
    return personality_types if personality_types else ["Neutral"]


def calculate_character_value(maturity_score: float) -> str:
    """
    Determine overall character value based on maturity
    
    Args:
        maturity_score: The maturity score (0-100)
        
    Returns:
        Character value rating
    """
    if maturity_score >= 75:
        return "Very High"
    elif maturity_score >= 60:
        return "High"
    elif maturity_score >= 40:
        return "Moderate"
    elif maturity_score >= 25:
        return "Low"
    else:
        return "Very Low"


def calculate_health_risk(age: int, lifestyle_factors: List[str]) -> float:
    """
    Calculate health risk score based on age and lifestyle
    
    Args:
        age: Current age
        lifestyle_factors: List of lifestyle factors
        
    Returns:
        Health risk score (0-100)
    """
    # Base risk increases with age
    base_risk = (age / 100) * 50
    risk_score = base_risk
    
    # Lifestyle risk factors
    risk_mapping = {
        "smokes_marijuana": 10,
        "smokes_cigarettes": 20,
        "heavy_alcohol": 15,
        "alcohol_abuse": 18,
        "sedentary": 12,
        "poor_diet": 8,
        "social_isolation": 15,
        "obsessive_thoughts": 10,
        "hates_men": 5,  # Negative emotions increase stress
        "passive_aggressive": 8,  # Internal conflict increases health risk
    }
    
    # Protective factors
    protective_mapping = {
        "active": -8,
        "exercises_regularly": -10,
        "good_diet": -8,
        "healthy_eating": -10,
        "strong_relationships": -12,
        "caring_for_others": -10,
        "low_stress": -8,
        "loves_everybody": -8,
        "nurturing": -6,
        "social": -5,
        "talkative": -4
    }
    
    # Apply risk factors
    for factor in lifestyle_factors:
        if factor in risk_mapping:
            risk_score += risk_mapping[factor]
        if factor in protective_mapping:
            risk_score += protective_mapping[factor]
    
    # Clamp score between 5 and 95
    risk_score = max(5, min(95, risk_score))
    return risk_score


def get_risk_level(risk_score: float) -> str:
    """
    Classify risk level based on risk score
    
    Args:
        risk_score: Health risk score (0-100)
        
    Returns:
        Risk level classification
    """
    if risk_score < 30:
        return "Low Risk"
    elif risk_score < 60:
        return "Moderate Risk"
    else:
        return "High Risk"


def predict_longevity(age: int, health_risk_score: float, maturity_score: float) -> Dict[str, float]:
    """
    Predict longevity based on age, health risk, and maturity
    
    Args:
        age: Current age
        health_risk_score: Health risk score (0-100)
        maturity_score: Maturity score (0-100)
        
    Returns:
        Dictionary with longevity predictions
    """
    # Base life expectancy for different countries (using global average)
    base_life_expectancy = 78
    
    # Calculate remaining years
    years_remaining = base_life_expectancy - age
    
    # Risk adjustment (higher risk = fewer years)
    risk_adjustment = (health_risk_score / 100) * -25
    years_remaining += risk_adjustment
    
    # Maturity bonus (more mature = better health decisions)
    maturity_bonus = (maturity_score / 100) * 12
    years_remaining += maturity_bonus
    
    # Ensure minimum realistic value
    years_remaining = max(1, years_remaining)
    
    predicted_age_at_death = age + years_remaining
    
    return {
        "years_remaining": years_remaining,
        "predicted_death_age": predicted_age_at_death,
        "confidence": "Medium (based on general health patterns)"
    }


# ============================================================================
# CHARACTER ANALYSIS
# ============================================================================

def analyze_character(character: Character) -> Dict:
    """
    Perform comprehensive analysis on a character
    
    Args:
        character: Character object to analyze
        
    Returns:
        Dictionary containing all analysis results
    """
    maturity = score_maturity(character.traits)
    personality = assess_personality(character.traits)
    character_value = calculate_character_value(maturity)
    health_risk = calculate_health_risk(character.age, character.lifestyle_factors)
    risk_level = get_risk_level(health_risk)
    longevity = predict_longevity(character.age, health_risk, maturity)
    
    return {
        "name": character.name,
        "age": character.age,
        "traits": character.traits,
        "lifestyle_factors": character.lifestyle_factors,
        "maturity_score": maturity,
        "personality_types": personality,
        "character_value": character_value,
        "health_risk_score": health_risk,
        "risk_level": risk_level,
        "years_remaining": longevity["years_remaining"],
        "predicted_death_age": longevity["predicted_death_age"],
        "confidence": longevity["confidence"]
    }


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def print_character_analysis(analysis: Dict) -> None:
    """
    Print formatted character analysis
    
    Args:
        analysis: Dictionary containing character analysis results
    """
    print("\n" + "="*80)
    print(f"CHARACTER PROFILE ANALYSIS: {analysis['name'].upper()}")
    print("="*80 + "\n")
    
    print("BASIC INFORMATION:")
    print(f"  Age: {analysis['age']} years old")
    print(f"  Traits: {', '.join(analysis['traits'])}")
    print(f"  Lifestyle Factors: {', '.join(analysis['lifestyle_factors'])}")
    print()
    
    print("CHARACTER ASSESSMENT:")
    print(f"  Maturity Score: {analysis['maturity_score']:.1f}/100")
    print(f"  Personality Types: {', '.join(analysis['personality_types'])}")
    print(f"  Overall Character Value: {analysis['character_value']}")
    print()
    
    print("HEALTH & LONGEVITY PREDICTION:")
    print(f"  Health Risk Score: {analysis['health_risk_score']:.1f}/100")
    print(f"  Risk Level: {analysis['risk_level']}")
    print(f"  Predicted Years Remaining: {analysis['years_remaining']:.1f} years")
    print(f"  Predicted Age at Death: {analysis['predicted_death_age']:.1f} years old")
    print(f"  Confidence Level: {analysis['confidence']}")
    print()


def create_comparison_table(analyses: List[Dict]) -> pd.DataFrame:
    """
    Create a comparison DataFrame for all characters
    
    Args:
        analyses: List of analysis dictionaries
        
    Returns:
        Pandas DataFrame with comparison data
    """
    data = []
    for analysis in analyses:
        data.append({
            "Name": analysis["name"],
            "Age": analysis["age"],
            "Maturity Score": round(analysis["maturity_score"], 1),
            "Character Value": analysis["character_value"],
            "Health Risk": round(analysis["health_risk_score"], 1),
            "Risk Level": analysis["risk_level"],
            "Years Remaining": round(analysis["years_remaining"], 1),
            "Predicted Death Age": round(analysis["predicted_death_age"], 1)
        })
    
    df = pd.DataFrame(data)
    # Sort by predicted death age (descending)
    df = df.sort_values("Predicted Death Age", ascending=False).reset_index(drop=True)
    df["Rank"] = range(1, len(df) + 1)
    
    return df[["Rank", "Name", "Age", "Maturity Score", "Character Value", "Health Risk", "Risk Level", "Predicted Death Age"]]


def print_comparison_analysis(df: pd.DataFrame, analyses: List[Dict]) -> None:
    """
    Print comparative analysis of all characters
    
    Args:
        df: Comparison DataFrame
        analyses: List of analysis dictionaries
    """
    print("\n" + "="*80)
    print("COMPARATIVE LONGEVITY RANKING")
    print("="*80 + "\n")
    
    print("Ranking by Predicted Longevity (Longest to Shortest):\n")
    print(df.to_string(index=False))
    print()
    
    print("\nKEY INSIGHTS:\n")
    
    # Most likely to live longest
    longest_idx = df["Predicted Death Age"].idxmax()
    longest_char = df.iloc[longest_idx]
    print(f"1. Most Likely to Live Longest: {longest_char['Name']} "
          f"(predicted to {longest_char['Predicted Death Age']:.1f} years old)")
    
    # Most at risk
    highest_risk_idx = df["Health Risk"].idxmax()
    highest_risk_char = df.iloc[highest_risk_idx]
    print(f"2. Most at Risk: {highest_risk_char['Name']} "
          f"(health risk score: {highest_risk_char['Health Risk']:.1f})")
    
    # Most mature
    maturity_scores = [a["maturity_score"] for a in analyses]
    max_maturity_idx = maturity_scores.index(max(maturity_scores))
    most_mature_char = df.iloc[max_maturity_idx]
    print(f"3. Most Mature: {most_mature_char['Name']} "
          f"(maturity score: {df.iloc[max_maturity_idx]['Maturity Score']:.1f})")
    
    # Best character value
    value_order = {"Very High": 5, "High": 4, "Moderate": 3, "Low": 2, "Very Low": 1}
    best_value_idx = df["Character Value"].map(value_order).idxmax()
    best_value_char = df.iloc[best_value_idx]
    print(f"4. Best Character Value: {best_value_char['Name']} "
          f"({best_value_char['Character Value']})")
    
    # Lowest health risk
    lowest_risk_idx = df["Health Risk"].idxmin()
    lowest_risk_char = df.iloc[lowest_risk_idx]
    print(f"5. Lowest Health Risk: {lowest_risk_char['Name']} "
          f"(health risk score: {lowest_risk_char['Health Risk']:.1f})")
    
    print("\n" + "="*80 + "\n")


# ============================================================================
# DETAILED PERSONALITY ANALYSIS
# ============================================================================

def print_detailed_traits_analysis(analyses: List[Dict]) -> None:
    """
    Print detailed analysis of traits for each character
    
    Args:
        analyses: List of analysis dictionaries
    """
    print("\n" + "="*80)
    print("DETAILED TRAIT ANALYSIS")
    print("="*80 + "\n")
    
    for analysis in analyses:
        print(f"\n{analysis['name'].upper()}:")
        print(f"  Personality Types: {', '.join(analysis['personality_types'])}")
        
        positive_traits = []
        negative_traits = []
        neutral_traits = []
        
        positive_list = {"caring", "nurturing", "analytical", "sympathetic", "helpful", 
                        "observant", "emotionally_intelligent", "loves_everybody", "curious", 
                        "funny", "talkative"}
        negative_list = {"gossips_a_lot", "gossips", "passive_aggressive", "obsessive", 
                        "obsessive_about_people", "narcissistic", "judgmental", 
                        "looks_down_on_people", "substance_abuse", "smokes_marijuana", 
                        "hates_men", "not_so_observant", "dismissive", "emotional", "nervous"}
        
        for trait in analysis["traits"]:
            if trait in positive_list:
                positive_traits.append(trait)
            elif trait in negative_list:
                negative_traits.append(trait)
            else:
                neutral_traits.append(trait)
        
        if positive_traits:
            print(f"  ✓ Positive Traits: {', '.join(positive_traits)}")
        if negative_traits:
            print(f"  ✗ Negative Traits: {', '.join(negative_traits)}")
        if neutral_traits:
            print(f"  • Neutral Traits: {', '.join(neutral_traits)}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    
    print("\n" + "="*80)
    print("CHARACTER PERSONALITY ANALYSIS & LONGEVITY PREDICTION SYSTEM")
    print("="*80)
    
    # ========================================================================
    # CREATE CHARACTER PROFILES
    # ========================================================================
    
    human1 = Character(
        name="Human 1",
        age=25,
        traits=["Likes_food", "Hates_men", "Gossips_a_lot", "Not_so_observant", 
                "Obsessive_about_people"],
        lifestyle_factors=["Smokes_marijuana", "Social"]
    )
    
    human2 = Character(
        name="Human 2",
        age=50,
        traits=["Caring", "Nurturing", "Loves_everybody", "Talkative", "Helpful"],
        lifestyle_factors=["Strong_relationships", "Caring_for_others", "Active", "Low_stress"]
    )
    
    human3 = Character(
        name="Human 3 (Feminine Man)",
        age=35,
        traits=["Emotional", "Passive_aggressive", "Likes_to_gossip", 
                "Looks_down_on_people"],
        lifestyle_factors=["Social", "Obsessive_thoughts"]
    )
    
    human4 = Character(
        name="Human 4",
        age=24,
        traits=["Funny", "Curious", "Analytical", "Very_sympathetic", "Nervous"],
        lifestyle_factors=["Active", "Good_diet", "Social", "Low_stress"]
    )
    
    characters = [human1, human2, human3, human4]
    
    # ========================================================================
    # PERFORM ANALYSIS
    # ========================================================================
    
    analyses = [analyze_character(char) for char in characters]
    
    # Display individual character analyses
    for analysis in analyses:
        print_character_analysis(analysis)
    
    # Create and display comparison table
    comparison_df = create_comparison_table(analyses)
    print_comparison_analysis(comparison_df, analyses)
    
    # Detailed trait analysis
    print_detailed_traits_analysis(analyses)
    
    # ========================================================================
    # STATISTICAL SUMMARY
    # ========================================================================
    
    print("\n" + "="*80)
    print("STATISTICAL SUMMARY")
    print("="*80 + "\n")
    
    maturity_scores = [a["maturity_score"] for a in analyses]
    risk_scores = [a["health_risk_score"] for a in analyses]
    predicted_ages = [a["predicted_death_age"] for a in analyses]
    
    print(f"Average Maturity Score: {statistics.mean(maturity_scores):.1f}/100")
    print(f"Average Health Risk Score: {statistics.mean(risk_scores):.1f}/100")
    print(f"Average Predicted Death Age: {statistics.mean(predicted_ages):.1f} years")
    print(f"Median Predicted Death Age: {statistics.median(predicted_ages):.1f} years")
    print(f"Life Expectancy Range: {min(predicted_ages):.1f} - {max(predicted_ages):.1f} years")
    
    print("\n" + "="*80 + "\n")
    
    # ========================================================================
    # SAVE RESULTS TO CSV
    # ========================================================================
    
    try:
        comparison_df.to_csv("character_analysis_results.csv", index=False)
        print("✓ Results saved to 'character_analysis_results.csv'")
    except Exception as e:
        print(f"Could not save CSV: {e}")


if __name__ == "__main__":
    main()
