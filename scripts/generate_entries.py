#!/usr/bin/env python3
"""
Script to generate pending entries for the queue.
Run this multiple times to append more entries.
"""

import json
import os

QUEUE_FILE = "queue/pending_entries.json"


def load_existing_queue():
    """Load existing queue or return empty list"""
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    return []


def save_queue(queue):
    """Save queue to file"""
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)


def generate_batch_1():
    """Generate first batch of 50 entries - Common compounds and correlations"""
    entries = []

    # Batch 1: Common Industrial Compounds (20 entries)
    compounds = [
        {"type": "compound", "name": "Ethanol", "formula": "C2H5OH", "molecular_weight": 46.07, "boiling_point_c": 78.37, "density_kg_m3": 789, "cas_number": "64-17-5"},
        {"type": "compound", "name": "Methanol", "formula": "CH3OH", "molecular_weight": 32.04, "boiling_point_c": 64.7, "density_kg_m3": 792, "cas_number": "67-56-1"},
        {"type": "compound", "name": "Acetone", "formula": "C3H6O", "molecular_weight": 58.08, "boiling_point_c": 56.05, "density_kg_m3": 784, "cas_number": "67-64-1"},
        {"type": "compound", "name": "Benzene", "formula": "C6H6", "molecular_weight": 78.11, "boiling_point_c": 80.1, "density_kg_m3": 876, "cas_number": "71-43-2"},
        {"type": "compound", "name": "Toluene", "formula": "C7H8", "molecular_weight": 92.14, "boiling_point_c": 110.6, "density_kg_m3": 867, "cas_number": "108-88-3"},
        {"type": "compound", "name": "Acetic Acid", "formula": "CH3COOH", "molecular_weight": 60.05, "boiling_point_c": 118.1, "density_kg_m3": 1049, "cas_number": "64-19-7"},
        {"type": "compound", "name": "Chloroform", "formula": "CHCl3", "molecular_weight": 119.38, "boiling_point_c": 61.2, "density_kg_m3": 1480, "cas_number": "67-66-3"},
        {"type": "compound", "name": "Ethylene Glycol", "formula": "C2H6O2", "molecular_weight": 62.07, "boiling_point_c": 197.3, "density_kg_m3": 1113, "cas_number": "107-21-1"},
        {"type": "compound", "name": "Propylene", "formula": "C3H6", "molecular_weight": 42.08, "boiling_point_c": -47.6, "density_kg_m3": 514, "cas_number": "115-07-1"},
        {"type": "compound", "name": "Styrene", "formula": "C8H8", "molecular_weight": 104.15, "boiling_point_c": 145.2, "density_kg_m3": 906, "cas_number": "100-42-5"},
        {"type": "compound", "name": "Ammonia", "formula": "NH3", "molecular_weight": 17.03, "boiling_point_c": -33.34, "density_kg_m3": 682, "cas_number": "7664-41-7"},
        {"type": "compound", "name": "Sulfuric Acid", "formula": "H2SO4", "molecular_weight": 98.08, "boiling_point_c": 337, "density_kg_m3": 1840, "cas_number": "7664-93-9"},
        {"type": "compound", "name": "Nitric Acid", "formula": "HNO3", "molecular_weight": 63.01, "boiling_point_c": 83, "density_kg_m3": 1513, "cas_number": "7697-37-2"},
        {"type": "compound", "name": "Hydrogen Peroxide", "formula": "H2O2", "molecular_weight": 34.01, "boiling_point_c": 150.2, "density_kg_m3": 1450, "cas_number": "7722-84-1"},
        {"type": "compound", "name": "Carbon Tetrachloride", "formula": "CCl4", "molecular_weight": 153.82, "boiling_point_c": 76.72, "density_kg_m3": 1594, "cas_number": "56-23-5"},
        {"type": "compound", "name": "Formaldehyde", "formula": "CH2O", "molecular_weight": 30.03, "boiling_point_c": -19.3, "density_kg_m3": 815, "cas_number": "50-00-0"},
        {"type": "compound", "name": "Phenol", "formula": "C6H5OH", "molecular_weight": 94.11, "boiling_point_c": 181.7, "density_kg_m3": 1071, "cas_number": "108-95-2"},
        {"type": "compound", "name": "Aniline", "formula": "C6H5NH2", "molecular_weight": 93.13, "boiling_point_c": 184.1, "density_kg_m3": 1022, "cas_number": "62-53-3"},
        {"type": "compound", "name": "Ethyl Acetate", "formula": "C4H8O2", "molecular_weight": 88.11, "boiling_point_c": 77.1, "density_kg_m3": 902, "cas_number": "141-78-6"},
        {"type": "compound", "name": "Diethyl Ether", "formula": "C4H10O", "molecular_weight": 74.12, "boiling_point_c": 34.6, "density_kg_m3": 714, "cas_number": "60-29-7"},
    ]

    # Batch 1: Important Correlations (15 entries)
    correlations = [
        {"type": "correlation", "name": "Antoine Equation", "description": "Vapor pressure correlation", "equation": "log10(P) = A - B/(C + T)", "variables": "A, B, C, T", "source": "Antoine (1888)"},
        {"type": "correlation", "name": "Ergun Equation", "description": "Pressure drop in packed beds", "equation": "ΔP/L = 150*μ*u*(1-ε)²/(ε³*dp²) + 1.75*ρ*u²*(1-ε)/(ε³*dp)", "variables": "μ, u, ε, dp, ρ", "source": "Ergun (1952)"},
        {"type": "correlation", "name": "Raoult's Law", "description": "Ideal vapor-liquid equilibrium", "equation": "y_i*P = x_i*P_i_sat", "variables": "y_i, x_i, P, P_i_sat", "source": "Raoult (1887)"},
        {"type": "correlation", "name": "Fanning Friction Factor", "description": "Friction factor for turbulent flow", "equation": "f = 0.079/Re^0.25", "variables": "Re", "source": "Fanning correlation"},
        {"type": "correlation", "name": "Hagen-Poiseuille Equation", "description": "Pressure drop in laminar pipe flow", "equation": "ΔP = 32*μ*L*v/(D²)", "variables": "μ, L, v, D", "source": "Hagen-Poiseuille"},
        {"type": "correlation", "name": "Darcy-Weisbach Equation", "description": "Pressure drop in pipes", "equation": "ΔP = f*(L/D)*(ρ*v²/2)", "variables": "f, L, D, ρ, v", "source": "Darcy-Weisbach"},
        {"type": "correlation", "name": "Churchill Equation", "description": "Friction factor for all flow regimes", "equation": "f = 8*[(8/Re)^12 + (A+B)^(-1.5)]^(1/12)", "variables": "Re, A, B", "source": "Churchill (1977)"},
        {"type": "correlation", "name": "Clausius-Clapeyron Equation", "description": "Temperature dependence of vapor pressure", "equation": "dP/dT = ΔH_vap/(T*ΔV)", "variables": "P, T, ΔH_vap, ΔV", "source": "Clausius-Clapeyron"},
        {"type": "correlation", "name": "Van der Waals Equation", "description": "Real gas equation of state", "equation": "(P + a/V²)*(V - b) = R*T", "variables": "P, V, T, a, b, R", "source": "Van der Waals (1873)"},
        {"type": "correlation", "name": "Redlich-Kwong Equation", "description": "Improved real gas equation", "equation": "P = R*T/(V-b) - a/(T^0.5*V*(V+b))", "variables": "P, V, T, a, b, R", "source": "Redlich-Kwong (1949)"},
        {"type": "correlation", "name": "Peng-Robinson EOS", "description": "Cubic equation of state", "equation": "P = R*T/(V-b) - a*α/(V²+2*b*V-b²)", "variables": "P, V, T, a, b, α, R", "source": "Peng-Robinson (1976)"},
        {"type": "correlation", "name": "Arrhenius Equation", "description": "Temperature dependence of reaction rates", "equation": "k = A*exp(-E_a/(R*T))", "variables": "k, A, E_a, R, T", "source": "Arrhenius (1889)"},
        {"type": "correlation", "name": "Langmuir Isotherm", "description": "Adsorption equilibrium", "equation": "q = q_max*K*C/(1 + K*C)", "variables": "q, q_max, K, C", "source": "Langmuir (1916)"},
        {"type": "correlation", "name": "BET Isotherm", "description": "Multilayer adsorption", "equation": "V/V_m = C*P/((P_0-P)*(1+(C-1)*P/P_0))", "variables": "V, V_m, C, P, P_0", "source": "Brunauer-Emmett-Teller (1938)"},
        {"type": "correlation", "name": "Nusselt Number Correlation", "description": "Heat transfer in pipes", "equation": "Nu = 0.023*Re^0.8*Pr^0.33", "variables": "Re, Pr", "source": "Dittus-Boelter"},
    ]

    # Batch 1: Fundamental Constants (15 entries)
    constants = [
        {"type": "constant", "name": "Universal Gas Constant", "symbol": "R", "value": "8.314", "units": "J/(mol·K)", "context": "Ideal gas law and thermodynamics"},
        {"type": "constant", "name": "Avogadro's Number", "symbol": "N_A", "value": "6.022e23", "units": "1/mol", "context": "Number of particles per mole"},
        {"type": "constant", "name": "Boltzmann Constant", "symbol": "k_B", "value": "1.381e-23", "units": "J/K", "context": "Statistical mechanics and kinetic theory"},
        {"type": "constant", "name": "Planck Constant", "symbol": "h", "value": "6.626e-34", "units": "J·s", "context": "Quantum mechanics"},
        {"type": "constant", "name": "Speed of Light", "symbol": "c", "value": "2.998e8", "units": "m/s", "context": "Electromagnetic radiation"},
        {"type": "constant", "name": "Standard Pressure", "symbol": "P_std", "value": "101325", "units": "Pa", "context": "Standard atmospheric pressure (1 atm)"},
        {"type": "constant", "name": "Standard Temperature", "symbol": "T_std", "value": "273.15", "units": "K", "context": "Standard temperature (0°C)"},
        {"type": "constant", "name": "Faraday Constant", "symbol": "F", "value": "96485", "units": "C/mol", "context": "Electrochemistry"},
        {"type": "constant", "name": "Gravitational Acceleration", "symbol": "g", "value": "9.807", "units": "m/s²", "context": "Earth's surface gravity"},
        {"type": "constant", "name": "Stefan-Boltzmann Constant", "symbol": "σ", "value": "5.670e-8", "units": "W/(m²·K⁴)", "context": "Thermal radiation"},
        {"type": "constant", "name": "Water Density at STP", "symbol": "ρ_water", "value": "1000", "units": "kg/m³", "context": "Reference density for water"},
        {"type": "constant", "name": "Air Density at STP", "symbol": "ρ_air", "value": "1.225", "units": "kg/m³", "context": "Reference density for air"},
        {"type": "constant", "name": "Water Heat of Vaporization", "symbol": "ΔH_vap_water", "value": "2257", "units": "kJ/kg", "context": "Latent heat at 100°C"},
        {"type": "constant", "name": "Water Specific Heat", "symbol": "Cp_water", "value": "4.186", "units": "kJ/(kg·K)", "context": "Specific heat capacity of liquid water"},
        {"type": "constant", "name": "Air Viscosity at 20C", "symbol": "μ_air", "value": "1.81e-5", "units": "Pa·s", "context": "Dynamic viscosity of air at 20°C"},
    ]

    entries.extend(compounds)
    entries.extend(correlations)
    entries.extend(constants)

    return entries


def main():
    print("Loading existing queue...")
    queue = load_existing_queue()
    print(f"Current queue size: {len(queue)}")

    print("\nGenerating Batch 1 (50 entries)...")
    new_entries = generate_batch_1()

    queue.extend(new_entries)

    print(f"Added {len(new_entries)} entries")
    print(f"New total: {len(queue)} entries")

    save_queue(queue)
    print(f"\nQueue saved to {QUEUE_FILE}")


if __name__ == "__main__":
    main()
