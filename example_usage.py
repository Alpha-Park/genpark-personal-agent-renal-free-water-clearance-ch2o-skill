"""
Example usage of Renal Free Water Clearance Skill.
Demonstrates physiological dehydration antidiuresis vs water diuresis / diabetes insipidus.
"""

import json
from client import FreeWaterClearanceClient


def main():
    print("=== Testing Renal Free Water Clearance Skill ===")
    client = FreeWaterClearanceClient()

    # 1. Antidiuresis / Water conservation (U_osm = 850 mOsm, P_osm = 290 mOsm, V = 0.8 mL/min -> Cosm ~ 2.34 mL/min, CH2O ~ -1.54 mL/min)
    res_antidiuresis = client.evaluate_water_clearance(
        urine_volume_ml=48.0,
        collection_duration_min=60.0,
        urine_osmolality_mosm_kg=850.0,
        plasma_osmolality_mosm_kg=290.0,
        urine_sodium_meq_l=90.0,
        urine_potassium_meq_l=45.0,
        plasma_sodium_meq_l=140.0
    )
    print("\n[Case 1: Dehydration / Concentrated Urine (Antidiuresis)]")
    print(json.dumps(res_antidiuresis, indent=2))

    # 2. Water diuresis / Diabetes insipidus (U_osm = 90 mOsm, P_osm = 295 mOsm, V = 8.0 mL/min -> Cosm ~ 2.44 mL/min, CH2O ~ +5.56 mL/min)
    res_diuresis = client.evaluate_water_clearance(
        urine_volume_ml=480.0,
        collection_duration_min=60.0,
        urine_osmolality_mosm_kg=90.0,
        plasma_osmolality_mosm_kg=295.0,
        urine_sodium_meq_l=15.0,
        urine_potassium_meq_l=8.0,
        plasma_sodium_meq_l=142.0
    )
    print("\n[Case 2: Water Diuresis / Polyuria]")
    print(json.dumps(res_diuresis, indent=2))

    # Assertions
    assert res_antidiuresis["clearance_rates_ml_min"]["free_water_clearance_c_h2o"] < 0
    assert "Negative" in res_antidiuresis["interpretation"]["physiological_state"]
    assert res_diuresis["clearance_rates_ml_min"]["free_water_clearance_c_h2o"] > 0
    assert "Positive" in res_diuresis["interpretation"]["physiological_state"]
    print("\n[SUCCESS] Free Water Clearance tests passed!")


if __name__ == "__main__":
    main()
