import ipywidgets as widgets
from IPython.display import display, clear_output

# 1. Manually add isotopes to your existing elements list
fusion_isotopes = [
    {'symbol': 'D', 'name': 'Deuterium', 'category': 'fusion fuel', 'z': 1, 'mass': 2},
    {'symbol': 'T', 'name': 'Tritium', 'category': 'fusion fuel', 'z': 1, 'mass': 3},
    {'symbol': 'He3', 'name': 'Helium-3', 'category': 'fusion fuel', 'z': 2, 'mass': 3},
    {'symbol': 'B11', 'name': 'Boron-11', 'category': 'fusion fuel', 'z': 5, 'mass': 11}
]
# Assume 'all_options' includes your previous elements + these new symbols
all_options = ['H', 'D', 'T', 'He3', 'B11', 'I', 'W', 'C'] # abbreviated for example

# 2. Dynamic UI for multiple elements
num_slots = widgets.IntSlider(value=3, min=2, max=6, description='Reactants:')
slot_container = widgets.VBox()
regime_toggle = widgets.RadioButtons(options=['Standard Chemistry', 'Fusion Plasma (keV)'], description='Environment:')
output = widgets.Output()

def update_slots(change):
    slots = []
    for i in range(num_slots.value):
        slots.append(widgets.Dropdown(options=all_options, description=f'Particle {i+1}:'))
    slot_container.children = slots

num_slots.observe(update_slots, names='value')
update_slots(None) # Initialize slots

# 3. Fusion Logic Matrix
def predict_plasma_interaction(plasma_pool):
    # Convert list of selected symbols to a set for easy cross-referencing
    particles = set(plasma_pool)
    messages = []
    
    # Check for primary fusion reactions
    if {'D', 'T'}.issubset(particles):
        messages.append("🔥 D-T Fusion: D + T → ⁴He (3.5 MeV) + n (14.1 MeV). Highest cross-section reaction.")
    if {'D'}.issubset(particles) and plasma_pool.count('D') >= 2:
        messages.append("🔥 D-D Fusion: D + D → ³He + n OR T + p. Requires higher temperature than D-T.")
    if {'H', 'B11'}.issubset(particles):
        messages.append("🔥 p-B11 Fusion: p + ¹¹B → 3 ⁴He. Aneutronic reaction, extreme temperature requirement.")
        
    # Check for Bremsstrahlung/High-Z radiation loss (like your Iodine scenario)
    high_z = [p for p in particles if p not in ['H', 'D', 'T', 'He3', 'Li', 'B11']]
    if high_z:
        messages.append(f"⚠️ Quench Warning: High-Z impurities detected ({', '.join(high_z)}). Bremsstrahlung radiation scales with Z². This will rapidly cool the FRC core.")
        
    if not messages:
        messages.append("No primary fusion cross-sections detected in this combination.")
        
    return "\n\n".join(messages)

def on_predict(b):
    with output:
        clear_output(wait=True)
        # Gather all current selections from the dynamically generated dropdowns
        current_pool = [dropdown.value for dropdown in slot_container.children]
        
        if regime_toggle.value == 'Fusion Plasma (keV)':
            print(predict_plasma_interaction(current_pool))
        else:
            print("Standard chemistry logic goes here (bypassed for this example).")

predict_btn = widgets.Button(description='Simulate Plasma', button_style='danger')
predict_btn.on_click(on_predict)

# Render UI
display(regime_toggle, num_slots, slot_container, predict_btn, output)
