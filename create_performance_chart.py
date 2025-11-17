#!/usr/bin/env python3
"""Generate performance comparison chart for blog post."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Chart 1: Inference Speed
models_speed = ['MiniMax\nM2-THRIFT', 'GPT-OSS\n120B', 'Kimi\nK2', 'Qwen3\nCoder']
speeds = [12.5, 8.5, 4.2, 3.8]
colors_speed = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']

bars1 = ax1.bar(models_speed, speeds, color=colors_speed, alpha=0.8, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Tokens per Second', fontsize=13, fontweight='bold')
ax1.set_title('Inference Speed (Mac Studio M2 Ultra, 128GB)', fontsize=14, fontweight='bold')
ax1.set_ylim(0, 15)
ax1.grid(axis='y', alpha=0.3)

# Add value labels
for i, (bar, v) in enumerate(zip(bars1, speeds)):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{v}',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

# Chart 2: Active Parameters (Memory Efficiency)
models_params = ['MiniMax\nM2', 'GPT-OSS\n120B', 'Kimi\nK2', 'Qwen3\nCoder', 'DeepSeek\nV3']
active_params = [10, 15, 32, 35, 37]
colors_params = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336']

bars2 = ax2.bar(models_params, active_params, color=colors_params, alpha=0.8, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Active Parameters (Billions)', fontsize=13, fontweight='bold')
ax2.set_title('Model Efficiency: Active Parameters per Token', fontsize=14, fontweight='bold')
ax2.set_ylim(0, 45)
ax2.grid(axis='y', alpha=0.3)
ax2.axhline(y=10, color='green', linestyle='--', alpha=0.5, linewidth=2)
ax2.text(4.2, 11, 'Most Efficient', fontsize=10, color='green', fontweight='bold')

# Add value labels
for bar, v in zip(bars2, active_params):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.8,
             f'{v}B',
             ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('images/performance-comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Performance chart saved to images/performance-comparison.png")

# Create second chart: RAM Usage
fig2, ax3 = plt.subplots(figsize=(10, 6))

models_ram = ['MiniMax\nTHRIFT\nIQ4_XS', 'MiniMax\nREAP-172B\nQ4', 'Qwen3\nCoder\nQ4', 'Kimi\nK2\nQ4']
ram_usage = [70, 65, 150, 120]
colors_ram = ['#4CAF50', '#8BC34A', '#FF9800', '#F44336']

bars3 = ax3.barh(models_ram, ram_usage, color=colors_ram, alpha=0.8, edgecolor='black', linewidth=1.5)
ax3.set_xlabel('RAM Usage (GB)', fontsize=13, fontweight='bold')
ax3.set_title('Memory Footprint Comparison (Quantized Models)', fontsize=14, fontweight='bold')
ax3.set_xlim(0, 160)
ax3.axvline(x=128, color='red', linestyle='--', alpha=0.7, linewidth=2)
ax3.text(130, 3.5, '128GB Limit', fontsize=11, color='red', fontweight='bold', rotation=90)
ax3.grid(axis='x', alpha=0.3)

# Add value labels
for bar, v in zip(bars3, ram_usage):
    width = bar.get_width()
    ax3.text(width + 2, bar.get_y() + bar.get_height()/2.,
             f'{v}GB',
             ha='left', va='center', fontweight='bold', fontsize=11)

# Add "Fits in 128GB" annotation
ax3.text(35, 0.5, '✓ Fits in 128GB', fontsize=10, color='green', fontweight='bold')
ax3.text(35, 1.5, '✓ Fits in 128GB', fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.savefig('images/ram-usage-comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ RAM usage chart saved to images/ram-usage-comparison.png")

print("\n📊 Charts generated successfully!")
print("Run: open images/")
