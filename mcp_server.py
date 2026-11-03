"""
MCP Server for Renal Free Water Clearance Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import FreeWaterClearanceClient


def main():
    client = FreeWaterClearanceClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_water_clearance",
                            "description": "Calculates renal Osmolar Clearance (Cosm), Free Water Clearance (CH2O), Negative Free Water Clearance (Tc_H2O), and Electrolyte-Free Water Clearance (E-FWC).",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "urine_volume_ml": {
                                        "type": "number",
                                        "description": "Total urine volume collected (mL)."
                                    },
                                    "collection_duration_min": {
                                        "type": "number",
                                        "description": "Duration of urine collection in minutes (e.g. 60 min or 1440 min)."
                                    },
                                    "urine_osmolality_mosm_kg": {
                                        "type": "number",
                                        "description": "Urine osmolality in mOsm/kg H2O."
                                    },
                                    "plasma_osmolality_mosm_kg": {
                                        "type": "number",
                                        "description": "Plasma osmolality in mOsm/kg H2O."
                                    },
                                    "urine_sodium_meq_l": {
                                        "type": "number",
                                        "description": "Urine sodium concentration in mEq/L (optional)."
                                    },
                                    "urine_potassium_meq_l": {
                                        "type": "number",
                                        "description": "Urine potassium concentration in mEq/L (optional)."
                                    },
                                    "plasma_sodium_meq_l": {
                                        "type": "number",
                                        "description": "Plasma sodium concentration in mEq/L (optional)."
                                    }
                                },
                                "required": [
                                    "urine_volume_ml",
                                    "collection_duration_min",
                                    "urine_osmolality_mosm_kg",
                                    "plasma_osmolality_mosm_kg"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_water_clearance":
                try:
                    out = client.evaluate_water_clearance(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
