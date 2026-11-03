---
name: genpark-personal-agent-renal-free-water-clearance-ch2o-skill
version: 1.0.0
description: Calculates renal Osmolar Clearance (Cosm), Free Water Clearance (CH2O), Negative Free Water Clearance (Tc_H2O), and Electrolyte-Free Water Clearance (E-FWC).
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - renal
  - nephrology
  - free-water-clearance
  - ch2o
  - osmoregulation
  - zero-dependency
---

# Renal Free Water Clearance Skill

## Mathematical Formulation

Urine flow rate:

$$V = \frac{\text{Urine Volume}}{\text{Collection Time}} \quad (\text{mL/min})$$

Osmolar clearance:

$$C_{\text{osm}} = \frac{U_{\text{osm}} \times V}{P_{\text{osm}}} \quad (\text{mL/min})$$

Free water clearance:

$$C_{\text{H}_2\text{O}} = V - C_{\text{osm}} \quad (\text{mL/min})$$

Tubular solute-free water reabsorption:

$$T^c_{\text{H}_2\text{O}} = -C_{\text{H}_2\text{O}} = C_{\text{osm}} - V \quad (\text{mL/min})$$

Electrolyte-free water clearance:

$$E\text{-FWC} = V \times \left(1 - \frac{U_{\text{Na}} + U_{\text{K}}}{P_{\text{Na}}}\right)$$

## Clinical Interpretation
- **$C_{\text{H}_2\text{O}} > 0$**: Positive free water clearance (water diuresis, hypotonic urine, diabetes insipidus, suppressed ADH).
- **$C_{\text{H}_2\text{O}} < 0$**: Negative free water clearance / antidiuresis (concentrated urine, high ADH, dehydration, SIADH).
- **$C_{\text{H}_2\text{O}} \approx 0$**: Isosthenuria (loss of tubular concentrating and diluting gradient).
