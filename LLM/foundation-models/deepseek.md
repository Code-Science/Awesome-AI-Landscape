# DeepSeek Series Models

## DeepSeek LLM Series
### DeepSeek Base Models
- **Release Date**: October 2023
- **Paper**: [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](https://arxiv.org/abs/2401.02954)
- **Available Sizes**:
  - DeepSeek-7B
  - DeepSeek-67B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-LLM)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--7B-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-llm-7b-base)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--67B-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-llm-67b-base)
  - [![Blog](https://img.shields.io/badge/📘%20Release%20Blog-blue?style=flat-square)](https://deepseek.ai/blog/)
- **Context Length**: 8192 tokens
- **Features**:
  - Strong general capabilities
  - High performance on reasoning tasks
  - Excellent coding abilities

### DeepSeek Chat Models
- **Available Variants**:
  - DeepSeek-7B-Chat
  - DeepSeek-67B-Chat
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--7B--Chat-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--67B--Chat-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-llm-67b-chat)
- **Features**:
  - Aligned with human preferences
  - Strong dialogue capabilities
  - Safety improvements

## DeepSeek-Coder Series
- **Release Date**: October 2023
- **Paper**: [DeepSeek Coder: Let the Code Write Itself](https://arxiv.org/abs/2401.14196)
- **Available Sizes**:
  - DeepSeek-Coder-1.3B
  - DeepSeek-Coder-6.7B
  - DeepSeek-Coder-33B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-Coder)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--Coder--6.7B-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--Coder--33B-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-coder-33b-base)
- **Features**:
  - Specialized in code generation
  - Multi-language support
  - Strong code understanding
  - Advanced problem-solving capabilities

### DeepSeek-Coder-Instruct Models
- **Available Variants**:
  - DeepSeek-Coder-1.3B-Instruct
  - DeepSeek-Coder-6.7B-Instruct
  - DeepSeek-Coder-33B-Instruct
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--Coder--6.7B--Instruct-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--Coder--33B--Instruct-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct)
- **Features**:
  - Instruction-following capabilities
  - Enhanced code explanation
  - Interactive coding assistance

## DeepSeek-MoE Series
- **Release Date**: January 2024
- **Available Models**:
  - DeepSeek-MoE-16B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepseek-ai/DeepSeek-MoE)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20DeepSeek--MoE--16B-ff69b4?style=flat-square)](https://huggingface.co/deepseek-ai/deepseek-moe-16b-base)
- **Features**:
  - Mixture of Experts architecture
  - Efficient computation
  - Strong performance with smaller parameter count
  - Enhanced reasoning capabilities

## Model Variants
Each series includes multiple variants:
- **Base**: Raw pretrained models
- **Chat/Instruct**: Fine-tuned for dialogue/instruction
- **Quantized**: INT4/INT8 versions for efficient deployment

## Development Resources

### Documentation
- [![Docs](https://img.shields.io/badge/📚%20Technical%20Docs-green?style=flat-square)](https://github.com/deepseek-ai/DeepSeek-LLM/tree/main/docs)
- [![Guide](https://img.shields.io/badge/📚%20Usage%20Guide-green?style=flat-square)](https://github.com/deepseek-ai/DeepSeek-LLM#usage)

### Integration & Tools
- [vLLM Support](https://github.com/vllm-project/vllm)
- [FastChat Integration](https://github.com/lm-sys/FastChat)