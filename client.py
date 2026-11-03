"""
Renal Free Water Clearance & Tubular Solute Transport Client.
Zero-mock pure Python standard library implementation.
Calculates Osmolar Clearance (Cosm), Free Water Clearance (CH2O),
Negative Free Water Clearance (Tc_H2O), and Electrolyte-Free Water Clearance (E-FWC).
"""

import math
from typing import Dict, Any, Optional


class FreeWaterClearanceClient:
    """
    Evaluates renal water balance and collecting duct aquaporin-2 response to ADH:
    Urine flow rate V (mL/min) = urine_volume_ml / collection_duration_min
    Cosm = (U_osm * V) / P_osm
    CH2O = V - Cosm
    Tc_H2O = -CH2O = Cosm - V (solute-free water reabsorption)
    E-FWC = V * (1 - (U_Na + U_K) / P_Na)
    """

    def __init__(self):
        pass

    def evaluate_water_clearance(
        self,
        urine_volume_ml: float,
        collection_duration_min: float,
        urine_osmolality_mosm_kg: float,
        plasma_osmolality_mosm_kg: float,
        urine_sodium_meq_l: Optional[float] = None,
        urine_potassium_meq_l: Optional[float] = None,
        plasma_sodium_meq_l: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates renal free water clearance metrics.
        urine_volume_ml: total urine volume during timed collection (mL)
        collection_duration_min: duration of urine collection in minutes (e.g. 60 min, 1440 min for 24h)
        urine_osmolality_mosm_kg: U_osm (mOsm/kg H2O)
        plasma_osmolality_mosm_kg: P_osm (mOsm/kg H2O)
        urine_sodium_meq_l, urine_potassium_meq_l, plasma_sodium_meq_l: optional for E-FWC
        """
        if urine_volume_ml <= 0 or collection_duration_min <= 0:
            raise ValueError("Urine volume and collection duration must be strictly positive.")
        if urine_osmolality_mosm_kg <= 0 or plasma_osmolality_mosm_kg <= 0:
            raise ValueError("Osmolality values must be strictly positive.")

        # Urine flow rate V in mL/min
        v_flow_rate = urine_volume_ml / collection_duration_min

        # Osmolar clearance Cosm (mL/min)
        c_osm = (urine_osmolality_mosm_kg * v_flow_rate) / plasma_osmolality_mosm_kg

        # Free water clearance CH2O (mL/min)
        c_h2o = v_flow_rate - c_osm

        # Tubular solute-free water reabsorption Tc_H2O (mL/min)
        tc_h2o = c_osm - v_flow_rate

        # Electrolyte-free water clearance E-FWC
        e_fwc = None
        if urine_sodium_meq_l is not None and urine_potassium_meq_l is not None and plasma_sodium_meq_l is not None:
            if plasma_sodium_meq_l > 0:
                e_fwc = round(v_flow_rate * (1.0 - ((urine_sodium_meq_l + urine_potassium_meq_l) / plasma_sodium_meq_l)), 2)

        # Clinical interpretation:
        # CH2O > 0: Water diuresis (excreting hypotonic urine, suppressed ADH / diabetes insipidus or high water intake)
        # CH2O < 0: Antidiuresis / Water conservation (excreting hypertonic urine, active ADH, dehydration, SIADH)
        # CH2O == 0: Isosthenuria (urine is isosmolar to plasma, tubular unresponsiveness or renal failure)
        u_p_ratio = urine_osmolality_mosm_kg / plasma_osmolality_mosm_kg

        if c_h2o > 0.5:
            state = "Positive Free Water Clearance (Water Diuresis)"
            adh_status = "Suppressed ADH action or vasopressin receptor unresponsiveness."
            clinical_risk = "Hypotonic polyuria; differential includes central/nephrogenic diabetes insipidus or psychogenic polydipsia."
        elif c_h2o < -0.5:
            state = "Negative Free Water Clearance (Antidiuresis / Water Conservation)"
            adh_status = "Active ADH-mediated medullary water reabsorption."
            clinical_risk = "Normal physiological response to dehydration or pathological SIADH / hypovolemia."
        else:
            state = "Isosmotic Excretion (Isosthenuria)"
            adh_status = "Impaired urinary concentrating and diluting ability."
            clinical_risk = "Tubulointerstitial nephropathy or acute tubular injury."

        return {
            "status": "success",
            "clearance_rates_ml_min": {
                "urine_flow_rate_v": round(v_flow_rate, 2),
                "osmolar_clearance_c_osm": round(c_osm, 2),
                "free_water_clearance_c_h2o": round(c_h2o, 2),
                "tubular_free_water_reabsorption_tc_h2o": round(tc_h2o, 2),
                "electrolyte_free_water_clearance_e_fwc": e_fwc
            },
            "osmolar_ratios": {
                "urine_plasma_osmolality_ratio": round(u_p_ratio, 2),
                "urine_osmolality_mosm_kg": urine_osmolality_mosm_kg,
                "plasma_osmolality_mosm_kg": plasma_osmolality_mosm_kg
            },
            "interpretation": {
                "physiological_state": state,
                "adh_activity": adh_status,
                "clinical_risk_profile": clinical_risk
            }
        }
