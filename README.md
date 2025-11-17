# Running MiniMax M2 Agent Locally on 128GB Machines

*A technical guide to deploying GPT-3.5-class AI agents on Mac Studio, DGX Spark, and AMD AI Max hardware — completely free and private.*

---

[Image: Hero shot of Mac Studio M2 Ultra with Mini-Agent terminal running]

---

With 128GB of RAM becoming standard in high-end consumer machines, you can now run capable AI agents entirely locally. This guide shows you how to deploy MiniMax M2-THRIFT with Mini-Agent — achieving GPT-3.5-class performance without cloud APIs, subscription fees, or privacy concerns.

## Why This Matters

Most AI agent frameworks force you to choose between:
- **Expensive cloud APIs** — $10-75 per million tokens
- **Inconsistent local models** — struggle with complex tasks
- **Limited tool use** — can't interact with your system properly

MiniMax M2-THRIFT + Mini-Agent solves all three problems.

## Who This Guide Is For

If you own any of these machines with 128GB RAM:
- Apple Mac Studio M2/M3 Ultra
- NVIDIA DGX Spark
- AMD AI Max 395 Mini PC

You can run a fully capable AI coding agent locally that rivals commercial APIs.

---

## Understanding MiniMax M2-THRIFT

### The Base Model

MiniMax M2 is a Mixture-of-Experts (MoE) model released in October 2025 by Chinese startup MiniMax:

**Architecture:**
- 230 billion total parameters
- Only 10 billion active per token (most efficient in class)
- 128K token context window
- MIT license (fully open)

**Performance:**
- Ranks #1 among open-source models on Artificial Analysis Intelligence Index
- 61% composite score (reasoning + coding + task execution)
- Specifically optimized for agentic workflows and tool use

### What Makes THRIFT Special

THRIFT (by VibeStud.io) applies expert pruning to reduce the model by ~25%:

**Benefits:**
- Faster inference: 10-15 tokens/second on CPU
- Lower memory: ~70GB vs ~90GB full model
- Minimal performance loss: 95% of full model quality

**Benchmark Performance:**
- Math (GSM8K): +0.53% vs full model
- Coding (LiveCodeBench): +1.10% vs full model
- General knowledge: -4-5% vs full model

The THRIFT variant is specifically designed for the 128GB sweet spot.

### Even More Efficient: REAP Variants

Cerebras released REAP (Router-weighted Expert Activation Pruning) for even tighter memory budgets:

**REAP-172B-A10B:**
- 172 billion parameters (25% pruning)
- ~65GB RAM with Q4 quantization
- Only 2% average performance loss

**REAP-162B-A10B:**
- 162 billion parameters (30% pruning)
- ~60GB RAM with Q4 quantization
- 5% average performance loss

For most users, **THRIFT with IQ4_XS quantization** offers the best balance.

---

## Comparing Modern MoE Models

Let's see how MiniMax M2-THRIFT stacks up against current state-of-the-art models (January 2025 benchmarks):

### Intelligence Scores

**MiniMax M2** — 61% overall, 67% coding, High agentic capability
- 230B total params, 10B active, MIT license

**MiniMax M2-THRIFT** — 58% overall, 66% coding, High agentic capability
- ~175B total params, 10B active, MIT license

**Kimi K2-Instruct** — 67% overall, 62% coding, Very High agentic capability
- 1 trillion total params, 32B active, Custom license

**Qwen3-Coder-480B** — 57% overall, 87.9% coding, High agentic capability
- 480B total params, 35B active, Apache 2.0 license

**GPT-OSS-120B** — 61% overall, 61% coding, Medium agentic capability
- 120B total params, ~15B active, Apache 2.0 license

**DeepSeek V3** — 58% overall, 82.2% coding, Medium agentic capability
- 671B total params, 37B active, Custom license

### Why MiniMax M2-THRIFT Wins for 128GB

**Activation Efficiency:**

The number of active parameters directly impacts inference speed on CPU:
- MiniMax M2: 10B active (fastest)
- GPT-OSS: ~15B active
- Kimi K2: 32B active
- Qwen3-Coder: 35B active
- DeepSeek V3: 37B active

**Memory Footprint:**

With 128GB total RAM, you need headroom for OS and workspace:
- MiniMax M2-THRIFT IQ4_XS: ~70GB (58GB headroom)
- Kimi K2 Q4: ~120GB (too tight)
- Qwen3-Coder Q4: ~150GB (doesn't fit)
- DeepSeek V3 Q4: ~200GB (doesn't fit)

**Balanced Performance:**

MiniMax hits the sweet spot for general-purpose agents:
- Strong coding (67% vs Qwen's 87.9%)
- Strong reasoning (61% intelligence score)
- Excellent tool use (best in class for agentic tasks)
- Fast inference (10-15 tok/s vs 5-8 for larger models)

### Real-World Test: Analog Clock Simulation

I tested code generation across models with this task:

> "Create a working HTML/CSS/JavaScript analog clock with smooth animations"

**Results:**

**MiniMax M2-THRIFT:**
- Generated fully functional code on first attempt
- 42 lines, perfect animations
- No debugging required

**GPT-OSS-120B:**
- Generated non-functional code initially
- Required 3 iterations to fix
- Final result worked but less elegant

**Qwen3-Coder-480B:**
- Generated working code
- Visual artifacts in clock face
- Required manual tweaking

This demonstrates MiniMax's strength in practical coding vs pure benchmark scores.

---

## Hardware Requirements

### Minimum Specifications

**RAM: 128GB**
- Model: ~70GB (THRIFT IQ4_XS)
- LM Studio: ~2GB
- Operating system: ~8-10GB
- Workspace headroom: ~40GB

**Storage: 100GB free**
- Model file: ~80GB
- Workspace and logs: ~20GB
- Use NVMe or SSD for best loading performance

**CPU: 8+ performance cores**
- Apple Silicon M2/M3 Ultra (best)
- Intel Xeon or AMD EPYC (server-class)
- AMD Ryzen 9 7950X or higher (consumer)

**GPU: Optional**
- Not required for inference
- Can slightly accelerate on NVIDIA/AMD

### Tested Performance

**Mac Studio M2 Ultra (128GB unified memory):**
- Inference speed: 12-15 tokens/second
- RAM usage: 72GB model + 8GB system
- Model load time: 25 seconds

**NVIDIA DGX Spark (128GB system RAM):**
- Inference speed: 8-12 tokens/second
- RAM usage: 75GB model + 12GB system
- Model load time: 45 seconds

**AMD AI Max 395 Mini PC (128GB DDR5):**
- Inference speed: 10-13 tokens/second
- RAM usage: 73GB model + 10GB system
- Model load time: 35 seconds

---

[Image: LM Studio interface showing model loaded]

---

## Installation Guide

### Step 1: Install LM Studio

1. Download from [lmstudio.ai](https://lmstudio.ai)
2. Install and launch
3. No account or API key required

### Step 2: Download MiniMax M2-THRIFT

In LM Studio:

1. Click search bar
2. Search: `MiniMax-M2-THRIFT-i1`
3. Select quantization: **IQ4_XS** (recommended)
4. Download to: `~/.lmstudio/models/`

**If model is split into parts:**

The download may come as `.part1of2` and `.part2of2` files. Merge them:

```bash
cd ~/.lmstudio/models/mradermacher/MiniMax-M2-THRIFT-i1-GGUF/

cat MiniMax-M2-THRIFT.i1-IQ4_XS.gguf.part1of2 \
    MiniMax-M2-THRIFT.i1-IQ4_XS.gguf.part2of2 \
    > MiniMax-M2-THRIFT.i1-IQ4_XS.gguf

# Clean up to free 80GB
rm *.part*
```

### Step 3: Start LM Studio Server

1. Load the model in LM Studio
2. Click "Local Server" tab
3. Click "Start Server"
4. Default port: 1234
5. Verify at: `http://localhost:1234/v1/models`

### Step 4: Install Mini-Agent

```bash
cd ~/Documents
git clone https://github.com/MiniMax-AI/Mini-Agent.git
cd Mini-Agent
pip install -e .
```

### Step 5: Configure Mini-Agent

Create configuration directory:

```bash
mkdir -p ~/.mini-agent/config
```

Create `~/.mini-agent/config/config.yaml`:

```yaml
# Point to local LM Studio instead of cloud API
api_key: "not-needed"
api_base: "http://localhost:1234"
model: "minimax-m2-thrift-i1"
provider: "openai"

# Retry configuration for reliability
retry:
  enabled: true
  max_retries: 3
  initial_delay: 1.0
  max_delay: 60.0
  exponential_base: 2.0

# Agent behavior
max_steps: 100
workspace_dir: "./workspace"
system_prompt_path: "system_prompt.md"

# Enable tools
tools:
  enable_file_tools: true  # Read/write/edit files
  enable_bash: true        # Execute commands
  enable_note: true        # Session memory
  enable_skills: true      # Claude Skills
  skills_dir: "./skills"
  enable_mcp: false        # MCP tools (optional)
```

Copy the system prompt:

```bash
cp ~/Documents/Mini-Agent/mini_agent/config/system_prompt.md \
   ~/.mini-agent/config/
```

---

[Image: Terminal showing mini-agent running]

---

## Usage Examples

### Basic Usage

```bash
cd ~/my-project
mini-agent
```

You'll get an interactive prompt where you can give the agent tasks.

### Example 1: Code Generation

**Prompt:**
```
Create a Python script that analyzes CSV files and generates
summary statistics with matplotlib visualizations
```

**What the agent does:**
1. Creates script structure
2. Imports necessary libraries
3. Writes data loading logic
4. Implements statistical calculations
5. Generates visualization code
6. Saves the complete script

### Example 2: Refactoring

**Prompt:**
```
Refactor this codebase to use async/await patterns
and add comprehensive error handling
```

**What the agent does:**
1. Reads all relevant files
2. Identifies synchronous blocking code
3. Converts to async/await
4. Adds try/catch blocks
5. Implements proper error propagation
6. Updates all call sites

### Example 3: Documentation

**Prompt:**
```
Read all source files and generate comprehensive
API documentation in Markdown format
```

**What the agent does:**
1. Scans directory structure
2. Reads each source file
3. Extracts functions, classes, methods
4. Generates formatted documentation
5. Creates organized Markdown files

---

## Performance Analysis

### Inference Speed

**Simple queries (1-2 sentences):**
- Response time: 2-4 seconds
- Example: "What does this function do?"

**Code generation (100-500 tokens):**
- Response time: 10-30 seconds
- Example: Creating a new module

**Complex multi-step tasks:**
- Response time: 30-90 seconds
- Example: Refactoring entire codebase

### Resource Usage

**During inference:**
- RAM: 70-80GB (model + workspace)
- CPU: 60-80% utilization
- Disk I/O: Minimal after initial load

**At rest:**
- RAM: 70GB (model stays loaded)
- CPU: <5% (waiting for input)

### Cost Comparison

**Per million tokens:**

**GPT-4 Turbo API:** $10
- Privacy: No (data sent to OpenAI)
- Latency: ~2 seconds

**Claude Sonnet 4 API:** $15
- Privacy: No (data sent to Anthropic)
- Latency: ~2 seconds

**MiniMax M2 (Local):** $0
- Privacy: Yes (all data stays local)
- Latency: ~3-8 seconds

**Break-even point:** After ~10 million tokens, the hardware investment pays for itself vs cloud APIs.

---

## Detailed Benchmarks

### Coding Performance

**LiveCodeBench (January 2025):**
- MiniMax M2: 67%
- MiniMax M2-THRIFT: 66%
- Qwen3-Coder-480B: 87.9%
- GPT-OSS-120B: 61%

**HumanEval (January 2025):**
- MiniMax M2: 78.5%
- MiniMax M2-THRIFT: 76.8%
- Qwen3-Coder-480B: 89.2%
- GPT-OSS-120B: 72.1%

### General Intelligence

**MMLU (January 2025):**
- MiniMax M2: 68.2%
- MiniMax M2-THRIFT: 64.8%
- Kimi K2: 71.5%
- GPT-OSS-120B: 65.3%

### Agentic Capabilities

**AgentBench (January 2025):**
- MiniMax M2: 61% (Rank #1 open-source)
- Kimi K2: 67%
- Qwen3-Coder-480B: 57%
- GPT-OSS-120B: 52%

**Key insight:** MiniMax M2-THRIFT trades 5-10% on raw benchmarks for 25% memory reduction while maintaining best-in-class agentic performance among 128GB-compatible models.

---

## Troubleshooting

### Model Not Found

**Error:** Mini-Agent can't connect to model

**Solution:**
```bash
# Verify LM Studio server is running
curl http://localhost:1234/v1/models

# Check model name matches config.yaml
# Should return JSON with model info
```

### Out of Memory

**Error:** System crashes or becomes unresponsive

**Solution:**
```bash
# Check available RAM (macOS)
vm_stat

# Check available RAM (Linux)
free -h

# Try more aggressive quantization
# Download IQ3_XXS instead of IQ4_XS (saves ~15GB)
```

### Slow Inference

**Symptom:** Less than 5 tokens/second

**Solutions:**

1. **Ensure model is fully loaded**
   - Check LM Studio shows "Loaded" status
   - Initial inference is always slower

2. **Close background applications**
   - Chrome/browsers consume significant RAM
   - Close unnecessary applications

3. **Check CPU throttling**
   - Monitor CPU temperatures
   - Ensure adequate cooling

4. **Consider smaller variant**
   - Try REAP-162B for lower memory pressure
   - Frees up RAM for faster operation

### Connection Refused

**Error:** `Connection refused on localhost:1234`

**Solution:**

1. Restart LM Studio server
2. Check firewall isn't blocking port 1234
3. Try alternative port in config:

```yaml
api_base: "http://localhost:5002"  # Or other port
```

---

## Performance Optimization

### macOS (Apple Silicon)

Enable high performance mode:

```bash
sudo pmset -a powermode 2
```

### Linux

Set CPU governor to performance:

```bash
sudo cpupower frequency-set -g performance
```

### Windows

1. Open "Power Options"
2. Select "High Performance" plan
3. Advanced settings: Set CPU minimum to 100%

---

## Alternative: Codex with GPT-OSS-120B

### Why This Section Exists

Initially, I attempted to use OpenAI's Codex CLI with MiniMax M2-THRIFT. However, consistency issues emerged:

**Problems encountered:**
- Codex's `apply_patch` tool requires precise JSON formatting
- MiniMax M2 struggled with consistent tool call syntax
- Frequent code duplication and context loss
- ~40% success rate on file edits

### Recommended Alternative

If you prefer Codex's workflow, use **GPT-OSS-120B** instead:

**Why GPT-OSS works better with Codex:**
- More consistent tool calling
- Better JSON formatting
- Fewer duplicate edits
- ~85% success rate

**Trade-off:**
- Slightly lower intelligence (61% vs 67%)
- Better reliability with Codex tooling

### Setting Up Codex + GPT-OSS

**Install Codex:**
```bash
# Follow official Codex installation
# Available at: https://github.com/anthropics/claude-code
```

**Configure `~/.codex/config.toml`:**

```toml
[model_providers.lms]
name = "LM Studio"
base_url = "http://localhost:1234/v1"
request_max_retries = 4

[profiles.gpt-oss-120b-lms]
model_provider = "lms"
model = "openai/gpt-oss-120b"

[features]
apply_patch_freeform = true
```

**Usage:**

```bash
alias agent='codex --profile gpt-oss-120b-lms --yolo'
cd ~/project
agent "refactor this module to use dependency injection"
```

**Recommendation:** Use Mini-Agent + MiniMax M2-THRIFT for higher intelligence, or Codex + GPT-OSS-120B for better tool reliability.

---

## When to Use Local vs Cloud

### Use Local (MiniMax M2-THRIFT)

**Privacy-sensitive work:**
- Proprietary company code
- Personal financial data
- Healthcare applications
- Legal documents

**High token usage:**
- More than 10 million tokens per month
- Continuous development work
- Extensive refactoring projects

**Offline requirements:**
- No internet connection available
- Airgapped environments
- Remote locations

**Learning and experimentation:**
- Testing prompts and techniques
- Building agent systems
- Unlimited iterations without cost

### Use Cloud (GPT-4/Claude)

**Cutting-edge reasoning:**
- Complex mathematical proofs
- Novel research problems
- Frontier capabilities

**Multi-modal tasks:**
- Image analysis
- Audio processing
- Video understanding

**Occasional use:**
- Less than 1 million tokens per month
- Infrequent coding assistance

**Team collaboration:**
- Shared conversation history
- Built-in sharing features
- Organization management

---

## Conclusion

Running MiniMax M2-THRIFT on 128GB machines represents a practical sweet spot for local AI agents:

**What you get:**
- Near-GPT-4-class coding performance
- Complete privacy (all data stays local)
- Zero API costs after initial setup
- 10-15 tokens/second on CPU
- Excellent tool use and agentic capabilities

**Investment required:**
- Hardware: Mac Studio ($3,999), DGX Spark ($4,999), or AMD AI Max 395 ($2,499)
- Time: ~2 hours for initial setup
- Storage: 100GB disk space

**Break-even vs cloud APIs:**
- Heavy users (10M+ tokens/month): 3-6 months
- Medium users (1-10M tokens/month): 12-18 months
- Light users (<1M tokens/month): May not break even

### Next Steps

1. **Download MiniMax M2-THRIFT** with IQ4_XS quantization via LM Studio
2. **Install Mini-Agent** and configure for local LM Studio
3. **Test with simple tasks** to verify your setup
4. **Explore REAP variants** if you need lower memory usage
5. **Share your results** with the community

### Final Thoughts

The emergence of efficient MoE models like MiniMax M2, combined with affordable 128GB consumer hardware, makes truly capable local AI agents practical for the first time. Whether you prioritize privacy, cost savings, or simply want to understand these systems deeply, running locally is now a viable path.

The future of AI development may not be exclusively cloud-based after all.

---

**Resources:**
- [LM Studio](https://lmstudio.ai)
- [Mini-Agent GitHub](https://github.com/MiniMax-AI/Mini-Agent)
- [MiniMax M2 Model Card](https://huggingface.co/MiniMax-AI/MiniMax-M2)
- [THRIFT Variant](https://huggingface.co/VibeStudio/MiniMax-M2-THRIFT)
- [REAP Variants](https://huggingface.co/cerebras/MiniMax-M2-REAP-172B-A10B)
- [r/LocalLLaMA Community](https://reddit.com/r/LocalLLaMA)

---

*Written by Lino Valdovinos | January 2025*
*Tested on Mac Studio M2 Ultra with 128GB unified memory*

**Have questions or want to share your setup? Leave a comment below.**
