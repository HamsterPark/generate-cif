# generate-cif

A Python script for generating CIF (Crystallographic Information File) files from atomic position data.

## Features

- Generate standard CIF files from lattice parameters, symmetry operations, and atomic coordinates
- Flexible API — easily adaptable to any crystal structure
- Includes a built-in example: **Al₂(MoO₄)₃** (Aluminum Molybdate, space group P2₁/a)

## Usage

### Quick Start

Run directly to generate the example CIF file:

```bash
python generate_cif.py
```

This will produce `Al2Mo3O12.cif` in the current directory.

### Custom Crystal Structure

Import the `generate_cif` function and provide your own parameters:

```python
from generate_cif import generate_cif

generate_cif(
    filename="output.cif",
    formula="Na1 Cl1",
    name="Sodium Chloride",
    a=5.6402, b=5.6402, c=5.6402,
    alpha=90.00, beta=90.00, gamma=90.00,
    space_group_name="F m -3 m",
    space_group_number=225,
    symmetry_ops=["x, y, z", ...],
    atoms=[
        {"label": "Na1", "symbol": "Na", "x": 0.0, "y": 0.0, "z": 0.0, "occ": 1.0, "u_iso": 0.01},
        {"label": "Cl1", "symbol": "Cl", "x": 0.5, "y": 0.5, "z": 0.5, "occ": 1.0, "u_iso": 0.01},
    ],
)
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `filename` | `str` | Output file name (e.g. `"NaCl.cif"`) |
| `formula` | `str` | Chemical formula (e.g. `"Na1 Cl1"`) |
| `name` | `str` | Compound name |
| `a, b, c` | `float` | Lattice parameters in Å |
| `alpha, beta, gamma` | `float` | Lattice angles in degrees |
| `space_group_name` | `str` | Hermann–Mauguin symbol |
| `space_group_number` | `int` | Space group number |
| `symmetry_ops` | `list[str]` | Symmetry operation strings |
| `atoms` | `list[dict]` | Atom list with keys: `label`, `symbol`, `x`, `y`, `z`, `occ`, `u_iso` |

## Requirements

Python 3.6+ (no external dependencies)

## License

MIT
