# Slapstick Enhancer MCP

A deterministic visual vocabulary server that maps slapstick design principles to locked aesthetic parameters for image generation. Part of the visual vocabularies ecosystem.

## What This Does

Slapstick is a comedy language with precise visual grammar: exaggeration, timing, physical impact, rule-of-three patterns, readability, and tension. This MCP translates those principles into locked aesthetic parameters for image generation, enabling reproducible comedic and dynamic visual aesthetics across any subject.

Generate a slapstick-enhanced image of a corporate office, a landscape, a portrait, or anything else. The vocabulary locks the comedic mechanics: how exaggerated the distortion is, how pronounced the timing/rhythm patterns are, how physical and impactful the composition feels, how the rule-of-three is applied, how readable the silhouettes stay, and how much precarious balance or suspense the image conveys.

No drift. Consistent comedic energy.

## Quick Start

### Installation

```bash
git clone https://github.com/dmarsters/slapstick-enhancer.git
cd slapstick-enhancer
pip install -r requirements.txt
```

### Usage with Claude

Add to your Claude client configuration:

```json
{
  "mcpServers": {
    "slapstick-enhancer": {
      "command": "python",
      "args": ["slapstick_enhancer_mcp.py"]
    }
  }
}
```

Then use Claude to enhance prompts:

```
Enhance this with slapstick design principles:
"A corporate office meeting in chaos"
Subject: architecture
Emotional tone: absurd
Intensity: strong
Visual priorities: scale, repetition, clarity
```

Claude will layer slapstick parameters onto your prompt, locking in exaggerated proportions, rhythmic repetition patterns, squash/stretch physics, rule-of-three compositional groupings, graphic clarity, and precarious balance moments.

## The Six Slapstick Parameters

Slapstick design works through six interlocking dimensions, each on a 0-10 scale:

### 1. Exaggeration (0-10)
**Scale distortion, color intensity, impossible proportions**

- 0: Subtle, barely noticeable distortion
- 3: Light touch, gentle exaggeration
- 5: Balanced, clearly stylized but believable
- 7: Heavy exaggeration, noticeable distortions
- 10: Extreme, impossible physics, hyper-saturated colors

Exaggeration creates the visual shock that makes slapstick work. It says "this is not real, watch what happens."

### 2. Timing (0-10)
**Repetition patterns, compositional cadence, motion blur**

- 0: No rhythm, random distribution
- 3: Subtle rhythm, gentle pacing
- 5: Clear rhythm, balanced cadence
- 7: Strong rhythm, pronounced repetition
- 10: Hypnotic rhythm, machine-like precision in patterning

Timing is about visual rhythm. Slapstick needs patterns that create anticipation and momentum. Rule-of-three thrives here.

### 3. Physical (0-10)
**Squash/stretch, gravity defiance, collision moments**

- 0: Static, no sense of physical action
- 3: Light movement, subtle deformation
- 5: Clear physical action, believable deformation
- 7: Exaggerated movement, obvious impact
- 10: Extreme squash/stretch, gravity-defying, mid-collision moments frozen

Physical is the actual comedy moment. It's the pratfall, the collision, the impossible twist. This parameter brings impact.

### 4. Rule of Three (0-10)
**Triplet groupings, establish-repeat-subvert patterns**

- 0: No grouping, isolated elements
- 3: Light triplet suggestion
- 5: Clear rule-of-three, balanced groupings
- 7: Strong triplet emphasis, obvious establish-repeat-subvert
- 10: Obsessive rule-of-three, three of everything, third item always subverts

Rule-of-three is the DNA of comedy structure. Two things establish a pattern, the third subverts it. This parameter controls how much that structure dominates the composition.

### 5. Readability (0-10)
**Silhouette clarity, graphic simplification**

- 0: Complex, busy, hard to parse at a glance
- 3: Somewhat simplified, readable elements
- 5: Clear silhouettes, good graphic design
- 7: Highly simplified, very clear readability
- 10: Stark silhouettes, poster-like clarity, no visual noise

Readability keeps slapstick from becoming chaos. Strong silhouettes and graphic clarity make the joke land. Without this, slapstick becomes confusing noise.

### 6. Tension (0-10)
**Precarious balance, suspense, about-to-happen moments**

- 0: Stable, no sense of danger
- 3: Subtle unease, minor imbalance
- 5: Clear tension, noticeable precariousness
- 7: High tension, obvious imbalance, suspense
- 10: Extreme tension, about to collapse, maximum suspense

Tension is the setup. The moment before the fall. Slapstick needs this anticipatory quality. High tension creates the pause that makes the punchline land harder.

## Usage Patterns

### Pattern 1: Intent-Based Enhancement

Start with design intent, let the system map to parameters:

```python
enhance_with_intent(
    base_prompt="A corporate office",
    subject_type="architecture",
    emotional_tone="absurd",
    intensity="strong",
    visual_priorities=["scale", "repetition", "clarity"]
)
```

Returns calculated slapstick parameters and enhanced prompt.

### Pattern 2: Direct Parameter Control

For precise control, specify parameters directly:

```python
enhance_with_parameters(
    base_prompt="A corporate office",
    exaggeration=8,
    timing=7,
    physical=6,
    ruleOfThree=9,
    readability=8,
    tension=5
)
```

Returns enhanced prompt with exactly these parameters locked.

### Pattern 3: Parameter Inspection

Understand what specific parameter values mean:

```python
describe_parameters(
    exaggeration=8,
    timing=7,
    physical=6,
    ruleOfThree=9,
    readability=8,
    tension=5
)
```

Returns human-readable descriptions: "Scale distortion level: Heavy exaggeration, noticeable distortions. Rhythmic composition level: Strong rhythm, pronounced repetition..." etc.

## Architecture

Two-layer design: intent-driven morphisms plus direct parameter control.

### Layer 1: Intent-to-Parameters Morphisms

Map creative intent to slapstick parameters:

- `subject_type` + `emotional_tone` + `intensity` → Parameter values
- `visual_priorities` → Parameter emphasis
- Ensures coherent, internally consistent parameter combinations

Example:
```
Subject: architecture
Tone: absurd
Intensity: strong
Priorities: [scale, repetition, clarity]
↓
exaggeration: 8 (strong absurdity needs heavy distortion)
timing: 7 (repetition priority drives high rhythmic value)
physical: 5 (architecture doesn't have obvious movement, moderate)
ruleOfThree: 8 (absurdity thrives on rule-of-three)
readability: 8 (high priority, keep clear)
tension: 4 (architecture doesn't need suspense, low)
```

### Layer 2: Direct Parameter Interface

Claude can override intent-derived parameters and specify exact values for precise control.

### Cost Efficiency

Traditional approach: Send full prompt + emotional direction to LLM for enhancement (expensive)

This approach:
1. Intent morphism (zero tokens) — categorical mapping
2. Parameter inspection (zero tokens) — taxonomy lookup
3. Single LLM call — creative synthesis of base prompt + locked parameters

Result: ~60% token savings vs. pure LLM enhancement.

## Subject Types

Slapstick works across all visual domains:

- **architecture**: Buildings, interiors, spaces
- **portrait**: Faces, people, characters
- **still_life**: Objects, arrangements, compositions
- **landscape**: Environments, nature, outdoor scenes
- **abstract**: Non-representational, pure form
- **product**: Objects for commerce, industrial design
- **scene**: Complex multi-element compositions

Each subject type has different natural slapstick tendencies. Architecture can exaggerate proportions and scale. Portraits can emphasize expression and physical deformation. Landscapes can play with gravity and impossible terrain.

## Emotional Tones

Slapstick tone shapes how parameters combine:

- **playful**: Light-hearted, fun, non-threatening exaggeration
- **tense**: Suspenseful, precarious, about-to-break energy
- **absurd**: Illogical, impossible, rule-breaking reality
- **whimsical**: Fanciful, dreamlike, unexpected charm
- **surreal**: Dream logic, impossible physics normalized
- **dramatic**: High-stakes, exaggerated impact, heroic
- **chaotic**: Uncontrolled, overwhelming, sensory overload
- **elegant**: Exaggerated but refined, sophisticated distortion
- **ominous**: Dark, threatening, menacing exaggeration

## Visual Priorities

Focus areas that emphasize specific slapstick mechanics:

- **scale**: Size relationships, proportion exaggeration
- **physics**: Movement, impact, collision moments
- **repetition**: Pattern, rhythm, rule-of-three
- **clarity**: Readability, silhouette, graphic design
- **suspense**: Tension, precarious balance, about-to-happen
- **rhythm**: Timing, cadence, pacing
- **distortion**: Warping, deformation, impossible shapes
- **balance**: Compositional equilibrium or imbalance
- **flow**: Visual movement, eye direction
- **impact**: Force, weight, consequence

Priority combinations shape parameter emphasis:

```
Priorities: [scale, repetition, clarity]
→ High exaggeration, high timing, high readability
→ Less emphasis on physical and tension
```

## Intensity Levels

Overall slapstick intensity determines parameter ranges:

- **subtle** (all parameters 0-4): Light comedic touch, barely stylized
- **moderate** (all parameters 3-6): Clear slapstick, balanced
- **strong** (all parameters 6-9): Heavy slapstick, very stylized
- **extreme** (all parameters 7-10): Maximum comedy, almost unreal

## Customization

These parameters represent specific comedy principles, not universal rules. You can edit, extend, or rebuild the morphism logic entirely.

### Adjust Morphism Logic

Edit intent-to-parameter mappings in `slapstick_enhancer_mcp.py`:

```python
@staticmethod
def calculate_exaggeration_from_intent(tone, intensity, priorities):
    # Your custom mapping logic
    base = intensity_to_base_value[intensity]
    if "scale" in priorities:
        base += 2
    return min(base, 10)
```

### Add New Emotional Tones

Extend the tone catalog:

```python
TONE_TO_PARAMETERS = {
    "melancholic": {
        "exaggeration": 4,
        "timing": 3,
        "physical": 2,
        "ruleOfThree": 3,
        "readability": 6,
        "tension": 6
    },
    # Your new tone
}
```

### Adjust Parameter Descriptions

Make the parameter meanings match your creative vision:

```python
PARAMETER_DESCRIPTIONS = {
    "exaggeration": {
        8: "Your custom description of what 8 exaggeration means for your work"
    }
}
```

## Example Use Cases

### Use Case 1: Comedic Product Photography

```
Base: "A bottle of hot sauce sitting on a kitchen counter"
Subject: product
Tone: playful
Intensity: strong
Priorities: [scale, clarity, repetition]

↓ Creates:
Exaggeration: 7 (bottle might be oversized or distorted)
Timing: 7 (repetitive kitchen elements in rhythmic pattern)
Physical: 5 (moderate impact feeling)
RuleOfThree: 7 (three kitchen elements establish-repeat-subvert)
Readability: 9 (product must be crystal clear)
Tension: 3 (playful, not suspenseful)

Result: Bold, fun product shot with rhythmic composition and clear subject focus
```

### Use Case 2: Absurd Architectural Visualization

```
Base: "A corporate office building facade"
Subject: architecture
Tone: absurd
Intensity: extreme
Priorities: [scale, distortion, repetition]

↓ Creates:
Exaggeration: 9 (impossible proportions, surreal distortions)
Timing: 8 (windows repeat in hypnotic pattern)
Physical: 4 (buildings don't move, low)
RuleOfThree: 8 (three-part compositional structure)
Readability: 6 (some chaos acceptable with absurdity)
Tension: 5 (moderate suspense about this weird structure)

Result: Surreal, impossible building that reads as comedy through scale and pattern
```

### Use Case 3: Tense Dramatic Scene

```
Base: "A character standing on a narrow bridge"
Subject: portrait
Tone: dramatic
Intensity: strong
Priorities: [tension, suspense, impact]

↓ Creates:
Exaggeration: 6 (moderate, dramatic not cartoony)
Timing: 5 (clear rhythm but not comedic pacing)
Physical: 7 (character's body language shows physical strain)
RuleOfThree: 4 (not emphasizing pattern, emphasizing moment)
Readability: 7 (clear silhouette of the character)
Tension: 9 (maximum precariousness, about-to-fall)

Result: High-stakes dramatic moment with physical intensity and visual clarity
```

## Composition with Other Vocabularies

Slapstick can layer with other visual vocabulary MCP servers, though direction matters:

```
Base: "A person in a luxury hotel lobby"
+ Magazine Photography (Life 1960s): documentary, authentic, grainy
+ Slapstick (strong): exaggerated, rhythmic, tension-filled
= Documentary-style slapstick composition
```

Some vocabularies work better with slapstick than others. Comedic, dynamic, or rhythmic aesthetics compose well. Minimal, subdued, or serene aesthetics may conflict.

## Limitations and Intentionality

Slapstick is a specific comedy language. It's not appropriate for all subjects or moods:

Most effective for:
- Comedic and satirical work
- Dynamic, energetic compositions
- Visual storytelling that needs impact
- Product and commercial photography with personality
- Exaggerated illustration and character design

Use with caution for:
- Serious, solemn, or tragic subjects
- Minimal or meditative aesthetics
- Photorealism without stylization
- Formal or corporate contexts (unless intentionally subverting them)

These parameters represent one approach to visual comedy. Other comedy traditions exist. This vocabulary focuses on physical, rhythmic, and exaggeration-based humor.

## Implementation Details

### Dependencies

- Python 3.8+
- fastmcp (for MCP server)
- No external API calls
- All operations deterministic and local

### File Structure

```
slapstick-enhancer/
├── slapstick_enhancer_mcp.py      # MCP interface and intent morphisms
├── slapstick_parameters.py         # Parameter definitions and descriptions
├── slapstick_principles.py         # Comedy principle definitions
├── requirements.txt                # Dependencies
└── README.md                        # This file
```

### Performance

- Cold start: ~50ms (initialization)
- Intent morphism: <1ms (dictionary lookup)
- Per-query: <5ms (parameter calculation)
- Token cost: Single LLM call for synthesis

## Contributing

This vocabulary is designed to be forked and modified for your specific slapstick language. If you develop variations:

1. Document your morphism logic and why you made changes
2. Test parameter combinations for internal consistency
3. Consider how your changes affect composition with other vocabularies
4. Share your work and the reasoning behind it

## References

Slapstick design principles derive from:
- Classical slapstick comedy (Chaplin, Keaton, Lloyd)
- Contemporary animation and character animation principles
- Graphic design and visual rhythm theory
- Classical comedy structure (setup, timing, punchline)

## License

[Specify your license here]

## Related

Part of the visual vocabularies ecosystem:
- [Cocktail Aesthetics](link)
- [Magazine Photography Aesthetics](link)
- [Terpene-based Aesthetics](link)
- [Constellation Composition](link)

See the visual vocabularies intro post for context on how these systems work together.

## Questions?

Open an issue or reach out. This is an active project exploring how deterministic comedy principles can enhance creative AI workflows.
