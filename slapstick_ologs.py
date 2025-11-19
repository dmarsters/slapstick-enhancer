"""
Slapstick Comedy Olog System
Three-layer architecture: Categorical taxonomy → Slapstick profiles → MCP interface

This olog formalizes the semantic relationships between:
- Subject types (architecture, portrait, still_life, etc.)
- Emotional tones (playful, tense, absurd, whimsical, etc.)
- Visual priorities (scale, physics, repetition, clarity, etc.)
- Intensity levels (subtle, moderate, strong, extreme)
- Slapstick parameters (exaggeration, timing, physical, ruleOfThree, readability, tension)

Using category theory principles to create deterministic parameter mappings.
"""

from enum import Enum
from typing import List, Dict, Literal
from dataclasses import dataclass


# ============================================================================
# LAYER 1: CATEGORICAL TAXONOMY (OLOG STRUCTURE)
# ============================================================================

class SubjectType(str, Enum):
    """Category of subject matter"""
    ARCHITECTURE = "architecture"
    PORTRAIT = "portrait"
    STILL_LIFE = "still_life"
    LANDSCAPE = "landscape"
    ABSTRACT = "abstract"
    PRODUCT = "product"
    SCENE = "scene"


class EmotionalTone(str, Enum):
    """Emotional quality to convey"""
    PLAYFUL = "playful"
    TENSE = "tense"
    ABSURD = "absurd"
    WHIMSICAL = "whimsical"
    SURREAL = "surreal"
    DRAMATIC = "dramatic"
    CHAOTIC = "chaotic"
    ELEGANT = "elegant"
    OMINOUS = "ominous"


class VisualPriority(str, Enum):
    """Which slapstick qualities to emphasize"""
    SCALE = "scale"  # Relates to: exaggeration
    PHYSICS = "physics"  # Relates to: physical
    REPETITION = "repetition"  # Relates to: ruleOfThree
    CLARITY = "clarity"  # Relates to: readability
    SUSPENSE = "suspense"  # Relates to: tension
    RHYTHM = "rhythm"  # Relates to: timing
    DISTORTION = "distortion"  # Relates to: exaggeration
    BALANCE = "balance"  # Relates to: tension
    FLOW = "flow"  # Relates to: timing
    IMPACT = "impact"  # Relates to: physical


class IntensityLevel(str, Enum):
    """Overall intensity level of slapstick effect"""
    SUBTLE = "subtle"
    MODERATE = "moderate"
    STRONG = "strong"
    EXTREME = "extreme"


class SlapstickParameter(str, Enum):
    """Six core slapstick parameters"""
    EXAGGERATION = "exaggeration"  # Scale distortions, color intensity, impossible proportions
    TIMING = "timing"  # Repetition patterns, compositional cadence, motion blur
    PHYSICAL = "physical"  # Squash/stretch, gravity defiance, collision moments
    RULE_OF_THREE = "ruleOfThree"  # Triplet groupings, establish-repeat-subvert patterns
    READABILITY = "readability"  # Silhouette clarity, graphic simplification
    TENSION = "tension"  # Precarious balance, suspense, about-to-happen moments


# ============================================================================
# LAYER 2: PROFILE STRUCTURES
# ============================================================================

@dataclass
class SlapstickParameterSet:
    """A set of slapstick parameter values (0-10)"""
    exaggeration: int
    timing: int
    physical: int
    ruleOfThree: int
    readability: int
    tension: int
    
    def to_dict(self) -> Dict[str, int]:
        """Convert to dictionary for serialization"""
        return {
            'exaggeration': self.exaggeration,
            'timing': self.timing,
            'physical': self.physical,
            'ruleOfThree': self.ruleOfThree,
            'readability': self.readability,
            'tension': self.tension
        }
    
    def validate(self) -> bool:
        """Ensure all parameters are within bounds"""
        for value in [self.exaggeration, self.timing, self.physical, 
                      self.ruleOfThree, self.readability, self.tension]:
            if not 0 <= value <= 10:
                return False
        return True


@dataclass
class SubjectTypeProfile:
    """Preset parameter values for a subject type"""
    subject_type: SubjectType
    base_parameters: SlapstickParameterSet
    description: str


@dataclass
class EmotionalToneModifier:
    """How emotional tone modifies parameters"""
    emotional_tone: EmotionalTone
    modifiers: Dict[str, int]  # Parameter name -> delta


@dataclass
class VisualPriorityBoost:
    """Which parameter a visual priority boosts"""
    priority: VisualPriority
    target_parameter: str  # Parameter name to boost
    boost_amount: int  # Usually +2


@dataclass
class DesignIntent:
    """Structured representation of creative intent"""
    subject_type: SubjectType
    emotional_tone: EmotionalTone
    visual_priorities: List[VisualPriority]
    intensity_level: IntensityLevel


@dataclass
class SlapstickEnhancement:
    """Result of applying slapstick enhancement"""
    original_prompt: str
    parameters: SlapstickParameterSet
    enhanced_prompt: str
    negative_prompt: str
    design_summary: str


# ============================================================================
# LAYER 3: OLOG MORPHISMS (DETERMINISTIC MAPPINGS)
# ============================================================================

class SlapstickOlogMorphisms:
    """
    Deterministic morphisms for slapstick enhancement.
    Maps design intent → parameters → enhanced prompts
    """
    
    # Subject type presets (Morphism source: SubjectType → SlapstickParameterSet)
    SUBJECT_TYPE_PRESETS = {
        SubjectType.ARCHITECTURE: SlapstickParameterSet(
            exaggeration=7, timing=4, physical=6, ruleOfThree=7, readability=6, tension=8
        ),
        SubjectType.PORTRAIT: SlapstickParameterSet(
            exaggeration=6, timing=5, physical=4, ruleOfThree=5, readability=8, tension=4
        ),
        SubjectType.STILL_LIFE: SlapstickParameterSet(
            exaggeration=8, timing=6, physical=7, ruleOfThree=8, readability=7, tension=6
        ),
        SubjectType.LANDSCAPE: SlapstickParameterSet(
            exaggeration=7, timing=7, physical=8, ruleOfThree=6, readability=5, tension=7
        ),
        SubjectType.ABSTRACT: SlapstickParameterSet(
            exaggeration=9, timing=8, physical=9, ruleOfThree=7, readability=4, tension=8
        ),
        SubjectType.PRODUCT: SlapstickParameterSet(
            exaggeration=8, timing=5, physical=6, ruleOfThree=7, readability=9, tension=5
        ),
        SubjectType.SCENE: SlapstickParameterSet(
            exaggeration=6, timing=7, physical=7, ruleOfThree=6, readability=6, tension=7
        ),
    }
    
    # Intensity multipliers (Morphism: IntensityLevel → float)
    INTENSITY_MULTIPLIERS = {
        IntensityLevel.SUBTLE: 0.3,
        IntensityLevel.MODERATE: 0.6,
        IntensityLevel.STRONG: 0.85,
        IntensityLevel.EXTREME: 1.0,
    }
    
    # Emotional tone modifiers (Morphism: EmotionalTone → parameter deltas)
    EMOTIONAL_TONE_MODIFIERS = {
        EmotionalTone.PLAYFUL: {'timing': +2, 'physical': +2, 'ruleOfThree': +1},
        EmotionalTone.TENSE: {'tension': +3, 'physical': -1, 'readability': +1},
        EmotionalTone.ABSURD: {'exaggeration': +3, 'physical': +2, 'readability': -2},
        EmotionalTone.WHIMSICAL: {'timing': +2, 'ruleOfThree': +2, 'exaggeration': +1},
        EmotionalTone.SURREAL: {'exaggeration': +3, 'physical': +3, 'readability': -1},
        EmotionalTone.DRAMATIC: {'tension': +3, 'readability': +2, 'timing': +1},
        EmotionalTone.CHAOTIC: {'exaggeration': +2, 'physical': +3, 'timing': +2, 'readability': -2},
        EmotionalTone.ELEGANT: {'readability': +3, 'ruleOfThree': +2, 'timing': +1, 'physical': -1},
        EmotionalTone.OMINOUS: {'tension': +4, 'timing': -1, 'readability': +1},
    }
    
    # Visual priority boosts (Morphism: VisualPriority → parameter boost)
    VISUAL_PRIORITY_BOOSTS = {
        VisualPriority.SCALE: 'exaggeration',
        VisualPriority.PHYSICS: 'physical',
        VisualPriority.REPETITION: 'ruleOfThree',
        VisualPriority.CLARITY: 'readability',
        VisualPriority.SUSPENSE: 'tension',
        VisualPriority.RHYTHM: 'timing',
        VisualPriority.DISTORTION: 'exaggeration',
        VisualPriority.BALANCE: 'tension',
        VisualPriority.FLOW: 'timing',
        VisualPriority.IMPACT: 'physical',
    }
    
    @staticmethod
    def design_intent_to_parameters(design_intent: DesignIntent) -> SlapstickParameterSet:
        """
        Convert design intent to slapstick parameters.
        Morphism: DesignIntent → SlapstickParameterSet
        """
        
        # Step 1: Get subject type preset
        subject_params = SlapstickOlogMorphisms.SUBJECT_TYPE_PRESETS.get(
            design_intent.subject_type,
            SlapstickOlogMorphisms.SUBJECT_TYPE_PRESETS[SubjectType.SCENE]
        )
        
        # Step 2: Apply intensity multiplier
        multiplier = SlapstickOlogMorphisms.INTENSITY_MULTIPLIERS.get(
            design_intent.intensity_level,
            SlapstickOlogMorphisms.INTENSITY_MULTIPLIERS[IntensityLevel.MODERATE]
        )
        
        params = {
            'exaggeration': round(subject_params.exaggeration * multiplier),
            'timing': round(subject_params.timing * multiplier),
            'physical': round(subject_params.physical * multiplier),
            'ruleOfThree': round(subject_params.ruleOfThree * multiplier),
            'readability': round(subject_params.readability * multiplier),
            'tension': round(subject_params.tension * multiplier),
        }
        
        # Step 3: Apply emotional tone modifiers
        modifiers = SlapstickOlogMorphisms.EMOTIONAL_TONE_MODIFIERS.get(
            design_intent.emotional_tone,
            {}
        )
        
        for param_name, delta in modifiers.items():
            if param_name in params:
                params[param_name] = max(0, min(10, params[param_name] + delta))
        
        # Step 4: Apply visual priority boosts
        for priority in design_intent.visual_priorities:
            target_param = SlapstickOlogMorphisms.VISUAL_PRIORITY_BOOSTS.get(priority)
            if target_param and target_param in params:
                params[target_param] = min(10, params[target_param] + 2)
        
        # Step 5: Ensure all values are within bounds
        for key in params:
            params[key] = max(0, min(10, round(params[key])))
        
        return SlapstickParameterSet(
            exaggeration=params['exaggeration'],
            timing=params['timing'],
            physical=params['physical'],
            ruleOfThree=params['ruleOfThree'],
            readability=params['readability'],
            tension=params['tension'],
        )
    
    @staticmethod
    def validate_parameters(params: SlapstickParameterSet) -> bool:
        """
        Validate that parameter set is within bounds.
        Morphism: SlapstickParameterSet → bool
        """
        return params.validate()
    
    @staticmethod
    def parameters_to_enhancement_description(params: SlapstickParameterSet) -> Dict[str, str]:
        """
        Convert parameters to human-readable descriptions.
        Morphism: SlapstickParameterSet → Enhancement descriptions
        """
        
        descriptions = {}
        
        # Exaggeration description
        if params.exaggeration >= 9:
            descriptions['exaggeration'] = "extreme distortions with impossible scales"
        elif params.exaggeration >= 6:
            descriptions['exaggeration'] = "obvious proportion exaggerations"
        elif params.exaggeration >= 3:
            descriptions['exaggeration'] = "subtle scale variations"
        else:
            descriptions['exaggeration'] = "minimal exaggeration"
        
        # Timing description
        if params.timing >= 9:
            descriptions['timing'] = "staccato visual interruptions"
        elif params.timing >= 6:
            descriptions['timing'] = "strong rhythmic composition"
        elif params.timing >= 3:
            descriptions['timing'] = "gentle repetition"
        else:
            descriptions['timing'] = "static composition"
        
        # Physical description
        if params.physical >= 9:
            descriptions['physical'] = "extreme elasticity and squash-stretch"
        elif params.physical >= 6:
            descriptions['physical'] = "squash and stretch principles"
        elif params.physical >= 3:
            descriptions['physical'] = "subtle material flexibility"
        else:
            descriptions['physical'] = "realistic physics"
        
        # Rule of three description
        if params.ruleOfThree >= 9:
            descriptions['ruleOfThree'] = "complex triplet patterns"
        elif params.ruleOfThree >= 6:
            descriptions['ruleOfThree'] = "clear triplet groupings"
        elif params.ruleOfThree >= 3:
            descriptions['ruleOfThree'] = "subtle triplet hints"
        else:
            descriptions['ruleOfThree'] = "no triplet emphasis"
        
        # Readability description
        if params.readability >= 9:
            descriptions['readability'] = "crystal clear graphic simplification"
        elif params.readability >= 6:
            descriptions['readability'] = "strong silhouette clarity"
        elif params.readability >= 3:
            descriptions['readability'] = "subtle graphic emphasis"
        else:
            descriptions['readability'] = "complex visual details"
        
        # Tension description
        if params.tension >= 9:
            descriptions['tension'] = "extreme precarious balance"
        elif params.tension >= 6:
            descriptions['tension'] = "strong suspenseful moment"
        elif params.tension >= 3:
            descriptions['tension'] = "subtle tension"
        else:
            descriptions['tension'] = "peaceful balance"
        
        return descriptions
