# Simple Generator
This code defines a **SimpleGenerator** class that generates a floorplan layout and places doors between rooms. Here’s what each part does:

1. **Initialization (`__init__`)**: Initializes the generator with the dimensions of the lot and a list of desired room types.

2. **get_largest_room**: Returns the room with the largest area from a list of rooms.

3. **get_random_point_in_room**: Selects a random point inside a room based on a Gaussian distribution around the room’s center.

4. **get_nearest_value**: Finds the nearest available value for a point coordinate (either `x` or `y`) within a specified search radius, adjusting to avoid previously used values.

5. **generate_candidate_floorplan**: 
   - Begins with a single large room and subdivides it into smaller rooms until the desired number of rooms is reached.
   - Subdivision occurs at randomly chosen points inside the largest room.
   - Two door generation methods are called: `add_doors_depth_first` and `add_doors_minimum_spanning_tree`.

6. **add_doors_depth_first**: 
   - Adds doors between rooms using a depth-first traversal.
   - It starts with one room and explores its neighbors. It places doors based on area-to-perimeter ratios between rooms to control door placement direction.

7. **add_doors_minimum_spanning_tree**: 
   - Builds a minimum spanning tree of room connections, ensuring all rooms are accessible through a minimal number of doors.
   - Doors are placed on the edges between connected rooms in the tree.

In summary, this code generates floorplans by subdividing rooms and adding doors between them in two phases: first using depth-first traversal, and then refining door placements using a minimum spanning tree algorithm to ensure optimal connectivity.


# Treejudge
This code defines a comprehensive system for generating and optimizing floorplans using a genetic algorithm and subdividing methods. Here's a breakdown of its key components and functionality:

### Key Classes and Functions:

1. **FloorplanDNA**: A `recordclass` to store a floorplan's metadata, including room list, dimensions, tree structure (`rootnode`), and door placements (`door_vector`). It acts as a snapshot of the floorplan for saving and loading.

2. **save_floorplan/load_floorplan**: Functions to serialize and deserialize `FloorplanDNA` objects using Python’s `pickle` module. These functions save or load the floorplan’s data into/from a `.pickle` file.

3. **FloorplanEvaluator**: 
   - Evaluates the quality of a floorplan based on weighted criteria applied to individual rooms (`score_floorplan`).
   - Scores the floorplan tree structure recursively (`score_tree`), ensuring the quality propagates up the hierarchy from child nodes to the root.

4. **PopulationCentrifuge**:
   - Handles the generation and optimization of floorplans and door placements.
   - **dump_plan**: Saves and renders a floorplan using `SvgRenderer` (which presumably generates an SVG visualization) and stores it as a file.
   - **create_perfect_floorplan**: 
     - Runs the main genetic algorithm to generate and refine floorplans over multiple generations.
     - Generates a tree structure of rooms using `SubdivideTreeGenerator` and instantiates a floorplan via `SubdivideTreeToFloorplan`.
     - Uses **GeneticTreeShaker** to evolve the subdivision tree and optimize the floorplan layout over 500 iterations.
     - After optimizing the layout, it runs **GeneticDoorShaker** to refine door placements across 200 iterations.
     - Tracks the best-scoring plan, based on composite scores (layout and door placement), and saves it when no further improvement is detected after several generations.
   
5. **SubdivideTreeGenerator** and **GeneticTreeShaker**:
   - **SubdivideTreeGenerator**: Generates an initial subdivision tree from room indexes, which will be optimized by the genetic algorithm.
   - **GeneticTreeShaker**: Applies genetic algorithm techniques (crossover, mutation, selection) to optimize the tree structure that defines how rooms are subdivided and laid out.

6. **GeneticDoorShaker**: 
   - Optimizes door placements by evolving door vectors through genetic algorithms.
   - A **door vector** encodes where doors are placed in the floorplan, and it is optimized by combining genetic operations (crossover, mutation) and scoring.

### Workflow Overview:

1. **Initial Room Layout**: 
   - A list of rooms (`list_o_rooms`) is defined with room types (e.g., living room, dining room, bedrooms, bathrooms).
   - A subdivision tree (`adam`) is generated, determining how the rooms will be arranged on the floorplan.

2. **Genetic Algorithm for Room Layout**: 
   - The `GeneticTreeShaker` optimizes the tree structure to generate the best possible room layout by evolving the tree through multiple generations, scoring each generation based on a weighted evaluation function.
   
3. **Genetic Algorithm for Door Placement**: 
   - Once the layout is optimized, the **GeneticDoorShaker** refines the door placements to ensure that the doors are optimally placed between rooms.

4. **Saving and Rendering**: 
   - The final optimized floorplan (including door placements) is saved and rendered as a file (SVG for visualization and `.pickle` for data).

### Summary:
This code generates optimized floorplans by combining genetic algorithms with subdivision tree techniques. It evolves both the room layout and door placements through multiple iterations, scoring each configuration to find the best possible design. The system is capable of saving and rendering the best results in each generation, ultimately producing a "perfect" floorplan based on the defined criteria.
