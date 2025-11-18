# State-of-the-Art Local AI Agents: What 128GB of RAM Can Do in Late 2025

*Running AI coding agents completely locally on Mac Studio, DGX Spark, and AMD AI Max hardware when you don't want to use cloud APIs.*

---

![AI Model Leaderboard](https://raw.githubusercontent.com/latent-variable/minimax-agent-guide/master/images/artificial_analysis_ranking.png)

*MiniMax M2 ranks among the top open-source models globally*

---

With 128GB of RAM becoming standard in high-end consumer machines, you can now run state-of-the-art AI agents entirely locally. This guide shows you how to deploy MiniMax M2-THRIFT with Mini-Agent, achieving near Claude 3.5 Sonnet performance for privacy-sensitive work and tasks where you prefer to avoid cloud APIs.

## Why This Matters

Most AI agent frameworks force you to choose between:

- **Expensive cloud APIs:** $10-75 per million tokens adds up fast
- **Inconsistent local models:** struggle with complex tasks and tool use
- **Privacy trade-offs:** your code and data sent to third parties

MiniMax M2-THRIFT + Mini-Agent solves all three problems.

## Who This Guide Is For

This guide is for you if:

- You have at least 128GB of RAM (Mac Studio, MacBook Pro, etc.)
- You have an AI workstation with GPUs (couple of A6000s, etc.)
- You're curious about running AI agents completely locally

You can run a fully capable AI coding agent locally that rivals commercial APIs.

---

## Understanding MiniMax M2-THRIFT

### The Base Model

MiniMax M2 is a Mixture-of-Experts (MoE) model released in October 2025:

**Architecture:**
- 230 billion total parameters
- Only 10 billion active per token
- Up to 200K token context window
- Modified MIT license (fully open)

**Performance:**
- Ranks #1 among open-source models on Artificial Analysis Intelligence Index
- 67% coding score, 61% overall intelligence
- Specifically optimized for agentic workflows
- Comparable to Claude 3.5 Sonnet on practical coding tasks

### What Makes THRIFT Special

THRIFT applies expert pruning to reduce the model by ~25%:

**Benefits:**
- Faster CPU inference
- Lower memory: ~100GB RAM required
- 95% of full model quality

**Benchmarks:**
- Math: +0.53% vs full
- Coding: +1.10% vs full
- Knowledge: -4-5% vs full

### REAP Variants

Even more efficient options:

**REAP-172B:** 65GB RAM, 2% performance loss
**REAP-162B:** 60GB RAM, 5% performance loss

---

## Hardware Requirements

**RAM: 128GB minimum**
- Model: ~100GB
- System + Headroom: ~28GB

**Storage: 100GB free**

**CPU: 16+ cores recommended** (Apple M3/M4 Max or better)
- M3/M4 Max: 16 CPU cores, 40 GPU cores
- Ideal for this workload

---

## Installation

### Step 1: Install LM Studio

Download from [lmstudio.ai](https://lmstudio.ai)

### Step 2: Download Model

In LM Studio:
1. Search: `MiniMax-M2-THRIFT-i1`
2. Select: **IQ4_XS** quantization
3. Download

**If split into parts:**

```bash
cd ~/.lmstudio/models/mradermacher/MiniMax-M2-THRIFT-i1-GGUF/
cat MiniMax-M2-THRIFT.i1-IQ4_XS.gguf.part1of2 \
    MiniMax-M2-THRIFT.i1-IQ4_XS.gguf.part2of2 \
    > MiniMax-M2-THRIFT.i1-IQ4_XS.gguf
rm *.part*
```

### Step 3: Start Server

1. Load model in LM Studio
2. Configure model settings:

![LM Studio Model Loading](https://raw.githubusercontent.com/latent-variable/minimax-agent-guide/master/images/LM-studio_model_loading.png)

3. Start Local Server (port 1234)
4. Verify: `http://localhost:1234/v1/models`

### Step 4: Install Mini-Agent

```bash
cd ~/Documents
git clone https://github.com/MiniMax-AI/Mini-Agent.git
cd Mini-Agent
pip install -e .
```

### Step 5: Configure

```bash
mkdir -p ~/.mini-agent/config
```

Create `~/.mini-agent/config/config.yaml`:

```yaml
api_key: "not-needed"
api_base: "http://localhost:1234"
model: "minimax-m2-thrift-i1"
provider: "openai"

retry:
  enabled: true
  max_retries: 3
  initial_delay: 1.0

max_steps: 100
workspace_dir: "./workspace"
system_prompt_path: "system_prompt.md"

tools:
  enable_file_tools: true
  enable_bash: true
  enable_note: true
  enable_skills: true
  skills_dir: "./skills"
```

Copy system prompt:

```bash
cp ~/Documents/Mini-Agent/mini_agent/config/system_prompt.md ~/.mini-agent/config/
```

### Step 6: Optimize for Local Performance

**The Problem:** By default, Mini-Agent sends requests that cause LM Studio to reprocess all tokens on every request, wasting time and resources.

**The Fix:** Edit `~/Documents/Mini-Agent/mini_agent/llm/openai_client.py` around line 65:

```python
params = {
    "model": self.model,
    "messages": api_messages,
    # Add consistent parameters for better KV cache stability
    "temperature": 0.7,  # Consistent temperature prevents cache invalidation
    "seed": 42,  # Fixed seed for deterministic behavior
    # NOTE: Comment out reasoning_split for local models
    # "extra_body": {"reasoning_split": True},
}
```

**What this does:**
- Consistent `temperature` and `seed` prevent cache invalidation
- Removing `reasoning_split` from `extra_body` improves cache compatibility
- LM Studio can now reuse KV cache between requests

**Expected results:**
- First request: Full processing (builds cache)
- Follow-up requests: Only process new tokens (much faster)
- Reduced token reprocessing: 90%+ improvement

---

## Usage

```bash
cd ~/my-project
mini-agent
```

### Example: Code Generation

```
Create a Python script for CSV analysis with visualizations
```

The agent will:
1. Create script structure
2. Import libraries
3. Write data loading
4. Add statistical analysis
5. Generate visualizations

### Example: Refactoring

```
Refactor to async/await with error handling
```

The agent will:
1. Read all files
2. Identify blocking code
3. Convert to async
4. Add error handling
5. Update call sites

---

## Cost Analysis

**ChatGPT Plus:** $20/month, no privacy, usage limits
**Claude Pro:** $20/month, no privacy, usage limits
**MiniMax Local:** $0/month, full privacy, unlimited usage

This won't replace your API subscriptions, but it allows you to do incredible things completely locally when you don't want to use cloud services.

---

## Real-World Test: Analog Clock

*Test methodology from [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1oxxrhc/kimi_k2_is_the_best_clock_ai/)*

**Prompt:**
```
Create HTML/CSS of an analog clock showing ${time}. Include numbers (or numerals)
if you wish, and have a CSS animated second hand. Make it responsive and use a
white background.
```

**Results:**

**MiniMax M2-THRIFT:** ✓ Working on first try

![MiniMax Clock Result](https://raw.githubusercontent.com/latent-variable/minimax-agent-guide/master/images/minimax_clock.png)

**GPT-OSS-120B:** Required 3 iterations

![GPT-OSS Clock Result](https://raw.githubusercontent.com/latent-variable/minimax-agent-guide/master/images/gpt-oss-120b_clock.png)

**Qwen3-Coder:** Too large for 128GB

---

## Troubleshooting

**Model not found:**
```bash
curl http://localhost:1234/v1/models
```

**Out of memory:**
Try IQ3_XXS quantization or REAP-162B variant

**Slow inference:**
- Close background apps
- Check CPU cooling
- Ensure model fully loaded

---

## Alternative: Codex + GPT-OSS

MiniMax M2 had consistency issues with Codex's `apply_patch` tool.

For Codex users, try GPT-OSS-120B instead:

```toml
[model_providers.lms]
base_url = "http://localhost:1234/v1"

[profiles.gpt-oss-120b-lms]
model_provider = "lms"
model = "openai/gpt-oss-120b"
```

---

## When to Use Local vs Cloud

**Use Local:**
- Privacy-sensitive work
- 10M+ tokens/month
- Offline requirements
- Unlimited experimentation

**Use Cloud:**
- Multi-modal tasks
- Occasional use (<1M tokens/month)
- Latest capabilities

---

## Conclusion

MiniMax M2-THRIFT on 128GB machines offers:

- Near Claude 3.5 Sonnet performance
- Complete privacy
- Zero ongoing costs
- Offline functionality
- Unlimited local experimentation

**Investment:** Mac Studio ($3,999) or alternatives
**Setup time:** ~2 hours

### Next Steps

1. Download THRIFT with IQ4_XS
2. Install Mini-Agent
3. Test with simple tasks
4. Explore REAP variants if needed

The future of AI development isn't exclusively cloud-based.

---

**Resources:**
- [LM Studio](https://lmstudio.ai)
- [Mini-Agent](https://github.com/MiniMax-AI/Mini-Agent)
- [THRIFT Model](https://huggingface.co/VibeStudio/MiniMax-M2-THRIFT)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

*By Lino Valdovinos | January 2025 | MacBook Pro M3 Max*
