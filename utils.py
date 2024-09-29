#!/usr/bin/env python

import json
import yaml


def load_config(filename):
    """Load configuration from a yaml file"""
    with open(filename, 'r') as f:
        # Ler o conteúdo e adicionar espaço após os dois pontos manualmente, caso esteja faltando
        content = f.read().replace(":", ": ")
        print("Conteúdo bruto do arquivo corrigido:\n", content)  # Mostra o conteúdo com os espaços adicionados
        config = yaml.safe_load(content)
        print("Tipo de config:", type(config))  # Verificar o tipo carregado
        print("Config carregado:", config)  # Exibe o conteúdo
        return config


def save_config(config, filename):
    """Save configuration to a yaml file"""
    with open(filename, "w+") as f:
        yaml.safe_dump(config, f, default_flow_style=False)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))
