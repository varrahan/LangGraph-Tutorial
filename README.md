# LangGraph Tutorial

A collection of small exercises providing a basic introduction to LangGraph, a powerful framework for building structured agents and workflows with LangChain.

## 📋 Overview

This repository contains practical exercises designed to help you learn the fundamentals of LangGraph. LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful AI agents. It provides the flexibility to create fully customizable agent workflows with support for durable execution, human-in-the-loop interactions, and comprehensive memory management.

## 🎯 What is LangGraph?

LangGraph is a Python framework inspired by Pregel and Apache Beam that allows you to:
- Build stateful, multi-actor applications with LLMs
- Create cyclical graph structures (unlike traditional DAGs)
- Implement explicit control flow between agent nodes
- Manage persistent state across conversations
- Support human oversight and intervention
- Stream results in real-time

## 📁 Repository Structure
```
LangGraph-Tutorial/
├── agents/           # Agent implementations and examples
├── .gitignore       # Git ignore file
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/varrahan/LangGraph-Tutorial.git
cd LangGraph-Tutorial
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔗 Key Concepts

### State Graph
The core building block of LangGraph applications. Define nodes (functions) and edges (transitions) to create your agent workflow.

### Nodes
Individual functions that process the current state and return updates. Each node represents a step in your agent's reasoning process.

### Edges
Define the flow between nodes. Can be:
- **Normal edges**: Direct transitions
- **Conditional edges**: Routing based on state
- **Entry/Exit points**: START and END nodes

## 🛠️ Useful Resources

- [LangGraph Documentation](https://docs.langchain.com/langgraph)
- [LangChain Academy](https://academy.langchain.com/) - Free structured LangGraph course
- [LangGraph Templates](https://github.com/langchain-ai/langgraph/tree/main/examples) - Pre-built reference applications
- [LangSmith](https://smith.langchain.com/) - Debugging and observability platform

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports or feature requests via issues
- Create pull requests with improvements or new exercises
- Share feedback on the learning materials

## 📝 License

This project is available for educational purposes. Please check the repository for specific license information.

## 🌟 Acknowledgments

This tutorial is built on top of:
- [LangGraph](https://github.com/langchain-ai/langgraph) by LangChain Inc.
- [LangChain](https://github.com/langchain-ai/langchain) ecosystem

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---

Happy learning! 🎓 Start building powerful AI agents with LangGraph!
