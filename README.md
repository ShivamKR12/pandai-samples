# PandAI Pathfinding & Dynamic NavMesh Samples

An interactive pathfinding, obstacle avoidance, and dynamic navigation mesh (NavMesh) generation showcase built using the [Panda3D](https://www.panda3d.org/) game engine and the `panda3d.ai` (PandAI) module.

This repository demonstrates runtime NavMesh construction from 3D models and collision primitives, dynamic placement of obstacle boundaries over terrain, and A* pathfinding character traversal.

## 🌟 Key Features

- **Dynamic Obstacle Avoidance**: Add wall boundaries and obstacle primitives over terrain at runtime while updating NavMesh connectivity.
- **NavMesh Generation (`NavMeshGenerator.py`)**: Automatically parse `.egg` geometries into connected navigation nodes and export pathfinding graphs (`navmesh.csv`).
- **Egg Primitive Creation (`EggPrimitiveCreation.py`)**: Procedurally generates collision meshes and egg geometry for bounding boxes, walls, and spheres.
- **Minimal Reproducible Example (`MRE.py`)**: A clean, self-contained implementation demonstrating camera setup, lighting, Ralph character actor, NavMesh building, and target-seeking AI.

## 🕹️ Controls (in `main.py`)

- **Enter**: Start Pathfinding (triggers Ralph character to navigate around obstacles to the target)
- **Arrow Keys**: Move Target / Pointer location
- **1**: Add Wall Boundary Section
- **i**: Load Default Wall Boundaries
- **F3**: Toggle Wireframe View
- **p**: Perspective Camera View
- **r**: Reset / Top-Down Camera View
- **0**: Capture Screenshot
- **Esc**: Quit

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamKR12/pandai-samples.git
   cd pandai-samples
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux / macOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the interactive sample:
   ```bash
   python main.py
   ```
   *(or run the minimal pathfinding demo: `python MRE.py`)*

## 🛠️ Project Structure

```
pandai-samples/
├── EggPrimitiveCreation.py  # Procedural egg collision & mesh builder
├── GridNode.py              # Grid graph node representation
├── NavMeshGenerator.py      # NavMesh generator parsing egg polygons into csv graphs
├── main.py                  # Full interactive tutorial demo with dynamic obstacles
├── MRE.py                   # Minimal reproducible PandAI pathfinding example
├── navmesh.csv              # Exported navigation graph data
├── wall_positions.txt       # Coordinates of placed obstacles
└── models/                  # 3D arena models, sphere pointers, and Ralph character
```

## 📜 Credits & Tech Stack

- **Game Engine**: [Panda3D](https://www.panda3d.org/)
- **AI Library**: `panda3d.ai` (PandAI)
- **Language**: Python 3

