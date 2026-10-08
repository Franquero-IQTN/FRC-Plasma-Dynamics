# Plasma-Toolkit: Multi-Particle FRC Plasma Simulation Engine

Welcome to the **Plasma-Toolkit**, a specialized computational module under the **Franquero Institute for Quantum-Thermodynamic Neuroscience (Franquero-IQTN)**. This repository houses the simulation code and logic for modeling high temperature plasma fusion alongside multi particle isotope expansion.

---

## Overview

Simulating high temperature plasma fusion alongside standard electron based chemistry requires moving beyond rigid periodic table datasets. This toolkit introduces an **isotope expansion architecture** and a distinct logic branch designed to handle arbitrary reactant pools and nuclear cross sections for Field Reversed Configuration (FRC) research.

---

## Core Features

1. **Custom Isotope Injection:** 
   * Manually appends specialized fusion fuels including **Deuterium (D)**, **Tritium (T)**, **Helium-3 (He3)**, and **Boron-11 (B11)** into the active element dataframes and UI dropdowns.
2. **Dynamic Multi-Slot UI:** 
   * Utilizes a dynamic layout (`ipywidgets.VBox`) rather than rigid dropdowns, allowing researchers to stack 3, 4, 5, or more elements into a single active "plasma pool".
3. **Thermodynamic Thresholding:** 
   * Features an environment toggle allowing users to switch between **Standard Chemistry** and **Fusion Plasma (keV)** regimes, completely bypassing covalent/ionic bond logic when plasma parameters are active.
4. **Fusion Reaction & Quench Matrix:** 
   * Automatically scans selected particle pools for primary fusion cross-sections (D-T, D-D, aneutronic p-B11) and flags high-Z impurities (such as Iodine or Tungsten) as radiative quenchants where Bremsstrahlung losses scale with $Z^2$.

---

## Requirements & Dependencies

The simulation script requires Python along with interactive widgets:
* Python 3.11+
* `ipywidgets`
* `IPython.display`

---

## Usage (Carnets Plus / Jupyter Environment)

1. Load the script into an interactive Python environment supporting Jupyter extensions or Carnets Plus.
2. Select your environment mode using the **Environment** radio buttons.
3. Adjust the **Reactants** slider to scale your plasma pool.
4. Choose your particle compositions and click **Simulate Plasma** to evaluate cross sections and radiative quench warnings.

---

## Institutional Structure & License

* **Organization:** Franquero IQTN
* **Hardware & Systems Development:** Franquero's Prototyping Laboratories LLC
* **License:** Distributed under the **MIT License**. See the `LICENSE` file for details.

