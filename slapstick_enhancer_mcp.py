#!/usr/bin/env python3
"""
Slapstick Enhancer MCP (Refactored)
Three-layer architecture: Olog + Prompt templates + FastMCP interface

This version separates:
1. Categorical taxonomy (slapstick_ologs.py) - pure logic, deterministic
2. Prompt enhancement templates (this file) - pre-crafted text at each intensity level
3. MCP interface (this file) - Claude interaction layer

Cost optimization: Claude called only for final creative synthesis if needed.
All parameter mapping and prompt generation is deterministic via ologs.
"""

from fastmcp import FastMCP
from typing import Dict, List, Any
import json

# Import olog system (Layer 1: Categorical Taxonomy)
from slapstick_ologs import (
    SlapstickOlogMorphisms,
    SubjectType,
    EmotionalTone,
    VisualPriority,
    IntensityLevel,
    SlapstickParameterSet,
    DesignIntent,
)

# Initialize MCP server
mcp = FastMCP("slapstick-enhancer")


# ============================================================================
# LAYER 2: PROMPT ENHANCEMENT TEMPLATES
# ============================================================================

class SlapstickPromptTemplates:
    """
    Pre-crafted enhancement text at each parameter level.
    These templates are deterministically selected based on parameter values.
    """
    
    EXAGGERATION_TEMPLATES = {
        (9, 10): "extreme distortions with impossible scales showing 3-5x size variations, surreal color intensity, warped perspective that shouldn't work but does",
        (6, 8): "obvious proportion exaggerations, oversaturated colors and heightened contrast, forced perspective",
        (3, 5): "subtle scale variations and slightly heightened color saturation",
        (0, 2): "realistic proportions and natural color",
    }
    
    TIMING_TEMPLATES = {
        (9, 10): "staccato visual interruptions, dramatic motion blur on static objects, speed lines suggesting imminent action",
        (6, 8): "strong rhythmic composition with repeating elements, anticipation spaces and visual pauses between key elements",
        (3, 5): "gentle repetition of visual elements creating compositional rhythm",
        (0, 2): "static composition without temporal elements",
    }
    
    PHYSICAL_TEMPLATES = {
        (9, 10): "extreme elasticity and squash-stretch distortion, mid-collision freeze-frame moment, materials stretched or compressed cartoonishly, complete defiance of physics",
        (6, 8): "squash and stretch principles applied to forms, gravity-defying elements, objects mid-fall or impossibly suspended",
        (3, 5): "subtle material flexibility, slight impossibilities in physics",
        (0, 2): "realistic physics and rigid materials",
    }
    
    RULE_OF_THREE_TEMPLATES = {
        (9, 10): "complex establish-repeat-subvert patterns, three-part visual jokes in composition, triple visual callbacks, all using rule of thirds positioning",
        (6, 8): "clear triplet groupings, establish one element then systematically repeat-with-variation twice more, visual pattern of three",
        (3, 5): "subtle hints of grouping in threes, occasional triplet arrangement",
        (0, 2): "no emphasis on triplet groupings",
    }
    
    READABILITY_TEMPLATES = {
        (9, 10): "crystal clear graphic simplification and silhouette clarity, high contrast separating subject from background, visual clarity even from distance",
        (6, 8): "strong silhouette clarity and graphic simplification, clear contrast between subject and environment",
        (3, 5): "subtle graphic emphasis with readable forms",
        (0, 2): "complex visual details without simplification",
    }
    
    TENSION_TEMPLATES = {
        (9, 10): "extreme precarious balance suggesting imminent collapse, maximum suspense and about-to-happen energy, frozen moment of chaos",
        (6, 8): "strong suspenseful moment with clear tension, objects at unstable angles, sense of impending action",
        (3, 5): "subtle underlying tension and unease",
        (0, 2): "peaceful balanced composition",
    }
    
    NEGATIVE_PROMPT_COMPONENTS = {
        'high_exaggeration': "realistic proportions, natural colors, subtle",
        'high_timing': "static composition, no motion, no rhythm",
        'high_physical': "realistic physics, rigid materials, no distortion",
        'high_rule_of_three': "no pattern, no rhythm, random composition",
        'low_readability': "cluttered, confusing, unclear silhouette",
        'high_tension': "peaceful, calm, balanced, serene",
    }
    
    @staticmethod
    def get_template(param_value: int, templates: Dict) -> str:
        """Get template text based on parameter value"""
        for (min_val, max_val), text in sorted(templates.items(), reverse=True):
            if min_val <= param_value <= max_val:
                return text
        return ""
    
    @staticmethod
    def build_enhanced_prompt(base_prompt: str, params: SlapstickParameterSet) -> str:
        """Deterministically build enhanced prompt from parameters"""
        additions = []
        
        # Add exaggeration enhancement
        exag_text = SlapstickPromptTemplates.get_template(
            params.exaggeration, 
            SlapstickPromptTemplates.EXAGGERATION_TEMPLATES
        )
        if exag_text:
            additions.append(exag_text)
        
        # Add timing enhancement
        timing_text = SlapstickPromptTemplates.get_template(
            params.timing,
            SlapstickPromptTemplates.TIMING_TEMPLATES
        )
        if timing_text:
            additions.append(timing_text)
        
        # Add physical comedy enhancement
        physical_text = SlapstickPromptTemplates.get_template(
            params.physical,
            SlapstickPromptTemplates.PHYSICAL_TEMPLATES
        )
        if physical_text:
            additions.append(physical_text)
        
        # Add rule of three enhancement
        rot_text = SlapstickPromptTemplates.get_template(
            params.ruleOfThree,
            SlapstickPromptTemplates.RULE_OF_THREE_TEMPLATES
        )
        if rot_text:
            additions.append(rot_text)
        
        # Add readability enhancement
        read_text = SlapstickPromptTemplates.get_template(
            params.readability,
            SlapstickPromptTemplates.READABILITY_TEMPLATES
        )
        if read_text:
            additions.append(read_text)
        
        # Add tension enhancement
        tension_text = SlapstickPromptTemplates.get_template(
            params.tension,
            SlapstickPromptTemplates.TENSION_TEMPLATES
        )
        if tension_text:
            additions.append(tension_text)
        
        # Combine base prompt with enhancements
        if additions:
            return f"{base_prompt}, {', '.join(additions)}"
        return base_prompt
    
    @staticmethod
    def build_negative_prompt(params: SlapstickParameterSet) -> str:
        """Deterministically build negative prompt from parameters"""
        negatives = []
        
        # Add negatives based on high parameter values
        if params.exaggeration >= 6:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['high_exaggeration'])
        
        if params.timing >= 6:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['high_timing'])
        
        if params.physical >= 6:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['high_physical'])
        
        if params.ruleOfThree >= 6:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['high_rule_of_three'])
        
        if params.readability >= 8:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['low_readability'])
        
        if params.tension >= 6:
            negatives.append(SlapstickPromptTemplates.NEGATIVE_PROMPT_COMPONENTS['high_tension'])
        
        # Always include general negatives
        base_negatives = ["blurry", "low quality", "distorted", "ugly"]
        
        return ", ".join(base_negatives + negatives) if negatives else ", ".join(base_negatives)


# ============================================================================
# LAYER 3: MCP TOOLS
# ============================================================================

@mcp.tool()
def enhance_with_intent(
    base_prompt: str,
    subject_type: str,
    emotional_tone: str,
    visual_priorities: List[str],
    intensity: str
) -> Dict[str, Any]:
    """
    Enhance an image prompt with slapstick design principles based on design intent.
    
    Maps creative intent to specific slapstick parameters and generates enhanced prompt.
    
    Args:
        base_prompt: The original image description (e.g., "A corporate office")
        subject_type: Category of subject - architecture, portrait, still_life, landscape, abstract, product, scene
        emotional_tone: Emotional quality - playful, tense, absurd, whimsical, surreal, dramatic, chaotic, elegant, ominous
        visual_priorities: List of priorities to emphasize (1-3 recommended) - scale, physics, repetition, clarity, suspense, rhythm, distortion, balance, flow, impact
        intensity: Overall intensity level - subtle, moderate, strong, extreme
    
    Returns:
        Dictionary with:
        - parameters_used: The calculated slapstick parameters
        - enhanced_prompt: The enhanced image prompt
        - negative_prompt: Suggested negative prompt to prevent unwanted effects
        - design_intent_summary: Human-readable explanation of choices
    """
    
    try:
        # Convert string inputs to enums
        subject = SubjectType[subject_type.upper()]
        emotion = EmotionalTone[emotional_tone.upper()]
        intensity_level = IntensityLevel[intensity.upper()]
        
        # Convert visual priorities to enums
        priorities = []
        for priority_str in visual_priorities:
            try:
                priorities.append(VisualPriority[priority_str.upper()])
            except KeyError:
                return {"error": f"Invalid visual priority: {priority_str}"}
        
        # Create design intent using ologs
        design_intent = DesignIntent(
            subject_type=subject,
            emotional_tone=emotion,
            visual_priorities=priorities,
            intensity_level=intensity_level
        )
        
        # Map intent to parameters using deterministic morphism
        params = SlapstickOlogMorphisms.design_intent_to_parameters(design_intent)
        
        # Validate parameters
        if not SlapstickOlogMorphisms.validate_parameters(params):
            return {"error": "Invalid parameters generated"}
        
        # Generate enhanced prompt using templates
        enhanced_prompt = SlapstickPromptTemplates.build_enhanced_prompt(base_prompt, params)
        negative_prompt = SlapstickPromptTemplates.build_negative_prompt(params)
        
        # Create summary
        visual_priorities_str = ", ".join([p.value for p in priorities]) if priorities else "none specified"
        summary = (
            f"Applied {intensity_level.value} {emotional_tone.value} treatment to "
            f"{subject_type}, emphasizing {visual_priorities_str}"
        )
        
        return {
            "parameters_used": params.to_dict(),
            "enhanced_prompt": enhanced_prompt,
            "negative_prompt": negative_prompt,
            "design_intent_summary": summary
        }
    
    except ValueError as e:
        return {"error": f"Invalid input: {str(e)}"}


@mcp.tool()
def enhance_with_parameters(
    base_prompt: str,
    exaggeration: int = 5,
    timing: int = 5,
    physical: int = 5,
    ruleOfThree: int = 5,
    readability: int = 5,
    tension: int = 5
) -> Dict[str, Any]:
    """
    Enhance an image prompt with explicit slapstick parameter values.
    
    Use this when you want direct control over the six slapstick parameters,
    or to adjust parameters suggested by enhance_with_intent.
    
    Parameters (all 0-10):
    - exaggeration: Scale distortions, color intensity, impossible proportions
    - timing: Repetition patterns, compositional cadence, motion blur
    - physical: Squash/stretch, gravity defiance, collision moments
    - ruleOfThree: Triplet groupings, establish-repeat-subvert patterns
    - readability: Silhouette clarity, graphic simplification
    - tension: Precarious balance, suspense, about-to-happen moments
    
    Args:
        base_prompt: The original image description
        exaggeration: Scale distortion level (0-10)
        timing: Rhythmic composition level (0-10)
        physical: Physical comedy level (0-10)
        ruleOfThree: Triplet pattern level (0-10)
        readability: Graphic clarity level (0-10)
        tension: Suspense/precarious balance level (0-10)
    
    Returns:
        Dictionary with:
        - parameters_used: The slapstick parameters
        - enhanced_prompt: The enhanced image prompt
        - negative_prompt: Suggested negative prompt
    """
    
    try:
        # Create parameter set
        params = SlapstickParameterSet(
            exaggeration=max(0, min(10, int(exaggeration))),
            timing=max(0, min(10, int(timing))),
            physical=max(0, min(10, int(physical))),
            ruleOfThree=max(0, min(10, int(ruleOfThree))),
            readability=max(0, min(10, int(readability))),
            tension=max(0, min(10, int(tension)))
        )
        
        # Validate parameters
        if not params.validate():
            return {"error": "Parameters must be between 0 and 10"}
        
        # Generate enhanced prompt using templates
        enhanced_prompt = SlapstickPromptTemplates.build_enhanced_prompt(base_prompt, params)
        negative_prompt = SlapstickPromptTemplates.build_negative_prompt(params)
        
        return {
            "parameters_used": params.to_dict(),
            "enhanced_prompt": enhanced_prompt,
            "negative_prompt": negative_prompt
        }
    
    except (ValueError, TypeError) as e:
        return {"error": f"Invalid parameter value: {str(e)}"}


@mcp.tool()
def describe_parameters(
    exaggeration: int = 5,
    timing: int = 5,
    physical: int = 5,
    ruleOfThree: int = 5,
    readability: int = 5,
    tension: int = 5
) -> Dict[str, Any]:
    """
    Get human-readable descriptions of what specific parameter values mean.
    
    Useful for understanding how parameters affect the final image.
    
    Args:
        exaggeration: Scale distortion level (0-10)
        timing: Rhythmic composition level (0-10)
        physical: Physical comedy level (0-10)
        ruleOfThree: Triplet pattern level (0-10)
        readability: Graphic clarity level (0-10)
        tension: Suspense/precarious balance level (0-10)
    
    Returns:
        Dictionary with human-readable descriptions for each parameter
    """
    
    try:
        params = SlapstickParameterSet(
            exaggeration=max(0, min(10, int(exaggeration))),
            timing=max(0, min(10, int(timing))),
            physical=max(0, min(10, int(physical))),
            ruleOfThree=max(0, min(10, int(ruleOfThree))),
            readability=max(0, min(10, int(readability))),
            tension=max(0, min(10, int(tension)))
        )
        
        descriptions = SlapstickOlogMorphisms.parameters_to_enhancement_description(params)
        descriptions['parameters'] = params.to_dict()
        
        return descriptions
    
    except (ValueError, TypeError) as e:
        return {"error": f"Invalid parameter value: {str(e)}"}


@mcp.tool()
def get_available_options() -> Dict[str, List[str]]:
    """
    Get all available options for design intent parameters.
    
    Returns:
        Dictionary with lists of valid values for each parameter type
    """
    
    return {
        "subject_types": [st.value for st in SubjectType],
        "emotional_tones": [et.value for et in EmotionalTone],
        "visual_priorities": [vp.value for vp in VisualPriority],
        "intensity_levels": [il.value for il in IntensityLevel],
    }


if __name__ == "__main__":
    mcp.run()
