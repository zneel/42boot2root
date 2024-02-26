import math

def parse_instruction(instruction):
    parts = instruction.split()
    action = parts[0].lower()
    return action

def parse_rotation():
    parts = instruction.split()
    direction = parts[1].lower()
    value = int(parts[3])
    return direction, value

def parse_move():
    parts = instruction.split()
    value = int(parts[1])
    return value

def calculate_destination(instructions):
    x, y = 0, 0
    angle = 0  # Angle en degres

    for instruction in instructions:
        action = parse_instruction(instruction)

        if action == 'avance':
            value = parse_move(instruction)
            x += value * math.cos(math.radians(angle))
            y += value * math.sin(math.radians(angle))
        elif action == 'recule':
            value = parse_move(instruction)
            x -= value * math.cos(math.radians(angle))
            y -= value * math.sin(math.radians(angle))
        elif action == 'tourne':
            direction, value = parse_rotation(instruction)
            if direction == 'gauche':
                angle += value
            else:
                angle -= value

    return x, y

# Votre sequence d'instructions
instructions = """
Tourne gauche de 90 degrees
Avance 50 spaces
Avance 1 spaces
Tourne gauche de 1 degrees
Avance 1 spaces
# ... (copiez et collez le reste de vos instructions ici)
"""

instructions = [line.strip() for line in instructions.split('\n') if line.strip() and not line.strip().startswith('#')]

# Calcul de la destination finale
destination = calculate_destination(instructions)
print("Destination finale :", destination)
