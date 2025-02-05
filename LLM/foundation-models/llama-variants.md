# LLaMA and Its Variants

## LLaMA (Original)
- **Paper**: [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
- **Release Date**: February 2023
- **Links**: 
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/facebookresearch/llama)
  - [![Paper Explained](https://img.shields.io/badge/📝%20Paper%20Explained-blue?style=flat-square)](https://blog.mlflow.org/llama-paper-explained-e66a8d7f2f0e)
  - [![Video](https://img.shields.io/badge/🎥%20Video-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=5wHwVs1kxRU)
- **Parameters**: 7B, 13B, 33B, 65B
- **Training Data**: 1.4T tokens

## LLaMA 2
- **Paper**: [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)
- **Release Date**: July 2023
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-ff69b4?style=flat-square)](https://huggingface.co/meta-llama)
  - [![Meta AI Blog](https://img.shields.io/badge/📘%20Meta%20AI%20Blog-blue?style=flat-square)](https://ai.meta.com/llama/)
  - [![Video](https://img.shields.io/badge/🎥%20Video-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=zJBpRn2zTco)
  - [![Paper Explained](https://img.shields.io/badge/📝%20Paper%20Explained-blue?style=flat-square)](https://blog.mlflow.org/llama-2-paper-summary-and-explained-5ba3494f46c8)
- **Parameters**: 7B, 13B, 70B
- **Variants**:
  - Llama 2 (Base)
  - Llama 2 Chat
  - Llama 2 Fine-tuned

## Notable Variants

### CodeLlama
- **Paper**: [Code Llama: Open Foundation Models for Code](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/)
- **Links**:
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-ff69b4?style=flat-square)](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)
  - [![Video](https://img.shields.io/badge/🎥%20Video-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=vf3tjuV3Z4g)
  - [![Tutorial](https://img.shields.io/badge/📚%20Tutorial-green?style=flat-square)](https://huggingface.co/blog/code-llama)
- **Specialization**: Code generation and understanding

### Vicuna
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lm-sys/FastChat)
  - [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-ff69b4?style=flat-square)](https://huggingface.co/lmsys/vicuna-13b-v1.5)
  - [![Video](https://img.shields.io/badge/🎥%20Video-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=NXF3JYVYFnE)
- **Based on**: LLaMA fine-tuning

### Alpaca
- **Links**:
  - [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tatsu-lab/stanford_alpaca)
  - [![Blog](https://img.shields.io/badge/📘%20Blog-blue?style=flat-square)](https://crfm.stanford.edu/2023/03/13/alpaca.html)
  - [![Video](https://img.shields.io/badge/🎥%20Video-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=v_FEzqmGAP0)
- **Training Data**: Self-instruct dataset generated using text-davinci-003

## Key Features
- Open source foundation model
- Competitive performance with closed models
- Efficient architecture
- Strong multilingual capabilities
- Extensive community adoption

## Training & Fine-tuning
- Pre-training approach
- Instruction fine-tuning methods
- RLHF implementation

## Additional Resources
### Technical Deep Dives
- [![Video](https://img.shields.io/badge/🎥%20Architecture%20Explained-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=Mn_9W1nCFLo)
- [![Article](https://img.shields.io/badge/📝%20Training%20Process-blue?style=flat-square)](https://www.databricks.com/blog/llama-2-foundation-models)
- [![Guide](https://img.shields.io/badge/📚%20Fine--tuning%20Guide-green?style=flat-square)](https://huggingface.co/blog/llama2)

### Community & Development
- [LLaMA.cpp](https://github.com/ggerganov/llama.cpp) - CPU inference optimization
- [Ollama](https://github.com/ollama/ollama) - Run LLaMA models locally
- [LangChain + LLaMA Guide](https://python.langchain.com/docs/integrations/llms/llama)
