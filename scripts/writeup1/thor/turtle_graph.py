import math
import matplotlib.pyplot as plt

def parse_instruction(instruction):
        parts = instruction.split(' ')
        action = parts[0].lower()
        return action

def parse_rotation(instruction):
        parts = instruction.split(' ')
        direction = parts[1].lower()
        value = int(parts[3])
        return direction, value

def parse_move(instruction):
        parts = instruction.split(' ')
        value = int(parts[1])
        return value

def calculate_destination(instructions):
        x, y = 0, 0
        angle = 90
        paths=[[(x, y)]]

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
                elif action == '':
                    y = 0
                    x = len(paths) * 200
                    angle = 90
                    paths.append([(x, y)])
                paths[-1].append((x, y))
        return paths

def plot_movement(paths):
        for i, path in enumerate(paths):
            x_values, y_values = zip(*path)
            plt.plot(x_values, y_values, marker='o', linestyle='-', label=f'Curseur {i+1}')
        x_values, y_values = zip(*path)
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
        plt.title('Trace du Mouvement')
        plt.xlabel('Axe X')
        plt.ylabel('Axe Y')
        plt.legend()
        plt.grid(True)
        plt.show()


file = open('turtle','r')
content = file.read()
file.close()

instructions = content.strip('\n').split('\n')

paths = calculate_destination(instructions)
print(paths[-1])
plot_movement(paths)
