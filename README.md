# Floorpy
This code is a system designed for generating, evaluating, and optimizing floorplans using genetic algorithms and tree-based subdivision techniques. It uses various evaluators and generators to create, refine, and score floorplans.

## Key Components:
### garbage_fire:

Calls the PopulationCentrifuge class to generate an optimized floorplan based on genetic algorithms.
It creates a "perfect" floorplan using the create_perfect_floorplan method of PopulationCentrifuge, which iteratively optimizes room layouts and door placements.
Optionally renders the resulting floorplan as an SVG using SvgRenderer (commented out).
### get_floorplan:

Loads a saved floorplan from a file using load_floorplan, which retrieves a FloorplanDNA object.
Reinstantiates the floorplan using the SubdivideTreeToFloorplan class, which takes the saved room data, tree structure, and dimensions to regenerate the floorplan.
Returns the floorplan object (fp).
### autofrob_tree_evaluator_weights:

Runs a genetic algorithm to optimize the weights used in the tree evaluator (likely for better scoring floorplans).
Reads pairs of floorplans from a file (scores.txt) where one is considered better than the other. These pairs are used to guide the optimization process.
Uses the GeneticWeightFrobber class to adjust the weights and improve the evaluation system, running through generations to refine the weights.
### manual_score:

Manually loads a specific floorplan (defined by the plan variable) and evaluates it using FloorplanEvaluator.
Outputs the score of the floorplan to the console.
### Additional Elements:
Randomness (bakedrandom): Random number generation is used in various parts of the floorplan generation process (e.g., subdivision, door placement).
## Evaluation:
CompositeEvaluator and BasicEvaluators (from the import) suggest the floorplan is evaluated based on a combination of criteria.
GeneticWeightFrobber attempts to optimize the evaluator weights based on performance across different generations.
Visualization: SvgRenderer (commented out in some places) is likely used to render floorplans as SVG images for visualization purposes.
## Functions Overview:
garbage_fire: Generates an optimal floorplan using genetic algorithms.
get_floorplan: Loads a previously saved floorplan and re-instantiates it.
autofrob_tree_evaluator_weights: Optimizes the weights of the tree evaluator through genetic algorithms, using pairwise comparisons of floorplans.
manual_score: Loads and scores a specific floorplan, outputting the result.
## Main Execution:
The main block (if __name__ == "__main__") calls the garbage_fire() function to generate and potentially render a floorplan. Other functions, such as manual_score() and autofrob_tree_evaluator_weights(), are commented out, suggesting they can be used when needed for scoring or weight optimization tasks.
