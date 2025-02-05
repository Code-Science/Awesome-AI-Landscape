# Qwen (通义千问) Series Models

## Qwen 1.0 Series (First Generation)
### Base Models
- **Paper**: [Qwen Technical Report](https://arxiv.org/abs/2309.16609)
- **Release Date**: September 2023
- **Available Sizes**: 
  - Qwen-7B
  - Qwen-14B
  - Qwen-72B
- **Links**: 
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/QwenLM/Qwen)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen--7B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen-7B)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen--14B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen-14B)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen--72B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen-72B)
  - [![Blog](https://img.shields.io/badge/📘%20Release%20Blog-blue?style=flat-square)](https://www.modelscope.cn/headlines/article/92)
- **Context Length**: 8192 tokens (7B/14B), 32768 tokens (72B)

### Multimodal Models
#### Qwen-VL
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen--VL-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen-VL)
  - [![Demo](https://img.shields.io/badge/🎮%20Demo-green?style=flat-square)](https://modelscope.cn/studios/qwen/Qwen-VL-Chat-Demo/summary)
- **Features**: Image understanding, generation, and visual QA

#### Qwen-Audio
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen--Audio-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen-Audio)
  - [![Demo](https://img.shields.io/badge/🎮%20Demo-green?style=flat-square)](https://modelscope.cn/studios/qwen/Qwen-Audio-Chat-Demo/summary)
- **Features**: Audio understanding and speech recognition

## Qwen 1.5 Series (Second Generation)
- **Release Date**: January 2024
- **Paper**: [Qwen 1.5 Technical Report](https://arxiv.org/abs/2401.08979)
- **Available Sizes**:
  - Qwen1.5-0.5B
  - Qwen1.5-1.8B
  - Qwen1.5-4B
  - Qwen1.5-7B
  - Qwen1.5-14B
  - Qwen1.5-72B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/QwenLM/Qwen1.5)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen1.5--7B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen1.5-7B)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen1.5--14B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen1.5-14B)
  - [![Blog](https://img.shields.io/badge/📘%20Release%20Blog-blue?style=flat-square)](https://www.modelscope.cn/headlines/article/164)
- **Improvements**:
  - Enhanced performance
  - Better instruction following
  - Improved reasoning capabilities
  - Extended context length (32K tokens)

## Qwen 2 Series (Third Generation)
- **Release Date**: March 2024
- **Available Sizes**:
  - Qwen2-0.5B
  - Qwen2-1.8B
  - Qwen2-4B
  - Qwen2-7B
  - Qwen2-14B
  - Qwen2-72B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/QwenLM/Qwen2)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen2--7B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen2-7B)
  - [![Blog](https://img.shields.io/badge/📘%20Release%20Blog-blue?style=flat-square)](https://www.modelscope.cn/headlines/article/204)
- **Key Features**:
  - New architecture design
  - Stronger performance
  - Better alignment
  - Native 32K context support

## Qwen 2.5 Series (Fourth Generation)
- **Release Date**: April 2024
- **Paper**: [Qwen 2.5 Technical Report](https://qwen.readthedocs.io/en/latest/)
- **Available Sizes**:
  - Qwen2.5-0.5B
  - Qwen2.5-1.5B
  - Qwen2.5-3B
  - Qwen2.5-7B
  - Qwen2.5-14B
  - Qwen2.5-32B
  - Qwen2.5-72B
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/QwenLM/Qwen2.5)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Qwen2.5--7B-ff69b4?style=flat-square)](https://huggingface.co/Qwen/Qwen2.5-7B)
  - [![Blog](https://img.shields.io/badge/📘%20Release%20Blog-blue?style=flat-square)](https://www.modelscope.cn/headlines/article/285)
- **Key Improvements**:
  - Advanced MoE (Mixture of Experts) architecture
  - Enhanced multilingual capabilities
  - Improved code generation
  - Better tool usage abilities
  - Native 32K context support
  - Reduced hallucination
- **New Features**:
  - Advanced reasoning capabilities
  - Enhanced system prompt control
  - Better few-shot learning abilities
  - Improved factual accuracy


## Model Variants
Each series includes multiple variants:
- **Base**: Raw pretrained models
- **Chat**: Fine-tuned for dialogue
- **Compressed**: INT4/INT8 quantized versions
- **Long**: Extended context length versions

## Development Resources

### Documentation
- [![Docs](https://img.shields.io/badge/📚%20Technical%20Docs-green?style=flat-square)](https://github.com/QwenLM/Qwen/tree/main/docs)
- [![Guide](https://img.shields.io/badge/📚%20Deployment%20Guide-green?style=flat-square)](https://github.com/QwenLM/Qwen/blob/main/docs/inference_zh.md)
- [![Tutorial](https://img.shields.io/badge/📚%20Fine--tuning%20Guide-green?style=flat-square)](https://github.com/QwenLM/Qwen/blob/main/docs/finetune_zh.md)

### Community
- [![Discord](https://img.shields.io/badge/💬%20Discord-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/z3GAxXZ9Ce)
- [![ModelScope](https://img.shields.io/badge/🔗%20ModelScope-blue?style=flat-square)](https://www.modelscope.cn/models/qwen)

### Integration & Tools
- [vLLM Support](https://github.com/vllm-project/vllm)
- [FastChat Integration](https://github.com/lm-sys/FastChat)
- [OpenCompass Evaluation](https://github.com/open-compass/opencompass)


