# Image Guide for Medium Article

## Required Images

### 1. Hero Image (Top of Article)
**File:** `hero-mac-studio.jpg`
**What to capture:**
- Mac Studio M2 Ultra
- External display showing terminal with mini-agent running
- Clean desk setup

**How to create:**
- Take a photo of your Mac Studio setup
- Or use: Screenshot of terminal running mini-agent with system monitor showing RAM usage
- Dimensions: 2000x1200px minimum

**Alternative sources:**
- Apple Mac Studio press photos (with attribution)
- Your own setup photo

---

### 2. LM Studio Interface
**File:** `lm-studio-loaded.png`
**What to capture:**
- LM Studio window with MiniMax M2-THRIFT loaded
- Show model parameters visible
- Local Server tab showing "Server running"

**How to create:**
```bash
# Open LM Studio
# Load MiniMax M2-THRIFT model
# Take screenshot (Cmd+Shift+4 on Mac)
```

**Key elements to show:**
- Model name: MiniMax-M2-THRIFT-i1
- Quantization: IQ4_XS
- RAM usage: ~70GB
- Server running on port 1234

---

### 3. Mini-Agent Running
**File:** `mini-agent-terminal.png`
**What to capture:**
- Terminal window with mini-agent running
- Show a successful code generation task
- Include timestamp and token speed

**How to create:**
```bash
cd ~/Documents/blogs/minimax-agent-guide
mini-agent
# Run a task: "Create a hello world Python script"
# Screenshot the terminal (Cmd+Shift+4)
```

**Alternative:**
Use screenshot of our actual test with the analog clock example

---

### 4. Performance Comparison (Optional)
**File:** `performance-chart.png`
**What to show:**
- Bar chart comparing inference speed
- MiniMax vs GPT-OSS vs Qwen
- X-axis: Model, Y-axis: Tokens/second

**How to create:**
You can generate this with a simple Python script:

```python
import matplotlib.pyplot as plt

models = ['MiniMax\nM2-THRIFT', 'GPT-OSS\n120B', 'Qwen3\nCoder']
speeds = [12.5, 8.5, 6.2]

plt.figure(figsize=(10, 6))
plt.bar(models, speeds, color=['#4CAF50', '#2196F3', '#FF9800'])
plt.ylabel('Tokens per Second', fontsize=12)
plt.title('Inference Speed Comparison (Mac Studio M2 Ultra)', fontsize=14)
plt.ylim(0, 15)
for i, v in enumerate(speeds):
    plt.text(i, v + 0.3, str(v), ha='center', fontweight='bold')
plt.savefig('performance-chart.png', dpi=300, bbox_inches='tight')
```

---

### 5. Architecture Diagram (Optional)
**File:** `architecture-diagram.png`
**What to show:**
- MiniMax M2 MoE architecture
- 230B total → 10B active
- Visual of expert selection

**How to create:**
- Use draw.io or Excalidraw
- Or screenshot from MiniMax documentation
- Keep it simple and clean

---

## Quick Screenshot Commands

**macOS:**
```bash
# Region screenshot
Cmd + Shift + 4

# Window screenshot
Cmd + Shift + 4, then Space

# Full screen
Cmd + Shift + 3
```

**Save to images folder:**
After taking screenshots, move them:
```bash
mv ~/Desktop/Screen\ Shot*.png ~/Documents/blogs/minimax-agent-guide/images/
```

---

## Image Optimization

Before uploading to GitHub/Medium:

```bash
# Install ImageOptim (macOS)
brew install --cask imageoptim

# Or use command line
# Install: brew install imagemagick
convert input.png -resize 2000x -quality 85 output.jpg
```

---

## Temporary Placeholder Images

If you don't have images yet, you can use these services:

1. **Unsplash** (free, attribution required)
   - Mac Studio: https://unsplash.com/s/photos/mac-studio
   - Terminal: https://unsplash.com/s/photos/terminal-coding

2. **Placeholder services**
   - https://via.placeholder.com/2000x1200/4CAF50/FFFFFF?text=Mac+Studio+Setup
   - https://via.placeholder.com/1600x900/2196F3/FFFFFF?text=LM+Studio+Interface

---

## Final Checklist

- [ ] Hero image (Mac Studio or terminal)
- [ ] LM Studio loaded screenshot
- [ ] Mini-agent running screenshot
- [ ] Performance chart (optional)
- [ ] All images optimized (<500KB each)
- [ ] Images committed to git
- [ ] README.md updated with image paths
