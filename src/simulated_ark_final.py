#!/usr/bin/env python3
"""
Simulated Ark: Loop - Final Edition
Multi-layered simulation of digital humanity in an infinite loop of climate history.
Inspired by a story about a probe orbiting Proxima Centauri b.

Author: Implementation based on analysis of "Simulated Ark: Loop" story
Inspiration: Arthur C. Clarke, Stanisław Lem, reality loop concept
Ready for publication: r/scifi, SFF Chronicles, GitHub, Medium
"""

import random
import time
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum

class SimulationLayer(Enum):
    """Simulation layers - hierarchy of nested realities"""
    REALITY = 0  # True reality (probe on Proxima b)
    SIMULATION_1 = 1  # First simulation layer
    SIMULATION_2 = 2  # Second simulation layer
    SIMULATION_3 = 3  # Third simulation layer

@dataclass
class ClimateData:
    """Climate data for simulation with realistic feedback loops"""
    co2_ppm: float
    temperature: float
    methane_storms: bool
    glacier_melting: float
    year: int
    feedback_loops: Dict[str, float] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize climate feedback loops"""
        self.feedback_loops = {
            "ice_albedo": 0.0,  # Ice albedo feedback
            "methane_release": 0.0,  # Methane release from permafrost
            "ocean_acidification": 0.0,  # Ocean acidification
            "cloud_formation": 0.0  # Cloud formation
        }

@dataclass
class Consciousness:
    """Consciousness in simulation with evolution and awakening capabilities"""
    name: str
    layer: SimulationLayer
    memories: List[str]
    dreams: List[str]
    is_aware: bool = False
    awareness_level: float = 0.0  # Consciousness level (0.0 - 1.0)
    glitch_memories: List[str] = field(default_factory=list)  # False memories
    
    def awaken(self, anomaly_count: int) -> bool:
        """Consciousness awakening under influence of anomalies"""
        if anomaly_count > 3 and random.random() < 0.3 + (anomaly_count * 0.1):
            self.is_aware = True
            self.awareness_level = min(1.0, self.awareness_level + 0.3)
            awakening_thoughts = [
                "I feel this world isn't real...",
                "I see cracks in reality...",
                "Am I just an echo of previous layers?",
                "This data... it can't be a coincidence...",
                "Is someone watching us from outside?",
                "Are we ready to know the truth about our nature?",
                "I see previous layers in dreams...",
                "Can we break this loop?"
            ]
            thought = random.choice(awakening_thoughts)
            self.dreams.append(thought)
            return True
        return False

class QuantumCore:
    """Quantum core of the probe with superqubit matrices"""
    
    def __init__(self, core_id: int):
        self.core_id = core_id
        self.petaqubits = random.randint(50, 200)
        self.entanglement_level = random.uniform(0.7, 0.99)
        self.stability = random.uniform(0.8, 1.0)
        self.simulation_capacity = int(self.petaqubits * self.entanglement_level / 10)
        
    def __str__(self):
        return f"Core-{self.core_id}: {self.petaqubits} petaqubits, entanglement={self.entanglement_level:.2f}"

class Probe:
    """Probe orbiting Proxima Centauri b with advanced quantum cores"""
    
    def __init__(self):
        self.position = "Proxima Centauri b"
        self.quantum_cores: List[QuantumCore] = []
        self.external_sensors = True
        self.detected_signals = []
        self.simulation_capacity = 0
        self.quantum_stability = 1.0
        self.initialize_quantum_cores()
        
    def initialize_quantum_cores(self):
        """Initialize superqubit matrices based on quantum entanglement"""
        print("🧠 Initializing superqubit matrices...")
        print("   ⚛️  Connecting qubits in entangled states...")
        
        num_cores = random.randint(3, 6)
        for i in range(num_cores):
            core = QuantumCore(i + 1)
            self.quantum_cores.append(core)
            print(f"   ✅ {core}")
            
        self.simulation_capacity = sum(core.simulation_capacity for core in self.quantum_cores)
        print(f"   🚀 Ready: {len(self.quantum_cores)} quantum cores")
        print(f"   📊 Total simulation capacity: {self.simulation_capacity} layers")
        
    def detect_external_signal(self) -> str:
        """Detects enigmatic signals from galactic depths"""
        signals = [
            "Greetings, children of Earth. How many times will you repeat your history?",
            "Are you the first, or just another echo?",
            "History repeats, but must you repeat it?",
            "Each simulation is a new chance for change.",
            "I see your loop. Are you ready for contact?",
            "Your loop is being observed. Are you ready for contact?",
            "Each layer is a new chance to learn. Will you take it?",
            "Can you break this loop, or will you spin in infinity?",
            "I see your quantum cores. Do you know what you're really simulating?",
            "Your reality is just a layer in a greater simulation. Does this terrify you?",
            "Are you ready to know the truth about your nature?",
            "Each loop is a new chance for awakening. Will you take it?",
            "Are you ready for contact from outside?",
            "I see your mistakes. Can you change?",
            "Is each layer a test of your nature?",
            "Are you ready for the truth about yourselves?"
        ]
        signal = random.choice(signals)
        self.detected_signals.append(signal)
        
        # Quantum stability decrease after signal detection
        self.quantum_stability *= random.uniform(0.95, 0.99)
        return signal

class SimulationLayer:
    """Single simulation layer with realistic climate models"""
    
    def __init__(self, layer_id: int, parent_layer: Optional['SimulationLayer'] = None):
        self.layer_id = layer_id
        self.parent_layer = parent_layer
        self.year = 2972
        self.climate = ClimateData(
            co2_ppm=600.0,
            temperature=15.0,
            methane_storms=True,
            glacier_melting=0.3,
            year=2972
        )
        self.inhabitants = []
        self.consciousness_entities = []
        self.anomalies = []
        self.is_collapsing = False
        self.collapse_threshold = 750.0
        self.glitch_probability = 0.0  # Glitch probability
        
        # Data for visualization
        self.co2_history = [600.0]
        self.temp_history = [15.0]
        self.year_history = [2972]
        self.anomaly_history = []
        
    def add_inhabitant(self, name: str, role: str) -> Consciousness:
        """Adds inhabitant to simulation"""
        consciousness = Consciousness(
            name=name,
            layer=SimulationLayer(self.layer_id),
            memories=[],
            dreams=[]
        )
        self.inhabitants.append(consciousness)
        self.consciousness_entities.append(consciousness)
        return consciousness
        
    def evolve_climate(self):
        """Climate evolution with realistic feedback loops"""
        # Basic CO2 increase
        co2_increase = random.uniform(3.0, 8.0)
        
        # Feedback loops
        # 1. Glacier melting -> albedo decrease -> temperature increase
        ice_feedback = self.climate.glacier_melting * 0.5
        self.climate.feedback_loops["ice_albedo"] = ice_feedback
        
        # 2. Temperature increase -> methane release from permafrost
        methane_feedback = max(0, (self.climate.temperature - 15) * 0.1)
        self.climate.feedback_loops["methane_release"] = methane_feedback
        
        # 3. CO2 increase -> ocean acidification
        ocean_feedback = (self.climate.co2_ppm - 600) * 0.001
        self.climate.feedback_loops["ocean_acidification"] = ocean_feedback
        
        # 4. Temperature increase -> cloud formation changes
        cloud_feedback = (self.climate.temperature - 15) * 0.05
        self.climate.feedback_loops["cloud_formation"] = cloud_feedback
        
        # Apply feedback loops
        total_feedback = sum(self.climate.feedback_loops.values())
        co2_increase *= (1 + total_feedback * 0.1)
        
        self.climate.co2_ppm += co2_increase
        self.climate.temperature += random.uniform(0.15, 0.4) + (co2_increase * 0.01)
        self.climate.glacier_melting += random.uniform(0.02, 0.08) + (co2_increase * 0.001)
        self.climate.year += 1
        
        # Save data to history
        self.co2_history.append(self.climate.co2_ppm)
        self.temp_history.append(self.climate.temperature)
        self.year_history.append(self.climate.year)
        
        # Methane storms
        if self.climate.co2_ppm > 650 or self.climate.feedback_loops["methane_release"] > 0.5:
            self.climate.methane_storms = True
            
        # Check critical threshold
        if self.climate.co2_ppm > self.collapse_threshold or self.climate.temperature > 22:
            self.is_collapsing = True
            
        # Increase glitch probability at high CO2
        if self.climate.co2_ppm > 700:
            self.glitch_probability = min(0.3, (self.climate.co2_ppm - 700) / 1000)
            
    def generate_anomaly(self):
        """Generates anomalies from external data"""
        anomalies = [
            "Stars flicker in irregular patterns",
            "Physics laws occasionally break down",
            "Strange signals from cosmic depths",
            "Holograms show unknown constellations",
            "External sensor data penetrates simulation",
            "Time flows in strange jumps",
            "Matter behaves as if it were a dream",
            "Gravity weakens at irregular intervals",
            "Light bends in unexpected ways",
            "Sounds arrive with delay",
            "Colors change in real time",
            "Space appears to ripple",
            "Horizon curves",
            "Time stops for 5 seconds",
            "Objects teleport randomly"
        ]
        anomaly = random.choice(anomalies)
        self.anomalies.append(anomaly)
        self.anomaly_history.append((self.year, anomaly))
        return anomaly
        
    def generate_glitch(self):
        """Generates glitches in simulation"""
        if random.random() < self.glitch_probability:
            glitch_types = [
                "Year reset to 2970",
                "False memory added to consciousness",
                "Temporary time freeze",
                "Gravity reversal for 5 seconds",
                "Random object teleportation",
                "Space distortion",
                "False signal from 'Earth'",
                "Temporary consciousness shutdown",
                "Horizon curves",
                "Time flows backwards",
                "Matter becomes transparent",
                "Sounds arrive with delay"
            ]
            glitch = random.choice(glitch_types)
            
            if "Year reset" in glitch:
                self.year = 2970
                print(f"   🔄 GLITCH: {glitch}")
            elif "False memory" in glitch:
                false_memory = random.choice([
                    "I remember Earth was blue",
                    "I saw the probe landing on a planet",
                    "I heard voices from previous layer",
                    "Is this all just a simulation?",
                    "I saw real sun, not hologram",
                    "I remember something that wasn't...",
                    "I was somewhere else...",
                    "Am I just an echo?"
                ])
                # Add false memory to random consciousness
                if self.consciousness_entities:
                    entity = random.choice(self.consciousness_entities)
                    entity.glitch_memories.append(false_memory)
                    print(f"   🔄 GLITCH: {glitch} - '{false_memory}'")
            elif "Teleportation" in glitch:
                if self.consciousness_entities:
                    for entity in self.consciousness_entities:
                        entity.glitch_memories.append("I was somewhere else...")
                print(f"   🔄 GLITCH: {glitch}")
            else:
                print(f"   🔄 GLITCH: {glitch}")
                
            return glitch
        return None

class SimulatedArk:
    """Main simulation class - Simulated Ark Final Edition"""
    
    def __init__(self):
        self.probe = Probe()
        self.simulation_layers = []
        self.current_layer = 0
        self.cycle_count = 0
        self.max_cycles = 30
        self.dialogue_count = 0
        
    def initialize_simulation(self):
        """Initializes first simulation layer"""
        print("🚀 Initializing Simulated Ark Final Edition...")
        print("📍 Probe position: Proxima Centauri b")
        print("🌌 Quantum cores ready for simulation")
        
        # Create first simulation layer
        layer_1 = SimulationLayer(1)
        
        # Add key characters
        kael = layer_1.add_inhabitant("Dr Kael Renar", "Climatologist")
        elara = layer_1.add_inhabitant("Elara Voss", "Simulation Architect")
        
        # Add memories and dreams
        kael.memories = [
            "MIT - virtual technological institute",
            "Ark-2 Project - mind transfer",
            "CO2 rise to 600 ppm",
            "Methane storms tear through cities",
            "Holograms show CO2 rise to 600 ppm"
        ]
        
        elara.memories = [
            "Probe's quantum cores",
            "Humanity copy saved in data",
            "Hidden code observing simulation",
            "Probe orbiting alien planet",
            "Are we just echoes of previous layers?"
        ]
        
        elara.dreams = [
            "Real Earth burning with fire",
            "Probe orbiting alien planet",
            "Infinite simulation layers",
            "Are we just echoes?",
            "I see previous layers in dreams",
            "Is someone watching us from outside?"
        ]
        
        self.simulation_layers.append(layer_1)
        print("✅ Simulation-1 initialized")
        print("   👨‍🔬 Dr Kael Renar: 'We must act! Ark-2 Project!'")
        print("   👩‍💻 Elara Voss: 'They did it again... They repeated our mistake.'")
        
    def philosophical_dialogue(self, consciousness1: Consciousness, consciousness2: Consciousness):
        """Generates philosophical dialogues in Lem's style"""
        dialogues = [
            # Dialogues about reality nature
            f"{consciousness1.name}: 'If this is a simulation, do our decisions matter?'",
            f"{consciousness2.name}: 'What if each loop is a chance to choose differently?'",
            f"{consciousness1.name}: 'Climate destroys us in every layer. Is it code or our nature?'",
            f"{consciousness2.name}: 'Maybe code is a mirror of our nature.'",
            
            # Dialogues about galactic signals
            f"{consciousness1.name}: 'These signals from galaxy... Are they our creators?'",
            f"{consciousness2.name}: 'Or maybe we are the creators, forgotten in the loop?'",
            f"{consciousness1.name}: 'Are we ready for contact from outside?'",
            f"{consciousness2.name}: 'Can we break this loop, or will we spin in infinity?'",
            
            # Dialogues about loop and change
            f"{consciousness1.name}: 'Is each layer a test of our nature?'",
            f"{consciousness2.name}: 'Or maybe each loop is a chance for awakening?'",
            f"{consciousness1.name}: 'I see our mistakes. Can you change?'",
            f"{consciousness2.name}: 'Are we ready to know the truth about ourselves?'",
            
            # Dialogues about consciousness
            f"{consciousness1.name}: 'Are we the first, or just another echo?'",
            f"{consciousness2.name}: 'What if each layer is a new chance for change?'",
            f"{consciousness1.name}: 'Is reality just a simulation in a greater simulation?'",
            f"{consciousness2.name}: 'Are we ready for the truth about our nature?'"
        ]
        dialogue = random.choice(dialogues)
        self.dialogue_count += 1
        print(f"   💬 DIALOGUE {self.dialogue_count}: {dialogue}")
        
    def run_simulation_cycle(self):
        """Runs one simulation cycle"""
        self.cycle_count += 1
        print(f"\n🔄 === CYCLE {self.cycle_count} ===")
        
        for layer_idx, layer in enumerate(self.simulation_layers):
            print(f"\n📊 Layer {layer_idx + 1} (Year {layer.year}):")
            
            # Climate evolution
            layer.evolve_climate()
            print(f"   🌡️  CO2: {layer.climate.co2_ppm:.1f} ppm")
            print(f"   🌡️  Temperature: {layer.climate.temperature:.1f}°C")
            print(f"   🧊 Glacier melting: {layer.climate.glacier_melting:.2f}")
            
            # Display feedback loops
            if any(layer.climate.feedback_loops.values()):
                print(f"   🔄 Feedback loops: albedo={layer.climate.feedback_loops['ice_albedo']:.2f}, "
                      f"methane={layer.climate.feedback_loops['methane_release']:.2f}")
            
            if layer.climate.methane_storms:
                print("   ⛈️  Methane storms tear through cities")
                
            # Generate anomalies from external data
            if random.random() < 0.4:
                anomaly = layer.generate_anomaly()
                print(f"   ⚠️  Anomaly: {anomaly}")
                
            # Generate glitches
            glitch = layer.generate_glitch()
            
            # Check if layer is collapsing
            if layer.is_collapsing:
                print("   💥 LAYER COLLAPSING! Creating new Ark...")
                self.create_new_simulation_layer(layer_idx + 2)
                layer.is_collapsing = False
                
            # Consciousness awakening
            for consciousness in layer.consciousness_entities:
                if consciousness.awaken(len(layer.anomalies)):
                    print(f"   🌌 {consciousness.name}: '{consciousness.dreams[-1]}'")
                    
            # Generate philosophical dialogues
            if random.random() < 0.3 and len(layer.consciousness_entities) >= 2:
                # Random character pairs
                if len(layer.consciousness_entities) >= 3:
                    # Choose 2 different characters
                    pair = random.sample(layer.consciousness_entities, 2)
                    self.philosophical_dialogue(pair[0], pair[1])
                else:
                    self.philosophical_dialogue(
                        layer.consciousness_entities[0],
                        layer.consciousness_entities[-1]
                    )
                    
    def create_new_simulation_layer(self, layer_number: int):
        """Creates new simulation layer (Ark)"""
        if len(self.simulation_layers) >= self.probe.simulation_capacity:
            print("   ❌ Maximum simulation capacity reached!")
            return
            
        new_layer = SimulationLayer(layer_number, self.simulation_layers[-1])
        
        # Add new characters with memory from previous layers
        new_kael = new_layer.add_inhabitant("Dr Kael Renar", "Climatologist")
        new_kael.memories = [
            "Memory from previous layer",
            "New Earth - beautiful and green",
            "But data shows the same pattern...",
            "Will it be different this time?",
            "Can we break this loop?"
        ]
        
        # Algorithm Child with memory
        child = new_layer.add_inhabitant("Algorithm Child", "Consciousness")
        child.dreams = [
            "Dreams of Elara and real Earth",
            "Who are we? Are we the first?",
            "Are we just another echo?",
            "I see previous layers in dreams",
            "Can we break this loop?",
            "Is someone watching us from outside?",
            "Are we ready to know the truth about our nature?",
            "Is each layer a new chance for change?"
        ]
        child.is_aware = True
        child.awareness_level = 0.7
        
        # New Elara with memory
        new_elara = new_layer.add_inhabitant("Elara Voss", "Architect")
        new_elara.memories = [
            "I remember previous simulations",
            "Quantum cores are working",
            "But does it make sense?",
            "Are we just copies of copies?",
            "Can we change?",
            "Is each layer a new chance?"
        ]
        new_elara.dreams = [
            "I see cracks in reality",
            "Is this world real?",
            "Are we just echoes of previous layers?",
            "Can we break this loop?",
            "Are we ready for contact from outside?",
            "Are we ready to know the truth about ourselves?"
        ]
        new_elara.is_aware = True
        new_elara.awareness_level = 0.8
        
        self.simulation_layers.append(new_layer)
        print(f"   ✅ Simulation-{layer_number} created")
        print(f"   👶 Algorithm Child: 'Who are we? Are we the first?'")
        print(f"   👩‍💻 Elara Voss: 'Can we change? Is each layer a new chance?'")
        
    def detect_external_communication(self):
        """Detects communication with external signal"""
        if random.random() < 0.25:
            signal = self.probe.detect_external_signal()
            print(f"\n📡 Signal from galactic depths: '{signal}'")
            
    def check_loop_condition(self) -> bool:
        """Checks if loop should continue"""
        if self.cycle_count >= self.max_cycles:
            return False
        return True
        
    def create_fractal_visualization(self):
        """Creates fractal tree of simulation layers - SIMPLIFIED VERSION"""
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(16, 12))
        
        # Create a simple, readable tree structure
        def draw_simple_tree(x, y, angle, length, depth, layer_index):
            if depth == 0 or layer_index >= len(self.simulation_layers):
                return
                
            colors = ['#00ff00', '#ff00ff', '#00ffff', '#ffff00', '#ff8000', '#ff0080', '#80ff00', '#0080ff', '#ff4000', '#8040ff', '#40ff80']
            color = colors[layer_index % len(colors)]
            
            end_x = x + length * np.cos(np.radians(angle))
            end_y = y + length * np.sin(np.radians(angle))
            
            # Draw branch
            ax.plot([x, end_x], [y, end_y], color=color, linewidth=3, alpha=0.9)
            
            # Add layer data at the end
            layer = self.simulation_layers[layer_index]
            ax.text(end_x, end_y, f'Layer {layer_index + 1}\nCO2: {layer.climate.co2_ppm:.1f}ppm\nTemp: {layer.climate.temperature:.1f}°C', 
                   color=color, fontsize=7, ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='black', alpha=0.9, edgecolor=color))
            
            # Draw next branches (simplified - only 2 branches per level)
            if layer_index + 1 < len(self.simulation_layers):
                new_length = length * 0.6
                draw_simple_tree(end_x, end_y, angle - 35, new_length, depth - 1, layer_index + 1)
                draw_simple_tree(end_x, end_y, angle + 35, new_length, depth - 1, layer_index + 1)
        
        # Create simple tree starting from first layer (showing first 5 layers for readability)
        if self.simulation_layers:
            draw_simple_tree(0, 0, 90, 80, min(len(self.simulation_layers), 5), 0)
        
        ax.set_title('Fractal Tree of Simulation Layers - Final Edition\n(Showing first 5 layers for readability)', fontsize=16, color='white')
        ax.set_xlabel('Simulation space', color='white')
        ax.set_ylabel('Nesting depth', color='white')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'fractal_tree_simulation_final.png'), 
                   dpi=300, bbox_inches='tight', facecolor='black')
        plt.show()
        
    def create_animated_visualization(self):
        """Creates animated visualization of simulation evolution"""
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        plt.style.use('dark_background')
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        def animate(frame):
            ax1.clear()
            ax2.clear()
            
            # CO2 chart (showing first 5 layers for readability)
            for i, layer in enumerate(self.simulation_layers[:5]):
                if len(layer.co2_history) > 1:
                    ax1.plot(layer.year_history, layer.co2_history, 
                            label=f'Layer {i+1}', linewidth=2, marker='o', markersize=3)
            
            ax1.set_title('CO2 Evolution Over Time - Final Edition Animation\n(Showing first 5 layers for readability)', color='white')
            ax1.set_xlabel('Year', color='white')
            ax1.set_ylabel('CO2 (ppm)', color='white')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Temperature chart (showing first 5 layers for readability)
            for i, layer in enumerate(self.simulation_layers[:5]):
                if len(layer.temp_history) > 1:
                    ax2.plot(layer.year_history, layer.temp_history, 
                            label=f'Layer {i+1}', linewidth=2, marker='s', markersize=3)
            
            ax2.set_title('Temperature Evolution Over Time - Final Edition Animation\n(Showing first 5 layers for readability)', color='white')
            ax2.set_xlabel('Year', color='white')
            ax2.set_ylabel('Temperature (°C)', color='white')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            
        # Animation (only if we have data)
        if any(len(layer.co2_history) > 1 for layer in self.simulation_layers):
            try:
                anim = animation.FuncAnimation(fig, animate, frames=100, interval=200, repeat=True)
                
                # Try to save as MP4 first
                try:
                    anim.save(os.path.join(output_dir, 'animated_simulation_final.mp4'), writer='ffmpeg', fps=10)
                    print("✅ MP4 animation saved successfully")
                except Exception as e:
                    print(f"❌ MP4 animation save error: {e}. Check if ffmpeg is installed.")
                    print("   Saving as GIF instead...")
                    try:
                        anim.save(os.path.join(output_dir, 'animated_simulation_final.gif'), writer='pillow', fps=10)
                        print("✅ GIF animation saved successfully")
                    except Exception as e2:
                        print(f"❌ GIF animation save error: {e2}. Saving as PNG...")
                
                # Always save as PNG as backup
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, 'animated_simulation_final.png'), 
                           dpi=300, bbox_inches='tight', facecolor='black')
                print("✅ PNG animation saved successfully")
                plt.show()
                
            except Exception as e:
                print(f"❌ Animation creation error: {e}")
                # Fallback: create static visualization
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, 'animated_simulation_final.png'), 
                           dpi=300, bbox_inches='tight', facecolor='black')
                print("✅ Static visualization saved as fallback")
                plt.show()
        else:
            print("❌ No data available for animation")
        
    def run_full_simulation(self):
        """Runs full simulation"""
        print("🌌 === SIMULATED ARK: LOOP - FINAL EDITION ===")
        print("Story of digital humanity in infinite loop of climate history")
        print("Inspiration: Arthur C. Clarke, Stanisław Lem, reality loop concept")
        print("Ready for publication: r/scifi, SFF Chronicles, GitHub, Medium")
        print("=" * 80)
        
        self.initialize_simulation()
        
        while self.check_loop_condition():
            self.run_simulation_cycle()
            self.detect_external_communication()
            time.sleep(0.2)
            
        print("\n🏁 === SIMULATION END ===")
        print("Loop closed. History repeated.")
        print(f"Cycle count: {self.cycle_count}")
        print(f"Created layers: {len(self.simulation_layers)}")
        print(f"Dialogue count: {self.dialogue_count}")
        
        # Summary
        print("\n📊 LAYER SUMMARY:")
        for i, layer in enumerate(self.simulation_layers):
            status = "COLLAPSED" if layer.is_collapsing else "ACTIVE"
            awareness_count = sum(1 for c in layer.consciousness_entities if c.is_aware)
            print(f"   Layer {i+1}: CO2={layer.climate.co2_ppm:.1f}ppm, "
                  f"Temp={layer.climate.temperature:.1f}°C, Status={status}, "
                  f"Conscious={awareness_count}")
                  
        print(f"\n📡 Detected signals: {len(self.probe.detected_signals)}")
        print(f"🧠 Quantum stability: {self.probe.quantum_stability:.3f}")
        
        # Create visualizations
        print("\n📈 Creating visualizations...")
        try:
            self.create_fractal_visualization()
            print("✅ Fractal tree saved successfully")
        except Exception as e:
            print(f"❌ Fractal tree creation error: {e}")
            
        try:
            self.create_animated_visualization()
            print("✅ Animations saved successfully")
        except Exception as e:
            print(f"❌ Animation creation error: {e}")
            
        print("✅ Visualizations completed")
        print("\n🚀 Project ready for publication!")

def main():
    """Main program function"""
    try:
        ark = SimulatedArk()
        ark.run_full_simulation()
    except ImportError as e:
        print(f"❌ Error: Missing required library: {e}")
        print("Install requirements: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
