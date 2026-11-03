# Renal Free Water Clearance Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Osmolar Clearance ($C_{\text{osm}}$), Free Water Clearance ($C_{\text{H}_2\text{O}}$), Solute-Free Water Reabsorption ($T^c_{\text{H}_2\text{O}}$), and Electrolyte-Free Water Clearance ($E\text{-FWC}$).

## Architecture

```mermaid
flowchart TD
    A[Urine Vol & Collection Time] --> B[Urine Flow Rate V mL/min]
    B --> C[U_osm & P_osm Ratio]
    C --> D[Osmolar Clearance Cosm]
    D --> E[Free Water Clearance CH2O = V - Cosm]
    E --> F[ADH Activity & Diuresis Stratification]
```

## Quickstart

```python
from client import FreeWaterClearanceClient

client = FreeWaterClearanceClient()
result = client.evaluate_water_clearance(
    urine_volume_ml=48.0,
    collection_duration_min=60.0,
    urine_osmolality_mosm_kg=850.0,
    plasma_osmolality_mosm_kg=290.0,
    urine_sodium_meq_l=90.0,
    urine_potassium_meq_l=45.0,
    plasma_sodium_meq_l=140.0
)
print(result)
```

## License

Apache-2.0
