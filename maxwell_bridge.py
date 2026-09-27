# maxwell_bridge.py
# Program to calculate unknown inductance
# using Maxwell's Inductance Bridge

print("=== Maxwell's Inductance Bridge ===")

# Input values
R2 = float(input("Enter R2 (Ohm): "))
R3 = float(input("Enter R3 (Ohm): "))
R4 = float(input("Enter R4 (Ohm): "))
C4 = float(input("Enter C4 (Farad): "))

# Calculate unknown resistance
R1 = (R2 * R3) / R4

# Calculate unknown inductance
L1 = R2 * R3 * C4

# Display results
print("\n--- Maxwell Bridge Results ---")
print(f"R1 = {R1:.4f} Ohm")
print(f"Unknown Inductance L1 = {L1:.6f} H")
print(f"Unknown Inductance L1 = {L1 * 1000:.3f} mH")
