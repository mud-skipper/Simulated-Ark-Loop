#!/usr/bin/env python3
"""
Simulated Ark: Loop - Visual Version (Final Edition)
Shows simulation with charts and data visualization
Improved version with better charts and error handling
"""

import random
import time
import json
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

class SimulationLayer(Enum):
    """Simulation layers"""
    REALITY = 0
    SIMULATION_1 = 1
    SIMULATION_2 = 2
    SIMULATION_3 = 3

@dataclass
class ClimateData:
    """Climate data for simulation"""
    co2_ppm: float
    temperature: float
    methane_storms: bool
    glacier_melting: float
    year: int

@dataclass
class Consciousness:
    """Consciousness in simulation"""
    name: str
    layer: SimulationLayer
    memories: List[str]
    dreams: List[str]
    is_aware: bool = False

class Probe:
    """Probe orbiting Proxima Centauri b"""
    
    def __init__(self):
        self.position = "Proxima Centauri b"
        self.quantum_cores = []
        self.external_sensors = True
        self.detected_signals = []
        self.simulation_capacity = 10  # Increased capacity for more layers
        
    def detect_external_signal(self) -> str:
        """Detects signal from galactic depths"""
        signals = [
            "Greetings, children of Earth. How many times will you repeat your history?",
            "Are you the first, or just another echo?",
            "History repeats, but must you repeat it?",
            "Each simulation is a new chance for change.",
            "I see your loop. Can you break it?",
            "Each layer is a new chance to learn. Will you take it?"
        ]
        signal = random.choice(signals)
        self.detected_signals.append(signal)
        return signal

class SimulationLayer:
    """Single simulation layer"""
    
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
        self.collapse_threshold = 750.0  # Restored realistic threshold
        
        # Data for visualization
        self.co2_history = [600.0]
        self.temp_history = [15.0]
        self.year_history = [2972]
        
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
        """Climate evolution in simulation"""
        # CO2 increase leads to climate changes
        self.climate.co2_ppm += random.uniform(3.0, 8.0)
        self.climate.temperature += random.uniform(0.15, 0.4)
        self.climate.glacier_melting += random.uniform(0.02, 0.08)
        self.climate.year += 1
        
        # Save data to history
        self.co2_history.append(self.climate.co2_ppm)
        self.temp_history.append(self.climate.temperature)
        self.year_history.append(self.climate.year)
        
        # Methane storms
        if self.climate.co2_ppm > 650:
            self.climate.methane_storms = True
            
        # Check critical threshold
        if self.climate.co2_ppm > self.collapse_threshold or self.climate.temperature > 22:
            self.is_collapsing = True
            
    def generate_anomaly(self):
        """Generates anomalies from external data"""
        anomalies = [
            "Stars flicker in irregular patterns",
            "Physics laws occasionally break down",
            "Strange signals from cosmic depths",
            "Holograms show unknown constellations",
            "External sensor data penetrates simulation",
            "Time flows in strange jumps",
            "Matter behaves as if it were a dream"
        ]
        anomaly = random.choice(anomalies)
        self.anomalies.append(anomaly)
        return anomaly

class SimulatedArk:
    """Main simulation class - Simulated Ark"""
    
    def __init__(self):
        self.probe = Probe()
        self.simulation_layers = []
        self.current_layer = 0
        self.cycle_count = 0
        self.max_cycles = 20
        
    def initialize_simulation(self):
        """Initializes first simulation layer"""
        print("🚀 Initializing Simulated Ark...")
        print("📍 Probe position: Proxima Centauri b")
        print("🧠 Quantum cores ready for simulation")
        
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
            "Methane storms tear through cities"
        ]
        
        elara.memories = [
            "Probe's quantum cores",
            "Humanity copy saved in data",
            "Hidden code observing simulation",
            "Probe orbiting alien planet"
        ]
        
        elara.dreams = [
            "Real Earth burning with fire",
            "Probe orbiting alien planet",
            "Infinite simulation layers",
            "Are we just echoes?"
        ]
        
        self.simulation_layers.append(layer_1)
        print("✅ Simulation-1 initialized")
        
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
            
            if layer.climate.methane_storms:
                print("   ⛈️  Methane storms tear through cities")
                
            # Generate anomalies from external data
            if random.random() < 0.3:
                anomaly = layer.generate_anomaly()
                print(f"   ⚠️  Anomaly: {anomaly}")
                
            # Check if layer is collapsing
            if layer.is_collapsing:
                print("   💥 LAYER COLLAPSING! Creating new Ark...")
                self.create_new_simulation_layer(layer_idx + 2)
                # Don't reset is_collapsing - layer can collapse multiple times
                
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
            "Will it be different this time?"
        ]
        
        # Algorithm Child with memory
        child = new_layer.add_inhabitant("Algorithm Child", "Consciousness")
        child.dreams = [
            "Dreams of Elara and real Earth",
            "Who are we? Are we the first?",
            "Are we just another echo?",
            "I see previous layers in dreams",
            "Can we break this loop?"
        ]
        child.is_aware = True
        
        self.simulation_layers.append(new_layer)
        print(f"   ✅ Simulation-{layer_number} created")
        print(f"   👶 Algorithm Child: 'Who are we? Are we the first?'")
        
    def detect_external_communication(self):
        """Detects communication with external signal"""
        if random.random() < 0.2:
            signal = self.probe.detect_external_signal()
            print(f"\n📡 Signal from galactic depths: '{signal}'")
            
    def check_loop_condition(self) -> bool:
        """Checks if loop should continue"""
        if self.cycle_count >= self.max_cycles:
            return False
        return True
        
    def create_visualization(self):
        """Creates simulation data visualization with improvements"""
        try:
            # Initialize simulation first
            print("🚀 Initializing simulation...")
            self.initialize_simulation()
            
            # Run simulation to generate data
            print("🔄 Running simulation to generate data...")
            # Temporarily increase max_cycles for visualization
            original_max_cycles = self.max_cycles
            self.max_cycles = 200
            for _ in range(200):  # Run 200 cycles to generate historical data and create more layers
                self.run_simulation_cycle()
                if not self.check_loop_condition():
                    break
            # Restore original max_cycles
            self.max_cycles = original_max_cycles
            
            plt.style.use('dark_background')
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle('Simulated Ark: Loop - Data Visualization (Final Edition)\n(Showing first 5 layers for readability)', fontsize=16, color='white')
            
            # Check if we have any data
            if not self.simulation_layers:
                print("❌ No simulation data available for visualization")
                return
            
            # Chart 1: CO2 over time (showing first 5 layers for readability)
            for i, layer in enumerate(self.simulation_layers[:5]):
                if len(layer.co2_history) > 1:
                    ax1.plot(layer.year_history, layer.co2_history, 
                            label=f'Layer {i+1}', linewidth=2, marker='o', markersize=3)
            ax1.set_title('CO2 Emissions Over Time', color='white')
            ax1.set_xlabel('Year', color='white')
            ax1.set_ylabel('CO2 (ppm)', color='white')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            
            # Chart 2: Temperature over time (showing first 5 layers for readability)
            for i, layer in enumerate(self.simulation_layers[:5]):
                if len(layer.temp_history) > 1:
                    ax2.plot(layer.year_history, layer.temp_history, 
                            label=f'Layer {i+1}', linewidth=2, marker='s', markersize=3)
            ax2.set_title('Temperature Over Time', color='white')
            ax2.set_xlabel('Year', color='white')
            ax2.set_ylabel('Temperature (°C)', color='white')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            
            # Chart 3: Layer comparison (showing first 5 layers for readability)
            if len(self.simulation_layers) > 1:
                layers = [f'Layer {i+1}' for i in range(min(len(self.simulation_layers), 5))]
                final_co2 = [layer.co2_history[-1] for layer in self.simulation_layers[:5]]
                final_temp = [layer.temp_history[-1] for layer in self.simulation_layers[:5]]
                
                x = np.arange(len(layers))
                width = 0.35
                
                ax3.bar(x - width/2, final_co2, width, label='CO2 (ppm)', alpha=0.8, color='red')
                ax3_twin = ax3.twinx()
                ax3_twin.bar(x + width/2, final_temp, width, label='Temperature (°C)', alpha=0.8, color='orange')
                
                ax3.set_title('Layer Comparison - Final Values', color='white')
                ax3.set_xlabel('Layers', color='white')
                ax3.set_ylabel('CO2 (ppm)', color='white')
                ax3_twin.set_ylabel('Temperature (°C)', color='white')
                ax3.set_xticks(x)
                ax3.set_xticklabels(layers)
                ax3.legend(loc='upper left')
                ax3_twin.legend(loc='upper right')
            else:
                ax3.text(0.5, 0.5, 'No data for comparison', ha='center', va='center', 
                        transform=ax3.transAxes, color='white', fontsize=12)
                ax3.set_title('Layer Comparison - No Data', color='white')
            
            # Chart 4: Detected signals
            if self.probe.detected_signals:
                signal_counts = {}
                for signal in self.probe.detected_signals:
                    # Shorten signals for better readability
                    short_signal = signal[:30] + "..." if len(signal) > 30 else signal
                    signal_counts[short_signal] = signal_counts.get(short_signal, 0) + 1
                
                signals = list(signal_counts.keys())
                counts = list(signal_counts.values())
                
                if signals:  # Check if there are signals
                    ax4.barh(signals, counts, alpha=0.8, color='cyan')
                    ax4.set_title('Detected Signals from Galaxy', color='white')
                    ax4.set_xlabel('Occurrence Count', color='white')
                else:
                    ax4.text(0.5, 0.5, 'No signals detected', ha='center', va='center', 
                            transform=ax4.transAxes, color='white', fontsize=12)
                    ax4.set_title('Detected Signals from Galaxy', color='white')
            else:
                ax4.text(0.5, 0.5, 'No signals detected', ha='center', va='center', 
                        transform=ax4.transAxes, color='white', fontsize=12)
                ax4.set_title('Detected Signals from Galaxy', color='white')
            
            plt.tight_layout()
            
            # Save to Downloads folder
            output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            output_path = os.path.join(output_dir, 'simulated_ark_visualization_final.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='black')
            print(f"✅ Visualization saved as: {output_path}")
            plt.show()
            
        except Exception as e:
            print(f"❌ Visualization creation error: {e}")
            print("   Check if matplotlib is installed: pip install matplotlib")
        
    def run_full_simulation(self):
        """Runs full simulation"""
        print("🌌 === SIMULATED ARK: LOOP - VISUAL EDITION ===")
        print("Story of digital humanity in infinite loop of climate history")
        print("=" * 60)
        
        self.initialize_simulation()
        
        while self.check_loop_condition():
            self.run_simulation_cycle()
            self.detect_external_communication()
            time.sleep(0.3)
            
        print("\n🏁 === SIMULATION END ===")
        print("Loop closed. History repeated.")
        print(f"Cycle count: {self.cycle_count}")
        print(f"Created layers: {len(self.simulation_layers)}")
        
        # Summary
        print("\n📊 LAYER SUMMARY:")
        for i, layer in enumerate(self.simulation_layers):
            status = "COLLAPSED" if layer.is_collapsing else "ACTIVE"
            print(f"   Layer {i+1}: CO2={layer.climate.co2_ppm:.1f}ppm, "
                  f"Temp={layer.climate.temperature:.1f}°C, Status={status}")
                  
        print(f"\n📡 Detected signals: {len(self.probe.detected_signals)}")
        
        # Create visualization
        print("\n📈 Creating visualization...")
        self.create_visualization()
        print("✅ Visualization completed")

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
