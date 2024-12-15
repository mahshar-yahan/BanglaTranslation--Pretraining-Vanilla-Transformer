# BanglaTranslation: Pretraining Vanilla Transformer

This repository contains the implementation of a **Vanilla Transformer** model for **Bangla translation**. The transformer is implemented from scratch, using basic of attention mechanisms and encoder-decoder architecture. This project demonstrates the power of the transformer model for machine translation tasks.
- **Multi-head Attension Based Architecture**: Exact replication of **attention all you need** . The encoder processes the input sequence by applying self-attention to capture intra-sequence dependencies, while the decoder generates the translated output through a combination of self-attention and cross-attention mechanisms.
- **Multi-Query Attention Based Architecture**: This approach enhances computational efficiency by sharing key-value pairs across all attention heads, making it more memory-efficient.
- **Positional Encoding**: Since transformers don't process data sequentially, positional encoding is added to provide information about the position of words in the sequence.


## Project Overview

The Vanilla Transformer model is designed to translate text from one language to another. In this project, it focuses on **Bangla translation**. The model is built from the ground up to help you understand how transformers work at a low level.

### Key Components:
- **Encoder-Decoder Architecture**: The model follows the standard encoder-decoder setup of the transformer, where the encoder processes the input sequence, and the decoder generates the translated output.
- **Multi-Head Attention**: A key component of the transformer model that allows the model to focus on different parts of the input sequence at the same time.
- **Positional Encoding**: Since transformers don't process data sequentially, positional encoding is added to provide information about the position of words in the sequence.

## Features
- **Training from scratch**: The transformer is implemented without using any pre-built libraries or models.
- **Customizable Architecture**: The model architecture can be adjusted based on the translation task requirements (e.g., changing the number of layers, heads in multi-head attention, etc.).
- **Bangla Language Support**: The model is specifically tailored for Bangla translation, but the code can be adapted to other languages.
## Hardware
- **GPU**: RTX 3070 8gb 256 bit varient
- **RAM**: 16 gb

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mahshar-yahan/BanglaTranslation--Pretraining-Vanilla-Transformer.git
